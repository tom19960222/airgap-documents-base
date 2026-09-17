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

Ceph 20.2.4 的全量產出可用 validator 重跑 metadata、RST table 與 offline link
檢查：

```bash
builder/.venv/bin/python builder/validate_ceph_corpus.py
```

這個完整模式需要建置端的固定 commit raw checkout；只有 corpus 時可明確使用
`--allow-missing-raw` 做 content-only 檢查。

無法解析的 RST reference 或 source-relative link 會保留明確 classification marker，
報告數量但不假裝全部 offline link 都已解析；真正殘留的 RST syntax、錯誤的 local
target 或 source/commit metadata mismatch 仍會 fail。

產出的 `corpus/` 進 git；`raw/` 只留在建置端。

## Air-gap 端（pull 下來就能用）

```bash
git pull
python3 runtime/build_index.py        # corpus → index/docs.db（純標準庫，預設增量更新）
```

首次執行或索引規則版本變更時會完整重建。之後先比對檔案大小、mtime、ctime、inode 與裝置編號，狀態未變就略過讀檔；其餘文件計算 SHA-256，只有內容變更才重新切段、更新全文搜尋索引。舊版 SHA-256 索引會原地補上快取，首次升級仍需讀取全部文件，但不必重建 FTS。

CLI 預設最多使用 4 個程序平行讀檔、雜湊與解析，由主程序依固定順序批次寫入 SQLite。少量變更會自動減少程序數；沒有變更時不啟動 worker，也不寫入資料庫。每批 32 頁，最多預先送出程序數兩倍的批次，避免一次載入整份語料。

需要強制完整重建時：

```bash
python3 runtime/build_index.py --full
```

需要逐檔驗證內容，或調整解析程序數時：

```bash
python3 runtime/build_index.py --verify-content  # 每頁都算 SHA-256，只重建內容有變的頁面
python3 runtime/build_index.py --full --jobs 8  # 指定最多 8 個解析程序
python3 runtime/build_index.py --jobs 1         # 使用單一程序
```

檔案狀態快取適用於 ctime 可靠的 POSIX 檔案系統，能偵測保留相同大小與 mtime 的一般改寫。使用低時間精度的檔案系統、網路掛載，或需要不依賴 metadata 的內容確認時，使用 `--verify-content`。Windows 會自動逐檔雜湊；`--full` 在所有平台都重新讀取全部文件。建置期間請勿修改 corpus。

輸出會列出 `cached`（略過讀檔）、`hashed`（實際雜湊）及 `jobs`（處理時採用的程序數）。`scan` 是檔案狀態掃描；`update` 包含互相重疊的讀檔、雜湊、解析及寫入；FTS 重建與 commit 另外計時。Python API `build_index()` 預設 `jobs=1`；程式使用 `jobs>1` 時，請將呼叫放在 `if __name__ == '__main__':` 之內。

增量更新失敗會回復整筆交易；完整重建先寫入同目錄暫存資料庫，成功才替換舊索引，因此需要容納新舊兩份資料庫的空間。請勿同時執行多個 build。完整重建後，已啟動的 MCP 程序需重新啟動才能開啟新的資料庫。

加速方式與本機完整語料的前後測數據見 [索引建置效能實測](docs/performance/2026-09-17-index-build.md)。

索引回歸測試（純標準庫）：

```bash
python3 -m unittest discover -s runtime/tests -v
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
