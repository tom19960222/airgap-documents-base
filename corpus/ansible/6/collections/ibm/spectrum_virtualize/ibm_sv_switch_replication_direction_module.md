---
collection: ansible
version: "6"
title: "ibm.spectrum_virtualize.ibm_sv_switch_replication_direction module – This module switches the replication direction on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ibm/spectrum_virtualize/ibm_sv_switch_replication_direction_module.html
fetched_at: 2026-07-27T17:50:23+00:00
---
# ibm.spectrum_virtualize.ibm_sv_switch_replication_direction module – This module switches the replication direction on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_sv_switch_replication_direction`.

New in ibm.spectrum_virtualize 1.10.0

- [Synopsis](ibm_sv_switch_replication_direction_module.md#synopsis)
- [Parameters](ibm_sv_switch_replication_direction_module.md#parameters)
- [Notes](ibm_sv_switch_replication_direction_module.md#notes)
- [Examples](ibm_sv_switch_replication_direction_module.md#examples)

## [Synopsis](ibm_sv_switch_replication_direction_module.md#id1)

- Ansible interface to manage the chvolumegroupreplication command.
- This module can be used to switch replication direction.

## [Parameters](ibm_sv_switch_replication_direction_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when the hostname is used for the parameter *clustername*. |
| **log_path**  string | Path of debug log file. |
| **mode**  string / required | Specifies the replication mode of the volume group.  Choices:   - `"independent"` - `"production"` |
| **name**  string / required | Specifies the name of the volume group. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **token**  string | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  Choices:   - `false` ← (default) - `true` |

## [Notes](ibm_sv_switch_replication_direction_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_switch_replication_direction_module.md#id4)

```yaml+jinja
- name: Switch to independent mode
  ibm.spectrum_virtualize.ibm_sv_switch_replication_direction:
    clustername: "{{ clustername }}"
    username: "{{ username }}"
    password: "{{ password }}"
    mode: independent
    name: vg0
```

### Authors

- Shilpi Jain(@Shilpi-J)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
[Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
