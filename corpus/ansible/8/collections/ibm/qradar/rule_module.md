---
collection: ansible
version: "8"
title: "ibm.qradar.rule module – Manage state of QRadar Rules, with filter options"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/qradar/rule_module.html
fetched_at: 2026-07-28T02:34:36+00:00
---
# ibm.qradar.rule module – Manage state of QRadar Rules, with filter options

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
> To use it in a playbook, specify: `ibm.qradar.rule`.

New in ibm.qradar 1.0.0

- [DEPRECATED](rule_module.md#deprecated)
- [Synopsis](rule_module.md#synopsis)
- [Parameters](rule_module.md#parameters)
- [Examples](rule_module.md#examples)
- [Status](rule_module.md#status)

## [DEPRECATED](rule_module.md#id1)

Removed in:
:   major release after 2024-09-01

Why:
:   Newer and updated modules released with more functionality.

Alternative:
:   qradar_analytics_rules

## [Synopsis](rule_module.md#id2)

- Manage state of QRadar Rules, with filter options

Aliases: qradar_rule

## [Parameters](rule_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **id**  integer | Manage state of a QRadar Rule by ID |
| **name**  string | Manage state of a QRadar Rule by name |
| **owner**  string | Manage ownership of a QRadar Rule |
| **state**  string / required | Manage state of a QRadar Rule  **Choices:**   - `"enabled"` - `"disabled"` - `"absent"` |

## [Examples](rule_module.md#id4)

```yaml+jinja
- name: Enable Rule 'Ansible Example DDoS Rule'
  qradar_rule:
    name: 'Ansible Example DDOS Rule'
    state: enabled
```

## [Status](rule_module.md#id5)

- This module will be removed in a major release after 2024-09-01.
  *[deprecated]*
- For more information see [DEPRECATED](rule_module.md#deprecated).

### Authors

- Ansible Security Automation Team (@maxamillion) <<https://github.com/ansible-security>>

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.qradar/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.qradar)
