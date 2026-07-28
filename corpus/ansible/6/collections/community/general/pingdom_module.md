---
collection: ansible
version: "6"
title: "community.general.pingdom module – Pause/unpause Pingdom alerts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pingdom_module.html
fetched_at: 2026-07-27T17:11:51+00:00
---
# community.general.pingdom module – Pause/unpause Pingdom alerts

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
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
- [Notes](pingdom_module.md#notes)
- [Examples](pingdom_module.md#examples)

## [Synopsis](pingdom_module.md#id1)

- This module will let you pause/unpause Pingdom alerts

## [Requirements](pingdom_module.md#id2)

The below requirements are needed on the host that executes this module.

- This pingdom python library: <https://github.com/mbabineau/pingdom-python>

## [Parameters](pingdom_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **checkid**  string / required | Pingdom ID of the check. |
| **key**  string / required | Pingdom API key. |
| **passwd**  string / required | Pingdom user password. |
| **state**  string / required | Define whether or not the check should be running or paused.  Choices:   - `"running"` - `"paused"` - `"started"` - `"stopped"` |
| **uid**  string / required | Pingdom user ID. |

## [Notes](pingdom_module.md#id4)

> **Note:**
>
> - This module does not yet have support to add/remove checks.

## [Examples](pingdom_module.md#id5)

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

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
