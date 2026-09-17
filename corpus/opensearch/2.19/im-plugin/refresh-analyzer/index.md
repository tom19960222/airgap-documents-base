---
collection: "opensearch"
version: "2.19"
title: "Refresh search analyzer"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_im-plugin/refresh-analyzer.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_im-plugin/refresh-analyzer.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/im-plugin/refresh-analyzer/"
canonical_url: "https://docs.opensearch.org/latest/im-plugin/refresh-analyzer/"
canonical_route: "/im-plugin/refresh-analyzer/"
redirect_from: ["/query-dsl/analyzers/refresh-analyzer/","/im-plugin/refresh-analyzer/index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_toc: false
layout: "default"
nav_order: 50
---
# Refresh search analyzer

You can refresh search analyzers in real time using the following API. This requires the [Index State Management](../ism/index.md) (ISM) plugin to be installed. For more information, see [Installing plugins](../../install-and-configure/plugins/index.md).

```json
POST /_plugins/_refresh_search_analyzers/<index or alias or wildcard>
```
For example, if you change the synonym list in your analyzer, the change takes effect without you needing to close and reopen the index.

To work, the token filter must have an `updateable` flag of `true`:

```json
{
  "analyzer": {
    "my_synonyms": {
      "tokenizer": "whitespace",
      "filter": [
        "synonym"
      ]
    }
  },
  "filter": {
    "synonym": {
      "type": "synonym_graph",
      "synonyms_path": "synonyms.txt",
      "updateable": true
    }
  }
}
```
