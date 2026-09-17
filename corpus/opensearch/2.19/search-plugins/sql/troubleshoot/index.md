---
collection: "opensearch"
version: "2.19"
title: "Troubleshooting"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/sql/troubleshoot.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/sql/troubleshoot.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/sql/troubleshoot/"
canonical_url: "https://docs.opensearch.org/latest/sql-and-ppl/troubleshoot/"
canonical_route: "/sql-and-ppl/troubleshoot/"
redirect_from: ["/search-plugins/sql/troubleshoot/","/sql-and-ppl/troubleshoot/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 88
parent: "SQL and PPL"
---
# Troubleshooting

The SQL plugin is stateless, so troubleshooting is mostly focused on why a particular query fails.

The most common error is the dreaded null pointer exception, which can occur during parsing errors or when using the wrong HTTP method (POST vs. GET and vice versa). The POST method and HTTP request body offer the most consistent results:

```json
POST _plugins/_sql
{
  "query": "SELECT * FROM my-index WHERE ['name.firstname']='saanvi' LIMIT 5"
}
```

If a query isn't behaving the way you expect, use the `_explain` API to see the translated query, which you can then troubleshoot. For most operations, `_explain` returns OpenSearch query DSL. For `UNION`, `MINUS`, and `JOIN`, it returns something more akin to a SQL execution plan.

#### Example request

```json
POST _plugins/_sql/_explain
{
  "query": "SELECT * FROM my-index LIMIT  50"
}
```

#### Example response

```json
{
  "from": 0,
  "size": 50
}
```

## Index mapping verification exception

If you see the following verification exception, make sure the index in your query isn't an index pattern and doesn't have multiple types:

```json
{
  "error": {
    "reason": "There was internal problem at backend",
    "details": "When using multiple indices, the mappings must be identical.",
    "type": "VerificationException"
  },
  "status": 503
}
```

If these steps don't work, submit a Github issue [here](https://github.com/opensearch-project/sql/issues).
