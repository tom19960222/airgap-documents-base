# 2026-09-16 元件文件版本與官方來源盤點

## 結論摘要

這份筆記前半段保留 2026-09-16 抓取前的來源與版本研究，後半段追加使用者確認後
實際建立的 manifest、corpus 與驗證結果。盤點判定原則如下：

1. 只採用專案官方 repository、官方文件網站、官方 Helm repository 或官方
   release/tag；image registry 的自訂 tag 本身不能證明 upstream 文件版本。
2. 使用者指定的端點版本照原值保留，即使同一 minor 已有較新的 patch，也不擅自
   升級端點。
3. 同一元件的兩個端點若相差超過一個 minor，依官方已發布的 minor line，加入每個
   中間 minor 在盤點日可確認的最新 stable patch。不存在的 minor line 不虛構。
4. app、Helm chart、Linux distribution package、downstream image 的版本命名空間
   分開處理；能證實對應關係時可共用同一份 upstream 文件，但不拿不同命名空間做
   minor 補版。
5. 「證實」代表官方來源可直接驗證；「推論」代表名稱或 chart metadata 可合理
   對應，但仍有部署端覆寫的可能；「未知」代表沒有足夠第一方資訊唯一定位專案。

本次「補中間 minor」規則只適用於使用者在本次需求中明確提供、且屬於同一元件的
兩個版本端點；既有 corpus 的 KubeVirt 1.9.0、CDI 1.64.0、kernel 6.8 並不構成
本次 KubeVirt 1.6.4、CDI 1.56.1、kernel 6.17 的第二個需求端點，因此不以它們
反向推導或補出另一組 minor。這個邊界也適用於其他同名但版本軸不同的 collection。

## 需要補齊中間 minor 的版本

以下是本次唯一需要展開中間 minor 的版本集合。連結皆指向官方 tag 清單或固定 tag。

