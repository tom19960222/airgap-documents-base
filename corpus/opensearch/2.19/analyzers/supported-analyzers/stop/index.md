---
collection: "opensearch"
version: "2.19"
title: "Stop analyzer"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_analyzers/supported-analyzers/stop.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_analyzers/supported-analyzers/stop.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/analyzers/supported-analyzers/stop/"
canonical_url: "https://docs.opensearch.org/latest/analyzers/supported-analyzers/stop/"
canonical_route: "/analyzers/supported-analyzers/stop/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 110
parent: "Analyzers"
---
# Stop analyzer

The `stop` analyzer removes a predefined list of stopwords. This analyzer consists of a `lowercase` tokenizer and a `stop` token filter.

## Parameters

You can configure a `stop` analyzer with the following parameters.

Parameter | Required/Optional | Data type | Description
:--- | :--- | :--- | :---
`stopwords` | Optional | String or list of strings | A string specifying a predefined list of stopwords (such as `_english_`) or an array specifying a custom list of stopwords. Default is `_english_`.
`stopwords_path` | Optional | String | The path (absolute or relative to the config directory) to the file containing a list of stopwords.

## Example

Use the following command to create an index named `my_stop_index` with a `stop` analyzer:

```json
PUT /my_stop_index
{
  "mappings": {
    "properties": {
      "my_field": {
        "type": "text",
        "analyzer": "stop"
      }
    }
  }
}
```

## Configuring a custom analyzer

Use the following command to configure an index with a custom analyzer that is equivalent to a `stop` analyzer:

```json
PUT /my_custom_stop_analyzer_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_stop_analyzer": {
          "tokenizer": "lowercase",
          "filter": [
            "stop"
          ]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "my_field": {
        "type": "text",
        "analyzer": "my_custom_stop_analyzer"
      }
    }
  }
}
```

## Generated tokens

Use the following request to examine the tokens generated using the analyzer:

```json
POST /my_custom_stop_analyzer_index/_analyze
{
  "analyzer": "my_custom_stop_analyzer",
  "text": "The large turtle is green and brown"
}
```

The response contains the generated tokens:

```json
{
  "tokens": [
    {
      "token": "large",
      "start_offset": 4,
      "end_offset": 9,
      "type": "word",
      "position": 1
    },
    {
      "token": "turtle",
      "start_offset": 10,
      "end_offset": 16,
      "type": "word",
      "position": 2
    },
    {
      "token": "green",
      "start_offset": 20,
      "end_offset": 25,
      "type": "word",
      "position": 4
    },
    {
      "token": "brown",
      "start_offset": 30,
      "end_offset": 35,
      "type": "word",
      "position": 6
    }
  ]
}
```

# Specifying stopwords

The following example request specifies a custom list of stopwords:

```json
PUT /my_new_custom_stop_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_stop_analyzer": {
          "type": "stop",
          "stopwords": ["is", "and", "was"]
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "description": {
        "type": "text",
        "analyzer": "my_custom_stop_analyzer"
      }
    }
  }
}
```

The following example request specifies a path to the file containing stopwords:

```json
PUT /my_new_custom_stop_index
{
  "settings": {
    "analysis": {
      "analyzer": {
        "my_custom_stop_analyzer": {
          "type": "stop",
          "stopwords_path": "stopwords.txt"
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "description": {
        "type": "text",
        "analyzer": "my_custom_stop_analyzer"
      }
    }
  }
}
```

In this example, the file is located in the config directory. You can also specify a full path to the file.
