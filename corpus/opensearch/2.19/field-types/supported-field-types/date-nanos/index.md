---
collection: "opensearch"
version: "2.19"
title: "Date nanoseconds"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_field-types/supported-field-types/date-nanos.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_field-types/supported-field-types/date-nanos.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/field-types/supported-field-types/date-nanos/"
canonical_url: "https://docs.opensearch.org/latest/mappings/supported-field-types/date-nanos/"
canonical_route: "/mappings/supported-field-types/date-nanos/"
redirect_from: ["/mappings/supported-field-types/date-nanos/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Supported field types"
has_children: false
layout: "default"
nav_order: 35
parent: "Date field types"
---
# Date nanoseconds field type
**Introduced 1.0**
{: .label .label-purple }

The `date_nanos` field type is similar to the [`date`](../date/index.md) field type in that it holds a date. However, `date` stores the date in millisecond resolution, while `date_nanos` stores the date in nanosecond resolution. Dates are stored as `long` values that correspond to nanoseconds since the epoch. Therefore, the range of supported dates is approximately 1970--2262.

Queries on `date_nanos` fields are converted to range queries on the field value's `long` representation. Then the stored fields and aggregation results are converted to a string using the format set on the field.

The `date_nanos` field supports all [formats](../date/index.md#formats) and [parameters](../date/index.md#parameters) that `date` supports. You can use multiple formats separated by `||`.
{: .note}

For `date_nanos` fields, you can use the `strict_date_optional_time_nanos` format to preserve nanosecond resolution. If you don't specify the format when mapping a field as `date_nanos`, the default format is `strict_date_optional_time||epoch_millis` that lets you pass values in either `strict_date_optional_time` or `epoch_millis` format. The `strict_date_optional_time` format supports dates in nanosecond resolution, but the `epoch_millis` format supports dates in millisecond resolution only.

## Example

Create a mapping with the `date` field of type `date_nanos` that has the `strict_date_optional_time_nanos` format:

```json
PUT testindex/_mapping
{
  "properties": {
      "date": {
        "type": "date_nanos",
        "format" : "strict_date_optional_time_nanos"
      }
    }
}
```

Index two documents into the index:

```json
PUT testindex/_doc/1
{ "date": "2022-06-15T10:12:52.382719622Z" }
```

```json
PUT testindex/_doc/2
{ "date": "2022-06-15T10:12:52.382719624Z" }
```

You can use a range query to search for a date range:

```json
GET testindex/_search
{
  "query": {
    "range": {
      "date": {
        "gte": "2022-06-15T10:12:52.382719621Z",
        "lte": "2022-06-15T10:12:52.382719623Z"
      }
    }
  }
}
```

The response contains the document whose date is in the specified range:

```json
{
  "took": 43,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "testindex",
        "_id": "1",
        "_score": 1,
        "_source": {
          "date": "2022-06-15T10:12:52.382719622Z"
        }
      }
    ]
  }
}
```

When querying documents with `date_nanos` fields, you can use `fields` or `docvalue_fields`:

```json
GET testindex/_search
{
  "fields": ["date"]
}
```

```json
GET testindex/_search
{
  "docvalue_fields" : [
    {
      "field" : "date"
    }
  ]
}
```

The response to either of the preceding queries contains both indexed documents:

```json
{
  "took": 4,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 2,
      "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "testindex",
        "_id": "1",
        "_score": 1,
        "_source": {
          "date": "2022-06-15T10:12:52.382719622Z"
        },
        "fields": {
          "date": [
            "2022-06-15T10:12:52.382719622Z"
          ]
        }
      },
      {
        "_index": "testindex",
        "_id": "2",
        "_score": 1,
        "_source": {
          "date": "2022-06-15T10:12:52.382719624Z"
        },
        "fields": {
          "date": [
            "2022-06-15T10:12:52.382719624Z"
          ]
        }
      }
    ]
  }
}
```

You can sort on a `date_nanos` field as follows:

```json
GET testindex/_search
{
  "sort": {
    "date": "asc"
  }
}
```

The response contains the sorted documents:

```json
{
  "took": 5,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 2,
      "relation": "eq"
    },
    "max_score": null,
    "hits": [
      {
        "_index": "testindex",
        "_id": "1",
        "_score": null,
        "_source": {
          "date": "2022-06-15T10:12:52.382719622Z"
        },
        "sort": [
          1655287972382719700
        ]
      },
      {
        "_index": "testindex",
        "_id": "2",
        "_score": null,
        "_source": {
          "date": "2022-06-15T10:12:52.382719624Z"
        },
        "sort": [
          1655287972382719700
        ]
      }
    ]
  }
}
```

You can also use a Painless script to access the nanoseconds part of the field:

```json
GET testindex/_search
{
  "script_fields" : {
    "my_field" : {
      "script" : {
        "lang" : "painless",
        "source" : "doc['date'].value.nano"
      }
    }
  }
}
```

The response contains only the nanosecond parts of the fields:

```json
{
  "took": 4,
  "timed_out": false,
  "_shards": {
    "total": 1,
    "successful": 1,
    "skipped": 0,
    "failed": 0
  },
  "hits": {
    "total": {
      "value": 2,
      "relation": "eq"
    },
    "max_score": 1,
    "hits": [
      {
        "_index": "testindex",
        "_id": "1",
        "_score": 1,
        "fields": {
          "my_field": [
            382719622
          ]
        }
      },
      {
        "_index": "testindex",
        "_id": "2",
        "_score": 1,
        "fields": {
          "my_field": [
            382719624
          ]
        }
      }
    ]
  }
}
```
