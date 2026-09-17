---
collection: "opensearch"
version: "2.19"
title: "Monitoring"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/sql/monitoring.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/sql/monitoring.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/sql/monitoring/"
canonical_url: "https://docs.opensearch.org/latest/sql-and-ppl/monitoring/"
canonical_route: "/sql-and-ppl/monitoring/"
redirect_from: ["/search-plugins/sql/monitoring/","/sql-and-ppl/monitoring/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 95
parent: "SQL and PPL"
---
# Monitoring

By a stats endpoint, you are able to collect metrics for the plugin
within the interval. Note that only node level statistics collecting is
implemented for now. In other words, you only get the metrics for the
node you're accessing. Cluster level statistics have yet to be
implemented.

## Node Stats

### Description

The meaning of fields in the response is as follows:

|                 Field name|                                                    Description|
| ------------------------- | ------------------------------------------------------------- |
|              request_total|                                         Total count of request|
|              request_count|                     Total count of request within the interval|
|failed_request_count_syserr|Count of failed request due to system error within the interval|
|failed_request_count_cuserr| Count of failed request due to bad request within the interval|
|    failed_request_count_cb| Indicate if plugin is being circuit broken within the interval|

### Example

SQL query:

```console
>> curl -H 'Content-Type: application/json' -X GET localhost:9200/_plugins/_sql/stats
```

Result set:

```json
{
  "failed_request_count_cb": 0,
  "failed_request_count_cuserr": 0,
  "circuit_breaker": 0,
  "request_total": 0,
  "request_count": 0,
  "failed_request_count_syserr": 0
}
```
