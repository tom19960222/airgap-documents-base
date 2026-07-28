---
collection: ansible
version: "6"
title: "community.general.scaleway_ip module – Scaleway IP management module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/scaleway_ip_module.html
fetched_at: 2026-07-27T17:12:57+00:00
---
# community.general.scaleway_ip module – Scaleway IP management module

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.scaleway_ip`.

- [Synopsis](scaleway_ip_module.md#synopsis)
- [Parameters](scaleway_ip_module.md#parameters)
- [Notes](scaleway_ip_module.md#notes)
- [Examples](scaleway_ip_module.md#examples)
- [Return Values](scaleway_ip_module.md#return-values)

## [Synopsis](scaleway_ip_module.md#id1)

- This module manages IP on Scaleway account <https://developer.scaleway.com>

## [Parameters](scaleway_ip_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  Default: `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  Default: `"https://api.scaleway.com"` |
| **id**  string | id of the Scaleway IP (UUID) |
| **organization**  string / required | Scaleway organization identifier |
| **query_parameters**  dictionary | List of parameters passed to the query string.  Default: `{}` |
| **region**  string / required | Scaleway region to use (for example par1).  Choices:   - `"ams1"` - `"EMEA-NL-EVS"` - `"par1"` - `"EMEA-FR-PAR1"` - `"par2"` - `"EMEA-FR-PAR2"` - `"waw1"` - `"EMEA-PL-WAW1"` |
| **reverse**  string | Reverse to assign to the IP |
| **server**  string | id of the server you want to attach an IP to.  To unattach an IP don’t specify this option |
| **state**  string | Indicate desired state of the IP.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  Choices:   - `false` - `true` ← (default) |

## [Notes](scaleway_ip_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence `SCW_TOKEN`, `SCW_API_KEY`, `SCW_OAUTH_TOKEN` or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_ip_module.md#id4)

```yaml+jinja
- name: Create an IP
  community.general.scaleway_ip:
    organization: '{{ scw_org }}'
    state: present
    region: par1
  register: ip_creation_task

- name: Make sure IP deleted
  community.general.scaleway_ip:
    id: '{{ ip_creation_task.scaleway_ip.id }}'
    state: absent
    region: par1
```

## [Return Values](scaleway_ip_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | This is only present when `state=present`  Returned: when `state=present`  Sample: `{"ips": [{"address": "212.47.232.136", "id": "dd9e8df6-6775-4863-b517-e0b0ee3d7477", "organization": "951df375-e094-4d26-97c1-ba548eeb9c42", "reverse": null, "server": {"id": "3f1568ca-b1a2-4e98-b6f7-31a0588157f1", "name": "ansible_tuto-1"}}]}` |

### Authors

- Remy Leone (@remyleone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
