---
collection: "opensearch"
version: "2.19"
title: "Integrating ML models"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/integrating-ml-models.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/integrating-ml-models.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/integrating-ml-models/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/integrating-ml-models/"
canonical_route: "/ml-commons-plugin/integrating-ml-models/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
external_model: [{"heading":"Externally hosted models","link":"/ml-commons-plugin/remote-models/","description":"Learn how to create connectors for models hosted on third-party platforms"}]
has_children: true
layout: "default"
local_model: [{"heading":"Pretrained models provided by OpenSearch","link":"/ml-commons-plugin/pretrained-models/","description":"Requires minimal setup and avoids the time and effort required to train a custom model"},{"heading":"Custom models","link":"/ml-commons-plugin/custom-local-models/","description":"Offers customization for your specific use case"}]
more_cards: [{"heading":"Get started with AI search","description":"Learn how to implement semantic and hybrid search in OpenSearch","link":"/vector-search/tutorials/neural-search-tutorial/"}]
nav_order: 15
---
# Integrating ML models

OpenSearch offers support for machine learning (ML) models that you can use in conjunction with k-NN search to retrieve semantically similar documents. This semantic search capability improves search relevance for your applications.

Before you get started, you'll need to [set up](../../getting-started/quickstart/index.md) and [secure](../../security/index.md) your cluster.
{: .tip}

## Choosing a model

To integrate an ML model into your search workflow, choose one of the following options.

### Local model

Upload a model to the OpenSearch cluster and use it locally. This option allows you to serve the model in your OpenSearch cluster but may require significant system resources.

<div class="card-container">

- [Pretrained models provided by OpenSearch](../pretrained-models/index.md)
  Requires minimal setup and avoids the time and effort required to train a custom model

- [Custom models](../custom-local-models/index.md)
  Offers customization for your specific use case

</div>

### Externally hosted model

Connect to a model hosted on a third-party platform. This requires more setup but allows the use of models that are already hosted on a service other than OpenSearch.

<div class="card-container">

- [Externally hosted models](../remote-models/index.md)
  Learn how to create connectors for models hosted on third-party platforms

</div>

In OpenSearch version 2.9 and later, you can integrate local and external models simultaneously within a single cluster.
{: .note}

## Tutorial

<div class="card-container">

- [Get started with AI search](../../tutorials/vector-search/neural-search-tutorial/index.md)
  Learn how to implement semantic and hybrid search in OpenSearch

</div>

## Using a model

You can use an ML model in one of the following ways:

- [Invoke a model for inference](#invoking-a-model-for-inference).
- [Use a model for search](#using-a-model-for-search).

### Invoking a model for inference

You can invoke your model by calling the [Predict API](../api/train-predict/predict/index.md). For example, testing text embedding models lets you see the vector embeddings they generate.

[Models trained](../api/train-predict/train/index.md) through the ML Commons plugin support model-based algorithms, such as k-means. After you've trained a model to your precision requirements, you can use such a model for inference. Alternatively, you can use the [Train and Predict API](../api/train-predict/train-and-predict/index.md) to test your model without having to evaluate the model's performance.

### Using a model for search

OpenSearch supports multiple search methods that integrate with ML models. For more information, see [AI search](../../vector-search/ai-search/index.md).

## Disabling a model

You can temporarily disable a model when you don't want to undeploy or delete it. Disable a model by calling the [Update Model API](../api/model-apis/update-model/index.md) and setting `is_enabled` to `false`. When you disable a model, it becomes unavailable for [Predict API](../api/train-predict/predict/index.md) requests. If you disable a model that is undeployed, the model remains disabled after deployment. You'll need to enable it in order to use it for inference.

## Rate limiting inference calls

Setting a rate limit for Predict API calls on your ML models allows you to reduce your model inference costs. You can set a rate limit for the number of Predict API calls at the following levels:

- **Model level**: Configure a rate limit for all users of the model by calling the Update Model API and specifying a `rate_limiter`. For more information, see [Update Model API](../api/model-apis/update-model/index.md).
- **User level**: Configure a rate limit for a specific user or users of the model by creating a controller. A model may be shared by multiple users; you can configure the controller to set different rate limits for different users. For more information, see [Create Controller API](../api/controller-apis/create-controller/index.md).

Model-level rate limiting applies to all users of the model. If you specify both a model-level rate limit and a user-level rate limit, the overall rate limit is set to the more restrictive of the two. For example, if the model-level limit is 2 requests per minute and the user-level limit is 4 requests per minute, the overall limit will be set to 2 requests per minute.

To set the rate limit, you must provide two inputs: the maximum number of requests and the time frame. OpenSearch uses these inputs to calculate the rate limit as the maximum number of requests divided by the time frame. For example, if you set the limit to be 4 requests per minute, the rate limit is `4 requests / 1 minute`, which is `1 request / 0.25 minutes`, or `1 request / 15 seconds`. OpenSearch processes predict requests sequentially, in a first-come-first-served manner, and will limit those requests to 1 request per 15 seconds. Imagine two users, Alice and Bob, calling the Predict API for the same model, which has a rate limit of 1 request per 15 seconds. If Alice calls the Predict API and immediately after that Bob calls the Predict API, OpenSearch processes Alice's predict request and rejects Bob's request. Once 15 seconds has passed since Alice's request, Bob can send a request again, and this request will be processed.
