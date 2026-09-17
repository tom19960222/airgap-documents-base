---
collection: "opensearch"
version: "2.19"
title: "Delete Script"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/script-apis/delete-script.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/script-apis/delete-script.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/script-apis/delete-script/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/script-apis/delete-script/"
canonical_route: "/api-reference/script-apis/delete-script/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 4
parent: "Script APIs"
---
# Delete script
**Introduced 1.0**
{: .label .label-purple }

Deletes a stored script.

## Endpoints

```json
DELETE _scripts/my-script
```

## Path parameters

Path parameters are optional.

| Parameter | Data type | Description |
:--- | :--- | :---
| script-id | String | ID of script to delete. |

## Query parameters

| Parameter | Data type | Description |
:--- | :--- | :---
| cluster_manager_timeout | Time | Amount of time to wait for a connection to the cluster manager. Optional, defaults to `30s`. |
| timeout | Time | The period of time to wait for a response. If a response is not received before the timeout value, the request will be dropped.

## Example request

The following request deletes the `my-first-script` script:

````json
DELETE _scripts/my-script
````

## Example response

The `DELETE _scripts/my-first-script` request returns the following field:

````json
{
  "acknowledged" : true
}
````

To determine whether the stored script was successfully deleted, use the [Get stored script](../get-stored-script/index.md) API, passing the script name as the `script` path parameter.

## Response body fields

The <HTTP METHOD> <endpoint> request returns the following response fields:

| Field | Data type | Description |
:--- | :--- | :---
| acknowledged | Boolean | Whether the delete script request was received. |
