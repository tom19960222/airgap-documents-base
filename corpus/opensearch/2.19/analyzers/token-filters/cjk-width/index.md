---
collection: "opensearch"
version: "2.19"
title: "CJK width"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/token-filters/cjk-width.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/token-filters/cjk-width.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/token-filters/cjk-width/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/token-filters/cjk-width/"
canonical_route: "/analyzers/token-filters/cjk-width/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 40
parent: "Token filters"
---
# CJK width token filter

The `cjk_width` token filter normalizes Chinese, Japanese, and Korean (CJK) tokens by converting full-width ASCII characters to their standard (half-width) ASCII equivalents and half-width katakana characters to their full-width equivalents.

### Converting full-width ASCII characters

In CJK texts, ASCII characters (such as letters and numbers) can appear in full-width form, occupying the space of two half-width characters. Full-width ASCII characters are typically used in East Asian typography for alignment with the width of CJK characters. However, for the purposes of indexing and searching, these full-width characters need to be normalized to their standard (half-width) ASCII equivalents.

The following example illustrates ASCII character normalization:

```
        Full-Width:              ＡＢＣＤＥ １２３４５
        Normalized (half-width): ABCDE 12345
```

### Converting half-width katakana characters

The `cjk_width` token filter converts half-width katakana characters to their full-width counterparts, which are the standard form used in Japanese text. This normalization, illustrated in the following example, is important for consistency in text processing and searching:

```
        Half-Width katakana:               ｶﾀｶﾅ
        Normalized (full-width) katakana:  カタカナ
```

## Example

The following example request creates a new index named `cjk_width_example_index` and defines an analyzer with the `cjk_width` filter:

```json
PUT /cjk_width_example_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "cjk_width_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["cjk_width"]
        }
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /cjk_width_example_index/_analyze
{
  "analyzer": "cjk_width_analyzer",
  "text": "Ｔｏｋｙｏ 2024 ｶﾀｶﾅ"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "Tokyo",
      "start_offset": 0,
      "end_offset": 5,
      "type": "<ALPHANUM>",
      "position": 0
    },
    {
      "token": "2024",
      "start_offset": 6,
      "end_offset": 10,
      "type": "<NUM>",
      "position": 1
    },
    {
      "token": "カタカナ",
      "start_offset": 11,
      "end_offset": 15,
      "type": "<KATAKANA>",
      "position": 2
    }
  ]
}
```
