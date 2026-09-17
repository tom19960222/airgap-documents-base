---
collection: "opensearch-dashboards"
version: "2.19"
title: "Notification settings"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_dashboards/im-dashboards/notifications.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_dashboards/im-dashboards/notifications.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/dashboards/im-dashboards/notifications/"
canonical_url: "https://docs.opensearch.org/latest/dashboards/im-dashboards/notifications/"
canonical_route: "/dashboards/im-dashboards/notifications/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.1"
chart_version: ""
layout: "default"
nav_order: 60
parent: "Index Management"
---
# Notification settings

You can configure global default notification settings for index operations on the **Notification settings** page. You can also configure additional notification settings for individual index operations.

## Configuring default notification settings

In the **Notification settings** interface, you can configure the default notification settings for the following index operations that may take longer to complete:

- Open
- Reindex
- Split
- Shrink
- Clone
- Force merge

To get started, from the OpenSearch Dashboards main menu, select **OpenSearch Plugins** > **Index Management**. Under **Index Management**, select **Notification settings**.

You can choose to be notified when the operation has completed or failed. Additionally, you can select the notification channels for this notification, as shown in the following image.

![Default notification settings](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/notifications.png)

If you don't have permission to view notification settings, you cannot view the default settings.
{: .note}

## Configuring notification settings for an individual operation

You can view default notification settings when you perform an indexing operation as well as set up additional notifications. For example, if you want to configure an additional notification for a reindex operation, perform the following steps:

1. Select **OpenSearch Plugins** > **Index Management**.

1. In the **Index Management** interface, select **Indices**.

1. Select the index you want to reindex.

1. Select **Reindex** from the **Actions** dropdown list.

1. After selecting all reindex options, expand **Advanced settings**. Under **Notifications**, default notifications are listed.

    If you don't have permission to view notification settings, you will not be able to view the default settings.
    {: .note}

1. To receive additional notifications, select **Send additional notifications**, as shown in the following image.

    ![Individual notification settings](https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/images/admin-ui-index/notifications-individual.png)

1. Select whether you want to be notified when the operation has failed or completed.

1. Select a channel from the **Notification channels** dropdown list. If you want to configure a new notification channel, select **Manage channels**.

    To configure a new notification channel, confirm that the `dashboards-notification` plugin is enabled in OpenSearch Dashboards.
    {: .note}

1. Select the **Reindex** button.
