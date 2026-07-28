---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_sv_manage_fc_partnership module – This module configures and manages Fibre Channel (FC) partnership on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_sv_manage_fc_partnership_module.html
fetched_at: 2026-07-28T02:35:14+00:00
---
# ibm.storage_virtualize.ibm_sv_manage_fc_partnership module – This module configures and manages Fibre Channel (FC) partnership on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_sv_manage_fc_partnership`.

New in ibm.storage_virtualize 1.12.0

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
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **linkbandwidthmbits**  string | Specifies the aggregate bandwidth of the remote copy link between two clustered systems (systems) in megabits per second (Mbps). The value must be in the range of 1 - 100000.  Valid when *state=present*. |
| **log_path**  string | Path of debug log file. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **pbrinuse**  string | Specifies whether policy-based replication will be used on the partnership.  Valid when *state=present* to update a partnership.  **Choices:**   - `"yes"` - `"no"` |
| **remote_clustername**  string | The hostname or management IP of the remote Storage Virtualize system. |
| **remote_domain**  string | Domain for the remote Storage Virtualize system.  Valid when hostname is used for the parameter *remote_clustername*. |
| **remote_password**  string | REST API password for the remote Storage Virtualize system.  The parameters *remote_username* and *remote_password* are required if not using *remote_token* to authenticate a user. |
| **remote_system**  string | Specifies the partner system ID or name. |
| **remote_token**  string | The authentication token to verify a user on the remote Storage Virtualize system.  To generate a token, use the [ibm.storage_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) module. |
| **remote_username**  string | REST API username for the remote Storage Virtualize system.  The parameters *remote_username* and *remote_password* are required if not using *remote_token* to authenticate a user. |
| **remote_validate_certs**  boolean | Validates certification for the remote Storage Virtualize system.  **Choices:**   - `false` ← (default) - `true` |
| **start**  boolean | Specifies to start a partnership.  Valid when *state=present*.  **Choices:**   - `false` - `true` |
| **state**  string / required | Creates or updates (`present`) or removes (`absent`) a FC partnership.  **Choices:**   - `"present"` - `"absent"` |
| **stop**  boolean | Specifies to stop a partnership.  Valid when *state=present* to update a partnership.  **Choices:**   - `false` - `true` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the [ibm.storage_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification for the local Storage Virtualize system.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_sv_manage_fc_partnership_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_fc_partnership_module.md#id4)

```yaml+jinja
- name: Create an FC partnership and start the partnership
  ibm.storage_virtualize.ibm_sv_manage_fc_partnership:
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
  ibm.storage_virtualize.ibm_sv_manage_fc_partnership:
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
  ibm.storage_virtualize.ibm_sv_manage_fc_partnership:
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

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
