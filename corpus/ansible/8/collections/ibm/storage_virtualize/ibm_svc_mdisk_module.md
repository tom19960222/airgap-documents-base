---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_mdisk module – This module manages MDisks on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_mdisk_module.html
fetched_at: 2026-07-28T02:35:41+00:00
---
# ibm.storage_virtualize.ibm_svc_mdisk module – This module manages MDisks on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_mdisk`.

New in ibm.storage_virtualize 1.0.0

- [Synopsis](ibm_svc_mdisk_module.md#synopsis)
- [Parameters](ibm_svc_mdisk_module.md#parameters)
- [Notes](ibm_svc_mdisk_module.md#notes)
- [Examples](ibm_svc_mdisk_module.md#examples)

## [Synopsis](ibm_svc_mdisk_module.md#id1)

- Ansible interface to manage ‘mkarray’ and ‘rmmdisk’ MDisk commands.

## [Parameters](ibm_svc_mdisk_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **drive**  string | Drive(s) to use as members of the RAID array.  Required when *state=present*, to create an MDisk array. |
| **driveclass**  string  *added in ibm.storage_virtualize 2.0.0* | Specifies the class that is being used to create the array.  Applies when *state=present*. |
| **drivecount**  string  *added in ibm.storage_virtualize 2.0.0* | Specifies the number of the drives.  The value must be a number in the range 2 - 128.  Applies when *state=present*. |
| **encrypt**  string | Defines use of encryption with the MDisk group.  Applies when *state=present*.  **Choices:**   - `"yes"` - `"no"` ← (default) |
| **level**  string | Specifies the RAID level.  Required when *state=present*, to create an MDisk array.  **Choices:**   - `"raid0"` - `"raid1"` - `"raid5"` - `"raid6"` - `"raid10"` |
| **log_path**  string | Path of debug log file. |
| **mdiskgrp**  string / required | The storage pool (mdiskgrp) to which you want to add the MDisk. |
| **name**  string / required | The MDisk name. |
| **old_name**  string  *added in ibm.storage_virtualize 2.0.0* | Specifies the old name of an existing pool.  Applies when *state=present*, to rename the existing pool. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **state**  string / required | Creates (`present`) or removes (`absent`) the MDisk.  **Choices:**   - `"absent"` - `"present"` |
| **stripewidth**  string  *added in ibm.storage_virtualize 2.0.0* | Specifies the width of a single unit of redundancy within a distributed set of drives  The value must be a number in the range 2 - 16.  Applies when *state=present*. |
| **token**  string  *added in ibm.storage_virtualize 1.5.0* | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_mdisk_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_mdisk_module.md#id4)

```yaml+jinja
- name: Create MDisk and name as mdisk20
  ibm.storage_virtualize.ibm_svc_mdisk:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    name: mdisk20
    state: present
    level: raid0
    drive: '5:6'
    encrypt: no
    mdiskgrp: pool20
- name: Delete MDisk named mdisk20
  ibm.storage_virtualize.ibm_svc_mdisk:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    name: mdisk20
    state: absent
    mdiskgrp: pool20
```

### Authors

- Peng Wang(@wangpww)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
