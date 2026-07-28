---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_svc_mdiskgrp module – This module manages pools on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_svc_mdiskgrp_module.html
fetched_at: 2026-07-28T02:35:07+00:00
---
# ibm.spectrum_virtualize.ibm_svc_mdiskgrp module – This module manages pools on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_mdiskgrp`.

New in ibm.spectrum_virtualize 1.0.0

- [Synopsis](ibm_svc_mdiskgrp_module.md#synopsis)
- [Parameters](ibm_svc_mdiskgrp_module.md#parameters)
- [Notes](ibm_svc_mdiskgrp_module.md#notes)
- [Examples](ibm_svc_mdiskgrp_module.md#examples)

## [Synopsis](ibm_svc_mdiskgrp_module.md#id1)

- Ansible interface to manage ‘mkmdiskgrp’ and ‘rmmdiskgrp’ pool commands.

## [Parameters](ibm_svc_mdiskgrp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **datareduction**  string | Defines use of data reduction pools (DRPs) on the MDisk group.  Applies when *state=present*, to create a pool.  **Choices:**   - `"yes"` - `"no"` ← (default) |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **easytier**  string | Defines use of easytier with the MDisk group.  Applies when *state=present*, to create a pool.  **Choices:**   - `"on"` - `"off"` ← (default) - `"auto"` |
| **encrypt**  string | Defines use of encryption with the MDisk group.  Applies when *state=present*, to create a pool.  **Choices:**   - `"yes"` - `"no"` ← (default) |
| **etfcmoverallocationmax**  string  *added in ibm.spectrum_virtualize 1.12.0* | Specifies the maximum over allocation which Easy Tier can migrate onto FlashCore Module arrays, when the array is used as the top tier in a multitier pool. The value acts as a multiplier of the physically available space.  The allowed values are a percentage in the range of 100% (default) to 400% or off. Setting the value to off disables this feature.  Applies when *state=present*. |
| **ext**  integer | Specifies the size of the extents for this group in MB.  Applies when *state=present*, to create a pool. |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the name to assign to the new pool. |
| **noownershipgroup**  boolean  *added in ibm.spectrum_virtualize 1.12.0* | Specifies to unmap ownershipgroup from the pool.  Applies when *state=present* to modify an existing pool.  **Choices:**   - `false` - `true` |
| **noprovisioningpolicy**  boolean  *added in ibm.spectrum_virtualize 1.10.0* | Specify to unmap provisioning policy from the pool.  Applies, when *state=present* to modify an existing pool.  **Choices:**   - `false` - `true` |
| **noquota**  boolean  *added in ibm.spectrum_virtualize 1.8.0* | Specify to create a data reduction child pool.  *noquota* and *size* parameters are mutually exclusive.  *noquota* parameter must be used with *datareduction* set to yes to create a data reduction child pool.  *noquota* parameter must be used with *parentmdiskgrp* in a parent data reduction storage pool.  **Choices:**   - `false` - `true` |
| **old_name**  string  *added in ibm.spectrum_virtualize 1.12.0* | Specifies the old name of an existing pool.  Applies when *state=present*, to rename the existing pool. |
| **ownershipgroup**  string  *added in ibm.spectrum_virtualize 1.12.0* | Specifies the name of the ownershipgroup to map it with the pool.  Applies when *state=present*. |
| **parentmdiskgrp**  string | Parentmdiskgrp for subpool.  Applies when *state=present*, to create a pool. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **provisioningpolicy**  string  *added in ibm.spectrum_virtualize 1.10.0* | Specify the name of the provisioning policy to map it with the pool.  Applies, when *state=present*. |
| **replication_partner_clusterid**  string  *added in ibm.spectrum_virtualize 1.10.0* | Specifies the id or name of the partner cluster which will be used for replication.  Applies, when *state=present*.  Supported in SV build 8.5.2.1 or later. |
| **replicationpoollinkuid**  string  *added in ibm.spectrum_virtualize 1.10.0* | Specifies the replication pool unique identifier which should be same as the pool that present in the replication server.  Applies, when *state=present*.  Supported in SV build 8.5.2.1 or later. |
| **resetreplicationpoollinkuid**  boolean  *added in ibm.spectrum_virtualize 1.10.0* | If set, any links between this pool on local system and pools on remote systems will be removed.  Applies, when *state=present* to modify an existing pool.  Supported in SV build 8.5.2.1 or later.  **Choices:**   - `false` - `true` |
| **safeguarded**  boolean  *added in ibm.spectrum_virtualize 1.8.0* | Specify to create a safeguarded child pool.  Applicable only during child pool creation.  **Choices:**   - `false` - `true` |
| **size**  integer | Specifies the child pool capacity. The value must be a numeric value (and an integer multiple of the extent size).  Applies when *state=present*, to create a pool. |
| **state**  string / required | Creates (`present`) or removes (`absent`) an MDisk group.  **Choices:**   - `"absent"` - `"present"` |
| **token**  string  *added in ibm.spectrum_virtualize 1.5.0* | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **unit**  string | Unit for subpool.  Applies when *state=present*, to create a pool. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |
| **vdiskprotectionenabled**  string  *added in ibm.spectrum_virtualize 1.12.0* | Specifies whether volume protection is enabled for this storage pool. The default value is ‘yes’.  Applies when *state=present*.  **Choices:**   - `"yes"` - `"no"` |
| **warning**  integer  *added in ibm.spectrum_virtualize 1.12.0* | If specified, generates a warning when the used disk capacity in the storage pool first exceeds the specified threshold.  The default value is 80. To disable it, specify the value as 0.  Applies when *state=present* while creating the pool. |

## [Notes](ibm_svc_mdiskgrp_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_mdiskgrp_module.md#id4)

```yaml+jinja
- name: Create mdisk group
  ibm.spectrum_virtualize.ibm_svc_mdiskgrp:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    name: pool1
    provisioningpolicy: pp0
    replicationpoollinkuid: 000000000000000
    replication_partner_clusterid: 000000000032432342
    etfcmoverallocationmax: 120
    state: present
    datareduction: no
    easytier: auto
    encrypt: no
    ext: 1024
- name: Create childpool with ownershipgroup
  ibm.spectrum_virtualize.ibm_svc_mdiskgrp:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    name: childpool0
    ownershipgroup: owner0
    parentmdiskgrp: pool1
    state: present
    datareduction: no
    easytier: auto
    encrypt: no
    ext: 1024
- name: Create a safeguarded backup location
  ibm.spectrum_virtualize.ibm_svc_mdiskgrp:
    clustername: "{{clustername}}"
    token: "{{results.token}}"
    log_path: "{{log_path}}"
    parentmdiskgrp: Pool1
    name: Pool1child1
    datareduction: 'yes'
    safeguarded: True
    ext: 1024
    noquota: True
    state: present
- name: Delete mdisk group
  ibm.spectrum_virtualize.ibm_svc_mdiskgrp:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    name: pool1
    state: absent
- name: Delete a safeguarded backup location
  ibm.spectrum_virtualize.ibm_svc_mdiskgrp:
    clustername: "{{clustername}}"
    token: "{{results.token}}"
    log_path: "{{log_path}}"
    parentmdiskgrp: Pool1
    name: Pool1child1
    state: absent
```

### Authors

- Peng Wang(@wangpww)
- Sanjaikumaar M (@sanjaikumaar)
- Lavanya C R(@lavanya)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
