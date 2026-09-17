---
collection: "opensearch"
version: "2.19"
title: "Delete Snapshot Repository"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/snapshots/delete-snapshot-repository.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/snapshots/delete-snapshot-repository.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/snapshots/delete-snapshot-repository/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/snapshots/delete-snapshot-repository/"
canonical_route: "/api-reference/snapshots/delete-snapshot-repository/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 3
parent: "Snapshot APIs"
---
# Delete snapshot repository configuration
**Introduced 1.0**
{: .label .label-purple }

Deletes a snapshot repository configuration.

A repository in OpenSearch is simply a configuration that maps a repository name to a type (file system or s3 repository) along with other information depending on the type. The configuration is backed by a file system location or an s3 bucket. When you invoke the API, the physical file system or s3 bucket itself is not deleted. Only the configuration is deleted.

To learn more about repositories, see [Register or update snapshot repository](../create-repository/index.md).

## Endpoints

```json
DELETE _snapshot/<repository>
```

## Path parameters

Parameter | Data type | Description
:--- | :--- | :---
repository | String | Repository to delete. |

## Example request

The following request deletes the `my-opensearch-repo` repository:

````json
DELETE _snapshot/my-opensearch-repo
````

## Example response

Upon success, the response returns the following JSON object:

````json
{
  "acknowledged" : true
}
````

To verify that the repository was deleted, use the [Get snapshot repository](../get-snapshot-repository/index.md) API, passing the repository name as the `repository` path parameter.
{: .note}
