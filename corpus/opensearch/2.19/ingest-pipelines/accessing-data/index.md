---
collection: "opensearch"
version: "2.19"
title: "Access data in a pipeline"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ingest-pipelines/accessing-data.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ingest-pipelines/accessing-data.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ingest-pipelines/accessing-data/"
canonical_url: "https://docs.opensearch.org/latest/ingest-pipelines/accessing-data/"
canonical_route: "/ingest-pipelines/accessing-data/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 20
---
# Access data in a pipeline

In ingest pipelines, you can access the document data using the `ctx` object. This object represents the processed document and allows you to read, modify, or enrich the document fields. Pipeline processors have read and write access to both the `_source` field of a document and its metadata fields.

## Accessing document fields

The `ctx` object exposes all document fields. You can access them directly using dot notation.

### Example: Access a top-level field

Given the following example document:

```json
{
  "user": "alice"
}
```

You can access `user` as follows:

```json
"field": "ctx.user"
```

### Example: Access a nested field

Given the following example document:

```json
{
  "user": {
    "name": "alice"
  }
}
```

You can access `user.name` as follows:

```json
"field": "ctx.user.name"
```

## Accessing a field in the source

To access a field in the document `_source`, refer to the field by its name:

```json
{
  "set": {
    "field": "environment",
    "value": "production"
  }
}
```

Alternatively, you can explicitly use `_source`:

```json
{
  "set": {
    "field": "_source.environment",
    "value": "production"
  }
}
```

## Accessing metadata fields

You can read or write to metadata fields such as the following:

- `_index`
- `_type`
- `_id`
- `_routing`

### Example: Set `_routing` dynamically

```json
{
  "set": {
    "field": "_routing",
    "value": "{{region}}"
  }
}
```

Using `{{_id}}` is not supported when document IDs are auto-generated.
{: .note}

## Accessing ingest metadata fields

The `_ingest.timestamp` field represents the time at which the ingest node received the document. To persist this timestamp, use the `set` processor:

```json
{
  "set": {
    "field": "received_at",
    "value": "{{_ingest.timestamp}}"
  }
}
```

## Using `ctx` in Mustache templates

Use Mustache templates to insert field values into processor settings. Use triple curly braces (`{{{` and `}}}`) for unescaped field values.

### Example: Combining source fields

The following processor configuration combines the `app` and `env` fields, separated by an underscore (_), and stores the result in the `log_label` field:

```json
{
  "set": {
    "field": "log_label",
    "value": "{{{app}}}_{{{env}}}"
  }
}
```

### Example: Generating a dynamic greeting using the `set` processor

If a document's `user` field is set to `alice`, use the following syntax to produce the result `"greeting": "Hello, alice!"`:

```json
{
  "set": {
    "field": "greeting",
    "value": "Hello, {{{user}}}!"
  }
}
```

## Dynamic field names

You can use a field's value as the name of a new field:

```json
{
  "set": {
    "field": "{{service}}",
    "value": "{{code}}"
  }
}
```

## Example: Routing to a dynamic index based on status

The following processor configuration sets the target index dynamically by appending `-events` to the value of the `status` field:

```json
{
  "set": {
    "field": "_index",
    "value": "{{status}}-events"
  }
}
```

## Using `ctx` in the `script` processor

Use the `script` processor for advanced transformations.

### Example: Adding a field only if another is missing

The following processor adds the `error_message` field with the value "none" only if the field is missing from the document:

```json
{
  "script": {
    "lang": "painless",
    "source": "if (ctx.error_message == null) { ctx.error_message = 'none'; }"
  }
}
```

### Example: Copying a value from one field to another

The following processor copies the value from the `timestamp` field into a new field called `event_time`:

```json
{
  "script": {
    "lang": "painless",
    "source": "ctx.event_time = ctx.timestamp;"
  }
}
```

## Example of a complete pipeline

The following example defines a complete ingest pipeline that sets a tagline using the `source` field, extracts the `year` from the `date` field, and records the document’s ingest timestamp in the `received_at` field:

```json
PUT _ingest/pipeline/example-pipeline
{
  "description": "Sets tags, log label, and defaults error message",
  "processors": [
    {
      "set": {
        "field": "tagline",
        "value": "{{{user.first}}} from {{{department}}}"
      }
    },
    {
      "script": {
        "lang": "painless",
        "source": "ctx.year = ctx.date.substring(0, 4);"
      }
    },
    {
      "set": {
        "field": "received_at",
        "value": "{{_ingest.timestamp}}"
      }
    }
  ]
}
```

To test the pipeline, use the following request:

```json
POST _ingest/pipeline/example-pipeline/_simulate
{
  "docs": [
    {
      "_source": {
        "user": {
          "first": "Liam"
        },
        "department": "Engineering",
        "date": "2024-12-03T14:05:00Z"
      }
    }
  ]
}
```

The response shows the enriched document after processing, including the newly added `tagline`, extracted `year`, and the `received_at` timestamp generated by the ingest pipeline:

```json
{
  "docs": [
    {
      "doc": {
        "_index": "_index",
        "_id": "_id",
        "_source": {
          "user": {
            "first": "Liam"
          },
          "department": "Engineering",
          "date": "2024-12-03T14:05:00Z",
          "tagline": "Liam from Engineering",
          "year": "2024",
          "received_at": "2025-04-14T18:40:00.000Z"
        },
        "_ingest": {
          "timestamp": "2025-04-14T18:40:00.000Z"
        }
      }
    }
  ]
}
```
