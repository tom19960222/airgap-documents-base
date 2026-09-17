---
collection: "opensearch"
version: "2.19"
title: "Actions"
source_url: "https://github.com/opensearch-project/documentation-website/blob/cc01280fc1f773421cbcb409bdc8fd7beae2638e/_observing-your-data/alerting/actions.md"
fetched_at: "2026-09-10T18:32:31-04:00"
source_path: "_observing-your-data/alerting/actions.md"
source_commit: "cc01280fc1f773421cbcb409bdc8fd7beae2638e"
renderer: "jekyll/opensearch"
permalink: "/observing-your-data/alerting/actions/"
canonical_url: "https://docs.opensearch.org/latest/observing-your-data/alerting/actions/"
canonical_route: "/observing-your-data/alerting/actions/"
redirect_from: []
canonical_collision: false
source_config_opensearch_version: "2.19.6"
source_config_opensearch_dashboards_version: "2.19.6"
app_version: "2.19.3"
chart_version: ""
grand_parent: "Alerting"
layout: "default"
nav_order: 50
parent: "Monitors"
---
# Actions

Actions send notifications when trigger conditions are met. See [Notifications](../../notifications/index.md) to learn about creating notifications. If you don't want to receive notifications, don't add actions to your triggers.

## Adding actions

To add an action:

1. In the **Triggers** panel, select **Add action**.
1. Enter the action details, including action name, notification channel, and notification message body, in the **Notification** section.

    You can add variables to your messages using [Mustache templates](https://mustache.github.io/mustache.5.html). You have access to `ctx.action.name`, the name of the current action, and all [actions variables](#actions-variables).

    If your notification channel is a custom webhook that expects a particular data format, include JSON (or XML) directly in the message body:

    ```json
    { "text": "Monitor {{ctx.monitor.name}} just entered alert status. Please investigate the issue. - Trigger: {{ctx.trigger.name}} - Severity: {{ctx.trigger.severity}} - Period start: {{ctx.periodStart}} - Period end: {{ctx.periodEnd}}" }
    ```

    In the preceding example, the message content must conform to the `Content-Type` header in the [custom webhook](../../notifications/index.md).

1. If you're using a bucket-level monitor, choose whether the monitor should perform an action for each execution or for each alert.
1. (Optional) Use action throttling to limit the number of notifications you receive within a given time frame.

    For example, if a monitor checks a trigger condition every minute, you could receive one notification per minute. If you set action throttling to 60 minutes, you receive no more than one notification per hour, even if the trigger condition is met dozens of times in that hour.

1. Choose **Create**.

After an action sends a message, the content of that message has left the purview of the [Security Analytics](../../../security-analytics/index.md) plugin. Securing access to the message (for example, access to the Slack channel) is your responsibility.

#### Example message

```mustache
Monitor {{ctx.monitor.name}} just entered an alert state. Please investigate the issue.
- Trigger: {{ctx.trigger.name}}
- Severity: {{ctx.trigger.severity}}
- Period start: {{ctx.periodStart}}
- Period end: {{ctx.periodEnd}}
```

To use the `ctx.results` variable in a message, use `{{ctx.results.0}}` rather than `{{ctx.results[0]}}`. This difference is due to how Mustache handles bracket notation.
{: .note }

#### Actions variables

Variable | Data type | Description
:--- | :--- | : ---
`ctx.trigger.actions.id` | String | The action ID.
`ctx.trigger.actions.name` | String | The action name.
`ctx.trigger.actions.message_template.source` | String | The message to send in the alert.
`ctx.trigger.actions.message_template.lang` | String | The scripting language used to define the message. Must be Mustache.
`ctx.trigger.actions.throttle_enabled` | Boolean | Whether throttling is enabled for this trigger. See [adding actions](#adding-actions) for more information about throttling.
`ctx.trigger.actions.subject_template.source` | String | The message's subject in the alert.
`ctx.trigger.actions.subject_template.lang` | String | The scripting language used to define the subject. Must be Mustache.
