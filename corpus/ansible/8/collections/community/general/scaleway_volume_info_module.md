---
collection: ansible
version: "8"
title: "community.general.scaleway_volume_info module – Gather information about the Scaleway volumes available"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/scaleway_volume_info_module.html
fetched_at: 2026-07-28T01:50:27+00:00
---
# community.general.scaleway_volume_info module – Gather information about the Scaleway volumes available

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
> To use it in a playbook, specify: `community.general.scaleway_volume_info`.

- [Synopsis](scaleway_volume_info_module.md#synopsis)
- [Parameters](scaleway_volume_info_module.md#parameters)
- [Attributes](scaleway_volume_info_module.md#attributes)
- [Notes](scaleway_volume_info_module.md#notes)
- [Examples](scaleway_volume_info_module.md#examples)
- [Return Values](scaleway_volume_info_module.md#return-values)

## [Synopsis](scaleway_volume_info_module.md#id1)

- Gather information about the Scaleway volumes available.

Aliases: cloud.scaleway.scaleway_volume_info

## [Parameters](scaleway_volume_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  **Default:** `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  **Default:** `"https://api.scaleway.com"` |
| **query_parameters**  dictionary | List of parameters passed to the query string.  **Default:** `{}` |
| **region**  string / required | Scaleway region to use (for example `par1`).  **Choices:**   - `"ams1"` - `"EMEA-NL-EVS"` - `"par1"` - `"EMEA-FR-PAR1"` - `"par2"` - `"EMEA-FR-PAR2"` - `"waw1"` - `"EMEA-PL-WAW1"` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](scaleway_volume_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](scaleway_volume_info_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence [`SCW_TOKEN`](../../environment_variables.md#envvar-SCW_TOKEN), [`SCW_API_KEY`](../../environment_variables.md#envvar-SCW_API_KEY), [`SCW_OAUTH_TOKEN`](../../environment_variables.md#envvar-SCW_OAUTH_TOKEN) or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_volume_info_module.md#id5)

```yaml+jinja
- name: Gather Scaleway volumes information
  community.general.scaleway_volume_info:
    region: par1
  register: result

- ansible.builtin.debug:
    msg: "{{ result.scaleway_volume_info }}"
```

## [Return Values](scaleway_volume_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **scaleway_volume_info**  list / elements=dictionary | Response from Scaleway API.  For more details please refer to: <https://developers.scaleway.com/en/products/instance/api/>.  **Returned:** success  **Sample:** `{"scaleway_volume_info": [{"creation_date": "2018-08-14T20:56:24.949660+00:00", "export_uri": null, "id": "b8d51a06-daeb-4fef-9539-a8aea016c1ba", "modification_date": "2018-08-14T20:56:24.949660+00:00", "name": "test-volume", "organization": "3f709602-5e6c-4619-b80c-e841c89734af", "server": null, "size": 50000000000, "state": "available", "volume_type": "l_ssd"}]}` |

### Authors

- Yanis Guenane (@Spredzy)
- Remy Leone (@remyleone)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
