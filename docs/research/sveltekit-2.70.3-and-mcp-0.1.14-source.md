# SvelteKit 2.70.3 與 @sveltejs/mcp 0.1.14 官方來源研究

研究日期：2026-08-31（America/New_York）

本筆記只採用 Svelte 官方 GitHub repository、tag 內的 package metadata 與
tag 內的文件原始碼。`raw/` 是建置端的暫存來源，不進語料 repo；提交的
內容只有由既有 builder 產出的純文字 Markdown。

## 結論

- SvelteKit 2.70.3 使用官方 `sveltejs/kit` repository 的
  `@sveltejs/kit@2.70.3` tag，peeled commit 為
  `39e8e1fbd4feba7f22dd46bfdf7335362c38de16`。tag 內的
  [`packages/kit/package.json`](https://raw.githubusercontent.com/sveltejs/kit/@sveltejs%2Fkit@2.70.3/packages/kit/package.json)
  將套件名稱與版本固定為 `@sveltejs/kit`、`2.70.3`；官方 release 頁也列出
  這個版本與相同 commit。[release](https://github.com/sveltejs/kit/releases/tag/@sveltejs%2Fkit@2.70.3)、
  [commit](https://github.com/sveltejs/kit/commit/39e8e1fbd4feba7f22dd46bfdf7335362c38de16)
- SvelteKit 文件位於同一 tag 的 `documentation/docs/`，共 80 個 Markdown
  page；這是版本化 source tree，不採用會持續變動的 `svelte.dev/docs/kit`
  作為 snapshot。[官方文件樹](https://github.com/sveltejs/kit/tree/@sveltejs%2Fkit@2.70.3/documentation/docs)
- `@sveltejs/mcp` 0.1.14 使用官方 Svelte AI tools repository 的
  `@sveltejs/mcp@0.1.14` tag，peeled commit 為
  `b891e4860b880144b15f2a86a4e1e98b1631c26f`。`sveltejs/mcp` 是此 repository
  的 GitHub alias/重新導向入口；tag 內的
  [`packages/mcp-stdio/package.json`](https://raw.githubusercontent.com/sveltejs/ai-tools/b891e4860b880144b15f2a86a4e1e98b1631c26f/packages/mcp-stdio/package.json)
  仍明確標示 package name `@sveltejs/mcp`、版本 `0.1.14`，並保留
  `sveltejs/mcp` 的 repository metadata。[官方 repository](https://github.com/sveltejs/mcp)、
  [canonical repository](https://github.com/sveltejs/ai-tools)、
  [commit](https://github.com/sveltejs/ai-tools/commit/b891e4860b880144b15f2a86a4e1e98b1631c26f)
- Svelte MCP 文件位於該 tag 的 `documentation/docs/`，共 10 個 Markdown
  page，涵蓋 introduction、local/remote setup、tools、resources 與 prompts。
  `0.1.14` 的 release note 也記錄此版本的 prompt token usage 修正，故文件與
  package release 使用同一 immutable ref。[文件樹](https://github.com/sveltejs/ai-tools/tree/@sveltejs%2Fmcp@0.1.14/documentation/docs)、
  [CHANGELOG](https://github.com/sveltejs/ai-tools/blob/b891e4860b880144b15f2a86a4e1e98b1631c26f/packages/mcp-stdio/CHANGELOG.md)

兩者使用獨立 Collection，避免把 SvelteKit framework 文件或 MCP server 使用說明
混入既有 `svelte/5.57.0` 語料：

```text
corpus/sveltekit/2.70.3/
corpus/svelte-mcp/0.1.14/
```

## Ref 查證

官方 tag ref 透過 `git ls-remote` 查證。tag object 與 peeled commit 分開記錄，後者
才是 checkout 內容的 commit：

```text
git ls-remote --tags https://github.com/sveltejs/kit.git \
  refs/tags/@sveltejs/kit@2.70.3 refs/tags/@sveltejs/kit@2.70.3^{}

d3dd898b10ef5132fef50948032abc06b692e609  refs/tags/@sveltejs/kit@2.70.3
39e8e1fbd4feba7f22dd46bfdf7335362c38de16  refs/tags/@sveltejs/kit@2.70.3^{}

git ls-remote --tags https://github.com/sveltejs/ai-tools.git \
  refs/tags/@sveltejs/mcp@0.1.14 refs/tags/@sveltejs/mcp@0.1.14^{}

2124295d2110315d37bd5908fc8d69ff244e0f08  refs/tags/@sveltejs/mcp@0.1.14
b891e4860b880144b15f2a86a4e1e98b1631c26f  refs/tags/@sveltejs/mcp@0.1.14^{}
```

這兩個 ref 也分別在官方 Git checkout 中以 `git describe --tags --exact-match HEAD`
驗證為 `@sveltejs/kit@2.70.3` 與 `@sveltejs/mcp@0.1.14`。SvelteKit tag 的 commit
時間是 `2026-08-18T10:57:39-04:00`；MCP tag 的 commit 時間是
`2025-12-17T18:36:08+01:00`。

## Manifest 與抓取範圍

SvelteKit manifest 是
[`builder/manifests/sveltekit-2.70.3.toml`](../../builder/manifests/sveltekit-2.70.3.toml)：

```toml
name = "sveltekit-2.70.3"
collection = "sveltekit"
version = "2.70.3"
source_type = "git"
repo_url = "https://github.com/sveltejs/kit"
git_ref = "@sveltejs/kit@2.70.3"
docs_paths = ["documentation/docs"]
sparse_paths = ["documentation/docs"]
source_url_template = "{repo_url}/blob/{git_ref}/{path}"
```

Svelte MCP manifest 是
[`builder/manifests/svelte-mcp-0.1.14.toml`](../../builder/manifests/svelte-mcp-0.1.14.toml)：

```toml
name = "svelte-mcp-0.1.14"
collection = "svelte-mcp"
version = "0.1.14"
source_type = "git"
repo_url = "https://github.com/sveltejs/ai-tools"
git_ref = "@sveltejs/mcp@0.1.14"
docs_paths = ["documentation/docs"]
sparse_paths = ["documentation/docs"]
source_url_template = "{repo_url}/blob/{git_ref}/{path}"
```

兩份 manifest 都只取官方 `documentation/docs/`；README、package source、測試、
圖片與其他呈現資產不納入 corpus。MCP 使用 canonical `sveltejs/ai-tools` 作為
`repo_url`，因為 `sveltejs/mcp` 目前是重新導向入口；package metadata 與官方入口
仍保留原始 package repository 身分。

## 抓取與正規化結果

```shell
builder/.venv/bin/python builder/git_source.py fetch \
  builder/manifests/sveltekit-2.70.3.toml
builder/.venv/bin/python builder/git_source.py normalize \
  builder/manifests/sveltekit-2.70.3.toml

builder/.venv/bin/python builder/git_source.py fetch \
  builder/manifests/svelte-mcp-0.1.14.toml
builder/.venv/bin/python builder/git_source.py normalize \
  builder/manifests/svelte-mcp-0.1.14.toml
```

結果：

- `raw/sveltekit/2.70.3/repo` HEAD 為
  `39e8e1fbd4feba7f22dd46bfdf7335362c38de16`，文件樹 80 個 Markdown；
  `corpus/sveltekit/2.70.3/` 正規化為 80 頁。
- `raw/svelte-mcp/0.1.14/repo` HEAD 為
  `b891e4860b880144b15f2a86a4e1e98b1631c26f`，文件樹 10 個 Markdown；
  `corpus/svelte-mcp/0.1.14/` 正規化為 10 頁。
- 每頁均由既有 `git_source.py` 寫入 `collection`、精確 `version`、固定 tag
  `source_url` 與 upstream commit date 的 `fetched_at`。
- raw 與 corpus 的相對 Markdown inventory 一一對應；raw checkout 只保留 manifest
  指定的文件樹，不把其他 repository 資產誤當成文件頁。

## 驗證

以下檢查已在本地完成：

```text
git -C raw/sveltekit/2.70.3/repo rev-parse HEAD
# 39e8e1fbd4feba7f22dd46bfdf7335362c38de16
git -C raw/sveltekit/2.70.3/repo describe --tags --exact-match HEAD
# @sveltejs/kit@2.70.3
find raw/sveltekit/2.70.3/repo/documentation/docs -type f -name '*.md' | wc -l
# 80
find corpus/sveltekit/2.70.3 -type f -name '*.md' | wc -l
# 80

git -C raw/svelte-mcp/0.1.14/repo rev-parse HEAD
# b891e4860b880144b15f2a86a4e1e98b1631c26f
git -C raw/svelte-mcp/0.1.14/repo describe --tags --exact-match HEAD
# @sveltejs/mcp@0.1.14
find raw/svelte-mcp/0.1.14/repo/documentation/docs -type f -name '*.md' | wc -l
# 10
find corpus/svelte-mcp/0.1.14 -type f -name '*.md' | wc -l
# 10
```

另以 inventory diff、frontmatter 欄位、fenced code block 平衡、來源 URL 版本字串與
trailing whitespace 進行檢查；兩個 corpus 均通過。`raw/` 與 `index/` 依 repo
規範被 `.gitignore` 排除，不應提交。
