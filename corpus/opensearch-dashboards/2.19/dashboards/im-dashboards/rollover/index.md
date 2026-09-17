---
collection: "opensearch-dashboards"
version: "2.19"
title: "Rollover"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/im-dashboards/rollover.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/im-dashboards/rollover.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/im-dashboards/rollover/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/im-dashboards/rollover/"
canonical_route: "/dashboards/im-dashboards/rollover/"
redirect_from: ["/dashboards/admin-ui-index/rollover/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
layout: "default"
nav_order: 40
parent: "Index Management"
---
# Rollover
Introduced 2.6
{: .label .label-purple }

OpenSearch Dashboards allows you to perform an [index rollover](https://docs.opensearch.org/latest/im-plugin/ism/error-prevention/index/#rollover) <!-- unresolved-cross-corpus-link: collection=opensearch route=/im-plugin/ism/error-prevention/ --> operation with **Index Management**.

## Data streams

To perform a rollover operation on a data stream, perform the following steps:

1. Under **Index Management**, choose **Data streams**.

1. Choose **Actions**, and then choose **Roll over**, as shown in the following image.

    ![Roll over](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/rollover1.png)

1. Under **Configure source**, select the source data stream on which you want to perform the rollover operation.

1. Choose **Roll over**, as shown in the following image.

    ![Roll over](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/rollover3.png)

## Aliases

To perform a rollover operation on an alias, perform the following steps:

1. Under **Index Management**, choose **Aliases**.

1. Choose **Actions**, and then choose **Roll over**, as shown in the following image.

    ![Roll over](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/rollover2.png)

1. Under **Configure source**, select the source alias on which you want to perform the rollover operation.

1. If the alias does not contain a write index, you are prompted to assign a write index, as shown in the following image.

    ![Roll over](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/rollover4.png)

1. Under **Configure a new rollover index** and on the **Define index** pane, specify an index name and an optional index alias.

1. Under **Index settings**, specify the number of primary shards, the number of replicas, and the refresh interval, as shown in the following image.

    ![Roll over](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/rollover5.png)

1. Choose **Roll over**.
