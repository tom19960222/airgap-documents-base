---
collection: ansible
version: "8"
title: "community.general.proxmox_pool_member module – Add or delete members from Proxmox VE cluster pools"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/proxmox_pool_member_module.html
fetched_at: 2026-07-28T01:49:21+00:00
---
# community.general.proxmox_pool_member module – Add or delete members from Proxmox VE cluster pools

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](proxmox_pool_member_module.md#ansible-collections-community-general-proxmox-pool-member-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox_pool_member`.

New in community.general 7.1.0

- [Synopsis](proxmox_pool_member_module.md#synopsis)
- [Requirements](proxmox_pool_member_module.md#requirements)
- [Parameters](proxmox_pool_member_module.md#parameters)
- [Attributes](proxmox_pool_member_module.md#attributes)
- [Examples](proxmox_pool_member_module.md#examples)
- [Return Values](proxmox_pool_member_module.md#return-values)

## [Synopsis](proxmox_pool_member_module.md#id1)

- Create or delete a pool member in Proxmox VE clusters.

## [Requirements](proxmox_pool_member_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- requests

## [Parameters](proxmox_pool_member_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use [`PROXMOX_PASSWORD`](../../environment_variables.md#envvar-PROXMOX_PASSWORD) environment variable. |
| **api_token_id**  string  *added in community.general 1.3.0* | Specify the token ID.  Requires `proxmoxer>=1.1.0` to work. |
| **api_token_secret**  string  *added in community.general 1.3.0* | Specify the token secret.  Requires `proxmoxer>=1.1.0` to work. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **member**  string / required | Specify the member name.  For `type=storage` it is a storage name.  For `type=vm` either vmid or vm name could be used. |
| **poolid**  aliases: name  string / required | The pool ID. |
| **state**  string | Indicate desired state of the pool member.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string | Member type to add/remove from the pool.  **Choices:**   - `"vm"` ← (default) - `"storage"` |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](proxmox_pool_member_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](proxmox_pool_member_module.md#id5)

```yaml+jinja
- name: Add new VM to Proxmox VE pool
  community.general.proxmox_pool_member:
    api_host: node1
    api_user: root@pam
    api_password: password
    poolid: test
    member: 101

- name: Add new storage to Proxmox VE pool
  community.general.proxmox_pool_member:
    api_host: node1
    api_user: root@pam
    api_password: password
    poolid: test
    member: zfs-data
    type: storage

- name: Remove VM from the Proxmox VE pool using VM name
  community.general.proxmox_pool_member:
    api_host: node1
    api_user: root@pam
    api_password: password
    poolid: test
    member: pxe.home.arpa
    state: absent

- name: Remove storage from the Proxmox VE pool
  community.general.proxmox_pool_member:
    api_host: node1
    api_user: root@pam
    api_password: password
    poolid: test
    member: zfs-storage
    type: storage
    state: absent
```

## [Return Values](proxmox_pool_member_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **member**  string | Member name.  **Returned:** success  **Sample:** `"101"` |
| **msg**  string | A short message on what the module did.  **Returned:** always  **Sample:** `"Member 101 deleted from the pool test"` |
| **poolid**  string | The pool ID.  **Returned:** success  **Sample:** `"test"` |

### Authors

- Sergei Antipov (@UnderGreen)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
