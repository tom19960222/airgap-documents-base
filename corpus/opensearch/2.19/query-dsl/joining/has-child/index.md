---
collection: "opensearch"
version: "2.19"
title: "Has child"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/joining/has-child.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/joining/has-child.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/joining/has-child/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/joining/has-child/"
canonical_route: "/query-dsl/joining/has-child/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 10
parent: "Joining queries"
---
# Has child query

The `has_child` query returns parent documents whose child documents match a specific query. You can establish parent/child relationships between documents in the same index by using a [join](../../../field-types/supported-field-types/join/index.md) field type.

The `has_child` query is slower than other queries because of the join operation it performs. Performance decreases as the number of matching child documents pointing to different parent documents increases. Each `has_child` query in your search may significantly impact query performance. If you prioritize speed, avoid using this query or limit its usage as much as possible.
{: .warning}

## Example

Before you can run a `has_child` query, your index must contain a [join](../../../field-types/supported-field-types/join/index.md) field in order to establish parent/child relationships. The index mapping request uses the following format:

```json
PUT /example_index
{
  "mappings": {
    "properties": {
      "relationship_field": {
        "type": "join",
        "relations": {
          "parent_doc": "child_doc"
        }
      }
    }
  }
}
```

In this example, you'll configure an index that contains documents representing products and their brands.

First, create the index and establish the parent/child relationship between `brand` and `product`:

```json
PUT testindex1
{
  "mappings": {
    "properties": {
      "product_to_brand": {
        "type": "join",
        "relations": {
          "brand": "product"
        }
      }
    }
  }
}
```

Index two parent (brand) documents:

```json
PUT testindex1/_doc/1
{
  "name": "Luxury brand",
  "product_to_brand" : "brand"
}
```

```json
PUT testindex1/_doc/2
{
  "name": "Economy brand",
  "product_to_brand" : "brand"
}
```

Index three child (product) documents:

```json
PUT testindex1/_doc/3?routing=1
{
  "name": "Mechanical watch",
  "sales_count": 150,
  "product_to_brand": {
    "name": "product",
    "parent": "1"
  }
}
```

```json
PUT testindex1/_doc/4?routing=2
{
  "name": "Electronic watch",
  "sales_count": 300,
  "product_to_brand": {
    "name": "product",
    "parent": "2"
  }
}
```

```json
PUT testindex1/_doc/5?routing=2
{
  "name": "Digital watch",
  "sales_count": 100,
  "product_to_brand": {
    "name": "product",
    "parent": "2"
  }
}
```

To search for the parent of a child, use a `has_child` query. The following query returns parent documents (brands) that make watches:

```json
GET testindex1/_search
{
  "query" : {
    "has_child": {
      "type":"product",
      "query": {
        "match" : {
            "name": "watch"
        }
      }
    }
  }
}
```

The response returns both brands:

```json
{
  "took": 15,
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
    "max_score": 1,
    "hits": [
      {
        "_index": "testindex1",
        "_id": "1",
        "_score": 1,
        "_source": {
          "name": "Luxury brand",
          "product_to_brand": "brand"
        }
      },
      {
        "_index": "testindex1",
        "_id": "2",
        "_score": 1,
        "_source": {
          "name": "Economy brand",
          "product_to_brand": "brand"
        }
      }
    ]
  }
}
```

## Retrieving inner hits

To return child documents that matched the query, provide the `inner_hits` parameter:

```json
GET testindex1/_search
{
  "query" : {
    "has_child": {
      "type":"product",
      "query": {
        "match" : {
            "name": "watch"
        }
      },
      "inner_hits": {}
    }
  }
}
```

The response contains child documents in the `inner_hits` field:

