---
collection: ansible
version: "6"
title: "splunk.es.correlation_search module – Manage Splunk Enterprise Security Correlation Searches"
source_url: https://docs.ansible.com/projects/ansible/6/collections/splunk/es/correlation_search_module.html
fetched_at: 2026-07-28T00:19:56+00:00
---
# splunk.es.correlation_search module – Manage Splunk Enterprise Security Correlation Searches

> **Note:**
>
> This module is part of the [splunk.es collection](https://galaxy.ansible.com/splunk/es) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install splunk.es`.
>
> To use it in a playbook, specify: `splunk.es.correlation_search`.

New in splunk.es 1.0.0

- [DEPRECATED](correlation_search_module.md#deprecated)
- [Synopsis](correlation_search_module.md#synopsis)
- [Parameters](correlation_search_module.md#parameters)
- [Notes](correlation_search_module.md#notes)
- [Examples](correlation_search_module.md#examples)
- [Status](correlation_search_module.md#status)

## [DEPRECATED](correlation_search_module.md#id1)

Removed in:
:   major release after 2024-09-01

Why:
:   Newer and updated modules released with more functionality.

Alternative:
:   splunk_correlation_searches

## [Synopsis](correlation_search_module.md#id2)

- This module allows for creation, deletion, and modification of Splunk Enterprise Security Correlation Searches

## [Parameters](correlation_search_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **app**  string | Splunk app to associate the correlation seach with  Default: `"SplunkEnterpriseSecuritySuite"` |
| **cron_schedule**  string | Enter a cron-style schedule.  For example `'*/5 * * * *'` (every 5 minutes) or `'0 21 * * *'` (every day at 9 PM).  Real-time searches use a default schedule of `'*/5 * * * *'`.  Default: `"*/5 * * * *"` |
| **description**  string / required | Description of the coorelation search, this will populate the description field for the web console |
| **name**  string / required | Name of coorelation search |
| **schedule_priority**  string | Raise the scheduling priority of a report. Set to “Higher” to prioritize it above other searches of the same scheduling mode, or “Highest” to prioritize it above other searches regardless of mode. Use with discretion.  Choices:   - `"Default"` ← (default) - `"Higher"` - `"Highest"` |
| **schedule_window**  string | Let report run at any time within a window that opens at its scheduled run time, to improve efficiency when there are many concurrently scheduled reports. The “auto” setting automatically determines the best window width for the report.  Default: `"0"` |
| **scheduling**  string | Controls the way the scheduler computes the next execution time of a scheduled search.  Learn more: <https://docs.splunk.com/Documentation/Splunk/7.2.3/Report/Configurethepriorityofscheduledreports#Real-time_scheduling_and_continuous_scheduling>  Choices:   - `"real-time"` ← (default) - `"continuous"` |
| **search**  string / required | SPL search string |
| **state**  string / required | Add, remove, enable, or disiable a correlation search.  Choices:   - `"present"` - `"absent"` - `"enabled"` - `"disabled"` |
| **suppress_alerts**  boolean | To suppress alerts from this correlation search or not  Choices:   - `false` ← (default) - `true` |
| **throttle_fields_to_group_by**  string | Type the fields to consider for matching events for throttling. |
| **throttle_window_duration**  string | How much time to ignore other events that match the field values specified in Fields to group by. |
| **time_earliest**  string | Earliest time using relative time modifiers.  Default: `"-24h"` |
| **time_latest**  string | Latest time using relative time modifiers.  Default: `"now"` |
| **trigger_alert_when**  string | Raise the scheduling priority of a report. Set to “Higher” to prioritize it above other searches of the same scheduling mode, or “Highest” to prioritize it above other searches regardless of mode. Use with discretion.  Choices:   - `"number of events"` ← (default) - `"number of results"` - `"number of hosts"` - `"number of sources"` |
| **trigger_alert_when_condition**  string | Conditional to pass to `trigger_alert_when`  Choices:   - `"greater than"` ← (default) - `"less than"` - `"equal to"` - `"not equal to"` - `"drops by"` - `"rises by"` |
| **trigger_alert_when_value**  string | Value to pass to `trigger_alert_when`  Default: `"10"` |
| **ui_dispatch_context**  string | Set an app to use for links such as the drill-down search in a notable event or links in an email adaptive response action. If None, uses the Application Context. |

## [Notes](correlation_search_module.md#id4)

> **Note:**
>
> - The following options are not yet supported: throttle_window_duration, throttle_fields_to_group_by, and adaptive_response_actions

## [Examples](correlation_search_module.md#id5)

```yaml+jinja
- name: Example of creating a correlation search with splunk.es.coorelation_search
  splunk.es.correlation_search:
    name: "Example Coorelation Search From Ansible"
    description: "Example Coorelation Search From Ansible, description."
    search: 'source="/var/log/snort.log"'
    state: "present"
```

## [Status](correlation_search_module.md#id6)

- This module will be removed in a major release after 2024-09-01.
  *[deprecated]*
- For more information see [DEPRECATED](correlation_search_module.md#deprecated).

### Authors

- Ansible Security Automation Team (@maxamillion) <<https://github.com/ansible-security>>

### Collection links

[Issue Tracker](https://github.com/ansible-collections/splunk.es/issues)
[Repository (Sources)](https://github.com/ansible-collections/splunk.es)
