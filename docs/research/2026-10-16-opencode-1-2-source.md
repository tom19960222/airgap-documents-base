# OpenCode 1.19.2、2.0.30 官方文件來源

查核時間：2026-10-16 16:56–17:00（Asia/Taipei；08:56–09:00 UTC）。

## 版本與不可變來源

截至上述查核時間，1.x 最新正式版本為 **1.19.2**，2.x 最新正式版本為
**2.0.30**。兩個系列使用不同 npm package；不能只看 GitHub 的 Latest 標籤，
也不能用舊的 `@opencode-ai/cli` beta 管道代表目前 2.x。

| 系列 | 官方發布管道 | 最新版本與發布時間（UTC） | 文件固定 commit |
| --- | --- | --- | --- |
| 1.x | [`opencode-ai` npm registry](https://registry.npmjs.org/opencode-ai)、[GitHub release](https://github.com/anomalyco/opencode/releases/tag/v1.19.2) | `1.19.2`；GitHub release `2026-10-16T02:30:38Z`，`prerelease=false` | [`7901b7d325c34852caa84fc2c325f3a08dd7a473`](https://github.com/anomalyco/opencode/commit/7901b7d325c34852caa84fc2c325f3a08dd7a473) |
| 2.x | [`@opencode/cli` npm registry](https://registry.npmjs.org/@opencode%2fcli) | `2.0.30`；npm `2026-10-15T19:46:59.090Z`，`dist-tags.latest=2.0.30` | [`f16ef9ad8878279ea2be3cfab7baeed97aef61aa`](https://github.com/anomalyco/opencode/commit/f16ef9ad8878279ea2be3cfab7baeed97aef61aa) |

1.x 由 npm `dist-tags.latest=1.19.2`、[GitHub latest release API](https://api.github.com/repos/anomalyco/opencode/releases/latest)
與[官方 changelog](https://dev.opencode.ai/changelog)交叉核對。changelog 的
2026-10-16 條目說明 1.x 只追蹤 `opencode-ai` 的最新版，升級到 2.x 必須另外選擇。
這也說明為何 GitHub latest release 仍指向 1.x。

2.x 由官方 npm `latest` 與所有 [`v2.*` Git tag refs](https://api.github.com/repos/anomalyco/opencode/git/matching-refs/tags/v2.)
交叉核對；以三段數字版本排序後，最大正式版本為 `v2.0.30`，排除 `dev`、
`beta` 與 `0.0.0-*`。官方 [2.x 安裝文件](https://opencode.ai/v2/docs/)及其
[固定版原始碼](https://github.com/anomalyco/opencode/blob/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/services/www/src/docs/content/index.mdx)
均指定 `npm install -g @opencode/cli`。查核時，
[`@opencode-ai/cli` registry](https://registry.npmjs.org/@opencode-ai%2fcli) 的
`latest`、`next` 都仍是 `0.0.0-beta-17823`，因此不採用這個舊 scope。

查核時 [2.0.30 GitHub release API](https://api.github.com/repos/anomalyco/opencode/releases/tags/v2.0.30)
回傳 HTTP 404；不能將它寫成已確認的 GitHub non-prerelease release。此處
「正式版本」的證據是官方 npm `latest` 發布與相同數字 Git tag，而非缺少的
GitHub Release 物件。

兩個 tag 都是 lightweight tag，`git ls-remote` 未出現額外 `^{}` ref：

```text
git ls-remote --tags https://github.com/anomalyco/opencode.git \
  'refs/tags/v1.19.2*' 'refs/tags/v2.0.30*'

7901b7d325c34852caa84fc2c325f3a08dd7a473  refs/tags/v1.19.2
f16ef9ad8878279ea2be3cfab7baeed97aef61aa  refs/tags/v2.0.30
```

1.x release metadata 的 `target_commitish` 是
`3be039593a9a2cbe44f9578e37ac2bd789768262`，與 tag 指向不同；本次文件使用
Git tag 實際指向的 commit。兩版 commit 的 committer date 分別為
`2026-10-16T02:30:23Z`、`2026-10-15T19:48:22Z`。

## 文件範圍與語言

| 版本 | 正式文件原始碼 | 本次英文來源範圍 | 格式 |
| --- | --- | --- | --- |
| 1.19.2 | [`packages/web/src/content/docs/`](https://github.com/anomalyco/opencode/tree/7901b7d325c34852caa84fc2c325f3a08dd7a473/packages/web/src/content/docs) | 根目錄 36 頁 | MDX |
| 2.0.30 | [`services/www/src/docs/content/`](https://github.com/anomalyco/opencode/tree/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/services/www/src/docs/content) 與 `services/www/openapi.json` | 61 MDX：根目錄 24、CLI 10、Build 12、Console 15；另加 1 頁 API reference，共 62 頁 | MDX、OpenAPI JSON |

1.x 文件樹共 614 個 MDX：36 個英文根頁，另有 17 個 locale 子目錄，各 34 頁；
包括 `zh-tw`。本次取英文來源，保留英文原文，未自行翻譯。`packages/docs/`
是另一套文件框架範例，不屬於此產品文件集，因此排除。

2.x 正式文件根目錄由其
[`content.config.ts`](https://github.com/anomalyco/opencode/blob/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/services/www/src/content.config.ts)
的 `base: "./src/docs/content"`、`pattern: "**/*.{md,mdx}"` 確認；導覽與章節
由 [`navigation.ts`](https://github.com/anomalyco/opencode/blob/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/services/www/src/docs/lib/navigation.ts)
確認，全部 61 頁均為英文。網站
[`astro.config.ts`](https://github.com/anomalyco/opencode/blob/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/services/www/astro.config.ts)
設定 `/v2/` base。此版 repository 同時殘留舊 `packages/web/src/content/docs/`
樹（560 個 MDX），不可當作 2.x 正式文件匯入。

兩版文件應分別放入 `corpus/opencode/1.19.2/`、`corpus/opencode/2.0.30/`；
manifest 與每頁 `source_url` 固定至上述 40 字 commit，避免未來 branch、tag
或網站內容變動改寫來源。圖片與 UI 元件原始碼不直接當作 prose 頁；MDX
內的實際說明、tab 內容、安裝指令與程式碼範例仍需在轉成 Markdown 時保留。

## 2.x HTTP API 的獨立來源

2.x 導覽的 HTTP API 專區並非第 62 個 MDX。
[`api/index.astro`](https://github.com/anomalyco/opencode/blob/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/services/www/src/pages/docs/api/index.astro)
載入 [`OpenApiReference.astro`](https://github.com/anomalyco/opencode/blob/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/services/www/src/docs/components/OpenApiReference.astro)，
再由 [`services/www/openapi.json`](https://github.com/anomalyco/opencode/blob/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/services/www/openapi.json)
呈現 operation、parameters、request body、responses 與 component schemas。
本次在 61 個 MDX 之外，另外將固定 commit 的 JSON 正規化成 `api.md`，
所以 2.0.30 的 corpus 合計為 62 頁。API 頁依 operation 與 schema 分 heading，
保留完整 JSON 節點，供離線搜尋依 heading 分塊。

其 [`generate-openapi.ts`](https://github.com/anomalyco/opencode/blob/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/services/www/script/generate-openapi.ts)
會將 [`packages/protocol/openapi.json`](https://github.com/anomalyco/opencode/blob/f16ef9ad8878279ea2be3cfab7baeed97aef61aa/packages/protocol/openapi.json)
複製到 `services/www/openapi.json`、`services/www/public/openapi.json`。
在固定 commit 中，三份檔案逐位元組相同：

```text
格式：OpenAPI 3.1.0
大小：578272 bytes
SHA-256：3fcd666b597b746bad26f56a92fe782cc86338a0b4498f43b435a2f97e4fa05a
paths：118
operations：142（GET 66、POST 51、DELETE 15、PATCH 5、PUT 5）
component schemas：285
tags：30
```

schema 的 `info.version=0.0.1` 是 API schema 自身的版本；匯入文件的產品
版本仍應標示 `2.0.30`。`info.description` 也明示這是實驗性的部分 instance
routes，因此不能把此 schema 描述成所有內部 API 的完整規格。

## 匯入與驗證結果

| 版本 | corpus 頁數 | 索引 chunks | 原始 fenced code blocks 全數保留 | Markdown table separator rows | corpus 內部檔案連結 |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1.19.2 | 36 | 567 | 617 | 85 | 109 |
| 2.0.30 | 62 | 1,221 | 891 | 125 | 273 |

兩份 manifest 都以實際 raw checkout 執行通用 validator，來源頁數與 corpus
頁數一致，metadata、固定 commit、檔案連結、RST 殘留檢查全部通過。
MDX 的 inline code 使用 Markdown 語意；validator 僅在此 profile 下先排除
inline literal，避免把 `<server>_<tool>` 或 ``_!`command`_`` 誤判成 RST reference。
新增回歸測試同時確認真正殘留的 RST include 仍會失敗。

轉換器保留所有 tabs，包括 CodeTabs 內額外的 9 組安裝指令，並展開 Callout、
Card、Go／Go Plus 表格與設定連結；不執行 JavaScript。所有 1,508 個原始
fenced code blocks 都已與 corpus 逐段比對，僅套用既有正規化的共同縮排、
行尾空白及連續空行規則。API 頁的 428 個 JSON blocks 依原始節點順序解碼後，
與完整來源 JSON 的 overview、path metadata、operations、components 相等。
285 個 schema anchors 與 operation anchors 均已保留，文件中的 64 個 API
fragment links 全部有對應 target。

Builder 測試 **94 個通過**，runtime 測試 **21 個通過**，Python compilation
與 `git diff --check` 通過。SQLite `PRAGMA integrity_check` 回傳 `ok`，FTS
`integrity-check` 通過；依版本篩選的 permissions、MCP、Plugin.define、
session.list、service account 五組搜尋與 `get_section` 都能取得內容。

同一份 raw checkout 重跑 normalize，兩次 corpus digest 一致。digest 依排序後
的版本目錄相對路徑、NUL separator、檔案內容依序輸入 SHA-256：

```text
1.19.2  5f27b5b934453d567b8ded38d3cc6af8bfb7383fd8cf363c450a7b24cc711922
2.0.30  e8a353a16b29100bc6904c78af5470c899ca04088d16d5a76893252ce64fa6e0
```

### 已知的上游 fragment 問題

以下四個 1.x 連結的目的檔案存在，但固定 commit 的原始 MDX 已經指向不存在
的 heading fragment。本次保留官方 fragment，沒有捏造段落或自行推測替代位置：

| 來源 corpus 頁 | 上游既有的 fragment target |
| --- | --- |
| `config.md` | `models.md#local` |
| `config.md` | `providers.md#authentication-precedence` |
| `models.md` | `providers.md#custom` |
| `mcp-servers.md` | `agents.md#tools` |

1.x 的 4 個圖片／asset 連結沿用 repo 的固定 commit 外部連結政策；圖片 binary
沒有額外包入 corpus。外部網站、下載檔與線上 Console 仍須連網，文件正文、
程式碼與本次 API schema 可離線搜尋。

## 重建與檢查

```bash
builder/.venv/bin/python builder/git_source.py all builder/manifests/opencode-1.19.2.toml
builder/.venv/bin/python builder/git_source.py all builder/manifests/opencode-2.0.30.toml
builder/.venv/bin/python builder/validate_ceph_corpus.py --manifest builder/manifests/opencode-1.19.2.toml --corpus-dir corpus/opencode/1.19.2 --raw-repo raw/opencode/1.19.2/repo
builder/.venv/bin/python builder/validate_ceph_corpus.py --manifest builder/manifests/opencode-2.0.30.toml --corpus-dir corpus/opencode/2.0.30 --raw-repo raw/opencode/2.0.30/repo
builder/.venv/bin/python -m unittest discover -s builder/tests -v
python3 -m unittest discover -s runtime/tests -v
python3 runtime/build_index.py --verify-content
python3 runtime/build_index.py
python3 runtime/build_index.py
```

最後兩次增量建置已確認 `added=0`、`modified=0`、`deleted=0`。
`raw/` 與 `index/` 都是建置端產物，不納入 Git。
