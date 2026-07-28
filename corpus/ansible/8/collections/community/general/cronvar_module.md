---
collection: ansible
version: "8"
title: "community.general.cronvar module – Manage variables in crontabs"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/cronvar_module.html
fetched_at: 2026-07-28T01:45:16+00:00
---
# community.general.cronvar module – Manage variables in crontabs

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
> see [Requirements](cronvar_module.md#ansible-collections-community-general-cronvar-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.cronvar`.

- [Synopsis](cronvar_module.md#synopsis)
- [Requirements](cronvar_module.md#requirements)
- [Parameters](cronvar_module.md#parameters)
- [Attributes](cronvar_module.md#attributes)
- [Examples](cronvar_module.md#examples)

## [Synopsis](cronvar_module.md#id1)

- Use this module to manage crontab variables.
- This module allows you to create, update, or delete cron variable definitions.

Aliases: system.cronvar

## [Requirements](cronvar_module.md#id2)

The below requirements are needed on the host that executes this module.

- cron

## [Parameters](cronvar_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | If set, create a backup of the crontab before it is modified. The location of the backup is returned in the `backup` variable by this module.  **Choices:**   - `false` ← (default) - `true` |
| **cron_file**  string | If specified, uses this file instead of an individual user’s crontab.  Without a leading `/`, this is assumed to be in `/etc/cron.d`.  With a leading `/`, this is taken as absolute. |
| **insertafter**  string | If specified, the variable will be inserted after the variable specified.  Used with `state=present`. |
| **insertbefore**  string | Used with `state=present`. If specified, the variable will be inserted just before the variable specified. |
| **name**  string / required | Name of the crontab variable. |
| **state**  string | Whether to ensure that the variable is present or absent.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **user**  string | The specific user whose crontab should be modified.  This parameter defaults to `root` when unset. |
| **value**  string | The value to set this variable to.  Required if `state=present`. |

## [Attributes](cronvar_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](cronvar_module.md#id5)

```yaml+jinja
- name: Ensure entry like "EMAIL=doug@ansibmod.con.com" exists
  community.general.cronvar:
    name: EMAIL
    value: doug@ansibmod.con.com

- name: Ensure a variable does not exist. This may remove any variable named "LEGACY"
  community.general.cronvar:
    name: LEGACY
    state: absent

- name: Add a variable to a file under /etc/cron.d
  community.general.cronvar:
    name: LOGFILE
    value: /var/log/yum-autoupdate.log
    user: root
    cron_file: ansible_yum-autoupdate
```

### Authors

- Doug Luce (@dougluce)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
