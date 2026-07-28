---
collection: ansible
version: "8"
title: "community.general.aix_inittab module – Manages the inittab on AIX"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/aix_inittab_module.html
fetched_at: 2026-07-28T01:44:33+00:00
---
# community.general.aix_inittab module – Manages the inittab on AIX

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
> see [Requirements](aix_inittab_module.md#ansible-collections-community-general-aix-inittab-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.aix_inittab`.

- [Synopsis](aix_inittab_module.md#synopsis)
- [Requirements](aix_inittab_module.md#requirements)
- [Parameters](aix_inittab_module.md#parameters)
- [Attributes](aix_inittab_module.md#attributes)
- [Notes](aix_inittab_module.md#notes)
- [Examples](aix_inittab_module.md#examples)
- [Return Values](aix_inittab_module.md#return-values)

## [Synopsis](aix_inittab_module.md#id1)

- Manages the inittab on AIX.

Aliases: system.aix_inittab

## [Requirements](aix_inittab_module.md#id2)

The below requirements are needed on the host that executes this module.

- itertools

## [Parameters](aix_inittab_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **action**  string | Action what the init has to do with this entry.  **Choices:**   - `"boot"` - `"bootwait"` - `"hold"` - `"initdefault"` - `"off"` - `"once"` - `"ondemand"` - `"powerfail"` - `"powerwait"` - `"respawn"` - `"sysinit"` - `"wait"` |
| **command**  string / required | What command has to run. |
| **insertafter**  string | After which inittabline should the new entry inserted. |
| **name**  aliases: service  string / required | Name of the inittab entry. |
| **runlevel**  string / required | Runlevel of the entry. |
| **state**  string | Whether the entry should be present or absent in the inittab file.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](aix_inittab_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](aix_inittab_module.md#id5)

> **Note:**
>
> - The changes are persistent across reboots.
> - You need root rights to read or adjust the inittab with the `lsitab`, `chitab`, `mkitab` or `rmitab` commands.
> - Tested on AIX 7.1.

## [Examples](aix_inittab_module.md#id6)

```yaml+jinja
# Add service startmyservice to the inittab, directly after service existingservice.
- name: Add startmyservice to inittab
  community.general.aix_inittab:
    name: startmyservice
    runlevel: 4
    action: once
    command: echo hello
    insertafter: existingservice
    state: present
  become: true

# Change inittab entry startmyservice to runlevel "2" and processaction "wait".
- name: Change startmyservice to inittab
  community.general.aix_inittab:
    name: startmyservice
    runlevel: 2
    action: wait
    command: echo hello
    state: present
  become: true

- name: Remove startmyservice from inittab
  community.general.aix_inittab:
    name: startmyservice
    runlevel: 2
    action: wait
    command: echo hello
    state: absent
  become: true
```

## [Return Values](aix_inittab_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Whether the inittab changed or not  **Returned:** always  **Sample:** `true` |
| **msg**  string | Action done with the inittab entry  **Returned:** changed  **Sample:** `"changed inittab entry startmyservice"` |
| **name**  string | Name of the adjusted inittab entry  **Returned:** always  **Sample:** `"startmyservice"` |

### Authors

- Joris Weijters (@molekuul)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
