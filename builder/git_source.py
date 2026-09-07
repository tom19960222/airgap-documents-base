"""Git 來源建置：clone git repo 並正規化 Markdown/RST 文件成 corpus。

用法：
    python git_source.py fetch manifests/node-driver-registrar-2.13.toml
    python git_source.py normalize manifests/node-driver-registrar-2.13.toml
    python git_source.py all manifests/node-driver-registrar-2.13.toml

fetch 階段會 clone 指定 tag/branch 到 raw/<collection>/<version>/repo，並記錄 commit date。
normalize 階段可離線重跑，將 docs_paths 下的 Markdown/RST 檔案轉換並附加統一 frontmatter。
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
from urllib.parse import urlsplit, urlunsplit

from common import REPO_ROOT, Manifest, load_manifest

FRONTMATTER_PATTERN = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
HEADING1_PATTERN = re.compile(r"^#\s+(.+)$", re.MULTILINE)

RST_SECTION_LEVELS = {
    "=": 1,
    "-": 2,
    "^": 3,
    "~": 4,
    '"': 5,
    "'": 6,
    "*": 3,
    "`": 3,
    "+": 4,
    "_": 5,
    ".": 6,
    "|": 6,
    "#": 6,
}
RST_DIRECTIVE_PATTERN = re.compile(
    r"^(?P<indent>[ ]*)\.\.\s+(?P<name>[A-Za-z0-9_.-]+)::(?:[ \t]*(?P<argument>.*))?$"
)
RST_TARGET_PATTERN = re.compile(
    r"^(?P<indent>[ ]*)\.\.\s+_(?P<label>`[^`]+`|[^:]+):(?:[ \t]*(?P<target>.*))?$",
    re.MULTILINE,
)
RST_LINK_ROLES = {"ref", "doc", "download", "numref"}
ASSET_SUFFIXES = {
    ".7z",
    ".bz2",
    ".eot",
    ".gif",
    ".gz",
    ".ico",
    ".jpeg",
    ".jpg",
    ".otf",
    ".pdf",
    ".png",
    ".svg",
    ".tar",
    ".tgz",
    ".ttf",
    ".webp",
    ".woff",
    ".woff2",
    ".xz",
    ".zip",
}
RST_ADMONITIONS = {
    "attention",
    "caution",
    "danger",
    "error",
    "hint",
    "important",
    "note",
    "seealso",
    "tip",
    "warning",
}
RST_CODE_DIRECTIVES = {"code", "code-block", "sourcecode", "prompt"}


def _indent_width(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _is_section_underline(line: str) -> bool:
    stripped = line.strip()
    return (
        len(stripped) >= 3
        and len(set(stripped)) == 1
        and stripped[0] in RST_SECTION_LEVELS
    )


def _section_level(line: str) -> int:
    return RST_SECTION_LEVELS[line.strip()[0]]


def _deindent(lines: list[str], minimum: int | None = None) -> list[str]:
    nonblank = [_indent_width(line) for line in lines if line.strip()]
    if not nonblank:
        return ["" if not line.strip() else line for line in lines]
    amount = min(nonblank) if minimum is None else minimum
    result = []
    for line in lines:
        if not line.strip():
            result.append("")
        else:
            result.append(line[min(amount, _indent_width(line)):])
    return result


def _inline_rst_to_markdown(line: str, *, preserve_rst_links: bool = False) -> str:
    """Convert safe inline RST constructs without interpreting unknown roles."""

    # Protect literal spans before interpreting roles or explicit links.  RST
    # teaching text such as ``:ref:`example``` is not a real cross-reference.
    literals: list[str] = []

    def protect_literal(match: re.Match[str]) -> str:
        literals.append(match.group(1))
        return f"\x00RST_INLINE_LITERAL_{len(literals) - 1}\x01"

    line = re.sub(r"``([^\n]*?)``", protect_literal, line)

    def explicit_link(match: re.Match[str]) -> str:
        label = match.group(1).strip()
        target = match.group(2).strip()
        return f"[{label}]({target})"

    def role_value(match: re.Match[str]) -> str:
        if preserve_rst_links and match.group(1).lower() in RST_LINK_ROLES:
            return match.group(0)
        value = match.group(2).strip()
        if "<" in value and value.endswith(">"):
            value = value.rsplit("<", 1)[0].strip() or value[1:-1].strip()
        return value

    line = re.sub(r"`([^`]+?)\s+<([^`>]+)>`_{1,2}", explicit_link, line)
    line = re.sub(r":([A-Za-z][\w.-]*):`([^`]+)`", role_value, line)
    if not preserve_rst_links:
        line = re.sub(r"`([^`]+)`_{1,2}", r"\1", line)

    def restore_literal(match: re.Match[str]) -> str:
        content = literals[int(match.group(1))]
        return f"``{content}``" if preserve_rst_links else f"`{content}`"

    line = re.sub(r"\x00RST_INLINE_LITERAL_(\d+)\x01", restore_literal, line)
    line = re.sub(r"^(\s*)#\.\s+", r"\g<1>1. ", line)
    return line


def _directive_block(lines: list[str], start: int) -> tuple[str, str, list[str], int] | None:
    match = RST_DIRECTIVE_PATTERN.match(lines[start])
    if match is None:
        return None
    indent = len(match.group("indent"))
    name = match.group("name").lower()
    argument = (match.group("argument") or "").strip()
    end = start + 1
    while end < len(lines):
        line = lines[end]
        if line.strip() and _indent_width(line) <= indent:
            break
        end += 1
    return name, argument, lines[start + 1:end], end


def _directive_content(body: list[str]) -> list[str]:
    """Drop directive options and normalize the indentation of its content."""

    content = body[:]
    while content:
        if not content[0].strip():
            content.pop(0)
            continue
        # Directive options have a space or end-of-line after the closing
        # colon.  Do not mistake an inline role such as ``:ref:`...`` for an
        # option in the directive body.
        if re.match(r"^[ ]+:[^:]+:(?:[ \t].*)?$", content[0]):
            content.pop(0)
            continue
        break
    while content and not content[-1].strip():
        content.pop()
    return _deindent(content)


RST_ROLE_OPEN_PATTERN = re.compile(r":(?:ref|doc|download|numref):`", re.IGNORECASE)


def _join_multiline_rst_roles(lines: list[str]) -> list[str]:
    """Join wrapped RST roles before adding Markdown blockquote prefixes."""

    output: list[str] = []
    pending: list[str] | None = None
    for line in lines:
        if pending is not None:
            pending.append(line.strip())
            if line.count("`") % 2:
                output.append(" ".join(part for part in pending if part))
                pending = None
            continue

        role = RST_ROLE_OPEN_PATTERN.search(line)
        if role is not None and line[role.start() :].count("`") % 2:
            pending = [line.strip()]
            continue
        output.append(line)
    if pending is not None:
        output.extend(pending)
    return output


def _directive_option(body: list[str], name: str) -> str:
    pattern = re.compile(rf"^[ ]+:{re.escape(name)}:(?:[ \t]+(.*))?$")
    for line in body:
        match = pattern.match(line)
        if match:
            return (match.group(1) or "").strip()
    return ""


def _grid_border_positions(line: str) -> list[int] | None:
    """Return column boundaries for an RST grid-table border."""

    raw = line.rstrip()
    if not raw:
        return None
    indent = len(raw) - len(raw.lstrip(" "))
    if indent >= len(raw) or raw[indent] not in "+|" or not raw.endswith("+"):
        return None
    if raw[indent] == "|" and "+" not in raw[indent + 1 :]:
        return None
    border = raw[indent + 1 : -1]
    if not border or any(char not in "+-=| " for char in border):
        return None
    positions: list[int] = []
    if raw[indent] == "|":
        positions.append(indent)
    for index, char in enumerate(raw):
        if char == "+" and (not positions or index > positions[-1] + 1):
            positions.append(index)
    return positions if len(positions) >= 2 else None


def _simple_border_spans(line: str) -> list[tuple[int, int]] | None:
    """Return fixed-width column spans for an RST simple-table border."""

    raw = line.rstrip()
    runs = list(re.finditer(r"=+", raw))
    if len(runs) < 2:
        return None
    if any(left.end() < right.start() and raw[left.end() : right.start()].strip()
           for left, right in zip(runs, runs[1:])):
        return None
    return [(match.start(), match.end()) for match in runs]


def _table_cell(value: str) -> str:
    value = " ".join(value.split())
    return value.replace("|", r"\|")


def _gfm_table(rows: list[list[str]]) -> list[str] | None:
    """Render parsed rows as GFM, treating the first row as the header."""

    if not rows or not rows[0] or not any(cell.strip() for cell in rows[0]):
        return None
    width = max(len(row) for row in rows)
    normalized = [row + [""] * (width - len(row)) for row in rows]
    output = [
        "| " + " | ".join(_table_cell(cell) for cell in normalized[0]) + " |",
        "| " + " | ".join("---" for _ in range(width)) + " |",
    ]
    output.extend(
        "| " + " | ".join(_table_cell(cell) for cell in row) + " |"
        for row in normalized[1:]
    )
    return output


def _grid_table_at(lines: list[str], start: int) -> tuple[list[str], int] | None:
    first_border = _grid_border_positions(lines[start])
    if first_border is None:
        return None

    border_positions = [first_border]
    outer_left = first_border[0]
    outer_right = first_border[-1]
    end = start + 1
    while end < len(lines):
        border = _grid_border_positions(lines[end])
        if border is not None:
            border_positions.append(border)
            outer_left = min(outer_left, border[0])
            outer_right = max(outer_right, border[-1])
            end += 1
            continue
        raw = lines[end].rstrip()
        if raw and len(raw) > outer_right and raw[outer_left] == "|":
            end += 1
            continue
        break

    if end <= start + 2 or _grid_border_positions(lines[end - 1]) is None:
        return None

    positions = sorted({position for border in border_positions for position in border})
    if len(positions) < 2:
        return None

    rows: list[list[str]] = []
    current: list[list[str]] = [[] for _ in range(len(positions) - 1)]
    for line in lines[start + 1 : end - 1]:
        if _grid_border_positions(line) is not None:
            if any(cell.strip() for column in current for cell in column):
                rows.append(["<br>".join(column) for column in current])
            current = [[] for _ in range(len(positions) - 1)]
            continue
        raw = line.rstrip()
        if len(raw) <= outer_left or raw[outer_left] != "|":
            return None
        # A literal ``|`` inside a cell is content, not a column boundary.
        # Only bars or plus signs at positions observed on a border line can
        # delimit cells.  A plus sign inside a content line is a partial
        # horizontal border for a spanning cell, so retain the text before it
        # and treat the dashed portions as empty cells.
        content_positions = [
            index for index in positions if index < len(raw) and raw[index] in "|+"
        ]
        logical_positions = {position: index for index, position in enumerate(positions)}
        if content_positions and content_positions[-1] != outer_right:
            for shifted_right in range(outer_right + 1, min(len(raw), outer_right + 5)):
                if raw[shifted_right] == "|":
                    content_positions.append(shifted_right)
                    logical_positions[shifted_right] = len(positions) - 1
                    break
        if len(content_positions) < 2 or content_positions[0] != outer_left:
            return None
        for left, right in zip(content_positions, content_positions[1:]):
            left_index = logical_positions.get(left)
            right_index = logical_positions.get(right)
            if left_index is None or right_index is None:
                return None
            if right_index <= left_index:
                return None
            cell = raw[left + 1 : right]
            if raw[left] == "+" and not cell.strip(" +-=|"):
                cell = ""
            current[left_index].append(cell)
    if any(cell.strip() for column in current for cell in column):
        rows.append(["<br>".join(column) for column in current])

    rendered = _gfm_table(rows)
    return (rendered, end) if rendered is not None else None


def _simple_table_at(lines: list[str], start: int) -> tuple[list[str], int] | None:
    spans = _simple_border_spans(lines[start])
    if spans is None:
        return None

    rows: list[list[str]] = []
    border_count = 1
    end = start + 1
    while end < len(lines):
        line = lines[end]
        if _simple_border_spans(line) is not None:
            border_count += 1
            end += 1
            if border_count >= 3 or (border_count == 2 and len(rows) >= 2):
                break
            continue
        if not line.strip():
            break
        if len(line) < spans[0][0]:
            break
        rows.append([line[left:right].strip() for left, right in spans])
        end += 1

    if border_count < 2 or not rows:
        return None
    rendered = _gfm_table(rows)
    return (rendered, end) if rendered is not None else None


def _rst_table_at(lines: list[str], start: int) -> tuple[list[str], int] | None:
    return _grid_table_at(lines, start) or _simple_table_at(lines, start)


def _normalize_embedded_tables(lines: list[str], *, allow_indented: bool = False) -> list[str]:
    """Convert RST tables while leaving fenced code and diagrams untouched."""

    output: list[str] = []
    in_fence = False
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("```"):
            in_fence = not in_fence
            output.append(line)
            index += 1
            continue
        if not in_fence and (allow_indented or _indent_width(line) == 0):
            table = _rst_table_at(lines, index)
            if table is not None:
                rendered, end = table
                output.extend(rendered)
                index = end
                continue
        output.append(line)
        index += 1
    return output


def _resolve_literalinclude(
    argument: str,
    raw_body: list[str],
    repo_dir: Path | None,
    source_path: Path | None,
) -> tuple[str, str, list[str]] | None:
    """Resolve a safe, unsliced literalinclude inside the fixed source tree."""

    if repo_dir is None or source_path is None or not argument:
        return None
    options = {
        match.group(1)
        for line in raw_body
        if (match := re.match(r"^[ ]+:([^:]+):", line))
    }
    if options - {"language", "linenos", "caption", "name", "class"}:
        return None

    repo_root = repo_dir.resolve()
    include_path = (source_path.parent / argument.strip()).resolve()
    try:
        include_rel = include_path.relative_to(repo_root).as_posix()
    except ValueError:
        return None
    if not include_path.is_file() or include_path.stat().st_size > 1_000_000:
        return None
    try:
        content = include_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    language = _directive_option(raw_body, "language")
    if not language:
        language = include_path.suffix.removeprefix(".")
    return include_rel, language, content.rstrip("\n").splitlines()


def _resolve_text_include(
    argument: str,
    repo_dir: Path | None,
    source_path: Path | None,
) -> tuple[str, Path, str] | None:
    """Resolve a bounded text include without allowing path escape."""

    if repo_dir is None or source_path is None or not argument:
        return None
    repo_root = repo_dir.resolve()
    include_path = (source_path.parent / argument.strip()).resolve()
    try:
        include_rel = include_path.relative_to(repo_root).as_posix()
    except ValueError:
        return None
    if not include_path.is_file() or include_path.stat().st_size > 1_000_000:
        return None
    if include_path.suffix.lower() not in {".rst", ".md", ".markdown", ".txt", ".inc"}:
        return None
    try:
        content = include_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    return include_rel, include_path, content


def rst_to_markdown(
    text: str,
    default_title: str = "",
    *,
    repo_dir: Path | None = None,
    source_path: Path | None = None,
    preserve_rst_links: bool = False,
    _include_depth: int = 0,
) -> tuple[str, str]:
    """Convert Ceph's RST to conservative Markdown while retaining unknown RST.

    This is deliberately not a Sphinx reimplementation.  Structural headings,
    code directives, admonitions, links, and common roles become Markdown; all
    other directives remain visible as indented RST so source content is not
    silently discarded when the upstream documentation adds a directive.
    """

    lines = text.replace("\r\n", "\n").replace("\r", "\n").expandtabs(8).split("\n")
    output: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]

        directive = _directive_block(lines, i)
        if directive is not None:
            name, argument, raw_body, end = directive
            content = _directive_content(raw_body)
            if name == "literalinclude":
                included = _resolve_literalinclude(argument, raw_body, repo_dir, source_path)
                if included is not None:
                    include_rel, language, include_lines = included
                    output.extend([f"Included file `{include_rel}`:", "", f"```{language}".rstrip()])
                    output.extend(include_lines)
                    output.extend(["```", ""])
                else:
                    output.append(f".. {name}::{(' ' + argument) if argument else ''}".rstrip())
                    for raw_line in _deindent(raw_body):
                        output.append(f"   {raw_line}" if raw_line else "")
                    output.append("")
            elif name in {"image", "figure"}:
                target = argument.split()[0] if argument else ""
                alt = _directive_option(raw_body, "alt") or _directive_option(raw_body, "caption")
                output.append(f"![{alt}]({target})" if target else f".. {name}::")
                output.append("")
            elif name == "include":
                included = _resolve_text_include(argument, repo_dir, source_path)
                if included is not None and _include_depth < 5:
                    include_rel, include_path, include_text = included
                    _, include_body = rst_to_markdown(
                        include_text,
                        default_title=include_path.stem,
                        repo_dir=repo_dir,
                        source_path=include_path,
                        preserve_rst_links=preserve_rst_links,
                        _include_depth=_include_depth + 1,
                    )
                    output.extend([f"Included file `{include_rel}`:", ""])
                    output.extend(include_body.rstrip("\n").splitlines())
                    output.append("")
                else:
                    output.append(f".. {name}::{(' ' + argument) if argument else ''}".rstrip())
                    output.extend(f"   {raw_line}" if raw_line else "" for raw_line in _deindent(raw_body))
                    output.append("")
            elif name == "table":
                if argument:
                    output.extend([f"**{_inline_rst_to_markdown(argument, preserve_rst_links=preserve_rst_links)}**", ""])
                rendered = _normalize_embedded_tables(content, allow_indented=True)
                output.extend(rendered)
                output.append("")
            elif name in RST_CODE_DIRECTIVES:
                language = argument.split()[0] if argument else ""
                output.extend(["", f"```{language}".rstrip()])
                output.extend(content)
                output.extend(["```", ""])
            elif name in RST_ADMONITIONS:
                label = name.capitalize()
                first = _inline_rst_to_markdown(argument, preserve_rst_links=preserve_rst_links) if argument else ""
                output.append(f"> **{label}:**" + (f" {first}" if first else ""))
                admonition_content = _normalize_embedded_tables(content, allow_indented=True)
                admonition_content = _join_multiline_rst_roles(admonition_content)
                for content_line in admonition_content:
                    output.append(">" if not content_line else f"> {_inline_rst_to_markdown(content_line, preserve_rst_links=preserve_rst_links)}")
                output.append("")
            else:
                output.append(f".. {name}::{(' ' + argument) if argument else ''}".rstrip())
                for content_line in _deindent(raw_body):
                    output.append(f"   {content_line}" if content_line else "")
                output.append("")
            i = end
            continue

        if line.strip():
            table = _rst_table_at(lines, i)
            if table is not None:
                rendered, end = table
                output.extend(rendered)
                output.append("")
                i = end
                continue

        if RST_TARGET_PATTERN.match(line):
            output.append(line.strip())
            i += 1
            continue

        if (
            _indent_width(line) == 0
            and _is_section_underline(line)
            and i + 2 < len(lines)
            and lines[i + 1].strip()
            and lines[i + 2].strip() == line.strip()
        ):
            # RST's overline/title/underline form, used by document roots.
            output.append(f"{'#' * _section_level(line)} {lines[i + 1].strip()}")
            i += 3
            continue

        if (
            line.strip()
            and _indent_width(line) == 0
            and i + 1 < len(lines)
            and _is_section_underline(lines[i + 1])
        ):
            # RST's title/underline form for ordinary sections.
            output.append(f"{'#' * _section_level(lines[i + 1])} {line.strip()}")
            i += 2
            continue

        if (
            line.strip().endswith("::")
            and i + 1 < len(lines)
            and not line.lstrip().startswith(".. ")
        ):
            body_start = i + 1
            if body_start < len(lines) and not lines[body_start].strip():
                body_start += 1
            base_indent = _indent_width(line)
            body_end = body_start
            while body_end < len(lines):
                if lines[body_end].strip() and _indent_width(lines[body_end]) <= base_indent:
                    break
                body_end += 1
            if body_end > body_start and any(lines[k].strip() for k in range(body_start, body_end)):
                output.append(_inline_rst_to_markdown(line.rstrip()[:-1], preserve_rst_links=preserve_rst_links))
                literal = _deindent(lines[body_start:body_end])
                while literal and not literal[-1].strip():
                    literal.pop()
                output.extend(["", "```"])
                output.extend(literal)
                output.extend(["```", ""])
                i = body_end
                continue

        output.append(_inline_rst_to_markdown(line.rstrip(), preserve_rst_links=preserve_rst_links))
        i += 1

    output = _normalize_embedded_tables(output)
    # RST examples frequently mix spaces and tabs.  Markdown renders them as
    # indentation, but the mixed form trips git's whitespace checker and can
    # make copied code depend on the viewer's tab stop.  Keep the rendered
    # layout while making the generated corpus deterministic.
    body = re.sub(r"[ \t]+$", "", "\n".join(output).expandtabs(8), flags=re.MULTILINE)
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    title = ""
    for candidate in body.splitlines():
        heading = re.match(r"^#\s+(.+)$", candidate)
        if heading:
            title = heading.group(1).strip()
            break
    return title or default_title, body

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
            import yaml

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
    text = content

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


def _discover_source_files(manifest: Manifest, repo_dir: Path) -> list[tuple[Path, str]]:
    supported_suffixes = {".md", ".markdown", ".rst"}
    if manifest.content_selector:
        supported_suffixes.add(".html")

    discovered: list[tuple[Path, str]] = []
    for doc_item in manifest.docs_paths:
        item_path = repo_dir / doc_item
        if not item_path.exists():
            print(f"[{manifest.name}] Warning: path not found in repo: {doc_item}", file=sys.stderr)
            continue
        if item_path.is_file():
            if item_path.suffix.lower() in supported_suffixes:
                discovered.append((item_path, Path(doc_item).name))
            continue
        for path in sorted(item_path.rglob("*")):
            if path.is_file() and path.suffix.lower() in supported_suffixes:
                discovered.append((path, path.relative_to(item_path).as_posix()))
    return discovered


def _has_source_content(text: str) -> bool:
    return bool(text.strip())


def _source_url(manifest: Manifest, repo_rel_path: str, doc_path: str = "") -> str:
    """Build the immutable source URL used by frontmatter and assets."""

    base_repo_url = manifest.repo_url.rstrip("/")
    if manifest.source_url_template:
        return manifest.source_url_template.format(
            repo_url=base_repo_url,
            git_ref=manifest.git_ref,
            path=repo_rel_path,
            doc_path=doc_path or repo_rel_path,
        )
    return f"{base_repo_url}/blob/{manifest.git_ref}/{repo_rel_path}"


def _pinned_asset_url(manifest: Manifest, target: str) -> str | None:
    """Pin same-repository GitHub blob assets to the manifest commit."""

    repository = urlsplit(manifest.repo_url.rstrip("/"))
    parsed = urlsplit(target)
    if (parsed.scheme, parsed.netloc) != (repository.scheme, repository.netloc):
        return None
    prefix = repository.path.rstrip("/") + "/blob/"
    if not parsed.path.startswith(prefix):
        return None
    remainder = parsed.path[len(prefix) :]
    parts = remainder.split("/", 1)
    if len(parts) != 2 or Path(parts[1]).suffix.lower() not in ASSET_SUFFIXES:
        return None
    pinned_path = f"{prefix}{manifest.git_ref}/{parts[1]}"
    return urlunsplit((parsed.scheme, parsed.netloc, pinned_path, parsed.query, parsed.fragment))


def _source_link_candidates(file_path: Path, target: str) -> list[Path]:
    target_path = target.split("#", 1)[0].split("?", 1)[0]
    if not target_path:
        return []
    candidates: list[Path] = []
    bases = (file_path.parent / file_path.stem, file_path.parent)
    for base in bases:
        candidate = Path(os.path.normpath(str(base / target_path)))
        candidates.append(candidate)
        if candidate.suffix == "":
            for suffix in (".rst", ".md", ".markdown"):
                candidates.append(candidate.with_suffix(suffix))
            candidates.extend((candidate / "index.rst", candidate / "index.md"))
        elif candidate.suffix.lower() in {".md", ".markdown"}:
            candidates.append(candidate.with_suffix(".rst"))
    unique: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        if candidate not in seen:
            unique.append(candidate)
            seen.add(candidate)
    return unique


def _rewrite_source_links(
    body: str,
    file_path: Path,
    target_rel: Path,
    repo_dir: Path,
    source_outputs: dict[str, str],
    manifest: Manifest,
) -> str:
    """Point source-relative Markdown links at corpus pages or fixed assets."""

    repo_root = repo_dir.resolve()

    def replacement(open_text: str, target: str) -> str:
        original = f"{open_text}{target})"
        target = target.strip()
        pinned_asset = _pinned_asset_url(manifest, target)
        if pinned_asset is not None:
            return f"{open_text}{pinned_asset})"
        if (
            not target
            or target.startswith(("#", "/", "//", "http:", "https:", "mailto:", "ftp:"))
            or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target)
            or ("@" in target and "/" not in target)
            or re.match(r"^[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+){2,}(?:/|$)", target)
        ):
            return original

        if target.startswith("<") and target.endswith(">"):
            target = target[1:-1].strip()
        path_part, hash_mark, fragment = target.partition("#")
        query = ""
        if "?" in path_part:
            path_part, query = path_part.split("?", 1)
        suffix = (f"?{query}" if query else "") + (f"#{fragment}" if hash_mark else "")

        for candidate in _source_link_candidates(file_path, path_part):
            try:
                repo_rel = candidate.resolve().relative_to(repo_root).as_posix()
            except ValueError:
                continue
            output_path = source_outputs.get(repo_rel)
            if output_path is not None:
                relative = os.path.relpath(output_path, start=target_rel.parent.as_posix()).replace(os.sep, "/")
                return f"{open_text}{relative}{suffix})"
            if candidate.is_file():
                return f"{open_text}{_source_url(manifest, repo_rel)}{suffix})"
        # Keep upstream prose readable when a source-relative target points to
        # a page outside the pinned documentation corpus, but make the
        # classification explicit instead of silently turning it into plain
        # text.
        return f"{original} <!-- unresolved-source-link: target={target} -->"

    link_open_pattern = re.compile(r"(?P<open>!?\[[^\]\n]*\]\()")

    def rewrite_segment(segment: str) -> str:
        output: list[str] = []
        cursor = 0
        while True:
            match = link_open_pattern.search(segment, cursor)
            if match is None:
                output.append(segment[cursor:])
                break
            output.append(segment[cursor : match.start()])
            target_start = match.end()
            index = target_start
            depth = 0
            escaped = False
            target_end: int | None = None
            while index < len(segment):
                char = segment[index]
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == "(":
                    depth += 1
                elif char == ")":
                    if depth == 0:
                        target_end = index
                        break
                    depth -= 1
                index += 1
            if target_end is None:
                output.append(segment[match.start() :])
                break
            output.append(replacement(match.group("open"), segment[target_start:target_end]))
            cursor = target_end + 1
        return "".join(output)

    output: list[str] = []
    normal: list[str] = []
    in_fence = False
    for line in body.splitlines(keepends=True):
        if line.startswith("```"):
            if normal:
                output.append(rewrite_segment("".join(normal)))
                normal = []
            output.append(line)
            in_fence = not in_fence
        elif in_fence:
            output.append(line)
        else:
            normal.append(line)
    if normal:
        output.append(rewrite_segment("".join(normal)))
    return "".join(output)


def _reference_key(label: str) -> str:
    return " ".join(label.strip().strip("`").split()).lower()


def _reference_anchor(label: str) -> str:
    anchor = re.sub(r"[^a-z0-9]+", "-", label.strip("`").lower()).strip("-")
    return anchor or "section"


RstTarget = tuple[Path, str, str]
RstTargetMap = dict[str, RstTarget | list[RstTarget]]


def _rst_target_candidates(
    rst_targets: RstTargetMap,
    key: str,
) -> list[RstTarget]:
    """Return all definitions for a label, keeping local collisions resolvable."""

    value = rst_targets.get(key)
    if value is None:
        return []
    if isinstance(value, tuple):
        # Keep compatibility with callers/tests that provide the old one-target map.
        return [value]
    return value


def _collect_rst_targets(
    files_to_process: list[tuple[Path, str]],
) -> RstTargetMap:
    targets: RstTargetMap = {}
    for file_path, _ in files_to_process:
        if file_path.suffix.lower() != ".rst":
            continue
        try:
            text = file_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for match in RST_TARGET_PATTERN.finditer(text):
            label = match.group("label").strip()
            targets.setdefault(_reference_key(label), []).append(
                (file_path, (match.group("target") or "").strip(), label)
            )
        lines = text.replace("\r\n", "\n").replace("\r", "\n").splitlines()
        for index, line in enumerate(lines[:-1]):
            if (
                line.strip()
                and _indent_width(line) == 0
                and _is_section_underline(lines[index + 1])
            ):
                label = line.strip()
                key = _reference_key(label)
                candidates = _rst_target_candidates(targets, key)
                if not any(candidate[0].resolve() == file_path.resolve() for candidate in candidates):
                    targets.setdefault(key, []).append((file_path, "", label))
    return targets


def _source_output_for(
    file_path: Path,
    repo_dir: Path,
    source_outputs: dict[str, str],
) -> str | None:
    try:
        return source_outputs.get(file_path.resolve().relative_to(repo_dir.resolve()).as_posix())
    except ValueError:
        return None


def _resolve_source_target(
    target: str,
    *,
    base_file: Path,
    target_rel: Path,
    repo_dir: Path,
    source_outputs: dict[str, str],
    manifest: Manifest,
) -> str | None:
    target = target.strip()
    if not target:
        return None
    if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", target) or target.startswith("//"):
        return target
    if target.startswith("#"):
        return target
    path_part, hash_mark, fragment = target.partition("#")
    link_suffix = f"#{fragment}" if hash_mark else ""
    query = ""
    if "?" in path_part:
        path_part, query = path_part.split("?", 1)
    link_suffix = (f"?{query}" if query else "") + link_suffix
    if path_part.startswith("/"):
        roots = [repo_dir]
        roots.extend(repo_dir / docs_path for docs_path in manifest.docs_paths)
        candidates = []
        for root in roots:
            candidate = root / path_part.lstrip("/")
            candidates.append(candidate)
            if candidate.suffix == "":
                for extension in (".rst", ".md", ".markdown"):
                    candidates.append(candidate.with_suffix(extension))
                candidates.extend((candidate / "index.rst", candidate / "index.md"))
    else:
        candidates = _source_link_candidates(base_file, path_part)
    for candidate in candidates:
        try:
            repo_rel = candidate.resolve().relative_to(repo_dir.resolve()).as_posix()
        except ValueError:
            continue
        output_path = source_outputs.get(repo_rel)
        if output_path is not None:
            relative = os.path.relpath(output_path, start=target_rel.parent.as_posix()).replace(os.sep, "/")
            return f"{relative}{link_suffix}"
        if candidate.is_file() and candidate.suffix.lower() in ASSET_SUFFIXES:
            return f"{_source_url(manifest, repo_rel)}{link_suffix}"
    return None


def _resolve_rst_reference(
    label: str,
    *,
    base_file: Path,
    target_rel: Path,
    repo_dir: Path,
    source_outputs: dict[str, str],
    manifest: Manifest,
    rst_targets: RstTargetMap,
) -> str | None:
    target = label.strip()
    candidates = _rst_target_candidates(rst_targets, _reference_key(target))
    target_spec = next(
        (candidate for candidate in candidates if candidate[0].resolve() == base_file.resolve()),
        candidates[0] if candidates else None,
    )
    if target_spec is not None:
        target_file, defined_target, defined_label = target_spec
        if not defined_target:
            output_path = _source_output_for(target_file, repo_dir, source_outputs)
            if output_path is None:
                return None
            relative = os.path.relpath(output_path, start=target_rel.parent.as_posix()).replace(os.sep, "/")
            return f"{relative}#{_reference_anchor(defined_label)}"
        target = defined_target
        base_file = target_file
    return _resolve_source_target(
        target,
        base_file=base_file,
        target_rel=target_rel,
        repo_dir=repo_dir,
        source_outputs=source_outputs,
        manifest=manifest,
    )


def _rewrite_rst_links(
    body: str,
    file_path: Path,
    target_rel: Path,
    repo_dir: Path,
    source_outputs: dict[str, str],
    manifest: Manifest,
    rst_targets: RstTargetMap | None = None,
) -> str:
    """Resolve RST roles and named references without touching fenced code."""

    rst_targets = rst_targets or {}
    anonymous_targets: list[str] = []
    in_fence = False
    for line in body.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^__\s+(?P<target>.+?)\s*$", line)
        if match is None:
            match = re.match(r"^\.\.\s+__:\s*(?P<target>.+?)\s*$", line)
        if match is not None:
            anonymous_targets.append(match.group("target"))
    anonymous_index = [0]
    bare_labels = sorted(
        {
            label
            for value in rst_targets.values()
            for _, _, label in (
                [value] if isinstance(value, tuple) else value
            )
            if label
        },
        key=len,
        reverse=True,
    )
    bare_reference_pattern = (
        re.compile(
            r"(?<![\w`])(?P<label>" + "|".join(re.escape(label) for label in bare_labels) + r")_(?!\w)"
        )
        if bare_labels
        else None
    )

    def rewrite_segment(segment: str) -> str:
        literals: list[str] = []

        def protect_literal(match: re.Match[str]) -> str:
            literals.append(match.group(1))
            return f"\x00RST_REWRITE_LITERAL_{len(literals) - 1}\x01"

        segment = re.sub(r"``([^\n]*?)``(?!_)", protect_literal, segment)

        def target_definition(match: re.Match[str]) -> str:
            label = match.group("label").strip()
            target = (match.group("target") or "").strip()
            if target:
                return ""
            return f'<a id="{_reference_anchor(label)}"></a>'

        segment = RST_TARGET_PATTERN.sub(target_definition, segment)
        segment = re.sub(r"(?m)^__\s+.*$\n?", "", segment)
        segment = _inline_rst_to_markdown(segment, preserve_rst_links=True)

        def resolve_value(kind: str, value: str) -> str:
            value = re.sub(r"\n[ \t]*>[ \t]?", " ", value)
            value = " ".join(value.split())
            label = value
            target = value
            explicit = re.match(r"^(?P<label>.+?)\s*<(?P<target>[^>]+)>$", value)
            if explicit is not None:
                label = explicit.group("label").strip()
                target = explicit.group("target").strip()
            resolved = _resolve_rst_reference(
                target,
                base_file=file_path,
                target_rel=target_rel,
                repo_dir=repo_dir,
                source_outputs=source_outputs,
                manifest=manifest,
                rst_targets=rst_targets,
            )
            if resolved is None:
                return f"{label} <!-- unresolved-rst-link: kind={kind} target={target} -->"
            return f"[{label}]({resolved})"

        segment = re.sub(
            r":(?P<kind>ref|doc|download|numref):[ \t]*`(?P<value>[^`]+)`",
            lambda match: resolve_value(match.group("kind").lower(), match.group("value")),
            segment,
            flags=re.IGNORECASE,
        )
        segment = re.sub(
            r":(?P<kind>ref|doc|download|numref):(?P<target>[A-Za-z0-9_./#-]+)",
            lambda match: resolve_value(match.group("kind").lower(), match.group("target")),
            segment,
            flags=re.IGNORECASE,
        )

        def named_link(label: str, kind: str = "named") -> str:
            label = re.sub(r"\n[ \t]*>[ \t]?", " ", label)
            label = " ".join(label.split())
            resolved = _resolve_rst_reference(
                label,
                base_file=file_path,
                target_rel=target_rel,
                repo_dir=repo_dir,
                source_outputs=source_outputs,
                manifest=manifest,
                rst_targets=rst_targets,
            )
            if resolved is None:
                return f"{label} <!-- unresolved-rst-link: kind={kind} target={label} -->"
            return f"[{label}]({resolved})"

        def named_reference(match: re.Match[str]) -> str:
            return named_link(match.group("label"))

        def multiline_named_reference(match: re.Match[str]) -> str:
            return named_link("\n".join((match.group("label"), match.group("continuation"))))

        def double_named_reference(match: re.Match[str]) -> str:
            return named_link(match.group("label"))

        def anonymous_link(label: str) -> str:
            label = re.sub(r"\n[ \t]*>[ \t]?", " ", label)
            label = " ".join(label.split())
            if anonymous_index[0] >= len(anonymous_targets):
                return f"{label} <!-- unresolved-rst-link: kind=anonymous target={label} -->"
            raw_target = anonymous_targets[anonymous_index[0]].strip()
            anonymous_index[0] += 1
            if raw_target.startswith("`") and raw_target.endswith("_"):
                target = raw_target[1:-2]
            else:
                target = raw_target[:-1] if raw_target.endswith("_") else raw_target
            resolved = _resolve_rst_reference(
                target,
                base_file=file_path,
                target_rel=target_rel,
                repo_dir=repo_dir,
                source_outputs=source_outputs,
                manifest=manifest,
                rst_targets=rst_targets,
            )
            if resolved is None:
                return f"{label} <!-- unresolved-rst-link: kind=anonymous target={target} -->"
            return f"[{label}]({resolved})"

        def anonymous_reference(match: re.Match[str]) -> str:
            return anonymous_link(match.group("label"))

        segment = re.sub(r"``(?P<label>[^`\n]+)``_{1,2}", double_named_reference, segment)

        # Apply one pattern to both single-line and wrapped anonymous links.
        # Separate substitutions reorder wrapped links ahead of single-line
        # links, which makes the positional anonymous-target mapping wrong.
        def anonymous_reference_match(match: re.Match[str]) -> str:
            label = match.group("label")
            continuation = match.group("continuation")
            if continuation:
                label = "\n".join((label, continuation))
            return anonymous_link(label)

        segment = re.sub(
            r"(?<![\w`])`(?P<label>[^`\n]{1,200})(?:\n(?P<continuation>[^`\n]{1,200}))?`__",
            anonymous_reference_match,
            segment,
        )

        segment = re.sub(
            r"(?<![\w`])`(?P<label>[^`\n]{1,200})\n(?P<continuation>[^`\n]{1,200})`_{1,2}",
            multiline_named_reference,
            segment,
        )
        segment = re.sub(r"(?<![\w`])`(?P<label>[^`\n]+)`_{1,2}", named_reference, segment)

        # Bare references must run after anonymous links.  Anonymous targets
        # are positional, so a preceding named-reference substitution must not
        # reorder the anonymous-reference pass.
        if bare_reference_pattern is not None:
            def bare_reference(match: re.Match[str]) -> str:
                return named_link(match.group("label"))

            segment = bare_reference_pattern.sub(bare_reference, segment)

        def restore_literal(match: re.Match[str]) -> str:
            return "``" + literals[int(match.group(1))] + "``"

        return re.sub(r"\x00RST_REWRITE_LITERAL_(\d+)\x01", restore_literal, segment)

    output: list[str] = []
    normal: list[str] = []
    in_fence = False
    for line in body.splitlines(keepends=True):
        if line.startswith("```"):
            if normal:
                output.append(rewrite_segment("".join(normal)))
                normal = []
            output.append(line)
            in_fence = not in_fence
        elif in_fence:
            output.append(line)
        else:
            normal.append(line)
    if normal:
        output.append(rewrite_segment("".join(normal)))
    return "".join(output)


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

    is_k8s = manifest.collection == "k8s"
    is_gitlab = manifest.collection == "gitlab"

    files_to_process = _discover_source_files(manifest, repo_dir)
    source_outputs = {
        file_path.relative_to(repo_dir).as_posix(): Path(rel_out_path).with_suffix(".md").as_posix()
        for file_path, rel_out_path in files_to_process
    }
    rst_targets = _collect_rst_targets(files_to_process)

    for file_path, rel_out_path_str in files_to_process:
        repo_rel_path = file_path.relative_to(repo_dir).as_posix()
        source_url = _source_url(manifest, repo_rel_path, rel_out_path_str)

        try:
            raw_text = file_path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            print(f"[{manifest.name}] Error reading {file_path}: {e}", file=sys.stderr)
            continue
        if not _has_source_content(raw_text):
            print(f"[{manifest.name}] Skipping empty source: {repo_rel_path}")
            continue

        target_rel = Path(rel_out_path_str).with_suffix(".md")
        default_title = target_rel.stem

        if file_path.suffix.lower() == ".html":
            from normalize import to_markdown as html_to_markdown

            page_url = f"{manifest.base_url.rstrip('/')}/{rel_out_path_str}"
            html_result = html_to_markdown(raw_text, page_url, manifest)
            if html_result is None:
                print(f"[{manifest.name}] Skipping HTML with no matching content: {repo_rel_path}", file=sys.stderr)
                continue
            title, body = html_result
            body = re.sub(r"[ \t]+$", "", body, flags=re.MULTILINE)
        elif file_path.suffix.lower() == ".rst":
            title, body = rst_to_markdown(
                raw_text,
                default_title=default_title,
                repo_dir=repo_dir,
                source_path=file_path,
                preserve_rst_links=True,
            )
        else:
            title, body = extract_frontmatter(raw_text, default_title=default_title)

        if is_k8s:
            body = clean_hugo_shortcodes(body, repo_dir)
        elif is_gitlab:
            body = clean_gitlab_shortcodes(body)

        if file_path.suffix.lower() in {".md", ".markdown", ".rst"}:
            if file_path.suffix.lower() == ".rst":
                body = _rewrite_rst_links(
                    body,
                    file_path,
                    target_rel,
                    repo_dir,
                    source_outputs,
                    manifest,
                    rst_targets,
                )
            body = _rewrite_source_links(
                body,
                file_path,
                target_rel,
                repo_dir,
                source_outputs,
                manifest,
            )
        title = _inline_rst_to_markdown(title)
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
