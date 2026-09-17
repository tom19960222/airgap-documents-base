---
collection: "opensearch"
version: "2.19"
title: "Span near"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/span/span-near.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/span/span-near.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/span/span-near/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/span/span-near/"
canonical_route: "/query-dsl/span/span-near/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Query DSL"
layout: "default"
nav_order: 50
parent: "Span queries"
---
# Span near query

The `span_near` query matches spans that are near one another. You can specify how far apart the spans can be and whether they need to appear in a specific order.

For example, you can use the `span_near` query to:
- Find terms that appear within a certain distance of each other.
- Match phrases in which words appear in a specific order.
- Find related concepts that appear close to each other in text.

## Example

To try the examples in this section, complete the [setup steps](../index.md#setup).
{: .tip}

The following query searches for any forms of "sleeve" and "long" appearing next to each other, in any order:

```json
GET /clothing/_search
{
  "query": {
    "span_near": {
      "clauses": [
        {
          "span_term": {
            "description.stemmed": "sleev"
          }
        },
        {
          "span_term": {
            "description.stemmed": "long"
          }
        }
      ],
      "slop": 1,
      "in_order": false
    }
  }
}
```

The query matches documents 1 ("Long-sleeved...") and 2 ("...long fluttered sleeves..."). In document 1, the words are next to each other, while in document 2, they are within the specified slop distance of `1` (there is 1 word between them).

<details markdown="block">
  <summary>
    Response
  </summary>
  {: .text-delta}

```json
{
  "took": 3,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 2,
      "relation": "eq"
    },
    "max_score": 0.36496973,
    "hits": [
      {
        "_index": "clothing",
        "_id": "1",
        "_score": 0.36496973,
        "_source": {
          "description": "Long-sleeved dress shirt with a formal collar and button cuffs. "
        }
      },
      {
        "_index": "clothing",
        "_id": "4",
        "_score": 0.25312424,
        "_source": {
          "description": "A set of two midi silk shirt dresses with long fluttered sleeves in black. "
        }
      }
    ]
  }
}
```

## Parameters

The following table lists all top-level parameters supported by `span_near` queries.

| Parameter | Data type | Description |
|:----------|:-----|:------------|
| `clauses` | An array of span queries that define the terms or phrases to match. All specified terms must appear within the defined slop distance. Required. |
| `slop` | Integer | The maximum number of intervening unmatched positions between spans. Required. |
| `in_order` | Boolean | Whether spans need to appear in the same order as in the `clauses` array. Optional. Default is `false`. |
