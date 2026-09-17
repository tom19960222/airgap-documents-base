---
collection: "opensearch"
version: "2.19"
title: "Date histogram"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/bucket/date-histogram.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/bucket/date-histogram.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/bucket/date-histogram/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/bucket/date-histogram/"
canonical_route: "/aggregations/bucket/date-histogram/"
redirect_from: ["/query-dsl/aggregations/bucket/date-histogram/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 20
parent: "Bucket aggregations"
---
# Date histogram aggregations

The `date_histogram` aggregation uses [date math](../../../field-types/supported-field-types/date/index.md#date-math) to generate histograms for time-series data.

For example, you can find how many hits your website gets per month:

```json
GET opensearch_dashboards_sample_data_logs/_search
{
  "size": 0,
  "aggs": {
    "logs_per_month": {
      "date_histogram": {
        "field": "@timestamp",
        "interval": "month"
      }
    }
  }
}
```

#### Example response

```json
...
"aggregations" : {
  "logs_per_month" : {
    "buckets" : [
      {
        "key_as_string" : "2020-10-01T00:00:00.000Z",
        "key" : 1601510400000,
        "doc_count" : 1635
      },
      {
        "key_as_string" : "2020-11-01T00:00:00.000Z",
        "key" : 1604188800000,
        "doc_count" : 6844
      },
      {
        "key_as_string" : "2020-12-01T00:00:00.000Z",
        "key" : 1606780800000,
        "doc_count" : 5595
      }
    ]
  }
}
}
```

The response has three months worth of logs. If you graph these values, you can see the peak and valleys of the request traffic to your website month over month.
