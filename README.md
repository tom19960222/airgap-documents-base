# airgap-documents-base

把技術文件站爬成 Markdown 語料，經 git pull 帶進網路受限環境，讓 agent（OpenCode + 本地 LLM）可以離線檢索並正確引用。設計決策見 [docs/poc-spec.md](docs/poc-spec.md) 與 [docs/adr/](docs/adr/)，詞彙見 [CONTEXT.md](CONTEXT.md)。

## 建置端（可連網）

### HTML 來源（文件網站）

```bash
cd builder
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python crawl.py manifests/ceph-19.toml       # 爬 → raw/（可中斷續跑）
.venv/bin/python normalize.py manifests/ceph-19.toml   # raw → corpus/（離線可重跑）
```

### Git 來源（GitHub repo 內的 Markdown 文件）

```bash
cd builder
.venv/bin/python git_source.py fetch manifests/node-driver-registrar-2.13.toml      # git clone → raw/
.venv/bin/python git_source.py normalize manifests/node-driver-registrar-2.13.toml  # raw → corpus/（離線可重跑）
# 或一次執行 fetch + normalize：
.venv/bin/python git_source.py all manifests/node-driver-registrar-2.13.toml
```

產出的 `corpus/` 進 git；`raw/` 只留在建置端。

## Air-gap 端（pull 下來就能用）

```bash
git pull
python3 runtime/build_index.py        # corpus → index/docs.db（純標準庫，幾秒鐘）
```

### 方式一：讓 agent 直接 grep corpus/（Phase 1 baseline）

不需任何服務，OpenCode 用原生工具搜 `corpus/` 即可。

### 方式二：MCP 搜尋（Phase 2）

OpenCode 設定（零依賴版，純 Python 標準庫）：

```json
{
  "mcp": {
    "airgap-docs": {
      "type": "local",
      "command": ["python3", "/path/to/repo/runtime/mcp_server_stdlib.py"]
    }
  }
}
```

或官方 SDK 版（需 `pip install "mcp>=1,<2"`）：`runtime/mcp_server_sdk.py`。兩者工具相同：`search_docs` / `get_section` / `list_collections`。
