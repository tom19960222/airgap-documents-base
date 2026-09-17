# 核心／網路／虛擬化官方文件來源研究

## 結論

本批語料共新增 11 個 immutable Git source manifest，來源均為上游官方
repository，並以使用者指定的 40 字 commit checkout 後，由 repo 的
`builder/git_source.py` 實際 fetch + normalize。產出的 corpus 共 803 頁；raw
checkout 的 HEAD 均與 manifest 的 `git_ref` 完全相同。

每個 corpus 的 `source_url` 都固定在同一個 commit，不依賴 mutable 的
`main`、`master` 或 tag URL。manifest 使用不帶 `.git` 的 GitHub repository URL，
以避免和既有 `source_url_template` 組合成錯誤的 `repo.git/blob/...` 路徑。

## 官方來源與文件範圍

| 元件 | 官方 release/tag | Immutable commit | Manifest 文件範圍 | Corpus 頁數 |
| --- | --- | --- | --- | ---: |
| CRI-O | [`v1.31.5`](https://github.com/cri-o/cri-o/tree/v1.31.5) | [`5184b74964ef620d64169a41fd27afdba6fe130e`](https://github.com/cri-o/cri-o/commit/5184b74964ef620d64169a41fd27afdba6fe130e) | `docs`, `tutorials`, `install.md`, `README.md`, `CONTRIBUTING.md` | 15 |
| etcd | [`v3.6.10`](https://github.com/etcd-io/etcd/tree/v3.6.10) | [`db8d13a5421fcbd1c5825a148735b80c7d36cd2d`](https://github.com/etcd-io/etcd/commit/db8d13a5421fcbd1c5825a148735b80c7d36cd2d) | `Documentation`, `README.md` | 15 |
| CoreDNS | [`v1.11.1`](https://github.com/coredns/coredns/tree/v1.11.1) | [`ae2bbc29be1aaae0b3ded5d188968a6c97bb3144`](https://github.com/coredns/coredns/commit/ae2bbc29be1aaae0b3ded5d188968a6c97bb3144) | `plugin`, `README.md`, `CONTRIBUTING.md`, `notes`；不收錄 roff manpage | 122 |
| Kubernetes DNS / NodeLocal DNSCache | [`1.23.1`](https://github.com/kubernetes/dns/tree/1.23.1) | [`fd33e8663c6f83c771cdad6178614b882ae4fba0`](https://github.com/kubernetes/dns/commit/fd33e8663c6f83c771cdad6178614b882ae4fba0) | `docs`, `README.md` | 3 |
| Multus CNI | [`v4.1.4`](https://github.com/k8snetworkplumbingwg/multus-cni/tree/v4.1.4) | [`4fc16b3bb8e870d36291312bd78d356411b5cba0`](https://github.com/k8snetworkplumbingwg/multus-cni/commit/4fc16b3bb8e870d36291312bd78d356411b5cba0) | `docs`, `README.md` | 6 |
| Multus Dynamic Networks Controller | [`v0.3.5`](https://github.com/k8snetworkplumbingwg/multus-dynamic-networks-controller/tree/v0.3.5) | [`0546691af236bf825d1822d2ad9e7d6a22e10088`](https://github.com/k8snetworkplumbingwg/multus-dynamic-networks-controller/commit/0546691af236bf825d1822d2ad9e7d6a22e10088) | `README.md`, `CONTRIBUTING.md` | 2 |
| Cilium certgen | [`v0.2.0`](https://github.com/cilium/certgen/tree/v0.2.0) | [`e0a9610f6ca926ee382f1536498de988fafa3706`](https://github.com/cilium/certgen/commit/e0a9610f6ca926ee382f1536498de988fafa3706) | `README.md` | 1 |
| Hubble UI | [`v0.13.1`](https://github.com/cilium/hubble-ui/tree/v0.13.1) | [`a06e19ba65299c63a58034a360aeedde9266ec01`](https://github.com/cilium/hubble-ui/commit/a06e19ba65299c63a58034a360aeedde9266ec01) | `README.md` | 1 |
| KubeVirt | [`v1.6.4`](https://github.com/kubevirt/kubevirt/tree/v1.6.4) | [`ac5324e8f6e7cda1cfe92542df3ceb0cd0d8e68f`](https://github.com/kubevirt/kubevirt/commit/ac5324e8f6e7cda1cfe92542df3ceb0cd0d8e68f) | `docs`, `README.md` | 56 |
| CDI | [`v1.56.1`](https://github.com/kubevirt/containerized-data-importer/tree/v1.56.1) | [`ee9a06635eed17f8a635915bbb2f354ce38c8f72`](https://github.com/kubevirt/containerized-data-importer/commit/ee9a06635eed17f8a635915bbb2f354ce38c8f72) | `doc`, `README.md` | 34 |
| Cilium | [`v1.16.7`](https://github.com/cilium/cilium/tree/v1.16.7) | [`2ab5f8da5915992a1e548c290105dbc08f4be52d`](https://github.com/cilium/cilium/commit/2ab5f8da5915992a1e548c290105dbc08f4be52d) | `Documentation`（指定 commit 沒有 `README.md`，見偏差） | 548 |

對應 manifest 檔案位於 `builder/manifests/`：

- `crio-1.31.toml`
- `etcd-3.6.toml`
- `coredns-1.11.toml`
- `k8s-dns-1.23.toml`
- `multus-cni-4.1.toml`
- `multus-dynamic-networks-controller-0.3.toml`
- `cilium-certgen-0.2.toml`
- `hubble-ui-0.13.toml`
- `kubevirt-1.6.toml`
- `cdi-1.56.toml`
- `cilium-1.16.toml`

## 正規化與 provenance

所有來源均使用同一種可重現流程：

```shell
builder/.venv/bin/python builder/git_source.py all builder/manifests/<manifest>.toml
```

`raw/<collection>/<version>/repo` 只作建置端 checkout，不進 Git；`corpus/`
則保存正規化後的 Markdown。每頁 front matter 的 `collection`、`version`、
`fetched_at` 與 commit-pinned `source_url` 都由 manifest 與 raw checkout metadata
產生。11 個 raw checkout 的實際 HEAD 如下：

```text
crio/1.31.5                                  5184b74964ef620d64169a41fd27afdba6fe130e
etcd/3.6.10                                  db8d13a5421fcbd1c5825a148735b80c7d36cd2d
coredns/1.11.1                               ae2bbc29be1aaae0b3ded5d188968a6c97bb3144
k8s-dns/1.23.1                               fd33e8663c6f83c771cdad6178614b882ae4fba0
multus-cni/4.1.4                             4fc16b3bb8e870d36291312bd78d356411b5cba0
multus-dynamic-networks-controller/0.3.5     0546691af236bf825d1822d2ad9e7d6a22e10088
cilium-certgen/0.2.0                         e0a9610f6ca926ee382f1536498de988fafa3706
hubble-ui/0.13.1                             a06e19ba65299c63a58034a360aeedde9266ec01
kubevirt/1.6.4                               ac5324e8f6e7cda1cfe92542df3ceb0cd0d8e68f
cdi/1.56.1                                   ee9a06635eed17f8a635915bbb2f354ce38c8f72
cilium/1.16.7                               2ab5f8da5915992a1e548c290105dbc08f4be52d
```

Cilium 的 `Documentation` 同時包含 Markdown 與 RST；manifest 沿用 repo 既有
git-source RST profile／mapping 與 commit-pinned source URL。未知 Sphinx directive
或無法安全內嵌的 source include 會保留原文，不捏造渲染結果；這些原始 directive
屬於 normalized source 的明確限制，見驗證偏差。

## 查證到的偏差

### Cilium 根目錄 README 不存在

指定 commit `2ab5f8da...` 的 checkout 中沒有 `README.md`；查證後已從 manifest
移除不存在的路徑，實際 scope 只有 `Documentation/`，因此 fetch/normalize 不再
產生缺失路徑 warning。`Documentation/` 成功產生 548 頁，不是零頁或 fetch 失敗。
不能用另一個 branch 或 tag 的 README 補入 1.16.7 corpus，故本筆記保留使用者
原要求與 upstream 實際文件範圍的差異。

### Dynamic Networks Controller 的 CONTRIBUTING.md 存在

指定 commit `0546691a...` 實際包含 `CONTRIBUTING.md`，因此 manifest 沒有刪除該
路徑；該 collection 產生 `README.md` 與 `CONTRIBUTING.md` 兩頁。

### CoreDNS roff manpage 排除

CoreDNS manifest 只設定 `plugin`、`README.md`、`CONTRIBUTING.md` 與 `notes`，並
以 `exclude_globs` 明確排除 `*.roff`、`*.1`、`*.5`、`*.8`。實際 raw checkout
在這個 scope 沒有 roff 輸入，corpus 122 頁全為 Markdown；沒有把 roff manpage
誤當成可搜尋文件。

### etcd 與 KubeVirt 的 README basename collision 已修正

初次 normalize 時，etcd 的 `Documentation/README.md` 與 root `README.md`，以及
KubeVirt 的 `docs/README.md` 與 root `README.md`，曾因相同 basename 互相覆蓋。後續
git-source collision guard 已保留 root basename，並以完整 repository-relative path
為碰撞來源配置唯一輸出路徑；兩份 README 現在都保留，沒有手動改寫 generated
corpus。

重新 normalize 後，兩個 collection 都通過 `discovered=corpus` inventory 檢查：
etcd 為 15 個 discovered source／15 頁 corpus，KubeVirt 為 56 個 discovered
source／56 頁 corpus。

## 驗證結果

### Corpus inventory 與 metadata

每個 collection 都完成 raw source inventory、corpus page count、front matter
collection/version/source URL、raw metadata、raw HEAD 與 manifest commit 一致性
檢查。頁數如下：

| Collection/version | Raw 非空 source | Corpus page | Result |
| --- | ---: | ---: | --- |
| `crio/1.31.5` | 15 | 15 | PASS |
| `etcd/3.6.10` | 15 | 15 | PASS（collision guard；discovered=corpus） |
| `coredns/1.11.1` | 122 | 122 | PASS |
| `k8s-dns/1.23.1` | 3 | 3 | PASS |
| `multus-cni/4.1.4` | 6 | 6 | PASS |
| `multus-dynamic-networks-controller/0.3.5` | 2 | 2 | PASS |
| `cilium-certgen/0.2.0` | 1 | 1 | PASS |
| `hubble-ui/0.13.1` | 1 | 1 | PASS |
| `kubevirt/1.6.4` | 56 | 56 | PASS（collision guard；discovered=corpus） |
| `cdi/1.56.1` | 34 | 34 | PASS |
| `cilium/1.16.7` | 548 | 548 | PASS（README 缺失後已移除 manifest scope） |

所有 corpus `source_url` 均符合：

```text
https://github.com/<owner>/<repo>/blob/<指定40字commit>/<repo-relative-path>
```

抽查與全量檢查均沒有 `.git/blob/` source URL，也沒有零頁 corpus；CoreDNS scope
下沒有 roff 輸出。

### `validate_ceph_corpus.py`／等價內容檢查

既有 `builder/validate_ceph_corpus.py` 能共用 metadata、raw checkout、source URL、
local link 與 table 檢查，但它的名稱與 table heuristic 是為 Ceph RST corpus
設計，不適合把所有其他 repository 的 Markdown code example 當成失敗：

- CRI-O、k8s-dns、Multus CNI、Dynamic Networks Controller、Cilium certgen、Hubble
  UI、CDI：validator exit 0。
- etcd：3 個 residual table border 是 fenced `etcdctl` ASCII table 被 validator
  誤判；metadata、source URL、raw HEAD 與 page inventory 通過。
- CoreDNS：134 個 residual table border 主要是 `notes/` release-note TOML
  front matter 與 Markdown release example，被 Ceph table heuristic 誤判；scope、
  metadata、source URL 與 page inventory 通過。
- KubeVirt：5 個 residual table border 是 `docs/architecture.md` 的 ASCII
  architecture diagram，不是 RST table；其餘 metadata、source URL、raw HEAD 通過。
- Cilium：12 個 residual RST image/include 與 12 個 ASCII/table border 是上游
  Sphinx source directive 或文件內的示意表格；既有 normalizer 對 unknown
  directive 採保留原文策略，並非錯誤 source URL 或 metadata。

因此上述 4 個 collection 的 validator 非零結果已分類為現有 validator／上游
source-format limitation，不把它們宣稱為全部 offline link 或 RST 已解析。真正的
fetch、固定 commit、非零 corpus、front matter 與 source URL 檢查均已完成。

交付流程已在所有 corpus 完成後統一執行 builder 與 runtime 測試，並完成 35,291
頁、300,450 個 chunks 的 full index build 與兩次 0 變更的 incremental build。

## Downstream custom image 邊界

本語料只代表上述 upstream repository 與固定 commit 的官方 base documentation。
環境中若使用 `cilium-agent:1.16.7-custom-v5`、`cilium-operator:1.16.7-custom-v1`
或其他 custom image，custom image 可能包含 downstream patch、設定或打包差異；
本次沒有對應的 downstream source、digest 或差異證據，因此不宣稱 custom image
與 upstream 文件完全相同，也不建立另一個「custom」官方 corpus。Cilium custom
image 只能引用本 corpus 作為 upstream base reference。
