---
collection: ansible
version: "8"
title: "ibm.spectrum_virtualize.ibm_sv_manage_fc_partnership module – This module configures and manages Fibre Channel (FC) partnership on IBM Spectrum Virtualize family storage systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/spectrum_virtualize/ibm_sv_manage_fc_partnership_module.html
fetched_at: 2026-07-28T02:34:39+00:00
---
# ibm.spectrum_virtualize.ibm_sv_manage_fc_partnership module – This module configures and manages Fibre Channel (FC) partnership on IBM Spectrum Virtualize family storage systems

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
> To use it in a playbook, specify: `ibm.spectrum_virtualize.ibm_sv_manage_fc_partnership`.

New in ibm.spectrum_virtualize 1.12.0

- [Synopsis](ibm_sv_manage_fc_partnership_module.md#synopsis)
- [Parameters](ibm_sv_manage_fc_partnership_module.md#parameters)
- [Notes](ibm_sv_manage_fc_partnership_module.md#notes)
- [Examples](ibm_sv_manage_fc_partnership_module.md#examples)

## [Synopsis](ibm_sv_manage_fc_partnership_module.md#id1)

- Ansible interface to manage mkfcpartnership, chpartnership, and rmpartnership commands.

## [Parameters](ibm_sv_manage_fc_partnership_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backgroundcopyrate**  string | Specifies the maximum percentage of aggregate link bandwidth that can be used for background copy operations. The value must be in the range of 0 - 100. The default value is 50.  Valid when *state=present*. |
| **clustername**  string / required | The hostname or management IP of the Spectrum Virtualize storage system. |
| **domain**  string | Domain for the Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *clustername*. |
| **linkbandwidthmbits**  string | Specifies the aggregate bandwidth of the remote copy link between two clustered systems (systems) in megabits per second (Mbps). The value must be in the range of 1 - 100000.  Valid when *state=present*. |
| **log_path**  string | Path of debug log file. |
| **password**  string | REST API password for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **pbrinuse**  string | Specifies whether policy-based replication will be used on the partnership.  Valid when *state=present* to update a partnership.  **Choices:**   - `"yes"` - `"no"` |
| **remote_clustername**  string | The hostname or management IP of the remote Spectrum Virtualize storage system. |
| **remote_domain**  string | Domain for the remote Spectrum Virtualize storage system.  Valid when hostname is used for the parameter *remote_clustername*. |
| **remote_password**  string | REST API password for the remote Spectrum Virtualize storage system.  The parameters *remote_username* and *remote_password* are required if not using *remote_token* to authenticate a user. |
| **remote_system**  string | Specifies the partner system ID or name. |
| **remote_token**  string | The authentication token to verify a user on the remote Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **remote_username**  string | REST API username for the remote Spectrum Virtualize storage system.  The parameters *remote_username* and *remote_password* are required if not using *remote_token* to authenticate a user. |
| **remote_validate_certs**  boolean | Validates certification for the remote Spectrum Virtualize storage system.  **Choices:**   - `false` ← (default) - `true` |
| **start**  boolean | Specifies to start a partnership.  Valid when *state=present*.  **Choices:**   - `false` - `true` |
| **state**  string / required | Creates or updates (`present`) or removes (`absent`) a FC partnership.  **Choices:**   - `"present"` - `"absent"` |
| **stop**  boolean | Specifies to stop a partnership.  Valid when *state=present* to update a partnership.  **Choices:**   - `false` - `true` |
| **token**  string | The authentication token to verify a user on the Spectrum Virtualize storage system.  To generate a token, use the [ibm.spectrum_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-spectrum-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Spectrum Virtualize storage system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification for the local Spectrum Virtualize storage system.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_sv_manage_fc_partnership_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_fc_partnership_module.md#id4)

```yaml+jinja
- name: Create an FC partnership and start the partnership
  ibm.spectrum_virtualize.ibm_sv_manage_fc_partnership:
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    remote_clustername: "{{remote_clustername}}"
    remote_username: "{{remote_username}}"
    remote_password: "{{remote_password}}"
    remote_system: "{{remote_system}}"
    linkbandwidthmbits: 50
    backgroundcopyrate: 50
    start: True
    state: present
- name: Update an FC partnership and stop the partnership
  ibm.spectrum_virtualize.ibm_sv_manage_fc_partnership:
    clustername: "{{clustername}}"
    username: "{{username}}"
    password: "{{password}}"
    remote_clustername: "{{remote_clustername}}"
    remote_username: "{{remote_username}}"
    remote_password: "{{remote_password}}"
    remote_system: "{{remote_system}}"
    linkbandwidthmbits: 40
    backgroundcopyrate: 20
    stop: True
    state: present
- name: Delete the FC partnership
  ibm.spectrum_virtualize.ibm_sv_manage_fc_partnership:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    remote_clustername: "{{remote_clustername}}"
    remote_username: "{{remote_username}}"
    remote_password: "{{remote_password}}"
    remote_system: "{{remote_system}}"
    state: absent
```

### Authors

- Sanjaikumaar M (@sanjaikumaar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.spectrum_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.spectrum_virtualize)