```json
{
  "took": 52,
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
    "max_score": 1,
    "hits": [
      {
        "_index": "testindex1",
        "_id": "1",
        "_score": 1,
        "_source": {
          "name": "Luxury brand",
          "product_to_brand": "brand"
        },
        "inner_hits": {
          "product": {
            "hits": {
              "total": {
                "value": 1,
                "relation": "eq"
              },
              "max_score": 0.53899646,
              "hits": [
                {
                  "_index": "testindex1",
                  "_id": "3",
                  "_score": 0.53899646,
                  "_routing": "1",
                  "_source": {
                    "name": "Mechanical watch",
                    "sales_count": 150,
                    "product_to_brand": {
                      "name": "product",
                      "parent": "1"
                    }
                  }
                }
              ]
            }
          }
        }
      },
      {
        "_index": "testindex1",
        "_id": "2",
        "_score": 1,
        "_source": {
          "name": "Economy brand",
          "product_to_brand": "brand"
        },
        "inner_hits": {
          "product": {
            "hits": {
              "total": {
                "value": 2,
                "relation": "eq"
              },
              "max_score": 0.53899646,
              "hits": [
                {
                  "_index": "testindex1",
                  "_id": "4",
                  "_score": 0.53899646,
                  "_routing": "2",
                  "_source": {
                    "name": "Electronic watch",
                    "sales_count": 300,
                    "product_to_brand": {
                      "name": "product",
                      "parent": "2"
                    }
                  }
                },
                {
                  "_index": "testindex1",
                  "_id": "5",
                  "_score": 0.53899646,
                  "_routing": "2",
                  "_source": {
                    "name": "Digital watch",
                    "sales_count": 100,
                    "product_to_brand": {
                      "name": "product",
                      "parent": "2"
                    }
                  }
                }
              ]
            }
          }
        }
      }
    ]
  }
}
```

For more information about retrieving inner hits, see [Inner hits](../../../search-plugins/searching-data/inner-hits/index.md).

## Parameters

The following table lists all top-level parameters supported by `has_child` queries.

| Parameter  | Required/Optional | Description  |
|:---|:---|:---|
| `type` | Required | Specifies the name of the child relationship as defined in the `join` field mapping. |
| `query` | Required | The query to run on child documents. If a child document matches the query, the parent document is returned. |
| `ignore_unmapped` | Optional | Indicates whether to ignore unmapped `type` fields and not return documents instead of throwing an error. You can provide this parameter when querying multiple indexes, some of which may not contain the `type` field. Default is `false`. |
| `max_children` | Optional | The maximum number of matching child documents for a parent document. If exceeded, the parent document is excluded from the search results. |
| `min_children` | Optional | The minimum number of matching child documents required for a parent document to be included in the results. If not met, the parent is excluded. Default is `1`.|
| `score_mode` | Optional | Defines how scores of matching child documents influence the parent document's score. Valid values are: <br> - `none`: Ignores the relevance scores of child documents and assigns a score of `0` to the parent document. <br> - `avg`: Uses the average relevance score of all matching child documents. <br> - `max`: Assigns the highest relevance score from the matching child documents to the parent. <br> - `min`: Assigns the lowest relevance score from the matching child documents to the parent. <br> - `sum`: Sums the relevance scores of all matching child documents. <br> Default is `none`. |
| `inner_hits` | Optional | If provided, returns the underlying hits (child documents) that matched the query. |

## Sorting limitations

The `has_child` query does not support [sorting results](../../../search-plugins/searching-data/sort/index.md) using standard sorting options. If you need to sort parent documents by fields in their child documents, you can use a [`function_score` query](../../compound/function-score/index.md) and sort by the parent document's score.

In the preceding example, you can sort parent documents (brands) based on the `sales_count` of their child products. This query multiplies the score by the `sales_count` field of the child documents and assigns the highest relevance score from the matching child documents to the parent:

```json
GET testindex1/_search
{
  "query": {
    "has_child": {
      "type": "product",
      "query": {
        "function_score": {
          "script_score": {
            "script": "_score * doc['sales_count'].value"
          }
        }
      },
      "score_mode": "max"
    }
  }
}
```

The response contains the brands sorted by the highest child `sales_count`:

```json
{
  "took": 6,
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
    "max_score": 300,
    "hits": [
      {
        "_index": "testindex1",
        "_id": "2",
        "_score": 300,
        "_source": {
          "name": "Economy brand",
          "product_to_brand": "brand"
        }
      },
      {
        "_index": "testindex1",
        "_id": "1",
        "_score": 150,
        "_source": {
          "name": "Luxury brand",
          "product_to_brand": "brand"
        }
      }
    ]
  }
}
```

## Next steps

- Learn more about [retrieving inner hits](../../../search-plugins/searching-data/inner-hits/index.md).
