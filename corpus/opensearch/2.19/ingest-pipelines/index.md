---
collection: "opensearch"
version: "2.19"
title: "Ingest pipelines"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/"
canonical_route: "/ingest-pipelines/"
redirect_from: ["/api-reference/ingest-apis/ingest-pipelines/","/ingest-pipelines/index/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_toc: true
layout: "default"
nav_exclude: true
nav_order: 5
---
# Ingest pipelines

An _ingest pipeline_ is a sequence of _processors_ that are applied to documents as they are ingested into an index. Each [processor](processors/index-processors/index.md) in a pipeline performs a specific task, such as filtering, transforming, or enriching data.

Processors are customizable tasks that run in a sequential order as they appear in the request body. This order is important, as each processor depends on the output of the previous processor. The modified documents appear in your index after the processors are applied.

## OpenSearch ingest pipelines compared to Data Prepper

OpenSeach ingest pipelines run within the OpenSearch cluster, whereas [Data Prepper](https://docs.opensearch.org/latest/data-prepper/) <!-- unresolved-jekyll-link: route=/data-prepper/ --> is an external component that runs on the OpenSearch cluster.

OpenSearch ingest pipelines perform actions on indexes and are preferred for use cases involving pre-processing simple datasets, [machine learning (ML) processors](processors/sparse-encoding/index.md), and [vector embedding processors](processors/text-image-embedding/index.md). OpenSearch ingest pipelines are recommended for simple data pre-processing and small datasets.

Data Prepper is recommended for any data processing tasks it supports, particularly when dealing with large datasets and complex data pre-processing requirements. It streamlines the process of transferring and fetching large datasets while providing robust capabilities for intricate data preparation and transformation operations. Refer to the [Data Prepper](https://docs.opensearch.org/latest/data-prepper/) <!-- unresolved-jekyll-link: route=/data-prepper/ --> documentation for more information.

OpenSearch ingest pipelines can only be managed using [Ingest API operations](../api-reference/ingest-apis/index.md).
{: .note}

## Prerequisites

The following are prerequisites for using OpenSearch ingest pipelines:

- When using ingestion in a production environment, your cluster should contain at least one node with the node roles permission set to `ingest`. For information about setting up node roles within a cluster, see [Cluster Formation](../tuning-your-cluster/index.md).
- If the OpenSearch Security plugin is enabled, you must have the `cluster_manage_pipelines` permission to manage ingest pipelines.

## Define a pipeline

A _pipeline definition_ describes the sequence of an ingest pipeline and can be written in JSON format. An ingest pipeline consists of the following:

```json
{
    "description" : "..."
    "processors" : [...]
}
```

#### Request body fields

Field | Required | Type | Description
:--- | :--- | :--- | :---
`processors` | Required | Array of processor objects | A component that performs a specific data processing task as the data is being ingested into OpenSearch.
`description` | Optional | String | A description of the ingest pipeline.

## Next steps

Learn how to:

- [Create a pipeline](create-ingest/index.md).
- [Test a pipeline](simulate-ingest/index.md).
- [Retrieve information about a pipeline](get-ingest/index.md).
- [Delete a pipeline](delete-ingest/index.md).
- [Use ingest processors in OpenSearch](processors/index-processors/index.md)
