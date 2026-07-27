"""raw archive → corpus Markdown。

用法：python normalize.py manifests/ceph-19.toml

不需要網路；改了轉換邏輯直接重跑即可（raw 不會被動到）。
"""

from __future__ import annotations

import argparse
import gzip
import json
import os
import re
from pathlib import PurePosixPath
from urllib.parse import urldefrag, urljoin

from bs4 import BeautifulSoup
from markdownify import MarkdownConverter

from common import Manifest, canonicalize, in_scope, load_manifest, url_key, url_to_relpath


def code_language(el, _style=None) -> str:
    """從 Sphinx 的 <div class="highlight-yaml ..."> 外層找語言標記。"""
    for parent in el.parents:
        for cls in parent.get("class") or []:
            if cls.startswith("highlight-"):
                lang = cls.removeprefix("highlight-")
                return "" if lang in {"default", "none", "text", "notranslate"} else lang
    return ""


class SphinxConverter(MarkdownConverter):
    def convert_pre(self, el, text, parent_tags=None):
        if not text:
            return ""
        lang = code_language(el)
        body = text.strip("\n")
        return f"\n\n```{lang}\n{body}\n```\n\n"


def rewrite_links(main, page_url: str, page_relpath: PurePosixPath, manifest: Manifest) -> None:
    """站內連結改寫成 corpus 內的相對 .md 路徑，站外保留絕對 URL。"""
    for a in main.find_all("a", href=True):
        absolute = urljoin(page_url, a["href"])
        _, fragment = urldefrag(absolute)
        canonical = canonicalize(a["href"], page_url)  # 去 fragment/query，與 crawl 的頁面身分一致
        if in_scope(canonical, manifest) and canonical.startswith(manifest.base_url):
            target_relpath = PurePosixPath(url_to_relpath(canonical, manifest).as_posix())
            rel = os.path.relpath(target_relpath, start=page_relpath.parent)
            a["href"] = rel + (f"#{fragment}" if fragment else "")
        else:
            a["href"] = absolute  # 原樣保留（已含 query/fragment）


def transform_admonitions(main) -> None:
    """Sphinx admonition → blockquote，標題轉成 **Note:** 這類前綴。"""
    for box in main.find_all("div", class_="admonition"):
        title = box.find("p", class_="admonition-title")
        if title:
            label = title.get_text(strip=True)
            title.string = f"{label}:"
            title.name = "strong"
        box.name = "blockquote"


def clean(main) -> None:
    # #banner: Ansible 的 unmaintained-version 警告；Report_Documentation_Bugs: Ceph 的回報連結
    for el in main.select(
        'a.headerlink, script, style, #banner, a[href*="Report_Documentation_Bugs"]'
    ):
        el.decompose()


def page_title(main, soup) -> str:
    h1 = main.find("h1")
    if h1:
        return h1.get_text(" ", strip=True)
    if soup.title:
        return soup.title.get_text(" ", strip=True)
    return "(untitled)"


def to_markdown(html: str, page_url: str, manifest: Manifest) -> tuple[str, str] | None:
    soup = BeautifulSoup(html, "lxml")
    main = soup.select_one(manifest.content_selector)
    if main is None:
        return None
    page_relpath = PurePosixPath(url_to_relpath(page_url, manifest).as_posix())
    clean(main)
    transform_admonitions(main)
    rewrite_links(main, page_url, page_relpath, manifest)
    title = page_title(main, soup)
    converter = SphinxConverter(heading_style="ATX", bullets="-", escape_underscores=False)
    markdown = converter.convert_soup(main)
    markdown = re.sub(r"\n{3,}", "\n\n", markdown).strip() + "\n"
    return title, markdown


def normalize(manifest: Manifest) -> None:
    pages_dir = manifest.raw_dir / "pages"
    index_path = manifest.raw_dir / "pages.jsonl"
    written = skipped = 0

    for line in index_path.read_text().splitlines():
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not entry.get("archived"):
            continue
        html_path = pages_dir / f"{url_key(entry['url'])}.html.gz"
        if not html_path.exists():
            continue
        html = gzip.decompress(html_path.read_bytes()).decode("utf-8", "replace")
        result = to_markdown(html, entry["url"], manifest)
        if result is None:
            skipped += 1
            continue
        title, markdown = result
        out_path = manifest.corpus_dir / url_to_relpath(entry["url"], manifest)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        frontmatter = "\n".join([
            "---",
            f"collection: {manifest.collection}",
            f'version: "{manifest.version}"',
            f"title: {json.dumps(title, ensure_ascii=False)}",
            f"source_url: {entry['url']}",
            f"fetched_at: {entry.get('fetched_at', '')}",
            "---",
            "",
        ])
        out_path.write_text(frontmatter + markdown)
        written += 1

    print(f"[{manifest.name}] corpus written: {written} pages, skipped (no main content): {skipped}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest")
    args = parser.parse_args()
    normalize(load_manifest(args.manifest))


if __name__ == "__main__":
    main()
