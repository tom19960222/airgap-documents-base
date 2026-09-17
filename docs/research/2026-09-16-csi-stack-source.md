# CSI stack 文件來源記錄

## 結論

本批新增 30 份 CSI component manifest 與 corpus，來源全部是官方 GitHub
repository 的 release tag，manifest 以 tag 對應的 40 字 peeled commit 固定來源，
共記錄 30 個版本、241 個 Markdown 頁面。每一頁的 `source_url` 都指向同一個
固定 commit，不使用
`master`、`main`、`tag` 或其他 mutable ref。

本次 hardening 另外在 Ceph CSI 3.15.1、3.16.3、3.17.1 與 ceph-csi-operator
1.0.4 四份 manifest 明確宣告 `mutable_refs = ["main", "master"]`。這是
source-link pinning 的 allowlist，不是文件版本來源：只有同一 repository 的
GitHub `blob`/`tree`/`raw` URL、`raw.githubusercontent.com` URL，以及普通正文
中的相同 repository URL 會把 allowlist ref 固定成該 manifest 的 40 字 commit；
非 asset 的 release-tag URL、cross-repository URL、fenced code 與 inline literal
保持不變，既有的 blob asset pinning 規則則維持原狀。

### 版本、tag、commit 與文件範圍

| 元件 | 版本 | 官方 release tag | 固定 commit | 文件範圍 | 頁數 | 狀態 |
| --- | --- | --- | --- | --- | ---: | --- |
| Ceph CSI | 3.15.1 | [v3.15.1](https://github.com/ceph/ceph-csi/tree/v3.15.1) | `f8b8b1416793ceaf6e01592b77f438e8b4c3b6b8` | `docs/`, `README.md` | 37 | 本批 |
| Ceph CSI | 3.16.3 | [v3.16.3](https://github.com/ceph/ceph-csi/tree/v3.16.3) | `6a6498b24a9c423c40a0116dc07688e8e6d76a6c` | `docs/`, `README.md` | 38 | 本批 |
| Ceph CSI | 3.17.1 | [v3.17.1](https://github.com/ceph/ceph-csi/tree/v3.17.1) | `e18ce8c76a24871d9abe905540d40bb80d0c40e1` | `docs/`, `README.md` | 41 | 本批 |
| ceph-csi-operator | 1.0.4 | [v1.0.4](https://github.com/ceph/ceph-csi-operator/tree/v1.0.4) | `29a66b683aa8873001c729b7b120e18604cdb445` | `docs/`, `README.md` | 17 | 本批 |
| external-provisioner | 5.1.0 | [v5.1.0](https://github.com/kubernetes-csi/external-provisioner/tree/v5.1.0) | `656955bc2294f10a5ec505acfac6091048e30a08` | `doc/`, `README.md`, `CONTRIBUTING.md` | 4 | 本批 |
| external-provisioner | 5.2.0 | [v5.2.0](https://github.com/kubernetes-csi/external-provisioner/tree/v5.2.0) | `12a344a40072d655cb9374a93483305f1a1be557` | `doc/`, `README.md`, `CONTRIBUTING.md` | 4 | 本批 |
| external-provisioner | 5.3.0 | [v5.3.0](https://github.com/kubernetes-csi/external-provisioner/tree/v5.3.0) | `1a7e9381439295969ad0336f1e21791f7dc3abe8` | `doc/`, `README.md`, `CONTRIBUTING.md` | 4 | 本批 |
| external-provisioner | 6.0.2 | [v6.0.2](https://github.com/kubernetes-csi/external-provisioner/tree/v6.0.2) | `753b615576935c6abdd9eb770708abb5845f2ee6` | `doc/`, `README.md`, `CONTRIBUTING.md` | 4 | 本批 |
| external-provisioner | 6.1.2 | [v6.1.2](https://github.com/kubernetes-csi/external-provisioner/tree/v6.1.2) | `bc5885430bd0312da7dbea82f6e09b5cc1456251` | `doc/`, `README.md`, `CONTRIBUTING.md` | 4 | 本批 |
| external-provisioner | 6.2.0 | [v6.2.0](https://github.com/kubernetes-csi/external-provisioner/tree/v6.2.0) | `4f8ed53be40718152d081eb485fcc388e7bd77fd` | `doc/`, `README.md`, `CONTRIBUTING.md` | 4 | 本批 |
| external-attacher | 4.8.0 | [v4.8.0](https://github.com/kubernetes-csi/external-attacher/tree/v4.8.0) | `16acc03adce9ae492e6e5cd4e6ef4a31cb9df7cc` | `doc/`, `README.md`, `CONTRIBUTING.md` | 3 | 本批 |
| external-attacher | 4.9.0 | [v4.9.0](https://github.com/kubernetes-csi/external-attacher/tree/v4.9.0) | `d87f235946455e247a9dc6401e3fbafc7031b220` | `doc/`, `README.md`, `CONTRIBUTING.md` | 3 | 本批 |
| external-attacher | 4.10.0 | [v4.10.0](https://github.com/kubernetes-csi/external-attacher/tree/v4.10.0) | `a54838aaedfb96ef9094aa8628be7a8ad930dd8f` | `doc/`, `README.md`, `CONTRIBUTING.md` | 3 | 本批 |
| external-attacher | 4.11.0 | [v4.11.0](https://github.com/kubernetes-csi/external-attacher/tree/v4.11.0) | `cc32e8cebcb4433b84c26aacc59e200aecd9f5be` | `doc/`, `README.md`, `CONTRIBUTING.md` | 3 | 本批 |
| external-attacher | 4.12.0 | [v4.12.0](https://github.com/kubernetes-csi/external-attacher/tree/v4.12.0) | `f395fb4ff4d3fb41d2e2dfde0f8373d9e7162aeb` | `doc/`, `README.md`, `CONTRIBUTING.md` | 3 | 本批 |
| external-resizer | 1.13.1 | [v1.13.1](https://github.com/kubernetes-csi/external-resizer/tree/v1.13.1) | `20072c0fdf8baaf919ef95d6e918538ba9d84eaf` | `README.md`, `CONTRIBUTING.md` | 2 | 本批 |
| external-resizer | 1.14.0 | [v1.14.0](https://github.com/kubernetes-csi/external-resizer/tree/v1.14.0) | `c82d78bf133263d5aae6c53f05a466f00c79a7cc` | `README.md`, `CONTRIBUTING.md` | 2 | 本批 |
| external-resizer | 2.0.0 | [v2.0.0](https://github.com/kubernetes-csi/external-resizer/tree/v2.0.0) | `665104f4a4eb88b48edd185d2b5544a5c850ac17` | `README.md`, `CONTRIBUTING.md` | 2 | 本批 |
| external-resizer | 2.1.0 | [v2.1.0](https://github.com/kubernetes-csi/external-resizer/tree/v2.1.0) | `aa898542ad5d6f459a30c694bafcaa03948b14b3` | `README.md`, `CONTRIBUTING.md` | 2 | 本批 |
| external-snapshotter | 8.2.0 | [v8.2.0](https://github.com/kubernetes-csi/external-snapshotter/tree/v8.2.0) | `0f215370c7ca3eeef4ab7028824d3bc66e1f63bd` | `README.md`, `CONTRIBUTING.md` | 2 | 本批 |
| external-snapshotter | 8.3.0 | [v8.3.0](https://github.com/kubernetes-csi/external-snapshotter/tree/v8.3.0) | `6b2feaaf7fc3d6d0fe21029d1032ea0eee2081e9` | `README.md`, `CONTRIBUTING.md` | 2 | 本批 |
| external-snapshotter | 8.4.0 | [v8.4.0](https://github.com/kubernetes-csi/external-snapshotter/tree/v8.4.0) | `f21cb02763e7cd6a7fc84846f106b83119b5371d` | `README.md`, `CONTRIBUTING.md` | 2 | 本批 |
| external-snapshotter | 8.5.0 | [v8.5.0](https://github.com/kubernetes-csi/external-snapshotter/tree/v8.5.0) | `5aab051d1af135e2c852f6fb7fc27fa709d877bf` | `README.md`, `CONTRIBUTING.md` | 2 | 本批 |
| node-driver-registrar | 2.14.0 | [v2.14.0](https://github.com/kubernetes-csi/node-driver-registrar/tree/v2.14.0) | `8bd83d14abc6a2abfeccaa87da919615a4ebc70e` | `README.md`, `CONTRIBUTING.md` | 2 | 本批 |
| node-driver-registrar | 2.15.0 | [v2.15.0](https://github.com/kubernetes-csi/node-driver-registrar/tree/v2.15.0) | `87d60a92e312fefe7965ccf2c2b88d6184e30077` | `README.md`, `CONTRIBUTING.md` | 2 | 本批 |
| node-driver-registrar | 2.16.0 | [v2.16.0](https://github.com/kubernetes-csi/node-driver-registrar/tree/v2.16.0) | `fb325021eed265c487fd3aa394d99806831b0eff` | `README.md`, `CONTRIBUTING.md` | 2 | 本批 |
| node-driver-registrar | 2.17.0 | [v2.17.0](https://github.com/kubernetes-csi/node-driver-registrar/tree/v2.17.0) | `c5794c45f34ce9c62e47dfd5a2b073c3824f2c79` | `README.md`, `CONTRIBUTING.md` | 2 | 本批 |
| CSI Addons | 0.12.0 | [v0.12.0](https://github.com/csi-addons/kubernetes-csi-addons/tree/v0.12.0) | `57383f123ba4500174f945b919e81f41b61541d9` | `docs/`, `README.md` | 13 | 本批 |
| CSI Addons | 0.13.0 | [v0.13.0](https://github.com/csi-addons/kubernetes-csi-addons/tree/v0.13.0) | `dc2e91db1a9d3878ab991dc025b59bebebb227b7` | `docs/`, `README.md` | 15 | 本批 |
| CSI Addons | 0.14.0 | [v0.14.0](https://github.com/csi-addons/kubernetes-csi-addons/tree/v0.14.0) | `621cfdc3b7d36922a8d328324643540eeac2671d` | `docs/`, `README.md` | 17 | 本批 |

`cephcsi` 3.16.3 與 CSI Addons 0.12.0、0.13.0、0.14.0 的 release tag 是
annotated tag；表內與 manifest 使用的是 tag 的 peeled commit，而不是 tag object
本身。其餘版本同樣以 fetched `git_meta.json` 的 40 字 commit 作為建置證據。

既有 `cephcsi` 3.14.0 與 `csi-node-driver-registrar` 2.13.0 維持原狀，依需求
不重建、不列入本批 30 個版本。

## 建置與驗證

每份 manifest 均使用 `source_type = "git"`、指定 40 字 `git_ref`，且
`docs_paths` 與 `sparse_paths` 完全相同。建置命令如下：

```shell
builder/.venv/bin/python builder/git_source.py all builder/manifests/<name>.toml
```

30 份本批 manifest 均逐一建置成功，沒有觸發空語料防護，共 241 頁；每頁
front matter 的 `collection`、`version` 均與 manifest
一致，`source_url` 格式為：

```text
https://github.com/<owner>/<repo>/blob/<40-hex-commit>/<relative-path>
```

靜態檢查確認所有 241 頁的 `source_url` 都使用 40 字 lowercase hexadecimal
commit，沒有 `master`、`main` 或 `tag` ref。共統計 177 個
`unresolved-source-link` marker，沒有 `unresolved-rst-link` marker；這些 marker
是文件範圍外的 upstream 連結被保留並分類的結果，不是空頁或建置失敗。

測試結果：

- `builder/tests`：整合後 74 tests，全部通過。
- `runtime/tests`：5 tests，全部通過。
- `runtime/build_index.py`：主整合流程已完成 full build 與兩次 incremental
  build；完整索引為 35,291 頁、300,450 個 chunks，兩次增量皆為 0 變更。

## 來源查證與重建

release tag 可由各官方 repository 的 tag 頁面查證；實際抓取時用指定 commit
執行 detached checkout，並由 `raw/<collection>/<version>/git_meta.json` 保存
`repo_url`、`git_ref`、`commit_hash` 與 commit date。corpus 與 manifest 會提交；
`raw/` 與 `index/docs.db` 是建置端或 air-gap 端產物，不列入來源變更。

重建全部 CSI corpus 後，再由 air-gap 端執行：

```shell
python3 runtime/build_index.py --full
python3 runtime/build_index.py
python3 runtime/build_index.py
```

第二次與第三次的增量結果均確認 `added`、`modified`、`deleted` 全為 0。
