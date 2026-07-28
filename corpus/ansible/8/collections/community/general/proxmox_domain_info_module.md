---
collection: ansible
version: "8"
title: "community.general.proxmox_domain_info module – Retrieve information about one or more Proxmox VE domains"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/proxmox_domain_info_module.html
fetched_at: 2026-07-28T01:49:17+00:00
---
# community.general.proxmox_domain_info module – Retrieve information about one or more Proxmox VE domains

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
> see [Requirements](proxmox_domain_info_module.md#ansible-collections-community-general-proxmox-domain-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.proxmox_domain_info`.

New in community.general 1.3.0

- [Synopsis](proxmox_domain_info_module.md#synopsis)
- [Requirements](proxmox_domain_info_module.md#requirements)
- [Parameters](proxmox_domain_info_module.md#parameters)
- [Attributes](proxmox_domain_info_module.md#attributes)
- [Examples](proxmox_domain_info_module.md#examples)
- [Return Values](proxmox_domain_info_module.md#return-values)

## [Synopsis](proxmox_domain_info_module.md#id1)

- Retrieve information about one or more Proxmox VE domains.

Aliases: cloud.misc.proxmox_domain_info

## [Requirements](proxmox_domain_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- proxmoxer
- requests

## [Parameters](proxmox_domain_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_host**  string / required | Specify the target host of the Proxmox VE cluster. |
| **api_password**  string | Specify the password to authenticate with.  You can use [`PROXMOX_PASSWORD`](../../environment_variables.md#envvar-PROXMOX_PASSWORD) environment variable. |
| **api_token_id**  string  *added in community.general 1.3.0* | Specify the token ID.  Requires `proxmoxer>=1.1.0` to work. |
| **api_token_secret**  string  *added in community.general 1.3.0* | Specify the token secret.  Requires `proxmoxer>=1.1.0` to work. |
| **api_user**  string / required | Specify the user to authenticate with. |
| **domain**  aliases: realm, name  string | Restrict results to a specific authentication realm. |
| **validate_certs**  boolean | If `false`, SSL certificates will not be validated.  This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](proxmox_domain_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](proxmox_domain_info_module.md#id5)

```yaml+jinja
- name: List existing domains
  community.general.proxmox_domain_info:
    api_host: helldorado
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
  register: proxmox_domains

- name: Retrieve information about the pve domain
  community.general.proxmox_domain_info:
    api_host: helldorado
    api_user: root@pam
    api_password: "{{ password | default(omit) }}"
    api_token_id: "{{ token_id | default(omit) }}"
    api_token_secret: "{{ token_secret | default(omit) }}"
    domain: pve
  register: proxmox_domain_pve
```

## [Return Values](proxmox_domain_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **proxmox_domains**  list / elements=dictionary | List of authentication domains.  **Returned:** always, but can be empty |
| **comment**  string | Short description of the realm.  **Returned:** on success |
| **digest**  string | Realm hash.  **Returned:** on success, can be absent |
| **realm**  string | Realm name.  **Returned:** on success |
| **type**  string | Realm type.  **Returned:** on success |

### Authors

- Tristan Le Guern (@tleguern)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
