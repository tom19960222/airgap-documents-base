# GitLab 17.9.8 Markdown corpus source research

## 結論

GitLab 17.9.8 的 Markdown 文件來源應固定為官方 GitLab monorepo 的
`v17.9.8-ee` tag，而不是以 `17.9` archive 或 `17-9-stable-ee` branch
作為可變來源。官方 tag 的 peeled commit 是：

```text
tag object: eba75738e18120485f9cd00cbad67496b76ff0da
commit:     610a89e5348b7d0e5e0955e04372fcd583fbac06
```

此 commit 由 GitLab Release Tools Bot 在 2025-05-07 建立，ref 為
`v17.9.8-ee`。應將來源資料放在 `raw/gitlab/17.9.8/repo`，只取
`doc/`，再由既有 builder 的 normalize 階段產生 `corpus/gitlab/17.9.8/`。

## 官方來源證據

| 項目 | 證據 |
| --- | --- |
| 官方 repository | [`gitlab-org/gitlab`](https://gitlab.com/gitlab-org/gitlab) |
| 精確 tag | [`v17.9.8-ee` tree](https://gitlab.com/gitlab-org/gitlab/-/tree/v17.9.8-ee) |
| tag peeled commit | [`610a89e5348b7d0e5e0955e04372fcd583fbac06`](https://gitlab.com/gitlab-org/gitlab/-/commit/610a89e5348b7d0e5e0955e04372fcd583fbac06) |
| Release/API metadata | [GitLab repository commit API](https://gitlab.com/api/v4/projects/gitlab-org%2Fgitlab/repository/commits/610a89e5348b7d0e5e0955e04372fcd583fbac06) |
| tag 下的 `doc/` tree | [GitLab repository tree API](https://gitlab.com/api/v4/projects/gitlab-org%2Fgitlab/repository/tree?ref=v17.9.8-ee\&path=doc\&per_page=100) |
| 文件根索引 | [`doc/_index.md`](https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/_index.md) |
| 文件內容範例 | [`doc/topics/offline/quick_start_guide.md`](https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/topics/offline/quick_start_guide.md) |
| commit-pinned raw 來源 | [`doc/` at 610a89e5](https://gitlab.com/gitlab-org/gitlab/-/tree/610a89e5348b7d0e5e0955e04372fcd583fbac06/doc) |

`git ls-remote` 的本地查證結果如下；tag object 與其 peeled commit 必須
分開記錄，後者才是要用來驗證 checkout 內容的 commit：

```text
git ls-remote --tags https://gitlab.com/gitlab-org/gitlab.git \
  refs/tags/v17.9.8-ee refs/tags/v17.9.8-ee^{}

eba75738e18120485f9cd00cbad67496b76ff0da  refs/tags/v17.9.8-ee
610a89e5348b7d0e5e0955e04372fcd583fbac06  refs/tags/v17.9.8-ee^{}
```

官方 tree API 在這個 tag 下列出 `doc/administration`、`doc/api`、
`doc/install`、`doc/topics`、`doc/update`、`doc/user` 等文件目錄；tag
raw 讀取 `doc/_index.md`、offline guide 與 installation requirements
皆成功。這證明 `doc/` 是該 tag 的官方文件樹，不是由 archive 反推的內容。

## 版本與 archive 邊界

GitLab 自己的 [release and maintenance policy](https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/policy/maintenance.md)
定義版本為 Semantic Versioning 的 `(Major).(Minor).(Patch)`，並說明
minor release 按月、patch release 只提供相容的 bug/security fixes。
因此：

- `17.9.8` 是 major `17`、minor `9`、patch `8`；它是應保留的精確
  corpus snapshot。
- `17.9` 是 minor-line 文件版本，不等同於 `17.9.8` 的 immutable source
  snapshot。
- GitLab 官方 archive 入口是 [`archives.docs.gitlab.com/17.9/`](https://archives.docs.gitlab.com/17.9/)。
  [Archives page](https://docs.gitlab.com/archives/) 也將 17.9 列為可離線
  瀏覽的 archive。
- 官方 [documentation deployment process](https://docs.gitlab.com/development/documentation/site_architecture/deployment_process/)
  說明 stable documentation image 可因 stable branch 後續變更而重建；
  所以 archive 適合查閱 17.9 minor line，不適合作為 17.9.8 精確抓取
  的替代來源。

實作決策是：產品語料使用 monorepo tag；archive 只作官方文件內容的
交叉驗證與人類瀏覽入口。若未來要收錄 `17.9.9`，應建立新的
`collection/version` 與新的 tag/commit，不覆寫 `17.9.8`；若需求是
「17.9 stable 最新文件」而非 patch snapshot，則必須另建以 stable branch
或 archive 為來源的版本，並記錄抓取時間與 ref。

## Corpus fetch contract

對應 manifest 應維持以下語意：

```toml
name = "gitlab-17.9"
collection = "gitlab"
version = "17.9.8"
source_type = "git"
repo_url = "https://gitlab.com/gitlab-org/gitlab"
git_ref = "v17.9.8-ee"
docs_paths = ["doc"]
sparse_paths = ["doc"]
source_url_template = "{repo_url}/-/blob/{git_ref}/{path}"
```

抓取命令：

```shell
cd builder
.venv/bin/python git_source.py fetch manifests/gitlab-17.9.toml
```

執行結果（2026-08-26）：

- `raw/gitlab/17.9.8/git_meta.json` 記錄 `git_ref=v17.9.8-ee`、
  `commit_hash=610a89e5348b7d0e5e0955e04372fcd583fbac06`、commit date
  `2025-05-07T10:05:15Z`。
- fetched repository 的 `HEAD` 是上述 commit，且 `git describe
  --tags --exact-match HEAD` 回傳 `v17.9.8-ee`。
- no-cone sparse checkout 最終只保留 `doc/`；`doc/` 共有 3,344 個檔案，
  其中 2,498 個是 `.md`，其餘是文件引用的圖片、YAML、SVG 等資產。
- 共享工作樹目前也已有 `corpus/gitlab/17.9.8/` 的 2,498 個 normalized
  Markdown page；該 normalize 是 concurrent work 完成的，不是本 fetch
  子任務執行的動作。本 note 不會把它誤記為本子任務的 fetch 結果。

## Fetch caveat / 後續實作範圍

Git 的 `--sparse` 預設使用 cone mode，即使 sparse path 是 `doc`，也會
保留 repository 根層檔案。Builder 會明確執行：

```shell
git -C raw/gitlab/17.9.8/repo sparse-checkout set --no-cone doc
```

以達成「只保留 `doc/`」的結果；不要用手工刪除檔案來代替 sparse 規則。
Normalize 則應只處理既有 builder 所定義的
`.md`/`.markdown`，不把圖片等資產誤當成 Markdown corpus page。

本研究不涵蓋 GitLab Linux package、container image、Runner 或 package
inventory；那些是不同的 artifact/source scope。
