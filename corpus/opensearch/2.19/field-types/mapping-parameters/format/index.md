---
collection: "opensearch"
version: "2.19"
title: "Format"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/mapping-parameters/format.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/mapping-parameters/format.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/mapping-parameters/format/"
canonical_url: "https://docs.opensearch.org/latest/mappings/mapping-parameters/format/"
canonical_route: "/mappings/mapping-parameters/format/"
redirect_from: ["/mappings/mapping-parameters/format/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Mapping and field types"
has_children: false
has_toc: false
layout: "default"
nav_order: 50
parent: "Mapping parameters"
---
# Format

The `format` mapping parameter specifies the [built-in date formats](../../supported-field-types/date/index.md#built-in-formats) that a date field can accept during indexing. By defining the expected date formats, you ensure that date values are correctly parsed and stored, facilitating accurate search and aggregation operations.

## Example: Defining a custom date format

Create an `events` index with the `event_date` field configured to a custom `yyyy-MM-dd HH:mm:ss` date format:

```json
PUT events
{
  "mappings": {
    "properties": {
      "event_date": {
        "type": "date",
        "format": "yyyy-MM-dd HH:mm:ss"
      }
    }
  }
}
```

Index a document using the specified format for the `event_date` field:

```json
PUT events/_doc/1
{
  "event_name": "Conference",
  "event_date": "2025-03-26 15:30:00"
}
```

## Example: Using multiple date formats

Create an index containing a `log_timestamp` field, which accepts both the custom `yyyy-MM-dd HH:mm:ss` date format and the `epoch_millis` format:

```json
PUT logs
{
  "mappings": {
    "properties": {
      "log_timestamp": {
        "type": "date",
        "format": "yyyy-MM-dd HH:mm:ss||epoch_millis"
      }
    }
  }
}
```

Index the first document using the custom format:

```json
PUT logs/_doc/1
{
  "message": "System rebooted",
  "log_timestamp": "2025-03-26 08:45:00"
}
```

Index the second document using the millisecond format:

```json
PUT logs/_doc/2
{
  "message": "System updated",
  "log_timestamp": 1711442700000
}
```

## Built-in date formats

For a comprehensive list of built-in date formats, see [Built-in formats](../../supported-field-types/date/index.md#built-in-formats).
