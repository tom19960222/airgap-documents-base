---
collection: "opensearch"
version: "2.19"
title: "Render Template"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_api-reference/render-template.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_api-reference/render-template.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/api-reference/render-template/"
canonical_url: "https://docs.opensearch.org/latest/api-reference/search-apis/search-template/render-template/"
canonical_route: "/api-reference/search-apis/search-template/render-template/"
redirect_from: ["/api-reference/search-apis/render-template/","/api-reference/search-apis/search-template/render-template/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
layout: "default"
nav_order: 82
---
# Render Template

The Render Template API renders a [search template](../search-template/index.md) as a search query.

## Paths and HTTP methods

```json
GET /_render/template
POST /_render/template
GET /_render/template/<id>
POST /_render/template/<id>
```

## Path parameters

The Render Template API supports the following optional path parameter.

| Parameter | Type | Description |
| :--- | :--- | :--- |
| `id` | String | The ID of the search template to render. |

## Request body fields

The following options are supported in the request body of the Render Template API.

| Parameter | Required | Type | Description |
| :--- | :--- | :--- | :--- |
| `id` | Conditional | String | The ID of the search template to render. Is not required if the ID is provided in the path or if an inline template is specified by the `source`. |
| `params` | No | Object | A list of key-value pairs that replace Mustache variables found in the search template. The key-value pairs must exist in the documents being searched. |
| `source` | Conditional | Object | An inline search template to render if a search template is not specified. Supports the same parameters as a [Search](../search/index.md) API request and [Mustache](https://mustache.github.io/mustache.5.html) variables. |

## Example request

Both of the following request examples use the search template with the template ID `play_search_template`:

```json
{
  "source": {
    "query": {
      "match": {
        "play_name": "{{play_name}}"
      }
    }
  },
  "params": {
    "play_name": "Henry IV"
  }
}
```

### Render template using template ID

The following example request validates a search template with the ID `play_search_template`:

```json
POST _render/template
{
  "id": "play_search_template",
  "params": {
    "play_name": "Henry IV"
  }
}
```

### Render template using `_source`

If you don't want to use a saved template, or want to test a template before saving, you can test a template with the `_source` parameter using [Mustache](https://mustache.github.io/mustache.5.html) variables, as shown in the following example:

```
{
  "source": {
     "from": "{{from}}{{^from}}0{{/from}}",
     "size": "{{size}}{{^size}}10{{/size}}",
    "query": {
      "match": {
        "play_name": "{{play_name}}"
      }
    }
  },
  "params": {
    "play_name": "Henry IV"
  }
}
```

## Example response

OpenSearch responds with information about the template's output:

```json
{
  "template_output": {
    "from": "0",
    "size": "10",
    "query": {
      "match": {
        "play_name": "Henry IV"
      }
    }
  }
}
```
