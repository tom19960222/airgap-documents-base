---
collection: ansible
version: "8"
title: "ibm.storage_virtualize.ibm_svc_auth module – This module generates an authentication token for a user on IBM Storage Virtualize family system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ibm/storage_virtualize/ibm_svc_auth_module.html
fetched_at: 2026-07-28T02:35:24+00:00
---
# ibm.storage_virtualize.ibm_svc_auth module – This module generates an authentication token for a user on IBM Storage Virtualize family system

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
> To use it in a playbook, specify: `ibm.storage_virtualize.ibm_svc_auth`.

New in ibm.storage_virtualize 1.5.0

- [Synopsis](ibm_svc_auth_module.md#synopsis)
- [Parameters](ibm_svc_auth_module.md#parameters)
- [Notes](ibm_svc_auth_module.md#notes)
- [Examples](ibm_svc_auth_module.md#examples)
- [Return Values](ibm_svc_auth_module.md#return-values)

## [Synopsis](ibm_svc_auth_module.md#id1)

- Ansible interface to generate the authentication token. The token is used to make REST API calls to the storage system.

## [Parameters](ibm_svc_auth_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clustername**  string / required | The hostname or management IP of the Storage Virtualize system. |
| **domain**  string | Domain for the Storage Virtualize system.  Valid when hostname is used for the parameter *clustername*. |
| **log_path**  string | Path of debug log file. |
| **password**  string | REST API password for the Storage Virtualize system.  This parameter is required in this module to generate the token. |
| **token**  string | The authentication token to verify a user on the Storage Virtualize system.  This field is not required for ibm_svc_auth module. |
| **username**  string | REST API username for the Storage Virtualize system.  This parameter is required in this module to generate the token. |
| **validate_certs**  boolean | Validates certification.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](ibm_svc_auth_module.md#id3)

> **Note:**
>
> - This module supports `check_mode`.

## [Examples](ibm_svc_auth_module.md#id4)

```yaml+jinja
- name: Obtain an authentication token
  register: result
  ibm.storage_virtualize.ibm_svc_auth:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
- name: Create a volume
  ibm.storage_virtualize.ibm_svc_manage_volume:
    clustername: "{{clustername}}"
    domain: "{{domain}}"
    username: "{{username}}"
    password: "{{password}}"
    token: "{{result.token}}"
    name: volume0
    state: present
    pool: Pool0
    size: "4294967296"
    unit: b
```

## [Return Values](ibm_svc_auth_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **token**  string  *added in ibm.storage_virtualize 1.5.0* | Authentication token for a user.  **Returned:** success |

### Authors

- Shilpi Jain(@Shilpi-J)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ibm.storage_virtualize/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ibm.storage_virtualize)
- [Report an issue](https://github.com/ansible-collections/community.REPO_NAME/issues/new/choose)
- [Communication](index.md#communication-for-ibm-storage-virtualize)
