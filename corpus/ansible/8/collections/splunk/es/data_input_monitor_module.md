---
collection: ansible
version: "8"
title: "splunk.es.data_input_monitor module – Manage Splunk Data Inputs of type Monitor"
source_url: https://docs.ansible.com/projects/ansible/8/collections/splunk/es/data_input_monitor_module.html
fetched_at: 2026-07-28T02:53:49+00:00
---
# splunk.es.data_input_monitor module – Manage Splunk Data Inputs of type Monitor

> **Note:**
>
> This module is part of the [splunk.es collection](https://galaxy.ansible.com/ui/repo/published/splunk/es/) (version 2.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install splunk.es`.
>
> To use it in a playbook, specify: `splunk.es.data_input_monitor`.

New in splunk.es 1.0.0

- [DEPRECATED](data_input_monitor_module.md#deprecated)
- [Synopsis](data_input_monitor_module.md#synopsis)
- [Parameters](data_input_monitor_module.md#parameters)
- [Examples](data_input_monitor_module.md#examples)
- [Status](data_input_monitor_module.md#status)

## [DEPRECATED](data_input_monitor_module.md#id1)

Removed in:
:   major release after 2024-09-01

Why:
:   Newer and updated modules released with more functionality.

Alternative:
:   splunk_data_inputs_monitor

## [Synopsis](data_input_monitor_module.md#id2)

- This module allows for addition or deletion of File and Directory Monitor Data Inputs in Splunk.

Aliases: splunk_data_input_monitor

## [Parameters](data_input_monitor_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **blacklist**  string | Specify a regular expression for a file path. The file path that matches this regular expression is not indexed. |
| **check_index**  boolean | If set to `true`, the index value is checked to ensure that it is the name of a valid index.  **Choices:**   - `false` ← (default) - `true` |
| **check_path**  boolean | If set to `true`, the name value is checked to ensure that it exists.  **Choices:**   - `false` - `true` |
| **crc_salt**  string | A string that modifies the file tracking identity for files in this input. The magic value <SOURCE> invokes special behavior (see admin documentation). |
| **disabled**  boolean | Indicates if input monitoring is disabled.  **Choices:**   - `false` ← (default) - `true` |
| **followTail**  boolean | If set to `true`, files that are seen for the first time is read from the end.  **Choices:**   - `false` ← (default) - `true` |
| **host**  string | The value to populate in the host field for events from this data input. |
| **host_regex**  string | Specify a regular expression for a file path. If the path for a file matches this regular expression, the captured value is used to populate the host field for events from this data input. The regular expression must have one capture group. |
| **host_segment**  integer | Use the specified slash-separate segment of the filepath as the host field value. |
| **ignore_older_than**  string | Specify a time value. If the modification time of a file being monitored falls outside of this rolling time window, the file is no longer being monitored. |
| **index**  string | Which index events from this input should be stored in. Defaults to default. |
| **name**  string / required | The file or directory path to monitor on the system. |
| **recursive**  boolean | Setting this to false prevents monitoring of any subdirectories encountered within this data input.  **Choices:**   - `false` ← (default) - `true` |
| **rename_source**  string | The value to populate in the source field for events from this data input. The same source should not be used for multiple data inputs. |
| **sourcetype**  string | The value to populate in the sourcetype field for incoming events. |
| **state**  string / required | Add or remove a data source.  **Choices:**   - `"present"` - `"absent"` |
| **time_before_close**  integer | When Splunk software reaches the end of a file that is being read, the file is kept open for a minimum of the number of seconds specified in this value. After this period has elapsed, the file is checked again for more data. |
| **whitelist**  string | Specify a regular expression for a file path. Only file paths that match this regular expression are indexed. |

## [Examples](data_input_monitor_module.md#id4)

```yaml+jinja
- name: Example adding data input monitor with splunk.es.data_input_monitor
  splunk.es.data_input_monitor:
    name: "/var/log/example.log"
    state: "present"
    recursive: true
```

## [Status](data_input_monitor_module.md#id5)

- This module will be removed in a major release after 2024-09-01.
  *[deprecated]*
- For more information see [DEPRECATED](data_input_monitor_module.md#deprecated).

### Authors

- Ansible Security Automation Team (@maxamillion) <<https://github.com/ansible-security>>

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/splunk.es/issues)
- [Repository (Sources)](https://github.com/ansible-collections/splunk.es)
