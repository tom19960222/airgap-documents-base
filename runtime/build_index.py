"""corpus/ → index/docs.db（FTS5）。純 Python 標準庫，air-gap 端 pull 完後執行。

用法：python runtime/build_index.py
"""

from __future__ import annotations

import json
import re
import sqlite3
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = REPO_ROOT / "corpus"
DB_PATH = REPO_ROOT / "index" / "docs.db"

MAX_CHUNK_CHARS = 6000

SCHEMA = """
CREATE TABLE chunks (
  id INTEGER PRIMARY KEY,
  chunk_id TEXT UNIQUE,
  collection TEXT NOT NULL,
  version TEXT NOT NULL,
  page_path TEXT NOT NULL,
  title TEXT NOT NULL,
  section_path TEXT NOT NULL,
  source_url TEXT NOT NULL,
  content TEXT NOT NULL
);
CREATE VIRTUAL TABLE chunks_fts USING fts5(
  title, section_path, content,
  content='chunks', content_rowid='id',
  tokenize='porter unicode61'
);
"""


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.index("\n---\n", 4)
    meta = {}
    for line in text[4:end].splitlines():
        key, _, value = line.partition(":")
        value = value.strip()
        if value.startswith('"'):
            value = json.loads(value)
        meta[key.strip()] = value
    return meta, text[end + 5:]


def slugify(heading: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", heading.lower()).strip("-")
    return slug or "section"


def split_sections(body: str) -> list[tuple[list[str], str]]:
    """以 H1–H3 切 section，回傳 (heading 路徑, 內容) 列表。"""
    sections: list[tuple[list[str], list[str]]] = []
    stack: list[tuple[int, str]] = []
    current: list[str] = []
    in_fence = False

    def push():
        if current and "".join(current).strip():
            sections.append(([h for _, h in stack], current[:]))

    for line in body.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
        match = None if in_fence else re.match(r"^(#{1,3}) (.+)$", line)
        if match:
            push()
            current = []
            level = len(match.group(1))
            heading = match.group(2).strip()
            while stack and stack[-1][0] >= level:
                stack.pop()
            stack.append((level, heading))
        else:
            current.append(line)
    push()
    return [(path, "\n".join(lines).strip()) for path, lines in sections]


def split_oversized(content: str) -> list[str]:
    if len(content) <= MAX_CHUNK_CHARS:
        return [content]
    # 從字元中點往後找換行來切；沒有換行（單一超長行）就硬切字元，保證兩段都變短
    mid = content.find("\n", len(content) // 2)
    if mid == -1 or mid == 0 or mid >= len(content) - 1:
        mid = len(content) // 2
    top = content[:mid].strip()
    bottom = content[mid:].strip()
    if not top or not bottom:
        return [content[:MAX_CHUNK_CHARS]]
    return split_oversized(top) + split_oversized(bottom)


def index_page(cursor: sqlite3.Cursor, md_path: Path) -> int:
    meta, body = parse_frontmatter(md_path.read_text())
    page_path = md_path.relative_to(CORPUS_DIR).as_posix()
    count = 0
    used_ids: set[str] = set()
    for section_path, content in split_sections(body):
        heading = section_path[-1] if section_path else meta.get("title", "")
        for part in split_oversized(content):
            chunk_id = f"{page_path}#{slugify(heading)}"
            serial = 1
            while chunk_id in used_ids:
                serial += 1
                chunk_id = f"{page_path}#{slugify(heading)}-{serial}"
            used_ids.add(chunk_id)
            cursor.execute(
                "INSERT INTO chunks (chunk_id, collection, version, page_path, title,"
                " section_path, source_url, content) VALUES (?,?,?,?,?,?,?,?)",
                (
                    chunk_id,
                    meta.get("collection", ""),
                    meta.get("version", ""),
                    page_path,
                    meta.get("title", ""),
                    " > ".join(section_path),
                    meta.get("source_url", ""),
                    part,
                ),
            )
            count += 1
    return count


def main() -> None:
    if not CORPUS_DIR.exists():
        sys.exit(f"corpus not found: {CORPUS_DIR}")
    DB_PATH.parent.mkdir(exist_ok=True)
    DB_PATH.unlink(missing_ok=True)
    db = sqlite3.connect(DB_PATH)
    db.executescript(SCHEMA)
    cursor = db.cursor()
    pages = chunks = 0
    for md_path in sorted(CORPUS_DIR.rglob("*.md")):
        chunks += index_page(cursor, md_path)
        pages += 1
    cursor.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')")
    db.commit()
    print(f"indexed {pages} pages, {chunks} chunks -> {DB_PATH}")


if __name__ == "__main__":
    main()
