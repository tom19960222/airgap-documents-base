"""將固定版本的 OpenCode MDX 與 OpenAPI 文件轉成可離線搜尋的 Markdown。"""

from __future__ import annotations

import html
import json
import os
import re
import textwrap
from pathlib import Path
from urllib.parse import urlsplit


def _mask_literals(content: str) -> tuple[str, list[str]]:
    if "\x00" in content:
        raise ValueError("OpenCode MDX 不接受 NUL 字元")
    protected: list[str] = []

    def protect(value: str) -> str:
        protected.append(value)
        return f"\x00OPENCODE_{len(protected) - 1}\x01"

    lines = content.splitlines(keepends=True)
    output: list[str] = []
    index = 0
    while index < len(lines):
        opener = re.match(r"^[ \t]*(`{3,}|~{3,})[^\n]*\n?$", lines[index])
        if opener is None:
            output.append(lines[index])
            index += 1
            continue
        marker = opener.group(1)
        block = [lines[index]]
        index += 1
        while index < len(lines):
            line = lines[index]
            block.append(line)
            index += 1
            if re.fullmatch(r"\s*" + re.escape(marker[0]) + "{" + str(len(marker)) + r",}\s*", line):
                break
        # MDX 的 TabItem 會縮排整個 code block；移除共同縮排，保留程式碼相對縮排。
        output.append(protect(textwrap.dedent("".join(block))) + "\n")
    masked = "".join(output)
    masked = re.sub(r"(?P<ticks>`+)[^`\n]*?(?P=ticks)", lambda m: protect(m.group()), masked)
    return masked, protected


def _attribute(attributes: str, name: str, default: str = "") -> str:
    match = re.search(r"\b" + re.escape(name) + r'''\s*=\s*(["'])(.*?)\1''', attributes, re.DOTALL)
    return html.unescape(match.group(2)) if match else default


def _code_tabs(match: re.Match[str]) -> str:
    # 只解析官方固定來源使用的 string-only literal；不執行 JavaScript。
    attributes = match.group(1)
    tabs = re.search(r"\btabs\s*=\s*\{\s*\[(.*?)\]\s*\}", attributes, re.DOTALL)
    if tabs is None:
        raise ValueError("OpenCode CodeTabs 缺少 tabs literal")
    string = r'"(?:[^"\\]|\\.)*"'
    entry = re.compile(r"\{\s*label:\s*(" + string + r"),\s*code:\s*(" + string + r"),?\s*\}")
    output = []
    cursor = 0
    for item in entry.finditer(tabs.group(1)):
        if tabs.group(1)[cursor:item.start()].strip(" \t\r\n,"):
            raise ValueError("OpenCode CodeTabs 包含未支援的 literal")
        label, code = (json.loads(item.group(n)) for n in (1, 2))
        fence = "`" * max(3, max((len(s) + 1 for s in re.findall(r"`+", code)), default=3))
        output.append(f"\n\n**{label}**\n\n{fence}bash\n{code}\n{fence}\n\n")
        cursor = item.end()
    if not output or tabs.group(1)[cursor:].strip(" \t\r\n,"):
        raise ValueError("OpenCode CodeTabs 包含未支援的 literal")
    return "".join(output)


def render_mdx(content: str, variables: dict[str, object]) -> str:
    """保留正文、所有 tab 與 code；將頁面元件轉成純 Markdown，不執行 MDX。"""
    text, protected = _mask_literals(content)
    values: dict[str, str] = {}

    def export(match: re.Match[str]) -> str:
        name, expression = match.group(1), match.group(2).strip().rstrip(";")
        if expression.startswith("config."):
            key = expression.removeprefix("config.")
            if key not in variables:
                raise ValueError(f"OpenCode 缺少 config.{key}")
            values[name] = str(variables[key])
        elif expression.startswith("\x00OPENCODE_"):
            # Template literal 先前被當成 inline code 保護，僅允許 config substitution。
            marker = re.fullmatch(r"\x00OPENCODE_(\d+)\x01", expression)
            if marker is None:
                raise ValueError(f"OpenCode 未支援的 export: {name}")
            literal = protected[int(marker.group(1))][1:-1]

            def config_value(value: re.Match[str]) -> str:
                key = value.group(1)
                if key not in variables:
                    raise ValueError(f"OpenCode 缺少 config.{key}")
                return str(variables[key])

            literal = re.sub(r"\$\{config\.(\w+)\}", config_value, literal)
            if "${" in literal:
                raise ValueError(f"OpenCode 未支援的 template: {name}")
            values[name] = literal
        else:
            values[name] = json.loads(expression)
        return ""

    text = re.sub(r"(?m)^export const (\w+)\s*=\s*(.+)$", export, text)
    text = re.sub(r"(?m)^import [^\n]+\n?", "", text)

    def anchor(match: re.Match[str]) -> str:
        variable, label = match.group(1), match.group(2)
        if variable not in values:
            raise ValueError(f"OpenCode 未定義 href: {variable}")
        label = re.sub(r"</?code>", "`", label)
        return f"[{label}]({values[variable]})"

    text = re.sub(r"<a\s+href=\{(\w+)\}>(.*?)</a>", anchor, text, flags=re.DOTALL)
    text = re.sub(r"<CodeTabs\b(.*?)/>", _code_tabs, text, flags=re.DOTALL)

    def tab(match: re.Match[str]) -> str:
        return f"\n\n**{_attribute(match.group(1), 'label')}**\n\n{textwrap.dedent(match.group(2)).strip()}\n\n"

    text = re.sub(r"<TabItem\b([^>]*)>(.*?)</TabItem>", tab, text, flags=re.DOTALL)
    text = re.sub(
        r'<div\s+slot="(go|go-plus)">(.*?)</div>',
        lambda m: f"\n\n**{'Go Plus' if m.group(1) == 'go-plus' else 'Go'}**\n\n{textwrap.dedent(m.group(2)).strip()}\n\n",
        text, flags=re.DOTALL,
    )
    text = re.sub(r"<Callout\b([^>]*)>", lambda m: f"\n\n**{_attribute(m.group(1), 'type', 'note').capitalize()}:**\n\n", text)
    text = re.sub(r"</Callout>", "\n\n", text)
    text = re.sub(
        r"<Card\b([^>]*)>",
        lambda m: f"\n\n[{_attribute(m.group(1), 'title')}]({_attribute(m.group(1), 'href')})\n\n",
        text,
    )
    text = re.sub(r"</?(?:Tabs|Steps|PlanTabs|CardGroup|Card)\b[^>]*>", "\n", text)
    text = re.sub(r"</?div\b[^>]*>", "\n", text)
    text = re.sub(
        r"(?m)^\s*:::(\w+)(?:\[([^\]]+)\])?\s*$",
        lambda m: f"\n**{m.group(1).capitalize()}{': ' + m.group(2) if m.group(2) else ''}:**\n",
        text,
    )
    text = re.sub(r"(?m)^\s*:::\s*$", "\n", text)
    unknown = re.search(r"(?<!\\)</?[A-Z][\w.]*\b[^>]*>", text)
    if unknown:
        raise ValueError(f"OpenCode 未支援的 MDX component: {unknown.group()}")
    for index in range(len(protected) - 1, -1, -1):
        text = text.replace(f"\x00OPENCODE_{index}\x01", protected[index])
    return text


