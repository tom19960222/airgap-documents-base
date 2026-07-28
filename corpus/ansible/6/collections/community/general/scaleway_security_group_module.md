---
collection: ansible
version: "6"
title: "community.general.scaleway_security_group module – Scaleway Security Group management module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/scaleway_security_group_module.html
fetched_at: 2026-07-27T17:13:00+00:00
---
# community.general.scaleway_security_group module – Scaleway Security Group management module

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
> To use it in a playbook, specify: `community.general.scaleway_security_group`.

- [Synopsis](scaleway_security_group_module.md#synopsis)
- [Parameters](scaleway_security_group_module.md#parameters)
- [Notes](scaleway_security_group_module.md#notes)
- [Examples](scaleway_security_group_module.md#examples)
- [Return Values](scaleway_security_group_module.md#return-values)

## [Synopsis](scaleway_security_group_module.md#id1)

- This module manages Security Group on Scaleway account <https://developer.scaleway.com>.

## [Parameters](scaleway_security_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  Default: `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL.  Default: `"https://api.scaleway.com"` |
| **description**  string | Description of the Security Group. |
| **inbound_default_policy**  string | Default policy for incoming traffic.  Choices:   - `"accept"` - `"drop"` |
| **name**  string / required | Name of the Security Group. |
| **organization**  string / required | Organization identifier. |
| **organization_default**  boolean | Create security group to be the default one.  Choices:   - `false` - `true` |
| **outbound_default_policy**  string | Default policy for outcoming traffic.  Choices:   - `"accept"` - `"drop"` |
| **query_parameters**  dictionary | List of parameters passed to the query string.  Default: `{}` |
| **region**  string / required | Scaleway region to use (for example `par1`).  Choices:   - `"ams1"` - `"EMEA-NL-EVS"` - `"par1"` - `"EMEA-FR-PAR1"` - `"par2"` - `"EMEA-FR-PAR2"` - `"waw1"` - `"EMEA-PL-WAW1"` |
| **state**  string | Indicate desired state of the Security Group.  Choices:   - `"absent"` - `"present"` ← (default) |
| **stateful**  boolean / required | Create a stateful security group which allows established connections in and out.  Choices:   - `false` - `true` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  Choices:   - `false` - `true` ← (default) |

## [Notes](scaleway_security_group_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence `SCW_TOKEN`, `SCW_API_KEY`, `SCW_OAUTH_TOKEN` or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_security_group_module.md#id4)

```yaml+jinja
- name: Create a Security Group
  community.general.scaleway_security_group:
    state: present
    region: par1
    name: security_group
    description: "my security group description"
    organization: "43a3b6c8-916f-477b-b7ec-ff1898f5fdd9"
    stateful: false
    inbound_default_policy: accept
    outbound_default_policy: accept
    organization_default: false
  register: security_group_creation_task
```

## [Return Values](scaleway_security_group_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | This is only present when `state=present`  Returned: when `state=present`  Sample: `{"scaleway_security_group": {"description": "my security group description", "enable_default_security": true, "id": "0168fb1f-cc46-4f69-b4be-c95d2a19bcae", "inbound_default_policy": "accept", "name": "security_group", "organization": "43a3b6c8-916f-477b-b7ec-ff1898f5fdd9", "organization_default": false, "outbound_default_policy": "accept", "servers": [], "stateful": false}}` |

### Authors

- Antoine Barbare (@abarbare)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
