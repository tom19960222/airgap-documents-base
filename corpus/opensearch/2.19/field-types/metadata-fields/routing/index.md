---
collection: "opensearch"
version: "2.19"
title: "Routing"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/metadata-fields/routing.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/metadata-fields/routing.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/metadata-fields/routing/"
canonical_url: "https://docs.opensearch.org/latest/mappings/metadata-fields/routing/"
canonical_route: "/mappings/metadata-fields/routing/"
redirect_from: ["/mappings/metadata-fields/routing/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 35
parent: "Metadata fields"
---
# Routing

OpenSearch uses a hashing algorithm to route documents to specific shards in an index. By default, the document's `_id` field is used as the routing value, but you can also specify a custom routing value for each document.

## Default routing

The following is the default OpenSearch routing formula. The `_routing` value is the document's `_id`.

```json
shard_num = hash(_routing) % num_primary_shards
```

## Custom routing

You can specify a custom routing value when indexing a document, as shown in the following example request:

```json
PUT sample-index1/_doc/1?routing=JohnDoe1
{
  "title": "This is a document"
}
```

In this example, the document is routed using the value `JohnDoe1` instead of the default `_id`.

You must provide the same routing value when retrieving, deleting, or updating the document, as shown in the following example request:

```json
GET sample-index1/_doc/1?routing=JohnDoe1
```

## Querying by routing

You can query documents based on their routing value by using the `_routing` field, as shown in the following example. This query only searches the shard(s) associated with the `JohnDoe1` routing value:

```json
GET sample-index1/_search
{
  "query": {
    "terms": {
      "_routing": [ "JohnDoe1" ]
    }
  }
}
```

## Required routing

You can make custom routing required for all CRUD operations on an index, as shown in the following example request. If you try to index a document without providing a routing value, OpenSearch will throw an exception.

```json
PUT sample-index2
{
  "mappings": {
    "_routing": {
      "required": true
    }
  }
}
```

## Routing to specific shards

You can configure an index to route custom values to a subset of shards rather than a single shard. This is done by setting `index.routing_partition_size` at the time of index creation. The formula for calculating the shard is `shard_num = (hash(_routing) + hash(_id)) % routing_partition_size) % num_primary_shards`.

The following example request routes documents to one of four shards in the index:

```json
PUT sample-index3
{
  "settings": {
    "index.routing_partition_size": 4
  },
  "mappings": {
    "_routing": {
      "required": true
    }
  }
}
```
