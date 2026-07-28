---
collection: ansible
version: "6"
title: "community.general.scaleway_security_group_info module – Gather information about the Scaleway security groups available"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/scaleway_security_group_info_module.html
fetched_at: 2026-07-27T17:13:01+00:00
---
# community.general.scaleway_security_group_info module – Gather information about the Scaleway security groups available

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
> To use it in a playbook, specify: `community.general.scaleway_security_group_info`.

- [Synopsis](scaleway_security_group_info_module.md#synopsis)
- [Parameters](scaleway_security_group_info_module.md#parameters)
- [Notes](scaleway_security_group_info_module.md#notes)
- [Examples](scaleway_security_group_info_module.md#examples)
- [Return Values](scaleway_security_group_info_module.md#return-values)

## [Synopsis](scaleway_security_group_info_module.md#id1)

- Gather information about the Scaleway security groups available.

## [Parameters](scaleway_security_group_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  Default: `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  Default: `"https://api.scaleway.com"` |
| **query_parameters**  dictionary | List of parameters passed to the query string.  Default: `{}` |
| **region**  string / required | Scaleway region to use (for example `par1`).  Choices:   - `"ams1"` - `"EMEA-NL-EVS"` - `"par1"` - `"EMEA-FR-PAR1"` - `"par2"` - `"EMEA-FR-PAR2"` - `"waw1"` - `"EMEA-PL-WAW1"` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  Choices:   - `false` - `true` ← (default) |

## [Notes](scaleway_security_group_info_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence `SCW_TOKEN`, `SCW_API_KEY`, `SCW_OAUTH_TOKEN` or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_security_group_info_module.md#id4)

```yaml+jinja
- name: Gather Scaleway security groups information
  community.general.scaleway_security_group_info:
    region: par1
  register: result

- ansible.builtin.debug:
    msg: "{{ result.scaleway_security_group_info }}"
```

## [Return Values](scaleway_security_group_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **scaleway_security_group_info**  list / elements=dictionary | Response from Scaleway API.  For more details please refer to: <https://developers.scaleway.com/en/products/instance/api/>.  Returned: success  Sample: `{"scaleway_security_group_info": [{"description": "test-ams", "enable_default_security": true, "id": "7fcde327-8bed-43a6-95c4-6dfbc56d8b51", "name": "test-ams", "organization": "3f709602-5e6c-4619-b80c-e841c89734af", "organization_default": false, "servers": [{"id": "12f19bc7-108c-4517-954c-e6b3d0311363", "name": "scw-e0d158"}]}]}` |

### Authors

- Yanis Guenane (@Spredzy)
- Remy Leone (@remyleone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
