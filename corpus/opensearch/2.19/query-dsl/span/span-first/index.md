---
collection: "opensearch"
version: "2.19"
title: "Span first"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/span/span-first.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/span/span-first.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/span/span-first/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/span/span-first/"
canonical_route: "/query-dsl/span/span-first/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Query DSL"
layout: "default"
nav_order: 30
parent: "Span queries"
---
# Span first query

The `span_first` query matches spans that begin at the start of a field and end within a specified number of positions. This query is useful when you want to find terms or phrases that appear near the beginning of a document.

For example, you can use the `span_first` query to perform the following searches:

- Find documents in which specific terms appear in the first few words of a field.
- Ensure certain phrases occur at or near the beginning of a text
- Match patterns only when they appear within a specified distance from the start

## Example

To try the examples in this section, complete the [setup steps](../index.md#setup).
{: .tip}

The following query searches for the stemmed word "dress" appearing within the first 4 positions of the description:

```json
GET /clothing/_search
{
  "query": {
    "span_first": {
      "match": {
        "span_term": {
          "description.stemmed": "dress"
        }
      },
      "end": 4
    }
  }
}
```

The query matches documents 1 and 2:
- Documents 1 and 2 contain the word `dress` at the third position ("Long-sleeved dress..." and "Beautiful long dress"). Indexing of the words starts with 0, so the word "dress" is at position 2.
- The position of the word `dress` must be less than `4`, as specified by the `end` parameter.

<details markdown="block">
  <summary>
    Response
  </summary>
  {: .text-delta}

```json
{
  "took": 13,
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
    "max_score": 0.110377684,
    "hits": [
      {
        "_index": "clothing",
        "_id": "1",
        "_score": 0.110377684,
        "_source": {
          "description": "Long-sleeved dress shirt with a formal collar and button cuffs. "
        }
      },
      {
        "_index": "clothing",
        "_id": "2",
        "_score": 0.110377684,
        "_source": {
          "description": "Beautiful long dress in red silk, perfect for formal events."
        }
      }
    ]
  }
}
```

</details>

The `match` parameter can contain any type of span query, allowing for more complex patterns to be matched at the beginning of fields.

## Parameters

The following table lists all top-level parameters supported by `span_first` queries. All parameters are required.

| Parameter | Data type | Description |
|:----------|:-----|:------------|
| `match` | Object | The span query to match. This defines the pattern you're searching for at the start of the field. |
| `end` | Integer | The maximum end position (exclusive) allowed for the span query match. For example, `end: 4` matches terms at positions 0--3. |
