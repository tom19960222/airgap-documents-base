"""corpus/ → index/docs.db（FTS5）。純 Python 標準庫，air-gap 端 pull 完後執行。

用法：python runtime/build_index.py [--full]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sqlite3
import sys
import tempfile
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = REPO_ROOT / "corpus"
DB_PATH = REPO_ROOT / "index" / "docs.db"

MAX_CHUNK_CHARS = 6000
# 修改切段、metadata 或索引規則時遞增，讓既有資料庫自動重建。
INDEX_VERSION = 1

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
CREATE INDEX chunks_page_path ON chunks(page_path);
CREATE TABLE pages (
  page_path TEXT PRIMARY KEY,
  sha256 TEXT NOT NULL,
  chunk_count INTEGER NOT NULL
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


def index_page(cursor: sqlite3.Cursor, md_path: Path,
               corpus_dir: Path = CORPUS_DIR, text: str | None = None) -> int:
    meta, body = parse_frontmatter(
        md_path.read_text(encoding="utf-8") if text is None else text
    )
    page_path = md_path.relative_to(corpus_dir).as_posix()
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


def build_index(corpus_dir: Path = CORPUS_DIR, db_path: Path = DB_PATH,
                *, full: bool = False) -> dict:
    """以內容雜湊增量更新；完整重建成功後才替換舊資料庫。"""
    started = time.perf_counter()
    if not corpus_dir.is_dir():
        raise FileNotFoundError(f"corpus not found: {corpus_dir}")
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if not full and db_path.exists():
        with sqlite3.connect(db_path) as existing:
            full = existing.execute("PRAGMA user_version").fetchone()[0] != INDEX_VERSION
        existing.close()
    else:
        full = True

    temp_path = None
    if full:
        fd, name = tempfile.mkstemp(prefix=db_path.name + ".", suffix=".tmp",
                                    dir=db_path.parent)
        os.close(fd)
        temp_path = Path(name)
    db = sqlite3.connect(temp_path or db_path)
    stats = dict(mode="full" if full else "incremental", added=0, modified=0,
                 deleted=0, skipped=0, scan_seconds=0.0, update_seconds=0.0)
    try:
        if full:
            db.executescript(SCHEMA)
            db.execute(f"PRAGMA user_version = {INDEX_VERSION}")
        # 一次交易包含文件紀錄、chunks 與 FTS；中途錯誤全部回復。
        db.execute("BEGIN IMMEDIATE")
        cursor = db.cursor()
        known = {path: (digest, count) for path, digest, count in
                 cursor.execute("SELECT page_path, sha256, chunk_count FROM pages")}
        scan_start = time.perf_counter()
        paths = sorted(corpus_dir.rglob("*.md"))
        stats["scan_seconds"] += time.perf_counter() - scan_start
        total_chunks = 0
        for path in paths:
            scan_start = time.perf_counter()
            data = path.read_bytes()
            digest = hashlib.sha256(data).hexdigest()
            page_path = path.relative_to(corpus_dir).as_posix()
            previous = known.pop(page_path, None)
            stats["scan_seconds"] += time.perf_counter() - scan_start
            if previous and previous[0] == digest:
                stats["skipped"] += 1
                total_chunks += previous[1]
                continue
            update_start = time.perf_counter()
            if previous:
                remove_page(cursor, page_path)
            # 和 read_text 一樣正規化換行；雜湊與解析使用同一次讀取。
            text = data.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
            count = index_page(cursor, path, corpus_dir, text)
            cursor.execute("INSERT OR REPLACE INTO pages VALUES (?, ?, ?)",
                           (page_path, digest, count))
            if not full:
                cursor.execute(
                    "INSERT INTO chunks_fts(rowid, title, section_path, content) "
                    "SELECT id, title, section_path, content FROM chunks WHERE page_path = ?",
                    (page_path,),
                )
            stats["modified" if previous else "added"] += 1
            total_chunks += count
            stats["update_seconds"] += time.perf_counter() - update_start
        update_start = time.perf_counter()
        for page_path in known:
            remove_page(cursor, page_path)
            cursor.execute("DELETE FROM pages WHERE page_path = ?", (page_path,))
        stats["deleted"] = len(known)
        stats["update_seconds"] += time.perf_counter() - update_start
        fts_start = time.perf_counter()
        if full:
            cursor.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')")
        stats["fts_rebuild_seconds"] = time.perf_counter() - fts_start
        commit_start = time.perf_counter()
        db.commit()
        stats["commit_seconds"] = time.perf_counter() - commit_start
        stats.update(pages=len(paths), chunks=total_chunks)
    except BaseException:
        db.rollback()
        raise
    finally:
        db.close()
        # 成功替換前，錯誤時也清掉暫存檔。
        if temp_path and sys.exc_info()[0] is not None:
            temp_path.unlink(missing_ok=True)
    if temp_path:
        try:
            temp_path.replace(db_path)
        finally:
            temp_path.unlink(missing_ok=True)
    stats["total_seconds"] = time.perf_counter() - started
    return stats


def remove_page(cursor: sqlite3.Cursor, page_path: str) -> None:
    # external-content FTS 的刪除指令需要原文，必須先於 chunks 刪除。
    cursor.execute(
        "INSERT INTO chunks_fts(chunks_fts, rowid, title, section_path, content) "
        "SELECT 'delete', id, title, section_path, content FROM chunks WHERE page_path = ?",
        (page_path,),
    )
    cursor.execute("DELETE FROM chunks WHERE page_path = ?", (page_path,))


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the documentation index incrementally.")
    parser.add_argument("--full", action="store_true", help="rebuild the entire index")
    args = parser.parse_args()
    stats = build_index(full=args.full)
    print(f"{stats['mode']}: indexed {stats['pages']} pages, {stats['chunks']} chunks -> {DB_PATH}")
    print("pages: " + ", ".join(f"{key}={stats[key]}" for key in
                                ("added", "modified", "deleted", "skipped")))
    print("timing: " + ", ".join(
        f"{key.removesuffix('_seconds')}={stats[key]:.3f}s" for key in
        ("scan_seconds", "update_seconds", "fts_rebuild_seconds", "commit_seconds", "total_seconds")))


if __name__ == "__main__":
    main()
