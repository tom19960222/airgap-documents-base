# CDI v1.56.1 與 v1.66.1 官方來源研究

研究日期：2026-09-30（America/New_York）

本筆記只採用 KubeVirt 官方 `kubevirt/containerized-data-importer`
repository、官方 Git refs 與 GitHub releases。研究範圍是版本化的純文字文件來源，
不把 container image、release binary 或部署 manifest 當成文件頁。

## 結論

`v1.56.1` 與 `v1.66.1` 都是官方存在的 annotated tags，也都有非 draft、非
prerelease 的 GitHub release。可重現的文件來源應固定到 tag 的 peeled commit，
並收錄 repository 根層 `README.md` 與 `doc/` 下的 Markdown：

| 版本 | Tag object | Peeled commit | 官方文件範圍 | Markdown 頁數 |
| --- | --- | --- | --- | ---: |
| `1.56.1` | [`379055362f47d92a2632186cb702b09aa6f19ff4`](https://api.github.com/repos/kubevirt/containerized-data-importer/git/ref/tags/v1.56.1) | [`ee9a06635eed17f8a635915bbb2f354ce38c8f72`](https://github.com/kubevirt/containerized-data-importer/commit/ee9a06635eed17f8a635915bbb2f354ce38c8f72) | [`README.md`](https://github.com/kubevirt/containerized-data-importer/blob/ee9a06635eed17f8a635915bbb2f354ce38c8f72/README.md)、[`doc/`](https://github.com/kubevirt/containerized-data-importer/tree/ee9a06635eed17f8a635915bbb2f354ce38c8f72/doc) | 34 |
| `1.66.1` | [`a03bc9211c6eb86db90dbe554b3bf0000e701cf5`](https://api.github.com/repos/kubevirt/containerized-data-importer/git/ref/tags/v1.66.1) | [`c8129be0728afa1a2c49b69b1c0847a42730a732`](https://github.com/kubevirt/containerized-data-importer/commit/c8129be0728afa1a2c49b69b1c0847a42730a732) | [`README.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/README.md)、[`doc/`](https://github.com/kubevirt/containerized-data-importer/tree/c8129be0728afa1a2c49b69b1c0847a42730a732/doc) | 40 |

官方 release 頁分別是 [`v1.56.1`](https://github.com/kubevirt/containerized-data-importer/releases/tag/v1.56.1)
與 [`v1.66.1`](https://github.com/kubevirt/containerized-data-importer/releases/tag/v1.66.1)。
官方 release metadata 顯示 `v1.56.1` 發布於 2023-07-31、`v1.66.1` 發布於
2026-09-06；兩者的 `tag_name`、release name 都與指定版本一致。

## Tag 查證

官方 Git repository 的精確 refs 為：

```text
379055362f47d92a2632186cb702b09aa6f19ff4  refs/tags/v1.56.1
ee9a06635eed17f8a635915bbb2f354ce38c8f72  refs/tags/v1.56.1^{}
a03bc9211c6eb86db90dbe554b3bf0000e701cf5  refs/tags/v1.66.1
c8129be0728afa1a2c49b69b1c0847a42730a732  refs/tags/v1.66.1^{}
```

可重現命令：

```shell
git ls-remote --tags \
  https://github.com/kubevirt/containerized-data-importer.git \
  'refs/tags/v1.56.1' 'refs/tags/v1.56.1^{}' \
  'refs/tags/v1.66.1' 'refs/tags/v1.66.1^{}'
```

CDI 官方的 [`doc/releases.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/doc/releases.md)
規定版本格式為 `vMAJOR.MINOR.PATCH`，release branch 搭配 annotated tag 發布；
這也與上述 refs 的 tag object／peeled commit 形式一致。導入時以 40 字 peeled
commit 作 `git_ref`，可避免未來 tag 被移動時悄悄改變語料內容。

## 文件來源與路徑

兩個版本都使用同一個官方 repository：
<https://github.com/kubevirt/containerized-data-importer>。根層
[`README.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/README.md)
提供 CDI 概觀、DataVolume、各種 import／clone／upload 來源、部署與使用入口；
版本化的詳細文件則在 `doc/`。

- `v1.56.1` 的 [`doc/`](https://github.com/kubevirt/containerized-data-importer/tree/v1.56.1/doc)
  有 33 個 Markdown，加上根層 README 共 34 頁。
- `v1.66.1` 的 [`doc/`](https://github.com/kubevirt/containerized-data-importer/tree/v1.66.1/doc)
  有 39 個 Markdown，加上根層 README 共 40 頁。
- `doc/diagrams/` 的 PNG 是呈現資產，不是 Markdown page；`manifests/` 是部署與
  使用範例 YAML，不應擴張成本次純文字文件 corpus。

相較 `v1.56.1`，`v1.66.1` 的文件樹新增
[`build-the-builder.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/doc/build-the-builder.md)、
[`cdi-populators.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/doc/cdi-populators.md)、
[`datavolume-claim-adoption.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/doc/datavolume-claim-adoption.md)、
[`maintainer.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/doc/maintainer.md)、
[`onboarding-storage-provisioners.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/doc/onboarding-storage-provisioners.md)
與 [`pvc-mutating-webhook-rendering.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/doc/pvc-mutating-webhook-rendering.md)，
而多數既有頁面也有修改；不能以現有其他 CDI 版本的 40 頁 corpus 代替。

## `CDI importer` 的版本邊界

官方 release 將 `cdi-importer` 列為 CDI release 所發布的多個 container 之一，
同一 release 還包含 controller、cloner、uploadproxy、apiserver、uploadserver 與
operator；可見 [`v1.66.1` release`](https://github.com/kubevirt/containerized-data-importer/releases/tag/v1.66.1)。
repository 的 `cmd/cdi-importer/` 只有程式與 build 檔，沒有獨立的版本化 Markdown
文件。因此文件 collection 應沿用 `cdi`，不要建立虛構的 `cdi-importer` 文件
repository 或將 importer image tag 當成另一套 docs version。

Importer 操作相關說明已包含在官方 CDI 文件樹，例如
[`datavolumes.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/doc/datavolumes.md)、
[`image-from-registry.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/doc/image-from-registry.md)、
[`import-block-pv.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/doc/import-block-pv.md)
與 [`scratch-space.md`](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/doc/scratch-space.md)。

## 建議的 manifest contract

兩個版本均沿用既有 Git source builder，不需要新增 importer 專用 normalizer：

```toml
collection = "cdi"
source_type = "git"
repo_url = "https://github.com/kubevirt/containerized-data-importer"
docs_paths = ["doc", "README.md"]
sparse_paths = ["doc", "README.md"]
source_url_template = "{repo_url}/blob/{git_ref}/{path}"
```

版本欄位與固定 ref：

```text
version 1.56.1 -> git_ref ee9a06635eed17f8a635915bbb2f354ce38c8f72
version 1.66.1 -> git_ref c8129be0728afa1a2c49b69b1c0847a42730a732
```

本 repo 已有 `cdi/1.56.1` 的 manifest 與 34 頁 corpus；此次實作應保留並驗證，
只新增獨立的 `cdi/1.66.1` 版本，不覆寫 `1.56.1`，也不把內容合併成單一版本。

## 官方來源索引

- [CDI 官方 repository](https://github.com/kubevirt/containerized-data-importer)
- [`v1.56.1` tag tree](https://github.com/kubevirt/containerized-data-importer/tree/v1.56.1)
- [`v1.56.1` release](https://github.com/kubevirt/containerized-data-importer/releases/tag/v1.56.1)
- [`v1.56.1` peeled commit](https://github.com/kubevirt/containerized-data-importer/commit/ee9a06635eed17f8a635915bbb2f354ce38c8f72)
- [`v1.66.1` tag tree](https://github.com/kubevirt/containerized-data-importer/tree/v1.66.1)
- [`v1.66.1` release](https://github.com/kubevirt/containerized-data-importer/releases/tag/v1.66.1)
- [`v1.66.1` peeled commit](https://github.com/kubevirt/containerized-data-importer/commit/c8129be0728afa1a2c49b69b1c0847a42730a732)
- [官方版本與 release 流程](https://github.com/kubevirt/containerized-data-importer/blob/c8129be0728afa1a2c49b69b1c0847a42730a732/doc/releases.md)
