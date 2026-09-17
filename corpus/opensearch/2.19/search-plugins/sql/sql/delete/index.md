---
collection: "opensearch"
version: "2.19"
title: "Delete"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/sql/sql/delete.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/sql/sql/delete.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/sql/sql/delete/"
canonical_url: "https://docs.opensearch.org/latest/sql-and-ppl/sql/delete/"
canonical_route: "/sql-and-ppl/sql/delete/"
redirect_from: ["/search-plugins/sql/delete/","/sql-and-ppl/sql/delete/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "SQL and PPL"
layout: "default"
nav_order: 12
parent: "SQL"
---
# Delete

The `DELETE` statement deletes documents that satisfy the predicates in the `WHERE` clause.
If you don't specify the `WHERE` clause, all documents are deleted.

### Setting

The `DELETE` statement is disabled by default. To enable the `DELETE` functionality in SQL, you need to update the configuration by sending the following request:

```json
PUT _plugins/_query/settings
{
  "transient": {
    "plugins.sql.delete.enabled": "true"
  }
}
```

### Syntax

Rule `singleDeleteStatement`:

![singleDeleteStatement](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/singleDeleteStatement.png)

### Example

SQL query:

```sql
DELETE FROM accounts
WHERE age > 30
```

Explain:

```json
{
  "size" : 1000,
  "query" : {
    "bool" : {
      "must" : [
        {
          "range" : {
            "age" : {
              "from" : 30,
              "to" : null,
              "include_lower" : false,
              "include_upper" : true,
              "boost" : 1.0
            }
          }
        }
      ],
      "adjust_pure_negative" : true,
      "boost" : 1.0
    }
  },
  "_source" : false
}
```

Result set:

```json
{
  "schema" : [
    {
      "name" : "deleted_rows",
      "type" : "long"
    }
  ],
  "total" : 1,
  "datarows" : [
    [
      3
    ]
  ],
  "size" : 1,
  "status" : 200
}
```

The `datarows` field shows the number of documents deleted.
