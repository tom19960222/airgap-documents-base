---
collection: "opensearch"
version: "2.19"
title: "API"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_monitoring-your-cluster/pa/rca/api.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_monitoring-your-cluster/pa/rca/api.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/monitoring-your-cluster/pa/rca/api/"
canonical_url: "https://docs.opensearch.org/latest/monitoring-your-cluster/pa/rca/api/"
canonical_route: "/monitoring-your-cluster/pa/rca/api/"
redirect_from: ["/monitoring-plugins/pa/rca/api/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Performance Analyzer"
layout: "default"
nav_order: 1
parent: "Root Cause Analysis"
---
# RCA API

## Example request

```
# Request all available RCAs
GET localhost:9600/_plugins/_performanceanalyzer/rca

# Request a specific RCA
GET localhost:9600/_plugins/_performanceanalyzer/rca?name=HighHeapUsageClusterRca
```

## Example response

```json
{
  "HighHeapUsageClusterRca": [{
    "rca_name": "HighHeapUsageClusterRca",
    "state": "unhealthy",
    "timestamp": 1587426650942,
    "HotClusterSummary": [{
      "number_of_nodes": 2,
      "number_of_unhealthy_nodes": 1,
      "HotNodeSummary": [{
        "host_address": "192.168.144.2",
        "node_id": "JtlEoRowSI6iNpzpjlbp_Q",
        "HotResourceSummary": [{
          "resource_type": "old gen",
          "threshold": 0.65,
          "value": 0.81827232588145373,
          "avg": NaN,
          "max": NaN,
          "min": NaN,
          "unit_type": "heap usage in percentage",
          "time_period_seconds": 600,
          "TopConsumerSummary": [{
              "name": "CACHE_FIELDDATA_SIZE",
              "value": 590702564
            },
            {
              "name": "CACHE_REQUEST_SIZE",
              "value": 28375
            },
            {
              "name": "CACHE_QUERY_SIZE",
              "value": 12687
            }
          ],
        }]
      }]
    }]
  }]
}
```