def rewrite_site_links(body: str, target_rel: Path, source_outputs: dict[str, str], manifest) -> str:
    """將兩代網站 route 對應到同版本 corpus；保留 query 與 fragment。"""
    routes = {}
    for output in source_outputs.values():
        path = Path(output)
        route = path.with_suffix("").as_posix()
        if path.name == "index.md":
            route = path.parent.as_posix()
        routes["/" + route.strip("./")] = output
    if "api.md" in source_outputs.values():
        routes["/api"] = "api.md"
    base = str(manifest.site_overrides["docs_url"]).rstrip("/")
    is_v1 = manifest.version.startswith("1.")
    text, protected = _mask_literals(body)

    def destination(match: re.Match[str]) -> str:
        target = match.group(2)
        parsed = urlsplit(target)
        path = parsed.path
        if parsed.netloc:
            if parsed.netloc not in {"opencode.ai", "dev.opencode.ai"}:
                return match.group()
            prefixes = ("/docs",) if is_v1 else ("/v2/docs",)
            if not any(path == prefix or path.startswith(prefix + "/") for prefix in prefixes):
                return match.group()
        elif not path.startswith("/") or path.startswith("//"):
            return match.group()
        for prefix in (("/docs",) if is_v1 else ("/v2/docs", "/docs")):
            if path == prefix or path.startswith(prefix + "/"):
                path = path[len(prefix):] or "/"
                break
        route = path.rstrip("/") or "/"
        suffix = ("?" + parsed.query if parsed.query else "") + ("#" + parsed.fragment if parsed.fragment else "")
        if route in routes:
            output = os.path.relpath(routes[route], target_rel.parent).replace(os.sep, "/")
            return f"{match.group(1)}{output}{suffix})"
        absolute = base + (path if path.startswith("/") else "/" + path) + suffix
        return f"{match.group(1)}{absolute}) <!-- unresolved-site-link: route={route} -->"

    text = re.sub(r"(!?\[(?:[^\[\]]|\[[^\[\]]*\])*\]\()([^\s)]*)\)", destination, text)
    for index in range(len(protected) - 1, -1, -1):
        text = text.replace(f"\x00OPENCODE_{index}\x01", protected[index])
    return text


def render_openapi(content: str) -> tuple[str, str]:
    """將完整 JSON 分段保存，不遺漏 path metadata、operation 或 component。"""
    schema = json.loads(content)
    if not str(schema.get("openapi", "")).startswith("3."):
        raise ValueError("OpenCode API 文件必須是 OpenAPI 3.x")

    def block(value: object) -> str:
        encoded = json.dumps(value, ensure_ascii=False, indent=2)
        fence = "`" * max(3, max((len(s) + 1 for s in re.findall(r"`+", encoded)), default=3))
        return f"\n{fence}json\n{encoded}\n{fence}\n"

    output = ["# HTTP API\n", "## Overview\n", block({k: v for k, v in schema.items() if k not in {"paths", "components"}})]
    methods = {"get", "post", "put", "patch", "delete", "options", "head", "trace"}
    for path, item in schema.get("paths", {}).items():
        output.append(f"\n## {path}\n")
        metadata = {k: v for k, v in item.items() if k not in methods}
        if metadata:
            output.append(block(metadata))
        for method, operation in item.items():
            if method not in methods:
                continue
            identifier = operation.get("operationId", f"{method}-{path}")
            output.append(f'\n<a id="{html.escape(identifier, quote=True)}"></a>\n\n### {method.upper()} {path} — {identifier}\n')
            output.append(block(operation))
    for category, items in schema.get("components", {}).items():
        if category == "schemas":
            output.append('\n<a id="schemas"></a>\n')
        output.append(f"\n## Components: {category}\n")
        if isinstance(items, dict):
            for name, value in items.items():
                if category == "schemas":
                    output.append(f'\n<a id="schema-{html.escape(name, quote=True)}"></a>\n')
                output.append(f"\n### {name}\n")
                output.append(block(value))
        else:
            output.append(block(items))
    return "HTTP API", "\n".join(output)
