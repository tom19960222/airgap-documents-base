"""corpus/ → index/docs.db（FTS5）。純 Python 標準庫，air-gap 端 pull 完後執行。

用法：python runtime/build_index.py [--full] [--verify-content] [--jobs N]
"""

from __future__ import annotations

import argparse
import hashlib
import json
import multiprocessing
import os
import re
import sqlite3
import sys
import tempfile
import time
from collections import deque
from concurrent.futures import ProcessPoolExecutor
from contextlib import closing
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_DIR = REPO_ROOT / "corpus"
DB_PATH = REPO_ROOT / "index" / "docs.db"

MAX_CHUNK_CHARS = 6000
PAGES_PER_BATCH = 32
HEADING_RE = re.compile(r"^(#{1,3}) (.+)$")
SLUG_RE = re.compile(r"[^a-z0-9]+")
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
  chunk_count INTEGER NOT NULL,
  fingerprint TEXT
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
    slug = SLUG_RE.sub("-", heading.lower()).strip("-")
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
        match = HEADING_RE.match(line) if not in_fence and line.startswith("#") else None
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


def page_chunks(page_path: str, text: str) -> list[tuple]:
    """純解析：產生固定順序的 chunks，不碰資料庫。"""
    meta, body = parse_frontmatter(text)
    used_ids: set[str] = set()
    next_serial: dict[str, int] = {}
    rows = []
    collection = meta.get("collection", "")
    version = meta.get("version", "")
    title = meta.get("title", "")
    source_url = meta.get("source_url", "")
    for section_path, content in split_sections(body):
        heading = section_path[-1] if section_path else title
        base_id = f"{page_path}#{slugify(heading)}"
        section = " > ".join(section_path)
        for part in split_oversized(content):
            serial = next_serial.get(base_id, 1)
            chunk_id = base_id if serial == 1 else f"{base_id}-{serial}"
            while chunk_id in used_ids:
                serial += 1
                chunk_id = f"{base_id}-{serial}"
            next_serial[base_id] = serial + 1
            used_ids.add(chunk_id)
            rows.append((chunk_id, collection, version, page_path, title,
                         section, source_url, part))
    return rows


def insert_chunks(cursor: sqlite3.Cursor, rows: list[tuple]) -> None:
    cursor.executemany(
        "INSERT INTO chunks (chunk_id, collection, version, page_path, title,"
        " section_path, source_url, content) VALUES (?,?,?,?,?,?,?,?)", rows,
    )


def file_fingerprint(stat: os.stat_result) -> str | None:
    # POSIX ctime 可偵測保留 mtime／大小的改寫；Windows ctime 是建立時間，
    # 因此 Windows 仍逐檔雜湊。跨主機、低精度或不可信的檔案狀態可強制驗證內容。
    if os.name != "posix":
        return None
    return f"{stat.st_dev}:{stat.st_ino}:{stat.st_size}:{stat.st_mtime_ns}:{stat.st_ctime_ns}"


def scan_pages(corpus_dir: Path) -> list[tuple[str, Path, str | None]]:
    """一次走訪並取得檔案狀態；維持原本 Path 排序以保留 chunk rowid 順序。"""
    pages = []
    pending = [(str(corpus_dir), "")]
    while pending:
        directory, prefix = pending.pop()
        with os.scandir(directory) as entries:
            for entry in entries:
                relative = prefix + entry.name
                if entry.is_dir(follow_symlinks=False):
                    pending.append((entry.path, relative + "/"))
                elif entry.name.endswith(".md"):
                    pages.append((relative, Path(entry.path), file_fingerprint(entry.stat())))
    pages.sort(key=lambda page: os.path.normcase(page[0]).replace(os.sep, "/").split("/"))
    return pages


def read_page(path: Path) -> tuple[bytes, str | None]:
    with path.open("rb") as source:
        before = file_fingerprint(os.fstat(source.fileno()))
        data = source.read()
        after = file_fingerprint(os.fstat(source.fileno()))
    # 讀取中被改寫的檔案不可快取；下一次執行必須重新讀取。
    return data, after if before == after else None


def prepare_batch(batch: list[tuple[str, Path, str | None]]) -> list[tuple]:
    """Worker 只讀文件；SHA-256 相同時不重新解析。"""
    prepared = []
    for page_path, path, old_digest in batch:
        data, fingerprint = read_page(path)
        digest = hashlib.sha256(data).hexdigest()
        rows = None
        if digest != old_digest:
            # 雜湊與解析使用同一次讀取，換行規則和 read_text 相同。
            text = data.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
            rows = page_chunks(page_path, text)
        prepared.append((page_path, digest, fingerprint, rows))
    return prepared


def prepared_pages(pages: list[tuple[str, Path, str | None]], jobs: int):
    """限制待處理 batch 數量，按原順序寫回；只有主程序可寫 SQLite。"""
    batches = (pages[i:i + PAGES_PER_BATCH] for i in range(0, len(pages), PAGES_PER_BATCH))
    if jobs == 1:
        for batch in batches:
            yield from prepare_batch(batch)
        return
    # spawn 避免 fork 繼承主程序已開啟的 SQLite connection，也支援 macOS/Windows。
    with ProcessPoolExecutor(max_workers=jobs, mp_context=multiprocessing.get_context("spawn")) as pool:
        pending = deque()
        try:
            for _ in range(jobs * 2):
                batch = next(batches, None)
                if batch is not None:
                    pending.append(pool.submit(prepare_batch, batch))
            while pending:
                result = pending.popleft().result()
                batch = next(batches, None)
                if batch is not None:
                    pending.append(pool.submit(prepare_batch, batch))
                yield from result
        finally:
            for future in pending:
                future.cancel()


