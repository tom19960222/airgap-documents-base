---
collection: ansible
version: "8"
title: "community.general.scaleway_volume module – Scaleway volumes management module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/scaleway_volume_module.html
fetched_at: 2026-07-28T01:50:26+00:00
---
# community.general.scaleway_volume module – Scaleway volumes management module

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
> To use it in a playbook, specify: `community.general.scaleway_volume`.

- [Synopsis](scaleway_volume_module.md#synopsis)
- [Parameters](scaleway_volume_module.md#parameters)
- [Attributes](scaleway_volume_module.md#attributes)
- [Notes](scaleway_volume_module.md#notes)
- [Examples](scaleway_volume_module.md#examples)
- [Return Values](scaleway_volume_module.md#return-values)

## [Synopsis](scaleway_volume_module.md#id1)

- This module manages volumes on Scaleway account <https://developer.scaleway.com>.

Aliases: cloud.scaleway.scaleway_volume

## [Parameters](scaleway_volume_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  **Default:** `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  **Default:** `"https://api.scaleway.com"` |
| **name**  string / required | Name used to identify the volume. |
| **organization**  string | ScaleWay organization ID to which volume belongs. |
| **project**  string  *added in community.general 4.3.0* | Scaleway project ID to which volume belongs. |
| **query_parameters**  dictionary | List of parameters passed to the query string.  **Default:** `{}` |
| **region**  string / required | Scaleway region to use (for example par1).  **Choices:**   - `"ams1"` - `"EMEA-NL-EVS"` - `"par1"` - `"EMEA-FR-PAR1"` - `"par2"` - `"EMEA-FR-PAR2"` - `"waw1"` - `"EMEA-PL-WAW1"` |
| **size**  integer | Size of the volume in bytes. |
| **state**  string | Indicate desired state of the volume.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  **Choices:**   - `false` - `true` ← (default) |
| **volume_type**  string | Type of the volume (for example ‘l_ssd’). |

## [Attributes](scaleway_volume_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](scaleway_volume_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence [`SCW_TOKEN`](../../environment_variables.md#envvar-SCW_TOKEN), [`SCW_API_KEY`](../../environment_variables.md#envvar-SCW_API_KEY), [`SCW_OAUTH_TOKEN`](../../environment_variables.md#envvar-SCW_OAUTH_TOKEN) or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_volume_module.md#id5)

```yaml+jinja
- name: Create 10GB volume
  community.general.scaleway_volume:
    name: my-volume
    state: present
    region: par1
    project: "{{ scw_org }}"
    "size": 10000000000
    volume_type: l_ssd
  register: server_creation_check_task

- name: Make sure volume deleted
  community.general.scaleway_volume:
    name: my-volume
    state: absent
    region: par1
```

## [Return Values](scaleway_volume_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | This is only present when `state=present`.  **Returned:** when `state=present`  **Sample:** `{"volume": {"export_uri": null, "id": "c675f420-cfeb-48ff-ba2a-9d2a4dbe3fcd", "name": "volume-0-3", "project": "000a115d-2852-4b0a-9ce8-47f1134ba95a", "server": null, "size": 10000000000, "volume_type": "l_ssd"}}` |

### Authors

- Henryk Konsek (@hekonsek)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
