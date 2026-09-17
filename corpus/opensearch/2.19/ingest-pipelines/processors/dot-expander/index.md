---
collection: "opensearch"
version: "2.19"
title: "Dot expander"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/processors/dot-expander.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/processors/dot-expander.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/processors/dot-expander/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/processors/dot-expander/"
canonical_route: "/ingest-pipelines/processors/dot-expander/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 65
parent: "Ingest processors"
---
# Dot expander

The `dot_expander` processor is a tool that helps you work with hierarchical data. It transforms fields containing dots into object fields, making them accessible to other processors in the pipeline. Without this transformation, fields with dots cannot be processed.

The following is the syntax for the `dot_expander` processor:

```json
{
  "dot_expander": {
    "field": "field.to.expand"
  }
}
```

## Configuration parameters

The following table lists the required and optional parameters for the `dot_expander` processor.

Parameter | Required/Optional | Description |
|-----------|-----------|-----------|
`field`  | Required  | The field to be expanded into an object field. |
`path` | Optional | This field is only required if the field to be expanded is nested within another object field. This is because the `field` parameter only recognizes leaf fields. |
`description`  | Optional  | A brief description of the processor. |
`if` | Optional | A condition for running the processor. |
`ignore_failure` | Optional | If set to `true`, failures are ignored. Default is `false`. |
`on_failure` | Optional | A list of processors to run if the processor fails. |
`tag` | Optional | An identifier tag for the processor. Useful for debugging in order to distinguish between processors of the same type. |

## Using the processor

Follow these steps to use the processor in a pipeline.

### Step 1: Create a pipeline

The following query creates a `dot_expander` processor that will expand two fields named `user.address.city` and `user.address.state` into nested objects:

```json
PUT /_ingest/pipeline/dot-expander-pipeline
{
  "description": "Dot expander processor",
  "processors": [
    {
      "dot_expander": {
        "field": "user.address.city"
      }
    },
    {
      "dot_expander":{
       "field": "user.address.state"
      }
    }
  ]
}
```

### Step 2 (Optional): Test the pipeline

It is recommended that you test your pipeline before you ingest documents.
{: .tip}

To test the pipeline, run the following query:

```json
POST _ingest/pipeline/dot-expander-pipeline/_simulate
{
  "docs": [
    {
      "_index": "testindex1",
      "_id": "1",
      "_source": {
        "user.address.city": "New York",
        "user.address.state": "NY"
      }
    }
  ]
}
```

#### Response

The following example response confirms that the pipeline is working as expected:

```json
{
  "docs": [
    {
      "doc": {
        "_index": "testindex1",
        "_id": "1",
        "_source": {
          "user": {
            "address": {
              "city": "New York",
              "state": "NY"
            }
          }
        },
        "_ingest": {
          "timestamp": "2024-01-17T01:32:56.501346717Z"
        }
      }
    }
  ]
}
```

### Step 3: Ingest a document

The following query ingests a document into an index named `testindex1`:

```json
PUT testindex1/_doc/1?pipeline=dot-expander-pipeline
{
  "user.address.city": "Denver",
  "user.address.state": "CO"
}
```

### Step 4 (Optional): Retrieve the document

To retrieve the document, run the following query:

```json
GET testindex1/_doc/1
```

#### Response

The following response confirms that the specified fields were expanded into nested fields:

```json
{
  "_index": "testindex1",
  "_id": "1",
  "_version": 1,
  "_seq_no": 3,
  "_primary_term": 1,
  "found": true,
  "_source": {
    "user": {
      "address": {
        "city": "Denver",
        "state": "CO"
      }
    }
  }
}
```

## The `path` parameter

You can use the `path` parameter to specify the path to a dotted field within an object. For example, the following pipeline specifies the `address.city` field that is located within the `user` object:

```json
PUT /_ingest/pipeline/dot-expander-pipeline
{
  "description": "Dot expander processor",
  "processors": [
    {
      "dot_expander": {
        "field": "address.city",
        "path": "user"
      }
    },
    {
      "dot_expander":{
       "field": "address.state",
       "path": "user"
      }
    }
  ]
}
```

You can simulate the pipeline as follows:

```json
POST _ingest/pipeline/dot-expander-pipeline/_simulate
{
  "docs": [
    {
      "_index": "testindex1",
      "_id": "1",
      "_source": {
        "user": {
          "address.city": "New York",
          "address.state": "NY"
        }
      }
    }
  ]
}
```

The `dot_expander` processor transforms the document into the following structure:

```json
{
  "user": {
    "address": {
      "city": "New York",
      "state": "NY"
    }
  }
}
```

## Field name conflicts

If a field already exists with the same path as the path to which the `dot_expander` processor should expand the value, the processor merges the two values into an array.

Consider the following pipeline that expands the field `user.name`:

```json
PUT /_ingest/pipeline/dot-expander-pipeline
{
  "description": "Dot expander processor",
  "processors": [
    {
      "dot_expander": {
        "field": "user.name"
      }
    }
  ]
}
```

You can simulate the pipeline with a document containing two values with the exact same path `user.name`:

```json
POST _ingest/pipeline/dot-expander-pipeline/_simulate
{
  "docs": [
    {
      "_index": "testindex1",
      "_id": "1",
      "_source": {
        "user.name": "John",
        "user": {
          "name": "Steve"
        }
      }
    }
  ]
}
```

The response confirms that the values were merged into an array:

```json
{
  "docs": [
    {
      "doc": {
        "_index": "testindex1",
        "_id": "1",
        "_source": {
          "user": {
            "name": [
              "Steve",
              "John"
            ]
          }
        },
        "_ingest": {
          "timestamp": "2024-01-17T01:44:57.420220551Z"
        }
      }
    }
  ]
}
```

If a field contains the same name but a different path, then the field needs to be renamed. For example, the following `_simulate` call returns a parse exception:

```json
POST _ingest/pipeline/dot-expander-pipeline/_simulate
{
  "docs": [
    {
      "_index": "testindex1",
      "_id": "1",
      "_source": {
        "user": "John",
        "user.name": "Steve"
      }
    }
  ]
}
```

To avoid the parse exception, first rename the field by using the `rename` processor:

```json
PUT /_ingest/pipeline/dot-expander-pipeline
{
  "processors" : [
    {
      "rename" : {
        "field" : "user",
        "target_field" : "user.name"
      }
    },
    {
      "dot_expander": {
        "field": "user.name"
      }
    }
  ]
}
```

Now you can simulate the pipeline:

```json
POST _ingest/pipeline/dot-expander-pipeline/_simulate
{
  "docs": [
    {
      "_index": "testindex1",
      "_id": "1",
      "_source": {
        "user": "John",
        "user.name": "Steve"
      }
    }
  ]
}
```

The response confirms that the fields were merged:

```json
{
  "docs": [
    {
      "doc": {
        "_index": "testindex1",
        "_id": "1",
        "_source": {
          "user": {
            "name": [
              "John",
              "Steve"
            ]
          }
        },
        "_ingest": {
          "timestamp": "2024-01-17T01:52:12.864432419Z"
        }
      }
    }
  ]
}
```
