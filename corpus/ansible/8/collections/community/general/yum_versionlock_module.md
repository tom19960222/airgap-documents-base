---
collection: ansible
version: "8"
title: "community.general.yum_versionlock module – Locks / unlocks a installed package(s) from being updated by yum package manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/yum_versionlock_module.html
fetched_at: 2026-07-28T01:51:37+00:00
---
# community.general.yum_versionlock module – Locks / unlocks a installed package(s) from being updated by yum package manager

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
> see [Requirements](yum_versionlock_module.md#ansible-collections-community-general-yum-versionlock-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.yum_versionlock`.

New in community.general 2.0.0

- [Synopsis](yum_versionlock_module.md#synopsis)
- [Requirements](yum_versionlock_module.md#requirements)
- [Parameters](yum_versionlock_module.md#parameters)
- [Attributes](yum_versionlock_module.md#attributes)
- [Notes](yum_versionlock_module.md#notes)
- [Examples](yum_versionlock_module.md#examples)
- [Return Values](yum_versionlock_module.md#return-values)

## [Synopsis](yum_versionlock_module.md#id1)

- This module adds installed packages to yum versionlock to prevent the package(s) from being updated.

Aliases: packaging.os.yum_versionlock

## [Requirements](yum_versionlock_module.md#id2)

The below requirements are needed on the host that executes this module.

- yum
- yum-versionlock

## [Parameters](yum_versionlock_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  list / elements=string / required | Package name or a list of package names with optional version or wildcards.  Specifying versions is supported since community.general 7.2.0. |
| **state**  string | If state is `present`, package(s) will be added to yum versionlock list.  If state is `absent`, package(s) will be removed from yum versionlock list.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](yum_versionlock_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](yum_versionlock_module.md#id5)

> **Note:**
>
> - Requires yum-plugin-versionlock package on the remote node.

## [Examples](yum_versionlock_module.md#id6)

```yaml+jinja
- name: Prevent Apache / httpd from being updated
  community.general.yum_versionlock:
    state: present
    name:
    - httpd

- name: Prevent Apache / httpd version 2.4.57-2 from being updated
  community.general.yum_versionlock:
    state: present
    name:
    - httpd-0:2.4.57-2.el9

- name: Prevent multiple packages from being updated
  community.general.yum_versionlock:
    state: present
    name:
    - httpd
    - nginx
    - haproxy
    - curl

- name: Remove lock from Apache / httpd to be updated again
  community.general.yum_versionlock:
    state: absent
    name: httpd
```

## [Return Values](yum_versionlock_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **packages**  list / elements=string | A list of package(s) in versionlock list.  **Returned:** success  **Sample:** `["httpd"]` |
| **state**  string | State of package(s).  **Returned:** success  **Sample:** `"present"` |

### Authors

- Florian Paul Azim Hoberg (@gyptazy)
- Amin Vakil (@aminvakil)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
