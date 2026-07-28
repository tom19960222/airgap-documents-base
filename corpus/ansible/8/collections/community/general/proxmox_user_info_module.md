---
collection: ansible
version: "8"
title: "community.general.proxmox_user_info module – Retrieve information about one or more Proxmox VE users"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/proxmox_user_info_module.html
fetched_at: 2026-07-28T01:49:25+00:00
---
# community.general.proxmox_user_info module – Retrieve information about one or more Proxmox VE users

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
> see [Requirements](proxmox_user_info_module.md#ansible-collections-community-general-proxmox-user-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox_user_info`.

New in community.general 1.3.0

- [Synopsis](proxmox_user_info_module.md#synopsis)
- [Requirements](proxmox_user_info_module.md#requirements)
- [Parameters](proxmox_user_info_module.md#parameters)
- [Attributes](proxmox_user_info_module.md#attributes)
- [Examples](proxmox_user_info_module.md#examples)
- [Return Values](proxmox_user_info_module.md#return-values)

## [Synopsis](proxmox_user_info_module.md#id1)

- Retrieve information about one or more Proxmox VE users

Aliases: cloud.misc.proxmox_user_info

## [Requirements](proxmox_user_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- requests

## [Parameters](proxmox_user_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use [`PROXMOX_PASSWORD`](../../environment_variables.md#envvar-PROXMOX_PASSWORD) environment variable. |
| **api_token_id**  string  *added in community.general 1.3.0* | Specify the token ID.  Requires `proxmoxer>=1.1.0` to work. |
| **api_token_secret**  string  *added in community.general 1.3.0* | Specify the token secret.  Requires `proxmoxer>=1.1.0` to work. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **domain**  aliases: realm  string | Restrict results to a specific authentication realm. |
| **user**  aliases: name  string | Restrict results to a specific user. |
| **userid**  string | Restrict results to a specific user ID, which is a concatenation of a user and domain parts. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](proxmox_user_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](proxmox_user_info_module.md#id5)

```yaml+jinja
- name: List existing users
  community.general.proxmox_user_info:
    api_host: helldorado
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
  register: proxmox_users

- name: List existing users in the pve authentication realm
  community.general.proxmox_user_info:
    api_host: helldorado
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
    domain: pve
  register: proxmox_users_pve

- name: Retrieve information about admin@pve
  community.general.proxmox_user_info:
    api_host: helldorado
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
    userid: admin@pve
  register: proxmox_user_admin

- name: Alternative way to retrieve information about admin@pve
  community.general.proxmox_user_info:
    api_host: helldorado
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
    user: admin
    domain: pve
  register: proxmox_user_admin
```

## [Return Values](proxmox_user_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **proxmox_users**  list / elements=dictionary | List of users.  **Returned:** always, but can be empty |
| **comment**  string | Short description of the user.  **Returned:** on success |
| **domain**  string | User’s authentication realm, also the right part of the user ID.  **Returned:** on success |
| **email**  string | User’s email address.  **Returned:** on success |
| **enabled**  boolean | User’s account state.  **Returned:** on success |
| **expire**  integer | Expiration date in seconds since EPOCH. Zero means no expiration.  **Returned:** on success |
| **firstname**  string | User’s first name.  **Returned:** on success |
| **groups**  list / elements=string | List of groups which the user is a member of.  **Returned:** on success |
| **keys**  string | User’s two factor authentication keys.  **Returned:** on success |
| **lastname**  string | User’s last name.  **Returned:** on success |
| **tokens**  list / elements=dictionary | List of API tokens associated to the user.  **Returned:** on success |
| **comment**  string | Short description of the token.  **Returned:** on success |
| **expire**  integer | Expiration date in seconds since EPOCH. Zero means no expiration.  **Returned:** on success |
| **privsep**  boolean | Describe if the API token is further restricted with ACLs or is fully privileged.  **Returned:** on success |
| **tokenid**  string | Token name.  **Returned:** on success |
| **user**  string | User’s login name, also the left part of the user ID.  **Returned:** on success |
| **userid**  string | Proxmox user ID, represented as [user@realm](mailto:user%40realm).  **Returned:** on success |

### Authors

- Tristan Le Guern (@tleguern)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
