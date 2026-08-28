"""Git 來源建置：clone git repo 並正規化 Markdown 文件成 corpus。

用法：
    python git_source.py fetch manifests/node-driver-registrar-2.13.toml
    python git_source.py normalize manifests/node-driver-registrar-2.13.toml
    python git_source.py all manifests/node-driver-registrar-2.13.toml

fetch 階段會 clone 指定 tag/branch 到 raw/<collection>/<version>/repo，並記錄 commit date。
normalize 階段可離線重跑，將 docs_paths 下的 Markdown 檔案轉換並附加統一 frontmatter。
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

from common import REPO_ROOT, Manifest, load_manifest
from normalize import to_markdown as html_to_markdown

FRONTMATTER_PATTERN = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
HEADING1_PATTERN = re.compile(r"^#\s+(.+)$", re.MULTILINE)

# 副檔名與代碼語言對映
EXT_TO_LANG: dict[str, str] = {
    ".yaml": "yaml",
    ".yml": "yaml",
    ".json": "json",
    ".sh": "bash",
    ".bash": "bash",
    ".go": "go",
    ".py": "python",
    ".c": "c",
    ".cpp": "cpp",
    ".h": "c",
    ".md": "markdown",
    ".txt": "",
    ".xml": "xml",
    ".toml": "toml",
    ".ini": "ini",
    ".dockerfile": "dockerfile",
}


def run_cmd(cmd: list[str], cwd: Path | None = None) -> str:
    """執行指令並回傳 stdout 字串，失敗時拋出 CalledProcessError。"""
    res = subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
        check=True,
    )
    return res.stdout.strip()


def get_git_commit_date(repo_dir: Path) -> str:
    """取得 repo 最新 commit 的 ISO 8601 時間字串。"""
    try:
        return run_cmd(["git", "-C", str(repo_dir), "log", "-1", "--format=%cI"])
    except (subprocess.CalledProcessError, FileNotFoundError):
        return datetime.now(timezone.utc).isoformat(timespec="seconds")


def get_git_commit_hash(repo_dir: Path) -> str:
    """取得 repo 最新 commit 的 hash。"""
    try:
        return run_cmd(["git", "-C", str(repo_dir), "log", "-1", "--format=%H"])
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def fetch(manifest: Manifest) -> None:
    """Fetch 階段：將 repo clone 到 raw_dir/repo。"""
    if manifest.source_type != "git":
        print(f"[{manifest.name}] source_type is '{manifest.source_type}', not 'git'. Skipping fetch.", file=sys.stderr)
        return

    raw_dir = manifest.raw_dir
    raw_dir.mkdir(parents=True, exist_ok=True)
    repo_dir = raw_dir / "repo"

    if repo_dir.exists():
        print(f"[{manifest.name}] Existing repo directory found at {repo_dir}, removing before clone...")
        shutil.rmtree(repo_dir)

    print(f"[{manifest.name}] Cloning {manifest.repo_url} (branch/tag/commit: {manifest.git_ref}) to {repo_dir}...")
    if re.fullmatch(r"[0-9a-fA-F]{40}", manifest.git_ref):
        # `git clone --branch` does not accept a raw commit ID. Fetch the exact
        # reachable commit so documentation snapshots can still be immutable
        # when an upstream documentation repository does not publish tags.
        subprocess.run(["git", "init", str(repo_dir)], check=True)
        subprocess.run(["git", "-C", str(repo_dir), "remote", "add", "origin", manifest.repo_url], check=True)
        if manifest.sparse_paths:
            subprocess.run(["git", "-C", str(repo_dir), "sparse-checkout", "init", "--no-cone"], check=True)
            subprocess.run(
                ["git", "-C", str(repo_dir), "sparse-checkout", "set", "--no-cone", *manifest.sparse_paths],
                check=True,
            )
        subprocess.run(
            ["git", "-C", str(repo_dir), "fetch", "--depth", "1", "origin", manifest.git_ref],
            check=True,
        )
        subprocess.run(["git", "-C", str(repo_dir), "checkout", "--detach", "FETCH_HEAD"], check=True)
    else:
        cmd = ["git", "clone", "--depth", "1", "--branch", manifest.git_ref]
        if manifest.sparse_paths:
            cmd.extend(["--filter=blob:none", "--sparse"])
        cmd.extend([manifest.repo_url, str(repo_dir)])
        subprocess.run(cmd, check=True)

        if manifest.sparse_paths:
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(repo_dir),
                    "sparse-checkout",
                    "set",
                    "--no-cone",
                    *manifest.sparse_paths,
                ],
                check=True,
            )

    commit_date = get_git_commit_date(repo_dir)
    commit_hash = get_git_commit_hash(repo_dir)

    meta_file = raw_dir / "git_meta.json"
    meta_data = {
        "repo_url": manifest.repo_url,
        "git_ref": manifest.git_ref,
        "commit_date": commit_date,
        "commit_hash": commit_hash,
        "fetched_at": commit_date,
    }
    meta_file.write_text(json.dumps(meta_data, indent=2, ensure_ascii=False) + "\n")
    print(f"[{manifest.name}] clone complete. Commit date: {commit_date} ({commit_hash[:8]})")


def extract_frontmatter(content: str, default_title: str) -> tuple[str, str]:
    """解析原始 markdown 的 frontmatter 並提取 title，回傳 (title, body)。"""
    match = FRONTMATTER_PATTERN.match(content)
    title = ""
    body = content

    if match:
        raw_yaml = match.group(1)
        body = content[match.end():]
        try:
            parsed = yaml.safe_load(raw_yaml)
            if isinstance(parsed, dict) and "title" in parsed:
                t = parsed["title"]
                if t is not None:
                    title = str(t).strip()
        except Exception:
            pass

        if not title:
            # Fallback regex search in raw yaml for title: ...
            t_match = re.search(r"^title:\s*(?:\"([^\"]*)\"|'([^']*)'|(.*))$", raw_yaml, re.MULTILINE)
            if t_match:
                title = (t_match.group(1) or t_match.group(2) or t_match.group(3) or "").strip()

    if not title:
        # Fallback to first # heading in body
        h_match = HEADING1_PATTERN.search(body)
        if h_match:
            title = h_match.group(1).strip()

    if not title:
        title = default_title

    return title, body


def resolve_example_file(repo_dir: Path, file_path_str: str) -> Path | None:
    """尋找 Hugo shortcode 引用的範例檔案路徑。"""
    rel = file_path_str.strip("/\\")
    candidates = [
        repo_dir / "content/en/examples" / rel,
        repo_dir / "content/examples" / rel,
        repo_dir / "content/en" / rel,
        repo_dir / "content" / rel,
        repo_dir / "examples" / rel,
        repo_dir / rel,
    ]
    for cand in candidates:
        if cand.is_file():
            return cand
    return None


def format_admonition(kind: str, title: str, inner_text: str) -> str:
    """將 admonition (note, warning, caution, tip, important) 轉為 blockquote 格式。"""
    kind_capital = kind.capitalize()
    header = f"**{kind_capital}:**" if not title else f"**{kind_capital} ({title}):**"
    
    # 縮排 inner_text 的每一行
    lines = inner_text.strip().splitlines()
    quoted_lines = [f"> {line}" if line.strip() else ">" for line in lines]
    quoted_body = "\n".join(quoted_lines)
    
    if quoted_body:
        return f"\n\n> {header}\n>\n{quoted_body}\n\n"
    return f"\n\n> {header}\n\n"


HEADINGS: dict[str, str] = {
    "whatsnext": "What's next",
    "prerequisites": "Before you begin",
    "objectives": "Objectives",
    "cleanup": "Cleaning up",
    "synopsis": "Synopsis",
    "seealso": "See also",
    "options": "Options",
    "parentoptions": "Options inherited from parent commands",
    "envvars": "Environment variables",
    "examples": "Examples",
}


def resolve_include_file(repo_dir: Path, file_path_str: str) -> Path | None:
    """尋找 Hugo shortcode 引用的 include 檔案路徑。"""
    rel = file_path_str.strip("/\\")
    candidates = [
        repo_dir / "content/en/includes" / rel,
        repo_dir / "content/includes" / rel,
        repo_dir / "content/en/docs" / rel,
        repo_dir / "content/en" / rel,
        repo_dir / rel,
    ]
    for cand in candidates:
        if cand.is_file():
            return cand
    return None


def clean_hugo_shortcodes(content: str, repo_dir: Path, depth: int = 0) -> str:
    """處理 Kubernetes 等 Hugo 網站 markdown 中的 shortcode。"""
    if depth > 5:
        return content
    text = content

    # 1. 移除 Hugo 註解 {{/* ... */}} 與 {{< comment >}}...{{< /comment >}} 以及 {{</* ... */>}}
    text = re.sub(r"\{\{[<%]?/\*.*?\*/[>%]?\}\}", "", text, flags=re.DOTALL)
    text = re.sub(r"\{\{[<%]\s*comment\s*[>%]\}\}.*?\{\{[<%]\s*/comment\s*[>%]\}\}", "", text, flags=re.DOTALL)

    # 2. 處理 {{< include "..." >}}
    def replace_include(m: re.Match) -> str:
        inc_path = m.group(1).strip("\"'")
        resolved = resolve_include_file(repo_dir, inc_path)
        if resolved:
            try:
                inc_text = resolved.read_text(encoding="utf-8", errors="replace")
                inc_text = re.sub(r"^---\r?\n.*?\r?\n---\r?\n?", "", inc_text, flags=re.DOTALL)
                return clean_hugo_shortcodes(inc_text, repo_dir, depth + 1)
            except Exception:
                return f"\n[Include {inc_path}]\n"
        return f"\n[Include {inc_path}]\n"

    text = re.sub(r"\{\{[<%]\s*include\s+[\"']?([^\"'\s>]+)[\"']?\s*[>%]\}\}", replace_include, text, flags=re.DOTALL)

    # 3. 處理 {{% heading "whatsnext" %}} 或 ## {{% heading "whatsnext" %}}
    def replace_heading(m: re.Match) -> str:
        hashes = m.group(1) or "##"
        h_key = m.group(2).strip("\"'").lower()
        title = HEADINGS.get(h_key, h_key.replace("_", " ").title())
        return f"\n\n{hashes} {title}\n\n"

    text = re.sub(
        r"(?:^|\n)[ \t]*(#{1,6})?[ \t]*\{\{[<%]\s*heading\s+[\"']?([\w\-]+)[\"']?\s*[>%]\}\}",
        replace_heading,
        text,
        flags=re.DOTALL,
    )
    # 清理多餘的空白標題行 (例如單獨的 ##)
    text = re.sub(r"(?m)^[ \t]*#{1,6}[ \t]*$", "", text)

    # 4. 處理 Hugo admonitions: {{< (note|warning|caution|tip|important|alert) ... >}}...{{< /... >}}
    admonition_pattern = re.compile(
        r"\{\{[<%]\s*(note|warning|caution|tip|important|alert)(?:\s+title=[\"']([^\"']*)[\"']|\s+title=([^\s>%]+)|\s+([^>%]*?))?\s*[>%]\}\}"
        r"(.*?)"
        r"\{\{[<%]\s*/\1\s*[>%]\}\}",
        re.DOTALL | re.IGNORECASE,
    )

    def replace_admonition(m: re.Match) -> str:
        kind = m.group(1).lower()
        title = m.group(2) or m.group(3) or ""
        inner = m.group(5)
        return format_admonition(kind, title, inner)

    for _ in range(5):
        if not admonition_pattern.search(text):
            break
        text = admonition_pattern.sub(replace_admonition, text)

    # 5. 處理 {{< code_sample file="..." >}}、{{< codenew file="..." >}}、{{< code file="..." >}}、{{< example file="..." >}}
    code_pattern = re.compile(
        r"\{\{[<%]\s*(?:code_sample|codenew|code|example)\s+(?:.*?file=[\"']([^\"']+)[\"']|([^\s>%]+)).*?[>%]\}\}",
        re.DOTALL,
    )

    def replace_code_include(m: re.Match) -> str:
        file_path = m.group(1) or m.group(2)
        if not file_path:
            return ""
        resolved = resolve_example_file(repo_dir, file_path)
        if resolved:
            try:
                code_content = resolved.read_text(encoding="utf-8", errors="replace")
                suffix = resolved.suffix.lower()
                lang = EXT_TO_LANG.get(suffix, suffix.lstrip("."))
                return f"\n```{lang}\n{code_content.rstrip()}\n```\n"
            except Exception as e:
                return f"\n[範例檔案 {file_path} 讀取失敗: {e}]\n"
        return f"\n[範例檔案 {file_path} 未能內嵌]\n"

    text = code_pattern.sub(replace_code_include, text)

    # 6. 處理 {{< highlight yaml ... >}}...{{< /highlight >}}
    def replace_highlight(m: re.Match) -> str:
        lang = m.group(1).strip()
        inner = m.group(2)
        return f"\n```{lang}\n{inner.strip()}\n```\n"

    text = re.sub(
        r"\{\{[<%]\s*highlight\s+([a-zA-Z0-9_\-]+)(?:.*?)?[>%]\}\}(.*?)\{\{[<%]\s*/highlight\s*[>%]\}\}",
        replace_highlight,
        text,
        flags=re.DOTALL,
    )

    # 7. 處理 {{< mermaid >}}...{{< /mermaid >}}
    def replace_mermaid(m: re.Match) -> str:
        inner = m.group(1).strip()
        return f"\n\n```mermaid\n{inner}\n```\n\n"

    text = re.sub(r"\{\{[<%]\s*mermaid\s*[>%]\}\}(.*?)\{\{[<%]\s*/mermaid\s*[>%]\}\}", replace_mermaid, text, flags=re.DOTALL)

    # 8. 處理 {{< details summary="..." >}}...{{< /details >}}
    def replace_details(m: re.Match) -> str:
        summary_m = re.search(r'summary=["\']([^"\']*)["\']', m.group(1) or "", re.DOTALL)
        summary = summary_m.group(1) if summary_m else (m.group(1).strip() if m.group(1) else "Details")
        inner = m.group(2).strip()
        return f"\n\n<details>\n<summary>{summary}</summary>\n\n{inner}\n\n</details>\n\n"

    text = re.sub(
        r"\{\{[<%]\s*details(?:\s+([^>%]*?))?\s*[>%]\}\}(.*?)\{\{[<%]\s*/details\s*[>%]\}\}",
        replace_details,
        text,
        flags=re.DOTALL,
    )

    # 9. 處理 {{< skew ... >}}
    def replace_skew(m: re.Match) -> str:
        args = m.group(1).strip().split()
        if not args:
            return "1.31"
        arg0 = args[0].strip("\"'")
        if arg0 in ("currentVersion", "latestVersion"):
            return "1.31"
        elif arg0 == "prevMinorVersion":
            return "1.30"
        elif arg0 == "oldestMinorVersion":
            return "1.29"
        elif arg0 == "nextMinorVersion":
            return "1.32"
        elif arg0 == "currentPatchVersion":
            return "1.31.6"
        elif "AddMinor" in arg0 and len(args) >= 2:
            try:
                offset = int(args[1])
                sep = args[2].strip("\"'") if len(args) >= 3 else "."
                return f"1{sep}{31 + offset}"
            except ValueError:
                return "1.31"
        return "1.31"

    text = re.sub(r"\{\{[<%]\s*skew\s+(.*?)\s*[>%]\}\}", replace_skew, text, flags=re.DOTALL)

    # 10. 處理 {{< glossary_tooltip text="..." term_id="..." >}}
    def replace_glossary_tooltip(m: re.Match) -> str:
        params_str = m.group(1)
        text_match = re.search(r'text=["\']([^"\']*)["\']', params_str, re.DOTALL)
        term_match = re.search(r'term_id=["\']([^"\']*)["\']', params_str, re.DOTALL)
        if text_match and text_match.group(1):
            return text_match.group(1)
        if term_match and term_match.group(1):
            return term_match.group(1)
        m_pos = re.search(r'["\']([^"\']*)["\']', params_str, re.DOTALL)
        if m_pos:
            return m_pos.group(1)
        return " ".join(params_str.split())

    text = re.sub(r"\{\{[<%]\s*glossary_tooltip\s+(.*?)\s*[>%]\}\}", replace_glossary_tooltip, text, flags=re.DOTALL)

    # 11. 處理 {{< glossary_definition ... >}}
    def replace_glossary_definition(m: re.Match) -> str:
        params_str = m.group(1)
        term_m = re.search(r'term_id=["\']([^"\']+)["\']', params_str, re.DOTALL)
        prepend_m = re.search(r'prepend=["\']([^"\']+)["\']', params_str, re.DOTALL)
        prepend = prepend_m.group(1).strip() if prepend_m else ""
        length_m = re.search(r'length=["\']([^"\']+)["\']', params_str, re.DOTALL)
        length = length_m.group(1) if length_m else "all"

        if term_m:
            term_id = term_m.group(1)
            term_candidates = [
                repo_dir / "content/en/docs/reference/glossary" / f"{term_id}.md",
                repo_dir / "content/docs/reference/glossary" / f"{term_id}.md",
                repo_dir / "content/en/reference/glossary" / f"{term_id}.md",
            ]
            for cand in term_candidates:
                if cand.is_file():
                    try:
                        raw = cand.read_text(encoding="utf-8", errors="replace")
                        fm_m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", raw, re.DOTALL)
                        body = fm_m.group(2) if fm_m else raw
                        if length == "short":
                            parts = re.split(r"<!--more-->", body, flags=re.IGNORECASE)
                            body = parts[0].strip()
                        else:
                            body = re.sub(r"<!--more-->", "", body, flags=re.IGNORECASE)
                        # Clean inner glossary_tooltip
                        body = re.sub(
                            r'\{\{[<%]\s*glossary_tooltip\s+(?:.*?text=["\']([^"\']+)["\']|.*?term_id=["\']([^"\']+)["\']).*?[>%]\}\}',
                            lambda tm: tm.group(1) or tm.group(2),
                            body,
                            flags=re.DOTALL,
                        )
                        body = body.strip()
                        if prepend and body:
                            first_char = body[0].lower()
                            rest = body[1:]
                            body = f"{prepend} {first_char}{rest}"
                        return f"\n\n{body}\n\n"
                    except Exception:
                        break
            if prepend:
                return f"{prepend} {term_id}"
            return term_id

        m_pos = re.search(r'["\']([^"\']*)["\']', params_str, re.DOTALL)
        if m_pos:
            return m_pos.group(1)
        return " ".join(params_str.split())

    text = re.sub(r"\{\{[<%]\s*glossary_definition\s+(.*?)\s*[>%]\}\}", replace_glossary_definition, text, flags=re.DOTALL)

    # 12. 處理 {{< feature-state ... >}}
    def replace_feature_state(m: re.Match) -> str:
        params_str = m.group(1)
        state_m = re.search(r'state=["\']?([a-zA-Z0-9_\-]+)["\']?', params_str, re.DOTALL)
        for_k8s_m = re.search(r'for_k8s_version=["\']?([a-zA-Z0-9_\.\-]+)["\']?', params_str, re.DOTALL)
        gate_m = re.search(r'feature_gate_name=["\']?([a-zA-Z0-9_\-]+)["\']?', params_str, re.DOTALL)
        
        parts = []
        if state_m:
            parts.append(f"state: {state_m.group(1)}")
        if for_k8s_m:
            parts.append(f"as of {for_k8s_m.group(1)}")
        if gate_m:
            parts.append(f"gate: {gate_m.group(1)}")
        if parts:
            return f"(Feature {', '.join(parts)})"
        return f"(Feature state: {' '.join(params_str.split())})"

    text = re.sub(r"\{\{[<%]\s*feature-state\s+(.*?)\s*[>%]\}\}", replace_feature_state, text, flags=re.DOTALL)

    # 13. 處理 {{< ref "..." >}} 與 {{< relref "..." >}}
    def replace_ref(m: re.Match) -> str:
        raw_ref = m.group(1).strip()
        ref_match = re.search(r'["\']([^"\']+)["\']', raw_ref, re.DOTALL)
        if ref_match:
            return ref_match.group(1)
        return raw_ref

    text = re.sub(r"\{\{[<%]\s*(?:relref|ref)\s+(.*?)\s*[>%]\}\}", replace_ref, text, flags=re.DOTALL)

    # 14. 處理 {{< tabs ... >}} 與 {{% tab name="..." %}}
    text = re.sub(r"\{\{[<%]\s*tabs(?:\s+.*?)?\s*[>%]\}\}", "", text, flags=re.DOTALL)
    text = re.sub(r"\{\{[<%]\s*/tabs\s*[>%]\}\}", "", text, flags=re.DOTALL)

    def replace_tab_start(m: re.Match) -> str:
        params_str = m.group(1)
        name_m = re.search(r'name=["\']([^"\']+)["\']', params_str, re.DOTALL)
        if name_m:
            return f"\n\n**Tab: {name_m.group(1)}**\n\n"
        pos_m = re.search(r'["\']([^"\']+)["\']', params_str, re.DOTALL)
        if pos_m:
            return f"\n\n**Tab: {pos_m.group(1)}**\n\n"
        return "\n\n**Tab:**\n\n"

    text = re.sub(r"\{\{[<%]\s*tab\s+(.*?)\s*[>%]\}\}", replace_tab_start, text, flags=re.DOTALL)
    text = re.sub(r"\{\{[<%]\s*/tab\s*[>%]\}\}", "", text, flags=re.DOTALL)

    # 15. 處理 {{< table caption="..." >}}
    def replace_table_start(m: re.Match) -> str:
        params_str = m.group(1) or ""
        cap_m = re.search(r'caption\s*=\s*["\']([^"\']+)["\']', params_str, re.DOTALL)
        if cap_m:
            return f"\n\n**Table: {cap_m.group(1)}**\n\n"
        return "\n\n"

    text = re.sub(r"\{\{[<%]\s*table(?:\s+(.*?))?\s*[>%]\}\}", replace_table_start, text, flags=re.DOTALL)
    text = re.sub(r"\{\{[<%]\s*/table\s*[>%]\}\}", "\n\n", text, flags=re.DOTALL)

    # 16. 處理 {{< figure ... >}}
    def replace_figure(m: re.Match) -> str:
        params_str = m.group(1)
        src_m = re.search(r'src=["\']([^"\']+)["\']', params_str, re.DOTALL)
        alt_m = re.search(r'alt=["\']([^"\']*)["\']', params_str, re.DOTALL)
        title_m = re.search(r'title=["\']([^"\']*)["\']', params_str, re.DOTALL)
        caption_m = re.search(r'caption=["\']([^"\']*)["\']', params_str, re.DOTALL)
        
        src = src_m.group(1).strip() if src_m else ""
        alt = ""
        if alt_m and alt_m.group(1).strip():
            alt = alt_m.group(1).strip()
        elif title_m and title_m.group(1).strip():
            alt = title_m.group(1).strip()
        elif caption_m and caption_m.group(1).strip():
            alt = caption_m.group(1).strip()
            
        alt = " ".join(alt.split())
        if src:
            return f"\n\n![{alt}]({src})\n\n"
        return ""

    text = re.sub(r"\{\{[<%]\s*figure\s+(.*?)\s*[>%]\}\}", replace_figure, text, flags=re.DOTALL)

    # 17. 處理 {{< param ... >}} / {{% param ... %}}
    def replace_param(m: re.Match) -> str:
        param_str = m.group(1).strip().strip("'\"")
        return param_str

    text = re.sub(r"\{\{[<%]\s*param\s+(.*?)\s*[>%]\}\}", replace_param, text, flags=re.DOTALL)

    # 18. 處理 {{< link text="..." url="..." >}}
    def replace_link(m: re.Match) -> str:
        p_str = m.group(1)
        text_m = re.search(r'text=["\']([^"\']+)["\']', p_str, re.DOTALL)
        url_m = re.search(r'url=["\']([^"\']+)["\']', p_str, re.DOTALL)
        link_text = text_m.group(1) if text_m else "link"
        url = url_m.group(1) if url_m else ""
        if url:
            return f"[{link_text}]({url})"
        return link_text

    text = re.sub(r"\{\{[<%]\s*link\s+(.*?)\s*[>%]\}\}", replace_link, text, flags=re.DOTALL)

    # 19. 處理 {{< api-reference ... >}} 與 {{< page-api-reference ... >}}
    def replace_api_ref(m: re.Match) -> str:
        p_str = m.group(1)
        page_m = re.search(r'page=["\']([^"\']+)["\']', p_str, re.DOTALL)
        kind_m = re.search(r'kind=["\']([^"\']+)["\']', p_str, re.DOTALL)
        text_m = re.search(r'text=["\']([^"\']+)["\']', p_str, re.DOTALL)
        anchor_m = re.search(r'anchor=["\']([^"\']+)["\']', p_str, re.DOTALL)
        page = page_m.group(1) if page_m else (kind_m.group(1) if kind_m else "")
        anchor = f"#{anchor_m.group(1)}" if anchor_m else ""
        label = text_m.group(1) if text_m else (anchor_m.group(1) if anchor_m else page.split("/")[-1])
        return f"[{label}](/docs/reference/kubernetes-api/{page}{anchor})"

    text = re.sub(r"\{\{[<%]\s*(?:api-reference|page-api-reference)\s+(.*?)\s*[>%]\}\}", replace_api_ref, text, flags=re.DOTALL)

    # 20. 常用固定短標籤 shortcodes
    text = re.sub(
        r"\{\{[<%]\s*thirdparty-content.*?[>%]\}\}",
        "> **Note:** This section links to third-party projects that provide functionality required by Kubernetes. The Kubernetes authors aren't responsible for these projects.\n",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\{\{[<%]\s*dockershim-removal.*?[>%]\}\}",
        "> **Note:** Dockershim was removed from Kubernetes in v1.24.\n",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\{\{[<%]\s*legacy-repos-deprecation.*?[>%]\}\}",
        "> **Warning:** The legacy package repositories (apt.kubernetes.io and yum.kubernetes.io) are deprecated and frozen.\n",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(
        r"\{\{[<%]\s*feature-gate-(?:table|list|description).*?[>%]\}\}",
        "(See Kubernetes Feature Gates documentation for feature stages and versions)",
        text,
        flags=re.DOTALL,
    )
    text = re.sub(r"\{\{[<%]\s*version-check\s*[>%]\}\}", "", text, flags=re.DOTALL)
    text = re.sub(r"\{\{[<%]\s*latest-version\s*[>%]\}\}", "v1.31", text, flags=re.DOTALL)
    text = re.sub(r"\{\{[<%]\s*latest-semver\s*[>%]\}\}", "1.31.6", text, flags=re.DOTALL)
    text = re.sub(r"\{\{[<%]\s*release-branch\s*[>%]\}\}", "release-1.31", text, flags=re.DOTALL)
    text = re.sub(r"\{\{[<%]\s*latest-release-notes\s*[>%]\}\}", "", text, flags=re.DOTALL)
    text = re.sub(r"\{\{[<%]\s*doc-versions-list(?:\s+.*?)?\s*[>%]\}\}", "", text, flags=re.DOTALL)
    text = re.sub(r"\{\{[<%]\s*kat-button(?:\s+.*?)?\s*[>%]\}\}", "", text, flags=re.DOTALL)
    text = re.sub(r"\{\{[<%]\s*cve-feed(?:\s+.*?)?\s*[>%]\}\}", "", text, flags=re.DOTALL)
    text = re.sub(r"\{\{[<%]\s*cncf-landscape(?:\s+.*?)?\s*[>%]\}\}", "", text, flags=re.DOTALL)

    # 21. 通用未列出 shortcode 的保留可讀字串處理
    def replace_generic_shortcode(m: re.Match) -> str:
        tag_content = m.group(1).strip()
        if tag_content.startswith("/"):
            return ""
        cleaned = " ".join(tag_content.split())
        return f"[{cleaned}]"

    text = re.sub(r"\{\{[<%]\s*(.*?)\s*[>%]\}\}", replace_generic_shortcode, text, flags=re.DOTALL)

    return text


def clean_gitlab_shortcodes(content: str) -> str:
    """Convert GitLab Docs Hugo shortcodes into readable plain Markdown."""
    # Some upstream API examples contain credential-shaped values. Keep the
    # examples useful without copying token-like values into the corpus.
    text = re.sub(
        r'("personal_access_token"\s*:\s*")[^"<]+(")',
        r"\1<your_bitbucket_server_personal_access_token>\2",
        content,
    )

    alert_pattern = re.compile(
        r'\{\{<\s*alert\s+type=["\']([^"\']+)["\']\s*>\}\}'
        r"(.*?)"
        r"\{\{<\s*/alert\s*>\}\}",
        re.DOTALL | re.IGNORECASE,
    )
    text = alert_pattern.sub(
        lambda match: format_admonition(match.group(1), "", match.group(2)),
        text,
    )

    # These containers carry useful prose; only their presentation is site-specific.
    text = re.sub(r"\{\{<\s*details\s*>\}\}", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\{\{<\s*/details\s*>\}\}", "", text, flags=re.IGNORECASE)
    text = re.sub(
        r"\{\{<\s*history\s*>\}\}",
        "\n\n**History:**\n\n",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"\{\{<\s*/history\s*>\}\}", "", text, flags=re.IGNORECASE)

    text = re.sub(r"\{\{<\s*tabs\s*>\}\}", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\{\{<\s*/tabs\s*>\}\}", "", text, flags=re.IGNORECASE)
    text = re.sub(
        r'\{\{<\s*tab\s+title=["\']([^"\']+)["\']\s*>\}\}',
        lambda match: f"\n\n**Tab: {match.group(1)}**\n\n",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"\{\{<\s*/tab\s*>\}\}", "", text, flags=re.IGNORECASE)

    text = re.sub(
        r'\{\{<\s*icon\s+name=["\']([^"\']+)["\']\s*>\}\}',
        lambda match: f"[icon: {match.group(1)}]",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\{\{<\s*feature-flags\s*>\}\}",
        "\n\n**Feature flags:**\n\n",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"\{\{<\s*/feature-flags\s*>\}\}", "", text, flags=re.IGNORECASE)

    # Preserve the arguments of any future shortcode instead of leaving template syntax.
    text = re.sub(
        r"\{\{<\s*(/)?([\w-]+)(.*?)>\}\}",
        lambda match: "" if match.group(1) else f"[{match.group(2)}{match.group(3)}]",
        text,
        flags=re.DOTALL,
    )
    return text


def normalize(manifest: Manifest) -> None:
    """Normalize 階段：將 repo 內的 Markdown/HTML 文件轉入 corpus。"""
    repo_dir = manifest.raw_dir / "repo"
    if not repo_dir.exists():
        print(f"[{manifest.name}] raw repo not found at {repo_dir}. Please run fetch first.", file=sys.stderr)
        sys.exit(1)

    # 讀取 commit date / fetched_at
    meta_file = manifest.raw_dir / "git_meta.json"
    fetched_at = ""
    if meta_file.exists():
        try:
            meta_data = json.loads(meta_file.read_text())
            fetched_at = meta_data.get("fetched_at", "")
        except Exception:
            pass

    if not fetched_at:
        fetched_at = get_git_commit_date(repo_dir)

    corpus_dir = manifest.corpus_dir
    written = 0

    base_repo_url = manifest.repo_url.rstrip("/")
    is_k8s = manifest.collection == "k8s"
    is_gitlab = manifest.collection == "gitlab"

    for doc_item in manifest.docs_paths:
        item_path = repo_dir / doc_item
        if not item_path.exists():
            print(f"[{manifest.name}] Warning: path not found in repo: {doc_item}", file=sys.stderr)
            continue

        supported_suffixes = {".md", ".markdown"}
        if manifest.content_selector:
            supported_suffixes.add(".html")

        if item_path.is_file():
            if item_path.suffix.lower() not in supported_suffixes:
                continue
            files_to_process = [(item_path, Path(doc_item).name)]
        else:
            files_to_process = []
            for p in sorted(item_path.rglob("*")):
                if p.is_file() and p.suffix.lower() in supported_suffixes:
                    rel_to_item = p.relative_to(item_path).as_posix()
                    files_to_process.append((p, rel_to_item))

        for file_path, rel_out_path_str in files_to_process:
            repo_rel_path = file_path.relative_to(repo_dir).as_posix()
            if manifest.source_url_template:
                source_url = manifest.source_url_template.format(
                    repo_url=base_repo_url,
                    git_ref=manifest.git_ref,
                    path=repo_rel_path,
                    doc_path=rel_out_path_str,
                )
            else:
                source_url = f"{base_repo_url}/blob/{manifest.git_ref}/{repo_rel_path}"

            try:
                raw_text = file_path.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                print(f"[{manifest.name}] Error reading {file_path}: {e}", file=sys.stderr)
                continue

            target_rel = Path(rel_out_path_str).with_suffix(".md")
            default_title = target_rel.stem

            if file_path.suffix.lower() == ".html":
                page_url = f"{manifest.base_url.rstrip('/')}/{rel_out_path_str}"
                html_result = html_to_markdown(raw_text, page_url, manifest)
                if html_result is None:
                    print(f"[{manifest.name}] Skipping HTML with no matching content: {repo_rel_path}", file=sys.stderr)
                    continue
                title, body = html_result
                body = re.sub(r"[ \t]+$", "", body, flags=re.MULTILINE)
            else:
                title, body = extract_frontmatter(raw_text, default_title=default_title)

            if is_k8s:
                body = clean_hugo_shortcodes(body, repo_dir)
            elif is_gitlab:
                body = clean_gitlab_shortcodes(body)
                body = re.sub(r"[ \t]+$", "", body, flags=re.MULTILINE)

            body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"

            out_path = corpus_dir / target_rel
            out_path.parent.mkdir(parents=True, exist_ok=True)

            frontmatter = "\n".join([
                "---",
                f"collection: {manifest.collection}",
                f'version: "{manifest.version}"',
                f"title: {json.dumps(title, ensure_ascii=False)}",
                f"source_url: {source_url}",
                f"fetched_at: {fetched_at}",
                "---",
                "",
            ])

            out_path.write_text(frontmatter + body, encoding="utf-8")
            written += 1

    print(f"[{manifest.name}] corpus written: {written} pages")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build corpus from git repositories.")
    parser.add_argument("command", choices=["fetch", "normalize", "all"], help="Action to perform")
    parser.add_argument("manifest", help="Path to manifest TOML file")
    args = parser.parse_args()

    manifest = load_manifest(args.manifest)

    if args.command in {"fetch", "all"}:
        fetch(manifest)
    if args.command in {"normalize", "all"}:
        normalize(manifest)


if __name__ == "__main__":
    main()
