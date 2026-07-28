---
collection: ansible
version: "8"
title: "ibm.qradar.offense_action module – Take action on a QRadar Offense"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/qradar/offense_action_module.html
fetched_at: 2026-07-28T02:34:32+00:00
---
# ibm.qradar.offense_action module – Take action on a QRadar Offense

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
> To use it in a playbook, specify: `ibm.qradar.offense_action`.

New in ibm.qradar 1.0.0

- [Synopsis](offense_action_module.md#synopsis)
- [Parameters](offense_action_module.md#parameters)
- [Notes](offense_action_module.md#notes)
- [Examples](offense_action_module.md#examples)

## [Synopsis](offense_action_module.md#id1)

- This module allows to assign, protect, follow up, set status, and assign closing reason to QRadar Offenses

Aliases: qradar_offense_action

## [Parameters](offense_action_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **assigned_to**  string | Assign to an user, the QRadar username should be provided |
| **closing_reason**  string | Assign a predefined closing reason here, by name. |
| **closing_reason_id**  integer | Assign a predefined closing reason here, by id. |
| **follow_up**  boolean | Set or unset the flag to follow up on a QRadar Offense  **Choices:**   - `false` - `true` |
| **id**  integer / required | ID of Offense |
| **protected**  boolean | Set or unset the flag to protect a QRadar Offense  **Choices:**   - `false` - `true` |
| **status**  string | One of “open”, “hidden” or “closed”. (Either all lower case or all caps)  **Choices:**   - `"open"` - `"OPEN"` - `"hidden"` - `"HIDDEN"` - `"closed"` - `"CLOSED"` |

## [Notes](offense_action_module.md#id3)

> **Note:**
>
> - Requires one of `name` or `id` be provided
> - Only one of `closing_reason` or `closing_reason_id` can be provided

## [Examples](offense_action_module.md#id4)

```yaml+jinja

```

### Authors

- Ansible Security Automation Team (@maxamillion) <<https://github.com/ansible-security>>

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.qradar/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.qradar)
