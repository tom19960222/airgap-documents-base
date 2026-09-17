# Ubuntu release notes 與 Linux kernel 6.17 文件來源研究

## 結論

本批新增四份以官方 rendered HTML 為來源的文件 corpus：Ubuntu 22.04、24.04、
26.04 release notes，以及 upstream Linux kernel v6.17 文件。四份 manifest 都以
官方版本根路徑為 `base_url`，透過 BFS crawl 實際發現頁面，再由同一份 raw HTML
archive 正規化成 Markdown；raw archive 不提交，只有 `corpus/` 與 manifest 進入
版本控制。

Ubuntu release notes 是各自固定版本的 release notes，不是 rolling 文件。Ubuntu
Server 的 `https://documentation.ubuntu.com/server/` 以最新 LTS 為目標，沒有被當成
22.04、24.04 或 26.04 的固定版本文件來源。

Linux kernel 官方文件以 major.minor 文件樹建置，這批固定使用 `v6.17`。部署環境
中若出現 `6.17.0-20-generic`，其中 `-20-generic` 是 Ubuntu 的 ABI/flavour
套件包版號，不是另一個 upstream kernel 文件版本，因此不另建 `6.17.0-20` corpus。

## 官方來源與版本邊界

| collection | version | 官方來源 | manifest | 文件邊界 |
| --- | --- | --- | --- | --- |
| Ubuntu | 22.04 | [Ubuntu 22.04 release notes](https://documentation.ubuntu.com/release-notes/22.04/) | [`ubuntu-22.04.toml`](../../builder/manifests/ubuntu-22.04.toml) | 22.04 LTS 首頁、22.04.1 至 22.04.5 point-release notes 與 release schedule |
| Ubuntu | 24.04 | [Ubuntu 24.04 release notes](https://documentation.ubuntu.com/release-notes/24.04/) | [`ubuntu-24.04.toml`](../../builder/manifests/ubuntu-24.04.toml) | 24.04 LTS 首頁、24.04.1 至 24.04.5 point-release notes 與 release schedule |
| Ubuntu | 26.04 | [Ubuntu 26.04 release notes](https://documentation.ubuntu.com/release-notes/26.04/) | [`ubuntu-26.04.toml`](../../builder/manifests/ubuntu-26.04.toml) | 26.04 LTS 首頁、26.04.1、LTS/interim change summary 與 release schedule |
| kernel | 6.17 | [Linux kernel v6.17 documentation](https://www.kernel.org/doc/html/v6.17/) | [`kernel-6.17.toml`](../../builder/manifests/kernel-6.17.toml) | upstream `v6.17/` 文件樹；不延伸到 `latest/`、其他 v6.x 或 Ubuntu package ABI/flavour |

Ubuntu 26.04 頁面內提到 24.10、25.04、25.10 的升級參考，是 release notes 的
內容，不是本批要抓取的版本；這些外部連結保留原始 URL，但沒有進入 26.04 corpus
之外的 Ubuntu 版本目錄。kernel 頁面內的 `latest/` 參考同樣只是 upstream 文件
文字中的外部參考，frontmatter 的 `source_url` 全部仍固定在 `v6.17/`。

## Crawl 與 normalize 結果

所有時間均為 `fetched_at` 的 UTC；每份 manifest 均使用
`content_selector` 指定的正文節點，且 `deny_prefixes = []`，由 crawler 的
`base_url` prefix scope 限制站內範圍，非 HTML 副檔名不進 corpus。

| manifest | discovered in-scope | raw entries | archived HTML | non-HTML | HTTP 404 / 未完成 | normalize entries | unique `.md` files | skipped |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ubuntu-22.04 | 7 | 7 | 7 | 0 | 0 | 7 | 7 | 0 |
| ubuntu-24.04 | 7 | 7 | 7 | 0 | 0 | 7 | 7 | 0 |
| ubuntu-26.04 | 5 | 5 | 5 | 0 | 0 | 5 | 5 | 0 |
| kernel-6.17 | 3,808 | 3,805 | 3,804 | 1 | 3 | 3,804 | 3,803 | 0 |

kernel 的三個未完成 URL 都是官方站回傳 HTTP 404，且在兩次 crawl/retry 後仍然
不存在：

- `https://www.kernel.org/doc/html/v6.17/bpf/instruction-set.html`
- `https://www.kernel.org/doc/html/v6.17/filesystems/ext4/Quota`
- `https://www.kernel.org/doc/html/v6.17/filesystems/ext4/quota`

`pages.jsonl` 只保留成功 archive 或可分類的 non-HTML response，不會另寫入 404
response；因此 3 筆失敗不會出現在 raw archive inventory。為了讓這個限制可重新
核對，於 `2026-09-16T18:14:04Z` 再直接請求上述三個固定 URL，三者仍各自回傳
HTTP 404。這項重驗證只確認 upstream 當下仍不存在，不把失敗頁偽造成 corpus
文件。

唯一的 non-HTML 條目是：
`https://www.kernel.org/doc/html/v6.17/_downloads/bf29fbb4b15af5f11533d4e2b6a0e85b/example-schema.yaml`
（`text/plain; charset=utf-8`）。它只存在於 raw `pages.jsonl` 的
`non_html` 記錄，沒有寫入 corpus。四份 crawl 都沒有 redirect alias；Ubuntu
沒有錯誤或排除項目。

kernel raw 的 3,804 個 archived URL 中，首頁 `/v6.17/` 與
`/v6.17/index.html` 都是 200 HTML，normalizer 依既有 URL 映射規則共同寫到
`index.md`。因此 normalizer 回報 3,804 entries、skipped 0，但檔案系統上是
3,803 個 unique Markdown files；這是同一首頁的相對路徑 collision，不是 selector
失效或內容遺失。

實際重建命令如下：

```shell
builder/.venv/bin/python builder/crawl.py builder/manifests/ubuntu-22.04.toml
builder/.venv/bin/python builder/normalize.py builder/manifests/ubuntu-22.04.toml
builder/.venv/bin/python builder/crawl.py builder/manifests/ubuntu-24.04.toml
builder/.venv/bin/python builder/normalize.py builder/manifests/ubuntu-24.04.toml
builder/.venv/bin/python builder/crawl.py builder/manifests/ubuntu-26.04.toml
builder/.venv/bin/python builder/normalize.py builder/manifests/ubuntu-26.04.toml
builder/.venv/bin/python builder/crawl.py builder/manifests/kernel-6.17.toml
builder/.venv/bin/python builder/normalize.py builder/manifests/kernel-6.17.toml
```

kernel crawl 初次與既有 archive retry 都會保留 3 個 404 作為未完成 URL；重跑
命令不會重抓已落盤的 HTML。抓取時間範圍如下：

| manifest | 最早 archived `fetched_at` | 最晚 archived `fetched_at` |
| --- | --- | --- |
| ubuntu-22.04 | 2026-09-16T16:16:29+00:00 | 2026-09-16T16:16:38+00:00 |
| ubuntu-24.04 | 2026-09-16T16:16:52+00:00 | 2026-09-16T16:17:03+00:00 |
| ubuntu-26.04 | 2026-09-16T16:17:16+00:00 | 2026-09-16T16:17:22+00:00 |
| kernel-6.17 | 2026-09-16T16:17:35+00:00 | 2026-09-16T16:56:27+00:00 |

## 靜態驗證與殘留項目

全量檢查 3,822 個 unique Markdown files：每頁的 frontmatter
`collection`、`version`、`source_url`、`fetched_at` 都存在且格式正確，
`bad_frontmatter = 0`；frontmatter `source_url` 沒有跨版本，且分別落在三個
Ubuntu base URL 或 kernel `v6.17/` base URL。四個 selector 都成功，normalize
的 `skipped (no main content) = 0`。

kernel 另有 7 個上游 title-only stub page：`mm/bootmem.md`、`mm/oom.md`、
`mm/page_allocation.md`、`mm/page_reclaim.md`、`mm/shmfs.md`、`mm/swap.md`、
`mm/vmalloc.md`。相應的固定 raw HTML 在 `div[role=main]` 中也只有標題，
不是 normalize 遺漏正文。corpus 保留這 7 頁與 provenance；runtime 因只有
標題而對每頁產生 0 chunks，不捏造上游不存在的內容。

正文沒有明顯網站導覽模板：`<nav>`、`<header>`、`<aside>`、`<script>`、
`Skip to content`、`Edit this page`、`Toggle navigation` 都是 0 個檔案。
kernel 有 28 個檔案出現 `table of contents`，是文件正文的目錄敘述，不是導覽
chrome；Ubuntu 26.04 有一處 `<style>` 文字，是 release notes 說明 HTML/CSS 的
內容，也不是模板殘留。另有 6 行 `..note::`/`..snip` 與 1 頁 Git conflict
marker 範例，均位於 kernel 文件的程式碼或語法說明中，不是建置衝突。

Markdown 相對連結檢查結果：

- Ubuntu 22.04、24.04：各 0 個 broken document link。
- Ubuntu 26.04：2 個刻意未收錄的 `strace-color.png` asset link；文件連結 0 個。
- kernel 6.17：183 個 local target 不存在，其中 170 個是刻意排除的圖片/CSS/JS
  asset，13 個是文件中的程式碼/記法或未落盤參考。13 個中包含前述 3 個 unique
  HTTP-404 document targets（實際出現 4 個連結）與 1 個 non-HTML YAML asset
  reference，其餘是 `part-name`、`kunit, property[, message]`、`srctree/...`
  與 V4L bit-field 記法等 literal/code 文字，不是 crawl 漏頁。

這些排除符合 corpus 的純文字 Markdown 邊界；沒有下載圖片、CSS、JS 或 YAML
資產進 corpus。整合流程最後已完整建立 35,291 頁、300,450 個 chunks 的
SQLite／FTS5 索引，並以兩次 0 變更的增量建立驗證穩定性。

本次 `normalize.py` hardening 後重新盤點 whitespace：Ubuntu 22.04、24.04、
26.04 的 19 頁均沒有 trailing-space 行；kernel 的 3,803 頁有 10 行保留
trailing whitespace，其中 3 行是 Markdown hard break（行尾正好兩個空白），
其餘 7 行是上游 code/prose literal 的既有空白。正文沒有 NUL。這些兩空白行
證明 `<br>` 轉換出的 hard break 沒有被全域裁空白誤刪；計數依所有 corpus
Markdown 的實際 bytes 重算，未把 fenced code 當成可刪除內容。

建置端測試 `builder/.venv/bin/python -m unittest discover -s builder/tests -v`
整合後共 74 tests，全部通過；runtime 測試
`builder/.venv/bin/python -m unittest discover -s runtime/tests -v` 共 5 tests，
全部通過。`builder/.venv/bin/python -m compileall -q builder runtime` 也通過。

## Audit note 更新

[`2026-09-16-component-doc-version-audit.md`](2026-09-16-component-doc-version-audit.md)
的「核心平台、網路與儲存」表已明確列出 Ubuntu **22.04、24.04、26.04** 三個
release notes URL，並保留「Ubuntu Server 是 rolling 文件、不能冒充固定 release
manual」的版本邊界說明。
