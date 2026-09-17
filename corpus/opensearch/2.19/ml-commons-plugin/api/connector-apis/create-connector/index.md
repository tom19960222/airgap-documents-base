---
collection: "opensearch"
version: "2.19"
title: "Create connector"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/connector-apis/create-connector.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/connector-apis/create-connector.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/connector-apis/create-connector/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/connector-apis/create-connector/"
canonical_route: "/ml-commons-plugin/api/connector-apis/create-connector/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "ML Commons APIs"
layout: "default"
nav_order: 10
parent: "Connector APIs"
---
# Create a connector

Creates a standalone connector. For more information, see [Connectors](../../../remote-models/connectors/index.md).

## Endpoints

```json
POST /_plugins/_ml/connectors/_create
```

## Request body fields

For a list of request fields, see [Blueprint configuration parameters](../../../remote-models/blueprints/index.md#configuration-parameters).

#### Example request

To create a standalone connector, send a request to the `connectors/_create` endpoint and provide all of the parameters described in [Connector blueprints](../../../remote-models/blueprints/index.md):

```json
POST /_plugins/_ml/connectors/_create
{
    "name": "OpenAI Chat Connector",
    "description": "The connector to public OpenAI model service for GPT 3.5",
    "version": 1,
    "protocol": "http",
    "parameters": {
        "endpoint": "api.openai.com",
        "model": "gpt-3.5-turbo"
    },
    "credential": {
        "openAI_key": "..."
    },
    "actions": [
        {
            "action_type": "predict",
            "method": "POST",
            "url": "https://${parameters.endpoint}/v1/chat/completions",
            "headers": {
                "Authorization": "Bearer ${credential.openAI_key}"
            },
            "request_body": "{ \"model\": \"${parameters.model}\", \"messages\": ${parameters.messages} }"
        }
    ]
}
```

#### Example response

```json
{
  "connector_id": "a1eMb4kBJ1eYAeTMAljY"
}
```
