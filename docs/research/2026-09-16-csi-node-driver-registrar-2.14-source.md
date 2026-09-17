# CSI node-driver-registrar 2.14.0 文件來源記錄

## 結論

CSI node-driver-registrar 2.14.0 語料取自官方 [`kubernetes-csi/node-driver-registrar`](https://github.com/kubernetes-csi/node-driver-registrar) repository。
Manifest 直接固定到 release tag 的 peeled commit，只納入根目錄下的 `README.md` 與 `CONTRIBUTING.md`。
兩頁的 `source_url` 皆固定到同一個 40 字 commit，不使用 mutable 的 `master`、`main` 或 tag。

| 項目 | 內容 |
| --- | --- |
| 官方 repository | [`kubernetes-csi/node-driver-registrar`](https://github.com/kubernetes-csi/node-driver-registrar) |
| Release tag | `v2.14.0` |
| Tag object / Peeled commit | [`8bd83d14abc6a2abfeccaa87da919615a4ebc70e`](https://github.com/kubernetes-csi/node-driver-registrar/commit/8bd83d14abc6a2abfeccaa87da919615a4ebc70e) |
| Collection | `csi-node-driver-registrar` |
| Version | `2.14.0` |
| 文件範圍 | `README.md`, `CONTRIBUTING.md` |
| Corpus 頁數 | 2 頁 |

上述 tag 與 peeled commit 以 `git ls-remote` 對官方 repository 查證：

```shell
git ls-remote https://github.com/kubernetes-csi/node-driver-registrar 'refs/tags/v2.14.0*'
```

查證結果：
```text
8bd83d14abc6a2abfeccaa87da919615a4ebc70e	refs/tags/v2.14.0
```
該 tag 為 lightweight tag，tag 參照直接指向 peeled commit `8bd83d14abc6a2abfeccaa87da919615a4ebc70e`。

## 文件範圍與結構

本元件為 Kubernetes CSI sidecar，官方 repository 並未包含獨立的 Sphinx 或 MkDocs 網站目錄，核心說明文件即為根目錄的 `README.md` 與貢獻指南 `CONTRIBUTING.md`。
- `README.md`：說明 node-driver-registrar 職責、與 Kubelet plugin registration 機制的相容性表格、UNIX domain sockets 設定方式與命令列參數。
- `CONTRIBUTING.md`：社群參與規範、CLA 簽署與 Kubernetes 貢獻流程說明。

轉換後的 corpus 頁面 front matter 如下：
- Collection：`csi-node-driver-registrar`
- Version：`"2.14.0"`
- Source URL：
  - `https://github.com/kubernetes-csi/node-driver-registrar/blob/8bd83d14abc6a2abfeccaa87da919615a4ebc70e/README.md`
  - `https://github.com/kubernetes-csi/node-driver-registrar/blob/8bd83d14abc6a2abfeccaa87da919615a4ebc70e/CONTRIBUTING.md`

建置端的 `raw/csi-node-driver-registrar/` 與 air-gap 端可重建的 `index/docs.db` 皆不提交 Git。

## 重建指令

```shell
# 1. 抓取與正規化語料（建置端）
builder/.venv/bin/python builder/git_source.py all builder/manifests/node-driver-registrar-2.14.toml

# 2. 增量更新搜尋索引（Air-gap 端）
python3 runtime/build_index.py
```
