---
collection: "opensearch"
version: "2.19"
title: "Geodistance"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_query-dsl/geo-and-xy/geodistance.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_query-dsl/geo-and-xy/geodistance.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/query-dsl/geo-and-xy/geodistance/"
canonical_url: "https://docs.opensearch.org/latest/query-dsl/geo-and-xy/geodistance/"
canonical_route: "/query-dsl/geo-and-xy/geodistance/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 20
parent: "Geographic and xy queries"
---
# Geodistance query

A geodistance query returns documents with geopoints that are within a specified distance from the provided geopoint. A document with multiple geopoints matches the query if at least one geopoint matches the query.

The searched document field must be mapped as `geo_point`.
{: .note}

## Example

Create a mapping with the `point` field mapped as `geo_point`:

```json
PUT testindex1
{
  "mappings": {
    "properties": {
      "point": {
        "type": "geo_point"
      }
    }
  }
}
```

Index a geopoint, specifying its latitude and longitude:

```json
PUT testindex1/_doc/1
{
  "point": {
    "lat": 74.00,
    "lon": 40.71
  }
}
```

Search for documents whose `point` objects are within the specified `distance` from the specified `point`:

```json
GET /testindex1/_search
{
  "query": {
    "bool": {
      "must": {
        "match_all": {}
      },
      "filter": {
        "geo_distance": {
          "distance": "50mi",
          "point": {
            "lat": 73.5,
            "lon": 40.5
          }
        }
      }
    }
  }
}
```

The response contains the matching document:

```json
{
  "took": 5,
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
    "max_score": 1,
    "hits": [
      {
        "_index": "testindex1",
        "_id": "1",
        "_score": 1,
        "_source": {
          "point": {
            "lat": 74,
            "lon": 40.71
          }
        }
      }
    ]
  }
}
```

## Parameters

Geodistance queries accept the following parameters.

Parameter | Data type | Description
:--- | :--- | :---
`_name` | String | The name of the filter. Optional.
`distance` | String | The distance within which to match the points. This distance is the radius of a circle centered at the specified point. For supported distance units, see [Distance units](../../../api-reference/common-parameters/index.md#distance-units). Required.
`distance_type` | String | Specifies how to calculate the distance. Valid values are `arc` or `plane` (faster but inaccurate for long distances or points close to the poles). Optional. Default is `arc`.
`validation_method` | String | The validation method. Valid values are `IGNORE_MALFORMED` (accept geopoints with invalid coordinates), `COERCE` (try to coerce coordinates to valid values), and `STRICT` (return an error when coordinates are invalid). Optional. Default is `STRICT`.
`ignore_unmapped` | Boolean | Specifies whether to ignore an unmapped field. If set to `true`, then the query does not return any documents that contain an unmapped field. If set to `false`, then an exception is thrown when the field is unmapped. Optional. Default is `false`.

## Accepted formats

You can specify the geopoint coordinates when indexing a document and searching for documents in any [format](../../../field-types/supported-field-types/geo-point/index.md#formats) accepted by the geopoint field type.
