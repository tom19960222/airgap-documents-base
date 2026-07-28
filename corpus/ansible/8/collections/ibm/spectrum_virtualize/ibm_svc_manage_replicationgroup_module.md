---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_svc_manage_replicationgroup module – This module manages remote copy consistency group on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_svc_manage_replicationgroup_module.html
fetched_at: 2026-07-28T02:35:01+00:00
---
# ibm.spectrum_virtualize.ibm_svc_manage_replicationgroup module – This module manages remote copy consistency group on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_manage_replicationgroup`.

New in ibm.spectrum_virtualize 1.3.0

- [Synopsis](ibm_svc_manage_replicationgroup_module.md#synopsis)
- [Parameters](ibm_svc_manage_replicationgroup_module.md#parameters)
- [Notes](ibm_svc_manage_replicationgroup_module.md#notes)
- [Examples](ibm_svc_manage_replicationgroup_module.md#examples)

## [Synopsis](ibm_svc_manage_replicationgroup_module.md#id1)

- Ansible interface to manage ‘mkrcconsistgrp’, ‘chrcconsistgrp’, and ‘rmrcconsistgrp’ remote copy consistency group commands.

## [Parameters](ibm_svc_manage_replicationgroup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **copytype**  string | Specifies the mirror type of the remote copy. ‘metro’ means MetroMirror, ‘global’ means GlobalMirror.  If not specified, a MetroMirror remote copy will be created when creating a remote copy *state=present*.  **Choices:**   - `"metro"` - `"global"` |
| **cyclingmode**  string | Specifies the behavior of Global Mirror for the relationship.  Active-active relationships and relationships with cycling modes set to Multiple must always be configured with change volumes.  Applies when *state=present* and *copytype=global*.  **Choices:**   - `"multi"` - `"none"` |
| **cyclingperiod**  integer | Specifies the cycle period in seconds. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **force**  boolean | If used to delete a consistency group, it specifies that you want the system to remove any relationship that belongs to the consistency group before the group is deleted.  If used to start a consistency group, it specifies that you want the system to process the copy operation even if it causes a temporary loss of consistency during synchronization.  It is required if the consistency group is in the ConsistentStopped state, but is not synchronized or is in the idling state - except if consistency protection is configured.  **Choices:**   - `false` - `true` |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the name for the new consistency group. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **remotecluster**  string | Specifies the name of the remote system. Only used while creating a consistency group. |
| **state**  string / required | Creates or updates (`present`) removes (`absent`) a consistency group.  **Choices:**   - `"absent"` - `"present"` |
| **token**  string  *added in ibm.spectrum_virtualize 1.5.0* | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_replicationgroup_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_replicationgroup_module.md#id4)

```yaml+jinja
- name: Define a new rc consistency group
  ibm_svc_manage_replicationgroup:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: rccg4test
    remotecluster: remotecluster
    state: present
- name: Delete rc consistency group
  ibm_svc_manage_replicationgroup:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: rccg4test
    force: true
    state: absent
- name: Update rc consistency group
  ibm_svc_manage_replicationgroup:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    name: rccg4test
    cyclingperiod: 60
    state: present
```

### Authors

- rohit(@rohitk-github)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
