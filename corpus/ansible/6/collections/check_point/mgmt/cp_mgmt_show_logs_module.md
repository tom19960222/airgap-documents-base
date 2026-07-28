---
collection: ansible
version: "6"
title: "check_point.mgmt.cp_mgmt_show_logs module – Showing logs according to the given filter."
source_url: https://docs.ansible.com/projects/ansible/6/collections/check_point/mgmt/cp_mgmt_show_logs_module.html
fetched_at: 2026-07-27T16:48:36+00:00
---
# check_point.mgmt.cp_mgmt_show_logs module – Showing logs according to the given filter.

> **Note:**
>
> This module is part of the [check_point.mgmt collection](https://galaxy.ansible.com/check_point/mgmt) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install check_point.mgmt`.
>
> To use it in a playbook, specify: `check_point.mgmt.cp_mgmt_show_logs`.

New in check_point.mgmt 2.9

- [Synopsis](cp_mgmt_show_logs_module.md#synopsis)
- [Parameters](cp_mgmt_show_logs_module.md#parameters)
- [Examples](cp_mgmt_show_logs_module.md#examples)
- [Return Values](cp_mgmt_show_logs_module.md#return-values)

## [Synopsis](cp_mgmt_show_logs_module.md#id1)

- Showing logs according to the given filter.
- All operations are performed over Web Services API.

## [Parameters](cp_mgmt_show_logs_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ignore_warnings**  boolean | Ignore warnings if exist.  Choices:   - `false` - `true` |
| **new_query**  dictionary | Running a new query. |
| **custom_end**  string | This option is only applicable when using the custom time-frame option. |
| **custom_start**  string | This option is only applicable when using the custom time-frame option. |
| **filter**  string | The filter as entered in SmartConsole/SmartView. |
| **log_servers**  list / elements=string | List of IP’s of logs servers to query. |
| **max_logs_per_request**  integer | Limit the number of logs to be retrieved. |
| **time_frame**  string | Specify the time frame to query logs.  Choices:   - `"last-7-days"` - `"last-hour"` - `"today"` - `"last-24-hours"` - `"yesterday"` - `"this-week"` - `"this-month"` - `"last-30-days"` - `"all-time"` - `"custom"` |
| **top**  dictionary | Top results configuration. |
| **count**  integer | The number of results to retrieve. |
| **field**  string | The field on which the top command is executed.  Choices:   - `"sources"` - `"destinations"` - `"services"` - `"actions"` - `"blades"` - `"origins"` - `"users"` - `"applications"` |
| **type**  string | Type of logs to return.  Choices:   - `"logs"` - `"audit"` |
| **query_id**  string | Get the next page of last run query with specified limit. |
| **version**  string | Version of checkpoint. If not given one, the latest version taken. |
| **wait_for_task**  boolean | Wait for the task to end. Such as publish task.  Choices:   - `false` - `true` ← (default) |
| **wait_for_task_timeout**  integer | How many minutes to wait until throwing a timeout error.  Default: `30` |

## [Examples](cp_mgmt_show_logs_module.md#id3)

```yaml+jinja
- name: show-logs
  cp_mgmt_show_logs:
    new_query:
      filter: blade:"Threat Emulation"
      max_logs_per_request: '2'
      time_frame: today
```

## [Return Values](cp_mgmt_show_logs_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **cp_mgmt_show_logs**  dictionary | The checkpoint show-logs output.  Returned: always. |

### Authors

- Or Soffer (@chkp-orso)

### Collection links

[Issue Tracker](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection/issues)
[Repository (Sources)](https://github.com/CheckPointSW/CheckPointAnsibleMgmtCollection)
