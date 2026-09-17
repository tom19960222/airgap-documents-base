---
collection: "opensearch"
version: "2.19"
title: "Path hierarchy"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/tokenizers/path-hierarchy.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/tokenizers/path-hierarchy.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/tokenizers/path-hierarchy/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/tokenizers/path-hierarchy/"
canonical_route: "/analyzers/tokenizers/path-hierarchy/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 90
parent: "Tokenizers"
---
# Path hierarchy tokenizer

The `path_hierarchy` tokenizer tokenizes file-system-like paths (or similar hierarchical structures) by breaking them down into tokens at each hierarchy level. This tokenizer is particularly useful when working with hierarchical data such as file paths, URLs, or any other delimited paths.

## Example usage

The following example request creates a new index named `my_index` and configures an analyzer with a `path_hierarchy` tokenizer:

```json
PUT /my_index
{
  "settings": {
    "analysis": {
      "tokenizer": {
        "my_path_tokenizer": {
          "type": "path_hierarchy"
        }
      },
      "analyzer": {
        "my_path_analyzer": {
          "type": "custom",
          "tokenizer": "my_path_tokenizer"
        }
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /my_index/_analyze
{
  "analyzer": "my_path_analyzer",
  "text": "/users/john/documents/report.txt"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "/users",
      "start_offset": 0,
      "end_offset": 6,
      "type": "word",
      "position": 0
    },
    {
      "token": "/users/john",
      "start_offset": 0,
      "end_offset": 11,
      "type": "word",
      "position": 0
    },
    {
      "token": "/users/john/documents",
      "start_offset": 0,
      "end_offset": 21,
      "type": "word",
      "position": 0
    },
    {
      "token": "/users/john/documents/report.txt",
      "start_offset": 0,
      "end_offset": 32,
      "type": "word",
      "position": 0
    }
  ]
}
```

## Parameters

The `path_hierarchy` tokenizer can be configured with the following parameters.

Parameter | Required/Optional | Data type | Description
:--- | :--- | :--- | :---
`delimiter` | Optional | String | Specifies the character used to separate path components. Default is `/`.
`replacement` | Optional | String | Configures the character used to replace the delimiter in the tokens. Default is `/`.
`buffer_size` | Optional | Integer | Specifies the buffer size. Default is `1024`.
`reverse` | Optional | Boolean | If `true`, generates tokens in reverse order. Default is `false`.
`skip` | Optional | Integer | Specifies the number of initial tokens (levels) to skip when tokenizing. Default is `0`.

## Example using delimiter and replacement parameters

The following example request configures custom `delimiter` and `replacement` parameters:

```json
PUT /my_index
{
  "settings": {
    "analysis": {
      "tokenizer": {
        "my_path_tokenizer": {
          "type": "path_hierarchy",
          "delimiter": "\\",
          "replacement": "\\"
        }
      },
      "analyzer": {
        "my_path_analyzer": {
          "type": "custom",
          "tokenizer": "my_path_tokenizer"
        }
      }
    }
  }
}
```

Use the following request to examine the tokens generated using the analyzer:

```json
POST /my_index/_analyze
{
  "analyzer": "my_path_analyzer",
  "text": "C:\\users\\john\\documents\\report.txt"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "C:",
      "start_offset": 0,
      "end_offset": 2,
      "type": "word",
      "position": 0
    },
    {
      "token": """C:\users""",
      "start_offset": 0,
      "end_offset": 8,
      "type": "word",
      "position": 0
    },
    {
      "token": """C:\users\john""",
      "start_offset": 0,
      "end_offset": 13,
      "type": "word",
      "position": 0
    },
    {
      "token": """C:\users\john\documents""",
      "start_offset": 0,
      "end_offset": 23,
      "type": "word",
      "position": 0
    },
    {
      "token": """C:\users\john\documents\report.txt""",
      "start_offset": 0,
      "end_offset": 34,
      "type": "word",
      "position": 0
    }
  ]
}
```
