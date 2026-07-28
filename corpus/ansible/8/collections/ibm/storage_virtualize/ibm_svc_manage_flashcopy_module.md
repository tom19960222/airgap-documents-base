---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_manage_flashcopy module – This module manages FlashCopy mappings on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_manage_flashcopy_module.html
fetched_at: 2026-07-28T02:35:31+00:00
---
# ibm.storage_virtualize.ibm_svc_manage_flashcopy module – This module manages FlashCopy mappings on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_manage_flashcopy`.

New in ibm.storage_virtualize 1.4.0

- [Synopsis](ibm_svc_manage_flashcopy_module.md#synopsis)
- [Parameters](ibm_svc_manage_flashcopy_module.md#parameters)
- [Notes](ibm_svc_manage_flashcopy_module.md#notes)
- [Examples](ibm_svc_manage_flashcopy_module.md#examples)

## [Synopsis](ibm_svc_manage_flashcopy_module.md#id1)

- Ansible interface to manage ‘mkfcmap’, ‘rmfcmap’, and ‘chfcmap’ volume commands. This module configures “clone”, “snapshot” or “backup” type FlashCopy mappings.

## [Parameters](ibm_svc_manage_flashcopy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **consistgrp**  string | Specifies the name of the consistency group to which the FlashCopy mapping is to be added.  Parameters *consistgrp* and *noconsistgrp* are mutually exclusive.  Valid when *state=present*, to create or modify a FlashCopy mapping. |
| **copyrate**  string | Specifies the copy rate. The rate varies between 0-150.  If unspecified, the default copy rate of 50 for clone and 0 for snapshot is used.  Valid when *state=present*, to create or modify a FlashCopy mapping. |
| **copytype**  string | Specifies the copy type when creating the FlashCopy mapping.  Required when *state=present*, to create a FlashCopy mapping.  **Choices:**   - `"snapshot"` - `"clone"` - `"backup"` |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **force**  boolean | Brings the target volume online. This parameter is required if the FlashCopy mapping is in the stopped state.  Valid when *state=absent*, to delete a FlashCopy mapping.  **Choices:**   - `false` - `true` |
| **grainsize**  string | Specifies the grain size for the FlashCopy mapping.  The grainsize can be set to 64 or 256. The default value is 256.  Valid when *state=present*, to create a FlashCopy mapping. |
| **log_path**  string | Path of debug log file. |
| **mdiskgrp**  string | Specifies the name of the storage pool to use when creating the target volume.  If unspecified, the pool associated with the source volume is used.  Valid when *state=present*, to create a FlashCopy mapping. |
| **name**  string / required | Specifies the name of the FlashCopy mapping. |
| **noconsistgrp**  boolean | If specified True, FlashCopy mapping is removed from the consistency group.  Parameters *noconsistgrp* and *consistgrp* are mutually exclusive.  Valid when *state=present*, to modify a FlashCopy mapping.  **Choices:**   - `false` - `true` |
| **old_name**  string | Specifies the old name of an mdiskgrp.  Applies when *state=present*, to rename the existing mdiskgrp. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **source**  string | Specifies the name of the source volume.  Required when *state=present*, to create a FlashCopy mapping. |
| **state**  string / required | Creates or updates (`present`) or removes (`absent`) a FlashCopy mapping.  **Choices:**   - `"present"` - `"absent"` |
| **target**  string | Specifies the name of the target volume.  Required when *state=present*, to create a FlashCopy mapping. |
| **token**  string  *added in ibm.storage_virtualize 1.5.0* | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_flashcopy_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_flashcopy_module.md#id4)

```yaml+jinja
- name: Create FlashCopy mapping for snapshot
  ibm.storage_virtualize.ibm_svc_manage_flashcopy:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    state: present
    name: snapshot-name
    copytype: snapshot
    source: source-volume-name
    target: target-volume-name
    mdiskgrp: Pool0
    consistgrp: consistencygroup-name
    copyrate: 50
    grainsize: 64
- name: Create FlashCopy mapping for clone
  ibm.storage_virtualize.ibm_svc_manage_flashcopy:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    state: present
    name: snapshot-name
    copytype: clone
    source: source-volume-name
    target: target-volume-name
    mdiskgrp: Pool0
    consistgrp: consistencygroup-name
    copyrate: 50
    grainsize: 64
- name: Create FlashCopy mapping for backup
  ibm.storage_virtualize.ibm_svc_manage_flashcopy:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    state: present
    name: snapshot-name
    copytype: backup
    source: source-volume-name
    target: target-volume-name
    mdiskgrp: Pool0
    copyrate: 50
    grainsize: 64
- name: Delete FlashCopy mapping for snapshot
  ibm.storage_virtualize.ibm_svc_manage_flashcopy:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: snapshot-name
    state: absent
    force: true
- name: Delete FlashCopy mapping for clone
  ibm.storage_virtualize.ibm_svc_manage_flashcopy:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: clone-name
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
