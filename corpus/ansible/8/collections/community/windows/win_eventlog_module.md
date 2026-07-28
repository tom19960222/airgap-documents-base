---
collection: ansible
version: "8"
title: "community.windows.win_eventlog module – Manage Windows event logs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_eventlog_module.html
fetched_at: 2026-07-28T02:01:51+00:00
---
# community.windows.win_eventlog module – Manage Windows event logs

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
> To use it in a playbook, specify: `community.windows.win_eventlog`.

- [Synopsis](win_eventlog_module.md#synopsis)
- [Parameters](win_eventlog_module.md#parameters)
- [See Also](win_eventlog_module.md#see-also)
- [Examples](win_eventlog_module.md#examples)
- [Return Values](win_eventlog_module.md#return-values)

## [Synopsis](win_eventlog_module.md#id1)

- Allows the addition, clearing and removal of local Windows event logs, and the creation and removal of sources from a given event log. Also allows the specification of settings per log and source.

## [Parameters](win_eventlog_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **category_file**  path | For one or more sources specified, the path to a custom category resource file. |
| **maximum_size**  string | The maximum size of the event log.  Value must be between 64KB and 4GB, and divisible by 64KB.  Size can be specified in KB, MB or GB (e.g. 128KB, 16MB, 2.5GB). |
| **message_file**  path | For one or more sources specified, the path to a custom event message resource file. |
| **name**  string / required | Name of the event log to manage. |
| **overflow_action**  string | The action for the log to take once it reaches its maximum size.  For `DoNotOverwrite`, all existing entries are kept and new entries are not retained.  For `OverwriteAsNeeded`, each new entry overwrites the oldest entry.  For `OverwriteOlder`, new log entries overwrite those older than the `retention_days` value.  **Choices:**   - `"DoNotOverwrite"` - `"OverwriteAsNeeded"` - `"OverwriteOlder"` |
| **parameter_file**  path | For one or more sources specified, the path to a custom parameter resource file. |
| **retention_days**  integer | The minimum number of days event entries must remain in the log.  This option is only used when `overflow_action` is `OverwriteOlder`. |
| **sources**  list / elements=string | A list of one or more sources to ensure are present/absent in the log.  When `category_file`, `message_file` and/or `parameter_file` are specified, these values are applied across all sources. |
| **state**  string | Desired state of the log and/or sources.  When `sources` is populated, state is checked for sources.  When `sources` is not populated, state is checked for the specified log itself.  If `state` is `clear`, event log entries are cleared for the target log.  **Choices:**   - `"absent"` - `"clear"` - `"present"` ← (default) |

## [See Also](win_eventlog_module.md#id3)

> **See also:**
>
> [community.windows.win_eventlog_entry](win_eventlog_entry_module.md#ansible-collections-community-windows-win-eventlog-entry-module)
> :   Write entries to Windows event logs.

## [Examples](win_eventlog_module.md#id4)

```yaml+jinja
- name: Add a new event log with two custom sources
  community.windows.win_eventlog:
    name: MyNewLog
    sources:
      - NewLogSource1
      - NewLogSource2
    state: present

- name: Change the category and message resource files used for NewLogSource1
  community.windows.win_eventlog:
    name: MyNewLog
    sources:
      - NewLogSource1
    category_file: C:\NewApp\CustomCategories.dll
    message_file: C:\NewApp\CustomMessages.dll
    state: present

- name: Change the maximum size and overflow action for MyNewLog
  community.windows.win_eventlog:
    name: MyNewLog
    maximum_size: 16MB
    overflow_action: DoNotOverwrite
    state: present

- name: Clear event entries for MyNewLog
  community.windows.win_eventlog:
    name: MyNewLog
    state: clear

- name: Remove NewLogSource2 from MyNewLog
  community.windows.win_eventlog:
    name: MyNewLog
    sources:
      - NewLogSource2
    state: absent

- name: Remove MyNewLog and all remaining sources
  community.windows.win_eventlog:
    name: MyNewLog
    state: absent
```

## [Return Values](win_eventlog_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **entries**  integer | The count of entries present in the event log.  **Returned:** success  **Sample:** `50` |
| **exists**  boolean | Whether the event log exists or not.  **Returned:** success  **Sample:** `true` |
| **maximum_size_kb**  integer | Maximum size of the log in KB.  **Returned:** success  **Sample:** `512` |
| **name**  string | The name of the event log.  **Returned:** always  **Sample:** `"MyNewLog"` |
| **overflow_action**  string | The action the log takes once it reaches its maximum size.  **Returned:** success  **Sample:** `"OverwriteOlder"` |
| **retention_days**  integer | The minimum number of days entries are retained in the log.  **Returned:** success  **Sample:** `7` |
| **sources**  list / elements=string | A list of the current sources for the log.  **Returned:** success  **Sample:** `["MyNewLog", "NewLogSource1", "NewLogSource2"]` |
| **sources_changed**  list / elements=string | A list of sources changed (e.g. re/created, removed) for the log; this is empty if no sources are changed.  **Returned:** always  **Sample:** `["NewLogSource2"]` |

### Authors

- Andrew Saraceni (@andrewsaraceni)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
