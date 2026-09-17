---
collection: "opensearch"
version: "2.19"
title: "Index request cache"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/caching/request-cache.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/caching/request-cache.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/caching/request-cache/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/caching/request-cache/"
canonical_route: "/search-plugins/caching/request-cache/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Improving search performance"
layout: "default"
nav_order: 5
parent: "Caching"
---
# Index request cache

The OpenSearch index request cache is a specialized caching mechanism designed to enhance search performance by storing the results of frequently executed search queries at the shard level. This reduces cluster load and improves response times for repeated searches. This cache is enabled by default and is particularly useful for read-heavy workloads where certain queries are executed frequently.

The cache is automatically invalidated at the configured refresh interval. The invalidation includes document updates (including document deletions) and changes to index settings. This ensures that stale results are never returned from the cache. When the cache size exceeds its configured limit, the least recently used entries are evicted to make room for new entries.

Some queries are ineligible for the request cache. These include profiled queries, scroll queries, and search requests with non-deterministic characteristics (such as those using `Math.random()` or DFS queries) or relative times (such as `now` or `new Date()`). By default, only requests with `size=0` are cacheable. In OpenSearch 2.19 and later, this behavior can be changed using `indices.requests.cache.maximum_cacheable_size`.
{: .note}

## Configuring request caching

You can configure the index request cache by setting the parameters in the `opensearch.yml` configuration file or using the REST API. For more information, see [Index settings](../../../install-and-configure/configuring-opensearch/index-settings/index.md).

### Settings

The following table lists the index request cache settings. For more information about dynamic settings, see [Index settings](../../../install-and-configure/configuring-opensearch/index-settings/index.md).

Setting | Data type  | Default | Level | Static/Dynamic | Description
:--- |:-----------|:--------| :--- | :--- | :---
`indices.cache.cleanup_interval` | Time unit  | `1m` (1 minute)  | Cluster | Static | Schedules a recurring background task that cleans up expired entries from the cache at the specified interval.
`indices.requests.cache.size` | Percentage | `1%`      | Cluster | Static | The cache size as a percentage of the heap size (for example, to use 1% of the heap, specify `1%`).
`index.requests.cache.enable` | Boolean    | `true`    | Index | Dynamic | Enables or disables the request cache.
`indices.requests.cache.maximum_cacheable_size` | Integer    | `0`    | Cluster | Dynamic | Sets the maximum `size` of queries to be added to the request cache.

### Example

To disable the request cache for an index, send the following request:

```json
PUT /my_index/_settings
{
  "index.requests.cache.enable": false
}
```

## Caching specific requests

In addition to providing index-level or cluster-level settings for the request cache, you can also cache specific search requests selectively by setting the `request_cache` query parameter to `true`:

```json
GET /students/_search?request_cache=true
{
  "query": {
    "match": {
      "name": "doe john"
    }
  }
}
```

## Monitoring the request cache

Monitoring cache usage and performance is crucial to maintaining an efficient caching strategy. OpenSearch provides several APIs to help monitor the cache.

### Retrieving cache statistics for all nodes

The [Nodes Stats API](../../../api-reference/nodes-apis/nodes-stats/index.md) returns cache statistics for all nodes in a cluster:

```json
GET /_nodes/stats/indices/request_cache
```

The response contains the request cache statistics:

```json
{
  "nodes": {
    "T7aqO6zaQX-lt8XBWBYLsA": {
      "indices": {
        "request_cache": {
          "memory_size_in_bytes": 10240,
          "evictions": 0,
          "hit_count": 50,
          "miss_count": 10
        }
      }
    }
  }
}
```

### Retrieving cache statistics for a specific index

The [Index Stats API](../../../api-reference/index-apis/stats/index.md) returns cache statistics for a specific index:

```json
GET /my_index/_stats/request_cache
```

The response contains the request cache statistics:

```json
{
  "_shards": {
    "total": 5,
    "successful": 5,
    "failed": 0
  },
  "_all": {
    "primaries": {
      "request_cache": {
        "memory_size_in_bytes": 2048,
        "evictions": 1,
        "hit_count": 30,
        "miss_count": 5
      }
    },
    "total": {
      "request_cache": {
        "memory_size_in_bytes": 4096,
        "evictions": 2,
        "hit_count": 60,
        "miss_count": 10
      }
    }
  },
  "indices": {
    "my_index": {
      "primaries": {
        "request_cache": {
          "memory_size_in_bytes": 2048,
          "evictions": 1,
          "hit_count": 30,
          "miss_count": 5
        }
      },
      "total":{
        "request_cache": {
          "memory_size_in_bytes": 4096,
          "evictions": 2,
          "hit_count": 60,
          "miss_count": 10
        }
      }
    }
  }
}
```

## Best practices

When using the index request cache, consider the following best practices:

- **Appropriate cache size**: Configure the cache size based on your query patterns. A larger cache can store more results but may consume significant resources.
- **Query optimization**: Ensure that frequently executed queries are optimized so that they can benefit from caching.
- **Monitoring**: Regularly monitor cache hit and cache miss rates to understand cache efficiency and make necessary adjustments.
