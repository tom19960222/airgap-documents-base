---
collection: "opensearch"
version: "2.19"
title: "Rename field"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/search-pipelines/rename-field-processor.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/search-pipelines/rename-field-processor.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/search-pipelines/rename-field-processor/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/search-pipelines/rename-field-processor/"
canonical_route: "/search-plugins/search-pipelines/rename-field-processor/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Search pipelines"
has_children: false
layout: "default"
nav_order: 100
parent: "Search processors"
---
# Rename field processor
Introduced 2.8
{: .label .label-purple }

The `rename_field` search response processor intercepts a search response and renames the specified field. This is useful when your index and your application use different names for the same field. For example, if you rename a field in your index, the `rename_field` processor can change the new name to the old one before sending the response to your application.

## Request body fields

The following table lists all available request fields.

Field | Data type | Description
:--- | :--- | :---
`field` | String | The field to rename. Required.
`target_field` | String | The new field name. Required.
`tag` | String | The processor's identifier.
`description` | String | A description of the processor.
`ignore_failure` | Boolean | If `true`, OpenSearch [ignores any failure](../creating-search-pipeline/index.md#ignoring-processor-failures) of this processor and continues to run the remaining processors in the search pipeline. Optional. Default is `false`.

## Example

The following example demonstrates using a search pipeline with a `rename_field` processor.

### Setup

Create an index named `my_index` and index a document with the field `message`:

```json
POST /my_index/_doc/1
{
  "message": "This is a public message",
  "visibility":"public"
}
```

### Creating a search pipeline

The following request creates a search pipeline with a `rename_field` response processor that renames the field `message` to `notification`:

```json
PUT /_search/pipeline/my_pipeline
{
  "response_processors": [
    {
      "rename_field": {
        "field": "message",
        "target_field": "notification"
      }
    }
  ]
}
```

### Using a search pipeline

Search for documents in `my_index` without a search pipeline:

```json
GET /my_index/_search
```

The response contains the field `message`:

<details open markdown="block">
  <summary>
    Response
  </summary>
  {: .text-delta}
```json
{
  "took" : 1,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 2,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : "my_index",
        "_id" : "1",
        "_score" : 1.0,
        "_source" : {
          "message" : "This is a public message",
          "visibility" : "public"
        }
      }
    ]
  }
}
```
</details>

To search with a pipeline, specify the pipeline name in the `search_pipeline` query parameter:

```json
GET /my_index/_search?search_pipeline=my_pipeline
```

The `message` field has been renamed to `notification`:

<details open markdown="block">
  <summary>
    Response
  </summary>
  {: .text-delta}
```json
{
  "took" : 2,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "my_index",
        "_id" : "1",
        "_score" : 0.0,
        "_source" : {
          "visibility" : "public",
          "notification" : "This is a public message"
        }
      }
    ]
  }
}
```
</details>

You can also use the `fields` option to search for specific fields in a document:

```json
POST /my_index/_search?pretty&search_pipeline=my_pipeline
{
    "fields":["visibility", "message"]
}
```

In the response, the field `message` has been renamed to `notification`:

<details open markdown="block">
  <summary>
    Response
  </summary>
  {: .text-delta}
```json
{
  "took" : 4,
  "timed_out" : false,
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "skipped" : 0,
    "failed" : 0
  },
  "hits" : {
    "total" : {
      "value" : 1,
      "relation" : "eq"
    },
    "max_score" : 0.0,
    "hits" : [
      {
        "_index" : "my_index",
        "_id" : "1",
        "_score" : 0.0,
        "_source" : {
          "visibility" : "public",
          "notification" : "This is a public message"
        },
        "fields" : {
          "visibility" : [
            "public"
          ],
          "notification" : [
            "This is a public message"
          ]
        }
      }
    ]
  }
}

```
</details>
