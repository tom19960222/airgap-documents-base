---
collection: "opensearch"
version: "2.19"
title: "Model APIs"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_ml-commons-plugin/api/model-apis/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_ml-commons-plugin/api/model-apis/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/ml-commons-plugin/api/model-apis/"
canonical_url: "https://docs.opensearch.org/latest/ml-commons-plugin/api/model-apis/index/"
canonical_route: "/ml-commons-plugin/api/model-apis/"
redirect_from: ["/ml-commons-plugin/api/model-apis/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 10
parent: "ML Commons APIs"
---
# Model APIs

ML Commons supports the following model-level CRUD APIs:

- [Register Model](register-model/index.md)
- [Deploy Model](deploy-model/index.md)
- [Get Model](get-model/index.md)
- [Search Model](search-model/index.md)
- [Update Model](update-model/index.md)
- [Undeploy Model](undeploy-model/index.md)
- [Delete Model](delete-model/index.md)

# Predict APIs

Predict APIs are used to invoke machine learning (ML) models. ML Commons supports the following Predict APIs:

- [Predict](../train-predict/predict/index.md)
- [Batch Predict](batch-predict/index.md) (experimental)

# Train API

The ML Commons Train API lets you train ML algorithms synchronously and asynchronously:

- [Train](../train-predict/train/index.md)

To train tasks through the API, three inputs are required:

- Algorithm name: Must be a [FunctionName](https://github.com/opensearch-project/ml-commons/blob/1.3/common/src/main/java/org/opensearch/ml/common/parameter/FunctionName.java). This determines what algorithm the ML model runs. To add a new function, see [How To Add a New Function](https://github.com/opensearch-project/ml-commons/blob/main/docs/how-to-add-new-function.md).
- Model hyperparameters: Adjust these parameters to improve model accuracy.
- Input data: The data that trains the ML model or applies it to predictions. You can input data in two ways: query against your index or use a data frame.

# Train and Predict API

The Train and Predict API lets you train and invoke the model using the same dataset:

- [Train and Predict](../train-predict/train-and-predict/index.md)

## Model access control considerations

For clusters with model access control enabled, users can perform API operations on models in model groups with specified access levels as follows:

- `public` model group: Any user.
- `restricted` model group: Only the model owner or users who share at least one backend role with the model group.
- `private` model group: Only the model owner.

For clusters with model access control disabled, any user can perform API operations on models in any model group.

Admin users can perform API operations for models in any model group.

For more information, see [Model access control](../../model-access-control/index.md).
