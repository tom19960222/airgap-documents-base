---
collection: "opensearch"
version: "2.19"
title: "Personalize search ranking"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/search-pipelines/personalize-search-ranking.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/search-pipelines/personalize-search-ranking.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/search-pipelines/personalize-search-ranking/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/search-pipelines/personalize-search-ranking/"
canonical_route: "/search-plugins/search-pipelines/personalize-search-ranking/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Search pipelines"
has_children: false
layout: "default"
nav_order: 85
parent: "Search processors"
---
# Personalize search ranking processor
Introduced 2.9
{: .label .label-purple }

The `personalize_search_ranking` search response processor intercepts a search response and uses [Amazon Personalize](https://aws.amazon.com/personalize/) to rerank search results according to their Amazon Personalize ranking. This ranking is based on the user's past behavior and metadata about the search items and the user.

To use the `personalize_search_ranking` processor, you must first install the Amazon Personalize Search Ranking (`opensearch-search-processor`) plugin. For detailed instructions, see [Installing and configuring the Amazon Personalize Search Ranking plugin](https://docs.aws.amazon.com/personalize/latest/dg/opensearch-install.html).
{: .important}

## Request body fields

The following table lists all available request fields.

Field | Data type | Description
:--- | :--- | :---
`campaign_arn` | String |  The Amazon Resource Name (ARN) of the Amazon Personalize campaign used to personalize results. Required.
`recipe` | String | The name of the Amazon Personalize recipe to use. Currently, the only supported value for this field is `aws-personalized-ranking`. Required.
`weight` | Float | The weight to use with rankings provided by OpenSearch and Amazon Personalize. Valid values are in the [0.0, 1.0] range. The closer the weight is to 1.0, the more weight is given to Amazon Personalize as opposed to OpenSearch when calculating the ranking. If you specify 0.0, OpenSearch rankings are used. If you specify 1.0, Amazon Personalize rankings are used. Required.
`item_id_field` | String | If the `_id` field for an indexed document in OpenSearch doesn't correspond with your Amazon Personalize `itemId`, specify the name of the field that does. By default, the plugin assumes the `_id` data matches the `itemId` in your Amazon Personalize data.
`iam_role_arn` | String | If you use multiple roles to restrict permissions for different groups of users in your organization, specify the ARN of the role that has permission to access Amazon Personalize. If you use only the AWS credentials in your OpenSearch keystore, you can omit this field. Optional.
`tag` | String | The processor's identifier. Optional.
`description` | String | A description of the processor. Optional.
`ignore_failure` | Boolean | If `true`, OpenSearch [ignores any failure](../creating-search-pipeline/index.md#ignoring-processor-failures) of this processor and continues to run the remaining processors in the search pipeline. Optional. Default is `false`.

## Example

The following example demonstrates using a search pipeline with a `personalize_search_ranking` processor.

### Creating a search pipeline

The following request creates a search pipeline with a `personalize_search_ranking` response processor:

```json
PUT /_search/pipeline/my-pipeline
{
  "description": "A pipeline to apply custom reranking from Amazon Personalize",
  "response_processors" : [
    {
      "personalized_search_ranking" : {
        "campaign_arn" : "Amazon Personalize Campaign ARN",
        "item_id_field" : "productId",
        "recipe" : "aws-personalized-ranking",
        "weight" : "0.3",
        "tag" : "personalize-processor",
        "iam_role_arn": "Role ARN",
        "aws_region": "AWS region"
      }
    }
  ]
}
```

### Using a search pipeline

To search with a pipeline, specify the pipeline name in the `search_pipeline` query parameter. For example, the following request searches for comedies using the pipeline set up in the previous section:

```json
GET /movies/_search?search_pipeline=my-pipeline
{
  "query": {
    "multi_match": {
      "query": "Comedy",
      "fields": ["GENRES"]
    }
  },
  "ext": {
    "personalize_request_parameters": {
      "user_id": "user ID",
      "context": { "DEVICE" : "mobile phone" }
    }
  }
}
```

For additional details, see [Personalizing search results from OpenSearch (self-managed)](https://docs.aws.amazon.com/personalize/latest/dg/personalize-opensearch.html).
