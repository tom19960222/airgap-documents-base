---
collection: ansible
version: "6"
title: "community.general.scaleway_private_network module – Scaleway private network management"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/scaleway_private_network_module.html
fetched_at: 2026-07-27T17:13:00+00:00
---
# community.general.scaleway_private_network module – Scaleway private network management

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
> To use it in a playbook, specify: `community.general.scaleway_private_network`.

New in community.general 4.5.0

- [Synopsis](scaleway_private_network_module.md#synopsis)
- [Parameters](scaleway_private_network_module.md#parameters)
- [Notes](scaleway_private_network_module.md#notes)
- [Examples](scaleway_private_network_module.md#examples)
- [Return Values](scaleway_private_network_module.md#return-values)

## [Synopsis](scaleway_private_network_module.md#id1)

- This module manages private network on Scaleway account (<https://developer.scaleway.com>).

## [Parameters](scaleway_private_network_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  Default: `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  Default: `"https://api.scaleway.com"` |
| **name**  string | Name of the VPC. |
| **project**  string / required | Project identifier. |
| **query_parameters**  dictionary | List of parameters passed to the query string.  Default: `{}` |
| **region**  string / required | Scaleway region to use (for example `par1`).  Choices:   - `"ams1"` - `"EMEA-NL-EVS"` - `"par1"` - `"EMEA-FR-PAR1"` - `"par2"` - `"EMEA-FR-PAR2"` - `"waw1"` - `"EMEA-PL-WAW1"` |
| **state**  string | Indicate desired state of the VPC.  Choices:   - `"present"` ← (default) - `"absent"` |
| **tags**  list / elements=string | List of tags to apply to the instance.  Default: `[]` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  Choices:   - `false` - `true` ← (default) |

## [Notes](scaleway_private_network_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence `SCW_TOKEN`, `SCW_API_KEY`, `SCW_OAUTH_TOKEN` or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_private_network_module.md#id4)

```yaml+jinja
- name: Create an private network
  community.general.scaleway_vpc:
    project: '{{ scw_project }}'
    name: 'vpc_one'
    state: present
    region: par1
  register: vpc_creation_task

- name: Make sure private network with name 'foo' is deleted in region par1
  community.general.scaleway_vpc:
    name: 'foo'
    state: absent
    region: par1
```

## [Return Values](scaleway_private_network_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **scaleway_private_network**  dictionary | Information on the VPC.  Returned: success when `state=present`  Sample: `{"created_at": "2022-01-15T11:11:12.676445Z", "id": "12345678-f1e6-40ec-83e5-12345d67ed89", "name": "network", "organization_id": "a123b4cd-ef5g-678h-90i1-jk2345678l90", "project_id": "a123b4cd-ef5g-678h-90i1-jk2345678l90", "tags": ["tag1", "tag2", "tag3", "tag4", "tag5"], "updated_at": "2022-01-15T11:12:04.624837Z", "zone": "fr-par-2"}` |

### Authors

- Pascal MANGIN (@pastral)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
