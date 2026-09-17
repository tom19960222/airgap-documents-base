# 2026-09-17 Logging、Exporter 與 Helm Chart 官方文件來源記錄

## 結論

本批新增 15 份 immutable Git source manifest，來源都是需求指定的官方
repository 與 40 字 commit。每份都實際執行 `builder/git_source.py all`；共產生
235 頁 normalized Markdown。`raw/` 是建置端 checkout，不納入 repository；可提交的
內容是 manifests、`corpus/` 與本筆記。

Fluent Bit 的 app `3.2.10` 對應 docs line `3.2`；Fluentd 的 downstream image 或
package suffix 不改寫 upstream 文件版本。Helm chart version 與 Chart.yaml 的
`appVersion` 是兩個不同欄位；環境若指定另一個 image version，保留為明確 override，
不把它改成 chart version，也不把 Chart.yaml 塞進本批 corpus。

## 官方來源、文件範圍與頁數

| 元件 | upstream tag／版本與 appVersion 邊界 | immutable commit | manifest `docs_paths`（正式 Markdown） | 頁數 |
| --- | --- | --- | --- | ---: |
| Fluent Bit docs | docs line `3.2`；對應 app `3.2.10` | [`36106a0740d3f62f05d0e9e69b2c0e21dfa9de21`](https://github.com/fluent/fluent-bit-docs/commit/36106a0740d3f62f05d0e9e69b2c0e21dfa9de21) | repository root 的 Markdown；排除 `.gitbook/`、`input/` placeholder 與 root `README.md`、`CONTRIBUTING.md`、`MAINTAINERS.md`、`SUMMARY.md` | 218 |
| Fluentd | upstream `1.18.0` source；downstream suffix 不等於 upstream docs version | [`46372ddd521870f6a203baefb5a598209486d0bc`](https://github.com/fluent/fluentd/commit/46372ddd521870f6a203baefb5a598209486d0bc) | `README.md`、`CONTRIBUTING.md`；固定 tree 沒有正式 `docs/` Markdown | 2 |
| x509-certificate-exporter | release／chart `3.18.1`；本批不另推導 appVersion | [`e2f8c4121eaa35800a0c3e96b86b404ebcc1eb96`](https://github.com/enix/x509-certificate-exporter/commit/e2f8c4121eaa35800a0c3e96b86b404ebcc1eb96) | `deploy/charts/x509-certificate-exporter/README.md` | 1 |
| frr-exporter | release `1.3.3` | [`9ee9720c0f5a3c9bf7a83003836ea423410d57e3`](https://github.com/tynany/frr_exporter/commit/9ee9720c0f5a3c9bf7a83003836ea423410d57e3) | `README.md` | 1 |
| blackbox-exporter | release `0.25.0` | [`ef3ff4fef195333fb8ee0039fb487b2f5007908f`](https://github.com/prometheus/blackbox_exporter/commit/ef3ff4fef195333fb8ee0039fb487b2f5007908f) | `README.md`、`CONFIGURATION.md` | 2 |
| smartctl-exporter | release `0.14.0` | [`ef5c03de02cb793e6a1540bef943fe6a167de635`](https://github.com/prometheus-community/smartctl_exporter/commit/ef5c03de02cb793e6a1540bef943fe6a167de635) | `README.md`、正式操作範例 `EXAMPLE.md`；不納入 changelog、testdata README | 2 |
| keepalived-exporter | release `1.3.2`；`linux-amd64` 是 artifact architecture，Ubuntu 22.04 是執行環境，兩者都不是 docs version | [`50b7c520504fd30b48496a2647fd0f41fbabe8a8`](https://github.com/mehdy/keepalived-exporter/commit/50b7c520504fd30b48496a2647fd0f41fbabe8a8) | `README.md` | 1 |
| kube-prometheus chart | chart `9.0.5`；Chart.yaml `appVersion: 0.73.2` | [`d502935e8ae025beb7690cc8d611f1e71972a594`](https://github.com/bitnami/charts/commit/d502935e8ae025beb7690cc8d611f1e71972a594) | `bitnami/kube-prometheus/README.md` | 1 |
| prometheus-pushgateway chart | chart `2.4.1`；Chart.yaml default `appVersion: v1.6.1`；環境 app `1.6.2` 是 image override | [`1c1f688d57805389d051777bef8f55176494e09e`](https://github.com/prometheus-community/helm-charts/commit/1c1f688d57805389d051777bef8f55176494e09e) | `charts/prometheus-pushgateway/README.md` | 1 |
| prometheus-adapter chart | chart `2.17.0`；Chart.yaml `appVersion: v0.9.0` | [`843d2f3d302ca24d745abf539a86ec680ae4f8c0`](https://github.com/prometheus-community/helm-charts/commit/843d2f3d302ca24d745abf539a86ec680ae4f8c0) | `charts/prometheus-adapter/README.md` | 1 |
| oauth2-proxy chart | chart `6.16.1`；Chart.yaml `appVersion: 7.4.0` | [`2befa05adf3fc42ee9337beb35074c4637745cf7`](https://github.com/oauth2-proxy/manifests/commit/2befa05adf3fc42ee9337beb35074c4637745cf7) | `helm/oauth2-proxy/README.md` | 1 |
| dex chart | chart `0.23.0`；Chart.yaml `appVersion: 2.42.0` | [`65db60c3c27b2124db53792eeab80a574588b92c`](https://github.com/dexidp/helm-charts/commit/65db60c3c27b2124db53792eeab80a574588b92c) | `charts/dex/README.md` | 1 |
| fluent-bit chart | chart `0.48.10`；Chart.yaml `appVersion: 3.2.10` | [`3e258b4d615d2db88d5468870be6c027f13a79bc`](https://github.com/fluent/helm-charts/commit/3e258b4d615d2db88d5468870be6c027f13a79bc) | `charts/fluent-bit/README.md` | 1 |
| opensearch chart | chart `2.27.0`；Chart.yaml default `appVersion: 2.18.0`；環境 app `2.19.3` 是 image override | [`e43cf7dea1c01570971c70ff7d120b165bcfc28e`](https://github.com/opensearch-project/helm-charts/commit/e43cf7dea1c01570971c70ff7d120b165bcfc28e) | `charts/opensearch/README.md` | 1 |
| opensearch-dashboards chart | chart `2.25.0`；Chart.yaml default `appVersion: 2.18.0`；環境 app `2.19.1` 是 image override | [`e43cf7dea1c01570971c70ff7d120b165bcfc28e`](https://github.com/opensearch-project/helm-charts/commit/e43cf7dea1c01570971c70ff7d120b165bcfc28e) | `charts/opensearch-dashboards/README.md` | 1 |

Fluent Bit docs 使用 `docs_paths = ["."]` 搭配 exclude，讓 normalized output 保留
repository-relative 路徑；這避免 `administration/`、`pipeline/` 等不同 subtree 的
同名 Markdown 被扁平化後互相覆寫。Sparse checkout 使用 `/*`，因此官方 GitBook
圖片可供 source-relative link 解析，但 `.gitbook/` 本身不會成為 corpus page。

Chart 的 `Chart.yaml` 已依上述固定 commit 查證 chart version 與 `appVersion`，但
manifest 的 `docs_paths` 僅列正式 README，符合本批「每個 chart 只抓 README」的範圍。
README 所引用的 `values.yaml` 只放進 sparse source 以便改寫成 commit-pinned source
URL，不會額外產生 corpus page。

## Provenance 與可重建流程

每頁 front matter 由 manifest 與 raw checkout metadata 產生，`source_url` 都是：

```text
https://github.com/<owner>/<repo>/blob/<指定40字commit>/<repository-relative-path>
```

本次 generic Git renderer 也將 manifest 的 `app_version` 保留為獨立 provenance
欄位：`corpus/cert-manager/1.14` 的 94 頁全部為 `1.14.7`，
`corpus/fluent-bit/3.2` 的 218 頁全部為 `3.2.10`。因此 frozen docs line
（1.14、3.2）與實際 app release 不會在離線搜尋時互相混淆。

所有 manifest 的 `repo_url` 都不含 `.git`。實際建置指令如下：

```shell
builder/.venv/bin/python builder/git_source.py all builder/manifests/<manifest>.toml
```

本批實際頁數為：

```text
fluent-bit/3.2                                  218
fluentd/1.18.0                                    2
x509-certificate-exporter/3.18.1                 1
frr-exporter/1.3.3                               1
blackbox-exporter/0.25.0                         2
smartctl-exporter/0.14.0                         2
keepalived-exporter/1.3.2                        1
kube-prometheus-chart/9.0.5                      1
prometheus-pushgateway-chart/2.4.1              1
prometheus-adapter-chart/2.17.0                 1
oauth2-proxy-chart/6.16.1                        1
dex-chart/0.23.0                                 1
fluent-bit-chart/0.48.10                         1
opensearch-chart/2.27.0                          1
opensearch-dashboards-chart/2.25.0              1
TOTAL                                           235
```

## 驗證結果與限制

### Inventory、collision 與 metadata

以最新 `builder/git_source.py` 對每個 manifest 重跑 discovery：每份
`discovered == unique corpus output == corpus page count`，15 份都沒有 basename
collision。各頁均有 `collection`、`version`、`title`、`source_url`、`fetched_at`
front matter；全量檢查通過 40 字小寫 hexadecimal commit source URL，沒有
`.git/blob/` URL。

### Template／shortcode

Fluent Bit docs line 的 upstream Markdown 在固定 snapshot 中有 532 個 GitBook
`{% ... %}` rendering tags，分布於 59 頁（其中 530 個是 paired tags，另有 2 個
self-closing `embed` token；類型為 `hint`、`tabs`、`tab`、`embed`）。加入 manifest-driven
`shortcode_profile = "gitbook"` 後，normalizer 會用 paired renderer 將 `hint
style="info"`／`warning` 轉成 Note／Warning、保留 tab 標題與 embed caption，並對
`content-ref`、`code`、`file`、`include`、`stepper`、`step`、`columns` 提供可搜尋的
Markdown 表示；fenced code（backtick／tilde fence，含 blockquote 與最多 3 個前置空白）內的
template literal 完全不動。離線重建前後的 GitBook template residual 為
`532 → 0`；找不到 paired close 的 `embed` 視為 self-closing，不會吞掉後續內容。
GitBook include 僅允許 repo `.gitbook/includes` 內的檔案，並拒絕 absolute／`..`
traversal、recursion 與深度超過 8。GitBook profile 不會處理 Hugo `{{< >}}`。

另外有少量合法範例中的 template-looking text：Fluent Bit Loki 範例含
`{{.log}}`，kube-prometheus chart README 含 Helm `{{ template ... }}`，oauth2-proxy
chart README 含 Helm／Go template 例子。x509、frr、blackbox、smartctl、keepalived
與其餘 chart README 沒有 shortcode 殘留。

### Offline／source-relative links

大部分 chart README 的 `values.yaml`、Fluentd 的 `SECURITY.md`／security audit PDF、
blackbox 的 `example.yml` 都因加入 sparse source 支援而改寫為同一 immutable commit
的 source URL，沒有 unresolved marker。GitHub 同 repo 的 `blob/main`、`tree/main`、
既有 `master` inline link，以及 CommonMark reference definition（含 no-space colon、
angle-bracket target、fragment 與 optional title）現在都固定到 manifest 的 40-hex
commit；relative definition、cross-repo／external definition 與 fenced definition
逐位元組保留。Fluent Bit 仍有 14 個
`unresolved-source-link` marker（10 頁），限制集中在：

- upstream 原始相對路徑本身不正確或指向未納入文件的 path，例如 `hot_reload.md`、
  `pipeline/filters.md` 與 `pipeline/outputs/`；
- GitBook 圖片檔名帶 escaped underscore，現有 resolver 未將 `\_` 還原成檔名；
- Markdown table／inline code 裡的 regex 括號被現有 link scanner 分類成 source target。

這些 marker 會明確保留 `unresolved-source-link` 分類，不偽造離線頁面；固定 commit、
front matter 與可重建性不受影響。

### Claude review 已核證的最小 tag／source 證據

- blackbox-exporter、smartctl-exporter、Fluentd 的 annotated release tag 都以
  `^{}` peeled ref 取 immutable commit；`fetched_at` 使用該 commit 的 commit date，
  不是 fetch 當下時間。
- x509-certificate-exporter 的 `v3.18.1` 解析到 `e2f8c4121eaa35800a0c3e96b86b404ebcc1eb96`；
  該 commit 的 `Chart.yaml` 仍是 `0.0.0` placeholder，本 collection 只納入 chart
  README，沒有把 placeholder 當成 release/app version。
- 兩份 OpenSearch chart（`opensearch`、`opensearch-dashboards`）的指定 tag 都指向
  `e43cf7dea1c01570971c70ff7d120b165bcfc28e`；各自的 `Chart.yaml` chart version 與
  `appVersion` 分開記錄。Dashboards README 的 `values.yaml` source link 即使上游
  path 誤指 `opensearch` chart，改寫後仍保留該上游 path，只固定 commit。
- Fluentd 固定 source 的 `docs/` 目錄僅有 PDF，故正式 corpus 範圍維持 `README.md`、
  `CONTRIBUTING.md`，沒有臆造 Markdown docs page。

`builder/validate_ceph_corpus.py` 可驗證 raw source count、page mapping、front matter、
source URL、table 與 link inventory；Fluent Bit 的上述檢查均通過，但該 validator
將兩個普通 Markdown 教學文字誤判為 residual RST named link：
`pipeline/inputs/windows-exporter-metrics.md` 的反引號文字後底線，以及
`pipeline/parsers/decoders.md` 的反引號文字中底線。它們不含 RST role、未指向離線
頁面，也不是 normalization 遺漏。

## 建置驗證

以下檢查已完成並通過：

```text
builder tests:      74 tests, OK
compileall:         builder runtime, OK
builder/research path-scoped git diff --check: OK
```

builder tests 同時覆蓋既有 collision、symlink、zero-page、Kubernetes、Istio 行為，
以及 GitBook fence／nested pair／include safety、unknown profile 與 GitHub link pin
回歸。完整 staged corpus 的 source-fidelity whitespace／literal marker findings
由主 audit 逐類記錄，不把 fenced console／JSON 原文改寫成較不忠實的內容。主整合
流程已完成 35,291 頁、300,450 個 chunks 的 full index build，並以
兩次 0 變更的 incremental build 驗證穩定性。

Fluent Bit Slack output 文件的上游範例使用完整 incoming-webhook URL 形狀，即使
token 只由 `0` 與 `X` 組成，GitHub Push Protection 仍會視為 secret。正規化器會把
三段 credential 改成明確且 URL-safe 的 `WORKSPACE_ID/CHANNEL_ID/REDACTED_TOKEN`
placeholder；endpoint
用途、設定鍵與固定來源 URL 均保留，但 corpus 不會攜帶可用 credential。此行為由
generic Git normalize regression test 覆蓋。
