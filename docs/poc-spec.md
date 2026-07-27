# PoC Spec

目標：驗證「爬取文件站 → Markdown 語料 → git pull 進 air-gap → OpenCode + 本地 LLM 檢索」這條路是否可用。詞彙見 [CONTEXT.md](../CONTEXT.md)，搬運決策見 [ADR-0001](adr/0001-git-repo-as-distribution-channel.md)。

## 兩階段驗證

1. **Phase 1 — Grep Baseline**：建置端產出 `corpus/`，air-gap 端 pull 後讓 OpenCode 直接用 grep/read 檢索。
2. **Phase 2 — MCP 搜尋**：加上 FTS5 索引與 MCP server，同一批試題再測一輪，與 baseline 比較。

驗收：非正式試題清單（5〜8 題真實問題，中文敘述為主，關鍵字中英混雜），兩階段同題手測。不預標命中頁面、不計算命中率。驗證重點包含：版本正確性（v6/v8 不混用）、「中文意圖→英文關鍵字」轉換、找不到時是否誠實說找不到。

## Repo 結構

```
airgap-documents-base/
├── CONTEXT.md
├── docs/
│   ├── poc-spec.md
│   └── adr/
├── corpus/                      # 語料（純文字，進 git）
│   └── <collection>/<version>/<page-path>.md
├── builder/                     # 建置端（可連網才會用到）
│   ├── manifests/               # 每個來源一個 TOML
│   ├── crawl.py                 # 爬取 → raw archive
│   ├── normalize.py             # raw HTML → corpus Markdown
│   └── requirements.txt
├── runtime/                     # air-gap 端（pull 下來就要能跑）
│   ├── search_core.py           # FTS5 查詢層（純標準庫）
│   ├── build_index.py           # corpus → index/docs.db（純標準庫）
│   ├── mcp_server_stdlib.py     # MCP stdio server，零依賴版
│   └── mcp_server_sdk.py        # MCP stdio server，官方 SDK 版
├── raw/                         # 原始 HTML（.gitignore，只在建置端）
└── index/                       # FTS5 db（.gitignore，air-gap 端本地建）
```

## PoC 語料來源（事實已確認 2026-07-28）

| Collection | Version | Base URL | 備註 |
|---|---|---|---|
| ansible | 6 | `https://docs.ansible.com/projects/ansible/6/` | 舊路徑 `/ansible/6/` 會 301 過來 |
| ansible | 8 | `https://docs.ansible.com/projects/ansible/8/` | |
| ceph | 19.2.2 | `https://docs.ceph.com/en/squid/` | squid = 19.2.x 系列 |

三站都是 sphinx_rtd_theme：正文在 `div[role="main"]`。sitemap 不可用（Read the Docs 的 sitemap 只列版本根目錄），discovery 一律用限定 prefix 的 BFS link crawl。

## Source Manifest（builder/manifests/*.toml）

```toml
name = "ansible-6"
collection = "ansible"
version = "6"
base_url = "https://docs.ansible.com/projects/ansible/6/"
content_selector = "div[role=main]"
# 只爬 base_url prefix 底下的頁面；deny 用於排除低價值頁
deny_prefixes = ["collections/"]     # 相對 base_url；視語料量調整
max_pages = 5000                     # 保險絲
delay_seconds = 0.5                  # 禮貌性間隔
```

## Raw Archive（建置端，不進 git）

```
raw/<collection>/<version>/
├── pages/<sha256(url)[:16]>.html.gz
└── pages.jsonl        # {url, status, fetched_at, ...}，三種條目：
                       #   archived: true（HTML 已落盤，url 為 redirect 後的 canonical URL）
                       #   alias: true（被 redirect 合併的 URL，final_url 指向 canonical）
                       #   non_html: true（200 但非 HTML）
```

頁面身分一律以 redirect 後的 canonical URL 為準（跳轉出範圍的不保存）。改 normalizer 重跑時讀 raw，不重爬；transport/HTTP error 不記入 jsonl，下次爬取重試。

## Corpus 頁面格式

檔案路徑：`corpus/<collection>/<version>/<url 相對路徑>.md`（`a/b.html` → `a/b.md`、`a/` → `a/index.md`）。

```markdown
---
collection: ansible
version: "6"
title: Ansible Vault
source_url: https://docs.ansible.com/projects/ansible/6/vault_guide/index.html
fetched_at: 2026-07-28T00:00:00Z
---

# Ansible Vault
...
```

轉換要求：保留標題層級、fenced code block（含語言標記）、表格（GFM）、admonition 轉為 blockquote 加 `**Note:**` 前綴、站內連結改寫為相對 `.md` 路徑（站外連結保留絕對 URL）。

## FTS5 Schema（index/docs.db，air-gap 端 `build_index.py` 產生）

```sql
CREATE TABLE chunks (
  id INTEGER PRIMARY KEY,
  chunk_id TEXT UNIQUE,        -- <collection>/<version>/<page-path>#<section-slug>
  collection TEXT NOT NULL,
  version TEXT NOT NULL,
  page_path TEXT NOT NULL,     -- corpus 相對路徑
  title TEXT NOT NULL,         -- 頁標題
  section_path TEXT NOT NULL,  -- "Vault > Encrypting content > Examples"
  source_url TEXT NOT NULL,
  content TEXT NOT NULL
);
CREATE VIRTUAL TABLE chunks_fts USING fts5(
  title, section_path, content,
  content='chunks', content_rowid='id',
  tokenize='porter unicode61'
);
```

Chunking：以標題（H1–H3）切 section，一個 section 一個 chunk；超過 6000 字元的 section 再對切。chunk 帶前後鄰居（由 rowid 順序推得），供「拿到步驟後往前要前置條件」。

## MCP 介面（stdio transport，兩個版本共用 search_core）

- `search_docs(query, collection?, version?, limit=8)` → `[{chunk_id, title, section_path, source_url, snippet, score}]`
  - tool description 明示：query 用英文關鍵字（文件為英文；中文問題請先轉成英文關鍵字）、有版本需求務必帶 version。
- `get_section(chunk_id)` → `{content, section_path, source_url, prev_chunk_id, next_chunk_id}`
- `list_collections()` → `[{collection, versions, page_count}]`

安全邊界：只讀、只接受合法 chunk_id（不接受任意路徑）、單次回傳內容設上限、搜尋結果是資料不是指令。

## 明確不做

Vector search、headless browser、WARC/WACZ、簽章／delta bundle／rollback、正式測試集與命中率統計、中文語料 tokenizer、通用全網爬蟲、REST API（MCP 直接疊在 search_core 上，REST 留待有第二種消費端再說）。
