"""建置端共用邏輯：manifest 載入、URL 正規化與路徑對映。"""

from __future__ import annotations

import hashlib
import tomllib
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urldefrag, urljoin, urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent

# 明顯不是文件頁的副檔名，crawl 階段直接跳過
NON_HTML_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".css", ".js",
    ".pdf", ".zip", ".gz", ".tgz", ".whl", ".epub", ".txt", ".xml",
    ".json", ".woff", ".woff2", ".ttf", ".eot", ".map", ".mp4", ".webm",
}


@dataclass
class Manifest:
    name: str
    collection: str
    version: str
    base_url: str = ""
    content_selector: str = ""
    deny_prefixes: list[str] = field(default_factory=list)
    max_pages: int = 5000
    delay_seconds: float = 0.5
    source_type: str = "html"
    repo_url: str = ""
    git_ref: str = ""
    docs_paths: list[str] = field(default_factory=list)
    sparse_paths: list[str] = field(default_factory=list)
    source_url_template: str = ""

    @property
    def raw_dir(self) -> Path:
        return REPO_ROOT / "raw" / self.collection / self.version

    @property
    def corpus_dir(self) -> Path:
        return REPO_ROOT / "corpus" / self.collection / self.version


def load_manifest(path: str | Path) -> Manifest:
    data = tomllib.loads(Path(path).read_text())
    return Manifest(**data)


def canonicalize(url: str, page_url: str) -> str:
    """把頁面內的連結轉成絕對 URL，去掉 fragment 與 query。壞 URL 回空字串。"""
    try:
        absolute = urljoin(page_url, url)
        absolute, _ = urldefrag(absolute)
        parsed = urlparse(absolute)
        return parsed._replace(query="").geturl()
    except ValueError:  # 例如頁面上寫壞的 IPv6 bracket URL
        return ""


def in_scope(url: str, manifest: Manifest) -> bool:
    if not url.startswith(manifest.base_url):
        return False
    rel = url[len(manifest.base_url):]
    if any(rel.startswith(p) for p in manifest.deny_prefixes):
        return False
    suffix = Path(urlparse(url).path).suffix.lower()
    if suffix and suffix not in {".html", ".htm"}:
        if suffix in NON_HTML_SUFFIXES:
            return False
    return True


def url_to_relpath(url: str, manifest: Manifest) -> Path:
    """URL → corpus 內的相對 .md 路徑。`a/b.html` → `a/b.md`，`a/` → `a/index.md`。"""
    rel = url[len(manifest.base_url):]
    if rel == "" or rel.endswith("/"):
        rel += "index.html"
    path = Path(rel)
    if path.suffix.lower() in {".html", ".htm"}:
        path = path.with_suffix(".md")
    else:
        path = path.with_name(path.name + ".md")
    return path


def url_key(url: str) -> str:
    """raw archive 的檔名 key。"""
    return hashlib.sha256(url.encode()).hexdigest()[:16]
