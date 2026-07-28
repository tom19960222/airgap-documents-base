---
collection: ansible
version: "6"
title: "ibm.qradar.rule_info module – Obtain information about one or many QRadar Rules, with filter options"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ibm/qradar/rule_info_module.html
fetched_at: 2026-07-27T17:50:17+00:00
---
# ibm.qradar.rule_info module – Obtain information about one or many QRadar Rules, with filter options

> **Note:**
>
> This module is part of the [ibm.qradar collection](https://galaxy.ansible.com/ibm/qradar) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.qradar`.
>
> To use it in a playbook, specify: `ibm.qradar.rule_info`.

New in ibm.qradar 1.0.0

- [DEPRECATED](rule_info_module.md#deprecated)
- [Synopsis](rule_info_module.md#synopsis)
- [Parameters](rule_info_module.md#parameters)
- [Notes](rule_info_module.md#notes)
- [Examples](rule_info_module.md#examples)
- [Status](rule_info_module.md#status)

## [DEPRECATED](rule_info_module.md#id1)

Removed in:
:   major release after 2024-09-01

Why:
:   Newer and updated modules released with more functionality.

Alternative:
:   qradar_analytics_rules

## [Synopsis](rule_info_module.md#id2)

- This module obtains information about one or many QRadar Rules, with filter options

## [Parameters](rule_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **id**  integer | Obtain only information of the Rule with provided ID |
| **name**  string | Obtain only information of the Rule that matches the provided name |
| **origin**  string | Obtain only information of Rules that are of a certain origin  Choices:   - `"SYSTEM"` - `"OVERRIDE"` - `"USER"` |
| **owner**  string | Obtain only information of Rules owned by a certain user |
| **type**  string | Obtain only information for the Rules of a certain type  Choices:   - `"EVENT"` - `"FLOW"` - `"COMMON"` - `"USER"` |

## [Notes](rule_info_module.md#id4)

> **Note:**
>
> - You may provide many filters and they will all be applied, except for `id` as that will return only the Rule identified by the unique ID provided.

## [Examples](rule_info_module.md#id5)

```yaml+jinja
- name: Get information about the Rule named "Custom Company DDoS Rule"
  ibm.qradar.rule_info:
    name: "Custom Company DDoS Rule"
  register: custom_ddos_rule_info

- name: debugging output of the custom_ddos_rule_info registered variable
  debug:
    var: custom_ddos_rule_info
```

## [Status](rule_info_module.md#id6)

- This module will be removed in a major release after 2024-09-01.
  *[deprecated]*
- For more information see [DEPRECATED](rule_info_module.md#deprecated).

### Authors

- Ansible Security Automation Team (@maxamillion) <<https://github.com/ansible-security>>”

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ibm.qradar/issues)
[Repository (Sources)](https://github.com/ansible-collections/ibm.qradar)
