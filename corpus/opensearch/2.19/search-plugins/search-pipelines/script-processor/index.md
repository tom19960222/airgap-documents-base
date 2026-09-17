---
collection: "opensearch"
version: "2.19"
title: "Script"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/search-pipelines/script-processor.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/search-pipelines/script-processor.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/search-pipelines/script-processor/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/search-pipelines/script-processor/"
canonical_route: "/search-plugins/search-pipelines/script-processor/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Search pipelines"
has_children: false
layout: "default"
nav_order: 120
parent: "Search processors"
---
# Script processor
Introduced 2.8
{: .label .label-purple }

The `script` search request processor intercepts a search request and adds an inline Painless script that is run on incoming requests. The script can only run on the following request fields:

- `from`
- `size`
- `explain`
- `version`
- `seq_no_primary_term`
- `track_scores`
- `track_total_hits`
- `min_score`
- `terminate_after`
- `profile`

For request field definitions, see [search request fields](../../../api-reference/search/index.md#request-body).

## Request body fields

The following table lists all available request fields.

Field | Data type | Description
:--- | :--- | :---
`source` | Inline script | The script to run. Required.
`lang` | String | The script language. Optional. Only `painless` is supported.
`tag` | String | The processor's identifier. Optional.
`description` | String | A description of the processor. Optional.
`ignore_failure` | Boolean | If `true`, OpenSearch [ignores any failure](../creating-search-pipeline/index.md#ignoring-processor-failures) of this processor and continues to run the remaining processors in the search pipeline. Optional. Default is `false`.

## Example

The following request creates a search pipeline with a `script` request processor. The script limits score explanation to only one document because `explain` is an expensive operation:

```json
PUT /_search/pipeline/explain_one_result
{
  "description": "A pipeline to limit the explain operation to one result only",
  "request_processors": [
    {
      "script": {
        "lang": "painless",
        "source": "if (ctx._source['size'] > 1) { ctx._source['explain'] = false } else { ctx._source['explain'] = true }"
      }
    }
  ]
}
```
