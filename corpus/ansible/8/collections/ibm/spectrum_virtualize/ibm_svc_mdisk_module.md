---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_svc_mdisk module – This module manages MDisks on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_svc_mdisk_module.html
fetched_at: 2026-07-28T02:35:07+00:00
---
# ibm.spectrum_virtualize.ibm_svc_mdisk module – This module manages MDisks on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_mdisk`.

New in ibm.spectrum_virtualize 1.0.0

- [Synopsis](ibm_svc_mdisk_module.md#synopsis)
- [Parameters](ibm_svc_mdisk_module.md#parameters)
- [Notes](ibm_svc_mdisk_module.md#notes)
- [Examples](ibm_svc_mdisk_module.md#examples)

## [Synopsis](ibm_svc_mdisk_module.md#id1)

- Ansible interface to manage ‘mkarray’ and ‘rmmdisk’ MDisk commands.

## [Parameters](ibm_svc_mdisk_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **drive**  string | Drive(s) to use as members of the RAID array.  Required when *state=present*, to create an MDisk array. |
| **encrypt**  string | Defines use of encryption with the MDisk group.  Applies when *state=present*.  **Choices:**   - `"yes"` - `"no"` ← (default) |
| **level**  string | Specifies the RAID level.  Required when *state=present*, to create an MDisk array.  **Choices:**   - `"raid0"` - `"raid1"` - `"raid5"` - `"raid6"` - `"raid10"` |
| **log_path**  string | Path of debug log file. |
| **mdiskgrp**  string / required | The storage pool (mdiskgrp) to which you want to add the MDisk. |
| **name**  string / required | The MDisk name. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **state**  string / required | Creates (`present`) or removes (`absent`) the MDisk.  **Choices:**   - `"absent"` - `"present"` |
| **token**  string  *added in ibm.spectrum_virtualize 1.5.0* | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_mdisk_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_mdisk_module.md#id4)

```yaml+jinja
- name: Create MDisk and name as mdisk20
  ibm.spectrum_virtualize.ibm_svc_mdisk:
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
  ibm.spectrum_virtualize.ibm_svc_mdisk:
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

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
