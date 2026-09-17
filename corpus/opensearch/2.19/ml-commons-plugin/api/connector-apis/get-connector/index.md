---
collection: "opensearch"
version: "2.19"
title: "Get connector"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/connector-apis/get-connector.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/connector-apis/get-connector.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/connector-apis/get-connector/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/connector-apis/get-connector/"
canonical_route: "/ml-commons-plugin/api/connector-apis/get-connector/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 20
parent: "Connector APIs"
---
# Get a connector

This API retrieves a connector by its ID.

### Endpoints

```json
GET /_plugins/_ml/connectors/<connector_id>
```

#### Example request

```json
GET /_plugins/_ml/connectors/N8AE1osB0jLkkocYjz7D
```

#### Example response

```json
{
  "name" : "BedRock Claude-Instant v1",
  "version" : "1",
  "description" : "Bedrock connector for Claude Instant testing",
  "protocol" : "aws_sigv4",
  "parameters" : {
    "endpoint" : "bedrock.us-east-1.amazonaws.com",
    "content_type" : "application/json",
    "auth" : "Sig_V4",
    "service_name" : "bedrock",
    "region" : "us-east-1",
    "anthropic_version" : "bedrock-2023-05-31"
  },
  "actions" : [
    {
      "action_type" : "PREDICT",
      "method" : "POST",
      "url" : "https://bedrock-runtime.us-east-1.amazonaws.com/model/anthropic.claude-instant-v1/invoke",
      "headers" : {
        "x-amz-content-sha256" : "required",
        "content-type" : "application/json"
      },
      "request_body" : "{\"prompt\":\"${parameters.prompt}\", \"max_tokens_to_sample\":${parameters.max_tokens_to_sample}, \"temperature\":${parameters.temperature},  \"anthropic_version\":\"${parameters.anthropic_version}\" }"
    }
  ]
}
```
