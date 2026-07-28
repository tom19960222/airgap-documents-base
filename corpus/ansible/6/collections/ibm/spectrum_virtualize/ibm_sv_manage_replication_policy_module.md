---
collection: ansible
version: "6"
title: "ibm.spectrum_virtualize.ibm_sv_manage_replication_policy module – This module configures and manages replication policies on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ibm/spectrum_virtualize/ibm_sv_manage_replication_policy_module.html
fetched_at: 2026-07-27T17:50:20+00:00
---
# ibm.spectrum_virtualize.ibm_sv_manage_replication_policy module – This module configures and manages replication policies on IBM Spectrum Virtualize family storage systems

> **Note:**
>
> This module is part of the [ibm.spectrum_virtualize collection](https://galaxy.ansible.com/ibm/spectrum_virtualize) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ibm.spectrum_virtualize`.
>
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_sv_manage_replication_policy`.

New in ibm.spectrum_virtualize 1.10.0

- [Synopsis](ibm_sv_manage_replication_policy_module.md#synopsis)
- [Parameters](ibm_sv_manage_replication_policy_module.md#parameters)
- [Notes](ibm_sv_manage_replication_policy_module.md#notes)
- [Examples](ibm_sv_manage_replication_policy_module.md#examples)

## [Synopsis](ibm_sv_manage_replication_policy_module.md#id1)

- Ansible interface to manage mkreplicationpolicy, chreplicationpolicy, and rmreplicationpolicy commands.
- This module manages policy based replication.
- This module can be run on all IBM Spectrum Virtualize storage systems with version 8.5.2.1 or later.

## [Parameters](ibm_sv_manage_replication_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **location1iogrp**  integer | Specifies the ID of the I/O group of the system in location 1 of the topology. |
| **location1system**  string | Specifies the name or ID of the system in location 1 of the topology. |
| **location2iogrp**  integer | Specifies the ID of the I/O group of the system in location 2 of the topology. |
| **location2system**  string | Specifies the name or ID of the system in location 2 of the topology. |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the name of the replication policy. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **rpoalert**  integer | Specifies the RPO alert threshold in seconds. The minimum value is 60 (1 minute) and the maximum value is 86400 (1 day).  The value must be a multiple of 60 seconds. |
| **state**  string / required | Creates, updates (`present`), or deletes (`absent`) a replication policy.  Choices:   - `"present"` - `"absent"` |
| **token**  string | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **topology**  string | Specifies the policy topology.  Choices:   - `"2-site-async-dr"` |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  Choices:   - `false` ← (default) - `true` |

## [Notes](ibm_sv_manage_replication_policy_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_replication_policy_module.md#id4)

```yaml+jinja
- name: Create replication policy
  ibm.spectrum_virtualize.ibm_sv_manage_replication_policy:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    name: replication_policy0
    topology: 2-site-async-dr
    location1system: x.x.x.x
    location1iogrp: 0
    location2system: x.x.x.x
    location2iogrp: 0
    rpoalert: 60
    state: present
- name: Delete replication policy
  ibm.spectrum_virtualize.ibm_sv_manage_replication_policy:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    name: replication_policy0
    state: absent
```

### Authors

- Sanjaikumaar M (@sanjaikumaar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
[Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
