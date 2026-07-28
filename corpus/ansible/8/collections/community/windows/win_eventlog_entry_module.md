---
collection: ansible
version: "8"
title: "community.windows.win_eventlog_entry module – Write entries to Windows event logs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_eventlog_entry_module.html
fetched_at: 2026-07-28T02:01:52+00:00
---
# community.windows.win_eventlog_entry module – Write entries to Windows event logs

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_eventlog_entry`.

- [Synopsis](win_eventlog_entry_module.md#synopsis)
- [Parameters](win_eventlog_entry_module.md#parameters)
- [Notes](win_eventlog_entry_module.md#notes)
- [See Also](win_eventlog_entry_module.md#see-also)
- [Examples](win_eventlog_entry_module.md#examples)

## [Synopsis](win_eventlog_entry_module.md#id1)

- Write log entries to a given event log from a specified source.

## [Parameters](win_eventlog_entry_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **category**  integer | A numeric task category associated with the category message file for the log source. |
| **entry_type**  string | Indicates the entry being written to the log is of a specific type.  **Choices:**   - `"Error"` - `"FailureAudit"` - `"Information"` - `"SuccessAudit"` - `"Warning"` |
| **event_id**  integer / required | The numeric event identifier for the entry.  Value must be between 0 and 65535. |
| **log**  string / required | Name of the event log to write an entry to. |
| **message**  string / required | The message for the given log entry. |
| **raw_data**  string | Binary data associated with the log entry.  Value must be a comma-separated array of 8-bit unsigned integers (0 to 255). |
| **source**  string / required | Name of the log source to indicate where the entry is from. |

## [Notes](win_eventlog_entry_module.md#id3)

> **Note:**
>
> - This module will always report a change when writing an event entry.

## [See Also](win_eventlog_entry_module.md#id4)

> **See also:**
>
> [community.windows.win_eventlog](win_eventlog_module.md#ansible-collections-community-windows-win-eventlog-module)
> :   Manage Windows event logs.

## [Examples](win_eventlog_entry_module.md#id5)

```yaml+jinja
- name: Write an entry to a Windows event log
  community.windows.win_eventlog_entry:
    log: MyNewLog
    source: NewLogSource1
    event_id: 1234
    message: This is a test log entry.

- name: Write another entry to a different Windows event log
  community.windows.win_eventlog_entry:
    log: AnotherLog
    source: MyAppSource
    event_id: 5000
    message: An error has occurred.
    entry_type: Error
    category: 5
    raw_data: 10,20
```

### Authors

- Andrew Saraceni (@andrewsaraceni)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