| 專案 | 使用者的兩個端點 | 中間 minor 最新 stable patch | 本次應新增的版本 | 判定 |
| --- | --- | --- | --- | --- |
| Ceph CSI | 3.14.0 → 3.17.1 | [3.15.1](https://github.com/ceph/ceph-csi/tree/v3.15.1)、[3.16.3](https://github.com/ceph/ceph-csi/tree/v3.16.3) | 3.15.1、3.16.3、[3.17.1](https://github.com/ceph/ceph-csi/tree/v3.17.1)；3.14.0 已存在 | 證實 |
| CSI node-driver-registrar | 2.13.0 → 2.17.0 | [2.14.0](https://github.com/kubernetes-csi/node-driver-registrar/tree/v2.14.0)、[2.15.0](https://github.com/kubernetes-csi/node-driver-registrar/tree/v2.15.0)、[2.16.0](https://github.com/kubernetes-csi/node-driver-registrar/tree/v2.16.0) | 2.14.0、2.15.0、2.16.0、[2.17.0](https://github.com/kubernetes-csi/node-driver-registrar/tree/v2.17.0)；2.13.0 已存在 | 證實 |
| CSI external-provisioner | 5.1.0 → 6.2.0 | [5.2.0](https://github.com/kubernetes-csi/external-provisioner/tree/v5.2.0)、[5.3.0](https://github.com/kubernetes-csi/external-provisioner/tree/v5.3.0)、[6.0.2](https://github.com/kubernetes-csi/external-provisioner/tree/v6.0.2)、[6.1.2](https://github.com/kubernetes-csi/external-provisioner/tree/v6.1.2) | [5.1.0](https://github.com/kubernetes-csi/external-provisioner/tree/v5.1.0)、5.2.0、5.3.0、6.0.2、6.1.2、[6.2.0](https://github.com/kubernetes-csi/external-provisioner/tree/v6.2.0) | 證實；盤點日已有 6.2.1，但端點仍依使用者指定 6.2.0 |
| CSI external-attacher | 4.8.0 → 4.12.0 | [4.9.0](https://github.com/kubernetes-csi/external-attacher/tree/v4.9.0)、[4.10.0](https://github.com/kubernetes-csi/external-attacher/tree/v4.10.0)、[4.11.0](https://github.com/kubernetes-csi/external-attacher/tree/v4.11.0) | [4.8.0](https://github.com/kubernetes-csi/external-attacher/tree/v4.8.0)、4.9.0、4.10.0、4.11.0、[4.12.0](https://github.com/kubernetes-csi/external-attacher/tree/v4.12.0) | 證實 |
| CSI external-resizer | 1.13.1 → 2.1.0 | [1.14.0](https://github.com/kubernetes-csi/external-resizer/tree/v1.14.0)、[2.0.0](https://github.com/kubernetes-csi/external-resizer/tree/v2.0.0) | [1.13.1](https://github.com/kubernetes-csi/external-resizer/tree/v1.13.1)、1.14.0、2.0.0、[2.1.0](https://github.com/kubernetes-csi/external-resizer/tree/v2.1.0) | 證實；盤點日已有 1.13.2，但端點仍依使用者指定 1.13.1 |
| CSI external-snapshotter | 8.2.0 → 8.5.0 | [8.3.0](https://github.com/kubernetes-csi/external-snapshotter/tree/v8.3.0)、[8.4.0](https://github.com/kubernetes-csi/external-snapshotter/tree/v8.4.0) | [8.2.0](https://github.com/kubernetes-csi/external-snapshotter/tree/v8.2.0)、8.3.0、8.4.0、[8.5.0](https://github.com/kubernetes-csi/external-snapshotter/tree/v8.5.0) | 證實 |
| Kubernetes CSI Addons | 0.12.0 → 0.14.0 | [0.13.0](https://github.com/csi-addons/kubernetes-csi-addons/tree/v0.13.0) | [0.12.0](https://github.com/csi-addons/kubernetes-csi-addons/tree/v0.12.0)、0.13.0、[0.14.0](https://github.com/csi-addons/kubernetes-csi-addons/tree/v0.14.0) | 證實 |
| Rook | 1.17.2 → 1.20.7 | 1.18.11、1.19.11 | 無；1.17.2、1.18.11、1.19.11、1.20.7 全部已存在 | 證實；官方來源為 [rook/rook](https://github.com/rook/rook/tags) |

Ceph 19.2.2 與 20.2.4 雖跨 major release，但使用者沒有要求補 Ceph 20.0/20.1，
而且 Ceph stable release 的版本軸不是本規則所稱的連續元件 minor；兩個端點也都已
存在。本次不額外推導不存在於需求中的 Ceph 版本。官方 release 可由
[Ceph releases](https://docs.ceph.com/en/latest/releases/) 與
[ceph/ceph tags](https://github.com/ceph/ceph/tags) 驗證。

## 盤點時尚未存在、其後已抓取的正式文件

「文件版本」是呈現在 corpus 的版本；「固定來源」是實際取得文件時使用的
第一方來源。只含 README 的小型專案仍可離線取得正式使用說明，但文件量會比完整
manual 小。

### 核心平台、網路與儲存

| 專案／涵蓋元件 | 文件版本 | 固定來源與範圍 | 判定 |
| --- | --- | --- | --- |
| CRI-O | 1.31.5 | [cri-o/cri-o v1.31.5](https://github.com/cri-o/cri-o/tree/v1.31.5)，以 website/docs、README 與 release 文件為準 | 證實 |
| etcd | 3.6.10 | [etcd-io/etcd v3.6.10](https://github.com/etcd-io/etcd/tree/v3.6.10)；官方 [3.6 文件](https://etcd.io/docs/v3.6/) 可交叉核對。image 的 3.6.10-0 尾碼是包裝 revision，不是另一個 etcd 文件版本 | 證實 |
| Ubuntu | 22.04、24.04、26.04 | [Ubuntu 22.04 release notes](https://documentation.ubuntu.com/release-notes/22.04/)、[24.04 release notes](https://documentation.ubuntu.com/release-notes/24.04/)、[26.04 release notes](https://documentation.ubuntu.com/release-notes/26.04/) | 證實；三者都是各自固定版本的 release notes。它們不代表 [Ubuntu Server rolling 文件](https://documentation.ubuntu.com/server/)，該文件明示以最新 LTS 為目標，不能冒充固定 release manual |
| Linux kernel | 6.17 | [kernel.org v6.17 文件](https://www.kernel.org/doc/html/v6.17/)；6.17.0-20-generic 的 -20-generic 是 Ubuntu ABI/flavour，不是 upstream 文件版本 | 證實 |
| Cilium（CNI、agent、operator、multi-rack operator） | 1.16.7 | [cilium/cilium v1.16.7](https://github.com/cilium/cilium/tree/v1.16.7/Documentation)；custom-v5/custom-v1 只代表 downstream image，沒有第二份 upstream 文件 | 證實 base 版本；custom 差異未知 |
| Cilium certgen | 0.2.0 | [cilium/certgen v0.2.0](https://github.com/cilium/certgen/tree/v0.2.0)，README 為主要正式說明 | 證實 |
| Hubble backend/frontend | 0.13.1 | [cilium/hubble-ui v0.13.1](https://github.com/cilium/hubble-ui/tree/v0.13.1)，同一 release 包含 backend/frontend | 證實 |
| Istio／istioctl | 1.24.0 | app 固定 [istio/istio 1.24.0](https://github.com/istio/istio/tree/1.24.0)；完整官方網站 source 固定 [istio/istio.io release-1.24](https://github.com/istio/istio.io/tree/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs) | 證實；1.24.0-custom-v2 不產生額外 upstream 文件版本 |
| CoreDNS | 1.11.1 | [coredns/coredns v1.11.1](https://github.com/coredns/coredns/tree/v1.11.1)，以 plugin、man 與 README 文件為準 | 證實 |
| Node Local DNS cache | 1.23.1 | [kubernetes/dns 1.23.1](https://github.com/kubernetes/dns/tree/1.23.1)，NodeLocal DNSCache 位於 nodelocaldns；deployment v8 是部署資產標籤，不是 upstream release | 證實 image base；v8 無法映射成另一個官方文件版本 |
| Multus CNI | 4.1.4 | [k8snetworkplumbingwg/multus-cni v4.1.4](https://github.com/k8snetworkplumbingwg/multus-cni/tree/v4.1.4) | 證實 |
| Dynamic Networks Controller | 0.3.5 | [k8snetworkplumbingwg/multus-dynamic-networks-controller v0.3.5](https://github.com/k8snetworkplumbingwg/multus-dynamic-networks-controller/tree/v0.3.5) | 證實 |
| ceph-csi-operator | 1.0.4 | [ceph/ceph-csi-operator v1.0.4](https://github.com/ceph/ceph-csi-operator/tree/v1.0.4) | 證實 |
| Ceph CSI | 3.15.1、3.16.3、3.17.1 | 上一節列出的 [ceph/ceph-csi](https://github.com/ceph/ceph-csi/tags) 固定 tags；3.14.0 已存在 | 證實 |
| CSI external-provisioner | 5.1.0、5.2.0、5.3.0、6.0.2、6.1.2、6.2.0 | [kubernetes-csi/external-provisioner tags](https://github.com/kubernetes-csi/external-provisioner/tags)，README/docs | 證實 |
| CSI external-attacher | 4.8.0、4.9.0、4.10.0、4.11.0、4.12.0 | [kubernetes-csi/external-attacher tags](https://github.com/kubernetes-csi/external-attacher/tags)，README/docs | 證實 |
| CSI external-resizer | 1.13.1、1.14.0、2.0.0、2.1.0 | [kubernetes-csi/external-resizer tags](https://github.com/kubernetes-csi/external-resizer/tags)，README/docs | 證實 |
| CSI external-snapshotter | 8.2.0、8.3.0、8.4.0、8.5.0 | [kubernetes-csi/external-snapshotter tags](https://github.com/kubernetes-csi/external-snapshotter/tags)，README/docs | 證實 |
| CSI node-driver-registrar | 2.14.0、2.15.0、2.16.0、2.17.0 | [kubernetes-csi/node-driver-registrar tags](https://github.com/kubernetes-csi/node-driver-registrar/tags)；2.13.0 已存在 | 證實 |
| Kubernetes CSI Addons | 0.12.0、0.13.0、0.14.0 | [csi-addons/kubernetes-csi-addons tags](https://github.com/csi-addons/kubernetes-csi-addons/tags) | 證實 |
| KubeVirt | 1.6.4 | [kubevirt/kubevirt v1.6.4](https://github.com/kubevirt/kubevirt/tree/v1.6.4/docs) 的 source docs 與 README | 證實但範圍有限；官方 [kubevirt/user-guide](https://github.com/kubevirt/user-guide/branches) 沒有 v1.6 tag/branch，不能把現行 user guide 標成精確 1.6.4 |
| CDI | 1.56.1 | [kubevirt/containerized-data-importer v1.56.1](https://github.com/kubevirt/containerized-data-importer/tree/v1.56.1) | 證實 |

Node Local DNS image tag v1.23.1-coredns-1.10.8 的第一段可由 kubernetes/dns
1.23.1 官方 tag 證實；coredns-1.10.8 是該 image 內含 CoreDNS 的描述，CoreDNS
官方 tags 並沒有 v1.10.8。因此不能額外建立「CoreDNS 1.10.8」文件集合；需求中
獨立指定的 CoreDNS v1.11.1 才是可固定的正式版本。官方 tag 清單：
[kubernetes/dns tags](https://github.com/kubernetes/dns/tags)、
[coredns/coredns tags](https://github.com/coredns/coredns/tags)。

### 監控、身分驗證與 policy

| 專案／涵蓋元件 | 文件版本 | 固定來源與版本映射 | 判定 |
| --- | --- | --- | --- |
| Prometheus | 2.51.2 | [prometheus/prometheus v2.51.2](https://github.com/prometheus/prometheus/tree/v2.51.2/documentation)；debian-12-r0 是 image rebuild suffix | 證實 |
| Prometheus Operator | 0.73.2 | [prometheus-operator/prometheus-operator v0.73.2](https://github.com/prometheus-operator/prometheus-operator/tree/v0.73.2/Documentation) | 證實 |
| Bitnami kube-prometheus chart | 9.0.5 | 官方 [kube-prometheus-9.0.5.tgz](https://charts.bitnami.com/bitnami/kube-prometheus-9.0.5.tgz)；官方 index 的 appVersion 是 0.73.2，與上述 Operator 對應 | 證實 chart metadata |
| Alertmanager | 0.27.0 | [prometheus/alertmanager v0.27.0](https://github.com/prometheus/alertmanager/tree/v0.27.0)；debian-12-r4 是 image rebuild suffix | 證實 |
| node_exporter | 1.7.0 | [prometheus/node_exporter v1.7.0](https://github.com/prometheus/node_exporter/tree/v1.7.0)；清單中的重複列只需一份 corpus | 證實 |
| kube-state-metrics | 2.12.0 | [kubernetes/kube-state-metrics v2.12.0](https://github.com/kubernetes/kube-state-metrics/tree/v2.12.0/docs)；debian-12-r2 是 image rebuild suffix | 證實 |
| Thanos | 0.37.1 | [thanos-io/thanos v0.37.1](https://github.com/thanos-io/thanos/tree/v0.37.1/docs)；兩筆相同 sidecar 只需一份 corpus | 證實 |
| Pushgateway | app 1.6.2；chart 2.4.1 | app 用 [prometheus/pushgateway v1.6.2](https://github.com/prometheus/pushgateway/tree/v1.6.2)；chart 用 [prometheus-community chart 2.4.1](https://github.com/prometheus-community/helm-charts/tree/prometheus-pushgateway-2.4.1/charts/prometheus-pushgateway) | 證實；chart 預設 appVersion 是 v1.6.1，環境的 v1.6.2 是明確 image override，不能把兩者寫成完全相同 |
| oauth2-proxy | app 7.4.0；chart 6.16.1 | [oauth2-proxy v7.4.0](https://github.com/oauth2-proxy/oauth2-proxy/tree/v7.4.0/docs)；[chart 6.16.1](https://github.com/oauth2-proxy/manifests/tree/oauth2-proxy-6.16.1/helm/oauth2-proxy) 的 appVersion 為 7.4.0 | 證實 |
| Prometheus Adapter | chart 2.17.0；推定 app 0.9.0 | [prometheus-adapter chart 2.17.0](https://github.com/prometheus-community/helm-charts/tree/prometheus-adapter-2.17.0/charts/prometheus-adapter) 的 appVersion 是 v0.9.0；app 文件可用 [kubernetes-sigs/prometheus-adapter v0.9.0](https://github.com/kubernetes-sigs/prometheus-adapter/tree/v0.9.0/docs) | chart 證實；app 版本是未提供 image override 時的推論 |
| Node Problem Detector | 0.8.18 | [kubernetes/node-problem-detector v0.8.18](https://github.com/kubernetes/node-problem-detector/tree/v0.8.18)；官方 tags 沒有 v20260728 | 證實 app；v20260728 是 downstream release label，不能建立第二份 upstream 文件 |
| cert-manager | 1.14.7／文件線 1.14 | release 用 [cert-manager v1.14.7](https://github.com/cert-manager/cert-manager/tree/v1.14.7)；官方網站保留 [v1.14-docs](https://cert-manager.io/v1.14-docs/)，source 是網站 repository 的 frozen content/v1.14-docs 路徑 | 證實；網站沒有對應 1.14.7 的獨立完整 docs tag，應固定網站 commit 再抓 frozen 路徑 |
| OPA Gatekeeper | 3.18.2 | [open-policy-agent/gatekeeper v3.18.2](https://github.com/open-policy-agent/gatekeeper/tree/v3.18.2/website) | 證實 |
| Dex | app 2.42.0；chart 0.23.0 | [dexidp/dex v2.42.0](https://github.com/dexidp/dex/tree/v2.42.0/Documentation)；[Dex chart 0.23.0](https://github.com/dexidp/helm-charts/tree/dex-0.23.0/charts/dex) 的 appVersion 是 2.42.0 | 證實 |
| Vault Secrets Operator | app 1.26.0；chart 2.7.0 | 正確專案是 [ricoberger/vault-secrets-operator v1.26.0](https://github.com/ricoberger/vault-secrets-operator/tree/v1.26.0)，不是 HashiCorp VSO；固定 commit [`0522e930be76ea763c6611a130d44b7ef59182b0`](https://github.com/ricoberger/vault-secrets-operator/commit/0522e930be76ea763c6611a130d44b7ef59182b0) 的 root `README.md` 實際連到 `charts/README.md`，同一 commit 的 [Chart.yaml](https://github.com/ricoberger/vault-secrets-operator/blob/0522e930be76ea763c6611a130d44b7ef59182b0/charts/vault-secrets-operator/Chart.yaml) 明列 `appVersion: v1.26.0`、`version: 2.7.0`；兩頁均已納入 corpus | 證實；固定 source 同時涵蓋 runtime 與 chart 說明 |
| Telegraf | 1.30.3 | [influxdata/telegraf v1.30.3](https://github.com/influxdata/telegraf/tree/v1.30.3/docs) | base 版本推論；telegraf-1.30.3.8 尾碼不是 upstream SemVer，需部署 image metadata 才能解釋 .8 |

### Logging 與 exporter

| 專案／涵蓋元件 | 文件版本 | 固定來源與版本映射 | 判定 |
| --- | --- | --- | --- |
| OpenSearch | app 2.19.3；文件線 2.19；chart 2.27.0 | app release [opensearch-project/OpenSearch 2.19.3](https://github.com/opensearch-project/OpenSearch/tree/2.19.3)；完整官方 docs 固定 [documentation-website 2.19 branch commit cc01280](https://github.com/opensearch-project/documentation-website/tree/cc01280fc1f773421cbcb409bdc8fd7beae2638e)；[chart 2.27.0](https://github.com/opensearch-project/helm-charts/tree/opensearch-2.27.0/charts/opensearch) | 證實；chart 預設 appVersion 2.18.0，環境 2.19.3 是 override |
| OpenSearch Dashboards | app 2.19.1；文件線 2.19；chart 2.25.0 | [OpenSearch-Dashboards 2.19.1](https://github.com/opensearch-project/OpenSearch-Dashboards/tree/2.19.1) 與同一份 2.19 官方 docs；[chart 2.25.0](https://github.com/opensearch-project/helm-charts/tree/opensearch-dashboards-2.25.0/charts/opensearch-dashboards) | 證實；chart 預設 appVersion 2.18.0，環境 2.19.1 是 override |
| Fluent Bit | app 3.2.10；文件線 3.2；chart 0.48.10 | [fluent/fluent-bit v3.2.10](https://github.com/fluent/fluent-bit/tree/v3.2.10)；完整 docs 固定 [fluent-bit-docs 3.2 branch commit 36106a0](https://github.com/fluent/fluent-bit-docs/tree/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21)；[chart 0.48.10](https://github.com/fluent/helm-charts/tree/fluent-bit-0.48.10/charts/fluent-bit) 的 appVersion 是 3.2.10 | 證實 |
| Fluentd | 1.18.0 | [fluent/fluentd v1.18.0](https://github.com/fluent/fluentd/tree/v1.18.0/docs)；event exporter sidecar tag 中的 debian-elasticsearch7-1.2-splunk-v3 是 downstream 組裝 suffix | 證實 base 版本 |
| x509 Certificate Exporter chart | 3.18.1 | [enix/x509-certificate-exporter v3.18.1](https://github.com/enix/x509-certificate-exporter/tree/v3.18.1/deploy/x509-certificate-exporter)，README/chart docs 可固定 | 證實 chart tag；source Chart.yaml 的 appVersion 是 release 打包時注入的 placeholder，不能由 source tag反推另一個 executable 版本 |
| FRR Exporter | 1.3.3 | [tynany/frr_exporter v1.3.3](https://github.com/tynany/frr_exporter/tree/v1.3.3)，README 為主要正式文件 | 證實 |
| Blackbox Exporter | 0.25.0 | [prometheus/blackbox_exporter v0.25.0](https://github.com/prometheus/blackbox_exporter/tree/v0.25.0) | 證實 |
| smartctl_exporter | 0.14.0 | [prometheus-community/smartctl_exporter v0.14.0](https://github.com/prometheus-community/smartctl_exporter/tree/v0.14.0) | 證實 |
| keepalived-exporter | 1.3.2 | [mehdy/keepalived-exporter v1.3.2](https://github.com/mehdy/keepalived-exporter/tree/v1.3.2)；linux-amd64 是 artifact architecture，Ubuntu 22.04 是執行環境 | 證實 |

## 已存在，因此不列入後續抓取

本節由 repository 內既有 manifest 驗證；官方連結只用來確認其產品身分。

| 使用者項目 | 已存在的 corpus | 處理 |
| --- | --- | --- |
| Kubernetes／kubeadm／kubelet／kubectl 1.31.5 | k8s 1.31.6 | 略過。Kubernetes 正式文件以 minor release 分站；現有 1.31 corpus 已覆蓋相同 1.31 文件線。這是 repo 文件政策推論，不代表 1.31.5 與 1.31.6 binary 完全相同；官方 [v1.31 文件](https://v1-31.docs.kubernetes.io/docs/home/) 可核對 |
| Ceph Provider 19.2.2、cephadm package 19.2.2-1jammy、ceph-common package 19.2.2-1jammy | ceph 19.2.2 | 略過。-1jammy 是 Ubuntu package revision，不是另一份 Ceph upstream docs；官方 [v19.2.2](https://github.com/ceph/ceph/tree/v19.2.2) |
| Ceph Provider 20.2.4（Tentacle） | ceph 20.2.4 | 略過；官方 [v20.2.4](https://github.com/ceph/ceph/tree/v20.2.4) |
| Rook operator 1.17.2、1.20.7 與需補的 1.18.11、1.19.11 | rook 1.17.2、1.18.11、1.19.11、1.20.7 | 全部略過；官方 [Rook tags](https://github.com/rook/rook/tags) |
| ceph-csi 3.14.0 | cephcsi 3.14.0 | 略過；只新增 3.15.1、3.16.3、3.17.1。官方 [v3.14.0](https://github.com/ceph/ceph-csi/tree/v3.14.0) |
| CSI node-driver-registrar 2.13.0 | csi-node-driver-registrar 2.13.0 | 略過；只新增 2.14.0 至 2.17.0。官方 [v2.13.0](https://github.com/kubernetes-csi/node-driver-registrar/tree/v2.13.0) |

現有 KubeVirt 1.9.0、CDI 1.64.0、kernel 6.8 與 libvirt 12.7 不等於本次指定的
KubeVirt 1.6.4、CDI 1.56.1、kernel 6.17 或 libvirt exporter；不能因為 collection
名稱相近而略過本次目標。

## 不應建立重複 corpus 的版本別名

| 環境標籤 | 應映射到的文件 | 理由與官方證據 |
| --- | --- | --- |
| Cilium agent 1.16.7-custom-v5、operator multi-rack 1.16.7-custom-v1 | Cilium 1.16.7 | upstream [v1.16.7](https://github.com/cilium/cilium/tree/v1.16.7) 可證實 base；custom 差異需內部 source/digest，不能另稱官方版本 |
| Istio custom image 1.24.0-custom-v2 | Istio 1.24.0 | upstream [1.24.0](https://github.com/istio/istio/tree/1.24.0) 可證實 base |
| Prometheus、Operator、Alertmanager、node_exporter、kube-state-metrics、Thanos 的 -debian-12-rN | 去掉 suffix 後的 app 版本 | suffix 是 downstream image rebuild；各 app 固定 tag 已列於上表 |
| Node Problem Detector label v20260728 | Node Problem Detector 0.8.18 | 官方 [tags](https://github.com/kubernetes/node-problem-detector/tags) 有 v0.8.18、沒有 v20260728 |
| Node Local DNS deployment v8 | kubernetes/dns 1.23.1 | v8 是部署 manifest/內部 release label，官方軟體 release 是 [1.23.1](https://github.com/kubernetes/dns/tree/1.23.1) |
| Vault Secrets Operator chart 2.7.0 | ricoberger VSO app 1.26.0 的同一固定 source | 固定 commit [`0522e930be76ea763c6611a130d44b7ef59182b0`](https://github.com/ricoberger/vault-secrets-operator/commit/0522e930be76ea763c6611a130d44b7ef59182b0) 下的 `charts/README.md` 是 root README 連結的 chart 說明；官方 [Chart.yaml](https://github.com/ricoberger/vault-secrets-operator/blob/0522e930be76ea763c6611a130d44b7ef59182b0/charts/vault-secrets-operator/Chart.yaml) 直接證實兩個版本欄位 |
| Dex chart 0.23.0 | Dex app 2.42.0，另保留 chart README | 官方 [Chart.yaml](https://github.com/dexidp/helm-charts/blob/dex-0.23.0/charts/dex/Chart.yaml) 直接證實 appVersion |
| Fluent Bit chart 0.48.10 | Fluent Bit app 3.2.10，另保留 chart README | 官方 [Chart.yaml](https://github.com/fluent/helm-charts/blob/fluent-bit-0.48.10/charts/fluent-bit/Chart.yaml) 直接證實 appVersion |
| oauth2-proxy chart 6.16.1 | oauth2-proxy app 7.4.0，另保留 chart README | 官方 [Chart.yaml](https://github.com/oauth2-proxy/manifests/blob/oauth2-proxy-6.16.1/helm/oauth2-proxy/Chart.yaml) 直接證實 appVersion |

## 目前無法唯一辨識，暫停抓取

下列名稱、tag 或 release label 無法由第一方公開來源唯一定位。若直接抓取，最容易
把同名專案、downstream fork 或內部 image 錯當 upstream。需要部署 manifest 中的
完整 image repository 與 digest，或內部 Git repository/commit 後才能繼續。

| 使用者項目 | 現況 | 所需補充 |
| --- | --- | --- |
| tools-net sidecar 1.0.5 | 未找到可唯一對應的第一方公開專案 | 完整 image repository、digest、source URL |
| nftables-exporter 1.0.2 | 名稱可對到多個 repo；較知名的 [metal-stack/nftables-exporter tags](https://github.com/metal-stack/nftables-exporter/tags) 並沒有 1.0.2，不能硬配 | 完整 image repository、digest |
| nftables-ubuntu 1.0 | 看似內部 utility image，而不是 nftables upstream release；官方 nftables 專案由 [Netfilter](https://www.netfilter.org/projects/nftables/) 維護，但版本不吻合 | 完整 image repository、digest、用途 |
| OPA scorecard exporter 0.0.4 | Gatekeeper 官方 [repository](https://github.com/open-policy-agent/gatekeeper) 沒有這個元件/tag | 完整 image repository、source URL |
| Autoheal job/operator/webhook 2.2.0／2.1.0／1.1.0 | 三個名字與版本無法唯一映射到同一公開第一方專案 | 每個 workload 的完整 image repository、digest |
| Telegraf CoreDNS emergency chart 3.13.3 | 無法從名稱判斷 chart repository；不是 Telegraf app version | Helm repository URL、chart name、chart archive digest |
| dex-k8s-authenticator latest-customized-20250422 | 官方 [mintel/dex-k8s-authenticator tags](https://github.com/mintel/dex-k8s-authenticator/tags) 只到 v1.4.0，custom tag 無官方對應 | fork repository、commit 或 image digest |
| Ephemeral storage webhook 20250908-pod-level-log | 日期式 tag 無法唯一定位公開專案 | 完整 image repository、digest、source URL |
| Active IP uploader 1.2.1 | 名稱無法唯一定位公開專案 | 完整 image repository、digest、source URL |
| kubelet-stats-exporter 1.0.3-custom-v1 | custom tag 無法唯一定位 upstream | 完整 image repository、digest、fork commit |
| Kubernetes Event Exporter 1.7.0 | 官方 [resmoio/kubernetes-event-exporter](https://github.com/resmoio/kubernetes-event-exporter/tags) 只有 v1.7，沒有 v1.7.0；目前需求也沒有提供能證明它是 Bitnami 包裝、以及 Bitnami 1.7.0 對應 resmoio v1.7 的第一方 metadata，因此最終分類維持待確認、不列入抓取 | 完整 image repository 與 digest，或對應 Bitnami chart/container 的第一方 metadata |
| IPVS exporter 1.0.2 | 候選 [kwanhur/ipvs-exporter](https://github.com/kwanhur/ipvs-exporter/tags) 與 [f1shl3gs/ipvs_exporter](https://github.com/f1shl3gs/ipvs_exporter/tags) 都沒有可證實的 1.0.2 對應 | 完整 image repository、digest |
| libvirt exporter latest for Ubuntu 22.04 | latest 是 mutable tag，而且有多個同名 exporter；現有 libvirt 12.7 docs 不能代替 exporter 文件 | 完整 image repository、digest、實際版本 |

Telegraf 1.30.3.8 仍列為 base 版本推論；在收到 image repository 與 digest 前，
不應宣稱精確 image 與 upstream v1.30.3 完全一致。

## 取得與重建的固定方式

實際取得時先逐項把 tag peel 成 40 字 commit，再由固定 commit 的
docs/、Documentation/、website/、README 或 chart directory 取得內容；不要讓
manifest 直接依賴 mutable branch。只有沒有 release tag、但有 frozen version
directory 的網站 source（例如 cert-manager 1.14、Istio 1.24、OpenSearch 2.19、
Fluent Bit 3.2）才使用本筆記列出的固定 branch commit。

chart 文件與 app 文件是兩種用途：chart README 說明部署參數，app docs 說明產品
行為。兩者即使 metadata 可互相映射，也應在 metadata 中保留各自版本，不應把 chart
version 改寫成 app version。

## 實際交付對帳

使用者確認後的建置結果如下。頁數是新增 corpus Markdown 的實際檔案數，
不含已存在而略過的版本。

| 批次 | 新增 manifest | 新增頁數 |
| --- | ---: | ---: |
| CSI 與 sidecar 版本連續性 | 30 | 241 |
| 核心平台、網路與虛擬化 | 11 | 803 |
| 監控、Policy 與 Identity | 15 | 789 |
| Logging、Exporter 與 Helm Chart | 15 | 235 |
| Istio 1.24 | 1 | 385 |
| Ubuntu 22.04／24.04／26.04 與 Linux kernel 6.17 | 4 | 3,822 |
| OpenSearch／OpenSearch Dashboards 2.19 | 2 | 1,104 |
| **合計** | **78** | **7,379** |

其中 74 份 Git manifest 的 tag／branch 全部已解析為 40 字 immutable
commit，raw checkout、`git_meta.json`、corpus frontmatter 與頁數已對帳；4 份
HTML manifest 的 raw archive 與 corpus 也無缺頁。整體 corpus 共 35,291 頁、
300,450 個索引 chunks；完整建立後連續兩次增量建立都是 0 新增、0 修改、0 刪除，
SQLite `integrity_check` 回傳 `ok`。FTS5 查詢已分別命中 Istio 1.24、OpenSearch
2.19、CSI 與 Vault Secrets Operator 文件，表示 corpus 與索引已穩定對齊且可搜尋。
另對本批 78 份 manifest 連續兩次全量 normalize；7,379 頁依排序後的
repository-relative path、NUL 分隔字元與檔案 bytes 計算，組合 SHA-256 兩次皆為
`12220398a4cb1e26a8620c81049394ebbb7c3546d8ece1649423e79180f28dcc`，證實 Git
與 HTML 來源的輸出都可重現，沒有時間戳或排序漂移。

現有 corpus validator 另逐一檢查 72 份非 Jekyll Git manifest：66 份直接通過；
6 份非零結果是各批次來源筆記已逐項分類的上游格式或 Ceph 專用 heuristic
（Cilium、CoreDNS、Fluent Bit、KubeVirt、oauth2-proxy、Thanos），其 raw
source count、非空 source count、預期輸出與實際 page count 仍全部一致。OpenSearch
兩份 Jekyll corpus 使用專用的 route、Liquid residual 與 link marker 驗證，不套用
Ceph RST heuristic。

完整 staged corpus 執行 `git diff --cached --check` 會保留 **76** 個已分類的
source-fidelity findings：4 個是只有 frontmatter 的空 index 頁尾端空行，10 個是
kernel 上游 preformatted text 的尾端空白，52 個是 Prometheus Operator／Thanos
fenced console 或 JSON 範例中的 space-before-tab，另 10 個是 kernel 圖示、Git
conflict 教學與 literal block 中外觀類似 conflict marker 的原文。這些都不是本
repository 的未解 merge conflict；為了不竄改上游指令輸出、圖示與教學範例而原樣
保留。建置程式、manifests、研究紀錄，以及 Istio／OpenSearch／Dashboards corpus
路徑的 path-scoped diff check 均為 0 findings。
