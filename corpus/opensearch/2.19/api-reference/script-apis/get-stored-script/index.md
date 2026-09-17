---
collection: "opensearch"
version: "2.19"
title: "Get Stored Script"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/script-apis/get-stored-script.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/script-apis/get-stored-script.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/script-apis/get-stored-script/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/script-apis/get-stored-script/"
canonical_route: "/api-reference/script-apis/get-stored-script/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 3
parent: "Script APIs"
---
# Get stored script
**Introduced 1.0**
{: .label .label-purple }

Retrieves a stored script.

## Endpoints

```json
GET _scripts/my-first-script
```

## Path parameters

| Parameter | Data type | Description |
:--- | :--- | :---
| script | String | Stored script or search template name. Required.|

## Query parameters

| Parameter | Data type | Description |
:--- | :--- | :---
| cluster_manager_timeout | Time | Amount of time to wait for a connection to the cluster manager. Optional, defaults to `30s`. |

## Example request

The following retrieves the `my-first-script` stored script.

````json
GET _scripts/my-first-script
````

## Example response

The `GET _scripts/my-first-script` request returns the following fields:

````json
{
  "_id" : "my-first-script",
  "found" : true,
  "script" : {
    "lang" : "painless",
    "source" : """
          int total = 0;
          for (int i = 0; i < doc['ratings'].length; ++i) {
            total += doc['ratings'][i];
          }
          return total;
        """
  }
}
````

## Response body fields

The `GET _scripts/my-first-script` request returns the following response fields:

| Field | Data type | Description |
:--- | :--- | :---
| _id | String | The script's name. |
| found | Boolean | The requested script exists and was retrieved. |
| script | Object | The script definition. See [Script object](#script-object).  |

#### Script object

| Field | Data type | Description |
:--- | :--- | :---
| lang | String | The script's language. |
|  source | String | The script's body. |
