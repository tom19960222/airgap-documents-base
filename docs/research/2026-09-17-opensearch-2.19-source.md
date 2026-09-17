# OpenSearch 2.19／OpenSearch Dashboards 2.19 來源盤點

> 狀態：**已 fetch、已 normalize、已完成 renderer／corpus 與整體索引驗證**。本 note 同時記錄固定來源、manifest、Jekyll/Liquid inventory、normalize 對帳、限制與驗證結果。

## Immutable source、scope 與版本證據

本次來源是官方 [`documentation-website`](https://github.com/opensearch-project/documentation-website) repository，固定在 immutable commit [`cc01280fc1f773421cbcb409bdc8fd7beae2638e`](https://github.com/opensearch-project/documentation-website/commit/cc01280fc1f773421cbcb409bdc8fd7beae2638e)。raw checkout 已 fetch 至：

- `raw/opensearch/2.19/repo`
- `raw/opensearch-dashboards/2.19/repo`

兩個 checkout 的 `HEAD` 都驗證為上述 docs commit。raw checkout 是為 Jekyll 解析保留 shared inputs 的 sparse checkout；raw 是暫存來源，不屬於提交內容。

應用程式 tag 與 docs line 是兩種不同證據，不能混稱：

| 項目 | `git ls-remote` tag target | 證據與解讀 |
| --- | --- | --- |
| OpenSearch app `2.19.3` | `a90f864b8524bc75570a8461ccb569d2a4bfed42` | `https://github.com/opensearch-project/OpenSearch` 的 `refs/tags/2.19.3`；remote 沒有另外輸出的 peeled `^{}` line，因此這次看到的是 lightweight tag target，effective commit 同值。 |
| OpenSearch Dashboards app `2.19.1` | `782801008fa7d872292e48caca1aca74be5304a6` | `https://github.com/opensearch-project/OpenSearch-Dashboards` 的 `refs/tags/2.19.1`；同樣沒有 `^{}` line，故為 lightweight tag target，effective commit 同值。 |
| 共同 docs line | `cc01280fc1f773421cbcb409bdc8fd7beae2638e` | `documentation-website` 的完整固定 tree；是本次兩份 docs manifest 的 source commit，不是 app repository tag commit。 |

可重現的 tag 證據指令與結果：

```text
git ls-remote https://github.com/opensearch-project/OpenSearch.git \
  'refs/tags/2.19.3' 'refs/tags/2.19.3^{}'
a90f864b8524bc75570a8461ccb569d2a4bfed42  refs/tags/2.19.3

git ls-remote https://github.com/opensearch-project/OpenSearch-Dashboards.git \
  'refs/tags/2.19.1' 'refs/tags/2.19.1^{}'
782801008fa7d872292e48caca1aca74be5304a6  refs/tags/2.19.1
```

固定 docs tree 的 [`_config.yml`](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_config.yml) 仍寫 source-config：`opensearch_version: '2.19.6'`、`opensearch_dashboards_version: '2.19.6'`、`opensearch_major_minor_version: '2.19'`。這些值不是本次 app tag mapping；兩份 manifest 都以 allowlisted `site_overrides` 明確指定 `site.opensearch_version = 2.19.3` 與 `site.opensearch_dashboards_version = 2.19.1`。輸出 frontmatter 保留 source-config 值，並以 `app_version` metadata 分別記錄 OpenSearch `2.19.3`、Dashboards `2.19.1`，不可靜默把兩種證據混為一談。

chart 是另一個 corpus，不要用 chart 版本 override docs line：目前 repo 另有 `opensearch-chart-2.27.0.toml`（helm commit `e43cf7dea1c01570971c70ff7d120b165bcfc28e`）與 `opensearch-dashboards-chart-2.25.0.toml`，分別收錄 chart README；它們不代表本次 documentation-website 的 2.19 docs。

## Manifest 與 OpenSearch／Dashboards 切分決策

已新增：

- [`builder/manifests/opensearch-2.19.toml`](../../builder/manifests/opensearch-2.19.toml)：`collection = "opensearch"`、`version = "2.19"`，收錄共同 docs tree 的 OpenSearch product roots。
- [`builder/manifests/opensearch-dashboards-2.19.toml`](../../builder/manifests/opensearch-dashboards-2.19.toml)：`collection = "opensearch-dashboards"`、`version = "2.19"`，只收錄專用 `_dashboards` collection，並保留 shared Jekyll inputs。

`_dashboards` 是 `_config.yml` 明確宣告的專用 Jekyll collection；固定 tree 中共有 **54** 個 Markdown page，且 54 個都有 frontmatter。因此可安全、無重複地建立獨立 Dashboards manifest。OpenSearch manifest 的 26 個 product roots 共有 **1,050** 個 Markdown page，全部都有 frontmatter：

| OpenSearch `docs_paths` root | Markdown files |
| --- | ---: |
| `_about` | 3 |
| `_aggregations` | 45 |
| `_analyzers` | 123 |
| `_api-reference` | 124 |
| `_automating-configurations` | 16 |
| `_developer-documentation` | 3 |
| `_field-types` | 73 |
| `_getting-started` | 7 |
| `_im-plugin` | 23 |
| `_ingest-pipelines` | 47 |
| `_install-and-configure` | 41 |
| `_integrations` | 1 |
| `_ml-commons-plugin` | 89 |
| `_monitoring-your-cluster` | 11 |
| `_observing-your-data` | 43 |
| `_query-dsl` | 60 |
| `_reporting` | 9 |
| `_search-plugins` | 102 |
| `_security-analytics` | 45 |
| `_security` | 42 |
| `_tools` | 12 |
| `_troubleshoot` | 5 |
| `_tuning-your-cluster` | 30 |
| `_tutorials` | 41 |
| `_upgrade-to` | 5 |
| `_vector-search` | 50 |
| **合計** | **1,050** |

`_install-and-configure/install-dashboards/**` 仍屬於 `install-and-configure` product root，所以留在 OpenSearch manifest；它是安裝指南的 source collection 邊界，不與 `_dashboards` page 重複。未納入本次 OpenSearch manifest 的 `_clients`、`_benchmark`、`_data-prepper`、`_migration-assistant` 是固定 tree 中可獨立分離的其他產品 roots，應由各自 corpus/manifest 處理。

`_upgrade-to` 雖未出現在 `_config.yml` 的 collections 宣告中，但有 5 個真實、具 frontmatter 的 product pages，且 canonical permalink 在 `/migrate-or-upgrade/`；為避免 source loss，manifest 先保留，profile 應以 permalink registry 處理，而非依 collection 宣告盲目丟棄。

### Raw sparse checkout 的 Jekyll support inventory

兩份 raw checkout 都保留 `_data`（6 files）、`_includes`（16 HTML）、`_layouts`（3）、`_plugins`（3）、`Gemfile`、`spec-insert`（35）、`assets`（157）與 `images`（612），以及各自的 docs roots。OpenSearch checkout 的相關 raw file count 是 1,917；Dashboards checkout 是 921。這些是 Jekyll input evidence，不是將 support code 當成 corpus page。

固定 tree root 中另有 `_benchmark`、`_clients`、`_data-prepper`、`_migration-assistant`、`_sass`、`release-notes` 等目錄，以及 root `index.md`、`404.md`、`search.md` 等 operational/theme pages。`_config.yml` 明確 exclude `release-notes`、templates、Gemfile、spec-insert 等；本次 product docs manifest 不收 blog/news/release-note、theme page 或非產品文件。若未來要收 release history，應另外定義 corpus，不可混進 2.19 product docs。

## Frontmatter、permalink、canonical 與 redirect

固定 docs source 使用 Jekyll frontmatter 與 `permalink: /:path/`，collection pages 再依 `_config.yml` 的 collection permalink `/:collection/:path/` 產生 URL。所有 1,050 個 OpenSearch pages 與 54 個 Dashboards pages 都有 `canonical_url` key；OpenSearch 有 1,038 個 unique canonical values、Dashboards 有 53 個 unique values。

- OpenSearch 有 27 個明確 `permalink` keys；Dashboards 只有 `_dashboards/index.md` 的 1 個，值為 `/dashboards/`。其他 page 應依 collection root、相對 source path 與 `index.md` collapse 規則推導。
- OpenSearch 的精確小寫 `redirect_from:` 出現 540 次、涵蓋 534 files；另有 1 個大小寫異常 `Redirect_from:`，位於 `_search-plugins/sql/sql/aggregations.md`。大小寫不敏感總數為 541。
- Dashboards 的小寫 `redirect_from:` 有 29 次、涵蓋 29 files。
- YAML 解析後 OpenSearch redirect aliases 共 876 entries、870 unique；有 6 個重複 alias。Dashboards 共 47 entries、46 unique，`/dashboards/run-queries/` 重複一次。profile 應合併大小寫變體、deduplicate alias，但保留 source provenance；product docs 沒有可用的 `redirect_to`。
- 代表性 duplicate alias（OpenSearch）包括 `/upgrade-opensearch/appendix/rolling-upgrade-lab/`、`/search-plugins/search-relevance/`、`/observability-plugin/ppl/`、`/search-plugins/ppl/commands/`、`/search-plugins/sql/aggregations/`、`/tutorials/ai-search-flows/building-flows/`。

目前 generic source-path discovery 若只把 collection root 剝掉，OpenSearch 會出現 collision：`index.md` 26 組、`api/index.md` 3 組、`security.md` 3 組、`settings.md` 2 組，共 30 個 duplicate output paths。這些是檔名推導的 collision，不是 page route；Jekyll profile 以 `permalink` 建立真實 route，再決定 corpus path。此次實測兩份 manifest 的 permalink route 都沒有 collision（各 0 組）；若未來真 permalink collision，仍固定輸出至 `__source__/<repository-relative-path>`，不以 deterministic suffix 假裝成 public URL。

## Liquid／Jekyll inventory

以下統計是在 product Markdown source（OpenSearch 的 1,050 files、Dashboards 的 54 files）逐行掃描 `{% ... %}` block tags 與 `{{ ... }}` output expressions 的 raw token 結果；shared `_includes` 另列，避免把 layout/include machinery 誤算成 page body。

| scope | block-tag occurrences | output-expression occurrences | combined raw Liquid tokens |
| --- | ---: | ---: | ---: |
| OpenSearch product pages | 3,715 | 7,448 | 11,163 |
| OpenSearch Dashboards pages | 114 | 834 | 948 |

### OpenSearch product pages

`{% ... %}` block tag totals：

| tag | count | files | 說明 |
| --- | ---: | ---: | --- |
| `include` | 3,475 | 715 | body-direct include targets 見下表 |
| `raw` | 104 | 20 | 104 pairs 的 opening tags |
| `endraw` | 104 | 20 | `raw` pairs 的 closing tags |
| `comment` | 13 | 13 | 13 pairs |
| `endcomment` | 13 | 13 | 13 pairs |
| `assign` | 6 | 3 | page-local variables |

沒有在 product page body 中發現 `link`、`highlight`、`if`、`for`、`capture`、`unless`、`case` 等 block tags；profile 仍應把它們列入 residual detector，防止日後來源變更或 include 展開後漏出。`{{ ... }}` 的 7,448 個 expressions 出現在 702 files，最主要是：

- `site.url` 3,472、`site.baseurl` 3,472；
- `site.opensearch_version` 232 個 direct expressions，另有 `site.opensearch_version | split: "." | first` 4 個，合計涉及 236 occurrences；
- `site.opensearch_major_minor_version` 23、`site.opensearch_dashboards_version` 2、`site.lucene_version` 1；
- product page body 沒有 `{{ page.* }}` output expression；`page.*` 主要透過 include argument 傳給 shared include。

Body include target：

| include | count | files | arguments / 用途 |
| --- | ---: | ---: | --- |
| `copy-curl.html` | 2,966 | 652 | 無 page variable，主要包住 copyable command |
| `copy.html` | 467 | 79 | 無 page variable |
| `cards.html` | 37 | 21 | `cards=page.*`，傳入 page frontmatter data |
| `list.html` | 4 | 3 | `list_items=page.steps/pre_items/auto_items/items` |
| `youtube-player.html` | 1 | 1 | `id='oX0HMAztP8E'` |
| **合計** | **3,475** | — | — |

`cards=page.*` 共 37 次，實際 key 包括 `getting_started`、`why_use`、`features`、`models`、`oa-toolkit`、`algorithms`、`more_cards`、`local_model`、`external_model`、`gpu`、`keyword`、`vector`、`ai`、`flows`、`chatbots`、`model_controls`、`rag`、`conversational_search`、`reranking`、`vector_search_101`、`semantic_search`、`vector_operations`、`search_method_cards`、`quickstart_cards`、`storage_cards`、`outside_cards`、`inside_cards`；另有 `documentation_link=true` 1 次。這代表 frontmatter page data 是 renderer input，不是可由 body text 猜出的值。

### Dashboards pages

Dashboards body 有 112 個 `include`（`copy-curl.html` 73、`copy.html` 39，分別在 16、11 files），以及 2 個 comment tags（`comment`／`endcomment` 各 1）。沒有 `raw`、`link`、`highlight` 或 conditional block tags。834 個 output expressions 全部是 `site.url` 417 與 `site.baseurl` 417；沒有 filters、`page.*` output 或 include arguments。

### Shared `_includes` closure

16 個 shared include templates 本身共有 484 個 block tags、95 個 output expressions。類型與數量包括：`for/endfor` 17/17、`if/endif` 77/77、`else` 27、`assign` 86、`comment/endcomment` 9/9、`unless/endunless` 7/7、`elsif` 3、`case/when/endcase` 2/74/2、`include` 17、`capture/endcapture` 24/24、`continue` 4、`last_modified_at` 1。include filters：`split:` 5、`join:` 5、`markdownify` 3、`absolute_url` 3、`replace:` 2、`relative_url` 1、`default:` 1、`first` 1、`strip_html` 1、`shift` 1。

三個 `_layouts`（`default.html`、`home.html`、`search_layout.html`）另有 118 個 block tags 與 57 個 output expressions：`include` 16、`if/endif` 34/34、`else` 7、`assign` 14、`elsif` 5、`for/endfor` 2/2、`unless/endunless` 1/1、`capture/endcapture` 1/1；layout filters 為 `relative_url` 10、`default` 3、`absolute_url` 1、`date` 1。三個 `_plugins`、`_config.yml` 與 `_data` 檔案沒有額外 Liquid token。這些 layout counts 是 Jekyll render machinery，不應加進 page-body residual page count，但 renderer 若要模擬完整 HTML layout，必須另有 scope 與 plugin policy。

`last_modified_at` 出現在 [`_includes/head_custom.html`](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_includes/head_custom.html) 的 HTML comment，由 Gemfile/Jekyll plugin 提供；它不在 page body。Body-direct includes 的 transitive closure 目前實際只需 `copy-curl.html`、`copy.html`、`cards.html`、`list.html`、`youtube-player.html`，這五個 include 沒有再引用其他 include；`_includes/redesign_buttons.html` 等是 layout/include machinery，不能誤當作每頁正文。

代表性 immutable source samples：

- [`_about/index.md`](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_about/index.md)：comment、`site.opensearch_major_minor_version`、`cards=page.getting_started`。
- [`_install-and-configure/install-opensearch/rpm.md`](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/install-opensearch/rpm.md)：`assign version_parts` 與 `major_version_mask`。
- [`_install-and-configure/install-opensearch/docker.md`](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_install-and-configure/install-opensearch/docker.md)：fenced command 中的 `site.opensearch_version | split: "." | first`。
- [`_api-reference/render-template.md`](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/render-template.md)：`{% raw %}{{play_name}}{% endraw %}` literal template。

## Fenced code、raw literals 與 Jekyll comments

source 內同時有「應由 Jekyll render 的 site variable」與「文件範例中的 literal template」，後者不可被誤處理。OpenSearch product pages 的 fence scan 找到 878 files、6,531 fence events；41 files 在 fence state 內有 366 個 `{{...}}` tokens。`raw/endraw` 共 104 pairs，其中 33 pairs 在 fence 外、71 pairs 在 fence 內（這是 conservative line scanner 結果；profile 應以 Markdown parser 的 fence/indentation semantics 為準）。常見 literal 包括 `{{play_name}}`、`{{#var}}`、`{{ctx.index}}`、`{{period_end}}`、`{{range .NetworkSettings.Networks}}` 與 `{{{field-name}}}`；這些必須保持原樣。`{% raw %}` wrapper 是明確的 protection boundary。

同一 conservative scanner 發現 5 個 fence 狀態異常／需 parser 驗證的 page：

1. `_aggregations/metric/percentile-ranks.md`（line 55 開 fence、未見 close）。
2. `_api-reference/cluster-api/cluster-awareness.md`（line 110 開 fence、`Next steps` 前未見 close；其後 line 125–126 的 site links 是 prose，不能因 scanner 狀態而跳過）。
3. `_install-and-configure/install-dashboards/index.md`（4-space nested fence 使簡易 scanner 誤判）。
4. `_install-and-configure/install-opensearch/docker.md`（line 512 附近 malformed fence）。
5. `_security/access-control/users-roles.md`（line 280 開 fence、未見 close）。

因此 renderer 要先以 Markdown/Kramdown fence semantics 分段，再在非 code、非 raw span 中處理 Liquid；不能用「看到第一個 ``` 後全部跳過」的 scanner。例外是 fenced code 中明確的 `site.*` expressions：例如 Docker command 的 `site.opensearch_version` 是文件要求的 renderable variable，應以 allowlist render；其他 Mustache/Go/Jinja literal 則以 sentinels/raw spans 保護，並在 restore 後另驗證原文仍存在。

## Kramdown IAL、HTML 與 layout 語意

OpenSearch product pages 有 1,379 個 Kramdown IAL occurrences、615 files；其中 conservative fence scan 判定 1,374 在 fence 外、5 在 fence state 內。Dashboards 有 190 個、49 files，全部在 fence 外。OpenSearch 的主要 normalized bodies：`.note` 433、`.label .label-purple` 386、`.tip` 136、`.text-delta` 134、`.warning` 94、`.important` 83、`toc` 25、`target='_blank'` 22、`:nomarkdown` 21、`{:/}` 21、`.no_toc` 7，另有少量 button、image style、其他 label/class；Dashboards 主要為 `:nomarkdown`/`{:/}` 43/43、`.note` 35、`.label .label-purple` 32、`.warning` 13、`.img-fluid` 8、`.tip` 7、`.text-delta` 4、`.note purple` 3、`.important` 2。

profile 必須保留 IAL 的 class/attribute 語意：`{:toc}` 應轉成 local TOC marker 或採明確移除策略；`:nomarkdown` paired block 常包住 inline HTML/image，不能把 wrapper 當正文；`target='_blank'`、style、class 等 attributes 要保留。IAL-like text 在 fenced literal 中不可當作 syntax。

## Internal links 與 include expansion 規格

`site.url`、`site.baseurl` 是所有 page link 的主要來源：OpenSearch 各 3,472 occurrences，Dashboards 各 417。固定 config 的 render context 是 `site.url=https://docs.opensearch.org`、`site.baseurl=/latest`；profile 應先 render site context，再去除 origin/baseurl/query/fragment，轉成 corpus-local canonical path。

建議最小 resolver 流程：

1. 先 parse 全部 frontmatter，建立 source-relative page registry；不要先輸出同名 Markdown。
2. `permalink`（explicit 或依 Jekyll collection `/:collection/:path/` 推導）決定 page route，並將 subtree `index.md` collapse 成目錄 root；`canonical_url` 只保留為 metadata，只有不會遮蔽真實 permalink route 時才登記 alias。
3. 將 `https://docs.opensearch.org/latest/...`、`/latest/...`、trailing-slash 與 `index` variant canonicalize 成同一 key；同時建立 source `.md`、extensionless path 與 permalink index。
4. 將 `redirect_from` aliases map 到同一 page，大小寫 normalize、deduplicate 並保留 source metadata。
5. 兩份 manifest 必須共享 registry：`/dashboards/...` 優先對 `_dashboards` corpus；Dashboards page 對 `/query-dsl`、`/security` 等 core routes 應對 OpenSearch registry。若 builder 一次只載入一個 manifest，必須留下明確 unresolved-cross-corpus marker 或 pinned source URL，不能靜默變成破連結。
6. `assets`／`images` 路徑要維持 immutable source URL 或明確 asset marker；不要把 binary asset 誤當 docs page。

body-direct include 目前可採 strict allowlist：`copy-curl.html`、`copy.html`、`cards.html`、`list.html`、`youtube-player.html`；先建立 include argument context（`include.cards`、`include.list_items`、`include.documentation_link`、`include.id` 與 page data），再展開。五個 direct include 目前沒有 nested include，故 closure 可有限、可測；layout-level include（例如 `redesign_buttons.html` -> `icons.html`）不應在 page corpus 中遞迴展開。

## 後續 zero-residual validation

下列 regex 只應套用在「去除 fenced code 與 `{% raw %}...{% endraw %}` protection spans 後」的 normalized text；先以 sentinels 保護，再 restore，才能同時達到 zero residual 與 literal preservation：

```regex
# Liquid block tags
\{%-?\s*(?:include|link|highlight|assign|capture|if|elsif|else|endif|for|endfor|unless|endunless|case|when|endcase|comment|endcomment|raw|endraw|continue|last_modified_at)\b.*?-?%\}

# Liquid output expressions
\{\{-?\s*[^}\n]*?-?\}\}

# broad combined detector
\{[{%]

# Kramdown IAL (run line-aware)
(?m)^\s*\{:[^}\n]+\}
```

完成 profile 後，正文區的 `include/link/highlight/assign/capture/conditional/raw/comment` 與 output tag 應無 residual；`:toc`、IAL、HTML comment 要依 profile contract 轉換或保留。`last_modified_at` 只存在 shared `head_custom.html`，若 corpus 不收 layout include，可在 scope 外明確排除；若 normalize layout，則需提供 plugin-equivalent deterministic value 或將該 comment 設為 layout-only metadata。

Validation 另需 assert：

- 所有 intended literal samples（Mustache/Go/Jinja、`raw` wrappers、fenced `{{...}}`）restore 後 byte/text equivalent。
- fenced `site.*` allowlist sample 只 render 已定義的 site variables；未定義 variable 不得變成空字串而悄悄破壞 command。
- normalized body 不含上列 residual regex；IAL class/attrs、canonical path、redirect aliases 與 source URL metadata 仍可追溯。

## 建議的最小 Jekyll profile 與測試矩陣（交給 Claude review）

建議 profile 由以下可測小函式組成，而不是泛用 template engine：

- `collect_frontmatter_and_page_registry`: YAML frontmatter、collection defaults、explicit permalink/canonical/redirect registry 與 duplicate collision report。
- `parse_jekyll_tags`: Markdown fence、raw/comment span、literal protection；需處理 4-space nested fence 與 malformed source fixture。
- `render_liquid_subset`: strict `include` allowlist、site/page/include context、`assign`、`raw/comment`、必要的 `split`/`first`；未知 tag/filter fail closed 並列出 source path/line。
- `expand_body_includes`: direct include closure、argument validation、遞迴深度上限與 layout-only include boundary。
- `normalize_ial`: preserve class/attributes、paired `:nomarkdown`、TOC marker。
- `resolve_jekyll_links`: origin/baseurl stripping、permalink/source-path/redirect lookup、core↔Dashboards shared registry 與 unresolved marker。
- `validate_no_residual_template_syntax`: scanner-aware regex、literal restore checks、source commit/version metadata。

最小測試矩陣：

1. frontmatter inheritance、explicit collection index permalink、`canonical_url`、redirect aliases、大小寫 `Redirect_from` merge/deduplicate、30 組 source filename collision。
2. 五個 body-direct include target、全部 page argument variants、未知 include/argument、nested include 與 layout-only include 不展開。
3. `site.url`/`site.baseurl`、`site.opensearch_version`、`site.opensearch_major_minor_version`、`site.opensearch_dashboards_version`、`site.lucene_version`；`split`/`first` chain；manifest `site_overrides` policy（OpenSearch 2.19.3／Dashboards 2.19.1）與 source-config 2.19.6 mismatch。
4. fenced Mustache/Go/Jinja literal、`{% raw %}` span、fenced `site.*` allowlist、Jekyll comment，以及五個 malformed/nested fence fixtures。
5. IAL `.note`、labels、`:nomarkdown`/`{:/}`、`:toc`、target/style/class，並確認 fenced IAL-like text 不變。
6. collection permalink、`index.md` collapse、source path ↔ permalink、redirect alias、core↔Dashboards cross-corpus link resolution、asset marker。
7. manifest/source metadata：repo URL 不帶 `.git`、immutable docs commit、raw checkout `HEAD`、fetch metadata；只在此之後才允許進入 normalize。

## Normalize 結果與驗證（2026-09-17）

兩份 manifest 均以 `shortcode_profile = "jekyll"` 完成 normalize；整體索引由主整合流程在全部 corpus 完成後建立。normalize 的固定輸出對帳如下：

| manifest | discovered | source | unique permalink routes | corpus pages | true permalink collision groups | same-corpus unresolved | cross-corpus markers | pinned assets |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| OpenSearch 2.19 | 1,050 | 1,050 | 1,050 | 1,050 | 0 | 50 | 53 | 268 |
| OpenSearch Dashboards 2.19 | 54 | 54 | 54 | 54 | 0 | 1 | 109 | 197 |

因此輸出共有 **1,104** pages；`discovered`、`source`、`corpus` 一一相等，且 expected output 與實際 output 沒有 stale/missing 或 empty directory。每頁 frontmatter 都驗證 `source_commit = cc01280fc1f773421cbcb409bdc8fd7beae2638e`、`source_url` 含相同的 40-hex commit、`source_path` 能回到 raw file、`renderer = jekyll/opensearch`。此次實測 OpenSearch 與 Dashboards 都是 **0** 組真 permalink collision；canonical shared routes（例如 `/migrate-or-upgrade/`）只保留在 `canonical_url` metadata，不能改寫 page route。若未來發生真 permalink collision，collision output 固定放在 `__source__/<repository-relative-path>`，不以 deterministic suffix 假裝成 canonical route。當前輸出路徑以 permalink 為準，例如 OpenSearch `_aggregations/metric/percentile-ranks.md` → `aggregations/metric/percentile-ranks/index.md`，`_upgrade-to/index.md` → `upgrade-to/index.md`；Dashboards `_dashboards/branding.md` → `dashboards/branding/index.md`。

| collection | true permalink collision route | source pages |
| --- | --- | --- |
| OpenSearch | — | 無（0 組） |
| OpenSearch Dashboards | — | 無（0 組） |

直接從 source 盤點出 **3,475** 個 OpenSearch include（`cards` 37、`list` 4、
`copy` 467、`copy-curl` 2,966、`youtube-player` 1），以及 **112** 個
Dashboards include（`copy` 39、`copy-curl` 73）。normalize 後，正式 source pages
中的 `include recursion blocked:` marker 為 **0**，fence/raw 保護範圍外的
include tag 也是 **0**；真正的遞迴阻擋只保留在合成 unit test。fence/raw-aware
validator 檢查全部 1,104 個 body，非 code 的 Liquid/Kramdown residual failure 為
**0**。較寬鬆的 `rg -l '\{%|\{\{'` 仍會命中 32 個 OpenSearch pages，但已
分類為 fenced code 內 208 個 token，以及刻意保留在 inline code 的 35 個
Mustache/Go/Jinja literal；Dashboards 的 broad hit 為 0。因此不會拿 broad grep
結果宣稱不實的全面零殘留。

最終 link marker 共 **213** 個：其中 **162** 個是 cross-corpus（`OpenSearch → Dashboards` 53、`Dashboards → OpenSearch` 109；包含 1 個 ambiguous route），另有 **51** 個 same-corpus unresolved（OpenSearch 50、Dashboards 1；包括 missing/out-of-scope routes、格式錯誤的 source-relative targets，以及 ambiguous redirect aliases）。每個 unresolved route 都保留原始 target 並附上明確 marker；cross-corpus alias 同時查詢另一個 corpus 的 true permalink route 與 redirect alias。HTML assets 全部固定到 immutable source blob URL，共有 OpenSearch 268 個、Dashboards 197 個 pinned assets；route-aware local-link scan 沒有發現未標記的 missing relative output link，也沒有 docs-origin HTML asset URL 仍指向未固定來源。

已知限制是刻意設定的範圍：這個 profile 只 render page body 直接使用的 `copy-curl.html`、`copy.html`、`cards.html`、`list.html`、`youtube-player.html`，layout-only include machinery 不在本批範圍。遇到未知 site variable、filter、include、路徑 traversal 或不支援的 Liquid block 時，會帶著 source path/line 立即失敗。fenced command 中的 `site.*` expression 只允許 allowlist 內的值；fence/raw 內的 literal example 會逐字還原。Kramdown IAL 的 class/attribute 會保留，包住 HTML 的 `:nomarkdown` wrapper 會移除，而 TOC IAL 會轉成 `<!-- local-toc -->`。

驗證完成：本次實測 builder tests **74** cases、runtime tests **5** cases、兩份 Jekyll corpus 的 1,104 頁 residual validator **0** failures、empty-directory scan **0** stale directories；`compileall builder runtime` 與 OpenSearch／Dashboards 路徑的 `git diff --check` 亦由整合流程確認。索引與 Git 交付狀態由主整合流程統一記錄。

### 審查結論

本次最可靠的切分是「共同固定 `documentation-website` tree + `_dashboards` dedicated collection」：OpenSearch 收 26 個 core product roots，Dashboards 收 `_dashboards` 54 pages；shared Jekyll inputs 可以在兩份 sparse checkout 重複保留，但 page source 不重複。安裝 Dashboards 的 `_install-and-configure` pages 留在 OpenSearch manifest，因為這是 source collection 邊界。此決策與 Jekyll profile 已完成 fetch、normalize、metadata/link/residual 驗證；本 note 的 source counts 與上方 normalize 對帳共同證明已產出 1,104 個 corpus pages。
