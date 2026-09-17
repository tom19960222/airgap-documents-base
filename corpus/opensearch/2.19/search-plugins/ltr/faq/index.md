---
collection: "opensearch"
version: "2.19"
title: "Common issues"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_search-plugins/ltr/faq.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_search-plugins/ltr/faq.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/search-plugins/ltr/faq/"
canonical_url: "https://docs.opensearch.org/latest/search-plugins/ltr/faq/"
canonical_route: "/search-plugins/ltr/faq/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: false
layout: "default"
nav_order: 1000
parent: "Learning to Rank"
---
# Common issues

To make the most of Learning to Rank (LTR), consider these helpful insights.

## Negative scores

Lucene does not allow for negative query scores. This can be problematic if your raw features include negative values. To address this, confirm that your features are non-negative _before_ training your model. You can achieve this by creating normalized fields with values shifted by the minimum value or by passing the scores through a function that produces a value greater than or equal to `0`.

## Bugs

If you encounter a bug while working with the plugin, you can open an issue in the [opensearch-learning-to-rank-base repository](https://github.com/opensearch-project/opensearch-learning-to-rank-base/issues). The project team regularly investigates and resolves issues. If you are seeking general support, the issue may be closed and you may be directed to the relevant support channel(s).

## Further assistance

If you need further assistance, join the [Relevance Slack Community](https://opensourceconnections.com/slack) and participate in the #opensearch-learn-to-rank channel to receive guidance and support from the community.
