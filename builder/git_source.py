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

    print(f"[{manifest.name}] Cloning {manifest.repo_url} (branch/tag: {manifest.git_ref}) to {repo_dir}...")
    cmd = [
        "git",
        "clone",
        "--depth",
        "1",
        "--branch",
        manifest.git_ref,
        manifest.repo_url,
        str(repo_dir),
    ]
    subprocess.run(cmd, check=True)

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


def clean_hugo_shortcodes(content: str, repo_dir: Path) -> str:
    """處理 Kubernetes 等 Hugo 網站 markdown 中的 shortcode。"""
    text = content

    # 1. 移除 Hugo 註解 {{/* ... */}}
    text = re.sub(r"\{\{/\*.*?\*/\}\}", "", text, flags=re.DOTALL)

    # 2. 處理 Hugo admonitions: {{< (note|warning|caution|tip|important) ... >}}...{{< /... >}}
    # 以及 {{% note %}}...{{% /note %}}
    admonition_pattern = re.compile(
        r"\{\{[<%]\s*(note|warning|caution|tip|important)(?:\s+title=\"([^\"]*)\"|\s+title='([^']*)'|\s+([^>%]*))?\s*[>%]\}\}"
        r"(.*?)"
        r"\{\{[<%]\s*/\1\s*[>%]\}\}",
        re.DOTALL | re.IGNORECASE,
    )

    def replace_admonition(m: re.Match) -> str:
        kind = m.group(1).lower()
        title = m.group(2) or m.group(3) or ""
        inner = m.group(5)
        return format_admonition(kind, title, inner)

    # 遞迴或多次置換以防巢狀
    for _ in range(3):
        if not admonition_pattern.search(text):
            break
        text = admonition_pattern.sub(replace_admonition, text)

    # 3. 處理 {{< codenew file="..." >}} 或 {{< code file="..." >}}
    code_pattern = re.compile(
        r"\{\{[<%]\s*(?:codenew|code)\s+.*?file=[\"']([^\"']+)[\"'].*?[>%]\}\}",
        re.DOTALL,
    )

    def replace_code_include(m: re.Match) -> str:
        file_path = m.group(1)
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

    # 4. 處理 {{< glossary_tooltip text="..." term_id="..." >}}
    def replace_glossary(m: re.Match) -> str:
        params_str = m.group(1)
        text_match = re.search(r'text=["\']([^"\']*)["\']', params_str)
        term_match = re.search(r'term_id=["\']([^"\']*)["\']', params_str)
        if text_match and text_match.group(1):
            return text_match.group(1)
        if term_match and term_match.group(1):
            return term_match.group(1)
        # Positional param or fallback
        m_pos = re.match(r'["\']([^"\']*)["\']', params_str.strip())
        if m_pos:
            return m_pos.group(1)
        return params_str.strip()

    text = re.sub(r"\{\{[<%]\s*glossary_tooltip\s+(.*?)\s*[>%]\}\}", replace_glossary, text)
    text = re.sub(r"\{\{[<%]\s*glossary_definition\s+(.*?)\s*[>%]\}\}", replace_glossary, text)

    # 5. 處理 {{< feature-state ... >}}
    def replace_feature_state(m: re.Match) -> str:
        params_str = m.group(1)
        state_m = re.search(r'state=["\']?([a-zA-Z0-9_\-]+)["\']?', params_str)
        for_k8s_m = re.search(r'for_k8s_version=["\']?([a-zA-Z0-9_\.\-]+)["\']?', params_str)
        gate_m = re.search(r'feature_gate_name=["\']?([a-zA-Z0-9_\-]+)["\']?', params_str)
        
        parts = []
        if state_m:
            parts.append(f"state: {state_m.group(1)}")
        if for_k8s_m:
            parts.append(f"as of {for_k8s_m.group(1)}")
        if gate_m:
            parts.append(f"gate: {gate_m.group(1)}")
        if parts:
            return f"(Feature {', '.join(parts)})"
        return f"(Feature state: {params_str.strip()})"

    text = re.sub(r"\{\{[<%]\s*feature-state\s+(.*?)\s*[>%]\}\}", replace_feature_state, text)

    # 6. 處理 {{< ref "..." >}} 與 {{< relref "..." >}}
    def replace_ref(m: re.Match) -> str:
        raw_ref = m.group(1).strip()
        ref_match = re.search(r'["\']([^"\']+)["\']', raw_ref)
        if ref_match:
            return ref_match.group(1)
        return raw_ref

    text = re.sub(r"\{\{[<%]\s*(?:relref|ref)\s+(.*?)\s*[>%]\}\}", replace_ref, text)

    # 7. 處理 {{< tabs ... >}} 與 {{% tab name="..." %}}
    text = re.sub(r"\{\{[<%]\s*tabs(?:\s+.*?)?\s*[>%]\}\}", "", text)
    text = re.sub(r"\{\{[<%]\s*/tabs\s*[>%]\}\}", "", text)

    def replace_tab_start(m: re.Match) -> str:
        params_str = m.group(1)
        name_m = re.search(r'name=["\']([^"\']+)["\']', params_str)
        if name_m:
            return f"\n\n**Tab: {name_m.group(1)}**\n\n"
        # Positional param
        pos_m = re.search(r'["\']([^"\']+)["\']', params_str)
        if pos_m:
            return f"\n\n**Tab: {pos_m.group(1)}**\n\n"
        return "\n\n**Tab:**\n\n"

    text = re.sub(r"\{\{[<%]\s*tab\s+(.*?)\s*[>%]\}\}", replace_tab_start, text)
    text = re.sub(r"\{\{[<%]\s*/tab\s*[>%]\}\}", "", text)

    # 8. 處理 {{< table caption="..." >}}
    def replace_table_start(m: re.Match) -> str:
        params_str = m.group(1)
        cap_m = re.search(r'caption=["\']([^"\']+)["\']', params_str)
        if cap_m:
            return f"\n\n**Table: {cap_m.group(1)}**\n\n"
        return "\n\n"

    text = re.sub(r"\{\{[<%]\s*table(?:\s+(.*?))?\s*[>%]\}\}", replace_table_start, text)
    text = re.sub(r"\{\{[<%]\s*/table\s*[>%]\}\}", "\n\n", text)

    # 9. 處理 {{< figure ... >}}
    def replace_figure(m: re.Match) -> str:
        params_str = m.group(1)
        src_m = re.search(r'src=["\']([^"\']+)["\']', params_str)
        alt_m = re.search(r'alt=["\']([^"\']+)["\']', params_str)
        title_m = re.search(r'title=["\']([^"\']+)["\']', params_str)
        src = src_m.group(1) if src_m else ""
        alt = alt_m.group(1) if alt_m else (title_m.group(1) if title_m else "")
        if src:
            return f"\n\n![{alt}]({src})\n\n"
        return ""

    text = re.sub(r"\{\{[<%]\s*figure\s+(.*?)\s*[>%]\}\}", replace_figure, text)

    # 10. 處理 {{< param ... >}} / {{% param ... %}}
    def replace_param(m: re.Match) -> str:
        param_str = m.group(1).strip().strip("'\"")
        return param_str

    text = re.sub(r"\{\{[<%]\s*param\s+(.*?)\s*[>%]\}\}", replace_param, text)

    # 11. 處理 {{< version-check >}} 等無內文 shortcodes
    def replace_generic_shortcode(m: re.Match) -> str:
        tag_content = m.group(1).strip()
        # 如果是結束標籤例如 /note
        if tag_content.startswith("/"):
            return ""
        # 保留可讀摘要
        return f"[{tag_content}]"

    text = re.sub(r"\{\{[<%]\s*(.*?)\s*[>%]\}\}", replace_generic_shortcode, text)

    return text


