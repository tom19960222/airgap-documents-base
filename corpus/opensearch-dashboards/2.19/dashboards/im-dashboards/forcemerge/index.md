---
collection: "opensearch-dashboards"
version: "2.19"
title: "Force merge"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/im-dashboards/forcemerge.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/im-dashboards/forcemerge.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/im-dashboards/forcemerge/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/im-dashboards/forcemerge/"
canonical_route: "/dashboards/im-dashboards/forcemerge/"
redirect_from: ["/dashboards/admin-ui-index/forcemerge/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
layout: "default"
nav_order: 30
parent: "Index Management"
---
# Force merge
Introduced 2.6
{: .label .label-purple }

OpenSearch Dashboards allows you to perform a [force merge](https://docs.opensearch.org/latest/im-plugin/ism/error-prevention/index#force_merge) <!-- unresolved-cross-corpus-link: collection=opensearch route=/im-plugin/ism/error-prevention/ --> operation on two or more indexes with **Index Management**.

## Force merging indexes

To perform a force merge operation on two or more indexes, perform the following steps:

1. Under **Index Management**, choose **Indices**.

1. Select the indexes you want to force merge.

1. Choose **Actions**, and then choose **Force merge**, as shown in the following image.

    ![Force Merge](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/forcemerge1.png)

1. Under **Configure source index**, specify the indexes you want to force merge.

1. Optionally, under **Advanced settings** you can to choose to **Flush indices** or **Only expunge delete** and then specify the **Max number of segments** to merge to as shown in the following image.

    ![Force Merge](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/forcemerge2.png)

## Force merging data streams

To perform a force merge operation on two or more indexes, perform the following steps:

1. Under **Index Management**, choose **Data streams**.

1. Select the data streams you want to force merge.

1. Choose **Actions**, and then choose **Force merge**.

1. Under **Configure source index**, specify the data streams you want to force merge.

1. Optionally, under **Advanced settings** you can to choose to **Flush indices** or **Only expunge delete** and then specify the **Max number of segments** to merge to as shown in the following image.

    ![Force Merge](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/forcemerge2.png)
