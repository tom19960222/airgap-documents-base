---
collection: ansible
version: "8"
title: "ibm.qradar.log_source_management module – Manage Log Sources in QRadar"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/qradar/log_source_management_module.html
fetched_at: 2026-07-28T02:34:32+00:00
---
# ibm.qradar.log_source_management module – Manage Log Sources in QRadar

> **Note:**
>
> This module is part of the [ibm.qradar collection](https://galaxy.ansible.com/ui/repo/published/ibm/qradar/) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.qradar`.
>
> To use it in a playbook, specify: `ibm.qradar.log_source_management`.

New in ibm.qradar 1.0.0

- [DEPRECATED](log_source_management_module.md#deprecated)
- [Synopsis](log_source_management_module.md#synopsis)
- [Parameters](log_source_management_module.md#parameters)
- [Notes](log_source_management_module.md#notes)
- [Examples](log_source_management_module.md#examples)
- [Status](log_source_management_module.md#status)

## [DEPRECATED](log_source_management_module.md#id1)

Removed in:
:   major release after 2024-09-01

Why:
:   Newer and updated modules released with more functionality.

Alternative:
:   qradar_log_sources_management

## [Synopsis](log_source_management_module.md#id2)

- This module allows for addition, deletion, or modification of Log Sources in QRadar

Aliases: qradar_log_source_management

## [Parameters](log_source_management_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string / required | Description of log source |
| **identifier**  string / required | Log Source Identifier (Typically IP Address or Hostname of log source) |
| **name**  string / required | Name of Log Source |
| **protocol_type_id**  integer | Type of protocol by id, as defined in QRadar Log Source Types Documentation |
| **state**  string / required | Add or remove a log source.  **Choices:**   - `"present"` - `"absent"` |
| **type_id**  integer | Type of resource by id, as defined in QRadar Log Source Types Documentation |
| **type_name**  string | Type of resource by name |

## [Notes](log_source_management_module.md#id4)

> **Note:**
>
> - Either `type` or `type_id` is required

## [Examples](log_source_management_module.md#id5)

```yaml+jinja
- name: Add a snort log source to IBM QRadar
  ibm.qradar.log_source_management:
    name: "Snort logs"
    type_name: "Snort Open Source IDS"
    state: present
    description: "Snort IDS remote logs from rsyslog"
    identifier: "192.168.1.101"
```

## [Status](log_source_management_module.md#id6)

- This module will be removed in a major release after 2024-09-01.
  *[deprecated]*
- For more information see [DEPRECATED](log_source_management_module.md#deprecated).

### Authors

- Ansible Security Automation Team (@maxamillion) <<https://github.com/ansible-security>>

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.qradar/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.qradar)
