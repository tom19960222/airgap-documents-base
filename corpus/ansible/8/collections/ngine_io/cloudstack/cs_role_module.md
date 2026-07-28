---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_role module – Manages user roles on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_role_module.html
fetched_at: 2026-07-28T02:46:17+00:00
---
# ngine_io.cloudstack.cs_role module – Manages user roles on Apache CloudStack based clouds.

> **Note:**
>
> This module is part of the [ngine_io.cloudstack collection](https://galaxy.ansible.com/ui/repo/published/ngine_io/cloudstack/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.cloudstack`.
> You need further requirements to be able to use this module,
> see [Requirements](cs_role_module.md#ansible-collections-ngine-io-cloudstack-cs-role-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_role`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_role_module.md#synopsis)
- [Requirements](cs_role_module.md#requirements)
- [Parameters](cs_role_module.md#parameters)
- [Notes](cs_role_module.md#notes)
- [Examples](cs_role_module.md#examples)
- [Return Values](cs_role_module.md#return-values)

## [Synopsis](cs_role_module.md#id1)

- Create, update, delete user roles.

## [Requirements](cs_role_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_role_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **description**  string | Description of the role. |
| **name**  string / required | Name of the role. |
| **role_type**  string | Type of the role.  Only considered for creation.  **Choices:**   - `"User"` ← (default) - `"DomainAdmin"` - `"ResourceAdmin"` - `"Admin"` |
| **state**  string | State of the role.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **uuid**  aliases: id  string | ID of the role.  If provided, *uuid* is used as key. |

## [Notes](cs_role_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_role_module.md#id5)

```yaml+jinja
- name: Ensure an user role is present
  ngine_io.cloudstack.cs_role:
    name: myrole_user

- name: Ensure a role having particular ID is named as myrole_user
  ngine_io.cloudstack.cs_role:
    name: myrole_user
    id: 04589590-ac63-4ffc-93f5-b698b8ac38b6

- name: Ensure a role is absent
  ngine_io.cloudstack.cs_role:
    name: myrole_user
    state: absent
```

## [Return Values](cs_role_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | Description of the role.  **Returned:** success  **Sample:** `"This is my role description"` |
| **id**  string | UUID of the role.  **Returned:** success  **Sample:** `"04589590-ac63-4ffc-93f5-b698b8ac38b6"` |
| **name**  string | Name of the role.  **Returned:** success  **Sample:** `"myrole"` |
| **role_type**  string | Type of the role.  **Returned:** success  **Sample:** `"User"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
