---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_svc_vdisk module – This module manages volumes on IBM Spectrum Virtualize Family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_svc_vdisk_module.html
fetched_at: 2026-07-28T02:35:10+00:00
---
# ibm.spectrum_virtualize.ibm_svc_vdisk module – This module manages volumes on IBM Spectrum Virtualize Family storage systems

> **Note:**
>
> This module is part of the [ibm.spectrum_virtualize collection](https://galaxy.ansible.com/ui/repo/published/ibm/spectrum_virtualize/) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.spectrum_virtualize`.
>
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_vdisk`.

New in ibm.spectrum_virtualize 1.0.0

- [DEPRECATED](ibm_svc_vdisk_module.md#deprecated)
- [Synopsis](ibm_svc_vdisk_module.md#synopsis)
- [Parameters](ibm_svc_vdisk_module.md#parameters)
- [Notes](ibm_svc_vdisk_module.md#notes)
- [Examples](ibm_svc_vdisk_module.md#examples)
- [Status](ibm_svc_vdisk_module.md#status)

## [DEPRECATED](ibm_svc_vdisk_module.md#id1)

Removed in:
:   version 2.0.0

Why:
:   New module released

Alternative:
:   Use [ibm.spectrum_virtualize.ibm_svc_manage_volume](ibm_svc_manage_volume_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-manage-volume-module) instead.

## [Synopsis](ibm_svc_vdisk_module.md#id2)

- Ansible interface to manage ‘mkvdisk’ and ‘rmvdisk’ volume commands.

## [Parameters](ibm_svc_vdisk_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **autoexpand**  boolean  *added in ibm.spectrum_virtualize 1.2.0* | Specifies that thin-provisioned volume copies can automatically expand their real capacities.  **Choices:**   - `false` - `true` |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **easytier**  string | Defines use of easytier with VDisk.  Applies when *state=present*.  **Choices:**   - `"on"` - `"off"` |
| **log_path**  string | Path of debug log file. |
| **mdiskgrp**  string | Specifies the name of the storage pool to use when creating this volume. This parameter is required when *state=present*. |
| **name**  string / required | Specifies the name to assign to the new volume. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **rsize**  string  *added in ibm.spectrum_virtualize 1.2.0* | Defines how much physical space is initially allocated to the thin-provisioned volume in %. If rsize is not passed, the volume created is a standard volume.  Applies when `state=present`. |
| **size**  string | Defines the size of VDisk. This parameter is required when *state=present*.  This parameter can also be used to resize an existing VDisk. |
| **state**  string / required | Creates (`present`) or removes (`absent`) a volume.  **Choices:**   - `"absent"` - `"present"` |
| **token**  string  *added in ibm.spectrum_virtualize 1.5.0* | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use ibm_svc_auth module. |
| **unit**  string | Defines the size option for the storage unit. This parameter is required when *state=present*.  **Choices:**   - `"b"` - `"kb"` - `"mb"` ← (default) - `"gb"` - `"tb"` - `"pb"` |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_vdisk_module.md#id4)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_vdisk_module.md#id5)

```yaml+jinja
- name: Create a volume
  ibm.spectrum_virtualize.ibm_svc_vdisk:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: volume0
    state: present
    mdiskgrp: Pool0
    easytier: 'off'
    size: "4294967296"
    unit: b
- name: Create a thin-provisioned volume
  ibm.spectrum_virtualize.ibm_svc_vdisk:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: volume0
    state: present
    mdiskgrp: Pool0
    easytier: 'off'
    size: "4294967296"
    unit: b
    rsize: '20%'
    autoexpand: true
- name: Delete a volume
  ibm.spectrum_virtualize.ibm_svc_vdisk:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: volume0
    state: absent
```

## [Status](ibm_svc_vdisk_module.md#id6)

- This module will be removed in version 2.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](ibm_svc_vdisk_module.md#deprecated).

### Authors

- Sreshtant Bohidar(@Sreshtant-Bohidar)
- Rohit Kumar(@rohitk-github)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
