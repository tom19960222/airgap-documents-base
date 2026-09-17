---
collection: "opensearch"
version: "2.19"
title: "Query Group Lifecycle API"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_tuning-your-cluster/availability-and-recovery/workload-management/query-group-lifecycle-api.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_tuning-your-cluster/availability-and-recovery/workload-management/query-group-lifecycle-api.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/tuning-your-cluster/availability-and-recovery/workload-management/query-group-lifecycle-api/"
canonical_url: "https://docs.opensearch.org/latest/tuning-your-cluster/availability-and-recovery/workload-management/workload-groups/"
canonical_route: "/tuning-your-cluster/availability-and-recovery/workload-management/workload-groups/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Availability and recovery"
layout: "default"
nav_order: 20
parent: "Workload management"
---
# Query Group Lifecycle API

The Query Group Lifecycle API creates, updates, retrieves, and deletes query groups. The API categorizes queries into specific groups, called _query groups_, based on desired resource limits.

## Endpoints

### Create a query group

<!-- spec_insert_start
api: wlm.create_query_group
component: endpoints
omit_header: true
-->
```json
PUT /_wlm/query_group
```
<!-- spec_insert_end -->

### Update a query group

<!-- spec_insert_start
api: wlm.create_query_group
component: endpoints
omit_header: true
-->
```json
PUT /_wlm/query_group
```
<!-- spec_insert_end -->

### Get a query group

<!-- spec_insert_start
api: wlm.get_query_group
component: endpoints
omit_header: true
-->
```json
GET /_wlm/query_group
GET /_wlm/query_group/{name}
```
<!-- spec_insert_end -->

### Delete a query group

<!-- spec_insert_start
api: wlm.create_query_group
component: endpoints
omit_header: true
-->
```json
PUT /_wlm/query_group
```
<!-- spec_insert_end -->

## Request body fields

| Field | Description	 |
| :--- | :--- |
| `_id`  | The ID of the query group, which can be used to associate query requests with the group and enforce the group's resource limits.  |
| `name`  | The name of the query group. |
| `resiliency_mode`  | The resiliency mode of the query group. Valid modes are `enforced`, `soft`, and `monitor`. For more information about resiliency modes, see [Operating modes](../wlm-feature-overview/index.md#operating-modes). |
| `resource_limits` | The resource limits for query requests in the query group. Valid resources are `cpu` and `memory`.  |

When creating a query group, make sure that the sum of the resource limits for a single resource, either `cpu` or `memory`, does not exceed 1.

## Example requests

The following example requests show how to use the Query Group Lifecycle API.

### Create a query group

```json
PUT _wlm/query_group
{
  "name": "analytics",
  "resiliency_mode": "enforced",
  "resource_limits": {
    "cpu": 0.4,
    "memory": 0.2
  }
}
```

### Update a query group

```json
PUT _wlm/query_group/analytics
{
  "resiliency_mode": "monitor",
  "resource_limits": {
    "cpu": 0.41,
    "memory": 0.21
  }
}
```

## Example responses

OpenSearch returns responses similar to the following.

### Creating a query group

```json
{
  "_id":"preXpc67RbKKeCyka72_Gw",
  "name":"analytics",
  "resiliency_mode":"enforced",
  "resource_limits":{
    "cpu":0.4,
    "memory":0.2
  },
  "updated_at":1726270184642
}
```

### Updating a query group

```json
{
  "_id":"preXpc67RbKKeCyka72_Gw",
  "name":"analytics",
  "resiliency_mode":"monitor",
  "resource_limits":{
    "cpu":0.41,
    "memory":0.21
  },
  "updated_at":1726270333804
}
```

## Response body fields

| Field | Description	 |
| :--- | :--- |
| `_id`  | The ID of the query group. |
| `name`  | The name of the query group. Required when creating a new query group. |
| `resiliency_mode`  | The resiliency mode of the query group. |
| `resource_limits` | The resource limits of the query group. |
| `updated_at` | The time at which the query group was last updated. |
