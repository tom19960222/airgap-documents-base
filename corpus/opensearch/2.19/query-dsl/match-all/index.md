---
collection: "opensearch"
version: "2.19"
title: "Match all queries"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/match-all.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/match-all.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/match-all/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/match-all/"
canonical_route: "/query-dsl/match-all/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 65
---
# Match all queries

The `match_all` query returns all documents. This query can be useful in testing large document sets if you need to return the entire set.

```json
GET _search
{
  "query": {
    "match_all": {}
  }
}
```

The `match_all` query has a `match_none` counterpart, which is rarely useful:

```json
GET _search
{
  "query": {
    "match_none": {}
  }
}
```

## Parameters

Both the matchall and match none queries accepts the following parameters. All parameters are optional.

Parameter | Data type | Description
:--- | :--- | :---
`boost` | Floating-point | A floating-point value that specifies the weight of this field toward the relevance score. Values above 1.0 increase the field’s relevance. Values between 0.0 and 1.0 decrease the field’s relevance. Default is 1.0.
`_name` | String | The name of the query for query tagging. Optional.
