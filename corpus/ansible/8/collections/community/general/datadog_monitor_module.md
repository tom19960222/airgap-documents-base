---
collection: ansible
version: "8"
title: "community.general.datadog_monitor module – Manages Datadog monitors"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/datadog_monitor_module.html
fetched_at: 2026-07-28T01:45:19+00:00
---
# community.general.datadog_monitor module – Manages Datadog monitors

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](datadog_monitor_module.md#ansible-collections-community-general-datadog-monitor-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.datadog_monitor`.

- [Synopsis](datadog_monitor_module.md#synopsis)
- [Requirements](datadog_monitor_module.md#requirements)
- [Parameters](datadog_monitor_module.md#parameters)
- [Attributes](datadog_monitor_module.md#attributes)
- [Examples](datadog_monitor_module.md#examples)

## [Synopsis](datadog_monitor_module.md#id1)

- Manages monitors within Datadog.
- Options as described on <https://docs.datadoghq.com/api/>.

Aliases: monitoring.datadog.datadog_monitor

## [Requirements](datadog_monitor_module.md#id2)

The below requirements are needed on the host that executes this module.

- datadog

## [Parameters](datadog_monitor_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string  *added in community.general 0.2.0* | The URL to the Datadog API. Default value is `https://api.datadoghq.com`.  This value can also be set with the `DATADOG_HOST` environment variable. |
| **api_key**  string / required | Your Datadog API key. |
| **app_key**  string / required | Your Datadog app key. |
| **escalation_message**  string | A message to include with a re-notification. Supports the [‘@username](mailto:'%40username)’ notification we allow elsewhere.  Not applicable if `renotify_interval=none`. |
| **evaluation_delay**  string | Time to delay evaluation (in seconds).  Effective for sparse values. |
| **id**  string | The ID of the alert.  If set, will be used instead of the name to locate the alert. |
| **include_tags**  boolean  *added in community.general 1.3.0* | Whether notifications from this monitor automatically inserts its triggering tags into the title.  **Choices:**   - `false` - `true` ← (default) |
| **locked**  boolean | Whether changes to this monitor should be restricted to the creator or admins.  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | The name of the alert. |
| **new_host_delay**  string | A positive integer representing the number of seconds to wait before evaluating the monitor for new hosts.  This gives the host time to fully initialize. |
| **no_data_timeframe**  string | The number of minutes before a monitor will notify when data stops reporting.  Must be at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks.  If not specified, it defaults to 2x timeframe for metric, 2 minutes for service. |
| **notification_message**  string | A message to include with notifications for this monitor.  Email notifications can be sent to specific users by using the same [‘@username](mailto:'%40username)’ notation as events.  Monitor message template variables can be accessed by using double square brackets, i.e ‘[[’ and ‘]]’. |
| **notification_preset_name**  string  *added in community.general 7.1.0* | Toggles the display of additional content sent in the monitor notification.  **Choices:**   - `"show_all"` - `"hide_query"` - `"hide_handles"` - `"hide_all"` |
| **notify_audit**  boolean | Whether tagged users will be notified on changes to this monitor.  **Choices:**   - `false` ← (default) - `true` |
| **notify_no_data**  boolean | Whether this monitor will notify when data stops reporting.  **Choices:**   - `false` ← (default) - `true` |
| **priority**  integer  *added in community.general 4.6.0* | Integer from 1 (high) to 5 (low) indicating alert severity. |
| **query**  string | The monitor query to notify on.  Syntax varies depending on what type of monitor you are creating. |
| **renotify_interval**  string | The number of minutes after the last notification before a monitor will re-notify on the current status.  It will only re-notify if it is not resolved. |
| **renotify_occurrences**  integer  *added in community.general 7.1.0* | The number of times re-notification messages should be sent on the current status at the provided re-notification interval. |
| **renotify_statuses**  list / elements=string  *added in community.general 7.1.0* | The types of monitor statuses for which re-notification messages are sent.  **Choices:**   - `"alert"` - `"warn"` - `"no data"` |
| **require_full_window**  boolean | Whether this monitor needs a full window of data before it gets evaluated.  We highly recommend you set this to False for sparse metrics, otherwise some evaluations will be skipped.  **Choices:**   - `false` - `true` |
| **silenced**  dictionary | Dictionary of scopes to silence, with timestamps or None.  Each scope will be muted until the given POSIX timestamp or forever if the value is None. |
| **state**  string / required | The designated state of the monitor.  **Choices:**   - `"present"` - `"absent"` - `"mute"` - `"unmute"` |
| **tags**  list / elements=string | A list of tags to associate with your monitor when creating or updating.  This can help you categorize and filter monitors. |
| **thresholds**  dictionary | A dictionary of thresholds by status.  Only available for service checks and metric alerts.  Because each of them can have multiple thresholds, we do not define them directly in the query.  If not specified, it defaults to: `{'ok': 1, 'critical': 1, 'warning': 1}`. |
| **timeout_h**  string | The number of hours of the monitor not reporting data before it will automatically resolve from a triggered state. |
| **type**  string | The type of the monitor.  The types `query alert`, `trace-analytics alert` and `rum alert` were added in community.general 2.1.0.  The type `composite` was added in community.general 3.4.0.  The type `event-v2 alert` was added in community.general 4.8.0.  **Choices:**   - `"metric alert"` - `"service check"` - `"event alert"` - `"event-v2 alert"` - `"process alert"` - `"log alert"` - `"query alert"` - `"trace-analytics alert"` - `"rum alert"` - `"composite"` |

## [Attributes](datadog_monitor_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](datadog_monitor_module.md#id5)

```yaml+jinja
- name: Create a metric monitor
  community.general.datadog_monitor:
    type: "metric alert"
    name: "Test monitor"
    state: "present"
    renotify_interval: 30
    renotify_occurrences: 1
    renotify_statuses: ["warn"]
    notification_preset_name: "show_all"
    query: "datadog.agent.up.over('host:host1').last(2).count_by_status()"
    notification_message: "Host [[host.name]] with IP [[host.ip]] is failing to report to datadog."
    api_key: "9775a026f1ca7d1c6c5af9d94d9595a4"
    app_key: "87ce4a24b5553d2e482ea8a8500e71b8ad4554ff"

- name: Deletes a monitor
  community.general.datadog_monitor:
    name: "Test monitor"
    state: "absent"
    api_key: "9775a026f1ca7d1c6c5af9d94d9595a4"
    app_key: "87ce4a24b5553d2e482ea8a8500e71b8ad4554ff"

- name: Mutes a monitor
  community.general.datadog_monitor:
    name: "Test monitor"
    state: "mute"
    silenced: '{"*":None}'
    api_key: "9775a026f1ca7d1c6c5af9d94d9595a4"
    app_key: "87ce4a24b5553d2e482ea8a8500e71b8ad4554ff"

- name: Unmutes a monitor
  community.general.datadog_monitor:
    name: "Test monitor"
    state: "unmute"
    api_key: "9775a026f1ca7d1c6c5af9d94d9595a4"
    app_key: "87ce4a24b5553d2e482ea8a8500e71b8ad4554ff"

- name: Use datadoghq.eu platform instead of datadoghq.com
  community.general.datadog_monitor:
    name: "Test monitor"
    state: "absent"
    api_host: https://api.datadoghq.eu
    api_key: "9775a026f1ca7d1c6c5af9d94d9595a4"
    app_key: "87ce4a24b5553d2e482ea8a8500e71b8ad4554ff"
```

### Authors

- Sebastian Kornehl (@skornehl)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
