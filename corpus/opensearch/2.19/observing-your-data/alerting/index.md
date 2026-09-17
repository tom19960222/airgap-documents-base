---
collection: "opensearch"
version: "2.19"
title: "Alerting"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_observing-your-data/alerting/index.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_observing-your-data/alerting/index.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/observing-your-data/alerting/"
canonical_url: "https://docs.opensearch.org/latest/observing-your-data/alerting/index/"
canonical_route: "/observing-your-data/alerting/"
redirect_from: ["/monitoring-plugins/alerting/","/observing-your-data/alerting/"]
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
has_children: true
layout: "default"
nav_order: 70
---
# Alerting

To create an alert, do the following:

- Configure a _monitor_, which is a job that runs on a defined schedule and queries OpenSearch indexes. Required.
- Configure one or more _triggers_, which define the conditions that generate events. Optional.
- Configure _actions_, which is what happens after an alert is triggered. Optional.

## Key terms

The following table lists alerting terminology commonly used in OpenSearch and throughout the Alerting documentation.

Term | Definition
:--- | :---
Monitor | Job that runs on a defined schedule and queries OpenSearch indexes. The results of these queries are then used as input for one or more triggers.
Trigger | Conditions that, if met, generate alerts. See [Triggers](triggers/index.md).
Alert | Event associated with a trigger. When an alert is created, the trigger performs actions, including sending notifications.
Action | Specific task that is performed when an alert is triggered. See [Actions](actions/index.md).
Notification | Message that is sent to users when an alert is triggered. See [Notifications](../notifications/index.md).

## Alert states

The following table lists the alert states.

State | Description
:--- | :---
Active | The alert is ongoing and unacknowledged. Alerts remain in this state until you acknowledge them, delete the trigger associated with the alert, or delete the monitor entirely. Alerts also can be moved out of the active state if the trigger condition is no longer met. For example, if an index has 4,000 documents and a trigger condition is `numOfDocs > 5000`, an active alert is generated when 3,000 documents are added to the index. If the added 3,000 documents are then deleted from the index, the alert changes to the completed state because the condition is no longer triggered.
Acknowledged | The alert is acknowledged but the root cause is not fixed.
Completed | The alert is no longer ongoing. Alerts enter this state after the corresponding trigger evaluates to `false`.
Error | An error occurred while executing the trigger---usually the result of a bad trigger or destination.
Deleted | The monitor or trigger associated with this alert was deleted while the alert was ongoing.

## Creating an alert monitor

You can follow these basic steps to create an alert monitor:

1. In the **OpenSearch Plugins** main menu, choose **Alerting**.
1. Choose **Create monitor**. See [Monitors](monitors/index.md) for more information about the monitor types.
1. Enter the **Monitor details**, including monitor type, method, and schedule.
1. Select a data source from the dropdown list.
1. Define the metrics in the Query section.
1. Add a trigger. See [Triggers](triggers/index.md) for more information about triggers.
1. Add an action. See [Actions](actions/index.md) for more information about actions.
1. Select **Create**.

Learn more about creating specific monitor types in their respective documentation.
