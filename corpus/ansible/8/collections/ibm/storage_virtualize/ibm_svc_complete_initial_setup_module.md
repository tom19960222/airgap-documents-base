---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_complete_initial_setup module – This module completes the initial setup configuration for LMC systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_complete_initial_setup_module.html
fetched_at: 2026-07-28T02:35:25+00:00
---
# ibm.storage_virtualize.ibm_svc_complete_initial_setup module – This module completes the initial setup configuration for LMC systems

> **Note:**
>
> This module is part of the [ibm.storage_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/storage_virtualize/) (version 2.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.storage_virtualize`.
>
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_complete_initial_setup`.

New in ibm.storage_virtualize 1.8.0

- [Synopsis](ibm_svc_complete_initial_setup_module.md#synopsis)
- [Parameters](ibm_svc_complete_initial_setup_module.md#parameters)
- [Notes](ibm_svc_complete_initial_setup_module.md#notes)
- [Examples](ibm_svc_complete_initial_setup_module.md#examples)

## [Synopsis](ibm_svc_complete_initial_setup_module.md#id1)

- It disables the GUI setup wizard for LMC systems.
- It is recommended to run this module after using ibm_svc_initial_setup module for intial setup configuration.
- This module works on SSH. Paramiko must be installed to use this module.

## [Parameters](ibm_svc_complete_initial_setup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **log_path**  string | Path of debug log file. |
| **password**  string / required | Password for the Storage Virtualize system. |
| **username**  string / required | Username for the Storage Virtualize system. |

## [Notes](ibm_svc_complete_initial_setup_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_complete_initial_setup_module.md#id4)

```yaml+jinja
- name: complete intial setup
  ibm.storage_virtualize.ibm_svc_complete_initial_setup:
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
```

### Authors

- Shilpi Jain(@Shilpi-J)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
