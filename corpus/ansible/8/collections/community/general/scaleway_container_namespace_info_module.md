---
collection: ansible
version: "8"
title: "community.general.scaleway_container_namespace_info module – Retrieve information on Scaleway Container namespace"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/scaleway_container_namespace_info_module.html
fetched_at: 2026-07-28T01:50:11+00:00
---
# community.general.scaleway_container_namespace_info module – Retrieve information on Scaleway Container namespace

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
> To use it in a playbook, specify: `community.general.scaleway_container_namespace_info`.

New in community.general 6.0.0

- [Synopsis](scaleway_container_namespace_info_module.md#synopsis)
- [Parameters](scaleway_container_namespace_info_module.md#parameters)
- [Attributes](scaleway_container_namespace_info_module.md#attributes)
- [Notes](scaleway_container_namespace_info_module.md#notes)
- [Examples](scaleway_container_namespace_info_module.md#examples)
- [Return Values](scaleway_container_namespace_info_module.md#return-values)

## [Synopsis](scaleway_container_namespace_info_module.md#id1)

- This module return information about a container namespace on Scaleway account.

## [Parameters](scaleway_container_namespace_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  **Default:** `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  **Default:** `"https://api.scaleway.com"` |
| **name**  string / required | Name of the container namespace. |
| **project_id**  string / required | Project identifier. |
| **query_parameters**  dictionary | List of parameters passed to the query string.  **Default:** `{}` |
| **region**  string / required | Scaleway region to use (for example `fr-par`).  **Choices:**   - `"fr-par"` - `"nl-ams"` - `"pl-waw"` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](scaleway_container_namespace_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](scaleway_container_namespace_info_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence [`SCW_TOKEN`](../../environment_variables.md#envvar-SCW_TOKEN), [`SCW_API_KEY`](../../environment_variables.md#envvar-SCW_API_KEY), [`SCW_OAUTH_TOKEN`](../../environment_variables.md#envvar-SCW_OAUTH_TOKEN) or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_container_namespace_info_module.md#id5)

```yaml+jinja
- name: Get a container namespace info
  community.general.scaleway_container_namespace_info:
    project_id: '{{ scw_project }}'
    region: fr-par
    name: my-awesome-container-namespace
  register: container_namespace_info_task
```

## [Return Values](scaleway_container_namespace_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **container_namespace**  dictionary | The container namespace information.  **Returned:** always  **Sample:** `{"description": "", "environment_variables": {"MY_VAR": "my_value"}, "error_message": null, "id": "531a1fd7-98d2-4a74-ad77-d398324304b8", "name": "my-awesome-container-namespace", "organization_id": "e04e3bdc-015c-4514-afde-9389e9be24b0", "project_id": "d44cea58-dcb7-4c95-bff1-1105acb60a98", "region": "fr-par", "registry_endpoint": "", "registry_namespace_id": "", "secret_environment_variables": [{"key": "MY_SECRET_VAR", "value": "$argon2id$v=19$m=65536,t=1,p=2$tb6UwSPWx/rH5Vyxt9Ujfw$5ZlvaIjWwNDPxD9Rdght3NarJz4IETKjpvAU3mMSmFg"}], "status": "pending"}` |

### Authors

- Guillaume MARTINEZ (@Lunik)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
