---
collection: "opensearch"
version: "2.19"
title: "Create pipeline"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/create-ingest.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/create-ingest.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/create-ingest/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/create-ingest/"
canonical_route: "/ingest-pipelines/create-ingest/"
redirect_from: ["/opensearch/rest-api/ingest-apis/create-update-ingest/","/api-reference/ingest-apis/create-ingest/","/api-reference/ingest-apis/create-update-ingest/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 10
---
# Create pipeline
**Introduced 1.0**
{: .label .label-purple }

Use the create pipeline API operation to create or update pipelines in OpenSearch. Note that the pipeline requires you to define at least one processor that specifies how to change the documents.

## Path and HTTP method

Replace `<pipeline-id>` with your pipeline ID:

```json
PUT _ingest/pipeline/<pipeline-id>
```
#### Example request

Here is an example in JSON format that creates an ingest pipeline with two `set` processors and an `uppercase` processor. The first `set` processor sets the `grad_year` to `2023`, and the second `set` processor sets `graduated` to `true`. The `uppercase` processor converts the `name` field to uppercase.

```json
PUT _ingest/pipeline/my-pipeline
{
  "description": "This pipeline processes student data",
  "processors": [
    {
      "set": {
        "description": "Sets the graduation year to 2023",
        "field": "grad_year",
        "value": 2023
      }
    },
    {
      "set": {
        "description": "Sets graduated to true",
        "field": "graduated",
        "value": true
      }
    },
    {
      "uppercase": {
        "field": "name"
      }
    }
  ]
}
```

To learn more about error handling, see [Handling pipeline failures](../pipeline-failures/index.md).

## Request body fields

The following table lists the request body fields used to create or update a pipeline.

Parameter | Required | Type | Description
:--- | :--- | :--- | :---
`processors` | Required | Array of processor objects | An array of processors, each of which transforms documents. Processors are run sequentially in the order specified.
`description` | Optional | String | A description of your ingest pipeline.

## Path parameters

Parameter | Required | Type | Description
:--- | :--- | :--- | :---
`pipeline-id` | Required | String | The unique identifier, or pipeline ID, assigned to the ingest pipeline.

## Query parameters

Parameter | Required | Type | Description
:--- | :--- | :--- | :---
`cluster_manager_timeout` | Optional | Time | Period to wait for a connection to the cluster manager node. Defaults to 30 seconds.
`timeout` | Optional | Time | Period to wait for a response. Defaults to 30 seconds.

## Template snippets

Some processor parameters support [Mustache](https://mustache.github.io/) template snippets. To get the value of a field, surround the field name in three curly braces, for example, `{{{field-name}}}`.

#### Example: `set` ingest processor using Mustache template snippet

The following example sets the field `{{{role}}}` with a value `{{{tenure}}}`:

```json
PUT _ingest/pipeline/my-pipeline
{
 "processors": [
    {
      "set": {
        "field": "{{{role}}}",
        "value": "{{{tenure}}}"
         }
    }
  ]
}
```
