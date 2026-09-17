---
collection: "opensearch"
version: "2.19"
title: "Delete memory"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/memory-apis/delete-memory.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/memory-apis/delete-memory.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/memory-apis/delete-memory/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/memory-apis/delete-memory/"
canonical_route: "/ml-commons-plugin/api/memory-apis/delete-memory/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 30
parent: "Memory APIs"
---
# Delete a memory
**Introduced 2.12**
{: .label .label-purple }

Use this API to delete a memory based on the `memory_id`.

When the Security plugin is enabled, all memories exist in a `private` security mode. Only the user who created a memory can interact with that memory and its messages.
{: .important}

## Endpoints

```json
DELETE /_plugins/_ml/memory/<memory_id>
```

## Path parameters

The following table lists the available path parameters.

Parameter | Data type | Description
:--- | :--- | :---
`memory_id` | String | The ID of the memory to be deleted.

#### Example request

```json
DELETE /_plugins/_ml/memory/MzcIJX8BA7mbufL6DOwl
```

#### Example response

```json
{
  "success": true
}
```
