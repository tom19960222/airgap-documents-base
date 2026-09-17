---
collection: "opensearch"
version: "2.19"
title: "Using ML models within OpenSearch"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/using-ml-models.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/using-ml-models.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/using-ml-models/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/using-ml-models/"
canonical_route: "/ml-commons-plugin/using-ml-models/"
redirect_from: ["/ml-commons-plugin/model-serving-framework/","/ml-commons-plugin/ml-framework/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
gpu: [{"heading":"GPU acceleration","link":"/ml-commons-plugin/gpu-acceleration/","description":"Take advantage of GPU acceleration on your ML node for better performance"}]
has_children: true
has_toc: false
layout: "default"
models: [{"heading":"Pretrained models provided by OpenSearch","link":"/ml-commons-plugin/pretrained-models/","description":"Explore OpenSearch's collection of optimized ML models for immediate use in AI applications"},{"heading":"Custom models","link":"/ml-commons-plugin/custom-local-models/","description":"Learn how to upload and serve your own ML models in OpenSearch for specialized use cases"}]
nav_order: 50
parent: "Integrating ML models"
---
# Using ML models within OpenSearch
**Introduced 2.9**
{: .label .label-purple }

To integrate machine learning (ML) models into your OpenSearch cluster, you can upload and serve them locally. Choose one of the following options.

<div class="card-container">

- [Pretrained models provided by OpenSearch](../pretrained-models/index.md)
  Explore OpenSearch's collection of optimized ML models for immediate use in AI applications

- [Custom models](../custom-local-models/index.md)
  Learn how to upload and serve your own ML models in OpenSearch for specialized use cases

</div>

For production environments, run local models on dedicated ML nodes rather than data nodes. For more information, see [Run tasks and models on ML nodes only](../cluster-settings/index.md#run-tasks-and-models-on-ml-nodes-only).
{: .important}

Running local models on the CentOS 7 operating system is not supported. Moreover, not all local models can run on all hardware and operating systems.
{: .important}

<div class="card-container">

- [GPU acceleration](../gpu-acceleration/index.md)
  Take advantage of GPU acceleration on your ML node for better performance

</div>
