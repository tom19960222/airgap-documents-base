# Rook 1.18.11、1.19.11、1.20.7 文件來源

## 結論

三版語料都取自官方 [`rook/rook`](https://github.com/rook/rook) repository，manifest
直接固定到 annotated release tag 的 peeled commit，只納入 `Documentation/`。
每頁 `source_url` 也固定到同一個 40 字 commit，不依賴 mutable `master`。

| 版本 | tag object | peeled commit | corpus 頁數 |
| --- | --- | --- | ---: |
| 1.18.11 | `49998a2e69e14ae230e4f3c46e382d0e15d3661c` | [`8059413c805f8ed3a0992af0113c002b0250805e`](https://github.com/rook/rook/commit/8059413c805f8ed3a0992af0113c002b0250805e) | 86 |
| 1.19.11 | `29682148b7b5a5014537fe0c74add31e96134cff` | [`e6818be5fcdcc4e3752f1cb03a7c0fbcc12dbdf1`](https://github.com/rook/rook/commit/e6818be5fcdcc4e3752f1cb03a7c0fbcc12dbdf1) | 87 |
| 1.20.7 | `a7af4e3f464fbc31bd2dcc542532c215c32d0e77` | [`95a8e2a8b61cf7f8152213939f995c88a2e72ab6`](https://github.com/rook/rook/commit/95a8e2a8b61cf7f8152213939f995c88a2e72ab6) | 92 |

上述 tag object 與 peeled commit 是以 `git ls-remote` 對官方 repository 的
`refs/tags/v<version>` 與 `refs/tags/v<version>^{}` 核對。

## 文件範圍

三版 `Documentation/` 分別有 89、90、95 個 Markdown 候選。官方 `mkdocs.yml`
都用 `exclude` plugin 排除 `README.md`、`*.gotmpl` 與 `*.gotmpl.md`；依同一規則
排除根目錄 redirect source 與兩個 Helm template 後，得到 86、87、92 個正式
prose pages。這也避免把 `{{ template ... }}` 帶入 corpus。

`Documentation/Getting-Started/intro.md` 與 `ceph-teardown.md` 是官方 symlink
頁；兩者都會從固定 checkout materialize 並保留。相對 Markdown page links 會改成
corpus-local 路徑；同 repository 的 GitHub `blob/master`、`tree/master` 連結則改成
manifest 指定 commit。percent-encoded asset 路徑會解析後改成 commit-pinned URL。

建置端的 `raw/rook/` 與 air-gap 端可重建的 `index/docs.db` 都不提交 Git。

```shell
builder/.venv/bin/python builder/git_source.py all builder/manifests/rook-1.18.toml
builder/.venv/bin/python builder/git_source.py all builder/manifests/rook-1.19.toml
builder/.venv/bin/python builder/git_source.py all builder/manifests/rook-1.20.toml
python3 runtime/build_index.py
```
