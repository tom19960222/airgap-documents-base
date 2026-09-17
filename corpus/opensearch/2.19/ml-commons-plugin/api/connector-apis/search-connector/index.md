---
collection: "opensearch"
version: "2.19"
title: "Search connector"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/connector-apis/search-connector.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/connector-apis/search-connector.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/connector-apis/search-connector/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/connector-apis/search-connector/"
canonical_route: "/ml-commons-plugin/api/connector-apis/search-connector/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 25
parent: "Connector APIs"
---
# Search for a connector

Use the `_search` endpoint to search for a connector. This API uses a query to search for matching connectors.

## Endpoints

```json
POST /_plugins/_ml/connectors/_search
GET /_plugins/_ml/connectors/_search
```

#### Example request

```json
POST /_plugins/_ml/connectors/_search
{
  "query": {
    "match_all": {}
  },
  "size": 1000
}
```

#### Example response

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
      "value" : 3,
      "relation" : "eq"
    },
    "max_score" : 1.0,
    "hits" : [
      {
        "_index" : ".plugins-ml-connector",
        "_id" : "7W-d74sBPD67W0wkEZdE",
        "_version" : 1,
        "_seq_no" : 2,
        "_primary_term" : 1,
        "_score" : 1.0,
        "_source" : {
          "protocol" : "aws_sigv4",
          "name" : "BedRock claude Connector",
          "description" : "The connector to BedRock service for claude model",
          "version" : "1",
          "parameters" : {
            "endpoint" : "bedrock.us-east-1.amazonaws.com",
            "content_type" : "application/json",
            "auth" : "Sig_V4",
            "max_tokens_to_sample" : "8000",
            "service_name" : "bedrock",
            "temperature" : "1.0E-4",
            "response_filter" : "$.completion",
            "region" : "us-east-1",
            "anthropic_version" : "bedrock-2023-05-31"
          },
          "actions" : [
            {
              "headers" : {
                "x-amz-content-sha256" : "required",
                "content-type" : "application/json"
              },
              "method" : "POST",
              "request_body" : "{\"prompt\":\"${parameters.prompt}\", \"max_tokens_to_sample\":${parameters.max_tokens_to_sample}, \"temperature\":${parameters.temperature},  \"anthropic_version\":\"${parameters.anthropic_version}\" }",
              "action_type" : "PREDICT",
              "url" : "https://bedrock.us-east-1.amazonaws.com/model/anthropic.claude-v2/invoke"
            }
          ]
        }
      },
      {
        "_index" : ".plugins-ml-connector",
        "_id" : "9W-d74sBPD67W0wk4pf_",
        "_version" : 1,
        "_seq_no" : 3,
        "_primary_term" : 1,
        "_score" : 1.0,
        "_source" : {
          "protocol" : "aws_sigv4",
          "name" : "BedRock claude Connector",
          "description" : "The connector to BedRock service for claude model",
          "version" : "1",
          "parameters" : {
            "endpoint" : "bedrock.us-east-1.amazonaws.com",
            "content_type" : "application/json",
            "auth" : "Sig_V4",
            "max_tokens_to_sample" : "8000",
            "service_name" : "bedrock",
            "temperature" : "1.0E-4",
            "response_filter" : "$.completion",
            "region" : "us-east-1",
            "anthropic_version" : "bedrock-2023-05-31"
          },
          "actions" : [
            {
              "headers" : {
                "x-amz-content-sha256" : "required",
                "content-type" : "application/json"
              },
              "method" : "POST",
              "request_body" : "{\"prompt\":\"${parameters.prompt}\", \"max_tokens_to_sample\":${parameters.max_tokens_to_sample}, \"temperature\":${parameters.temperature},  \"anthropic_version\":\"${parameters.anthropic_version}\" }",
              "action_type" : "PREDICT",
              "url" : "https://bedrock.us-east-1.amazonaws.com/model/anthropic.claude-v2/invoke"
            }
          ]
        }
      },
      {
        "_index" : ".plugins-ml-connector",
        "_id" : "rm_u8osBPD67W0wkCpsG",
        "_version" : 1,
        "_seq_no" : 4,
        "_primary_term" : 1,
        "_score" : 1.0,
        "_source" : {
          "protocol" : "aws_sigv4",
          "name" : "BedRock Claude-Instant v1",
          "description" : "Bedrock connector for Claude Instant testing",
          "version" : "1",
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
              "headers" : {
                "x-amz-content-sha256" : "required",
                "content-type" : "application/json"
              },
              "method" : "POST",
              "request_body" : "{\"prompt\":\"${parameters.prompt}\", \"max_tokens_to_sample\":${parameters.max_tokens_to_sample}, \"temperature\":${parameters.temperature},  \"anthropic_version\":\"${parameters.anthropic_version}\" }",
              "action_type" : "PREDICT",
              "url" : "https://bedrock-runtime.us-east-1.amazonaws.com/model/anthropic.claude-instant-v1/invoke"
            }
          ]
        }
      }
    ]
  }
}
```
