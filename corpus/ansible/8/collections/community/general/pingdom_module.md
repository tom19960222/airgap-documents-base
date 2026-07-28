---
collection: ansible
version: "8"
title: "community.general.pingdom module – Pause/unpause Pingdom alerts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pingdom_module.html
fetched_at: 2026-07-28T01:49:00+00:00
---
# community.general.pingdom module – Pause/unpause Pingdom alerts

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](pingdom_module.md#ansible-collections-community-general-pingdom-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.pingdom`.

- [Synopsis](pingdom_module.md#synopsis)
- [Requirements](pingdom_module.md#requirements)
- [Parameters](pingdom_module.md#parameters)
- [Attributes](pingdom_module.md#attributes)
- [Notes](pingdom_module.md#notes)
- [Examples](pingdom_module.md#examples)

## [Synopsis](pingdom_module.md#id1)

- This module will let you pause/unpause Pingdom alerts

Aliases: monitoring.pingdom

## [Requirements](pingdom_module.md#id2)

The below requirements are needed on the host that executes this module.

- This pingdom python library: <https://github.com/mbabineau/pingdom-python>

## [Parameters](pingdom_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **checkid**  string / required | Pingdom ID of the check. |
| **key**  string / required | Pingdom API key. |
| **passwd**  string / required | Pingdom user password. |
| **state**  string / required | Define whether or not the check should be running or paused.  **Choices:**   - `"running"` - `"paused"` - `"started"` - `"stopped"` |
| **uid**  string / required | Pingdom user ID. |

## [Attributes](pingdom_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](pingdom_module.md#id5)

> **Note:**
>
> - This module does not yet have support to add/remove checks.

## [Examples](pingdom_module.md#id6)

```yaml+jinja
- name: Pause the check with the ID of 12345
  community.general.pingdom:
    uid: example@example.com
    passwd: password123
    key: apipassword123
    checkid: 12345
    state: paused

- name: Unpause the check with the ID of 12345
  community.general.pingdom:
    uid: example@example.com
    passwd: password123
    key: apipassword123
    checkid: 12345
    state: running
```

### Authors

- Dylan Silva (@thaumos)
- Justin Johns

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
