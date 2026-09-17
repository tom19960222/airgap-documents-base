---
collection: "opensearch"
version: "2.19"
title: "Get Snapshot"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/snapshots/get-snapshot.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/snapshots/get-snapshot.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/snapshots/get-snapshot/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/snapshots/get-snapshot/"
canonical_route: "/api-reference/snapshots/get-snapshot/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 6
parent: "Snapshot APIs"
---
# Get snapshot.
**Introduced 1.0**
{: .label .label-purple }

Retrieves information about a snapshot.

## Endpoints

```json
GET _snapshot/<repository>/<snapshot>/
```

## Path parameters

| Parameter | Data type | Description |
| :--- | :--- | :--- |
| repository | String | The repository that contains the snapshot to retrieve. |
| snapshot | String | Snapshot to retrieve.

## Query parameters

| Parameter | Data type | Description |
:--- | :--- | :---
| verbose | Boolean | Whether to show all, or just basic snapshot information. If `true`, returns all information. If `false`, omits information like start/end times, failures, and shards. Optional, defaults to `true`.|
| ignore_unavailable | Boolean | How to handle snapshots that are unavailable (corrupted or otherwise temporarily can't be returned). If `true` and the snapshot is unavailable, the request does not return the snapshot. If `false` and the snapshot is unavailable, the request returns an error. Optional, defaults to `false`.|

## Example request

The following request retrieves information for the `my-first-snapshot` located in the `my-opensearch-repo` repository:

````json
GET _snapshot/my-opensearch-repo/my-first-snapshot
````

## Example response

Upon success, the response returns snapshot information:

````json
{
  "snapshots" : [
    {
      "snapshot" : "my-first-snapshot",
      "uuid" : "3P7Qa-M8RU6l16Od5n7Lxg",
      "version_id" : 136217927,
      "version" : "2.0.1",
      "indices" : [
        ".opensearch-observability",
        ".opendistro-reports-instances",
        ".opensearch-notifications-config",
        "shakespeare",
        ".opendistro-reports-definitions",
        "opensearch_dashboards_sample_data_flights",
        ".kibana_1"
      ],
      "data_streams" : [ ],
      "include_global_state" : true,
      "state" : "SUCCESS",
      "start_time" : "2022-08-11T20:30:00.399Z",
      "start_time_in_millis" : 1660249800399,
      "end_time" : "2022-08-11T20:30:14.851Z",
      "end_time_in_millis" : 1660249814851,
      "duration_in_millis" : 14452,
      "failures" : [ ],
      "shards" : {
        "total" : 7,
        "failed" : 0,
        "successful" : 7
      }
    }
  ]
}
````
## Response body fields

| Field | Data type | Description |
| :--- | :--- | :--- |
| snapshot | string | Snapshot name. |
| uuid | string | Snapshot's universally unique identifier (UUID). |
| version_id | int | Build ID of the Open Search version that created the snapshot. |
| version | float | Open Search version that created the snapshot. |
| indices | array | Indices in the snapshot. |
| data_streams | array | Data streams in the snapshot. |
| include_global_state | boolean | Whether the current cluster state is included in the snapshot. |
| start_time | string | Date/time when the snapshot creation process began. |
| start_time_in_millis | long | Time (in milliseconds) when the snapshot creation process began. |
| end_time | string | Date/time when the snapshot creation process ended. |
| end_time_in_millis | long | Time (in milliseconds) when the snapshot creation process ended. |
| duration_in_millis | long | Total time (in milliseconds) that the snapshot creation process lasted. |
| failures | array | Failures, if any, that occured during snapshot creation. |
| shards | object | Total number of shards created along with number of successful and failed shards. |
| state | string | Snapshot status. Possible values: `IN_PROGRESS`, `SUCCESS`, `FAILED`, `PARTIAL`. |
