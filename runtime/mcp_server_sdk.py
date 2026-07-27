"""MCP stdio server，官方 Python SDK 版（需要 `pip install mcp`）。

與 mcp_server_stdlib.py 功能相同，二擇一使用；比較兩者相容性/穩定性用。
"""

from __future__ import annotations

import json

from mcp.server.fastmcp import FastMCP

from search_core import SearchCore
from tool_defs import (
    GET_SECTION_DESCRIPTION,
    LIST_COLLECTIONS_DESCRIPTION,
    SEARCH_DOCS_DESCRIPTION,
    dispatch,
)

mcp = FastMCP("airgap-docs")
core = SearchCore()


def as_text(result) -> str:
    return json.dumps(result, ensure_ascii=False, indent=1)


@mcp.tool(description=SEARCH_DOCS_DESCRIPTION)
def search_docs(query: str, collection: str | None = None,
                version: str | None = None, limit: int = 8) -> str:
    return as_text(dispatch(core, "search_docs", {
        "query": query, "collection": collection, "version": version, "limit": limit,
    }))


@mcp.tool(description=GET_SECTION_DESCRIPTION)
def get_section(chunk_id: str) -> str:
    return as_text(dispatch(core, "get_section", {"chunk_id": chunk_id}))


@mcp.tool(description=LIST_COLLECTIONS_DESCRIPTION)
def list_collections() -> str:
    return as_text(dispatch(core, "list_collections", {}))


if __name__ == "__main__":
    mcp.run()
