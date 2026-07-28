---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_svc_manage_cv module – This module manages the change volume for a given volume on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_svc_manage_cv_module.html
fetched_at: 2026-07-28T02:34:54+00:00
---
# ibm.spectrum_virtualize.ibm_svc_manage_cv module – This module manages the change volume for a given volume on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_svc_manage_cv`.

New in ibm.spectrum_virtualize 1.3.0

- [Synopsis](ibm_svc_manage_cv_module.md#synopsis)
- [Parameters](ibm_svc_manage_cv_module.md#parameters)
- [Notes](ibm_svc_manage_cv_module.md#notes)
- [Examples](ibm_svc_manage_cv_module.md#examples)

## [Synopsis](ibm_svc_manage_cv_module.md#id1)

- Ansible interface to manage the change volume in remote copy replication on IBM Spectrum Virtualize family storage systems.

## [Parameters](ibm_svc_manage_cv_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **basevolume**  string | Specifies the base volume name (master or auxiliary).  Required when *state=present*, to create the change volume. |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **cvname**  string / required | Specifies the name to assign to the master or auxiliary change volume. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **ismaster**  boolean | Specifies whether the change volume is being (dis)associated with master cluster.  Required when the change volume is being associated or disassociated from the master cluster.  **Choices:**   - `false` - `true` ← (default) |
| **log_path**  string | Path of debug log file. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **rname**  string / required | Specifies the name of the remote copy relationship. |
| **state**  string / required | Creates or updates (`present`) or removes (`absent`), a change volume.  **Choices:**   - `"absent"` - `"present"` |
| **token**  string  *added in ibm.spectrum_virtualize 1.5.0* | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the ibm_svc_auth module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_manage_cv_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_manage_cv_module.md#id4)

```yaml+jinja
- name: Create master change volume and associate with rcopy
  ibm.spectrum_virtualize.ibm_svc_manage_cv:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    state: present
    rname: sample_rcopy
    cvname: vol1_cv
    basevolume: vol1
- name: Create auxiliary change volume and associate with rcopy
  ibm.spectrum_virtualize.ibm_svc_manage_cv:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    state: present
    rname: sample_rcopy
    cvname: vol2_aux_cv
    basevolume: vol2
    ismaster: false
- name: Delete master change volume and disassociate from rcopy
  ibm.spectrum_virtualize.ibm_svc_manage_cv:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    state: absent
    rname: sample_rcopy
    cvname: vol1_cv
- name: Delete auxiliary change volume and disassociate from rcopy
  ibm.spectrum_virtualize.ibm_svc_manage_cv:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    log_path: /tmp/playbook.debug
    state: absent
    rname: sample_rcopy
    cvname: vol2_aux_cv
    ismaster: false
```

### Authors

- Shilpi Jain(@Shilpi-Jain1)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
