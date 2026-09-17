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
import fnmatch
import html
import json
import os
import re
import shutil
import shlex
import subprocess
import sys
import textwrap
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import quote, unquote, urlsplit, urlunsplit

from common import REPO_ROOT, Manifest, load_manifest

FRONTMATTER_PATTERN = re.compile(r"^---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)
HEADING1_PATTERN = re.compile(r"^#\s+(.+)$", re.MULTILINE)
SLACK_INCOMING_WEBHOOK_PATTERN = re.compile(
    r"https://hooks\.slack\.com/services/T[A-Z0-9]{8,}/B[A-Z0-9]{8,}/[A-Za-z0-9_-]{20,}"
)

RST_SECTION_CHARS = set("=-^~\"'*`+_.|#")
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


def redact_secret_like_examples(content: str) -> str:
    """Replace credential-shaped documentation examples with explicit placeholders.

    Some upstream projects publish syntactically valid Slack webhook examples.
    GitHub push protection correctly treats that shape as a secret even when the
    value is made of zeroes and ``X`` characters.  Keep the endpoint structure
    useful while ensuring the generated corpus never carries a usable token.
    """

    return SLACK_INCOMING_WEBHOOK_PATTERN.sub(
        "https://hooks.slack.com/services/WORKSPACE_ID/CHANNEL_ID/REDACTED_TOKEN",
        content,
    )


def _indent_width(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def _is_section_underline(line: str) -> bool:
    stripped = line.strip()
    return (
        len(stripped) >= 3
        and len(set(stripped)) == 1
        and stripped[0] in RST_SECTION_CHARS
    )


def _rst_section_at(lines: list[str], index: int) -> tuple[str, str, bool, int] | None:
    """Return a top-level RST section's title, adornment, and shape."""

    line = lines[index]
    if RST_TARGET_PATTERN.match(line):
        return None
    if (
        _indent_width(line) == 0
        and _is_section_underline(line)
        and index + 2 < len(lines)
        and lines[index + 1].strip()
        and lines[index + 2].strip() == line.strip()
    ):
        return lines[index + 1].strip(), line.strip(), True, index + 3
    if (
        line.strip()
        and _indent_width(line) == 0
        and index + 1 < len(lines)
        and _is_section_underline(lines[index + 1])
    ):
        return line.strip(), lines[index + 1].strip(), False, index + 2
    return None


def _section_levels(lines: list[str]) -> dict[tuple[str, bool], int]:
    """Assign levels by first-seen RST adornment style and shape."""

    levels: dict[tuple[str, bool], int] = {}
    index = 0
    while index < len(lines):
        section = _rst_section_at(lines, index)
        if section is None:
            index += 1
            continue
        _, adornment, overline, end = section
        levels.setdefault((adornment[0], overline), len(levels) + 1)
        index = end
    return levels


def _section_level(adornment: str, overline: bool, levels: dict[tuple[str, bool], int]) -> int:
    return levels[(adornment.strip()[0], overline)]


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


def _is_fenced_markdown_line(line: str) -> bool:
    """Recognize fences with any depth of Markdown blockquote prefix."""

    return re.match(r"^(?:>\s*)*```", line) is not None


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
    _section_levels_context: dict[tuple[str, bool], int] | None = None,
) -> tuple[str, str]:
    """Convert Ceph's RST to conservative Markdown while retaining unknown RST.

    This is deliberately not a Sphinx reimplementation.  Structural headings,
    code directives, admonitions, links, and common roles become Markdown; all
    other directives remain visible as indented RST so source content is not
    silently discarded when the upstream documentation adds a directive.
    """

    lines = text.replace("\r\n", "\n").replace("\r", "\n").expandtabs(8).split("\n")
    local_section_levels = _section_levels(lines)
    if _section_levels_context is None:
        section_levels = local_section_levels
    else:
        section_levels = dict(_section_levels_context)
        next_level = max(section_levels.values(), default=0) + 1
        for style in local_section_levels:
            if style not in section_levels:
                section_levels[style] = next_level
                next_level += 1
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
                        _section_levels_context=section_levels,
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
                admonition_content = _join_multiline_rst_roles(content)
                _, rendered_content = rst_to_markdown(
                    "\n".join(admonition_content),
                    repo_dir=repo_dir,
                    source_path=source_path,
                    preserve_rst_links=preserve_rst_links,
                    _include_depth=_include_depth,
                    _section_levels_context=section_levels,
                )
                rendered_in_fence = False
                for content_line in rendered_content.rstrip("\n").splitlines():
                    if _is_fenced_markdown_line(content_line):
                        rendered_in_fence = not rendered_in_fence
                        rendered_line = content_line
                    elif rendered_in_fence:
                        rendered_line = content_line
                    else:
                        rendered_line = _inline_rst_to_markdown(
                            content_line,
                            preserve_rst_links=preserve_rst_links,
                        )
                    output.append(">" if not rendered_line else f"> {rendered_line}")
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

        section = _rst_section_at(lines, i)
        if section is not None:
            title, adornment, overline, end = section
            level = _section_level(adornment, overline, section_levels)
            output.append(f"{'#' * level} {title}")
            i = end
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


def extract_frontmatter_description(content: str) -> str:
    """Return a source description without changing legacy frontmatter rules."""

    match = FRONTMATTER_PATTERN.match(content)
    if match is None:
        return ""
    raw_yaml = match.group(1)
    try:
        import yaml

        parsed = yaml.safe_load(raw_yaml)
        if isinstance(parsed, dict):
            value = parsed.get("description")
            if isinstance(value, str):
                return value.strip()
    except Exception:
        pass

    # Keep the fallback deliberately scalar-only.  A multiline YAML value is
    # ambiguous without a parser and should not be guessed into corpus prose.
    description_match = re.search(
        r"^description:\s*(?:\"([^\"]*)\"|'([^']*)'|(.*))$",
        raw_yaml,
        re.MULTILINE,
    )
    if description_match is None:
        return ""
    return (
        description_match.group(1)
        or description_match.group(2)
        or description_match.group(3)
        or ""
    ).strip()


def _safe_repo_file(repo_dir: Path, candidate: Path) -> Path | None:
    """Return a regular file only when it resolves inside ``repo_dir``."""

    repo_root = repo_dir.resolve()
    try:
        resolved = candidate.resolve()
        resolved.relative_to(repo_root)
    except (OSError, ValueError):
        return None
    return resolved if resolved.is_file() else None


def resolve_example_file(repo_dir: Path, file_path_str: str) -> Path | None:
    """尋找 Hugo shortcode 引用的範例檔案路徑。"""
    raw = file_path_str.strip()
    if not raw or raw.startswith(("/", "\\")) or re.match(r"^[A-Za-z]:[\\/]", raw):
        return None
    rel = raw.replace("\\", "/")
    candidates = [
        repo_dir / "content/en/examples" / rel,
        repo_dir / "content/examples" / rel,
        repo_dir / "content/en" / rel,
        repo_dir / "content" / rel,
        repo_dir / "examples" / rel,
        repo_dir / rel,
    ]
    for cand in candidates:
        resolved = _safe_repo_file(repo_dir, cand)
        if resolved is not None:
            return resolved
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
    raw = file_path_str.strip()
    if not raw or raw.startswith(("/", "\\")) or re.match(r"^[A-Za-z]:[\\/]", raw):
        return None
    rel = raw.replace("\\", "/")
    candidates = [
        repo_dir / "content/en/includes" / rel,
        repo_dir / "content/includes" / rel,
        repo_dir / "content/en/docs" / rel,
        repo_dir / "content/en" / rel,
        repo_dir / rel,
    ]
    for cand in candidates:
        resolved = _safe_repo_file(repo_dir, cand)
        if resolved is not None:
            return resolved
    return None


def _clean_kubernetes_shortcodes(content: str, repo_dir: Path, depth: int = 0) -> str:
    """處理 Kubernetes Hugo 網站 markdown 中的 shortcode。

    Keep this implementation isolated from source-specific profiles.  Existing
    Kubernetes manifests historically reached this function implicitly, and
    their rendered output is part of the compatibility contract.
    """
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
                return _clean_kubernetes_shortcodes(inc_text, repo_dir, depth + 1)
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


ISTIO_SHORTCODE_TOKEN_PATTERN = re.compile(
    r"\{\{[<%](?P<body>.*?)[>%]\}\}",
    re.DOTALL,
)
ISTIO_PAIRED_SHORTCODES = {
    "gloss",
    "idea",
    "quote",
    "tab",
    "tabset",
    "text",
    "tip",
    "warning",
}
ISTIO_ADMONITION_SHORTCODES = {"idea", "quote", "tip", "warning"}

# These shortcodes are defined by the Istio documentation site, but the
# referenced application repository is a different checkout from
# ``istio/istio.io``.  Keep the application source immutable even when the
# documentation checkout is rebuilt later.
ISTIO_APPLICATION_REPO = "https://github.com/istio/istio"
ISTIO_APPLICATION_COMMIT = "8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99"
ISTIO_RELEASE_URL = f"{ISTIO_APPLICATION_REPO}/releases/tag/1.24.0"


@dataclass(frozen=True)
class _ShortcodeToken:
    body: str
    start: int
    end: int


def _iter_shortcode_tokens(content: str) -> list[_ShortcodeToken]:
    """Scan Hugo tags while allowing nested tags inside quoted arguments."""

    tokens: list[_ShortcodeToken] = []
    cursor = 0
    while True:
        opening = re.search(r"\{\{(?P<delimiter>[<%])", content[cursor:])
        if opening is None:
            break
        start = cursor + opening.start()
        body_start = cursor + opening.end()
        delimiters = [">" if opening.group("delimiter") == "<" else "%"]
        index = body_start
        end: int | None = None
        closed = False
        while index < len(content):
            if content.startswith("{{<", index):
                delimiters.append(">")
                index += 3
                continue
            if content.startswith("{{%", index):
                delimiters.append("%")
                index += 3
                continue
            if delimiters and content.startswith(delimiters[-1] + "}}", index):
                index += 3
                delimiters.pop()
                if not delimiters:
                    end = index
                    closed = True
                    break
                continue
            index += 1
        if end is None:
            # Keep an incomplete tag from surviving normalization.  The
            # renderer will turn its remaining body into a readable marker.
            end = len(content)
        body_end = end - 3 if closed else end
        tokens.append(_ShortcodeToken(content[body_start:body_end], start, end))
        cursor = end
        if end == len(content):
            break
    return tokens


def _shortcode_parts(raw_body: str) -> tuple[str, str, bool]:
    """Return ``(name, arguments, closing)`` for one Hugo tag body."""

    body = raw_body.strip()
    closing = body.startswith("/")
    if closing:
        body = body[1:].lstrip()
    match = re.match(
        r"(?P<name>[A-Za-z0-9_.-]+)(?:[ \t]+(?P<args>.*?))?$",
        body,
        re.DOTALL,
    )
    if match is None:
        return "", body, closing
    return match.group("name").lower(), (match.group("args") or "").strip(), closing


def _shortcode_arguments(arguments: str) -> tuple[list[str], dict[str, str]]:
    """Split Hugo shortcode arguments while tolerating incomplete quoting."""

    try:
        tokens = shlex.split(arguments, posix=True)
    except ValueError:
        tokens = arguments.split()
    positional: list[str] = []
    named: dict[str, str] = {}
    for token in tokens:
        match = re.match(
            r"^(?P<key>[A-Za-z][A-Za-z0-9_-]*)=(?P<value>.*)$",
            token,
            re.DOTALL,
        )
        if match is None:
            positional.append(token)
        else:
            named[match.group("key").lower()] = match.group("value")
    return positional, named


def _shortcode_marker(name: str, arguments: str) -> str:
    """Represent an unsupported shortcode as readable Markdown text."""

    cleaned = " ".join(arguments.split())
    return f"[{name}{(' ' + cleaned) if cleaned else ''}]"


def _repo_relative_file(repo_dir: Path, file_path_str: str) -> Path | None:
    """Resolve a user-supplied path only when it stays inside the checkout."""

    raw = file_path_str.strip()
    if not raw or raw.startswith(("/", "\\")) or re.match(r"^[A-Za-z]:[\\/]", raw):
        return None
    candidate = repo_dir / Path(raw.replace("\\", "/"))
    return _safe_repo_file(repo_dir, candidate)


def _dedent_shortcode_body(inner: str) -> str:
    """Remove only common source indentation from a shortcode body."""

    return textwrap.dedent(inner.replace("\r\n", "\n").replace("\r", "\n")).strip("\n")


def _render_fenced_shortcode(language: str, inner: str) -> str:
    body = _dedent_shortcode_body(inner)
    # A longer fence keeps code examples containing Markdown fences readable.
    fence = "```"
    fence_runs = [len(match.group(0)) for match in re.finditer(r"`{3,}", body)]
    if fence_runs:
        fence = "`" * max(3, max(fence_runs) + 1)
    opening = f"{fence}{language}" if language else fence
    return f"\n\n{opening}\n{body}\n{fence}\n\n"


def _extract_shortcode_language(arguments: str) -> tuple[str, dict[str, str]]:
    positional, named = _shortcode_arguments(arguments)
    language = named.get("syntax", "") or named.get("language", "")
    if not language and positional:
        language = positional[0]
    return language, named


def _render_text_import(
    arguments: str,
    repo_dir: Path,
    *,
    depth: int,
    active_files: frozenset[Path],
) -> str:
    positional, named = _shortcode_arguments(arguments)
    file_name = named.get("file", "") or (positional[0] if positional else "")
    imported = _repo_relative_file(repo_dir, file_name)
    if imported is None or imported.stat().st_size > 1_000_000:
        return _shortcode_marker("text_import", arguments)
    if imported in active_files or depth > 8:
        return f"[text_import recursion blocked: {file_name}]"
    try:
        imported_text = imported.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return _shortcode_marker("text_import", arguments)

    snippet = named.get("snippet", "")
    if snippet:
        snippet_pattern = re.compile(
            rf"(?ms)^\s*#\s*\$snippet\s+{re.escape(snippet)}\s*$"
            rf"(?P<body>.*?)^\s*#\s*\$endsnippet\s*$"
        )
        snippet_match = snippet_pattern.search(imported_text)
        if snippet_match is not None:
            imported_text = snippet_match.group("body").strip("\r\n")
    imported_text = _render_istio_shortcodes(
        imported_text,
        repo_dir,
        depth=depth + 1,
        active_files=active_files | {imported},
    )
    language = named.get("syntax", "") or named.get("language", "")
    return _render_fenced_shortcode(language, imported_text)


def _render_include(
    arguments: str,
    repo_dir: Path,
    *,
    depth: int,
    active_files: frozenset[Path],
) -> str:
    positional, named = _shortcode_arguments(arguments)
    file_name = named.get("file", "") or (positional[0] if positional else "")
    included = resolve_include_file(repo_dir, file_name)
    if included is None or included.stat().st_size > 1_000_000:
        return _shortcode_marker("include", arguments)
    if included in active_files or depth > 8:
        return f"[include recursion blocked: {file_name}]"
    try:
        included_text = included.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return _shortcode_marker("include", arguments)
    included_text = re.sub(
        r"^---\r?\n.*?\r?\n---\r?\n?",
        "",
        included_text,
        count=1,
        flags=re.DOTALL,
    )
    rendered = _render_istio_shortcodes(
        included_text,
        repo_dir,
        depth=depth + 1,
        active_files=active_files | {included},
    ).strip()
    return f"\n\n{rendered}\n\n" if rendered else ""


def _render_boilerplate(
    arguments: str,
    repo_dir: Path,
    *,
    depth: int,
    active_files: frozenset[Path],
) -> str:
    positional, named = _shortcode_arguments(arguments)
    name = named.get("file", "") or (positional[0] if positional else "")
    if not name:
        return _shortcode_marker("boilerplate", arguments)
    relative = name if name.lower().endswith((".md", ".markdown")) else f"{name}.md"
    boilerplate_root = (repo_dir / "content/en/boilerplates").resolve()
    boilerplate = _repo_relative_file(boilerplate_root, relative)
    if boilerplate is None:
        return _shortcode_marker("boilerplate", arguments)
    if boilerplate in active_files or depth > 8:
        return f"[boilerplate recursion blocked: {name}]"
    try:
        raw = boilerplate.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return _shortcode_marker("boilerplate", arguments)
    raw = re.sub(r"^---\r?\n.*?\r?\n---\r?\n?", "", raw, count=1, flags=re.DOTALL)
    rendered = _render_istio_shortcodes(
        raw,
        repo_dir,
        depth=depth + 1,
        active_files=active_files | {boilerplate},
    ).strip()
    return f"\n\n{rendered}\n\n" if rendered else ""


def _matching_shortcode_close(
    tokens: list[_ShortcodeToken],
    opening_index: int,
    name: str,
) -> int | None:
    nested = 0
    for index in range(opening_index + 1, len(tokens)):
        candidate_name, _, closing = _shortcode_parts(tokens[index].body)
        if candidate_name != name:
            continue
        if closing:
            if nested == 0:
                return index
            nested -= 1
        else:
            nested += 1
    return None


def _render_istio_shortcode(
    name: str,
    arguments: str,
    inner: str,
    repo_dir: Path,
    *,
    depth: int,
    active_files: frozenset[Path],
) -> str:
    if "{{" in arguments:
        arguments = _render_istio_shortcodes(
            arguments,
            repo_dir,
            depth=depth + 1,
            active_files=active_files,
        )
    if name == "text":
        language, _ = _extract_shortcode_language(arguments)
        return _render_fenced_shortcode(language, inner)
    if name == "text_import":
        return _render_text_import(
            arguments,
            repo_dir,
            depth=depth,
            active_files=active_files,
        )
    if name == "include":
        return _render_include(
            arguments,
            repo_dir,
            depth=depth,
            active_files=active_files,
        )
    if name == "boilerplate":
        return _render_boilerplate(
            arguments,
            repo_dir,
            depth=depth,
            active_files=active_files,
        )
    if name in ISTIO_ADMONITION_SHORTCODES:
        positional, named = _shortcode_arguments(arguments)
        title = named.get("title", "") or (positional[0] if positional else "")
        return format_admonition(name, title, inner)
    if name == "tabset":
        _, named = _shortcode_arguments(arguments)
        category = named.get("category-name", "")
        label = f"**Tabset ({category}):**" if category else ""
        return f"\n\n{label}\n\n{inner.strip()}\n\n" if label else f"\n\n{inner.strip()}\n\n"
    if name == "tab":
        positional, named = _shortcode_arguments(arguments)
        title = named.get("name", "") or named.get("title", "") or (positional[0] if positional else "")
        label = f"**Tab: {title}**" if title else "**Tab:**"
        return f"\n\n{label}\n\n{inner.strip()}\n\n"
    if name == "gloss":
        positional, _ = _shortcode_arguments(arguments)
        rendered = inner.strip()
        return rendered or (positional[0] if positional else "")
    if name == "image":
        positional, named = _shortcode_arguments(arguments)
        source = named.get("src", "") or named.get("link", "") or (positional[0] if positional else "")
        caption = named.get("caption", "") or named.get("alt", "") or named.get("title", "")
        if source:
            return f"\n\n![{' '.join(caption.split())}]({source})\n\n"
        return _shortcode_marker(name, arguments)
    if name in {"github_tree", "github_blob", "github_file"}:
        # The source shortcode is normally followed by ``/path`` in the
        # surrounding Markdown or shell command.  Render only the immutable
        # base here so that that path, query, and fragment remain byte-for-byte
        # intact for the subsequent link pass.
        if name == "github_tree":
            return f"{ISTIO_APPLICATION_REPO}/tree/{ISTIO_APPLICATION_COMMIT}"
        if name == "github_blob":
            return f"{ISTIO_APPLICATION_REPO}/blob/{ISTIO_APPLICATION_COMMIT}"
        return f"https://raw.githubusercontent.com/istio/istio/{ISTIO_APPLICATION_COMMIT}"
    if name == "istio_release_url":
        return ISTIO_RELEASE_URL
    # Paired but presentation-only containers retain their prose.  Unknown
    # arguments remain visible so future source changes do not silently vanish.
    return f"\n\n{_shortcode_marker(name, arguments)}\n\n{inner.strip()}\n\n"


def _mask_istio_literals(content: str) -> tuple[str, list[str], list[str]]:
    """Protect Markdown fences and inline code before parsing Istio tags."""

    masked, fenced = _mask_gitbook_fences(content)
    inline: list[str] = []

    def protect_inline(match: re.Match[str]) -> str:
        inline.append(match.group(0))
        return f"\x00ISTIO_INLINE_{len(inline) - 1}\x01"

    masked = re.sub(
        r"(?P<ticks>`+)(?P<body>[^`\n]*?)(?P=ticks)",
        protect_inline,
        masked,
    )
    return masked, fenced, inline


def _render_istio_shortcodes(
    content: str,
    repo_dir: Path,
    *,
    depth: int = 0,
    active_files: frozenset[Path] = frozenset(),
) -> str:
    """Render Istio's Hugo shortcodes into searchable, readable Markdown."""

    if depth > 10:
        deep_tokens = _iter_shortcode_tokens(content)
        if not deep_tokens:
            return content
        output: list[str] = []
        cursor = 0
        for token in deep_tokens:
            output.append(content[cursor : token.start])
            output.append(_shortcode_marker(*_shortcode_parts(token.body)[:2]))
            cursor = token.end
        output.append(content[cursor:])
        return "".join(output)

    def replace_escaped_shortcode_comment(match: re.Match[str]) -> str:
        name, arguments, closing = _shortcode_parts(match.group("body"))
        if not name:
            return _shortcode_marker("shortcode", arguments)
        return _shortcode_marker(name, arguments)

    masked, fenced, inline = _mask_istio_literals(content)

    # Istio uses escaped shortcode comments in its shortcode documentation to
    # show source syntax without executing it.  Keep those examples readable,
    # while ordinary Hugo comments remain intentionally hidden.
    text = re.sub(
        r"\{\{[<%]/\*(?P<body>.*?)\*/[>%]\}\}",
        replace_escaped_shortcode_comment,
        masked,
        flags=re.DOTALL,
    )
    text = re.sub(r"\{\{/\*.*?\*/\}\}", "", text, flags=re.DOTALL)
    text = re.sub(
        r"\{\{[<%]\s*comment\s*[>%]\}\}.*?\{\{[<%]\s*/comment\s*[>%]\}\}",
        "",
        text,
        flags=re.DOTALL | re.IGNORECASE,
    )
    tokens = _iter_shortcode_tokens(text)
    if not tokens:
        # A page may contain only ordinary Markdown.  Literal masking still
        # happened above, so restore those spans before returning; otherwise
        # the NUL sentinels would leak into the corpus whenever no shortcode
        # token was present.
        rendered = text

        def restore_inline_literal(match: re.Match[str]) -> str:
            index = int(match.group(1))
            # A parent shortcode renderer may have supplied this sentinel;
            # only the frame that created it owns its replacement value.
            return inline[index] if index < len(inline) else match.group(0)

        rendered = re.sub(
            r"\x00ISTIO_INLINE_(\d+)\x01",
            restore_inline_literal,
            rendered,
        )
        for index, fence in enumerate(fenced):
            rendered = rendered.replace(f"\x00GITBOOK_FENCE_{index}\x01", fence)
        return rendered

    output: list[str] = []
    cursor = 0
    index = 0
    while index < len(tokens):
        token = tokens[index]
        output.append(text[cursor : token.start])
        name, arguments, closing = _shortcode_parts(token.body)
        if not name:
            output.append(_shortcode_marker("shortcode", arguments))
            cursor = token.end
            index += 1
            continue
        if closing:
            # A closing tag is consumed by its matching opening tag.  An
            # unmatched generic close carries no useful prose of its own.
            cursor = token.end
            index += 1
            continue

        close_index = _matching_shortcode_close(tokens, index, name)
        if close_index is None:
            if name in {
                "text_import",
                "include",
                "boilerplate",
                "image",
                "github_tree",
                "github_blob",
                "github_file",
                "istio_release_url",
            }:
                output.append(
                    _render_istio_shortcode(
                        name,
                        arguments,
                        "",
                        repo_dir,
                        depth=depth,
                        active_files=active_files,
                    )
                )
            elif name in ISTIO_PAIRED_SHORTCODES:
                output.append(_shortcode_marker(name, arguments))
            else:
                output.append(_shortcode_marker(name, arguments))
            cursor = token.end
            index += 1
            continue

        close_token = tokens[close_index]
        inner = text[token.end : close_token.start]
        rendered_inner = _render_istio_shortcodes(
            inner,
            repo_dir,
            depth=depth + 1,
            active_files=active_files,
        )
        output.append(
            _render_istio_shortcode(
                name,
                arguments,
                rendered_inner,
                repo_dir,
                depth=depth,
                active_files=active_files,
            )
        )
        cursor = close_token.end
        index = close_index + 1
    output.append(text[cursor:])
    rendered = "".join(output)

    def restore_inline(match: re.Match[str]) -> str:
        index = int(match.group(1))
        # Nested shortcode frames can carry a parent sentinel through this
        # pass; leave it for the owning outer frame to restore.
        return inline[index] if index < len(inline) else match.group(0)

    rendered = re.sub(r"\x00ISTIO_INLINE_(\d+)\x01", restore_inline, rendered)
    for index, fence in enumerate(fenced):
        rendered = rendered.replace(f"\x00GITBOOK_FENCE_{index}\x01", fence)
    return rendered


@dataclass(frozen=True)
class _GitBookToken:
    body: str
    start: int
    end: int


def _gitbook_fence_marker(line: str) -> tuple[str, int, str] | None:
    """Return a Markdown fence marker, allowing blockquotes and 0-3 spaces."""

    match = re.match(
        r"^ {0,3}(?:>\s*)*(?P<marker>`{3,}|~{3,})(?P<rest>[^\r\n]*)(?:\r?\n|$)",
        line,
    )
    if match is None:
        return None
    marker = match.group("marker")
    return marker[0], len(marker), match.group("rest")


def _mask_gitbook_fences(content: str) -> tuple[str, list[str]]:
    """Replace fenced Markdown spans with sentinels before shortcode parsing.

    A sentinel lets a paired GitBook tag span a code fence while ensuring that
    every `{% ... %}` literal inside that fence remains byte-for-byte intact.
    """

    lines = content.splitlines(keepends=True)
    masked: list[str] = []
    protected: list[str] = []
    index = 0
    while index < len(lines):
        marker = _gitbook_fence_marker(lines[index])
        if marker is None:
            masked.append(lines[index])
            index += 1
            continue

        fence_char, fence_length, _ = marker
        fence_lines = [lines[index]]
        index += 1
        while index < len(lines):
            fence_lines.append(lines[index])
            candidate = _gitbook_fence_marker(lines[index])
            index += 1
            if (
                candidate is not None
                and candidate[0] == fence_char
                and candidate[1] >= fence_length
                and not candidate[2].strip()
            ):
                break
        protected.append("".join(fence_lines))
        masked.append(f"\x00GITBOOK_FENCE_{len(protected) - 1}\x01")
    return "".join(masked), protected


def _iter_gitbook_tokens(content: str) -> list[_GitBookToken]:
    """Scan GitBook `{% ... %}` tags, including whitespace-trimmed delimiters."""

    tokens: list[_GitBookToken] = []
    cursor = 0
    while True:
        match = re.search(r"(?<!\{)\{%-?", content[cursor:])
        if match is None:
            break
        start = cursor + match.start()
        body_start = cursor + match.end()
        close = content.find("%}", body_start)
        if close < 0:
            tokens.append(_GitBookToken(content[body_start:], start, len(content)))
            break
        body_end = close
        if body_end > body_start and content[body_end - 1] == "-":
            body_end -= 1
        tokens.append(_GitBookToken(content[body_start:body_end], start, close + 2))
        cursor = close + 2
    return tokens


def _gitbook_shortcode_parts(raw_body: str) -> tuple[str, str, bool]:
    """Return `(name, arguments, closing)` for a GitBook tag body."""

    body = raw_body.strip()
    closing = False
    if body.startswith("/"):
        closing = True
        body = body[1:].lstrip()
    elif body.lower().startswith("end"):
        remainder = body[3:]
        if remainder and (remainder[0].isspace() or re.match(r"[A-Za-z0-9_.-]", remainder[0])):
            closing = True
            body = remainder.lstrip()
    match = re.match(
        r"(?P<name>[A-Za-z0-9_.-]+)(?:[ \t]+(?P<args>.*?))?$",
        body,
        re.DOTALL,
    )
    if match is None:
        return "", body, closing
    return match.group("name").lower(), (match.group("args") or "").strip(), closing


def _matching_gitbook_close(
    tokens: list[_GitBookToken],
    opening_index: int,
    name: str,
) -> int | None:
    nested = 0
    for index in range(opening_index + 1, len(tokens)):
        candidate_name, _, closing = _gitbook_shortcode_parts(tokens[index].body)
        if candidate_name != name:
            continue
        if closing:
            if nested == 0:
                return index
            nested -= 1
        else:
            nested += 1
    return None


def _resolve_gitbook_include(repo_dir: Path, file_name: str) -> Path | None:
    """Resolve only files below the checkout's `.gitbook/includes` directory."""

    raw = file_name.strip().strip("\"'").replace("\\", "/")
    if not raw or raw.startswith("/") or re.match(r"^[A-Za-z]:/", raw):
        return None
    parts = [part for part in raw.split("/") if part not in {"", "."}]
    if ".." in parts:
        return None
    prefix = [".gitbook", "includes"]
    if parts[:2] == prefix:
        parts = parts[2:]
    if not parts:
        return None
    include_root = (repo_dir / ".gitbook" / "includes").resolve()
    return _safe_repo_file(include_root, include_root.joinpath(*parts))


def _render_gitbook_include(
    arguments: str,
    repo_dir: Path,
    *,
    depth: int,
    active_files: frozenset[Path],
) -> str:
    positional, named = _shortcode_arguments(arguments)
    file_name = (
        named.get("file", "")
        or named.get("src", "")
        or (positional[0] if positional else "")
    )
    included = _resolve_gitbook_include(repo_dir, file_name)
    if included is None or included.stat().st_size > 1_000_000:
        return _shortcode_marker("include", arguments)
    if included in active_files or depth > 8:
        return f"[include recursion blocked: {file_name}]"
    try:
        included_text = included.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return _shortcode_marker("include", arguments)
    included_text = re.sub(
        r"^---\r?\n.*?\r?\n---\r?\n?",
        "",
        included_text,
        count=1,
        flags=re.DOTALL,
    )
    rendered = _render_gitbook_shortcodes(
        included_text,
        repo_dir,
        depth=depth + 1,
        active_files=active_files | {included},
    ).strip()
    return f"\n\n{rendered}\n\n" if rendered else ""


def _render_gitbook_shortcode(
    name: str,
    arguments: str,
    inner: str,
    repo_dir: Path,
    *,
    depth: int,
    active_files: frozenset[Path],
) -> str:
    positional, named = _shortcode_arguments(arguments)
    if name == "hint":
        style = named.get("style", "info").lower()
        kind = {"info": "note", "warning": "warning"}.get(style, style or "note")
        return format_admonition(kind, named.get("title", ""), inner)
    if name in {"tabs", "stepper", "columns", "column"}:
        return f"\n\n{inner.strip()}\n\n" if inner.strip() else ""
    if name == "tab":
        title = named.get("title", "") or (positional[0] if positional else "")
        label = f"**Tab: {title}**" if title else "**Tab:**"
        return f"\n\n{label}\n\n{inner.strip()}\n\n"
    if name == "step":
        title = named.get("title", "") or (positional[0] if positional else "")
        label = f"**Step: {title}**" if title else "**Step**"
        return f"\n\n{label}\n\n{inner.strip()}\n\n"
    if name == "embed":
        url = named.get("url", "") or named.get("src", "") or (positional[0] if positional else "")
        caption = " ".join(inner.split()) or url
        return f"\n\n[{caption}]({url})\n\n" if url else _shortcode_marker(name, arguments)
    if name == "content-ref":
        url = named.get("url", "") or named.get("src", "") or (positional[0] if positional else "")
        caption = " ".join(inner.split()) or named.get("title", "") or url
        return f"\n\n[{caption}]({url})\n\n" if url else _shortcode_marker(name, arguments)
    if name == "code":
        language = named.get("language", "") or named.get("lang", "") or named.get("syntax", "")
        if not language and positional:
            language = positional[0]
        rendered = _render_fenced_shortcode(language, inner)
        title = named.get("title", "")
        return f"\n\n**Code: {title}**\n{rendered}" if title else rendered
    if name == "file":
        url = named.get("src", "") or named.get("url", "") or (positional[0] if positional else "")
        caption = " ".join(inner.split()) or named.get("title", "") or url
        return f"\n\n[{caption}]({url})\n\n" if url else _shortcode_marker(name, arguments)
    if name == "include":
        return _render_gitbook_include(
            arguments,
            repo_dir,
            depth=depth,
            active_files=active_files,
        )
    marker = _shortcode_marker(name, arguments)
    if inner.strip():
        return f"\n\n{marker}\n\n{inner.strip()}\n\n"
    return f"\n\n{marker}\n\n"


def _render_gitbook_segment(
    content: str,
    repo_dir: Path,
    *,
    depth: int,
    active_files: frozenset[Path],
) -> str:
    tokens = _iter_gitbook_tokens(content)
    if not tokens:
        return content
    output: list[str] = []
    cursor = 0
    index = 0
    while index < len(tokens):
        token = tokens[index]
        output.append(content[cursor : token.start])
        name, arguments, closing = _gitbook_shortcode_parts(token.body)
        if not name:
            output.append(_shortcode_marker("gitbook", arguments))
            cursor = token.end
            index += 1
            continue
        if closing:
            output.append(_shortcode_marker(f"end{name}", arguments))
            cursor = token.end
            index += 1
            continue
        close_index = _matching_gitbook_close(tokens, index, name)
        if close_index is None:
            output.append(
                _render_gitbook_shortcode(
                    name,
                    arguments,
                    "",
                    repo_dir,
                    depth=depth,
                    active_files=active_files,
                )
            )
            cursor = token.end
            index += 1
            continue
        close_token = tokens[close_index]
        inner = _render_gitbook_shortcodes(
            content[token.end : close_token.start],
            repo_dir,
            depth=depth + 1,
            active_files=active_files,
        )
        output.append(
            _render_gitbook_shortcode(
                name,
                arguments,
                inner,
                repo_dir,
                depth=depth,
                active_files=active_files,
            )
        )
        cursor = close_token.end
        index = close_index + 1
    output.append(content[cursor:])
    return "".join(output)


def _render_gitbook_shortcodes(
    content: str,
    repo_dir: Path,
    *,
    depth: int = 0,
    active_files: frozenset[Path] = frozenset(),
) -> str:
    masked, protected = _mask_gitbook_fences(content)
    rendered = _render_gitbook_segment(
        masked,
        repo_dir,
        depth=depth,
        active_files=active_files,
    )
    for index, fence in enumerate(protected):
        rendered = rendered.replace(f"\x00GITBOOK_FENCE_{index}\x01", fence)
    return rendered


# ---------------------------------------------------------------------------
# OpenSearch documentation-website Jekyll renderer
# ---------------------------------------------------------------------------

# The OpenSearch documentation site uses a small, deliberately boring subset
# of Liquid in page bodies.  Keeping the implementation here (instead of
# adding a general-purpose template engine) makes the air-gapped build
# deterministic and gives us a place to enforce the source trust boundary.
JEKYLL_INCLUDE_ALLOWLIST = frozenset(
    {"copy-curl.html", "copy.html", "cards.html", "list.html", "youtube-player.html"}
)
JEKYLL_SITE_ALLOWLIST = frozenset(
    {
        "url",
        "baseurl",
        "opensearch_version",
        "opensearch_major_minor_version",
        "opensearch_dashboards_version",
        "lucene_version",
    }
)
JEKYLL_SITE_OVERRIDE_ALLOWLIST = frozenset(
    {
        # Keep overrides deliberately narrower than arbitrary Liquid context.
        # These are the version/origin values that the source manifests may
        # pin for an application-specific documentation snapshot.
        "url",
        "baseurl",
        "opensearch_version",
        "opensearch_major_minor_version",
        "opensearch_dashboards_version",
        "lucene_version",
    }
)
JEKYLL_DEFAULT_SITE = {
    "url": "https://docs.opensearch.org",
    "baseurl": "/latest",
    "opensearch_version": "2.19.6",
    "opensearch_major_minor_version": "2.19",
    "opensearch_dashboards_version": "2.19.6",
    "lucene_version": "9_12_0",
}


class JekyllRenderError(ValueError):
    """Raised when a page uses Liquid outside the supported profile."""

    def __init__(self, message: str, source_path: Path | None = None, line: int | None = None):
        self.source_path = source_path
        self.line = line
        location = ""
        if source_path is not None:
            location = f"{source_path}"
            if line is not None:
                location += f":{line}"
            location += ": "
        super().__init__(location + message)


@dataclass(frozen=True)
class _JekyllPage:
    file_path: Path
    repo_rel_path: str
    metadata: dict[str, Any]
    collection: str
    route: str
    canonical_url: str
    canonical_route: str
    permalink: str
    redirect_aliases: tuple[str, ...]
    output_rel_path: str
    canonical_collision: bool = False


@dataclass
class _JekyllRegistry:
    manifest: Manifest
    pages: list[_JekyllPage]
    by_source: dict[str, _JekyllPage]
    by_route: dict[str, list[_JekyllPage]]
    by_alias: dict[str, list[_JekyllPage]]

    @property
    def unique_routes(self) -> int:
        return len(self.by_route)

    @property
    def route_collisions(self) -> dict[str, list[_JekyllPage]]:
        return {route: pages for route, pages in self.by_route.items() if len(pages) > 1}


_LIQUID_BLOCK_PATTERN = re.compile(
    r"\{%-?\s*(?P<body>.*?)\s*-?%\}",
    re.DOTALL,
)
_LIQUID_OUTPUT_PATTERN = re.compile(
    r"(?<!\{)\{\{\-?\s*(?P<body>.*?)\s*\-?\}\}(?!\})",
    re.DOTALL,
)
_LIQUID_LITERAL_MUSTACHE_PATTERN = re.compile(r"\{\{\{.*?\}\}\}", re.DOTALL)
_JYAML_KEY_PATTERN = re.compile(r"^(?P<key>[A-Za-z_][A-Za-z0-9_-]*)\s*:", re.MULTILINE)


def _yaml_scalar_fallback(value: str) -> Any:
    """Parse the small scalar subset needed when PyYAML is unavailable."""

    value = value.strip()
    if not value:
        return None
    if value in {"true", "True", "TRUE"}:
        return True
    if value in {"false", "False", "FALSE"}:
        return False
    if value in {"null", "Null", "NULL", "~"}:
        return None
    try:
        return json.loads(value)
    except (TypeError, json.JSONDecodeError):
        pass
    if (value.startswith("'") and value.endswith("'")) or (
        value.startswith('"') and value.endswith('"')
    ):
        return value[1:-1]
    return value


def _parse_yaml_mapping(raw_yaml: str) -> dict[str, Any]:
    """Load source YAML without making the profile depend on a new package."""

    try:
        import yaml

        parsed = yaml.safe_load(raw_yaml)
    except (ImportError, OSError, ValueError):
        parsed = None
    if isinstance(parsed, dict):
        return dict(parsed)

    # This fallback intentionally only handles top-level values.  The normal
    # builder environment installs PyYAML (it is already in requirements.txt),
    # while this path still gives useful title/version behaviour in a minimal
    # standard-library test environment.
    result: dict[str, Any] = {}
    lines = raw_yaml.replace("\r\n", "\n").replace("\r", "\n").splitlines()
    current_key: str | None = None
    current_lines: list[str] = []
    for line in lines + [""]:
        key_match = re.match(r"^(?P<key>[A-Za-z_][A-Za-z0-9_-]*)\s*:\s*(?P<value>.*)$", line)
        if key_match and not line.startswith((" ", "\t")):
            if current_key is not None:
                result[current_key] = _yaml_scalar_fallback("\n".join(current_lines))
            current_key = key_match.group("key")
            current_lines = [key_match.group("value")]
        elif current_key is not None:
            current_lines.append(line.strip())
    if current_key is not None and current_key not in result:
        result[current_key] = _yaml_scalar_fallback("\n".join(current_lines))
    return result


def parse_jekyll_frontmatter(content: str, default_title: str = "") -> tuple[dict[str, Any], str]:
    """Return complete page data and body from a Jekyll Markdown document."""

    match = FRONTMATTER_PATTERN.match(content)
    if match is None:
        metadata: dict[str, Any] = {}
        body = content
    else:
        metadata = _parse_yaml_mapping(match.group(1))
        body = content[match.end() :]
    if not str(metadata.get("title", "") or "").strip():
        heading = HEADING1_PATTERN.search(body)
        metadata["title"] = heading.group(1).strip() if heading else default_title
    return metadata, body


def _jekyll_fence_marker(line: str) -> tuple[str, int, int, str] | None:
    """Return ``(char, length, indentation, rest)`` for a Markdown fence."""

    match = re.match(
        r"^(?P<indent> *)(?P<quotes>(?:>\s*)*)(?P<marker>`{3,}|~{3,})(?P<rest>[^\r\n]*)(?:\r?\n|$)",
        line,
    )
    if match is None:
        return None
    return (
        match.group("marker")[0],
        len(match.group("marker")),
        len(match.group("indent")),
        match.group("rest"),
    )


def _mask_jekyll_fences(content: str) -> tuple[str, list[str]]:
    """Mask fenced spans while allowing only safe ``site.*`` rendering later."""

    lines = content.splitlines(keepends=True)
    masked: list[str] = []
    protected: list[str] = []
    index = 0
    while index < len(lines):
        marker = _jekyll_fence_marker(lines[index])
        if marker is None:
            masked.append(lines[index])
            index += 1
            continue
        char, length, indentation, _ = marker
        # A line with a same-line closing marker is an inline code span, not a
        # block-fence opener. Keep it as normal text so it cannot hide all
        # following prose from Liquid/link passes.
        if re.search(re.escape(char) * length + r"\s*$", marker[3]):
            masked.append(lines[index])
            index += 1
            continue
        fence_lines = [lines[index]]
        index += 1
        while index < len(lines):
            candidate_line = lines[index]
            candidate = _jekyll_fence_marker(candidate_line)
            if (
                candidate is not None
                and candidate[0] == char
                and candidate[1] >= length
                and candidate[3].strip() == ""
                # A fence nested below an ordered/bulleted list commonly has
                # one extra indentation column on its closing line.  Kramdown
                # accepts up to three columns of container indentation; use
                # that allowance while still keeping a top-level 4-space code
                # block from closing a top-level fence accidentally.
                and candidate[2] <= indentation + 3
            ):
                fence_lines.append(candidate_line)
                index += 1
                break
            # A fixed-source page has one known malformed JSON fence followed
            # by a real Markdown heading. Treat a heading after a blank line as
            # the implicit boundary so subsequent prose is not hidden in the
            # code span. An unclosed fence without that structural boundary
            # remains protected through EOF.
            if (
                candidate is None
                and fence_lines
                and not fence_lines[-1].strip()
                # A single ``#`` is commonly a language comment inside the
                # malformed block (for example ``# Array of hosts`` in a
                # Python snippet).  Only a structural second-level-or-deeper
                # heading may delimit the known malformed JSON fence.
                and re.match(r"^ {0,3}#{2,6}\s", candidate_line)
            ):
                break
            fence_lines.append(candidate_line)
            index += 1
        protected.append("".join(fence_lines))
        masked.append(f"\x00JEKYLL_FENCE_{len(protected) - 1}\x01")
    return "".join(masked), protected


def _unmask_jekyll_fences(text: str, protected: list[str]) -> str:
    for index, fence in enumerate(protected):
        text = text.replace(f"\x00JEKYLL_FENCE_{index}\x01", fence)
    return text


def _split_jekyll_filters(expression: str) -> list[str]:
    """Split a Liquid expression at unquoted pipe characters."""

    parts: list[str] = []
    start = 0
    quote: str | None = None
    escaped = False
    for index, char in enumerate(expression):
        if escaped:
            escaped = False
        elif char == "\\" and quote:
            escaped = True
        elif quote:
            if char == quote:
                quote = None
        elif char in {"'", '"'}:
            quote = char
        elif char == "|":
            parts.append(expression[start:index].strip())
            start = index + 1
    parts.append(expression[start:].strip())
    return parts


def _liquid_arguments(raw: str) -> list[str]:
    raw = raw.strip()
    if not raw:
        return []
    if raw.startswith(":"):
        raw = raw[1:].lstrip()
    try:
        return shlex.split(raw, posix=True)
    except ValueError as error:
        raise JekyllRenderError(f"invalid Liquid filter arguments: {raw!r}") from error


def _liquid_string(value: Any) -> str:
    if value is None:
        return ""
    if value is True:
        return "true"
    if value is False:
        return "false"
    if isinstance(value, (list, tuple)):
        return " ".join(_liquid_string(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, separators=(",", ":"))
    return str(value)


def _liquid_path_parts(value: str) -> list[str | int]:
    if not re.match(r"^[A-Za-z_]", value.strip()):
        return []
    parts: list[str | int] = []
    for match in re.finditer(r"(?:^|\.)([A-Za-z_][A-Za-z0-9_-]*)|\[\s*(['\"]?)([^\]\"']+)\2\s*\]", value):
        if match.group(1) is not None:
            parts.append(match.group(1))
        else:
            raw = match.group(3).strip()
            parts.append(int(raw) if raw.isdigit() else raw)
    return parts


def _liquid_lookup(value: str, context: dict[str, Any], *, strict: bool = True) -> Any:
    value = value.strip()
    literal = _yaml_scalar_fallback(value)
    if value and (
        (value[0] in {"'", '"'} and value[-1:] == value[0])
        or value in {"true", "false", "nil", "null", "blank", "empty"}
        or re.fullmatch(r"-?\d+(?:\.\d+)?", value)
    ):
        return literal
    parts = _liquid_path_parts(value)
    if not parts:
        if strict:
            raise JekyllRenderError(f"undefined Liquid variable: {value!r}")
        return ""
    current: Any = context
    for part in parts:
        if isinstance(part, int):
            if not isinstance(current, (list, tuple)) or part >= len(current):
                if strict:
                    raise JekyllRenderError(f"undefined Liquid variable: {value!r}")
                return ""
            current = current[part]
        elif isinstance(current, dict) and part in current:
            current = current[part]
        else:
            if strict:
                raise JekyllRenderError(f"undefined Liquid variable: {value!r}")
            return ""
    return current


def _evaluate_liquid_expression(expression: str, context: dict[str, Any]) -> Any:
    parts = _split_jekyll_filters(expression)
    value = _liquid_lookup(parts[0], context)
    for filter_part in parts[1:]:
        match = re.match(r"^(?P<name>[A-Za-z_][A-Za-z0-9_-]*)\s*(?::\s*(?P<args>.*))?$", filter_part, re.DOTALL)
        if match is None:
            raise JekyllRenderError(f"invalid Liquid filter: {filter_part!r}")
        name = match.group("name").lower()
        args = _liquid_arguments(match.group("args") or "")
        def filter_value(arg: str) -> Any:
            # ``shlex`` removes quotes from filter arguments.  A token that is
            # not a variable path is therefore a literal string (for example
            # the ``"."`` in ``split: "."``).
            if _liquid_path_parts(arg):
                return _liquid_lookup(arg, context)
            return _yaml_scalar_fallback(arg)

        values = [filter_value(arg) for arg in args]
        if name == "split":
            value = _liquid_string(value).split(_liquid_string(values[0] if values else ""))
        elif name == "append":
            value = _liquid_string(value) + _liquid_string(values[0] if values else "")
        elif name == "prepend":
            value = _liquid_string(values[0] if values else "") + _liquid_string(value)
        elif name == "first":
            value = value[0] if isinstance(value, (list, tuple)) and value else ""
        elif name == "last":
            value = value[-1] if isinstance(value, (list, tuple)) and value else ""
        elif name == "join":
            value = _liquid_string(values[0] if values else "").join(_liquid_string(item) for item in value)
        elif name == "replace":
            old = _liquid_string(values[0] if values else "")
            new = _liquid_string(values[1] if len(values) > 1 else "")
            value = _liquid_string(value).replace(old, new)
        elif name == "default":
            if value in {None, "", False, []}:
                value = values[0] if values else ""
        elif name == "strip_html":
            value = re.sub(r"<[^>]+>", "", _liquid_string(value))
        elif name == "markdownify":
            # Include descriptions use this filter.  The source descriptions
            # are already Markdown/plain text, so preserve text and remove
            # only presentation tags that would not be searchable.
            value = re.sub(r"<[^>]+>", "", _liquid_string(value))
        elif name == "escape":
            value = html.escape(_liquid_string(value))
        else:
            raise JekyllRenderError(f"unsupported Liquid filter: {name!r}")
    return value


def _liquid_line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


_JEKYLL_RAW_TAG_PATTERN = re.compile(
    r"\{%-?\s*(?P<name>raw|endraw)\s*-?%\}",
    re.IGNORECASE,
)


def _protect_jekyll_raw_blocks(
    text: str,
    *,
    source_path: Path | None = None,
    line_offset: int = 0,
) -> tuple[str, list[str]]:
    """Remove Jekyll raw wrappers while protecting their literal contents.

    Fenced pages need a separate pass because only ``site.*`` expressions are
    evaluated there.  A raw block must therefore be replaced with a sentinel
    before that pass, otherwise a literal ``{{ site.foo }}`` would be rendered
    accidentally.  Treat malformed or nested wrappers as an error instead of
    silently leaking template syntax into the corpus.
    """

    output: list[str] = []
    literals: list[str] = []
    cursor = 0
    open_tag: re.Match[str] | None = None
    for match in _JEKYLL_RAW_TAG_PATTERN.finditer(text):
        name = match.group("name").lower()
        if name == "raw":
            if open_tag is not None:
                line = line_offset + _liquid_line_number(text, match.start())
                raise JekyllRenderError("nested raw/endraw block", source_path, line)
            output.append(text[cursor : match.start()])
            open_tag = match
            cursor = match.end()
            continue

        if open_tag is None:
            line = line_offset + _liquid_line_number(text, match.start())
            raise JekyllRenderError("unmatched raw/endraw block", source_path, line)
        literals.append(text[open_tag.end() : match.start()])
        output.append(f"\x00JEKYLL_RAW_LITERAL_{len(literals) - 1}\x01")
        cursor = match.end()
        open_tag = None

    if open_tag is not None:
        line = line_offset + _liquid_line_number(text, open_tag.start())
        raise JekyllRenderError("unmatched raw/endraw block", source_path, line)
    output.append(text[cursor:])
    return "".join(output), literals


def _restore_jekyll_raw_blocks(text: str, literals: list[str]) -> str:
    for index, literal in enumerate(literals):
        text = text.replace(f"\x00JEKYLL_RAW_LITERAL_{index}\x01", literal)
    return text


def _render_jekyll_fence(
    text: str,
    context: dict[str, Any],
    *,
    source_path: Path | None = None,
) -> str:
    """Render allowlisted site expressions in one fence.

    The fence itself remains literal Markdown.  Only site expressions outside
    explicit raw spans are evaluated; raw wrappers are stripped while their
    inner text is restored byte-for-byte.
    """

    protected, literals = _protect_jekyll_raw_blocks(text, source_path=source_path)
    rendered = _render_site_expressions(protected, context, strict=True)
    return _restore_jekyll_raw_blocks(rendered, literals)


def _render_site_expressions(text: str, context: dict[str, Any], *, strict: bool = True) -> str:
    """Render only allowlisted ``site.*`` expressions in a fenced span."""

    def replace(match: re.Match[str]) -> str:
        expression = match.group("body").strip()
        first = _split_jekyll_filters(expression)[0]
        if not first.startswith("site."):
            return match.group(0)
        try:
            value = _evaluate_liquid_expression(expression, context)
        except JekyllRenderError:
            if strict:
                raise
            return match.group(0)
        return _liquid_string(value)

    return _LIQUID_OUTPUT_PATTERN.sub(replace, text)


def _resolve_jekyll_include_path(repo_dir: Path, name: str) -> Path:
    raw = name.strip().strip("\"'").replace("\\", "/")
    if raw not in JEKYLL_INCLUDE_ALLOWLIST:
        raise JekyllRenderError(
            f"include is not in the direct allowlist: {name!r}; allowed={sorted(JEKYLL_INCLUDE_ALLOWLIST)}"
        )
    if any(part in {"", ".", ".."} for part in raw.split("/")) or "/" in raw:
        raise JekyllRenderError(f"include path traversal rejected: {name!r}")
    include_root = (repo_dir / "_includes").resolve()
    resolved = _safe_repo_file(repo_dir, include_root / raw)
    if resolved is None or resolved.parent != include_root:
        raise JekyllRenderError(f"include file is missing or outside _includes: {name!r}")
    if resolved.stat().st_size > 1_000_000:
        raise JekyllRenderError(f"include file is too large: {name!r}")
    return resolved


def _parse_jekyll_include_arguments(raw: str, context: dict[str, Any]) -> dict[str, Any]:
    try:
        tokens = shlex.split(raw, posix=True)
    except ValueError as error:
        raise JekyllRenderError(f"invalid include arguments: {raw!r}") from error
    result: dict[str, Any] = {}
    for token in tokens:
        match = re.match(r"^(?P<key>[A-Za-z_][A-Za-z0-9_-]*)=(?P<value>.*)$", token, re.DOTALL)
        if match is None:
            raise JekyllRenderError(f"include argument must be key=value: {token!r}")
        key = match.group("key")
        value = match.group("value")
        path_parts = _liquid_path_parts(value)
        if path_parts and (
            value in context
            or value.startswith(("page.", "site.", "include."))
        ):
            result[key] = _liquid_lookup(value, context)
        else:
            result[key] = _yaml_scalar_fallback(value)
    return result


def _plain_include_text(value: Any) -> str:
    return re.sub(r"<[^>]+>", "", _liquid_string(value)).strip()


def _render_jekyll_include(
    name: str,
    arguments: str,
    repo_dir: Path,
    context: dict[str, Any],
    *,
    active_includes: frozenset[str],
) -> str:
    normalized_name = name.strip().strip("\"'")
    if normalized_name in active_includes:
        return f"\n\n[include recursion blocked: {normalized_name}]\n\n"
    include_path = _resolve_jekyll_include_path(repo_dir, normalized_name)
    # Reading the file verifies sparse-checkout and source provenance.  The
    # profile renders the five known templates semantically rather than
    # interpreting arbitrary Liquid from a repository file.
    try:
        include_source = include_path.read_text(encoding="utf-8", errors="replace")
    except OSError as error:
        raise JekyllRenderError(f"cannot read include {normalized_name!r}: {error}") from error
    nested = re.findall(r"\{%-?\s*include\s+([^%]+?)\s*-?%\}", include_source)
    for nested_name in nested:
        nested_name = nested_name.strip().split()[0].strip("\"'")
        if nested_name in active_includes or nested_name == normalized_name:
            return f"\n\n[include recursion blocked: {nested_name}]\n\n"
        if nested_name not in JEKYLL_INCLUDE_ALLOWLIST:
            raise JekyllRenderError(f"nested include is not allowlisted: {nested_name!r}")
    include_context = dict(context)
    include_context["include"] = _parse_jekyll_include_arguments(arguments, context)
    values = include_context["include"]
    if normalized_name in {"copy.html", "copy-curl.html"}:
        unknown = set(values) - set()
        if unknown:
            raise JekyllRenderError(f"unexpected arguments for {normalized_name}: {sorted(unknown)}")
        return ""
    if normalized_name == "cards.html":
        unknown = set(values) - {"cards", "documentation_link"}
        if unknown or "cards" not in values:
            raise JekyllRenderError(
                f"cards include requires cards and accepts documentation_link; unexpected={sorted(unknown)}"
            )
        cards = values["cards"]
        if not isinstance(cards, (list, tuple)):
            raise JekyllRenderError("cards include argument must be a list")
        output: list[str] = ["", "<div class=\"card-container\">", ""]
        for card in cards:
            if not isinstance(card, dict):
                raise JekyllRenderError("cards include entries must be mappings")
            heading = _plain_include_text(card.get("heading", ""))
            if not heading:
                raise JekyllRenderError("cards include entry is missing heading")
            link = _liquid_string(card.get("link", "")).strip()
            label = f"[{heading}]({link})" if link else heading
            output.append(f"- {label}")
            description = _plain_include_text(card.get("description", ""))
            if description:
                output.append(f"  {description}")
            items = card.get("list")
            if isinstance(items, (list, tuple)):
                output.extend(f"  - {_plain_include_text(item)}" for item in items)
            if values.get("documentation_link"):
                output.append("  Documentation →")
            output.append("")
        output.extend(["</div>", ""])
        return "\n".join(output)
    if normalized_name == "list.html":
        unknown = set(values) - {"list_title", "list_items"}
        if unknown or "list_items" not in values:
            raise JekyllRenderError(
                f"list include requires list_items and accepts list_title; unexpected={sorted(unknown)}"
            )
        items = values["list_items"]
        if not isinstance(items, (list, tuple)):
            raise JekyllRenderError("list include argument must be a list")
        output = [""]
        if values.get("list_title"):
            output.append(f"**{_plain_include_text(values['list_title'])}**")
            output.append("")
        for index, item in enumerate(items, 1):
            if not isinstance(item, dict):
                raise JekyllRenderError("list include entries must be mappings")
            heading = _plain_include_text(item.get("heading", ""))
            if not heading:
                raise JekyllRenderError("list include entry is missing heading")
            link = _liquid_string(item.get("link", "")).strip()
            label = f"[{heading}]({link})" if link else heading
            output.append(f"{index}. {label}")
            description = _plain_include_text(item.get("description", ""))
            if description:
                output.append(f"   {description}")
        output.append("")
        return "\n".join(output)
    if normalized_name == "youtube-player.html":
        unknown = set(values) - {"id"}
        if unknown or not values.get("id"):
            raise JekyllRenderError(
                f"youtube-player include requires id; unexpected={sorted(unknown)}"
            )
        video_id = html.escape(_liquid_string(values["id"]), quote=True)
        return (
            '\n\n<div class="embed-container">\n'
            f'  <iframe src="https://www.youtube.com/embed/{video_id}" '
            'width="640" height="385" frameborder="0" allowfullscreen="true"></iframe>\n'
            "</div>\n\n"
        )
    raise JekyllRenderError(f"unhandled Jekyll include: {normalized_name!r}")


def _is_literal_jekyll_output(expression: str) -> bool:
    """Recognize template examples that are intentionally not Liquid."""

    expression = expression.strip()
    return bool(
        expression.startswith(("#", "/", "^", "!", ">", "range ", "with ", "end "))
        or expression.startswith("/")
        or ("{{" in expression and expression.endswith("}}"))
    )


def _liquid_expression_root(expression: str) -> str | None:
    """Return the leading variable name of a Liquid output expression."""

    primary = _split_jekyll_filters(expression)[0].strip()
    match = re.match(r"(?P<root>[A-Za-z_][A-Za-z0-9_-]*)", primary)
    return match.group("root") if match is not None else None


def _render_jekyll_segment(
    text: str,
    repo_dir: Path,
    context: dict[str, Any],
    *,
    source_path: Path | None,
    active_includes: frozenset[str] = frozenset(),
) -> str:
    """Render non-fenced page text, failing closed on unknown Liquid."""

    protected_literals: list[str] = []

    def protect_literal(match: re.Match[str]) -> str:
        protected_literals.append(match.group(0))
        return f"\x00JEKYLL_LITERAL_{len(protected_literals) - 1}\x01"

    # Triple braces are Mustache/Handlebars examples, never an output tag.
    text = _LIQUID_LITERAL_MUSTACHE_PATTERN.sub(protect_literal, text)

    def protect_raw(match: re.Match[str]) -> str:
        protected_literals.append(match.group("inner"))
        return f"\x00JEKYLL_LITERAL_{len(protected_literals) - 1}\x01"

    raw_pattern = re.compile(
        r"\{%-?\s*raw\s*-?%\}(?P<inner>.*?)\{%-?\s*endraw\s*-?%\}",
        re.DOTALL | re.IGNORECASE,
    )
    text = raw_pattern.sub(protect_raw, text)
    if re.search(r"\{%-?\s*(?:raw|endraw)\b", text, re.IGNORECASE):
        raise JekyllRenderError("unmatched raw/endraw block", source_path)

    # Inline code is a literal context just like a fenced block.  Protect it
    # before evaluating Liquid so examples such as ``{{page.title}}`` remain
    # examples while the same expression in prose is rendered.
    text = re.sub(
        r"(?P<ticks>`+)(?P<body>[^`\n]*?)(?P=ticks)",
        protect_literal,
        text,
    )

    comment_pattern = re.compile(
        r"\{%-?\s*comment\s*-?%\}.*?\{%-?\s*endcomment\s*-?%\}",
        re.DOTALL | re.IGNORECASE,
    )
    text = comment_pattern.sub("", text)
    if re.search(r"\{%-?\s*(?:comment|endcomment)\b", text, re.IGNORECASE):
        raise JekyllRenderError("unmatched comment/endcomment block", source_path)

    # Assignments are deliberately evaluated in source order.  This covers
    # the version_parts/major_version_mask pattern used by OpenSearch RPM
    # instructions and makes undefined variables fail before any output is
    # written to the corpus.
    assign_pattern = re.compile(
        r"\{%-?\s*assign\s+(?P<name>[A-Za-z_][A-Za-z0-9_-]*)\s*=\s*(?P<expr>.*?)\s*-?%\}",
        re.DOTALL | re.IGNORECASE,
    )

    def assign(match: re.Match[str]) -> str:
        expression = match.group("expr").strip()
        try:
            context[match.group("name")] = _evaluate_liquid_expression(expression, context)
        except JekyllRenderError as error:
            raise JekyllRenderError(str(error), source_path, _liquid_line_number(text, match.start())) from error
        return ""

    text = assign_pattern.sub(assign, text)

    include_pattern = re.compile(
        r"\{%-?\s*include\s+(?P<name>[^%\s]+)(?:\s+(?P<args>.*?))?\s*-?%\}",
        re.DOTALL | re.IGNORECASE,
    )

    def include(match: re.Match[str]) -> str:
        try:
            return _render_jekyll_include(
                match.group("name"),
                match.group("args") or "",
                repo_dir,
                context,
                active_includes=active_includes,
            )
        except JekyllRenderError as error:
            raise JekyllRenderError(str(error), source_path, _liquid_line_number(text, match.start())) from error

    text = include_pattern.sub(include, text)

    def output(match: re.Match[str]) -> str:
        expression = match.group("body").strip()
        root = _liquid_expression_root(expression)
        if _is_literal_jekyll_output(expression) or (
            not any(char.isspace() for char in expression)
            and root not in context
        ):
            return match.group(0)
        try:
            return _liquid_string(_evaluate_liquid_expression(expression, context))
        except JekyllRenderError as error:
            raise JekyllRenderError(str(error), source_path, _liquid_line_number(text, match.start())) from error

    text = _LIQUID_OUTPUT_PATTERN.sub(output, text)
    residual = _LIQUID_BLOCK_PATTERN.search(text)
    if residual is not None:
        body = " ".join(residual.group("body").split())
        raise JekyllRenderError(f"unsupported Liquid block tag: {body!r}", source_path, _liquid_line_number(text, residual.start()))

    def restore(match: re.Match[str]) -> str:
        return protected_literals[int(match.group(1))]

    sentinel_pattern = re.compile(r"\x00JEKYLL_LITERAL_(\d+)\x01")
    # A raw span may contain a protected triple-Mustache literal. Restoring
    # the outer raw span exposes the inner sentinel, so expand the finite
    # protection stack until no internal marker remains.
    for _ in range(len(protected_literals) + 1):
        if sentinel_pattern.search(text) is None:
            return text
        text = sentinel_pattern.sub(restore, text)
    raise JekyllRenderError("Jekyll literal restoration did not converge", source_path)


def normalize_jekyll_ial(body: str) -> str:
    """Keep Kramdown classes/attributes and normalize presentation wrappers."""

    masked, protected = _mask_jekyll_fences(body)

    def normalize_segment(segment: str) -> str:
        # ``nomarkdown`` is a Kramdown wrapper around inline HTML.  Its inner
        # HTML is useful corpus content, whereas the wrapper itself is not.
        segment = re.sub(r"\{::nomarkdown\}", "", segment, flags=re.IGNORECASE)
        segment = re.sub(r"\{:/\}", "", segment)
        segment = re.sub(r"(?m)^\s*\{:{1,2}toc\}\s*$", "<!-- local-toc -->", segment, flags=re.IGNORECASE)
        return segment

    normalized = normalize_segment(masked)
    return _unmask_jekyll_fences(normalized, protected)


def render_jekyll_template(
    content: str,
    repo_dir: Path,
    *,
    manifest: Manifest | None = None,
    page_data: dict[str, Any] | None = None,
    source_path: Path | None = None,
) -> str:
    """Render the supported OpenSearch Jekyll/Liquid page-body subset."""

    site = dict(JEKYLL_DEFAULT_SITE)
    if repo_dir.is_dir() and (repo_dir / "_config.yml").is_file():
        try:
            site.update(
                {
                    key: value
                    for key, value in _parse_yaml_mapping(
                        (repo_dir / "_config.yml").read_text(encoding="utf-8", errors="replace")
                    ).items()
                    if key in JEKYLL_SITE_ALLOWLIST and value is not None
                }
            )
        except OSError:
            pass
    if manifest is not None:
        overrides = manifest.site_overrides
        if not isinstance(overrides, dict):
            raise JekyllRenderError("site_overrides must be a mapping", source_path)
        disallowed = set(overrides) - JEKYLL_SITE_OVERRIDE_ALLOWLIST
        if disallowed:
            raise JekyllRenderError(
                f"site_overrides contains disallowed keys: {sorted(disallowed)}",
                source_path,
            )
        for key, value in overrides.items():
            if value is None or isinstance(value, (dict, list, tuple, set)):
                raise JekyllRenderError(
                    f"site_overrides.{key} must be a scalar value",
                    source_path,
                )
            site[key] = value
    context: dict[str, Any] = {"site": {key: site[key] for key in JEKYLL_SITE_ALLOWLIST if key in site}}
    context.update(page_data or {})
    context["page"] = page_data or {}
    masked, protected = _mask_jekyll_fences(content)

    def render_fence(match: re.Match[str]) -> str:
        index = int(match.group(1))
        return _render_jekyll_fence(
            protected[index],
            context,
            source_path=source_path,
        )

    rendered = _render_jekyll_segment(
        masked,
        repo_dir,
        context,
        source_path=source_path,
    )
    rendered = re.sub(r"\x00JEKYLL_FENCE_(\d+)\x01", render_fence, rendered)
    return normalize_jekyll_ial(rendered)


# Short aliases make the profile easy to exercise in focused tests and keep
# the source-specific API discoverable without changing the historical helper.
render_jekyll = render_jekyll_template
clean_jekyll = render_jekyll_template


def validate_no_residual_template_syntax(body: str) -> list[str]:
    """Return non-code Liquid/Kramdown residuals for corpus-wide validation."""

    masked, protected = _mask_jekyll_fences(body)
    validation_text = re.sub(
        r"(?P<ticks>`+)(?P<body>[^`\n]*?)(?P=ticks)",
        "",
        masked,
    )
    failures: list[str] = []
    for match in _LIQUID_BLOCK_PATTERN.finditer(validation_text):
        failures.append(f"block:{match.group('body').strip()}")
    for match in _LIQUID_OUTPUT_PATTERN.finditer(validation_text):
        expression = match.group("body").strip()
        # A raw-protected Mustache/Go/Jinja example is restored as a literal
        # output expression after the protection span is removed.  The
        # renderer has already failed on an unprotected unknown expression;
        # here a compact no-whitespace token is the explicit literal
        # exception (``{{play_name}}``, ``{{ctx.index}}`` and similar).
        root = _liquid_expression_root(expression)
        if not _is_literal_jekyll_output(expression) and not (
            not any(char.isspace() for char in expression)
            and root not in {"site", "page", "include"}
        ):
            failures.append(f"output:{expression}")
    if re.search(
        r"\{::nomarkdown\}|\{:/\}|^\s*\{:{1,2}toc\}\s*$",
        validation_text,
        flags=re.MULTILINE,
    ):
        failures.append("kramdown-wrapper")
    # Fences are masked from the general Liquid scan, but raw/endraw wrappers
    # are executable Jekyll syntax and must be removed there as well.  Keep a
    # dedicated marker so a corpus check cannot report a false clean result
    # merely because the whole fence was protected.
    for fence in protected:
        if re.search(r"\{%-?\s*(?:raw|endraw)\b", fence, flags=re.IGNORECASE):
            failures.append("fence-raw")
            break
    # Fence contents are explicit code/literal exceptions.  Still check that
    # the masking did not accidentally lose any source bytes.
    if _unmask_jekyll_fences(masked, protected) != body:
        failures.append("fence-restore")
    return failures


def _jekyll_config(repo_dir: Path) -> dict[str, Any]:
    if not (repo_dir / "_config.yml").is_file():
        return dict(JEKYLL_DEFAULT_SITE)
    try:
        loaded = _parse_yaml_mapping((repo_dir / "_config.yml").read_text(encoding="utf-8", errors="replace"))
    except OSError:
        return dict(JEKYLL_DEFAULT_SITE)
    result = dict(JEKYLL_DEFAULT_SITE)
    result.update({key: loaded[key] for key in JEKYLL_SITE_ALLOWLIST if key in loaded and loaded[key] is not None})
    return result


def _jekyll_route(value: str, *, baseurl: str = "", site_url: str = "") -> str:
    """Canonicalize a Jekyll URL/permalink to a lower-case route key."""

    value = str(value or "").strip()
    if not value:
        return "/"
    parsed = urlsplit(value)
    path = parsed.path if parsed.scheme or parsed.netloc else value.split("#", 1)[0].split("?", 1)[0]
    path = unquote(path).replace("\\", "/")
    base = str(baseurl or "").strip().rstrip("/")
    if base and (path == base or path.startswith(base + "/")):
        path = path[len(base) :] or "/"
    path = "/" + re.sub(r"/+", "/", path).lstrip("/")
    path = re.sub(r"/index(?:\.html?)?/?$", "/", path, flags=re.IGNORECASE)
    if path.endswith(".html"):
        path = path[:-5] + "/"
    elif path.endswith(".htm"):
        path = path[:-4] + "/"
    elif not path.endswith("/"):
        path += "/"
    if path == "//":
        path = "/"
    return path.lower()


def _jekyll_route_from_source(repo_rel_path: str, *, baseurl: str = "", site_url: str = "") -> str:
    parts = Path(repo_rel_path).parts
    if parts and parts[0].startswith("_"):
        parts = (parts[0][1:],) + parts[1:]
    if parts and Path(parts[-1]).suffix.lower() in {".md", ".markdown"}:
        parts = parts[:-1] + (Path(parts[-1]).stem,)
    if parts and parts[-1].lower() == "index":
        parts = parts[:-1]
    return _jekyll_route("/" + "/".join(parts), baseurl=baseurl, site_url=site_url)


def _jekyll_permalink(metadata: dict[str, Any], repo_rel_path: str, *, collection: str, config: dict[str, Any]) -> str:
    raw = metadata.get("permalink")
    if raw:
        value = str(raw)
        source_parts = list(Path(repo_rel_path).parts)
        if source_parts and source_parts[0].startswith("_"):
            source_parts = source_parts[1:]
        if source_parts and Path(source_parts[-1]).suffix:
            source_parts[-1] = Path(source_parts[-1]).stem
        if source_parts and source_parts[-1].lower() == "index":
            source_parts = source_parts[:-1]
        value = value.replace(":collection", collection).replace(":path", "/".join(source_parts))
        return value
    return _jekyll_route_from_source(repo_rel_path, baseurl=str(config.get("baseurl", "")), site_url=str(config.get("url", "")))


def _jekyll_alias_values(
    metadata: dict[str, Any],
    *,
    config: dict[str, Any] | None = None,
) -> list[str]:
    values: list[str] = []
    for key, value in metadata.items():
        if key.lower() != "redirect_from":
            continue
        if isinstance(value, (list, tuple)):
            values.extend(str(item) for item in value if item is not None)
        elif value:
            values.append(str(value))
    result: list[str] = []
    seen: set[str] = set()
    baseurl = str((config or {}).get("baseurl", ""))
    site_url = str((config or {}).get("url", ""))
    for value in values:
        route = _jekyll_route(value, baseurl=baseurl, site_url=site_url)
        if route not in seen:
            seen.add(route)
            result.append(value)
    return result


def _discover_jekyll_source_files(manifest: Manifest, repo_dir: Path) -> list[Path]:
    discovered: list[Path] = []
    seen: set[str] = set()
    for doc_item in manifest.docs_paths:
        item = repo_dir / doc_item
        if not item.exists():
            print(f"[{manifest.name}] Warning: path not found in repo: {doc_item}", file=sys.stderr)
            continue
        candidates = [item] if item.is_file() else sorted(item.rglob("*"))
        for path in candidates:
            if not path.is_file() or path.suffix.lower() not in {".md", ".markdown"}:
                continue
            relative_to_item = path.relative_to(item).as_posix() if item.is_dir() else path.name
            if any(fnmatch.fnmatch(relative_to_item, pattern) for pattern in manifest.exclude_globs):
                continue
            key = path.relative_to(repo_dir).as_posix()
            if key not in seen:
                seen.add(key)
                discovered.append(path)
    return discovered


def _route_to_output(route: str) -> str:
    route = route.strip().lstrip("/")
    if not route:
        return "index.md"
    if route.endswith("/"):
        return f"{route}index.md"
    suffix = Path(route).suffix.lower()
    return route if suffix == ".md" else f"{route}.md"


def _build_jekyll_registry(manifest: Manifest, repo_dir: Path) -> _JekyllRegistry:
    config = _jekyll_config(repo_dir)
    pages: list[_JekyllPage] = []
    for file_path in _discover_jekyll_source_files(manifest, repo_dir):
        repo_rel = file_path.relative_to(repo_dir).as_posix()
        metadata, _ = parse_jekyll_frontmatter(file_path.read_text(encoding="utf-8", errors="replace"), Path(repo_rel).stem)
        collection = Path(repo_rel).parts[0].lstrip("_") if Path(repo_rel).parts else manifest.collection
        permalink = _jekyll_permalink(metadata, repo_rel, collection=collection, config=config)
        canonical_value = str(metadata.get("canonical_url", "") or "")
        # ``permalink`` is the page's actual public route.  ``canonical_url``
        # is SEO metadata and may intentionally point at a shared route (for
        # example, several upgrade pages canonicalize to one landing page).
        # It must never decide the output path or hide a real permalink.
        route = _jekyll_route(
            permalink,
            baseurl=str(config.get("baseurl", "")),
            site_url=str(config.get("url", "")),
        )
        canonical_route = _jekyll_route(
            canonical_value or permalink,
            baseurl=str(config.get("baseurl", "")),
            site_url=str(config.get("url", "")),
        )
        canonical_url = canonical_value or f"{str(config.get('url', '')).rstrip('/')}{str(config.get('baseurl', '')).rstrip('/')}{route}"
        pages.append(
            _JekyllPage(
                file_path=file_path,
                repo_rel_path=repo_rel,
                metadata=metadata,
                collection=collection,
                route=route,
                canonical_url=canonical_url,
                canonical_route=canonical_route,
                permalink=permalink if str(permalink).startswith("/") else f"/{permalink}",
                redirect_aliases=tuple(_jekyll_alias_values(metadata, config=config)),
                output_rel_path="",
            )
        )
    route_groups: dict[str, list[_JekyllPage]] = {}
    for page in pages:
        route_groups.setdefault(page.route, []).append(page)
    assigned: set[str] = set()
    finalized: list[_JekyllPage] = []
    for page in pages:
        collision = len(route_groups[page.route]) > 1
        output = _route_to_output(page.route) if not collision else f"__source__/{page.repo_rel_path}"
        # A route such as /__source__/... must not overlap the explicit source
        # namespace.  Such a source is uncommon, but its output remains clear.
        if output in assigned:
            output = f"__source__/{page.repo_rel_path}"
        assigned.add(output)
        finalized.append(
            _JekyllPage(
                file_path=page.file_path,
                repo_rel_path=page.repo_rel_path,
                metadata=page.metadata,
                collection=page.collection,
                route=page.route,
                canonical_url=page.canonical_url,
                canonical_route=page.canonical_route,
                permalink=page.permalink,
                redirect_aliases=page.redirect_aliases,
                output_rel_path=output,
                canonical_collision=collision,
            )
        )
    by_source = {page.repo_rel_path: page for page in finalized}
    by_route: dict[str, list[_JekyllPage]] = {}
    by_alias: dict[str, list[_JekyllPage]] = {}
    for page in finalized:
        by_route.setdefault(page.route, []).append(page)
    for page in finalized:
        # A Jekyll page can expose aliases through redirect_from, and an
        # explicit canonical_url can also identify a shared documentation
        # route.  Register those paths only when they do not overlap a real
        # permalink route; otherwise an alias would mask the page that owns
        # that route.  Keep duplicate aliases from different pages so the
        # resolver can report an ambiguity instead of guessing.
        # Route keys are lower-cased and de-duplicated per page; if two pages
        # claim the same alias, the resolver retains both and emits an
        # explicit ambiguous-link marker.
        aliases = list(page.redirect_aliases)
        if page.canonical_route != page.route:
            aliases.append(page.canonical_url)
        seen_alias_routes: set[str] = set()
        for alias in aliases:
            alias_route = _jekyll_route(
                alias,
                baseurl=str(config.get("baseurl", "")),
                site_url=str(config.get("url", "")),
            )
            if (
                alias_route in seen_alias_routes
                or alias_route == page.route
                or alias_route in by_route
            ):
                continue
            seen_alias_routes.add(alias_route)
            by_alias.setdefault(alias_route, []).append(page)
    return _JekyllRegistry(manifest, finalized, by_source, by_route, by_alias)


def _peer_jekyll_registry(manifest: Manifest) -> _JekyllRegistry | None:
    if manifest.collection not in {"opensearch", "opensearch-dashboards"}:
        return None
    peer_collection = "opensearch-dashboards" if manifest.collection == "opensearch" else "opensearch"
    # Derive the repository root from the current manifest so tests can use a
    # temporary ``REPO_ROOT`` without accidentally reading the live checkout.
    try:
        repository_root = manifest.raw_dir.parents[2]
    except IndexError:
        repository_root = REPO_ROOT

    manifests_dir = repository_root / "builder" / "manifests"
    if not manifests_dir.is_dir():
        return None
    # The filename is a convenient fast path, not the identity of a peer.
    # Releases can use a patch-level version or a descriptive manifest name,
    # so fall back to inspecting manifest content and match both collection
    # and version exactly.
    candidate_paths: list[Path] = []
    preferred = manifests_dir / f"{peer_collection}-{manifest.version}.toml"
    if preferred.is_file():
        candidate_paths.append(preferred)
    candidate_paths.extend(
        path for path in sorted(manifests_dir.glob("*.toml")) if path != preferred
    )
    peer_manifest: Manifest | None = None
    for peer_path in candidate_paths:
        try:
            candidate = load_manifest(peer_path)
        except (OSError, TypeError, ValueError):
            continue
        if candidate.collection == peer_collection and candidate.version == manifest.version:
            peer_manifest = candidate
            break
    if peer_manifest is None:
        return None
    peer_repo = peer_manifest.raw_dir / "repo"
    if not peer_repo.is_dir():
        return None
    return _build_jekyll_registry(peer_manifest, peer_repo)


def _source_relative_page_target(page: _JekyllPage, target: str, registry: _JekyllRegistry) -> _JekyllPage | None:
    path_part = unquote(target.split("#", 1)[0].split("?", 1)[0]).strip()
    if not path_part or path_part.startswith(("/", "//")):
        return None
    candidates = [Path(os.path.normpath(str(Path(page.repo_rel_path).parent / path_part)))]
    if candidates[0].suffix == "":
        candidates.extend(
            [candidates[0].with_suffix(suffix) for suffix in (".md", ".markdown")]
            + [candidates[0] / "index.md", candidates[0] / "index.markdown"]
        )
    elif candidates[0].suffix.lower() == ".md":
        candidates.append(candidates[0].with_suffix(".markdown"))
    for candidate in candidates:
        found = registry.by_source.get(candidate.as_posix())
        if found is not None:
            return found
    return None


def _markdown_destination(raw_target: str) -> tuple[str, str]:
    raw_target = raw_target.strip()
    if raw_target.startswith("<"):
        end = raw_target.find(">", 1)
        if end >= 0:
            return raw_target[1:end], raw_target[end + 1 :]
    match = re.match(r"(?P<url>\S+)(?P<rest>.*)$", raw_target, re.DOTALL)
    return (match.group("url"), match.group("rest")) if match else (raw_target, "")


def _docs_route_from_target(target: str, site: dict[str, Any]) -> tuple[str, str] | None:
    parsed = urlsplit(target)
    configured_origin = urlsplit(str(site.get("url", "")).rstrip("/"))
    if parsed.scheme or parsed.netloc:
        if (parsed.scheme.lower(), parsed.netloc.lower()) != (
            configured_origin.scheme.lower(),
            configured_origin.netloc.lower(),
        ):
            return None
    elif not target.startswith("/"):
        return None
    path = parsed.path if parsed.scheme or parsed.netloc else target.split("#", 1)[0].split("?", 1)[0]
    route = _jekyll_route(path, baseurl=str(site.get("baseurl", "")), site_url=str(site.get("url", "")))
    suffix = (f"?{parsed.query}" if parsed.query else "") + (f"#{parsed.fragment}" if parsed.fragment else "")
    return route, suffix


def _rewrite_jekyll_links(
    body: str,
    page: _JekyllPage,
    registry: _JekyllRegistry,
    peer_registry: _JekyllRegistry | None,
    repo_dir: Path,
) -> tuple[str, dict[str, int]]:
    """Resolve docs-origin links and classify unresolved/cross-corpus links."""

    site = _jekyll_config(repo_dir)
    stats = {"unresolved": 0, "cross_corpus": 0, "assets": 0}
    repo_root = repo_dir.resolve()

    def resolve_target(target: str) -> tuple[str, str]:
        destination, rest = _markdown_destination(target)
        docs_route = _docs_route_from_target(destination, site)
        target_page: _JekyllPage | None = None
        target_registry = registry
        route: str | None = None
        suffix = ""
        if docs_route is not None:
            route, suffix = docs_route
            current = registry.by_route.get(route, [])
            if len(current) == 1:
                target_page = current[0]
            elif len(current) > 1:
                stats["unresolved"] += 1
                return destination + rest, f" <!-- unresolved-jekyll-link: route={route} -->"
            elif peer_registry is not None:
                peer = peer_registry.by_route.get(route, [])
                if not peer:
                    # A peer page may be reached through its source-derived
                    # permalink even when canonical_url points elsewhere.
                    # Treat that alias as a cross-corpus match only after
                    # checking canonical routes, preserving ambiguity markers.
                    peer = peer_registry.by_alias.get(route, [])
                if len(peer) == 1:
                    stats["cross_corpus"] += 1
                    return destination + rest, f" <!-- unresolved-cross-corpus-link: collection={peer_registry.manifest.collection} route={route} -->"
                if len(peer) > 1:
                    stats["cross_corpus"] += 1
                    return destination + rest, f" <!-- unresolved-cross-corpus-link: ambiguous route={route} -->"
            # A docs-origin image/download is not a page route.  Preserve it
            # as an immutable blob URL when the asset exists in the sparse
            # checkout instead of manufacturing a page link ending in `/`.
            parsed_destination = urlsplit(destination)
            asset_path = parsed_destination.path
            base = str(site.get("baseurl", "")).rstrip("/")
            if base and (asset_path == base or asset_path.startswith(base + "/")):
                asset_path = asset_path[len(base) :]
            asset_candidate = (repo_dir / unquote(asset_path.lstrip("/"))).resolve()
            try:
                asset_rel = asset_candidate.relative_to(repo_root).as_posix()
            except ValueError:
                asset_rel = ""
            if asset_rel and asset_candidate.is_file() and asset_candidate.suffix.lower() in ASSET_SUFFIXES:
                stats["assets"] += 1
                return _source_url(registry.manifest, asset_rel) + suffix + rest, ""
            alias = registry.by_alias.get(route, [])
            if len(alias) == 1:
                target_page = alias[0]
            elif len(alias) > 1:
                stats["unresolved"] += 1
                return destination + rest, f" <!-- unresolved-jekyll-link: ambiguous-redirect={route} -->"
            if target_page is None:
                stats["unresolved"] += 1
                return destination + rest, f" <!-- unresolved-jekyll-link: route={route} -->"
        else:
            target_page = _source_relative_page_target(page, destination, registry)
            if target_page is not None:
                suffix = ""
            elif destination.startswith(("#", "mailto:", "http:", "https:", "//")):
                pinned = _pinned_repository_url(registry.manifest, destination)
                return (pinned or destination) + rest, ""
            else:
                # A relative image/asset may live in the sparse checkout but
                # is intentionally not a documentation page.
                candidate = (repo_dir / Path(page.repo_rel_path).parent / destination).resolve()
                try:
                    repo_rel = candidate.relative_to(repo_root).as_posix()
                except ValueError:
                    repo_rel = ""
                if repo_rel and candidate.is_file() and candidate.suffix.lower() in ASSET_SUFFIXES:
                    stats["assets"] += 1
                    return _source_url(registry.manifest, repo_rel) + rest, ""
                stats["unresolved"] += 1
                return destination + rest, f" <!-- unresolved-jekyll-link: target={destination} -->"
        relative = os.path.relpath(target_page.output_rel_path, start=Path(page.output_rel_path).parent.as_posix()).replace(os.sep, "/")
        return relative + suffix + rest, ""

    link_open_pattern = re.compile(r"(?P<open>!?\[[^\]\n]*\]\()")

    def rewrite_segment(segment: str) -> str:
        output: list[str] = []
        cursor = 0
        while True:
            match = link_open_pattern.search(segment, cursor)
            if match is None:
                output.append(segment[cursor:])
                break
            output.append(segment[cursor : match.end()])
            index = match.end()
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
                output.append(segment[match.end() :])
                break
            raw_target = segment[match.end() : target_end]
            rewritten, marker = resolve_target(raw_target)
            output.append(rewritten)
            output.append(")")
            output.append(marker)
            cursor = target_end + 1
        return "".join(output)

    masked, protected = _mask_jekyll_fences(body)
    # A few fixed-source pages contain a malformed nested Markdown link such
    # as [label]([display](target) (the outer closing parenthesis is missing),
    # or [label]/(target). Repair only these unambiguous patterns before
    # scanning; otherwise one malformed link can prevent all later links on
    # the same segment from being resolved.
    masked = re.sub(
        r"\]\(\[[^\]\n]+\]\((?P<target>[^()\n]+)\)",
        r"](\g<target>)",
        masked,
    )
    masked = re.sub(r"\]\s*/\(", "](", masked)
    rewritten = rewrite_segment(masked)

    # nomarkdown inline HTML carries the same docs-origin URLs as Markdown
    # links.  Attributes are handled separately because they do not have a
    # closing parenthesis to scan.
    attr_pattern = re.compile(r"(?P<prefix>\b(?:href|src)=\s*[\"'])(?P<target>[^\"']+)(?P<suffix>[\"'])", re.IGNORECASE)

    def unresolved_attr(match: re.Match[str], detail: str) -> str:
        # Keep the original URL usable for readers while recording why it was
        # not rewritten. A data attribute is valid on both anchors and images,
        # unlike inserting a Markdown comment inside an HTML tag.
        marker = html.escape(f"unresolved:{detail}", quote=True)
        return f"{match.group(0)} data-airgap-link-status=\"{marker}\""

    def asset_url(destination: str, rest: str = "") -> str | None:
        parsed_destination = urlsplit(destination)
        asset_path = parsed_destination.path
        base = str(site.get("baseurl", "")).rstrip("/")
        if base and (asset_path == base or asset_path.startswith(base + "/")):
            asset_path = asset_path[len(base) :]
        asset_candidate = (repo_dir / unquote(asset_path.lstrip("/"))).resolve()
        try:
            asset_rel = asset_candidate.relative_to(repo_root).as_posix()
        except ValueError:
            return None
        if (
            not asset_rel
            or not asset_candidate.is_file()
            or asset_candidate.suffix.lower() not in ASSET_SUFFIXES
        ):
            return None
        query_fragment = (f"?{parsed_destination.query}" if parsed_destination.query else "") + (
            f"#{parsed_destination.fragment}" if parsed_destination.fragment else ""
        )
        stats["assets"] += 1
        return _source_url(registry.manifest, asset_rel) + query_fragment + rest

    def attr_replace(match: re.Match[str]) -> str:
        target, rest = _markdown_destination(match.group("target"))
        docs_route = _docs_route_from_target(target, site)
        if docs_route is not None:
            route, suffix = docs_route
            pinned_asset = asset_url(target, rest)
            if pinned_asset is not None:
                return f"{match.group('prefix')}{pinned_asset}{match.group('suffix')}"
            current = registry.by_route.get(route, [])
            if len(current) == 1:
                relative = os.path.relpath(
                    current[0].output_rel_path,
                    start=Path(page.output_rel_path).parent.as_posix(),
                ).replace(os.sep, "/")
                return f"{match.group('prefix')}{relative}{suffix}{rest}{match.group('suffix')}"
            if len(current) > 1:
                stats["unresolved"] += 1
                return unresolved_attr(match, f"ambiguous route={route}")
            if peer_registry is not None:
                peer = peer_registry.by_route.get(route, [])
                if not peer:
                    peer = peer_registry.by_alias.get(route, [])
                if len(peer) == 1:
                    stats["cross_corpus"] += 1
                    return unresolved_attr(
                        match,
                        f"cross-corpus collection={peer_registry.manifest.collection} route={route}",
                    )
                if len(peer) > 1:
                    stats["cross_corpus"] += 1
                    return unresolved_attr(match, f"cross-corpus ambiguous route={route}")
            alias = registry.by_alias.get(route, [])
            if len(alias) == 1:
                relative = os.path.relpath(
                    alias[0].output_rel_path,
                    start=Path(page.output_rel_path).parent.as_posix(),
                ).replace(os.sep, "/")
                return f"{match.group('prefix')}{relative}{suffix}{rest}{match.group('suffix')}"
            stats["unresolved"] += 1
            detail = f"ambiguous redirect={route}" if len(alias) > 1 else f"route={route}"
            return unresolved_attr(match, detail)

        target_page = _source_relative_page_target(page, target, registry)
        if target_page is not None:
            relative = os.path.relpath(
                target_page.output_rel_path,
                start=Path(page.output_rel_path).parent.as_posix(),
            ).replace(os.sep, "/")
            return f"{match.group('prefix')}{relative}{rest}{match.group('suffix')}"
        if target.startswith(("#", "mailto:", "http:", "https:", "//")):
            pinned = _pinned_repository_url(registry.manifest, target)
            if pinned is not None:
                return f"{match.group('prefix')}{pinned}{rest}{match.group('suffix')}"
            return match.group(0)
        pinned_asset = asset_url(target, rest)
        if pinned_asset is not None:
            return f"{match.group('prefix')}{pinned_asset}{match.group('suffix')}"
        stats["unresolved"] += 1
        return unresolved_attr(match, f"target={target}")

    rewritten = attr_pattern.sub(attr_replace, rewritten)
    return _unmask_jekyll_fences(rewritten, protected), stats


def _prometheus_operator_ref_candidates(
    source_path: Path | None,
    repo_dir: Path,
    target_path: str,
) -> list[Path]:
    """Return Hugo page candidates used by the Prometheus Operator docs.

    The repository keeps its Hugo content directly below ``Documentation``.
    Most references are page-name references, so Hugo first finds a sibling
    page and then a page at the Documentation root.  Keeping this lookup
    source-aware lets the normal source-link pass map the result to the actual
    corpus output path later.
    """

    normalized = target_path.replace("\\", "/").lstrip("/")
    if not normalized:
        return []
    documentation = (repo_dir / "Documentation").resolve()
    roots: list[Path] = []
    if source_path is not None:
        roots.append(source_path.resolve().parent)
    roots.extend((documentation, repo_dir.resolve()))

    candidates: list[Path] = []

    def add_candidates(root: Path, relative: str) -> None:
        candidate = root / relative
        candidates.append(candidate)
        if candidate.suffix == "":
            candidates.extend(
                candidate.with_suffix(extension)
                for extension in (".md", ".markdown", ".rst")
            )
            candidates.extend(
                (candidate / "index.md", candidate / "index.markdown", candidate / "index.rst")
            )
        elif candidate.suffix.lower() in {".md", ".markdown"}:
            candidates.append(candidate.with_suffix(".rst"))

    for root in roots:
        add_candidates(root, normalized)

    # Hugo callers occasionally include the content root in a ref.  Do not
    # duplicate that prefix when trying the Documentation-root candidate.
    if normalized.startswith("Documentation/"):
        without_root = normalized[len("Documentation/") :]
        if source_path is not None:
            add_candidates(source_path.resolve().parent, without_root)
        add_candidates(documentation, without_root)
        add_candidates(repo_dir.resolve(), without_root)

    unique: list[Path] = []
    seen: set[Path] = set()
    for candidate in candidates:
        if candidate not in seen:
            seen.add(candidate)
            unique.append(candidate)
    return unique


def _prometheus_operator_ref(
    name: str,
    arguments: str,
    repo_dir: Path,
    source_path: Path | None,
) -> str:
    """Render a Prometheus Operator ``ref``/``relref`` to a source path."""

    arguments = re.sub(r"/\s*$", "", arguments.strip())
    positional, named = _shortcode_arguments(arguments)
    target = (
        named.get("path", "")
        or named.get("target", "")
        or (positional[0] if positional else "")
    )
    if not target:
        return _shortcode_marker(name, arguments)
    target = target.strip()
    if target.startswith("#") or source_path is None:
        return target

    path_part, hash_mark, fragment = target.partition("#")
    query = ""
    if "?" in path_part:
        path_part, query = path_part.split("?", 1)
    suffix = (f"?{query}" if query else "") + (f"#{fragment}" if hash_mark else "")
    for candidate in _prometheus_operator_ref_candidates(source_path, repo_dir, path_part):
        resolved = _safe_repo_file(repo_dir, candidate)
        if resolved is None or resolved.suffix.lower() not in {".md", ".markdown", ".rst"}:
            continue
        relative = os.path.relpath(
            resolved,
            start=source_path.resolve().parent,
        ).replace(os.sep, "/")
        return f"{relative}{suffix}"
    # Keep an unknown reference explicit and searchable.  Valid refs in the
    # fixed source inventory always take the branch above.
    return _shortcode_marker(name, arguments)


def _prometheus_operator_alert(arguments: str, inner: str) -> str:
    """Turn the source site's self-closing alert into searchable Markdown."""

    arguments = re.sub(r"/\s*$", "", arguments.strip())
    _, named = _shortcode_arguments(arguments)
    text = named.get("text", "").strip()
    icon = named.get("icon", "").strip()
    message = " ".join(part for part in (icon, text, inner.strip()) if part)
    if not message:
        return _shortcode_marker("alert", arguments)
    return f"\n\n> **Note:** {message}\n\n"


def _mask_prometheus_operator_literals(content: str) -> tuple[str, list[str]]:
    """Protect Markdown/Hugo literal regions while rendering source tags."""

    masked, protected = _mask_gitbook_fences(content)

    def protect(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"\x00PROMETHEUS_LITERAL_{len(protected) - 1}\x01"

    # Escaped Hugo tags and Hugo comments are documentation examples, not
    # executable source tags.  Raw HTML blocks and inline code are literals as
    # well, and must remain byte-for-byte unchanged.
    masked = re.sub(
        r"\{\{(?:[<%])?/\*.*?\*/(?:[>%])?\}\}",
        protect,
        masked,
        flags=re.DOTALL,
    )
    masked = re.sub(r"(?is)<pre\b[^>]*>.*?</pre\s*>", protect, masked)
    masked = re.sub(r"(?P<ticks>`+)(?P<body>[^`\n]*?)(?P=ticks)", protect, masked)
    return masked, protected


def _render_prometheus_operator_segment(
    content: str,
    repo_dir: Path,
    *,
    source_path: Path | None,
    depth: int,
) -> str:
    if depth > 10:
        tokens = _iter_shortcode_tokens(content)
        if not tokens:
            return content
        output: list[str] = []
        cursor = 0
        for token in tokens:
            output.append(content[cursor : token.start])
            name, arguments, _ = _shortcode_parts(token.body)
            output.append(_shortcode_marker(name or "shortcode", arguments))
            cursor = token.end
        output.append(content[cursor:])
        return "".join(output)

    tokens = _iter_shortcode_tokens(content)
    if not tokens:
        return content
    output: list[str] = []
    cursor = 0
    index = 0
    while index < len(tokens):
        token = tokens[index]
        output.append(content[cursor : token.start])
        name, arguments, closing = _shortcode_parts(re.sub(r"\s+", " ", token.body.strip()))
        self_closing = token.body.strip().endswith("/")
        arguments = re.sub(r"/\s*$", "", arguments)
        if not name:
            output.append(_shortcode_marker("shortcode", arguments))
            cursor = token.end
            index += 1
            continue
        if closing:
            output.append(_shortcode_marker(name, arguments))
            cursor = token.end
            index += 1
            continue

        close_index = None if self_closing else _matching_shortcode_close(tokens, index, name)
        if close_index is None:
            inner = ""
            next_index = index + 1
        else:
            close_token = tokens[close_index]
            inner = _render_prometheus_operator_segment(
                content[token.end : close_token.start],
                repo_dir,
                source_path=source_path,
                depth=depth + 1,
            )
            next_index = close_index + 1

        if name in {"ref", "relref"}:
            rendered = _prometheus_operator_ref(name, arguments, repo_dir, source_path)
        elif name == "alert":
            rendered = _prometheus_operator_alert(arguments, inner)
        else:
            marker = _shortcode_marker(name, arguments)
            rendered = (
                f"\n\n{marker}\n\n{inner.strip()}\n\n"
                if inner.strip()
                else f"\n\n{marker}\n\n"
            )
        output.append(rendered)
        cursor = tokens[next_index - 1].end
        index = next_index
    output.append(content[cursor:])
    return "".join(output)


def _render_prometheus_operator_shortcodes(
    content: str,
    repo_dir: Path,
    *,
    source_path: Path | None = None,
    depth: int = 0,
) -> str:
    """Render the small Hugo subset used by Prometheus Operator documents."""

    # The profile uses NUL-delimited sentinels for literal spans.  Reject a
    # source NUL before masking so an upstream byte cannot impersonate a
    # sentinel or make restoration appear to converge on the wrong text.
    if "\x00" in content:
        raise ValueError("Prometheus Operator shortcode rendering rejects NUL bytes")

    masked, protected = _mask_prometheus_operator_literals(content)
    rendered = _render_prometheus_operator_segment(
        masked,
        repo_dir,
        source_path=source_path,
        depth=depth,
    )
    # Literal spans can nest (for example an escaped Hugo comment inside an
    # inline-code span).  The outer span is protected later and therefore
    # contains the inner sentinel.  Restore in reverse stack order and keep
    # iterating until no generated marker remains; a single forward pass would
    # leak the inner sentinel into the corpus.
    marker_pattern = re.compile(r"\x00(?:GITBOOK_FENCE|PROMETHEUS_LITERAL)_\d+\x01")
    for _ in range(len(protected) + 1):
        changed = False
        for index in range(len(protected) - 1, -1, -1):
            for prefix in ("GITBOOK_FENCE", "PROMETHEUS_LITERAL"):
                marker = f"\x00{prefix}_{index}\x01"
                if marker in rendered:
                    rendered = rendered.replace(marker, protected[index])
                    changed = True
        if marker_pattern.search(rendered) is None:
            return rendered
        if not changed:
            break
    raise ValueError("Prometheus Operator literal restoration did not converge")


def clean_hugo_shortcodes(
    content: str,
    repo_dir: Path,
    depth: int = 0,
    *,
    profile: str = "kubernetes",
    source_path: Path | None = None,
) -> str:
    """Clean Hugo shortcodes using the manifest-selected source profile.

    ``kubernetes`` remains the default for callers that used the historical
    helper directly.  Manifests with no profile are not routed here by
    ``normalize``.
    """

    if profile == "kubernetes":
        return _clean_kubernetes_shortcodes(content, repo_dir, depth)
    if profile == "istio":
        return _render_istio_shortcodes(content, repo_dir, depth=depth)
    if profile == "gitbook":
        return _render_gitbook_shortcodes(content, repo_dir, depth=depth)
    if profile in {"prometheus-operator", "prometheus_operator"}:
        return _render_prometheus_operator_shortcodes(
            content,
            repo_dir,
            source_path=source_path,
            depth=depth,
        )
    if profile in {"jekyll", "opensearch", "opensearch-jekyll"}:
        return render_jekyll_template(content, repo_dir)
    raise ValueError(f"unknown Hugo shortcode profile: {profile!r}")


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
    seen_sources: set[str] = set()

    def excluded(relative_path: str) -> bool:
        return any(fnmatch.fnmatch(relative_path, pattern) for pattern in manifest.exclude_globs)

    for doc_item in manifest.docs_paths:
        item_path = repo_dir / doc_item
        if not item_path.exists():
            print(f"[{manifest.name}] Warning: path not found in repo: {doc_item}", file=sys.stderr)
            continue
        if item_path.is_file():
            if item_path.suffix.lower() in supported_suffixes and not excluded(Path(doc_item).name):
                source_key = item_path.relative_to(repo_dir).as_posix()
                if source_key not in seen_sources:
                    seen_sources.add(source_key)
                    discovered.append((item_path, Path(doc_item).name))
            continue
        for path in sorted(item_path.rglob("*")):
            relative_path = path.relative_to(item_path).as_posix()
            if (
                path.is_file()
                and path.suffix.lower() in supported_suffixes
                and not excluded(relative_path)
            ):
                source_key = path.relative_to(repo_dir).as_posix()
                if source_key not in seen_sources:
                    seen_sources.add(source_key)
                    discovered.append((path, relative_path))

    def output_path(relative_path: str) -> str:
        return Path(relative_path).with_suffix(".md").as_posix()

    collision_groups: dict[str, list[int]] = {}
    for index, (_, relative_path) in enumerate(discovered):
        collision_groups.setdefault(output_path(relative_path), []).append(index)

    disambiguate: set[int] = set()
    for indices in collision_groups.values():
        if len(indices) < 2:
            continue

        def collision_preference(index: int) -> tuple[bool, int, str, int]:
            file_path, relative_path = discovered[index]
            repo_relative_path = file_path.relative_to(repo_dir).as_posix()
            # A source explicitly listed at the repository root should retain
            # its historical basename when it collides with a docs directory.
            return (
                repo_relative_path != relative_path,
                len(Path(repo_relative_path).parts),
                repo_relative_path,
                index,
            )

        keeper = min(indices, key=collision_preference)
        disambiguate.update(index for index in indices if index != keeper)

    # Preserve all original non-colliding output paths.  A collision candidate
    # may propose one of those paths after repo-relative disambiguation, so
    # reserve them before assigning the changed paths.
    reserved_outputs = {
        output_path(relative_path)
        for index, (_, relative_path) in enumerate(discovered)
        if index not in disambiguate
    }
    assigned_outputs: set[str] = set()
    resolved: list[tuple[Path, str]] = []
    for index, (file_path, relative_path) in enumerate(discovered):
        output_relative_path = relative_path
        if index in disambiguate:
            output_relative_path = file_path.relative_to(repo_dir).as_posix()
            while (
                output_path(output_relative_path) in reserved_outputs
                or output_path(output_relative_path) in assigned_outputs
            ):
                # Keep the repository-relative source path visible while
                # making a second .md/.rst collision deterministic as well.
                output_relative_path += ".source"
        assigned_outputs.add(output_path(output_relative_path))
        resolved.append((file_path, output_relative_path))
    return resolved


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


def _mutable_ref_allowlist(manifest: Manifest) -> tuple[str, ...]:
    """Return the exact branch/ref names eligible for URL pinning.

    Older manifests do not carry ``mutable_refs`` yet, so retain the
    historical ``main``/``master`` behavior for them.  An explicit empty
    list remains an opt-out.  Ref names are treated as path literals by the
    URL matcher; callers that build a regex must escape them first.
    """

    configured = getattr(manifest, "mutable_refs", ("main", "master"))
    if isinstance(configured, str):
        configured = [configured]
    refs: list[str] = []
    for value in configured or ():
        ref = str(value).strip().strip("/")
        if not ref or any(character in ref for character in "\x00?#"):
            continue
        if ref not in refs:
            refs.append(ref)
    return tuple(refs)


def _mutable_ref_source_path(path: str, refs: tuple[str, ...]) -> str | None:
    """Return the path after an allowlisted ref, including an empty suffix."""

    for ref in sorted(refs, key=len, reverse=True):
        if path == ref:
            return ""
        prefix = f"{ref}/"
        if path.startswith(prefix):
            return path[len(prefix) :]
    return None


def _pinned_repository_url(manifest: Manifest, target: str) -> str | None:
    """Pin mutable same-repository GitHub links to the manifest commit."""

    repository = urlsplit(manifest.repo_url.rstrip("/"))
    try:
        parsed = urlsplit(target)
    except ValueError:
        # A prose URL can contain a literal bracket (for example an IPv6
        # placeholder).  It is not a pinning candidate and must remain intact.
        return None
    if repository.netloc.lower() != "github.com" or not manifest.git_ref:
        return None
    mutable_refs = _mutable_ref_allowlist(manifest)
    prefix = repository.path.rstrip("/") + "/"
    same_github_host = (parsed.scheme.lower(), parsed.netloc.lower()) == (
        repository.scheme.lower(),
        repository.netloc.lower(),
    )
    if same_github_host and parsed.path.startswith(prefix):
        remainder = parsed.path[len(prefix) :]
        kind, separator, ref_and_path = remainder.partition("/")
        if not separator or kind not in {"blob", "tree", "raw"}:
            return None
        mutable_source_path = _mutable_ref_source_path(ref_and_path, mutable_refs)
        if mutable_source_path is not None:
            is_mutable_branch_link = True
            source_path = mutable_source_path
        else:
            # Keep the established asset policy for versioned/tagged blob
            # links.  Non-asset tag/branch URLs are not mutable and remain
            # byte-for-byte unchanged.
            ref, source_separator, source_path = ref_and_path.partition("/")
            if not source_separator:
                source_path = ""
            is_mutable_branch_link = False
        # GitHub accepts a tree URL at the repository root, but blob/raw URLs
        # require a path. Preserve that distinction while still pinning
        # reference definitions such as ``[main]: .../tree/main``.
        if not source_path and kind != "tree":
            return None
        is_blob_asset = kind == "blob" and Path(source_path).suffix.lower() in ASSET_SUFFIXES
        if not (is_mutable_branch_link or is_blob_asset):
            return None
        pinned_path = f"{prefix}{kind}/{manifest.git_ref}"
        if source_path:
            pinned_path += f"/{source_path}"
        return urlunsplit((parsed.scheme, parsed.netloc, pinned_path, parsed.query, parsed.fragment))

    # GitHub's raw host omits the ``blob``/``raw`` path component:
    # /<owner>/<repo>/<branch>/<path>.  It is still the same repository when
    # the owner/repository path exactly matches the manifest.
    raw_prefix = prefix
    if parsed.scheme.lower() in {"http", "https"} and parsed.netloc.lower() == "raw.githubusercontent.com":
        if not parsed.path.startswith(raw_prefix):
            return None
        remainder = parsed.path[len(raw_prefix) :]
        path = None
        for ref in sorted(mutable_refs, key=len, reverse=True):
            ref_prefix = f"{ref}/"
            if remainder.startswith(ref_prefix):
                path = remainder[len(ref_prefix) :]
                break
        if not path:
            return None
        pinned_path = f"{raw_prefix}{manifest.git_ref}/{path}"
        return urlunsplit((parsed.scheme, parsed.netloc, pinned_path, parsed.query, parsed.fragment))
    return None


def _pin_mutable_repository_urls_in_text(manifest: Manifest, text: str) -> str:
    """Pin same-repository branch URLs embedded in ordinary prose.

    Markdown permits an image inside a link label, and some documentation
    passes a raw GitHub URL inside another URL's query string. Those shapes
    are not standalone Markdown destinations, so the structural link parser
    cannot see them. This final, repository-scoped pass changes only the
    exact ``main``/``master`` branch segment; callers protect code literals
    before invoking it.
    """

    repository = urlsplit(manifest.repo_url.rstrip("/").removesuffix(".git"))
    if repository.netloc.lower() != "github.com" or not manifest.git_ref:
        return text
    mutable_refs = _mutable_ref_allowlist(manifest)
    if not mutable_refs:
        return text
    repository_path = re.escape(repository.path.rstrip("/"))
    mutable_ref_pattern = "|".join(
        re.escape(ref) for ref in sorted(mutable_refs, key=len, reverse=True)
    )
    branch_boundary = r"(?=/|[?#)\]}>.,;:'\"]|\s|$)"
    patterns = (
        re.compile(
            rf"(?P<prefix>https?://github\.com{repository_path}/(?:blob|tree|raw)/)"
            rf"(?:{mutable_ref_pattern}){branch_boundary}",
            re.IGNORECASE,
        ),
        re.compile(
            rf"(?P<prefix>https?://raw\.githubusercontent\.com{repository_path}/)"
            rf"(?:{mutable_ref_pattern}){branch_boundary}",
            re.IGNORECASE,
        ),
    )
    for pattern in patterns:
        text = pattern.sub(lambda match: f"{match.group('prefix')}{manifest.git_ref}", text)
    return text


def _source_link_candidates(file_path: Path, target: str) -> list[Path]:
    target_path = unquote(target.split("#", 1)[0].split("?", 1)[0])
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


def _istio_site_config(manifest: Manifest) -> tuple[str, str] | None:
    """Return the manifest-gated Istio version-site root and docs prefix.

    Istio's Markdown uses site-root ``/docs`` routes while the corpus stores
    pages relative to ``content/en/docs``.  The mapping is deliberately
    enabled only by an explicit ``istio`` shortcode profile plus manifest
    site configuration; no version URL is inferred from a collection name.
    """

    if getattr(manifest, "shortcode_profile", "") != "istio":
        return None
    overrides = getattr(manifest, "site_overrides", {})
    if not isinstance(overrides, dict):
        return None

    configured_root = overrides.get("site_url") or overrides.get("version_url")
    if configured_root:
        site_root = str(configured_root).strip().rstrip("/")
    else:
        origin = str(overrides.get("url", "")).strip().rstrip("/")
        baseurl = str(overrides.get("baseurl", "")).strip().strip("/")
        if not origin:
            return None
        site_root = f"{origin}/{baseurl}" if baseurl else origin

    try:
        parsed_root = urlsplit(site_root)
    except ValueError:
        return None
    if parsed_root.scheme.lower() not in {"http", "https"} or not parsed_root.netloc:
        return None

    docs_prefix = str(overrides.get("docs_prefix", "/docs")).strip()
    if not docs_prefix.startswith("/"):
        docs_prefix = f"/{docs_prefix}"
    docs_prefix = re.sub(r"/{2,}", "/", docs_prefix).rstrip("/") or "/docs"
    return site_root, docs_prefix


def _istio_normalize_route(path: str) -> str:
    """Normalize a Hugo route for lookup without changing URL suffixes."""

    path = unquote(path).strip()
    if not path.startswith("/"):
        path = f"/{path}"
    path = re.sub(r"/{2,}", "/", path)
    if path != "/":
        path = path.rstrip("/")
    if path.lower().endswith((".html", ".htm")):
        path = path.rsplit(".", 1)[0]
    if path != "/" and path.endswith("/index"):
        path = path[: -len("/index")] or "/"
    return path or "/"


def _istio_site_routes(
    manifest: Manifest,
    source_outputs: dict[str, str],
) -> dict[str, str]:
    """Map version-site routes to normalized corpus output paths."""

    config = _istio_site_config(manifest)
    if config is None:
        return {}
    _, docs_prefix = config
    routes: dict[str, str] = {}
    for output in source_outputs.values():
        output_path = Path(output)
        if output_path.suffix.lower() != ".md":
            continue
        if output_path.name.lower() in {"index.md", "_index.md"}:
            relative_route = output_path.parent.as_posix()
        else:
            relative_route = output_path.with_suffix("").as_posix()
        if relative_route == ".":
            relative_route = ""
        route = _istio_normalize_route(f"{docs_prefix}/{relative_route}")
        routes.setdefault(route, output_path.as_posix())
    return routes


def _istio_site_link_rewrite(
    target: str,
    *,
    target_rel: Path,
    manifest: Manifest,
    site_routes: dict[str, str],
    repo_dir: Path | None = None,
) -> tuple[str, str | None] | None:
    """Rewrite an Istio site route and retain query/fragment byte-for-byte.

    The return value is ``(destination, marker)``.  ``marker`` is populated
    only when a site route is outside the corpus map, making every fallback
    auditable by the validator.  Non-Istio, cross-site, and source-relative
    links return ``None`` so the historical source-link logic remains intact.
    """

    config = _istio_site_config(manifest)
    if config is None:
        return None
    site_root, docs_prefix = config

    original = target.strip()
    if not original:
        return None
    angle = original.startswith("<") and original.endswith(">")
    destination = original[1:-1].strip() if angle else original
    # An inline Markdown title is not a site destination.  The existing
    # source-link parser intentionally leaves such malformed/extended shapes
    # alone; keep that boundary here as well.
    if any(character.isspace() for character in destination):
        return None

    path_part, hash_mark, fragment = destination.partition("#")
    query = ""
    if "?" in path_part:
        path_part, query = path_part.split("?", 1)
    suffix = (f"?{query}" if query else "") + (f"#{fragment}" if hash_mark else "")

    parsed_root = urlsplit(site_root)
    path: str
    relative_docs_prefix = docs_prefix.lstrip("/")
    if path_part.startswith("/") and not path_part.startswith("//"):
        path = path_part
    elif path_part == relative_docs_prefix or path_part.startswith(
        f"{relative_docs_prefix}/"
    ):
        # A few upstream pages omit the leading slash while still spelling a
        # Hugo site route (``docs/...``).  Treat that explicit docs prefix as
        # site-rooted before the generic source-relative resolver runs.
        path = f"/{path_part}"
    else:
        try:
            parsed = urlsplit(path_part)
        except ValueError:
            return None
        if parsed.scheme.lower() not in {"http", "https"} or not parsed.netloc:
            return None
        if parsed.netloc.lower() != parsed_root.netloc.lower():
            return None
        path = parsed.path or "/"
        base_path = parsed_root.path.rstrip("/")
        if base_path and (path == base_path or path.startswith(f"{base_path}/")):
            path = path[len(base_path) :] or "/"
        elif path != docs_prefix and not path.startswith(f"{docs_prefix}/"):
            # Versioned and ``latest`` Istio site URLs both point at the same
            # source route.  Remove one leading site-version component only
            # when it is immediately followed by the configured docs prefix.
            versioned_docs = re.match(r"^/[^/]+(?P<docs>/docs(?:/|$).*)$", path)
            if versioned_docs is not None:
                path = versioned_docs.group("docs")

    normalized_path = _istio_normalize_route(path)
    normalized_docs = _istio_normalize_route(docs_prefix)
    in_docs_scope = normalized_path == normalized_docs or normalized_path.startswith(
        f"{normalized_docs}/"
    )
    if in_docs_scope:
        output = site_routes.get(normalized_path)
        if output is not None:
            relative = os.path.relpath(
                output,
                start=target_rel.parent.as_posix(),
            ).replace(os.sep, "/")
            rewritten = f"{relative}{suffix}"
            return (f"<{rewritten}>" if angle else rewritten), None

        # Markdown image links are site routes too, but assets are not emitted
        # as corpus pages.  When the referenced file is present below an
        # explicit docs root, pin it to the documentation checkout commit so
        # the offline corpus never depends on a mutable site asset.
        relative_asset = normalized_path[len(normalized_docs) :].lstrip("/")
        if repo_dir is not None and Path(relative_asset).suffix.lower() in ASSET_SUFFIXES:
            for docs_root in manifest.docs_paths:
                candidate = _safe_repo_file(
                    repo_dir,
                    repo_dir / docs_root / Path(relative_asset),
                )
                if candidate is None:
                    continue
                repo_relative = candidate.relative_to(repo_dir.resolve()).as_posix()
                pinned_source = _source_url(
                    manifest,
                    quote(repo_relative, safe="/"),
                )
                rewritten = f"{pinned_source}{suffix}"
                return (f"<{rewritten}>" if angle else rewritten), None

    # Keep all out-of-scope site paths as absolute links to the verified
    # version site.  A marker is required for both an unmapped docs route and
    # a route such as /blog or /about that is intentionally outside the corpus.
    absolute = f"{site_root}{path if path.startswith('/') else f'/{path}'}{suffix}"
    marker = f"unresolved-site-link: route={normalized_path}"
    return (f"<{absolute}>" if angle else absolute), marker


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
    istio_site_routes = _istio_site_routes(manifest, source_outputs)

    def replacement(open_text: str, target: str) -> str:
        original = f"{open_text}{target})"
        target = target.strip()
        site_rewrite = _istio_site_link_rewrite(
            target,
            target_rel=target_rel,
            manifest=manifest,
            site_routes=istio_site_routes,
            repo_dir=repo_dir,
        )
        if site_rewrite is not None:
            rewritten_target, marker = site_rewrite
            suffix = f" <!-- {marker} -->" if marker else ""
            return f"{open_text}{rewritten_target}){suffix}"
        pinned_repository_url = _pinned_repository_url(manifest, target)
        if pinned_repository_url is not None:
            return f"{open_text}{pinned_repository_url})"
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
                pinned_source = _source_url(manifest, quote(repo_rel, safe="/"))
                return f"{open_text}{pinned_source}{suffix})"
        # Keep upstream prose readable when a source-relative target points to
        # a page outside the pinned documentation corpus, but make the
        # classification explicit instead of silently turning it into plain
        # text.
        return f"{original} <!-- unresolved-source-link: target={target} -->"

    # Istio pages commonly wrap a link label over multiple source lines and
    # occasionally contain a generated marker with one nested ``[... ]``
    # label.  Support that shape while fence/inline masking keeps literals
    # untouched.
    link_open_pattern = re.compile(
        r"(?P<open>!?\[(?:[^\[\]]|\[[^\[\]]*\])*\]\()"
    )
    reference_definition_pattern = re.compile(
        r"(?m)^(?P<prefix>[ \t]{0,3}\[[^\]\n]+\]:[ \t]*)(?P<rest>[^\r\n]*)(?P<newline>\r?\n|$)"
    )

    def rewrite_reference_definition(match: re.Match[str]) -> str:
        """Pin only an absolute same-repository destination in a definition."""

        original = match.group(0)
        rest = match.group("rest")
        if not rest:
            return original
        if rest.startswith("<"):
            close = rest.find(">", 1)
            if close < 0:
                return original
            target = rest[1:close]
            suffix = rest[close + 1 :]
            angle = True
        else:
            destination = re.match(r"\S+", rest)
            if destination is None:
                return original
            target = destination.group(0)
            suffix = rest[destination.end() :]
            angle = False
        if suffix and not suffix[0].isspace():
            return original
        title = suffix.strip()
        if title and not (
            (title.startswith('"') and title.endswith('"'))
            or (title.startswith("'") and title.endswith("'"))
            or (title.startswith("(") and title.endswith(")"))
        ):
            return original
        pinned = _pinned_repository_url(manifest, target)
        if pinned is None:
            return original
        destination = f"<{pinned}>" if angle else pinned
        return f"{match.group('prefix')}{destination}{suffix}{match.group('newline')}"

    def rewrite_segment(segment: str) -> str:
        literals: list[str] = []

        def protect_literal(match: re.Match[str]) -> str:
            literals.append(match.group(0))
            return f"\x00SOURCE_LINK_LITERAL_{len(literals) - 1}\x01"

        # Fences are masked by the caller.  Protect inline code, escaped Hugo
        # examples, and raw HTML blocks here as well so URL pinning cannot
        # alter source syntax shown as a literal.
        segment = re.sub(
            r"\{\{(?:[<%])?/\*.*?\*/(?:[>%])?\}\}",
            protect_literal,
            segment,
            flags=re.DOTALL,
        )
        segment = re.sub(r"(?is)<pre\b[^>]*>.*?</pre\s*>", protect_literal, segment)
        segment = re.sub(r"(?P<ticks>`+)(?P<body>[^`\n]*?)(?P=ticks)", protect_literal, segment)

        segment = reference_definition_pattern.sub(rewrite_reference_definition, segment)
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
        rewritten = "".join(output)

        # Reference definitions were handled as a whole above.  Keep malformed
        # definitions byte-for-byte unchanged and prevent the bare-URL pass
        # from partially pinning a destination that has no valid title/angle
        # boundary.
        rewritten = reference_definition_pattern.sub(protect_literal, rewritten)

        # Pin bare URLs and Markdown autolinks in ordinary prose.  The same
        # helper used by inline/reference destinations enforces exact
        # repository identity and leaves external/cross-repository URLs alone.
        def rewrite_bare_url(match: re.Match[str]) -> str:
            target = match.group("url")
            # Structural Markdown destinations were already handled above;
            # their URL starts immediately after ``](``.  Do not process it a
            # second time or append a duplicate unresolved-site marker.
            if match.start() >= 2 and rewritten[match.start() - 2 : match.start()] == "](":
                return target
            site_rewrite = _istio_site_link_rewrite(
                target,
                target_rel=target_rel,
                manifest=manifest,
                site_routes=istio_site_routes,
                repo_dir=repo_dir,
            )
            if site_rewrite is not None:
                rewritten_target, marker = site_rewrite
                suffix = f" <!-- {marker} -->" if marker else ""
                return rewritten_target + suffix
            return _pinned_repository_url(manifest, target) or target

        rewritten = re.sub(
            r"(?<![A-Za-z0-9_@])(?P<url>https?://[^\s<>\"]+)",
            rewrite_bare_url,
            rewritten,
            flags=re.IGNORECASE,
        )
        rewritten = _pin_mutable_repository_urls_in_text(manifest, rewritten)

        def restore_literal(match: re.Match[str]) -> str:
            return literals[int(match.group(1))]

        sentinel_pattern = re.compile(r"\x00SOURCE_LINK_LITERAL_(\d+)\x01")
        # A protected reference definition can itself contain a protected
        # inline-code sentinel. One substitution pass restores the outer
        # definition and exposes the inner sentinel, so continue until the
        # finite literal stack is fully expanded.
        for _ in range(len(literals) + 1):
            if sentinel_pattern.search(rewritten) is None:
                return rewritten
            rewritten = sentinel_pattern.sub(restore_literal, rewritten)
        raise ValueError("source-link literal restoration did not converge")

    masked, protected = _mask_gitbook_fences(body)
    rewritten = rewrite_segment(masked)
    for index, fence in enumerate(protected):
        rewritten = rewritten.replace(f"\x00GITBOOK_FENCE_{index}\x01", fence)
    return rewritten


def _reference_key(label: str) -> str:
    plain = re.sub(r"``([^`\n]+)``", r"\1", label)
    plain = re.sub(r"`([^`\n]+)`", r"\1", plain)
    return " ".join(plain.strip().split()).lower()


def _reference_anchor(label: str) -> str:
    plain = re.sub(r"``([^`\n]+)``", r"\1", label)
    plain = re.sub(r"`([^`\n]+)`", r"\1", plain)
    anchor = plain.lower().strip()
    anchor = re.sub(r"[^\w\s-]", "", anchor)
    anchor = re.sub(r"\s", "-", anchor)
    anchor = anchor.strip("-")
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
        if _is_fenced_markdown_line(line):
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
        if _is_fenced_markdown_line(line):
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


def _frontmatter_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def _jekyll_page_frontmatter(
    page: _JekyllPage,
    manifest: Manifest,
    fetched_at: str,
    site: dict[str, Any],
) -> str:
    """Serialize source page data plus deterministic corpus provenance."""

    # Required corpus metadata comes first for the runtime index and for human
    # inspection.  Remaining source frontmatter is retained as JSON-compatible
    # YAML scalars so cards/list data and navigation metadata remain available
    # to offline consumers.
    source_data = dict(page.metadata)
    title = str(source_data.get("title", "") or page.route.strip("/").split("/")[-1])
    aliases = list(page.redirect_aliases)
    canonical_url = page.canonical_url
    app_version = manifest.app_version or str(source_data.get("app_version", "") or "")
    chart_version = manifest.chart_version or str(source_data.get("chart_version", "") or "")
    lines = [
        "---",
        f"collection: {_frontmatter_json(manifest.collection)}",
        f"version: {_frontmatter_json(manifest.version)}",
        f"title: {_frontmatter_json(title)}",
        f"source_url: {_frontmatter_json(_source_url(manifest, page.repo_rel_path))}",
        f"fetched_at: {_frontmatter_json(fetched_at)}",
        f"source_path: {_frontmatter_json(page.repo_rel_path)}",
        f"source_commit: {_frontmatter_json(manifest.git_ref)}",
        f"renderer: {_frontmatter_json('jekyll/opensearch')}",
        f"permalink: {_frontmatter_json(page.permalink)}",
        f"canonical_url: {_frontmatter_json(canonical_url)}",
        f"canonical_route: {_frontmatter_json(page.canonical_route)}",
        f"redirect_from: {_frontmatter_json(aliases)}",
        f"canonical_collision: {_frontmatter_json(page.canonical_collision)}",
        f"source_config_opensearch_version: {_frontmatter_json(site.get('opensearch_version', ''))}",
        f"source_config_opensearch_dashboards_version: {_frontmatter_json(site.get('opensearch_dashboards_version', ''))}",
        f"app_version: {_frontmatter_json(app_version)}",
        f"chart_version: {_frontmatter_json(chart_version)}",
    ]
    for key in sorted(source_data):
        if key in {
            "collection",
            "version",
            "title",
            "source_url",
            "fetched_at",
            "source_path",
            "source_commit",
            "renderer",
            "permalink",
            "canonical_url",
            "canonical_route",
            "redirect_from",
            "canonical_collision",
            "source_config_opensearch_version",
            "source_config_opensearch_dashboards_version",
            "app_version",
            "chart_version",
        }:
            continue
        lines.append(f"{key}: {_frontmatter_json(source_data[key])}")
    lines.extend(["---", ""])
    return "\n".join(lines)


def _normalize_jekyll(manifest: Manifest) -> None:
    """Normalize an OpenSearch documentation-website checkout."""

    repo_dir = manifest.raw_dir / "repo"
    if not repo_dir.exists():
        print(f"[{manifest.name}] raw repo not found at {repo_dir}. Please run fetch first.", file=sys.stderr)
        sys.exit(1)
    files = _discover_jekyll_source_files(manifest, repo_dir)
    if not files:
        print(
            f"[{manifest.name}] Error: no processable Jekyll documentation files found in docs_paths: {manifest.docs_paths}",
            file=sys.stderr,
        )
        sys.exit(1)
    registry = _build_jekyll_registry(manifest, repo_dir)
    peer_registry = _peer_jekyll_registry(manifest)
    config = _jekyll_config(repo_dir)

    meta_file = manifest.raw_dir / "git_meta.json"
    fetched_at = ""
    if meta_file.exists():
        try:
            fetched_at = str(json.loads(meta_file.read_text(encoding="utf-8")).get("fetched_at", ""))
        except (OSError, TypeError, ValueError):
            fetched_at = ""
    if not fetched_at:
        fetched_at = get_git_commit_date(repo_dir)

    rendered_pages: list[tuple[_JekyllPage, str, dict[str, int]]] = []
    for page in registry.pages:
        try:
            raw_text = page.file_path.read_text(encoding="utf-8", errors="replace")
        except OSError as error:
            raise JekyllRenderError(f"cannot read source page: {error}", page.file_path) from error
        source_data, body = parse_jekyll_frontmatter(raw_text, Path(page.repo_rel_path).stem)
        # Registry metadata and the body parse intentionally come from the
        # same source file; this guards against a source changing between the
        # two read operations during a local rebuild.
        if source_data != page.metadata:
            raise JekyllRenderError("frontmatter changed while building registry", page.file_path)
        try:
            rendered = render_jekyll_template(
                body,
                repo_dir,
                manifest=manifest,
                page_data=source_data,
                source_path=page.file_path,
            )
            rendered, link_stats = _rewrite_jekyll_links(
                rendered,
                page,
                registry,
                peer_registry,
                repo_dir,
            )
        except JekyllRenderError:
            raise
        residual = validate_no_residual_template_syntax(rendered)
        if residual:
            raise JekyllRenderError(
                f"non-code Liquid/Kramdown residuals: {', '.join(residual[:4])}", page.file_path
            )
        rendered = re.sub(r"[ \t]+$", "", rendered, flags=re.MULTILINE)
        rendered = re.sub(r"\n{3,}", "\n\n", rendered).strip() + "\n"
        output = _jekyll_page_frontmatter(page, manifest, fetched_at, config) + rendered
        rendered_pages.append((page, redact_secret_like_examples(output), link_stats))

    corpus_dir = manifest.corpus_dir
    expected = {Path(page.output_rel_path) for page, _, _ in rendered_pages}
    # Only derived Markdown under this exact corpus version is eligible for
    # stale cleanup.  Raw checkouts and unrelated corpus versions are never
    # touched.
    if corpus_dir.is_dir():
        for old in corpus_dir.rglob("*.md"):
            if old.relative_to(corpus_dir) not in expected:
                old.unlink()
    for page, output, _ in rendered_pages:
        out_path = corpus_dir / page.output_rel_path
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output, encoding="utf-8")
    # Removing stale files can leave a tree of empty directories after a
    # permalink change.  Prune only empty directories below this exact
    # collection/version; never remove the version root itself or touch raw
    # checkouts and sibling corpus versions.
    if corpus_dir.is_dir():
        directories = sorted(
            (path for path in corpus_dir.rglob("*") if path.is_dir()),
            key=lambda path: len(path.relative_to(corpus_dir).parts),
            reverse=True,
        )
        for directory in directories:
            try:
                directory.rmdir()
            except OSError:
                pass

    stats = {
        "unresolved": sum(item[2]["unresolved"] for item in rendered_pages),
        "cross_corpus": sum(item[2]["cross_corpus"] for item in rendered_pages),
        "assets": sum(item[2]["assets"] for item in rendered_pages),
    }
    collisions = len(registry.route_collisions)
    print(
        f"[{manifest.name}] discovered={len(files)} source={len(registry.pages)} "
        f"unique={registry.unique_routes} corpus={len(rendered_pages)} "
        f"canonical_collisions={collisions} unresolved={stats['unresolved']} "
        f"unresolved_cross_corpus={stats['cross_corpus']} pinned_assets={stats['assets']}"
    )


def normalize(manifest: Manifest) -> None:
    """Normalize 階段：將 repo 內的 Markdown/HTML 文件轉入 corpus。"""
    if manifest.shortcode_profile in {"jekyll", "opensearch", "opensearch-jekyll"}:
        _normalize_jekyll(manifest)
        return

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

    is_gitlab = manifest.collection == "gitlab"
    shortcode_profile = manifest.shortcode_profile or (
        "kubernetes" if manifest.collection == "k8s" else ""
    )

    files_to_process = _discover_source_files(manifest, repo_dir)
    if not files_to_process:
        print(
            f"[{manifest.name}] Error: no processable documentation files found in docs_paths: {manifest.docs_paths}",
            file=sys.stderr,
        )
        sys.exit(1)

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
        preserve_description = bool(
            manifest.preserve_description and manifest.shortcode_profile == "istio"
        )
        description = (
            extract_frontmatter_description(raw_text)
            if preserve_description and file_path.suffix.lower() in {".md", ".markdown"}
            else ""
        )

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
            if description and not body.strip():
                body = description

        if shortcode_profile:
            body = clean_hugo_shortcodes(
                body,
                repo_dir,
                profile=shortcode_profile,
                source_path=file_path,
            )
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

        frontmatter_lines = [
            "---",
            f"collection: {manifest.collection}",
            f'version: "{manifest.version}"',
            f"title: {json.dumps(title, ensure_ascii=False)}",
            f"source_url: {source_url}",
            f"fetched_at: {fetched_at}",
        ]
        if manifest.app_version:
            # Keep the application/document-line distinction explicit for
            # generic Git sources whose manifest represents a frozen docs
            # branch rather than the app release itself.
            frontmatter_lines.append(
                f"app_version: {json.dumps(manifest.app_version, ensure_ascii=False)}"
            )
        if manifest.chart_version:
            frontmatter_lines.append(
                f"chart_version: {json.dumps(manifest.chart_version, ensure_ascii=False)}"
            )
        if description:
            frontmatter_lines.append(
                f"description: {json.dumps(description, ensure_ascii=False)}"
            )
        frontmatter_lines.extend(["---", ""])
        frontmatter = "\n".join(frontmatter_lines)

        out_path.write_text(
            redact_secret_like_examples(frontmatter + body),
            encoding="utf-8",
        )
        written += 1

    if written == 0:
        print(f"[{manifest.name}] Error: 0 pages written to corpus.", file=sys.stderr)
        sys.exit(1)

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
