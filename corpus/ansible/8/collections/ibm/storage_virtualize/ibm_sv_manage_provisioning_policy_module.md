---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_sv_manage_provisioning_policy module – This module configures and manages provisioning policies on IBM Storage Virtualize family systems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_sv_manage_provisioning_policy_module.html
fetched_at: 2026-07-28T02:35:16+00:00
---
# ibm.storage_virtualize.ibm_sv_manage_provisioning_policy module – This module configures and manages provisioning policies on IBM Storage Virtualize family systems

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_sv_manage_provisioning_policy`.

New in ibm.storage_virtualize 1.10.0

- [Synopsis](ibm_sv_manage_provisioning_policy_module.md#synopsis)
- [Parameters](ibm_sv_manage_provisioning_policy_module.md#parameters)
- [Notes](ibm_sv_manage_provisioning_policy_module.md#notes)
- [Examples](ibm_sv_manage_provisioning_policy_module.md#examples)

## [Synopsis](ibm_sv_manage_provisioning_policy_module.md#id1)

- Ansible interface to manage mkprovisioningpolicy, chprovisioningpolicy, and rmprovisioningpolicy commands.

## [Parameters](ibm_sv_manage_provisioning_policy_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **capacitysaving**  string | Specifies the policy capacity savings.  Applies, when *state=present*, to create a provisioning policy.  **Choices:**   - `"drivebased"` - `"thin"` - `"compressed"` |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **deduplicated**  boolean | Specifies when volumes should be deduplicated.  Applicable when *capacitysaving=thin* or *capacitysaving=compressed*.  **Choices:**   - `false` ← (default) - `true` |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **log_path**  string | Path of debug log file. |
| **name**  string / required | Specifies the name of the provisioning policy.  Specifies the new name during rename. |
| **old_name**  string | Specifies the old name of the provisioning policy during renaming.  Valid when *state=present* to rename an existing policy. |
| **password**  string | REST API password for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **state**  string / required | Creates, updates (`present`), or deletes (`absent`) a provisioning policy.  **Choices:**   - `"present"` - `"absent"` |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  To generate a token, use the [ibm.storage_virtualize.ibm_svc_auth](ibm_svc_auth_module.md#ansible-collections-ibm-storage-virtualize-ibm-svc-auth-module) module. |
| **username**  string | REST API username for the Storage Virtualize system.  The parameters *username* and *password* are required if not using *token* to authenticate a user. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_sv_manage_provisioning_policy_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_sv_manage_provisioning_policy_module.md#id4)

```yaml+jinja
- name: Create provisioning policy
  ibm.storage_virtualize.ibm_sv_manage_provisioning_policy:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    name: provisioning_policy0
    capacitysaving: "compressed"
    deduplicated: true
    state: present
- name: Rename provisioning policy
  ibm.storage_virtualize.ibm_sv_manage_provisioning_policy:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    name: pp0
    old_name: provisioning_policy0
    state: present
- name: Delete replication policy
  ibm.storage_virtualize.ibm_sv_manage_provisioning_policy:
    clustername: "{{cluster}}"
    username: "{{username}}"
    password: "{{password}}"
    name: pp0
    state: absent
```

### Authors

- Sanjaikumaar M (@sanjaikumaar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
