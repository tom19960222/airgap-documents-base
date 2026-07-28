---
collection: ansible
version: "8"
title: "community.general.installp module – Manage packages on AIX"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/installp_module.html
fetched_at: 2026-07-28T01:46:33+00:00
---
# community.general.installp module – Manage packages on AIX

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.installp`.

- [Synopsis](installp_module.md#synopsis)
- [Parameters](installp_module.md#parameters)
- [Attributes](installp_module.md#attributes)
- [Notes](installp_module.md#notes)
- [Examples](installp_module.md#examples)

## [Synopsis](installp_module.md#id1)

- Manage packages using ‘installp’ on AIX

Aliases: packaging.os.installp

## [Parameters](installp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **accept_license**  boolean | Whether to accept the license for the package(s).  **Choices:**   - `false` ← (default) - `true` |
| **name**  aliases: pkg  list / elements=string / required | One or more packages to install or remove.  Use `all` to install all packages available on informed `repository_path`. |
| **repository_path**  path | Path with AIX packages (required to install). |
| **state**  string | Whether the package needs to be present on or absent from the system.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](installp_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](installp_module.md#id4)

> **Note:**
>
> - If the package is already installed, even the package/fileset is new, the module will not install it.

## [Examples](installp_module.md#id5)

```yaml+jinja
- name: Install package foo
  community.general.installp:
    name: foo
    repository_path: /repository/AIX71/installp/base
    accept_license: true
    state: present

- name: Install bos.sysmgt that includes bos.sysmgt.nim.master, bos.sysmgt.nim.spot
  community.general.installp:
    name: bos.sysmgt
    repository_path: /repository/AIX71/installp/base
    accept_license: true
    state: present

- name: Install bos.sysmgt.nim.master only
  community.general.installp:
    name: bos.sysmgt.nim.master
    repository_path: /repository/AIX71/installp/base
    accept_license: true
    state: present

- name: Install bos.sysmgt.nim.master and bos.sysmgt.nim.spot
  community.general.installp:
    name: bos.sysmgt.nim.master, bos.sysmgt.nim.spot
    repository_path: /repository/AIX71/installp/base
    accept_license: true
    state: present

- name: Remove packages bos.sysmgt.nim.master
  community.general.installp:
    name: bos.sysmgt.nim.master
    state: absent
```

### Authors

- Kairo Araujo (@kairoaraujo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