def rebuild_fts(cursor: sqlite3.Cursor) -> None:
    # 僅用於新暫存 DB：大量匯入時延後 segment merge，最後一次合併，
    # 避免同一批 postings 在中途反覆重寫。完成後恢復 FTS5 預設增量策略。
    cursor.execute("INSERT INTO chunks_fts(chunks_fts, rank) VALUES('automerge', 0)")
    cursor.execute("INSERT INTO chunks_fts(chunks_fts, rank) VALUES('crisismerge', 1000000)")
    cursor.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('rebuild')")
    cursor.execute("INSERT INTO chunks_fts(chunks_fts) VALUES('optimize')")
    cursor.execute("INSERT INTO chunks_fts(chunks_fts, rank) VALUES('automerge', 4)")
    cursor.execute("INSERT INTO chunks_fts(chunks_fts, rank) VALUES('crisismerge', 16)")


def build_index(corpus_dir: Path = CORPUS_DIR, db_path: Path = DB_PATH,
                *, full: bool = False, verify_content: bool = False, jobs: int = 1) -> dict:
    """以檔案狀態快取與內容雜湊增量更新；完整重建成功才替換舊資料庫。"""
    started = time.perf_counter()
    if jobs < 1:
        raise ValueError("jobs must be at least 1")
    if not corpus_dir.is_dir():
        raise FileNotFoundError(f"corpus not found: {corpus_dir}")
    db_path.parent.mkdir(parents=True, exist_ok=True)
    if not full and db_path.exists():
        with closing(sqlite3.connect(db_path)) as existing:
            full = existing.execute("PRAGMA user_version").fetchone()[0] != INDEX_VERSION
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
                 deleted=0, skipped=0, cached=0, hashed=0,
                 scan_seconds=0.0, update_seconds=0.0)
    try:
        if full:
            db.executescript(SCHEMA)
            db.execute(f"PRAGMA user_version = {INDEX_VERSION}")
        # 一次交易包含文件紀錄、chunks 與 FTS；中途錯誤全部回復。
        db.execute("BEGIN IMMEDIATE")
        cursor = db.cursor()
        if "fingerprint" not in {row[1] for row in cursor.execute("PRAGMA table_info(pages)")}:
            # 舊版 manifest 原地升級，只補雜湊快取，不必重新切段或重建 FTS。
            cursor.execute("ALTER TABLE pages ADD COLUMN fingerprint TEXT")
        known = {path: (digest, count, fingerprint) for path, digest, count, fingerprint in
                 cursor.execute("SELECT page_path, sha256, chunk_count, fingerprint FROM pages")}
        scan_start = time.perf_counter()
        paths = scan_pages(corpus_dir)
        stats["scan_seconds"] += time.perf_counter() - scan_start
        total_chunks = 0
        pending_pages = []
        changed = {}
        for page_path, path, fingerprint in paths:
            previous = known.pop(page_path, None)
            if previous and not verify_content and fingerprint is not None and previous[2] == fingerprint:
                stats["cached"] += 1
                stats["skipped"] += 1
                total_chunks += previous[1]
            else:
                changed[page_path] = previous
                pending_pages.append((page_path, path, previous[0] if previous else None))
        stats["jobs"] = min(jobs, max(1, (len(pending_pages) + PAGES_PER_BATCH - 1) // PAGES_PER_BATCH))
        update_start = time.perf_counter()
        # 平行讀取、雜湊、解析和主程序寫入重疊，合併計入 update_seconds。
        with closing(prepared_pages(pending_pages, stats["jobs"])) as prepared:
            for page_path, digest, fingerprint, rows in prepared:
                previous = changed[page_path]
                stats["hashed"] += 1
                if rows is None:
                    if previous[2] != fingerprint:
                        cursor.execute("UPDATE pages SET fingerprint = ? WHERE page_path = ?",
                                       (fingerprint, page_path))
                    stats["skipped"] += 1
                    total_chunks += previous[1]
                    continue
                if previous:
                    remove_page(cursor, page_path)
                insert_chunks(cursor, rows)
                count = len(rows)
                cursor.execute(
                    "INSERT OR REPLACE INTO pages (page_path, sha256, chunk_count, fingerprint) VALUES (?, ?, ?, ?)",
                    (page_path, digest, count, fingerprint),
                )
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
            rebuild_fts(cursor)
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
    parser = argparse.ArgumentParser(description="建立文件索引（預設增量更新）。")
    parser.add_argument("--full", action="store_true", help="重新讀取全部文件並重建索引")
    parser.add_argument("--verify-content", action="store_true",
                        help="逐檔計算 SHA-256，不使用檔案狀態快取")
    parser.add_argument("--jobs", type=int, default=min(4, os.cpu_count() or 1),
                        help="最多解析程序數（預設最多 4；1 表示單一程序）")
    args = parser.parse_args()
    if args.jobs < 1:
        parser.error("--jobs 必須至少為 1")
    stats = build_index(full=args.full, verify_content=args.verify_content, jobs=args.jobs)
    print(f"{stats['mode']}: indexed {stats['pages']} pages, {stats['chunks']} chunks -> {DB_PATH}")
    print("pages: " + ", ".join(f"{key}={stats[key]}" for key in
                                ("added", "modified", "deleted", "skipped", "cached", "hashed", "jobs")))
    print("timing: " + ", ".join(
        f"{key.removesuffix('_seconds')}={stats[key]:.3f}s" for key in
        ("scan_seconds", "update_seconds", "fts_rebuild_seconds", "commit_seconds", "total_seconds")))


if __name__ == "__main__":
    main()
