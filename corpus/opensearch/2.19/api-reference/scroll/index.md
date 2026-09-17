---
collection: "opensearch"
version: "2.19"
title: "Scroll"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/scroll.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/scroll.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/scroll/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/search-apis/scroll/"
canonical_route: "/api-reference/search-apis/scroll/"
redirect_from: ["/opensearch/rest-api/scroll/","/api-reference/search-apis/scroll/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 71
---
# Scroll
**Introduced 1.0**
{: .label .label-purple }

You can use the `scroll` operation to retrieve a large number of results. For example, for machine learning jobs, you can request an unlimited number of results in batches.

To use the `scroll` operation, add a `scroll` parameter to the request header with a search context to tell OpenSearch how long you need to keep scrolling. This search context needs to be long enough to process a single batch of results.

Because search contexts consume a lot of memory, we suggest you don't use the `scroll` operation for frequent user queries. Instead, use the `sort` parameter with the `search_after` parameter to scroll responses for user queries.
{: .note }

## Endpoints

```json
GET _search/scroll
POST _search/scroll
GET _search/scroll/<scroll-id>
POST _search/scroll/<scroll-id>
```

## Path parameters

Parameter | Type | Description
:--- | :--- | :---
scroll_id | String | The scroll ID for the search.

## Query parameters

All scroll parameters are optional.

Parameter | Type | Description
:--- | :--- | :---
scroll | Time | Specifies the amount of time the search context is maintained.
scroll_id | String | The scroll ID for the search.
rest_total_hits_as_int | Boolean | Whether the `hits.total` property is returned as an integer (`true`) or an object (`false`). Default is `false`.

## Example requests

To set the number of results that you want returned for each batch, use the `size` parameter:

```json
GET shakespeare/_search?scroll=10m
{
  "size": 10000
}
```

OpenSearch caches the results and returns a scroll ID to access them in batches:

```json
"_scroll_id" : "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAAUWdmpUZDhnRFBUcWFtV21nMmFwUGJEQQ=="
```

Pass this scroll ID to the `scroll` operation to get back the next batch of results:

```json
GET _search/scroll
{
  "scroll": "10m",
  "scroll_id": "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAAUWdmpUZDhnRFBUcWFtV21nMmFwUGJEQQ=="
}
```

Using this scroll ID, you get results in batches of 10,000 as long as the search context is still open. Typically, the scroll ID does not change between requests, but it *can* change, so make sure to always use the latest scroll ID. If you don't send the next scroll request within the set search context, the `scroll` operation does not return any results.

If you expect billions of results, use a sliced scroll. Slicing allows you to perform multiple scroll operations for the same request, but in parallel.
Set the ID and the maximum number of slices for the scroll:

```json
GET shakespeare/_search?scroll=10m
{
  "slice": {
    "id": 0,
    "max": 10
  },
  "query": {
    "match_all": {}
  }
}
```

With a single scroll ID, you get back 10 results.
You can have up to 10 IDs.

Close the search context when you’re done scrolling, because the `scroll` operation continues to consume computing resources until the timeout:

```json
DELETE _search/scroll/DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAAcWdmpUZDhnRFBUcWFtV21nMmFwUGJEQQ==
```

To close all open scroll contexts:

```json
DELETE _search/scroll/_all
```

The `scroll` operation corresponds to a specific timestamp. It doesn't consider documents added after that timestamp as potential results.

## Example response

```json
{
  "succeeded": true,
  "num_freed": 1
}
```
