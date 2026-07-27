"""FTS5 查詢層。純 Python 標準庫，被兩個 MCP 前端共用。"""

from __future__ import annotations

import re
import sqlite3
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = REPO_ROOT / "index" / "docs.db"

MAX_SECTION_CHARS = 20_000  # 單次回傳上限（安全邊界）
MAX_CHUNK_ID_LEN = 512
MAX_QUERY_LEN = 1_000

# 只擋住會淹沒 OR fallback 的常見英文虛詞，刻意保持小集合
STOPWORDS = {
    "a", "an", "the", "is", "are", "was", "were", "be", "been", "to", "of",
    "in", "on", "at", "for", "and", "or", "not", "no", "do", "does", "did",
    "how", "what", "which", "when", "where", "why", "who", "can", "could",
    "should", "would", "will", "may", "might", "with", "from", "into", "that",
    "this", "these", "those", "it", "its", "my", "your", "i", "you", "we",
}


def _tokens(query: str) -> list[str]:
    words = re.findall(r"[A-Za-z0-9_.-]+", query[:MAX_QUERY_LEN])
    kept = [w for w in words if w.lower() not in STOPWORDS]
    return kept or words  # 全是 stopword 時退回原詞，不要空手


class SearchCore:
    def __init__(self, db_path: Path = DB_PATH):
        if not db_path.exists():
            raise FileNotFoundError(
                f"{db_path} not found — run `python runtime/build_index.py` first"
            )
        self.db = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        self.db.row_factory = sqlite3.Row

    def search(self, query: str, collection: str | None = None,
               version: str | None = None, limit: int = 8) -> list[dict]:
        tokens = _tokens(str(query))
        if not tokens:
            return []
        limit = max(1, min(int(limit), 20))
        quoted = [f'"{t}"' for t in tokens]
        results = self._run_search(" ".join(quoted), collection, version, limit)
        if not results and len(quoted) > 1:
            # 全部 AND 沒中時退回 OR（stopword 已剔除），寧可鬆一點也不要空手
            results = self._run_search(" OR ".join(quoted), collection, version, limit)
        return results

    def _run_search(self, match: str, collection: str | None,
                    version: str | None, limit: int) -> list[dict]:
        sql = """
            SELECT c.chunk_id, c.collection, c.version, c.title, c.section_path,
                   c.source_url, bm25(chunks_fts) AS score,
                   snippet(chunks_fts, 2, '«', '»', ' … ', 24) AS snip
            FROM chunks_fts JOIN chunks c ON c.id = chunks_fts.rowid
            WHERE chunks_fts MATCH ?
        """
        params: list = [match]
        if collection:
            sql += " AND c.collection = ?"
            params.append(str(collection))
        if version:
            sql += " AND c.version = ?"
            params.append(str(version))
        sql += " ORDER BY score LIMIT ?"
        params.append(limit)
        # 注意：這裡刻意不吞 sqlite 例外——schema 壞掉要浮上去變成 tool error，
        # 不能偽裝成「沒有結果」讓 agent 誤以為文件不存在
        rows = self.db.execute(sql, params).fetchall()
        return [
            {
                "chunk_id": r["chunk_id"],
                "collection": r["collection"],
                "version": r["version"],
                "title": r["title"],
                "section_path": r["section_path"],
                "source_url": r["source_url"],
                "snippet": r["snip"],
                "score": round(r["score"], 2),
            }
            for r in rows
        ]

    def get_section(self, chunk_id) -> dict | None:
        if not isinstance(chunk_id, str) or not chunk_id or len(chunk_id) > MAX_CHUNK_ID_LEN:
            return None
        # 合法性以 DB membership 為準（參數化查詢），不猜字元集
        row = self.db.execute(
            "SELECT * FROM chunks WHERE chunk_id = ?", (chunk_id,)
        ).fetchone()
        if row is None:
            return None
        neighbor = lambda offset: self.db.execute(
            "SELECT chunk_id FROM chunks WHERE id = ? AND page_path = ?",
            (row["id"] + offset, row["page_path"]),
        ).fetchone()
        prev_row, next_row = neighbor(-1), neighbor(+1)
        return {
            "chunk_id": row["chunk_id"],
            "collection": row["collection"],
            "version": row["version"],
            "title": row["title"],
            "section_path": row["section_path"],
            "source_url": row["source_url"],
            "content": row["content"][:MAX_SECTION_CHARS],
            "prev_chunk_id": prev_row["chunk_id"] if prev_row else None,
            "next_chunk_id": next_row["chunk_id"] if next_row else None,
        }

    def list_collections(self) -> list[dict]:
        rows = self.db.execute(
            """SELECT collection, version, COUNT(DISTINCT page_path) AS pages
               FROM chunks GROUP BY collection, version ORDER BY collection, version"""
        ).fetchall()
        by_collection: dict[str, dict] = {}
        for r in rows:
            info = by_collection.setdefault(
                r["collection"], {"collection": r["collection"], "versions": [], "page_count": 0}
            )
            info["versions"].append(r["version"])
            info["page_count"] += r["pages"]
        return list(by_collection.values())
