"""MCP stdio server，純 Python 標準庫（零安裝）。

OpenCode 設定範例：
  { "mcp": { "airgap-docs": { "type": "local",
      "command": ["python3", "/path/to/repo/runtime/mcp_server_stdlib.py"] } } }

實作 MCP 最小子集：initialize / tools/list / tools/call（newline-delimited JSON-RPC）。
"""

from __future__ import annotations

import json
import sys

from search_core import SearchCore
from tool_defs import TOOL_DEFS, dispatch

PROTOCOL_VERSION = "2025-06-18"
SUPPORTED_VERSIONS = {"2024-11-05", "2025-03-26", "2025-06-18"}
SERVER_INFO = {"name": "airgap-docs", "version": "0.1.0"}
MAX_MESSAGE_BYTES = 1_000_000


def reply(msg_id, result=None, error=None) -> None:
    response = {"jsonrpc": "2.0", "id": msg_id}
    if error is not None:
        response["error"] = error
    else:
        response["result"] = result
    sys.stdout.write(json.dumps(response) + "\n")
    sys.stdout.flush()


def handle(core: SearchCore, msg: dict) -> None:
    method = msg.get("method")
    msg_id = msg.get("id")
    if msg_id is None:
        return  # notification：一律不回覆（含 notifications/initialized）

    if method == "initialize":
        client_version = msg.get("params", {}).get("protocolVersion")
        version = client_version if client_version in SUPPORTED_VERSIONS else PROTOCOL_VERSION
        reply(msg_id, {
            "protocolVersion": version,
            "capabilities": {"tools": {}},
            "serverInfo": SERVER_INFO,
        })
    elif method == "tools/list":
        reply(msg_id, {"tools": TOOL_DEFS})
    elif method == "tools/call":
        params = msg.get("params", {})
        if not isinstance(params, dict):
            reply(msg_id, error={"code": -32602, "message": "params must be an object"})
            return
        try:
            result = dispatch(core, params.get("name", ""), params.get("arguments") or {})
        except ValueError as exc:
            # 未知 tool 或參數驗證失敗是 protocol error，不是 tool 執行結果
            reply(msg_id, error={"code": -32602, "message": str(exc)})
        except Exception as exc:
            reply(msg_id, {
                "content": [{"type": "text", "text": f"error: {exc}"}],
                "isError": True,
            })
        else:
            reply(msg_id, {
                "content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False, indent=1)}],
                "isError": False,
            })
    elif method == "ping":
        reply(msg_id, {})
    else:
        reply(msg_id, error={"code": -32601, "message": f"method not found: {method}"})


def main() -> None:
    core = SearchCore()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        if len(line) > MAX_MESSAGE_BYTES:
            reply(None, error={"code": -32600, "message": "message too large"})
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            reply(None, error={"code": -32700, "message": "parse error"})
            continue
        if not isinstance(msg, dict):
            reply(None, error={"code": -32600, "message": "invalid request"})
            continue
        handle(core, msg)


if __name__ == "__main__":
    main()
