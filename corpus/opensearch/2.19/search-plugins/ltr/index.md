---
collection: "opensearch"
version: "2.19"
title: "Learning to Rank"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/ltr/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/ltr/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/ltr/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/ltr/index/"
canonical_route: "/search-plugins/ltr/"
redirect_from: ["/search-plugins/ltr/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
has_toc: false
layout: "default"
nav_order: 20
---
# Learning to Rank

The Learning to Rank plugin for OpenSearch enables you to use machine learning (ML) and behavioral data to fine-tune the relevance of documents. It uses models from the [XGBoost](https://xgboost.ai/) and [RankLib](https://lemurproject.org/ranklib.php) libraries. These models rescore the search results, considering query-dependent features such as click-through data or field matches, which can further improve relevance.

The term _learning to rank_ is abbreviated as LTR throughout the OpenSearch documentation when the term is used in a general sense. For the plugin developer documentation, see [opensearch-learning-to-rank-base](https://github.com/opensearch-project/opensearch-learning-to-rank-base).
{: .note}

## Getting started

The following resources can help you get started:

- If you are new to LTR, start with the [ML ranking core concepts](core-concepts/index.md) documentation.
- For a quick introduction, see the demo in [hello-ltr](https://github.com/o19s/hello-ltr).
- If you are familiar with LTR, start with the [Integrating the plugin](fits-in/index.md) documentation.
