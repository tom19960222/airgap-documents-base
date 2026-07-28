---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_syslog_files module – Configure file management syslog module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_syslog_files_module.html
fetched_at: 2026-07-27T17:55:42+00:00
---
# mellanox.onyx.onyx_syslog_files module – Configure file management syslog module

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_syslog_files`.

New in mellanox.onyx 0.2.0

- [Synopsis](onyx_syslog_files_module.md#synopsis)
- [Parameters](onyx_syslog_files_module.md#parameters)
- [Examples](onyx_syslog_files_module.md#examples)
- [Return Values](onyx_syslog_files_module.md#return-values)

## [Synopsis](onyx_syslog_files_module.md#id1)

- This module provides declarative management of syslog on Mellanox ONYX network devices.

## [Parameters](onyx_syslog_files_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **debug**  boolean | Configure settings for debug log files  Choices:   - `false` ← (default) - `true` |
| **delete_group**  string | Delete certain log files  Choices:   - `"current"` - `"oldest"` |
| **rotation**  dictionary | rotation related attributes |
| **force**  boolean | force an immediate rotation of log files  Choices:   - `false` - `true` |
| **frequency**  string | Rotate log files on a fixed time-based schedule  Choices:   - `"daily"` - `"weekly"` - `"monthly"` |
| **max_num**  integer | Sepcify max_num of old log files to keep |
| **size**  float | Rotate files when they pass max size |
| **size_pct**  float | Rotatoe files when they pass percent of HD |
| **upload_file**  string | Upload compressed log file (current or filename) |
| **upload_url**  string | upload local log files to remote host (ftp, scp, sftp, tftp) with format protocol://username[:password]@server/path |

## [Examples](onyx_syslog_files_module.md#id3)

```yaml+jinja
- name: Syslog delete old files
- onyx_syslog_files:
    delete_group: oldest
- name: Syslog upload file
- onyx_syslog_files:
    upload_url: scp://username:password@hostnamepath/filename
    upload_file: current
- name: Syslog rotation force, frequency and max number
- onyx_syslog_files:
    rotation:
        force: true
        max_num: 30
        frequency: daily
        size: 128
```

## [Return Values](onyx_syslog_files_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["logging files delete current", "logging files rotate criteria", "logging files upload current url"]` |

### Authors

- Anas Shami (@anass)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