def normalize(manifest: Manifest) -> None:
    """Normalize 階段：將 repo 內的 Markdown 檔案轉入 corpus。"""
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
    is_k8s = (manifest.collection == "k8s")

    for doc_item in manifest.docs_paths:
        item_path = repo_dir / doc_item
        if not item_path.exists():
            print(f"[{manifest.name}] Warning: path not found in repo: {doc_item}", file=sys.stderr)
            continue

        if item_path.is_file():
            if item_path.suffix.lower() not in {".md", ".markdown"}:
                continue
            files_to_process = [(item_path, Path(doc_item).name)]
        else:
            files_to_process = []
            for p in sorted(item_path.rglob("*")):
                if p.is_file() and p.suffix.lower() in {".md", ".markdown"}:
                    rel_to_item = p.relative_to(item_path).as_posix()
                    files_to_process.append((p, rel_to_item))

        for file_path, rel_out_path_str in files_to_process:
            repo_rel_path = file_path.relative_to(repo_dir).as_posix()
            source_url = f"{base_repo_url}/blob/{manifest.git_ref}/{repo_rel_path}"

            try:
                raw_text = file_path.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                print(f"[{manifest.name}] Error reading {file_path}: {e}", file=sys.stderr)
                continue

            target_rel = Path(rel_out_path_str).with_suffix(".md")
            default_title = target_rel.stem

            title, body = extract_frontmatter(raw_text, default_title=default_title)

            if is_k8s:
                body = clean_hugo_shortcodes(body, repo_dir)

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
