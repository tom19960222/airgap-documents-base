---
collection: "opensearch"
version: "2.19"
title: "Span containing"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/span/span-containing.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/span/span-containing.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/span/span-containing/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/span/span-containing/"
canonical_route: "/query-dsl/span/span-containing/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Query DSL"
layout: "default"
nav_order: 10
parent: "Span queries"
---
# Span containing query

The `span_containing` query finds matches where a larger text pattern (like a phrase or a set of words) contains a smaller text pattern within its boundaries. Think of it as finding a word or phrase but only when it appears within a specific larger context.

For example, you can use the `span_containing` query to perform the following searches:

- Find the word "quick" but only when it appears in sentences that mention both foxes and behavior.
- Ensure that certain terms appear within the context of other terms---not just anywhere in the document.
- Search for specific words that appear within larger meaningful phrases.

## Example

To try the examples in this section, complete the [setup steps](../index.md#setup).
{: .tip}

The following query searches for occurrences of the word "red" that appear within a larger span containing the words "silk" and "dress" (not necessarily in that order) within 5 words of each other:

```json
GET /clothing/_search
{
  "query": {
    "span_containing": {
      "little": {
        "span_term": {
          "description": "red"
        }
      },
      "big": {
        "span_near": {
          "clauses": [
            {
              "span_term": {
                "description": "silk"
              }
            },
            {
              "span_term": {
                "description": "dress"
              }
            }
          ],
          "slop": 5,
          "in_order": false
        }
      }
    }
  }
}
```

The query matches document 1 because:

- It finds a span in which "silk" and "dress" appear within at most 5 words of each other ("...dress in red silk..."). The terms "silk" and "dress" are within 2 words of each other (there are 2 words between them).
- Within this larger span, it finds the term "red".

<details markdown="block">
  <summary>
    Response
  </summary>
  {: .text-delta}

```json
{
  "took": 4,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 1.1577396,
    "hits": [
      {
        "_index": "clothing",
        "_id": "2",
        "_score": 1.1577396,
        "_source": {
          "description": "Beautiful long dress in red silk, perfect for formal events."
        }
      }
    ]
  }
}
```

</details>

Both `little` and `big` parameters can contain any type of span query, allowing for complex nested span queries when needed.

## Parameters

The following table lists all top-level parameters supported by `span_containing` queries. All parameters are required.

| Parameter |  Data type | Description |
|:-----------|:------|:-------------|
| `little` | Object | The span query that must be contained within the `big` span. This defines the span you're searching for within a larger context. |
| `big` | Object | The containing span query that defines the boundaries within which the `little` span must appear. This establishes the context for your search. |
