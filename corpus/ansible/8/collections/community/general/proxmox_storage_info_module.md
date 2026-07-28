---
collection: ansible
version: "8"
title: "community.general.proxmox_storage_info module – Retrieve information about one or more Proxmox VE storages"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/proxmox_storage_info_module.html
fetched_at: 2026-07-28T01:49:22+00:00
---
# community.general.proxmox_storage_info module – Retrieve information about one or more Proxmox VE storages

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
> see [Requirements](proxmox_storage_info_module.md#ansible-collections-community-general-proxmox-storage-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox_storage_info`.

New in community.general 2.2.0

- [Synopsis](proxmox_storage_info_module.md#synopsis)
- [Requirements](proxmox_storage_info_module.md#requirements)
- [Parameters](proxmox_storage_info_module.md#parameters)
- [Attributes](proxmox_storage_info_module.md#attributes)
- [Notes](proxmox_storage_info_module.md#notes)
- [Examples](proxmox_storage_info_module.md#examples)
- [Return Values](proxmox_storage_info_module.md#return-values)

## [Synopsis](proxmox_storage_info_module.md#id1)

- Retrieve information about one or more Proxmox VE storages.

Aliases: cloud.misc.proxmox_storage_info

## [Requirements](proxmox_storage_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- requests

## [Parameters](proxmox_storage_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use [`PROXMOX_PASSWORD`](../../environment_variables.md#envvar-PROXMOX_PASSWORD) environment variable. |
| **api_token_id**  string  *added in community.general 1.3.0* | Specify the token ID.  Requires `proxmoxer>=1.1.0` to work. |
| **api_token_secret**  string  *added in community.general 1.3.0* | Specify the token secret.  Requires `proxmoxer>=1.1.0` to work. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **storage**  aliases: name  string | Only return information on a specific storage. |
| **type**  string | Filter on a specific storage type. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](proxmox_storage_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](proxmox_storage_info_module.md#id5)

> **Note:**
>
> - Storage specific options can be returned by this module, please look at the documentation at <https://pve.proxmox.com/wiki/Storage>.

## [Examples](proxmox_storage_info_module.md#id6)

```yaml+jinja
- name: List existing storages
  community.general.proxmox_storage_info:
    api_host: helldorado
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
  register: proxmox_storages

- name: List NFS storages only
  community.general.proxmox_storage_info:
    api_host: helldorado
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
    type: nfs
  register: proxmox_storages_nfs

- name: Retrieve information about the lvm2 storage
  community.general.proxmox_storage_info:
    api_host: helldorado
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
    storage: lvm2
  register: proxmox_storage_lvm
```

## [Return Values](proxmox_storage_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **proxmox_storages**  list / elements=dictionary | List of storage pools.  **Returned:** on success |
| **content**  list / elements=string | Proxmox content types available in this storage  **Returned:** on success |
| **digest**  string | Storage’s digest  **Returned:** on success |
| **nodes**  list / elements=string | List of nodes associated to this storage  **Returned:** on success, if storage is not local |
| **path**  string | Physical path to this storage  **Returned:** on success |
| **prune-backups**  list / elements=dictionary | Backup retention options  **Returned:** on success |
| **shared**  boolean | Is this storage shared  **Returned:** on success |
| **storage**  string | Storage name  **Returned:** on success |
| **type**  string | Storage type  **Returned:** on success |

### Authors

- Tristan Le Guern (@tleguern)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
