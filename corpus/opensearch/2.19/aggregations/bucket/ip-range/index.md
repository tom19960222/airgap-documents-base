---
collection: "opensearch"
version: "2.19"
title: "IP range"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_aggregations/bucket/ip-range.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_aggregations/bucket/ip-range.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/aggregations/bucket/ip-range/"
canonical_url: "https://docs.opensearch.org/latest/aggregations/bucket/ip-range/"
canonical_route: "/aggregations/bucket/ip-range/"
redirect_from: ["/query-dsl/aggregations/bucket/ip-range/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 110
parent: "Bucket aggregations"
---
# IP range aggregations

The `ip_range` aggregation is for IP addresses.
It works on `ip` type fields. You can define the IP ranges and masks in the [CIDR](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) notation.

```json
GET opensearch_dashboards_sample_data_logs/_search
{
  "size": 0,
  "aggs": {
    "access": {
      "ip_range": {
        "field": "ip",
        "ranges": [
          {
            "from": "1.0.0.0",
            "to": "126.158.155.183"
          },
          {
            "mask": "1.0.0.0/8"
          }
        ]
      }
    }
  }
}
```

#### Example response

```json
...
"aggregations" : {
  "access" : {
    "buckets" : [
      {
        "key" : "1.0.0.0/8",
        "from" : "1.0.0.0",
        "to" : "2.0.0.0",
        "doc_count" : 98
      },
      {
        "key" : "1.0.0.0-126.158.155.183",
        "from" : "1.0.0.0",
        "to" : "126.158.155.183",
        "doc_count" : 7184
      }
    ]
  }
 }
}
```

If you add a document with malformed fields to an index that has `ip_range` set to `false` in its mappings, OpenSearch rejects the entire document. You can set `ignore_malformed` to `true` to specify that OpenSearch should ignore malformed fields. The default is `false`.

```json
...
"mappings": {
  "properties": {
    "ips": {
      "type": "ip_range",
      "ignore_malformed": true
    }
  }
}
```
