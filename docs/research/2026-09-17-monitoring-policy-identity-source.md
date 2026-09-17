# 2026-09-17 監控、Policy 與 Identity 文件來源記錄

## 結論

本次新增 15 份官方 Git source corpus，所有 manifest 都固定到需求指定的 40 字
commit；builder 已逐份執行 `fetch + normalize`，不使用 mutable branch。文件範圍
只包含下表列出的官方 Markdown（builder 目前處理 `.md`、`.markdown` 與 `.rst`），
不把 repository 內的程式碼、binary 或未列入 `docs_paths` 的目錄帶入 corpus。

`version` 是供離線搜尋與 front matter 使用的 upstream 文件版本；container image
尾碼、Helm chart version、部署 label 與 app version 是不同命名空間，不能互相改寫。

## 固定來源、版本映射與頁數

| 元件 | app／文件版本與映射 | 官方 repository／release tag | 固定 commit | Manifest 文件範圍 | 頁數 |
| --- | --- | --- | --- | --- | ---: |
| Prometheus | app `2.51.2`；`debian-12-r0` 是 downstream image rebuild suffix | [`prometheus/prometheus` v2.51.2](https://github.com/prometheus/prometheus/tree/v2.51.2) | [`b4c0ab52c3e9b940ab803581ddae9b3d9a452337`](https://github.com/prometheus/prometheus/commit/b4c0ab52c3e9b940ab803581ddae9b3d9a452337) | `docs/`、`documentation/internal_architecture.md`、`README.md` | 30 |
| Prometheus Operator | app `0.73.2`；Bitnami kube-prometheus chart `9.0.5` 的 `appVersion` 對應 `0.73.2` | [`prometheus-operator/prometheus-operator` v0.73.2](https://github.com/prometheus-operator/prometheus-operator/tree/v0.73.2) | [`20beb0b00b0bb61840ec2461ace4f22e4037b474`](https://github.com/prometheus-operator/prometheus-operator/commit/20beb0b00b0bb61840ec2461ace4f22e4037b474) | `Documentation/`、`README.md` | 32 |
| Alertmanager | app `0.27.0`；`debian-12-r4` 是 downstream image rebuild suffix | [`prometheus/alertmanager` v0.27.0](https://github.com/prometheus/alertmanager/tree/v0.27.0) | [`0aa3c2aad14cff039931923ab16b26b7481783b5`](https://github.com/prometheus/alertmanager/commit/0aa3c2aad14cff039931923ab16b26b7481783b5) | `docs/`、`README.md` | 10 |
| node_exporter | app `1.7.0` | [`prometheus/node_exporter` v1.7.0](https://github.com/prometheus/node_exporter/tree/v1.7.0) | [`7333465abf9efba81876303bb57e6fadb946041b`](https://github.com/prometheus/node_exporter/commit/7333465abf9efba81876303bb57e6fadb946041b) | `README.md`、`docs/`、`CONTRIBUTING.md` | 5 |
| kube-state-metrics | app `2.12.0`；`debian-12-r2` 是 downstream image rebuild suffix | [`kubernetes/kube-state-metrics` v2.12.0](https://github.com/kubernetes/kube-state-metrics/tree/v2.12.0) | [`1e8b837eb1fa1cb2dc3c37821637334e2dd47488`](https://github.com/kubernetes/kube-state-metrics/commit/1e8b837eb1fa1cb2dc3c37821637334e2dd47488) | `docs/`、`README.md` | 41 |
| Thanos | app `0.37.1` | [`thanos-io/thanos` v0.37.1](https://github.com/thanos-io/thanos/tree/v0.37.1) | [`e0812e2f46f81af3324686d910d885d8f2751d46`](https://github.com/thanos-io/thanos/commit/e0812e2f46f81af3324686d910d885d8f2751d46) | `docs/`、`README.md` | 76 |
| Pushgateway | app `1.6.2`；chart `2.4.1` 預設 `appVersion` 是 `v1.6.1`，環境若使用 `1.6.2` 是明確 image override | [`prometheus/pushgateway` v1.6.2](https://github.com/prometheus/pushgateway/tree/v1.6.2) | [`dd0ca68e2cf68ba061ed9e73b19e1928a4f6338f`](https://github.com/prometheus/pushgateway/commit/dd0ca68e2cf68ba061ed9e73b19e1928a4f6338f) | `README.md`、`CONTRIBUTING.md` | 2 |
| Prometheus Adapter | app `0.9.0`；chart `2.17.0` 的 `appVersion` 為 `v0.9.0` | [`kubernetes-sigs/prometheus-adapter` v0.9.0](https://github.com/kubernetes-sigs/prometheus-adapter/tree/v0.9.0) | [`0a9c781e5c69b1777b922ede2f9df100ef90703c`](https://github.com/kubernetes-sigs/prometheus-adapter/commit/0a9c781e5c69b1777b922ede2f9df100ef90703c) | `docs/`、`README.md` | 5 |
| Node Problem Detector | app `0.8.18`；部署 label `v20260728` 是 downstream label，沒有用它替代 upstream release | [`kubernetes/node-problem-detector` v0.8.18](https://github.com/kubernetes/node-problem-detector/tree/v0.8.18) | [`775a138ad6cff2bef32d7a6facfdcfed4437d768`](https://github.com/kubernetes/node-problem-detector/commit/775a138ad6cff2bef32d7a6facfdcfed4437d768) | `docs/`、`README.md` | 3 |
| OPA Gatekeeper | app `3.18.2` | [`open-policy-agent/gatekeeper` v3.18.2](https://github.com/open-policy-agent/gatekeeper/tree/v3.18.2) | [`35f8bb97ec9badb12266e2e3f74465ef718c6237`](https://github.com/open-policy-agent/gatekeeper/commit/35f8bb97ec9badb12266e2e3f74465ef718c6237) | `website/docs/`、`README.md` | 35 |
| oauth2-proxy | app `7.4.0`；chart `6.16.1` 的 `appVersion` 為 `7.4.0` | [`oauth2-proxy/oauth2-proxy` v7.4.0](https://github.com/oauth2-proxy/oauth2-proxy/tree/v7.4.0) | [`aafa96655048bc1ed26487e92410f5fe64968fa2`](https://github.com/oauth2-proxy/oauth2-proxy/commit/aafa96655048bc1ed26487e92410f5fe64968fa2) | `docs/versioned_docs/version-7.4.x/`、`README.md` | 10 |
| Dex | app `2.42.0`；chart `0.23.0` 的 `appVersion` 為 `2.42.0` | [`dexidp/dex` v2.42.0](https://github.com/dexidp/dex/tree/v2.42.0) | [`7d1a7473c8a07e22ee97925cc10236c70e5ecf34`](https://github.com/dexidp/dex/commit/7d1a7473c8a07e22ee97925cc10236c70e5ecf34) | `README.md`、實際存在的 `docs/`；`Documentation/` 不存在 | 5 |
| Vault Secrets Operator | app `1.26.0`；正確專案是 `ricoberger`；同一 immutable commit 的 `Chart.yaml` 證實 chart `2.7.0`、`appVersion` 為 `v1.26.0` | [`ricoberger/vault-secrets-operator` v1.26.0](https://github.com/ricoberger/vault-secrets-operator/tree/v1.26.0) | [`0522e930be76ea763c6611a130d44b7ef59182b0`](https://github.com/ricoberger/vault-secrets-operator/commit/0522e930be76ea763c6611a130d44b7ef59182b0) | `README.md`、root README 連結的 `charts/README.md` | 2 |
| cert-manager | 文件線 `1.14`；release app `v1.14.7` 的版本證據 commit 為 [`636559655f1efa8eff236981edb950b4ef40b253`](https://github.com/cert-manager/cert-manager/commit/636559655f1efa8eff236981edb950b4ef40b253) | 官方 website frozen `v1.14-docs` 內容 | [`d2e1bdfbbe23fcf24dcb68ab54353a65a4131c20`](https://github.com/cert-manager/website/commit/d2e1bdfbbe23fcf24dcb68ab54353a65a4131c20) | `content/v1.14-docs/` | 94 |
| Telegraf | app `1.30.3`；`telegraf-1.30.3.8` 的 `.8` 是 downstream image/package suffix，不能另建 upstream 版本 | [`influxdata/telegraf` v1.30.3](https://github.com/influxdata/telegraf/tree/v1.30.3) | [`fd4af886672c8256ff17c888935a801d941894c4`](https://github.com/influxdata/telegraf/commit/fd4af886672c8256ff17c888935a801d941894c4) | `docs/`、`plugins/` 下 Markdown、`README.md` | 439 |

目前這 15 份 manifest 對應的 corpus 目錄實際有 **789 頁**。頁數是各 manifest 最終寫入的 Markdown 檔案數，不是
上游網站頁數；同一 repository 未列入的 source subtree、程式碼與非 Markdown 檔案不在
本次 corpus。修正前共用 builder 以每個 `docs_paths` 項目的 basename 計算輸出路徑，

造成六份 manifest 的 README 碰撞，執行輸出計數各少 1（etcd 15→14、KubeVirt 56→55、
KSM 41→40、Thanos 76→75、Dex 5→4、Telegraf 439→438）。目前已改為只對真正碰撞的
來源使用 repo-relative path；六份重建後的 discovered count 均等於 corpus 實際 Markdown
count，兩份 README 的 source_url 與不同內容也都保留，沒有 stale page。

## Frontmatter-only section-index allowlist（4 頁）

本文件所涵蓋的監控元件中，有 4 頁是上游 section index 的
frontmatter-only source；它們是刻意保留的 page/provenance，不是遺漏正文：

| collection/version | 精確的 corpus-relative allowlist | 頁數 |
| --- | --- | ---: |
| `alertmanager/0.27.0` | `index.md` | 1 |
| `prometheus/2.51.2` | `command-line/index.md`、`configuration/index.md`、`querying/index.md` | 3 |

`runtime/build_index.py` 會將這 4 頁的空 body 轉成 **0 chunks**，但 page
與其 frontmatter provenance 仍保留在 corpus。因此 runtime chunk count 為 0
不代表 page 或來源遺失。本次不刪除頁面、不捏造正文，也不擴大
改動空 body 邏輯。Istio 的 45 頁對應清單另記錄在 Istio 來源研究。

## Telegraf 的 Markdown 範圍

Telegraf 的需求同時指定 `docs/`、`plugins/` 與根目錄 `README.md`，並要求保留 plugin
README、避免程式碼。現有 builder 的 discovery 只接受 `.md`、`.markdown`、`.rst`，因此
這份 manifest 的 `docs_paths`／`sparse_paths` 已把來源樹限制在上述三個位置，實際產出
439 頁且未將 Go、TOML、YAML 或其他程式碼檔寫入 corpus。若後續共用 builder 新增
`include_globs` schema，應將等價的 `**/*.md`、`**/*.markdown` 限制補入 manifest；在
目前 builder 版本中沒有擅自加入未知欄位，避免 `Manifest(**data)` 解析失敗。

## 版本與文件邊界

1. Prometheus、Alertmanager、kube-state-metrics 等 image 的 `debian-12-rN`，以及
   Telegraf 的 `.8`，是 downstream rebuild／package suffix，不是另一個 upstream
   文件版本。
2. Helm chart version 與 app version 分開記錄。Pushgateway chart `2.4.1` 的預設
   appVersion 與環境 app `1.6.2` 不同時，不把 chart 版本改成 app 版本。
3. Prometheus Adapter 的 `0.9.0` 是 chart `2.17.0` 的 `appVersion` 對應；本 corpus
   仍取 app repository 的固定 commit。Node Problem Detector 的 `v20260728` 只當
   downstream deployment label，文件綁 upstream `v0.8.18`。
4. Dex manifest 的 `Documentation/` 在固定 commit 不存在；builder 實際警告後依需求
   採用存在的 `docs/` 與根目錄 `README.md`。Vault Secrets Operator 明確採用
   `ricoberger/vault-secrets-operator`，不是 HashiCorp 的另一個 VSO 專案；固定 commit
   下 root `README.md` 實際連到 `charts/README.md`，故兩頁一併納入，並由同一 commit
   的 `charts/vault-secrets-operator/Chart.yaml` 證實 chart `2.7.0` 與 `appVersion: v1.26.0`。
5. cert-manager website 沒有把網站 frozen `v1.14-docs` 內容拆成對應 `v1.14.7` 的
   獨立 website tag；因此 manifest version 是文件線 `1.14`，另以
   `cert-manager/cert-manager` 的 v1.14.7 commit 作 release 證據。

## 驗證結果與已知偏差

每份 corpus 都以現有 `builder/validate_ceph_corpus.py` 指定 manifest、corpus 與 raw
checkout 執行；其名稱雖含 `ceph`，但實際檢查的是通用 front matter、固定 commit、
來源頁數、Markdown link、table 與 RST 殘留。Prometheus、Prometheus Operator、
Alertmanager、node-exporter、Pushgateway、Prometheus Adapter、Node Problem Detector、
Gatekeeper、Dex、Vault Secrets Operator（2 頁）、cert-manager、Telegraf 通過；本次六份 collision
修正後的 output path 也都唯一，raw source count 不再因 README basename collision 而
少頁。Thanos 與 oauth2-proxy 的既有 RST residual 維持記錄如下，未在本次擴張修復。

Thanos 與 oauth2-proxy 各有 1 個 validator residual RST named-link 分類，位置如下；
這些是上游 Markdown／HTML comment 中的教學連結，不是本次抓取的 mutable source URL：

- `corpus/thanos/0.37.1/components/query.md:196`（validator body line；來源檔實際行約
  200）：HTML comment 內的
  `PartialResponseStrategy enum here` link。
- `corpus/oauth2-proxy/7.4.0/configuration/overview.md:88`：validator 報告的
  named-link 分類落在 OAuth client-secret 表格列，該列是普通 Markdown table 內容。

針對 cert-manager、Gatekeeper、oauth2-proxy corpus 的 template／shortcode 掃描結果：
`{{<`、`{{%`、`{%`、`{::` 四種模式在三份 corpus 均為 **0 個檔案、0 個命中**，不需
為這三份 corpus 修改共用 builder。全 15 份 corpus 的額外掃描只看到 Prometheus
Operator 的 Hugo `{{< ... >}}`（6 個檔案）與 Vault Secrets Operator README 對
`{% ... %}` Go template delimiter 的說明／範例（1 個檔案）；它們是官方內容，不是
cert-manager、Gatekeeper 或 oauth2-proxy 的轉換殘留。

## 重建指令

```shell
# 建置端：每份 manifest 都已實際執行過；離線重建可分別執行 all
builder/.venv/bin/python builder/git_source.py all builder/manifests/prometheus-2.51.2.toml

# Air-gap 端完整重建；後兩次增量建置應為 0 變更
python3 runtime/build_index.py --full
python3 runtime/build_index.py
python3 runtime/build_index.py
```

raw checkout 只存在建置端；Git 應提交 manifest、`corpus/<collection>/<version>/` 與本
研究筆記，不提交 `raw/`。
