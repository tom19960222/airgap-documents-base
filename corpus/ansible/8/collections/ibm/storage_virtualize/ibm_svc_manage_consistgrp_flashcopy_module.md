---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_manage_consistgrp_flashcopy module – This module manages FlashCopy consistency groups on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_manage_consistgrp_flashcopy_module.html
fetched_at: 2026-07-28T02:35:29+00:00
---
# ibm.storage_virtualize.ibm_svc_manage_consistgrp_flashcopy module – This module manages FlashCopy consistency groups on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_manage_consistgrp_flashcopy`.

New in ibm.storage_virtualize 1.4.0

- [Synopsis](ibm_svc_manage_consistgrp_flashcopy_module.md#synopsis)
- [Parameters](ibm_svc_manage_consistgrp_flashcopy_module.md#parameters)
- [Notes](ibm_svc_manage_consistgrp_flashcopy_module.md#notes)
- [Examples](ibm_svc_manage_consistgrp_flashcopy_module.md#examples)

## [Synopsis](ibm_svc_manage_consistgrp_flashcopy_module.md#id1)

- Ansible interface to manage ‘mkfcconsistgrp’ and ‘rmfcconsistgrp’ volume commands.

## [Parameters](ibm_svc_manage_consistgrp_flashcopy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **force**  boolean | If specified True, removes all the associated FlashCopy mappings while deleting the FlashCopy consistency group.  Valid when *state=absent*, to delete a FlashCopy consistency group.  **Choices:**   - `false` - `true` |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the name of the FlashCopy consistency group. |
| **noownershipgroup**  boolean | If specified True, the consistency group is removed from all associated ownership groups.  Parameters *noownershipgroup* and *ownershipgroup* are mutually exclusive.  Valid when *state=present*, to modify a FlashCopy consistency group.  **Choices:**   - `false` - `true` |
| **ownershipgroup**  string | Specifies the name of the ownership group.  Parameters *ownershipgroup* and *noownershipgroup* are mutually exclusive.  Valid when *state=present*, to create or modify a FlashCopy consistency group. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **state**  string / required | Creates (`present`) or removes (`absent`) a FlashCopy consistency group.  **Choices:**   - `"present"` - `"absent"` |
| **token**  string  *added in ibm.storage_virtualize 1.5.0* | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the [ibm.storage_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_consistgrp_flashcopy_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_consistgrp_flashcopy_module.md#id4)

```yaml+jinja
- name: Create a FlashCopy consistency group
  ibm.storage_virtualize.ibm_svc_manage_consistgrp_flashcopy:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: consistgroup-name
    state: present
    ownershipgroup: ownershipgroup-name
- name: Delete a FlashCopy consistency group
  ibm.storage_virtualize.ibm_svc_manage_consistgrp_flashcopy:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: consistgroup-name
    state: absent
    force: true
```

### Authors

- Sreshtant Bohidar(@Sreshtant-Bohidar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
