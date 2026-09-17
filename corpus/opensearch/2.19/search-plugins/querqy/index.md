---
collection: "opensearch"
version: "2.19"
title: "Querqy"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/querqy/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/querqy/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/querqy/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/querqy/index/"
canonical_route: "/search-plugins/querqy/"
redirect_from: ["/search-plugins/querqy/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Search relevance"
has_children: false
layout: "default"
nav_order: 210
parent: "Query rewriting"
---
# Querqy

Querqy is a community plugin for query rewriting that helps to solve relevance issues, making search engines more precise regarding matching and scoring.

Querqy is currently only supported in OpenSearch 2.3.
{: .warning }

## Querqy plugin installation

The Querqy plugin is now available for OpenSearch 2.3.0. Run the following command to install the Querqy plugin.

````bash
./bin/opensearch-plugin install \
   "https://repo1.maven.org/maven2/org/querqy/opensearch-querqy/1.0.os2.3.0/opensearch-querqy-1.0.os2.3.0.zip"
````

Answer `yes` to the security prompts during the installation as Querqy requires additional permissions to load query rewriters.

After installing the Querqy plugin you can find comprehensive documentation on the Querqy.org site: [Querqy](https://docs.querqy.org/querqy/index.html)

## Endpoints

```
POST /myindex/_search
```

## Example query

````json
{
   "query": {
       "querqy": {
           "matching_query": {
               "query": "books"
           },
           "query_fields": [ "title^3.0", "words^2.1", "shortSummary"]
       }
   }
}
````
