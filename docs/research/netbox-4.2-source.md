# NetBox Community 4.2 文件來源研究

## 結論

本 repo 以 NetBox Community upstream monorepo 的 `v4.2.9` tag 作為 4.2
系列的固定文件來源。官方 GitHub tag 指向 commit
`e5cdd8f2b0273ad3a109b6a88a4d87028660dd53`，commit subject 為 `Release
v4.2.9`，時間為 `2025-04-30T14:31:30-04:00`。`v4.2.9` 是目前官方
`v4.2*` tags 中最後一個 patch tag；因此本語料的版本欄位使用 `4.2.9`
而非浮動的 `4.2` 或 `main`。

來源與固定 ref：

- upstream repository：<https://github.com/netbox-community/netbox>
- fixed tag：<https://github.com/netbox-community/netbox/tree/v4.2.9>
- fixed commit：<https://github.com/netbox-community/netbox/commit/e5cdd8f2b0273ad3a109b6a88a4d87028660dd53>
- official 4.2 release notes in that tag：<https://github.com/netbox-community/netbox/blob/v4.2.9/docs/release-notes/version-4.2.md>

## 為什麼選 `v4.2.9`

NetBox upstream 的 4.2 release notes 將 patch releases 逐一列在同一份
`docs/release-notes/version-4.2.md`，其中最上方是 `v4.2.9 (2025-04-30)`。
這份 release note 也保留 4.2.0 到 4.2.9 的版本歷史，故抓取 v4.2.9 的
`docs/` 可同時涵蓋 4.2 系列最後 patch 的完整官方文件內容，而不必將
不同 patch 的文件混在一起。

官方 repository ref 查詢結果中的 4.2 tags 為：`v4.2-beta1`、`v4.2.0`
至 `v4.2.9`，沒有更晚的 `v4.2.x` tag。這個判斷只以 upstream GitHub
refs 為準；不把 Read the Docs 的 `stable`、`feature` 或網站當成 immutable
版本來源。

## Manifest 與抓取範圍

對應 manifest 是 [`builder/manifests/netbox-4.2.toml`](../../builder/manifests/netbox-4.2.toml)：

```toml
name = "netbox-4.2"
collection = "netbox"
version = "4.2.9"
source_type = "git"
repo_url = "https://github.com/netbox-community/netbox"
git_ref = "v4.2.9"
docs_paths = ["docs"]
sparse_paths = ["docs"]
source_url_template = "{repo_url}/blob/{git_ref}/{path}"
```

抓取與正規化命令：

```shell
builder/.venv/bin/python builder/git_source.py fetch builder/manifests/netbox-4.2.toml
builder/.venv/bin/python builder/git_source.py normalize builder/manifests/netbox-4.2.toml
```

`sparse_paths = ["docs"]` 讓 raw checkout 只保留官方 `docs/` 文件樹；
`source_url_template` 則讓每個 normalized page 回指同一個固定 tag 下的
GitHub 原始 Markdown 路徑。

## Fetch 結果

截至 2026-08-28，本地 raw checkout 的證據如下：

- `HEAD`：`e5cdd8f2b0273ad3a109b6a88a4d87028660dd53`。
- `git describe --tags --exact-match HEAD`：`v4.2.9`。
- `docs/` tracked files：284。
- Markdown（`.md`/`.markdown`）：248。
- 非 Markdown 文件資產：36（31 PNG、2 SVG、2 HTML、1 CSS）。
- normalizer 產生 `corpus/netbox/4.2.9/` 下 248 個 Markdown pages，
  與 upstream `docs/` 的 Markdown inventory 一一對應。
- raw 與 normalized 都有 313 行、分布於 133 頁的 `!!!` MkDocs
  admonition；這是 NetBox upstream 的原生 Markdown 語法，既有 git
  normalizer 目前保留它，不會遺失 admonition 內文。
- Hugo shortcode（`{{< ... >}}` 或 `{{% ... %}}`）為 0 行、0 頁；沒有
  這類未解析的 Hugo macro。
- `{{ ... }}` 出現在 9 頁 18 行，`{% ... %}` 出現在 5 頁 35 行；逐頁
  檢查後皆是 NetBox 文件本身示範 Django/Jinja/模板語法的文字或 fenced
  code，不是網站建置時應展開的 macro。
- 248 個 Markdown page 內共檢查 621 個相對文件連結，未發現指向 docs
  樹外或不存在目標的連結（unresolved = 0）。

raw repo、`git_meta.json` 與下載頁面位於 `raw/netbox/4.2.9/`，遵循 repo
的 `.gitignore`，不進 Corpus Repo。可提交的語料只包含純文字 Markdown；
圖片、logo、theme HTML/CSS 等二進位或呈現資產不納入 corpus，這與
[`docs/poc-spec.md`](../poc-spec.md) 對 corpus 的定義一致。

## 排除與注意事項

- 沒有排除任何 upstream Markdown page；`administration`、`configuration`、
  `customization`、`development`、`features`、`getting-started`、
  `installation`、`integrations`、`models`、`plugins`、`reference` 與
  `release-notes` 全部納入。
- 36 個非 Markdown 資產僅因本 repo 的 corpus contract 是純文字而排除，
  不是文件內容遺漏；原始資產仍在建置端 raw checkout，可由固定 tag 取得。
- NetBox 的原始 Markdown 使用 MkDocs admonition（例如 `!!! note`）。本次
  使用既有 `git_source.py` normalizer，保留其文字內容與 fenced code；
  `!!!` 指令仍保留為 313 行原生語法，沒有誤把它當成遺失的 include。
  這個 normalizer 不把 upstream 文件重寫成另一個版本，也不把圖片／CSS
  等資產假裝成 Markdown page。

## 驗證

驗證命令與預期結果：

```shell
git -C raw/netbox/4.2.9/repo rev-parse HEAD
# e5cdd8f2b0273ad3a109b6a88a4d87028660dd53

git -C raw/netbox/4.2.9/repo describe --tags --exact-match HEAD
# v4.2.9

find raw/netbox/4.2.9/repo/docs -type f -name '*.md' | wc -l
# 248

find corpus/netbox/4.2.9 -type f -name '*.md' | wc -l
# 248
```

此外，對 raw 與 corpus 的相對 Markdown 路徑做排序後的差異為空；每個
corpus page 都包含 `collection: netbox`、`version: "4.2.9"`、固定 tag
的 `source_url`，以及來自 `git_meta.json` 的 fetch timestamp。
