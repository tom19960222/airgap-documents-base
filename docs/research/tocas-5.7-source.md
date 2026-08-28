# Tocas UI 5.7.0 官方來源追查

研究日期：2026-08-28（Asia/Taipei）

本檔是獨立的 5.7 追查筆記。選擇新增檔案而不是把 5.7 混進
[`tocas-5.0-source.md`](./tocas-5.0-source.md)，是因為兩個版本的官方
文件快照、source ref 和導入決策不同；原 5.0.2 研究與導入結論保持不動。

## 結論

- 官方 `teacat/tocas` 有 `5.7.0` tag，指向 commit
  `3d4f2d86d9c6231e5eac978f56124c906188f419`；tag commit 時間是
  `2026-02-25 00:25:21 +08:00`，subject 為 `5.7.0`。
- 該 immutable tag 的官方 [`package.json`](https://raw.githubusercontent.com/teacat/tocas/5.7.0/package.json)
  版本是 `5.7.0`。官方 tag/commit 來源：[tag tree](https://github.com/teacat/tocas/tree/5.7.0)、
  [commit](https://github.com/teacat/tocas/commit/3d4f2d86d9c6231e5eac978f56124c906188f419)。
- 官方 `teacat/tocas-docs` 有 `tocas5.7.0` branch；其 5.7.0 文件快照
  固定在 commit `ef8248b165f458215fb8f18bb400c4bfba1767fa`，時間
  `2026-02-25 00:25:36 +08:00`，subject 為 `5.7.0`。這是本次可重現的
  immutable docs ref：[commit](https://github.com/teacat/tocas-docs/commit/ef8248b165f458215fb8f18bb400c4bfba1767fa)、
  [branch path](https://github.com/teacat/tocas-docs/tree/tocas5.7.0/docs/5.7/zh-tw)。
- `docs/5.7/zh-tw/` 在該 commit 有 1,309 個檔案，其中 88 個 HTML：根目錄
  66 頁、`examples/` 22 頁；另有 CSS/JS、圖片、SVG、字型等呈現資產。
  因此以文件 page 計算是 88 頁，不應把 1,309 個資產檔誤算成頁面。
- 官方 live URL `https://tocas-ui.com/5.7/zh-tw/index.html` 在本次查核
  回應 `HTTP/2 200`、`content-type: text/html; charset=utf-8`，並回報
  `last-modified: Wed, 25 Feb 2026 04:20:01 GMT`（Cloudflare/GitHub Pages
  headers）。這確認 5.7 正體中文首頁已發布；網站本身是 mutable 入口，
  語料 provenance 應使用上述 commit-pinned GitHub source。此次只取得 HEAD
  狀態，沒有宣稱 live body SHA-256。

## 5.7.0 是否為最新官方 release

在已取得的官方 `teacat/tocas` refs 中，版本 tag 最高是 `5.7.0`；沒有看到
比 `5.7.0` 更高的官方 tag。`origin/master` 當時仍是 commit
`ef1c1d42d43a796647ae0b483526e5c62ad1e970`（2026-03-06），subject
`5.0.3 for README.md now, 5.7 is WIP`；所以不能把 master 的 5.0.3
README 文字當成 5.7 文件 ref。嚴格說，Git tag 是 source release ref；GitHub
Releases 頁的舊快照不應取代 tag/ref 查核。就本次官方 refs 證據而言，未發現
5.7.1 或更高版本，故 5.7.0 是目前可確認的最高官方版本。

## 為什麼上一輪選 5.0.2 合理

合理，而且是正確的 scope 決策：上一輪的使用者要求明確指向
`https://tocas-ui.com/5.0/zh-tw/index.html`。5.0.2 tag 與該 5.0 已發布文件
快照相互對應；改用 5.7.0 會變成新增另一個版本文件，而不是完成指定的
5.0 URL。版本選擇應由目標 URL／文件快照決定，不能只因後來出現更高 tag
就替換既有、已驗證的 5.0.2 corpus。

## 建議

建議「新增並保留 5.0.2」，不要取代：

1. 保留既有 `tocas-5.0`／5.0.2 corpus，因它履行原始 5.0 URL 要求，且
   source 與 live 5.0 文件已完成對應驗證。
2. 若產品要涵蓋最新版本，再以本檔記錄的 `teacat/tocas` tag
   `3d4f2d86...` 與 `teacat/tocas-docs` commit `ef8248b...` 新增獨立
   `tocas-5.7` source/corpus；不要覆蓋 5.0.2，也不要把兩個版本混成同一
   `version`。
3. 導入使用獨立 `tocas-5.7` manifest 與 `5.7.0` version，不改寫
   已發布的 5.0.2 corpus。

## 查核命令與可重現計數

```text
teacat/tocas
  tag 5.7.0 = 3d4f2d86d9c6231e5eac978f56124c906188f419
  commit time = 2026-02-25T00:25:21+08:00
  package.json version = 5.7.0

teacat/tocas-docs
  ref = tocas5.7.0
  commit = ef8248b165f458215fb8f18bb400c4bfba1767fa
  subtree docs/5.7/zh-tw = 4cdabe37c7413b8bddebb59333479a2597cc085e
  commit time = 2026-02-25T00:25:36+08:00
  HTML = 88 (root 66 + examples 22)
  all files under subtree = 1,309
```

## 官方來源索引

- [Tocas 5.7.0 package.json（tag-pinned raw source）](https://raw.githubusercontent.com/teacat/tocas/5.7.0/package.json)
- [Tocas 5.7.0 tag tree](https://github.com/teacat/tocas/tree/5.7.0)
- [Tocas 5.7.0 commit](https://github.com/teacat/tocas/commit/3d4f2d86d9c6231e5eac978f56124c906188f419)
- [Tocas docs 5.7.0 immutable commit](https://github.com/teacat/tocas-docs/commit/ef8248b165f458215fb8f18bb400c4bfba1767fa)
- [Tocas docs 5.7 正體中文文件樹](https://github.com/teacat/tocas-docs/tree/ef8248b165f458215fb8f18bb400c4bfba1767fa/docs/5.7/zh-tw)
- [官方 live 5.7 正體中文首頁](https://tocas-ui.com/5.7/zh-tw/index.html)

## 導入結果

- manifest：[`builder/manifests/tocas-5.7.toml`](../../builder/manifests/tocas-5.7.toml)。
- corpus：`corpus/tocas/5.7.0/` 共 88 頁，包含 66 個主文件頁與
  22 個 standalone 範例頁，與固定 commit 的 HTML inventory 一致。
- 每頁都有 `collection: tocas`、`version: "5.7.0"`、commit-pinned
  `source_url` 與 commit timestamp。
- 正規化後保留 569 個 HTML fenced code blocks；相對 Markdown 連結已驗證
  目標存在，code fence 平衡且沒有 trailing whitespace。
- CSS、JavaScript、圖片、SVG 與字型只保留在 ignored raw source，不會被
  當成 FTS corpus page。
