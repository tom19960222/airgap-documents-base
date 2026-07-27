# CONTEXT

本專案的詞彙表（ubiquitous language）。只放詞彙定義，不放實作細節。

## 詞彙

### Corpus（語料）
爬取並正規化後、供 agent 檢索的 Markdown 文件集合。目錄結構以 `corpus/<collection>/<version>/` 分層。

### Collection
單一產品的文件集，例如 `ansible`、`ceph`。一個 Collection 可含多個 Version。

### Version
Collection 內的文件版本，例如 Ansible 的 `6`、`8`，Ceph 的 `19.2.2`。版本正確性是檢索的一級需求：回答某版本的問題不得引用其他版本的文件。

### Frontmatter Metadata
每頁 Markdown 開頭的 YAML metadata，至少含 `collection`、`version`、`source_url`。

### Grep Baseline
PoC 第一階段的檢索方式：agent（OpenCode）直接用原生檔案工具（grep/read）在 Corpus 上搜尋，不經任何搜尋服務。作為與 MCP 搜尋比較的對照組。

### Air-gap 區 / 建置區
建置區（可連網）負責爬取與建置語料；Air-gap 區（網路受限）只執行檢索。Air-gap 區的 agent 是 OpenCode + 本地 LLM（Qwen / GLM 級別）。

### Corpus Repo（語料 repo）
承載 Corpus 的 git repository，是語料進入 Air-gap 區的唯一搬運管道（air-gap 端以 git pull 取得與更新）。repo 內只放純文字（Markdown、manifest、scripts），不放二進位索引檔。

### Raw Archive
建置端保留的原始 HTML（含 URL 與抓取時間），供重跑正規化使用。只存在建置端，不進 Corpus Repo。

### 試題清單
一份非正式的真實問題清單（5〜8 題，中文敘述為主），Grep Baseline 與 MCP 搜尋兩階段用同一批題目手動測試，作為比較依據。不預標命中頁面、不計算命中率。

### Search Core
Air-gap 端的檢索核心（FTS5 查詢層），被兩個 protocol 前端共用：一個用官方 MCP SDK，一個純 Python 標準庫。
