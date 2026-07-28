---
collection: ansible
version: "6"
title: "ibm.spectrum_virtualize.ibm_svc_manage_replication module – This module manages remote copies (or rcrelationship) on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ibm/spectrum_virtualize/ibm_svc_manage_replication_module.html
fetched_at: 2026-07-27T17:50:34+00:00
---
# ibm.spectrum_virtualize.ibm_svc_manage_replication module – This module manages remote copies (or rcrelationship) on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_manage_replication`.

New in ibm.spectrum_virtualize 1.3.0

- [Synopsis](ibm_svc_manage_replication_module.md#synopsis)
- [Parameters](ibm_svc_manage_replication_module.md#parameters)
- [Notes](ibm_svc_manage_replication_module.md#notes)
- [Examples](ibm_svc_manage_replication_module.md#examples)

## [Synopsis](ibm_svc_manage_replication_module.md#id1)

- Ansible interface to manage remote copy replication.

## [Parameters](ibm_svc_manage_replication_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aux**  string | Specifies the auxiliary volume name when creating a remote copy. |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **consistgrp**  string | Specifies a consistency group that this relationship will join. If not specified by user, the relationship is created as a stand-alone relationship.  Applies when *state=present*. |
| **copytype**  string | Specifies the mirror type of the remote copy. ‘metro’ means MetroMirror, ‘global’ means GlobalMirror, and ‘GMCV’ means GlobalMirror with change volume.  If not specified, a MetroMirror remote copy will be created when creating a remote copy *state=present*.  Choices:   - `"metro"` - `"global"` - `"GMCV"` |
| **cyclingperiod**  integer | Specifies the cycle period in seconds. The default cycle is of 300 seconds. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **force**  boolean | Specifies that the relationship must be deleted even if it results in the secondary volume containing inconsistent data.  Choices:   - `false` - `true` |
| **log_path**  string | Path of debug log file. |
| **master**  string | Specifies the master volume name when creating a remote copy. |
| **name**  string | Specifies the name to assign to the new remote copy relationship or to operate on the existing remote copy. |
| **noconsistgrp**  boolean | Specifies whether to remove the specified relationship from a consistency group, making the relationship a stand-alone relationship.  Applies when *state=present*.  Choices:   - `false` ← (default) - `true` |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **remotecluster**  string | Specifies the name of remote cluster when creating a remote copy. |
| **state**  string / required | Creates or updates (`present`), removes (`absent`) a remote copy relationship.  Choices:   - `"absent"` - `"present"` |
| **sync**  boolean | Specifies whether to create a synchronized relationship.  Choices:   - `false` ← (default) - `true` |
| **token**  string  added in ibm.spectrum_virtualize 1.5.0 | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  Choices:   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_replication_module.md#id3)

> **Note:**
>
> - The parameters *primary* and *aux* are mandatory only when a remote copy relationship does not exist.
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_replication_module.md#id4)

```yaml+jinja
- name: Create remote copy
  ibm.spectrum_virtualize.ibm_svc_manage_replication:
    name: sample_rcopy
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/ansible.log
    state: present
    remotecluster: "{{remotecluster}}"
    master: SourceVolume0
    aux: TargetVolume0
    copytype: global
    sync: true
    consistgrp: sample_rccg
  register: result
- name: Exclude the remote copy from consistency group
  ibm.spectrum_virtualize.ibm_svc_manage_replication:
    name: sample_rcopy2
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/ansible.log
    state: present
    noconsistgrp: true
- name: Delete remote copy
  ibm.spectrum_virtualize.ibm_svc_manage_replication:
    name: sample_rcopy3
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/ansible.log
    state: absent
- name: Create GlobalMirror remote copy relationship with change volume
  ibm.spectrum_virtualize.ibm_svc_manage_replication:
    name: sample_rcopy4
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/ansible.log
    state: present
    remotecluster: "{{remotecluster}}"
    master: SourceVolume1
    aux: TargetVolume1
    copytype: GMCV
    sync: true
  register: result
```

### Authors

- rohit(@rohitk-github)
- Shilpi Jain (@Shilpi-Jain1)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
[Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
