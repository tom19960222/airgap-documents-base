---
collection: ansible
version: "6"
title: "community.general.proxmox_group_info module – Retrieve information about one or more Proxmox VE groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/proxmox_group_info_module.html
fetched_at: 2026-07-27T17:12:08+00:00
---
# community.general.proxmox_group_info module – Retrieve information about one or more Proxmox VE groups

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](proxmox_group_info_module.md#ansible-collections-community-general-proxmox-group-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox_group_info`.

New in community.general 1.3.0

- [Synopsis](proxmox_group_info_module.md#synopsis)
- [Requirements](proxmox_group_info_module.md#requirements)
- [Parameters](proxmox_group_info_module.md#parameters)
- [Examples](proxmox_group_info_module.md#examples)
- [Return Values](proxmox_group_info_module.md#return-values)

## [Synopsis](proxmox_group_info_module.md#id1)

- Retrieve information about one or more Proxmox VE groups

## [Requirements](proxmox_group_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- requests

## [Parameters](proxmox_group_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use `PROXMOX_PASSWORD` environment variable. |
| **api_token_id**  string  added in community.general 1.3.0 | Specify the token ID. |
| **api_token_secret**  string  added in community.general 1.3.0 | Specify the token secret. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **group**  aliases: groupid, name  string | Restrict results to a specific group. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  Choices:   - `false` ← (default) - `true` |

## [Examples](proxmox_group_info_module.md#id4)

```yaml+jinja
- name: List existing groups
  community.general.proxmox_group_info:
    api_host: helldorado
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
  register: proxmox_groups

- name: Retrieve information about the admin group
  community.general.proxmox_group_info:
    api_host: helldorado
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
    group: admin
  register: proxmox_group_admin
```

## [Return Values](proxmox_group_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **proxmox_groups**  list / elements=dictionary | List of groups.  Returned: always, but can be empty |
| **comment**  string | Short description of the group.  Returned: on success, can be absent |
| **groupid**  string | Group name.  Returned: on success |
| **users**  list / elements=string | List of users in the group.  Returned: on success |

### Authors

- Tristan Le Guern (@tleguern)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
