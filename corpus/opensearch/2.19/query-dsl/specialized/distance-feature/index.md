---
collection: "opensearch"
version: "2.19"
title: "Distance feature"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/specialized/distance-feature.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/specialized/distance-feature.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/specialized/distance-feature/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/specialized/distance-feature/"
canonical_route: "/query-dsl/specialized/distance-feature/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_math: true
layout: "default"
nav_order: 5
parent: "Specialized queries"
---
# Distance feature query

Use the `distance_feature` query to boost the relevance of documents that are closer to a specific date or geographic point. This can help you prioritize more recent or nearby content in your search results. For example, you can assign more weight to products manufactured more recently or boost items closest to a user-specified location.

You can apply this query to fields containing date or location data. It's commonly used within a `bool` query `should` clause to improve relevance scoring without filtering out results.

## Configuring the index

Before using the `distance_feature` query, ensure that your index contains at least one of the following field types:

- [`date`](../../../field-types/supported-field-types/date/index.md)
- [`date_nanos`](../../../field-types/supported-field-types/date-nanos/index.md)
- [`geo_point`](../../../field-types/supported-field-types/geo-point/index.md)

In this example, you'll configure the `opening_date` and `coordinates` fields that you can use to run distance feature queries:

```json
PUT /stores
{
  "mappings": {
    "properties": {
      "opening_date": {
        "type": "date"
      },
      "coordinates": {
        "type": "geo_point"
      }
    }
  }
}
```

Add sample documents to the index:

```json
PUT /stores/_doc/1
{
  "store_name": "Green Market",
  "opening_date": "2025-03-10",
  "coordinates": [74.00, 40.70]
}
```

```json
PUT /stores/_doc/2
{
  "store_name": "Fresh Foods",
  "opening_date": "2025-04-01",
  "coordinates": [73.98, 40.75]
}
```

```json
PUT /stores/_doc/3
{
  "store_name": "City Organics",
  "opening_date": "2021-04-20",
  "coordinates": [74.02, 40.68]
}
```

## Example: Boost scores based on recency

The following query searches for documents with a `store_name` matching `market` and boosts recently opened stores:

```json
GET /stores/_search
{
  "query": {
    "bool": {
      "must": {
        "match": {
          "store_name": "market"
        }
      },
      "should": {
        "distance_feature": {
          "field": "opening_date",
          "origin": "2025-04-07",
          "pivot": "10d"
        }
      }
    }
  }
}
```

The response contains the matching document:

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
    "max_score": 1.2372394,
    "hits": [
      {
        "_index": "stores",
        "_id": "1",
        "_score": 1.2372394,
        "_source": {
          "store_name": "Green Market",
          "opening_date": "2025-03-10",
          "coordinates": [
            74,
            40.7
          ]
        }
      }
    ]
  }
}
```

### Example: Boost scores based on geographic proximity

The following query searches for documents with a `store_name` matching `market` and boosts results closer to the given origin point:

```json
GET /stores/_search
{
  "query": {
    "bool": {
      "must": {
        "match": {
          "store_name": "market"
        }
      },
      "should": {
        "distance_feature": {
          "field": "coordinates",
          "origin": [74.00, 40.71],
          "pivot": "500m"
        }
      }
    }
  }
}
```

The response contains the matching document:

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
      "value": 1,
      "relation": "eq"
    },
    "max_score": 1.2910118,
    "hits": [
      {
        "_index": "stores",
        "_id": "1",
        "_score": 1.2910118,
        "_source": {
          "store_name": "Green Market",
          "opening_date": "2025-03-10",
          "coordinates": [
            74,
            40.7
          ]
        }
      }
    ]
  }
}
```

## Parameters

The following table lists all top-level parameters supported by `distance_feature` queries.

| Parameter | Required/Optional | Description |
|-----------|-------------------|-------------|
| `field`   | Required          | The name of the field used to calculate distances. Must be a `date`, `date_nanos`, or `geo_point` field with `index: true` (default) and `doc_values: true` (default). |
| `origin`  | Required          | The point of origin used to calculate distances. Use a [date](../../../field-types/supported-field-types/date/index.md) or [date math expression](../../../field-types/supported-field-types/date/index.md#date-math) (for example, `now-1h`) for `date` fields or a [geopoint](../../../field-types/supported-field-types/geo-point/index.md) for `geo_point` fields. |
| `pivot`   | Required          | The distance from the `origin` at which scores receive half of the `boost` value. Use a time unit (for example, `10d`) for date fields or a distance unit (for example, `1km`) for geographic fields. For more information, see [Units](../../../api-reference/common-parameters/index.md#units).|
| `boost`   | Optional          | A multiplier for the relevance score of matching documents. Must be a non-negative float. Default is `1.0`. |

## How scores are calculated

The `distance_feature` query calculates a document's relevance score using the following formula:

$$ \text{score} = \text{boost} \cdot \frac {\text{pivot}} {\text{pivot} + \text{distance}} $$,

where $$\text{distance}$$ is the absolute difference between the `origin` and the field's value.

## Skipping non-competitive hits

Unlike other score-modifying queries like the `function_score` query, the `distance_feature` query is optimized to efficiently skip non-competitive hits when total hit tracking (`track_total_hits`) is disabled.
