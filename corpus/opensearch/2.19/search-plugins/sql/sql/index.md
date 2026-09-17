---
collection: "opensearch"
version: "2.19"
title: "SQL"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/sql/sql/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/sql/sql/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/sql/sql/"
canonical_url: "https://docs.opensearch.org/latest/sql-and-ppl/sql/index/"
canonical_route: "/sql-and-ppl/sql/"
redirect_from: ["/search-plugins/sql/sql/index/","/sql-and-ppl/sql/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 4
parent: "SQL and PPL"
---
# SQL

SQL in OpenSearch bridges the gap between traditional relational database concepts and the flexibility of OpenSearch's document-oriented data storage. This integration gives you the ability to use your SQL knowledge to query, analyze, and extract insights from your OpenSearch data.

## SQL and OpenSearch terminology

Here’s how core SQL concepts map to OpenSearch:

SQL | OpenSearch
:--- | :---
Table | Index
Row | Document
Column | Field

## REST API

For a complete REST API reference for the SQL plugin, see [SQL/PPL API](../sql-ppl-api/index.md).

To use the SQL plugin with your own applications, send requests to the `_plugins/_sql` endpoint:

```json
POST _plugins/_sql
{
  "query": "SELECT * FROM my-index LIMIT 50"
}
```

You can query multiple indexes by using a comma-separated list:

```json
POST _plugins/_sql
{
  "query": "SELECT * FROM my-index1,myindex2,myindex3 LIMIT 50"
}
```

You can specify an index pattern with a wildcard expression:

```json
POST _plugins/_sql
{
  "query": "SELECT * FROM my-index* LIMIT 50"
}
```

To run the preceding query in the command line, use the [curl](https://curl.haxx.se/) command:

```bash
curl -XPOST https://localhost:9200/_plugins/_sql -u 'admin:<custom-admin-password>' -k -H 'Content-Type: application/json' -d '{"query": "SELECT * FROM my-index* LIMIT 50"}'
```

You can specify the [response format](../response-formats/index.md) as JDBC, standard OpenSearch JSON, CSV, or raw. By default, queries return data in JDBC format. The following query sets the format to JSON:

```json
POST _plugins/_sql?format=json
{
  "query": "SELECT * FROM my-index LIMIT 50"
}
```

For more information about request parameters, settings, supported operations, and tools, see the related topics under [SQL](index.md).
