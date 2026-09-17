---
collection: "opensearch"
version: "2.19"
title: "Wildcard"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/term/wildcard.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/term/wildcard.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/term/wildcard/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/term/wildcard/"
canonical_route: "/query-dsl/term/wildcard/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 100
parent: "Term-level queries"
---
# Wildcard query

Use wildcard queries to search for terms that match a wildcard pattern. Wildcard queries support the following operators.

Operator | Description
:--- | :---
`*` | Matches zero or more characters.
`?` | Matches any single character.
`case_insensitive` | If `true`, the wildcard query is case insensitive. If `false`, the wildcard query is case sensitive. Default is `false` (case sensitive).

For a case-sensitive search for terms that start with `H` and end with `Y`, use the following request:

```json
GET shakespeare/_search
{
  "query": {
    "wildcard": {
      "speaker": {
        "value": "H*Y",
        "case_insensitive": false
      }
    }
  }
}
```

If you change `*` to `?`, you get no matches because `?` refers to a single character.

Wildcard queries tend to be slow because they need to iterate over a lot of terms. Avoid placing wildcard characters at the beginning of a query because it could be a very expensive operation in terms of both resources and time.

The [wildcard field type](../../../field-types/supported-field-types/wildcard/index.md) builds an index that is specially designed to be very efficient for wildcard and regular expression queries.

## Parameters

The query accepts the name of the field (`<field>`) as a top-level parameter:

```json
GET _search
{
  "query": {
    "wildcard": {
      "<field>": {
        "value": "patt*rn",
        ...
      }
    }
  }
}
```

The `<field>` accepts the following parameters. All parameters except `value` are optional.

Parameter | Data type | Description
:--- | :--- | :---
`value` | String | The wildcard pattern used for matching terms in the field specified in `<field>`.
`boost` | Floating-point | A floating-point value that specifies the weight of this field toward the relevance score. Values above 1.0 increase the field’s relevance. Values between 0.0 and 1.0 decrease the field’s relevance. Default is 1.0.
`case_insensitive` | Boolean | If `true`, allows case-insensitive matching of the value with the indexed field values. Default is `false` (case sensitivity is determined by the field's mapping).
`rewrite` | String | Determines how OpenSearch rewrites and scores multi-term queries. Valid values are `constant_score`, `scoring_boolean`, `constant_score_boolean`, `top_terms_N`, `top_terms_boost_N`, and `top_terms_blended_freqs_N`. Default is `constant_score`.

If [`search.allow_expensive_queries`](../../index.md#expensive-queries) is set to `false`, then wildcard queries are not executed.
{: .important}
