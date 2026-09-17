---
collection: "opensearch"
version: "2.19"
title: "Search pipeline metrics"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/search-pipelines/search-pipeline-metrics.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/search-pipelines/search-pipeline-metrics.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/search-pipelines/search-pipeline-metrics/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/search-pipelines/search-pipeline-metrics/"
canonical_route: "/search-plugins/search-pipelines/search-pipeline-metrics/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Search"
has_children: false
layout: "default"
nav_order: 50
parent: "Search pipelines"
---
# Search pipeline metrics

To view search pipeline metrics, use the [Nodes Stats API](../../../api-reference/nodes-apis/nodes-stats/index.md):

```json
GET /_nodes/stats/search_pipeline
```

The response contains statistics for all search pipelines:

```json
{
  "_nodes" : {
    "total" : 1,
    "successful" : 1,
    "failed" : 0
  },
  "cluster_name" : "runTask",
  "nodes" : {
    "CpvTK7KuRD6Oww8TTp8g2Q" : {
      "timestamp" : 1689007282929,
      "name" : "runTask-0",
      "transport_address" : "127.0.0.1:9300",
      "host" : "127.0.0.1",
      "ip" : "127.0.0.1:9300",
      "roles" : [
        "cluster_manager",
        "data",
        "ingest",
        "remote_cluster_client"
      ],
      "attributes" : {
        "testattr" : "test",
        "shard_indexing_pressure_enabled" : "true"
      },
      "search_pipeline" : {
        "total_request" : {
          "count" : 5,
          "time_in_millis" : 158,
          "current" : 0,
          "failed" : 0
        },
        "total_response" : {
          "count" : 2,
          "time_in_millis" : 1,
          "current" : 0,
          "failed" : 0
        },
        "pipelines" : {
          "public_info" : {
            "request" : {
              "count" : 3,
              "time_in_millis" : 71,
              "current" : 0,
              "failed" : 0
            },
            "response" : {
              "count" : 0,
              "time_in_millis" : 0,
              "current" : 0,
              "failed" : 0
            },
            "request_processors" : [
              {
                "filter_query:abc" : {
                  "type" : "filter_query",
                  "stats" : {
                    "count" : 1,
                    "time_in_millis" : 0,
                    "current" : 0,
                    "failed" : 0
                  }
                }
              },
              {
                "filter_query" : {
                  "type" : "filter_query",
                  "stats" : {
                    "count" : 4,
                    "time_in_millis" : 2,
                    "current" : 0,
                    "failed" : 0
                  }
                }
              }
            ],
            "response_processors" : [ ]
          },
          "guest_pipeline" : {
            "request" : {
              "count" : 2,
              "time_in_millis" : 87,
              "current" : 0,
              "failed" : 0
            },
            "response" : {
              "count" : 2,
              "time_in_millis" : 1,
              "current" : 0,
              "failed" : 0
            },
            "request_processors" : [
              {
                "script" : {
                  "type" : "script",
                  "stats" : {
                    "count" : 2,
                    "time_in_millis" : 86,
                    "current" : 0,
                    "failed" : 0
                  }
                }
              },
              {
                "filter_query:abc" : {
                  "type" : "filter_query",
                  "stats" : {
                    "count" : 1,
                    "time_in_millis" : 0,
                    "current" : 0,
                    "failed" : 0
                  }
                }
              },
              {
                "filter_query" : {
                  "type" : "filter_query",
                  "stats" : {
                    "count" : 3,
                    "time_in_millis" : 0,
                    "current" : 0,
                    "failed" : 0
                  }
                }
              }
            ],
            "response_processors" : [
              {
                "rename_field" : {
                  "type" : "rename_field",
                  "stats" : {
                    "count" : 2,
                    "time_in_millis" : 1,
                    "current" : 0,
                    "failed" : 0
                  }
                }
              }
            ]
          }
        }
      }
    }
  }
}
```

For descriptions of each field in the response, see the [Nodes Stats search pipeline section](../../../api-reference/nodes-apis/nodes-stats/index.md#search_pipeline).
