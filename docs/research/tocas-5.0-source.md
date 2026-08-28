# Tocas UI 5.0 官方來源研究

研究日期：2026-08-28（Asia/Taipei）

本筆記只採用 Tocas 官方 GitHub repository 與官方文件網站；`raw/tocas/`
是本次研究使用的本地暫存來源，不是要提交到語料 repo 的內容。

## 結論

Tocas UI 的套件原始碼和 5.0 文件是兩個官方 repository，不能只 clone
`teacat/tocas`：

1. 套件原始碼固定為 [`teacat/tocas` 的 `5.0.2` tag](https://github.com/teacat/tocas/tree/5.0.2)，其 commit 是
   `62f96d2a5abb3994da6c4176ef2a4d0f10ddc0bd`（2025-03-19 23:44:15
   +08:00）。這個 tag 的 [`package.json`](https://github.com/teacat/tocas/blob/5.0.2/package.json)
   版本是 `5.0.2`，README 也把文件原始碼指向 `teacat/tocas-docs`。
2. 文件固定為 [`teacat/tocas-docs` 的 commit
   `e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7`](https://github.com/teacat/tocas-docs/commit/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7)。該 repo 沒有版本 tag；截至研究日，這是官方 refs 中最後一次修改
   [`docs/5.0/`](https://github.com/teacat/tocas-docs/tree/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0) 的 commit，subject 為
   `temporary fix tocas -> tocas-ui cdnjs hang`（2025-03-22 01:53:10
   +08:00）。
3. 目標語系的已發布文件樹是
   [`docs/5.0/zh-tw/`](https://github.com/teacat/tocas-docs/tree/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw)，不是 Markdown，而是提交在 Git 裡的靜態 HTML。官方網站
   [`https://tocas-ui.com/5.0/zh-tw/index.html`](https://tocas-ui.com/5.0/zh-tw/index.html) 的頁面版本也明確顯示 `v5.0`、最新 `v5.0.2`；因此這一組 ref 與官方 5.0 網站內容對得上。

`teacat/tocas` 還有 `5.0.3` tag（commit
`e3a430cf07fd05eac00010f237ea6933a5749e6e`），但目前官方 5.0 網站與
`tocas-docs` 的 `meta.yml` 都是 `5.0.2`。`5.0.3` 可以是「只要套件
原始碼的最新 5.0 patch」的選擇，卻不是這個已發布文件快照的對應版本；本
語料以網站文件為目標，所以選 `5.0.2`。

## 官方來源與固定 ref

| 用途 | 固定來源 | 證據 |
| --- | --- | --- |
| Tocas UI 套件 | `https://github.com/teacat/tocas` | [官方 README](https://github.com/teacat/tocas/blob/5.0.2/README.md)、[MIT LICENSE](https://github.com/teacat/tocas/blob/5.0.2/LICENSE) |
| 套件 ref | tag `5.0.2` → `62f96d2a5abb3994da6c4176ef2a4d0f10ddc0bd` | [tag tree](https://github.com/teacat/tocas/tree/5.0.2)、[commit](https://github.com/teacat/tocas/commit/62f96d2a5abb3994da6c4176ef2a4d0f10ddc0bd) |
| 文件 repository | `https://github.com/teacat/tocas-docs` | Tocas 5.0.2 README 的[文件原始碼連結](https://github.com/teacat/tocas/blob/5.0.2/README.md) |
| 文件 ref | commit `e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7` | [commit](https://github.com/teacat/tocas-docs/commit/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7)、[5.0 tree](https://github.com/teacat/tocas-docs/tree/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0) |
| 正體中文網站 | `/5.0/zh-tw/` | [官方首頁](https://tocas-ui.com/5.0/zh-tw/index.html)、[開始使用](https://tocas-ui.com/5.0/zh-tw/getting-started.html)、[元件樣式](https://tocas-ui.com/5.0/zh-tw/button.html)、[範例](https://tocas-ui.com/5.0/zh-tw/examples.html) |

### 為什麼文件用 commit 而不是 branch

`tocas-docs` 沒有 `5.0.2` tag；`master` 會繼續包含其他版本（目前也有
5.7）。因此不能把 `master` 當作 5.0 的 immutable source。固定 commit
`e62614c...` 有兩個可重現的證據：

- `git log --all -- docs/5.0/zh-tw` 的最新路徑 commit 是這個 commit。
- 它是目前 `origin/master` 的 ancestor，而且 `docs/5.0/zh-tw` 與目前
  `origin/master` 的差異為空；後續 docs repo 更新沒有改動這棵 5.0 文件樹。

研究時將 `raw/tocas/docs` checkout 到這個 commit，將
`raw/tocas/repo` checkout 到 `5.0.2` tag。

## 文件所在路徑與格式

### 已發布靜態文件

`docs/5.0/zh-tw/` 在固定 commit 共有 1,308 個檔案，其中：

- 89 個 `.html`：根目錄 67 頁，`examples/` 下 22 個 standalone 範例頁。
- 69 個 `.css`、11 個 `.js`，以及圖片、SVG、字型等呈現資產。
- 沒有 `.md` 檔案。

89 個 HTML 才是要進文字語料的候選文件；`assets/` 下的 CSS、JavaScript、
字型、圖片不是文件 page，不應被當成 Markdown page。`examples/*.html` 是
獨立的 UI 範例頁，若語料目標包含「如何組合元件」可保留；若只要元件
API/說明，則可在 normalizer 中另列為可選範圍。

代表頁的 commit-pinned source：

- [`index.html`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/index.html)
- [`getting-started.html`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/getting-started.html)
- [`button.html`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/button.html)
- [`examples.html`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/examples.html)
- [`examples/blog.html`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/examples/blog.html)

固定 commit 的已發布 HTML 比即時網站 URL 更適合做 source provenance；
網站 URL 只用來提供人類瀏覽入口。

### 原始資料與模板

`tocas-docs` 同時保留可重建文件的來源資料：

- [`translations/zh-tw/meta.yml`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/translations/zh-tw/meta.yml)：語言、路徑、版本與 UI 翻譯。`Information.Version` 是 `5.0.2`，`ShortVersion` 是 `5.0`；首頁安裝片段中的 `{version}` 也由這裡代入。
- [`translations/zh-tw/components/`](https://github.com/teacat/tocas-docs/tree/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/translations/zh-tw/components)：65 個 YAML 元件文件。每個 YAML 以 `Title`、`Description`、`Definitions`、`Sections`、`HTML`、`AttachedHTML`、`Variables` 等欄位描述頁面和範例。
- [`build/templates/index.html`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/build/templates/index.html)、[`article.html`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/build/templates/article.html)、[`examples.html`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/build/templates/examples.html)：HTML 外觀和頁面骨架。
- [`build/data.go`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/build/data.go)：Go struct 對應上述 YAML 欄位。
- [`docs/CNAME`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/CNAME)：內容是 `tocas-ui.com`。已發布樹以 `docs/` 目錄保存，並用這個 CNAME 設定官方網域。

YAML 是重建輸入，不是已發布的文件格式；它包含 `[[...]]`、`{{...}}` 等
供模板和語法高亮處理的 placeholder。若語料要與官方網站顯示內容一致，應
以 commit-pinned 的 generated HTML 為主要輸入，YAML 只作追溯和必要時的
原始碼對照。

## 靜態網站生成方式

官方 builder 是 [`build/main.go`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/build/main.go) 提供的 Go CLI，要求兩個環境變數：

- `TOCAS_PATH`：`teacat/tocas` checkout 的路徑。
- `TOCAS_DOCS`：`teacat/tocas-docs` checkout 的路徑。

命令的語意是 `tocas-buildtool build --lang zh-tw`；語系預設也是
`zh-tw`。[`build/build.go`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/build/build.go) 可直接證明以下流程：

1. 讀取 `translations/{lang}/components` 與 `translations/{lang}/meta.yml`。
2. 清理並建立 `docs-dev/{lang}`，複製 `build/templates/assets`。
3. 呼叫 compile，把 Tocas repo 的 `src/` 編譯到 `dist/`，再把 `dist/` 和
   `src/` 複製到 `docs-dev/{lang}/assets/tocas`。
4. 複製 `examples/` 到 `docs-dev/{lang}/examples`。
5. 用 Go templates 產生 `index.html`、`examples.html`，以及每個 component
   的 `{name}.html`。

[`build/compile.go`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/build/compile.go) 的編譯內容是：

- 讀取 `TOCAS_PATH/src/tocas.css`，展開 CSS `@import`，輸出未壓縮和
  minified CSS。
- 讀取 `TOCAS_PATH/src/scripts/tocas.js`，展開 JavaScript imports，輸出
  未壓縮和 minified JavaScript。
- 複製 `src/fonts/icons` 與 `src/flags` 到 `dist/`。

`build/README.md` 另外列出 `babel-minify`、`js-beautify`、
`highlight.js-cli` 和 `css-minify` 等外部工具；Go 依賴與版本則在
[`build/go.mod`](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/build/go.mod)。這表示完整重建需要
matching 的套件 checkout 和工具版本，不能把「重新執行 builder」當成
文件 snapshot 的 immutable proof。

程式實際寫入的是被 `.gitignore` 排除的 `docs-dev/{lang}`；固定 commit 中
提交的 `docs/5.0/zh-tw/` 是已發布的靜態產物。從 repository source 可以
確認「YAML + Go template → docs-dev HTML」；但將 docs-dev promotion 到
版本化 `docs/5.0/` 的發布動作沒有在這個 repo 的 checked-in builder 中
另外表達。因此導入語料時應直接讀固定 commit 的 `docs/5.0/zh-tw/`，不要
為了重建而引入一套新的 renderer。

## 授權與第三方內容

- [`teacat/tocas` 的 LICENSE](https://github.com/teacat/tocas/blob/5.0.2/LICENSE) 是 MIT，版權行標示 Yami Odymel（2022）。Tocas 5.0.2 README 也說明原始碼採 MIT。
- Tocas 5.0.2 README 的官方聲明是「文件則為 [CC 0](https://creativecommons.org/publicdomain/zero/1.0/deed.zh_TW) 公眾領域」；同一聲明也出現在固定 commit 的[正體中文首頁 footer](https://github.com/teacat/tocas-docs/blob/e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7/docs/5.0/zh-tw/index.html)。
- `tocas-docs` 固定 commit 的 repository root 沒有自己的 `LICENSE` 檔；因此 CC0 是 upstream README/footer 的授權聲明，應在 provenance 中保留，不能把它擴張解讀成所有嵌入資產都自動是 CC0。
- Tocas README 明列使用的部分原始碼來自 [Font Awesome](https://github.com/FortAwesome/Font-Awesome)、[Floating UI](https://github.com/floating-ui/floating-ui) 和 [flag-icons](https://github.com/lipis/flag-icons)。`docs/5.0/zh-tw/assets/` 也包含字型、旗幟與圖片；本 repo 的純文字 corpus 應排除這些非文字資產。若未來要分發資產，需逐項保留其 upstream license/notice。

## 導入方案

### Manifest

本 repo 使用 [`builder/manifests/tocas-5.0.toml`](../../builder/manifests/tocas-5.0.toml)：

```toml
name = "tocas-5.0"
collection = "tocas"
version = "5.0.2"
source_type = "git"
repo_url = "https://github.com/teacat/tocas-docs"
git_ref = "e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7"
docs_paths = ["docs/5.0/zh-tw"]
sparse_paths = ["docs/5.0/zh-tw"]
source_url_template = "{repo_url}/blob/{git_ref}/{path}"
```

`source_url_template` 會把每個 page 指到
`https://github.com/teacat/tocas-docs/blob/e62614c.../docs/5.0/zh-tw/...html`，
這比 `https://tocas-ui.com/5.0/zh-tw/...` 更能保證 provenance 不隨網站部署
變動。網站 URL 可以額外作為人類閱讀連結，但不應取代 commit-pinned
source URL。

### Builder 導入實作

本次導入補上兩個通用接縫：

1. [`builder/git_source.py`](../../builder/git_source.py) 現在可對 40 位 commit
   SHA 做 depth-1 fetch 與 detached checkout，不需改用 mutable `master`。
2. 當 git manifest 提供 `content_selector` 時，`git_source.normalize`
   也會處理 HTML；Tocas 使用專用的主內容選擇順序和清理規則，
   最後寫出全部 89 頁。

目前 HTML normalizer：

- 對 `docs/5.0/zh-tw/**/*.html` 建立相同相對路徑的 `.md` page，保留
  `examples/` 層級。
- component/getting-started 頁從 template 定義的
  `<main class="主體-格局-內容...">` 擷取；首頁擷取 `.主要內容`，範例
  索引擷取 `.文件內容`；standalone `examples/*.html` 移除 head 後擷取
  body。應移除 header/nav/sidebar/footer、script/style 和純呈現資產引用。
- 保留 `h1`–`h3`、段落、列表、表格、`pre/code` 與錨點；HTML 中的
  syntax-highlight `<span>`/`<mark>` 要還原成可搜尋的純文字或 fenced code，
  不要把 CSS class 當成文件內容。
- 將相對站內連結從 `.html` 改成 corpus 的 `.md`，外部 URL 保留；每頁的
  `source_url` 使用上方 commit-pinned `blob` URL。
- 只收文字 page，排除 `assets/` 的 CSS、JS、字型、圖片。若需要完整 UI
  demo，另存 raw asset 但不要把它們混進 FTS 文件 page。

不要直接把 YAML 當成最終 corpus：YAML 的 placeholder 和 `HTML` 欄位是
模板輸入；已提交的 generated HTML 才是官方網站實際發布、且已經過
highlight/beautify 的內容。YAML 路徑可在研究記錄中保留作 secondary
provenance。

## 本次抓取與驗證

### 本地 fixed checkout

```text
raw/tocas/repo
  HEAD = 62f96d2a5abb3994da6c4176ef2a4d0f10ddc0bd
  describe --tags --exact-match = 5.0.2

raw/tocas/docs
  HEAD = e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7
  latest commit touching docs/5.0/zh-tw = e62614c61a3fdb5d75cc5573e66f64dbfdbb7be7
```

`docs/5.0/zh-tw` 的固定 subtree SHA 是
`3972fc5411ad7929a35e3b59d9de7764dafaf8f2`；套件 tag 5.0.2 的 `src/` 和
`dist/` subtree SHA 分別是
`fed2461e5314ba99c4adf57d6d89158b378cc1cf` 和
`62ac82cff06318f73874bae2d7485b8a15baf504`。

### 官方網站與固定產物比對

在 2026-08-28 讀取官方 HTTPS 頁面，以下 SHA-256 均是 live page 與
`raw/tocas/docs` 固定 commit 檔案相同：

| Page | SHA-256 |
| --- | --- |
| [`index.html`](https://tocas-ui.com/5.0/zh-tw/index.html) | `fc5bd60c79571b6bf69235013c3acb7ce35fccf6d102028b222dd953e17f7858` |
| [`getting-started.html`](https://tocas-ui.com/5.0/zh-tw/getting-started.html) | `6453a2e05f38fc0c8a271881e4c3869a3c73e7d39c36ad041bbfbda767a6e064` |
| [`button.html`](https://tocas-ui.com/5.0/zh-tw/button.html) | `626a6a5b7d2ac2c2e4eb5532438d517a436b03182b7a589a3dc7204b6b0103e3` |
| [`examples.html`](https://tocas-ui.com/5.0/zh-tw/examples.html) | `036ecd8f1410cf2eceaf89c6ab87db6fead43d7c2038775dadec3933226b1d53` |

此外，`teacat/tocas` 5.0.2 tag 的 `dist/tocas.css`、`dist/tocas.min.css`、
`dist/tocas.js`、`dist/tocas.min.js`，與文件固定 commit 的
`docs/5.0/zh-tw/assets/tocas/` 對應檔案 SHA-256 也完全相同。這確認文件
頁面內嵌的 Tocas runtime 是 5.0.2，而不是後來的 5.0.3 或 master。

## 導入結果

- `corpus/tocas/5.0.2/` 共 89 頁：67 個主文件頁與 22 個
  standalone 範例頁，與固定 commit 的 HTML inventory 一致。
- 每頁都有 `collection: tocas`、`version: "5.0.2"`、commit-pinned
  `source_url` 與 commit timestamp。
- 元件頁的導覽與預覽外殼已移除，說明、表格、錨點與 586 個
  HTML fenced code blocks 保留；standalone 範例頁則保留 body 可搜尋文字。
- 純呈現的 CSS、JavaScript、字型與圖片沒有被當成 corpus page。
