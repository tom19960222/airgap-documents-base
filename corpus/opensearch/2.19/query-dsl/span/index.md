---
collection: "opensearch"
version: "2.19"
title: "Span queries"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/span/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/span/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/span/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/span/index/"
canonical_route: "/query-dsl/span/"
redirect_from: ["/opensearch/query-dsl/span-query/","/query-dsl/query-dsl/span-query/","/query-dsl/span-query/","/query-dsl/span/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 60
---
# Span queries

You can use span queries to perform precise positional searches. Span queries are low-level, specific queries that provide control over the order and proximity of specified query terms. They are primarily used to search legal documents and patents.

Span queries include the following query types:

- [**Span containing**](span-containing/index.md): Returns larger spans that contain smaller spans within them. Useful for finding specific terms or phrases within a broader context. The opposite of `span_within` query.

- [**Span field masking**](span-field-masking/index.md): Allows span queries to work across different fields by making one field appear as another. Particularly useful when the same text is indexed using different analyzers.

- [**Span first**](span-first/index.md): Matches terms or phrases that appear within a specified number of positions from the start of a field. Useful for finding content at the beginning of text.

- [**Span multi-term**](span-multi-term/index.md): Enables multi-term queries (like `prefix`, `wildcard`, or `fuzzy`) to work within span queries. Allows for more flexible matching patterns in span searches.

- [**Span near**](span-near/index.md): Finds terms or phrases that appear within a specified distance of each other. You can require matches to appear in a specific order and control how many words can appear between them.

- [**Span not**](span-not/index.md): Excludes matches that overlap with another span query. Useful for finding terms when they do not appear in specific phrases or contexts.

- [**Span or**](span-or/index.md): Matches documents that satisfy any of the provided span queries. Combines multiple span patterns with OR logic.

- [**Span term**](span-term/index.md): The basic building block for span queries. Matches a single term while maintaining position information for use in other span queries.

- [**Span within**](span-within/index.md): Returns smaller spans that are enclosed by larger spans. The opposite of the `span_containing` query.

## Setup

To try the examples in this section, use the following steps to configure an example index.

### Step 1: Create an index

First, create an index for an e-commerce clothing website. The `description` field uses the default `standard` analyzer, while the `description.stemmed` subfield applies the `english` analyzer to enable stemming:

```json
PUT /clothing
{
  "mappings": {
    "properties": {
      "description": {
        "type": "text",
        "analyzer": "standard",
        "fields": {
          "stemmed": {
            "type": "text",
            "analyzer": "english"
          }
        }
      }
    }
  }
}
```

### Step 2: Index data

Index sample documents into the index:

```json
POST /clothing/_doc/1
{
  "description": "Long-sleeved dress shirt with a formal collar and button cuffs. "
}

```

```json
POST /clothing/_doc/2
{
  "description": "Beautiful long dress in red silk, perfect for formal events."
}
```

```json
POST /clothing/_doc/3
{
  "description": "Short-sleeved shirt with a button-down collar, can be dressed up or down."
}
```

```json
POST /clothing/_doc/4
{
  "description": "A set of two midi silk shirt dresses with long sleeves in black. "
}
```
