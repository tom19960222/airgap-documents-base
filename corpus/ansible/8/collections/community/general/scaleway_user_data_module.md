---
collection: ansible
version: "8"
title: "community.general.scaleway_user_data module – Scaleway user_data management module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/scaleway_user_data_module.html
fetched_at: 2026-07-28T01:50:25+00:00
---
# community.general.scaleway_user_data module – Scaleway user_data management module

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.scaleway_user_data`.

- [Synopsis](scaleway_user_data_module.md#synopsis)
- [Parameters](scaleway_user_data_module.md#parameters)
- [Attributes](scaleway_user_data_module.md#attributes)
- [Notes](scaleway_user_data_module.md#notes)
- [Examples](scaleway_user_data_module.md#examples)

## [Synopsis](scaleway_user_data_module.md#id1)

- This module manages user_data on compute instances on Scaleway.
- It can be used to configure cloud-init for instance.

Aliases: cloud.scaleway.scaleway_user_data

## [Parameters](scaleway_user_data_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  **Default:** `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  **Default:** `"https://api.scaleway.com"` |
| **query_parameters**  dictionary | List of parameters passed to the query string.  **Default:** `{}` |
| **region**  string / required | Scaleway compute zone.  **Choices:**   - `"ams1"` - `"EMEA-NL-EVS"` - `"par1"` - `"EMEA-FR-PAR1"` - `"par2"` - `"EMEA-FR-PAR2"` - `"waw1"` - `"EMEA-PL-WAW1"` |
| **server_id**  string / required | Scaleway Compute instance ID of the server. |
| **user_data**  dictionary | User defined data. Typically used with `cloud-init`.  Pass your `cloud-init` script here as a string. |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](scaleway_user_data_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](scaleway_user_data_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence [`SCW_TOKEN`](../../environment_variables.md#envvar-SCW_TOKEN), [`SCW_API_KEY`](../../environment_variables.md#envvar-SCW_API_KEY), [`SCW_OAUTH_TOKEN`](../../environment_variables.md#envvar-SCW_OAUTH_TOKEN) or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_user_data_module.md#id5)

```yaml+jinja
- name: Update the cloud-init
  community.general.scaleway_user_data:
    server_id: '5a33b4ab-57dd-4eb6-8b0a-d95eb63492ce'
    region: ams1
    user_data:
      cloud-init: 'final_message: "Hello World!"'
```

### Authors

- Remy Leone (@remyleone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
