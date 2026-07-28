---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_manage_volume module – This module manages standard volumes on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_manage_volume_module.html
fetched_at: 2026-07-28T02:35:39+00:00
---
# ibm.storage_virtualize.ibm_svc_manage_volume module – This module manages standard volumes on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_manage_volume`.

New in ibm.storage_virtualize 1.6.0

- [Synopsis](ibm_svc_manage_volume_module.md#synopsis)
- [Parameters](ibm_svc_manage_volume_module.md#parameters)
- [Notes](ibm_svc_manage_volume_module.md#notes)
- [Examples](ibm_svc_manage_volume_module.md#examples)

## [Synopsis](ibm_svc_manage_volume_module.md#id1)

- Ansible interface to manage ‘mkvolume’, ‘rmvolume’, and ‘chvdisk’ volume commands.

## [Parameters](ibm_svc_manage_volume_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allow_hs**  boolean  *added in ibm.storage_virtualize 2.0.0* | If specified `True`, manages the hyperswap volume by ignoring the volume type validation.  Valid when *state=present*, to modify an existing volume.  **Choices:**   - `false` ← (default) - `true` |
| **buffersize**  string | Specifies the pool capacity that the volume will reserve as a buffer for thin-provisioned and compressed volumes.  Parameter ‘thin’ or ‘compressed’ must be specified to use this parameter.  The default buffer size is 2%.  *thin* or *compressed* is required when using *buffersize*.  Valid when *state=present*, to create a volume. |
| **cloud_account_name**  string  *added in ibm.storage_virtualize 1.11.0* | Specifies the name of the cloud account name.  Valid when *enable_cloud_snapshot=true*. |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **compressed**  boolean | Specifies that a compressed volume is to be created.  Parameters ‘compressed’ and ‘thin’ are mutually exclusive.  Valid when *state=present*, to create a compressed volume.  **Choices:**   - `false` - `true` |
| **deduplicated**  boolean | Specifies that a deduplicated volume is to be created.  Required when *state=present*, to create a deduplicated volume.  **Choices:**   - `false` - `true` |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **enable_cloud_snapshot**  boolean  *added in ibm.storage_virtualize 1.11.0* | Specify to enable or disable cloud snapshot.  Valid when *state=present*, to modify an existing volume.  **Choices:**   - `false` - `true` |
| **iogrp**  string | Specifies the list of I/O group names. Group names in the list must be separated by using a comma.  While creating a new volume, the first I/O group in the list is added as both cached & access I/O group, while remaining I/O groups are added as access I/O groups.  This parameter supports update functionality.  Valid when *state=present*, to create or modify a volume. |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the name to assign to the new volume. |
| **novolumegroup**  boolean | If specified `True`, the volume is removed from its associated volumegroup.  Parameters ‘novolumegroup’ and ‘volumegroup’ are mutually exclusive.  Valid when *state=present*, to modify a volume.  **Choices:**   - `false` - `true` |
| **old_name**  string  *added in ibm.storage_virtualize 1.9.0* | Specifies the old name of the volume during renaming.  Valid when *state=present*, to rename an existing volume. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **pool**  string | Specifies the name of the storage pool to use while creating the volume.  This parameter is required when *state=present*, to create a volume. |
| **size**  string | Defines the size of the volume. This parameter can also be used to resize an existing volume.  Required when *state=present*, to create or modify a volume. |
| **state**  string / required | Creates or updates (`present`) or removes (`absent`) a volume.  **Choices:**   - `"absent"` - `"present"` |
| **thin**  boolean | Specifies that a thin-provisioned volume is to be created.  Parameters ‘thin’ and ‘compressed’ are mutually exclusive.  Valid when *state=present*, to create a thin-provisioned volume.  **Choices:**   - `false` - `true` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the ibm_svc_auth module. |
| **unit**  string | Specifies the data units to use with the capacity that is specified by the ‘size’ parameter.  *size* is required when using *unit*.  **Choices:**   - `"b"` - `"kb"` - `"mb"` ← (default) - `"gb"` - `"tb"` - `"pb"` |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |
| **volumegroup**  string | Specifies the name of the volumegroup to which the volume is to be added.  Parameters ‘volumegroup’ and ‘novolumegroup’ are mutually exclusive.  Valid when *state=present*, to create or modify a volume. |

## [Notes](ibm_svc_manage_volume_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_volume_module.md#id4)

```yaml+jinja
- name: Create a volume
  ibm.storage_virtualize.ibm_svc_manage_volume:
    clustername: "{{ clustername }}"
    domain: "{{domain}}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: "{{ log_path }}"
    name: "volume_name"
    state: "present"
    pool: "pool_name"
    size: "1"
    unit: "gb"
    iogrp: "io_grp0, io_grp1"
    volumegroup: "test_volumegroup"
- name: Create a thin-provisioned volume
  ibm.storage_virtualize.ibm_svc_manage_volume:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: "{{ log_path }}"
    name: "volume_name"
    state: "present"
    pool: "pool_name"
    size: "1"
    unit: "gb"
    iogrp: "io_grp0, io_grp1"
    thin: true
    buffersize: 10%
- name: Create a compressed volume
  ibm.storage_virtualize.ibm_svc_manage_volume:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: "{{ log_path }}"
    name: "volume_name"
    state: "present"
    pool: "pool_name"
    size: "1"
    unit: "gb"
    iogrp: "io_grp0, io_grp1"
    compressed: true
    buffersize: 10%
- name: Creating a volume with iogrp- io_grp0
  ibm.storage_virtualize.ibm_svc_manage_volume:
    clustername: "{{ clustername }}"
    domain: "{{ domain}}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: "{{ log_path }}"
    name: "volume_name"
    state: "present"
    pool: "pool_name"
    size: "1"
    unit: "gb"
    iogrp: "io_grp0"
- name: Adding a new iogrp- io_grp1
  ibm.storage_virtualize.ibm_svc_manage_volume:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: "{{ log_path }}"
    name: "volume_name"
    state: "present"
    pool: "pool_name"
    size: "1"
    unit: "gb"
    iogrp: "io_grp0, iogrp1"
- name: Rename an existing volume
  ibm.storage_virtualize.ibm_svc_manage_volume:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    old_name: "volume_name"
    name: "new_volume_name"
    state: "present"
- name: Enable cloud backup in an existing volume
  ibm.storage_virtualize.ibm_svc_manage_volume:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    name: "volume_name"
    enable_cloud_snapshot: true
    cloud_account_name: "aws_acc"
    state: "present"
- name: Delete a volume
  ibm.storage_virtualize.ibm_svc_manage_volume:
    clustername: "{{ clustername }}"
    domain: "{{ domain }}"
    username: "{{ username }}"
    password: "{{ password }}"
    log_path: "{{ log_path }}"
    name: "new_volume_name"
    state: "absent"
```

### Authors

- Sreshtant Bohidar(@Sreshtant-Bohidar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
