# Ceph 20.2.4 官方文件來源研究

## 結論

本語料不直接把 `https://docs.ceph.com/en/tentacle/` 當成 immutable
source。它是 Tentacle release series 的文件路徑，會隨 20.2.x 更新；實測
`/en/v20.2.4/`、`/en/20.2.4/` 與各自的 `index.html` 都是 HTTP 404。

可重現的來源改用 Ceph 官方 `ceph/ceph` repository 的 `v20.2.4` tag 所指向
的 peeled commit `7f793731f1b39eb4f465e960113d2363c311b964`，只取該 commit
的 `doc/` source tree，再由 repo 的 git-source builder 離線正規化成 Markdown。
因此每一頁的 `source_url` 都是 commit-pinned GitHub URL，而不是 mutable
Read the Docs URL。

## 官方來源證據

| 項目 | 官方證據 |
| --- | --- |
| upstream repository | [`ceph/ceph`](https://github.com/ceph/ceph) |
| v20.2.4 release | [`Release v20.2.4`](https://github.com/ceph/ceph/releases/tag/v20.2.4) |
| fixed tag tree | [`v20.2.4`](https://github.com/ceph/ceph/tree/v20.2.4) |
| peeled commit | [`7f793731f1b39eb4f465e960113d2363c311b964`](https://github.com/ceph/ceph/commit/7f793731f1b39eb4f465e960113d2363c311b964) |
| fixed documentation root | [`doc/` at the peeled commit](https://github.com/ceph/ceph/tree/7f793731f1b39eb4f465e960113d2363c311b964/doc) |
| fixed documentation index | [`doc/index.rst`](https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/index.rst) |
| official Tentacle release notes | [`Tentacle` release page](https://docs.ceph.com/en/latest/releases/tentacle/) |
| rendered series site (not immutable) | [`docs.ceph.com/en/tentacle/`](https://docs.ceph.com/en/tentacle/) |

Ceph 的官方 release page 將 Tentacle 定義為 Ceph 的第 20 個 stable release，
並列出 v20.2.4 為 Tentacle 的第四個 minor release、日期為 2026-08-19。
GitHub 的 release page 顯示 tag `v20.2.4` 與短 commit `7f79373`；本地
`git ls-remote` 另外確認：

```text
d034dca571c94ea8a3d0c5da8aaf1051fce200cf  refs/tags/v20.2.4
7f793731f1b39eb4f465e960113d2363c311b964  refs/tags/v20.2.4^{}
```

第一行是 annotated tag object，第二行才是 checkout 與內容驗證使用的 commit。
manifest 因此直接使用第二行的 40 字 commit，避免依賴可移動的 tag ref。

注意：固定 tag 的 `doc/releases/` 有歷史 release 文件，但沒有
`tentacle.rst`。v20.2.4 的 release date、版本說明與 changelog 以官方
[Tentacle release page](https://docs.ceph.com/en/latest/releases/tentacle/)
作為獨立 release evidence；它不是這個 fixed commit `doc/` source tree
內的一個 v20.2.4 page。

## 文件範圍

Ceph v20.2.4 的 `doc/index.rst` toctree 列出 getting started、installation、
cephadm、RADOS、CephFS、RBD、RGW、manager、monitoring、API、architecture、
developer guide、governance、foundation、ceph-volume、release、security、
hardware monitoring、glossary 與 tracing 等官方文件區域。這個 repo 的範圍是
整個 fixed commit 的 `doc/`，不是只抓首頁 toctree 能直接走到的頁面：

- source inventory 有 567 個 `.rst` 檔案（包括 3 個 `.inc.rst` source
  fragment）與 4 個 `.md` 檔案；
- 其中 570 個非空 text source 產生 corpus page；固定 tag 的 0-byte
  `doc/README.md` 明確跳過，不提交只有 frontmatter 的假頁面；
- 圖片、SVG、CSS、JSON、Python 等非 Markdown/RST 資產不進 corpus，因為
  本 repo 的 corpus contract 是純文字 Markdown；
- 兩個 `literalinclude`（`demo-ceph.conf`、`pool-pg.conf`）會在安全的
  repo-root path check 後嵌入引用頁面的 fenced `ini` code，確保範例內容也
  可全文搜尋；
- `raw/ceph/20.2.4/` 只作建置端暫存，`index/docs.db` 只由 air-gap 端重建，
  兩者都不 commit。

這樣的範圍比只依賴 rendered website 的 BFS 更可檢查：raw source inventory
可以和 normalized corpus inventory 一一比對（571 個候選 source、570 個
非空 corpus page、1 個明確跳過的空檔），且 source URL 可回到同一個
immutable commit。

## 正規化決策與可重現性

對應 manifest 是 [`builder/manifests/ceph-20.2.toml`](../../builder/manifests/ceph-20.2.toml)：

```toml
name = "ceph-20.2"
collection = "ceph"
version = "20.2.4"
source_type = "git"
repo_url = "https://github.com/ceph/ceph"
git_ref = "7f793731f1b39eb4f465e960113d2363c311b964"
docs_paths = ["doc"]
sparse_paths = ["doc"]
source_url_template = "{repo_url}/blob/{git_ref}/{path}"
```

既有 `git_source.py` 原本只處理 Markdown/HTML；本次加入最小的 RST-to-Markdown
normalizer。它會把 RST section title、grid/simple table、`table::`、
code/code-block/prompt、常見 admonition、image/include、safe explicit link 與
inline role 轉成可搜尋 Markdown；section heading level 依每頁 RST 樣式的出現順序與
overline 形狀決定，include 沿用父層樣式上下文，nested admonition 保留 fenced code；
source-relative text link 會改成 corpus page
的相對路徑，source asset 則改成同一個 commit 的固定 GitHub URL。named reference、
`:ref:`、`:doc:`、`:download:` 與 `.rst` target 會盡量解析；same-page section
reference 會使用該頁的 Markdown anchor。固定 source 中不存在或在 corpus 範圍外的
link 會保留可讀的原始 link，並附上 `unresolved-source-link` classification marker；
無法解析的 RST reference 也會保留 label 並附上 `unresolved-rst-link` marker。validator
會把這些列為明確分類，不把它們誤報成全部解析成功；真正殘留的 RST syntax、錯誤的
local target 或 source/commit metadata mismatch 才是 failure。
未知 directive 與無法安全判斷的結構保留成原始 RST 文字，不猜測 Sphinx 語意，也
不丟掉程式碼或 ditaa/CLI 圖形。
因此不需要安裝完整 Sphinx/Read the Docs build stack，normalize 可以在無網路環境
從已 checkout 的固定 source 重跑。

建置命令：

```shell
builder/.venv/bin/python builder/git_source.py fetch builder/manifests/ceph-20.2.toml
builder/.venv/bin/python builder/git_source.py normalize builder/manifests/ceph-20.2.toml
```

`fetch` 的 `git_meta.json` 會記錄 repo、指定 commit、實際 HEAD、commit date
與 fetch timestamp；normalized frontmatter 的 `source_url` 則固定為
`https://github.com/ceph/ceph/blob/7f793731f1b39eb4f465e960113d2363c311b964/doc/...`。
`docs.ceph.com/en/tentacle/` 只作官方 rendered series 的人工交叉參考，不作
本語料的 reproduction input。

## 本地驗證結果

在 fixed source checkout 與 normalized corpus 上完成以下檢查：

- raw inventory：571 個 source candidate；567 個 `.rst`、4 個 `.md`；570 個
  非空 source，1 個空檔跳過；corpus 產生 570 頁；
- validator：142 個 GFM table separator rows；一般內容沒有殘留 RST table
  border；79 個 fenced-code border lines 與 402 個 `ditaa` border lines 明確
  保留；`pinned-assets=54`；未解析 RST reference 分類為 `download=67`、
  `named=18`、`ref=9`，另有 4 個 source-relative link classification。這些
  classification marker 會留在輸出中，不冒充全數 offline link 已解析；真正殘留
  RST syntax、失效 local target 與 source/commit mismatch 仍會使 validator fail。
- `literalinclude` 的兩個設定檔範例均確認有嵌入，並通過 repo-root path escape
  測試；固定 source 中不存在或超出 corpus 範圍的四個舊連結保留原始 target 並附上
  `unresolved-source-link` marker，沒有被誤轉成另一個 local page。
- SQLite `integrity_check` 為 `ok`；整體 index 為 27647 頁、241249 chunks；以
  `collection='ceph' AND version='20.2.4'` 精確篩選後，Ceph 20.2.4 為 570 頁、
  6429 chunks。FTS 對 `mclock`、`cephadm`、`osd_mclock_max_capacity_iops_ssd`、
  `osd_pool_default_size` 分別命中 88、503、5、16 chunks；不符合 pinned
  `source_url` 的 Ceph chunks 為 0；
- `builder/.venv/bin/python -m unittest discover -s builder/tests -v`：25 tests，
  全部通過。
