---
collection: ansible
version: "8"
title: "ngine_io.cloudstack.cs_role_permission module – Manages role permissions on Apache CloudStack based clouds."
source_url: https://docs.ansible.com/projects/ansible/8/collections/ngine_io/cloudstack/cs_role_permission_module.html
fetched_at: 2026-07-28T02:46:18+00:00
---
# ngine_io.cloudstack.cs_role_permission module – Manages role permissions on Apache CloudStack based clouds.

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
> see [Requirements](cs_role_permission_module.md#ansible-collections-ngine-io-cloudstack-cs-role-permission-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.cloudstack.cs_role_permission`.

New in ngine_io.cloudstack 0.1.0

- [Synopsis](cs_role_permission_module.md#synopsis)
- [Requirements](cs_role_permission_module.md#requirements)
- [Parameters](cs_role_permission_module.md#parameters)
- [Notes](cs_role_permission_module.md#notes)
- [Examples](cs_role_permission_module.md#examples)
- [Return Values](cs_role_permission_module.md#return-values)

## [Synopsis](cs_role_permission_module.md#id1)

- Create, update and remove CloudStack role permissions.
- Managing role permissions only supported in CloudStack >= 4.9.

## [Requirements](cs_role_permission_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6
- cs >= 0.9.0

## [Parameters](cs_role_permission_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_http_method**  string | HTTP method used to query the API endpoint.  If not given, the `CLOUDSTACK_METHOD` env variable is considered.  **Choices:**   - `"get"` ← (default) - `"post"` |
| **api_key**  string / required | API key of the CloudStack API.  If not given, the `CLOUDSTACK_KEY` env variable is considered. |
| **api_secret**  string / required | Secret key of the CloudStack API.  If not set, the `CLOUDSTACK_SECRET` env variable is considered. |
| **api_timeout**  integer | HTTP timeout in seconds.  If not given, the `CLOUDSTACK_TIMEOUT` env variable is considered.  **Default:** `10` |
| **api_url**  string / required | URL of the CloudStack API e.g. <https://cloud.example.com/client/api>.  If not given, the `CLOUDSTACK_ENDPOINT` env variable is considered. |
| **api_verify_ssl_cert**  string | Verify CA authority cert file.  If not given, the `CLOUDSTACK_VERIFY` env variable is considered. |
| **description**  string | The description of the role permission. |
| **name**  string / required | The API name of the permission. |
| **parent**  string | The parent role permission uuid. use 0 to move this rule at the top of the list. |
| **permission**  string | The rule permission, allow or deny. Defaulted to deny.  **Choices:**   - `"allow"` - `"deny"` ← (default) |
| **role**  string / required | Name or ID of the role. |
| **state**  string | State of the role permission.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](cs_role_permission_module.md#id4)

> **Note:**
>
> - A detailed guide about cloudstack modules can be found in the [CloudStack Cloud Guide](../scenario_guides/guide_cloudstack.md).
> - This module supports check mode.

## [Examples](cs_role_permission_module.md#id5)

```yaml+jinja
- name: Create a role permission
  ngine_io.cloudstack.cs_role_permission:
    role: My_Custom_role
    name: createVPC
    permission: allow
    description: My comments

- name: Remove a role permission
  ngine_io.cloudstack.cs_role_permission:
    state: absent
    role: My_Custom_role
    name: createVPC

- name: Update a system role permission
  ngine_io.cloudstack.cs_role_permission:
    role: Domain Admin
    name: createVPC
    permission: deny

- name: Update rules order. Move the rule at the top of list
  ngine_io.cloudstack.cs_role_permission:
    role: Domain Admin
    name: createVPC
    parent: 0
```

## [Return Values](cs_role_permission_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **description**  string | The description of the role permission  **Returned:** success  **Sample:** `"Deny createVPC for users"` |
| **id**  string | The ID of the role permission.  **Returned:** success  **Sample:** `"a6f7a5fc-43f8-11e5-a151-feff819cdc9f"` |
| **name**  string | The API name of the permission.  **Returned:** success  **Sample:** `"createVPC"` |
| **permission**  string | The permission type of the api name.  **Returned:** success  **Sample:** `"allow"` |
| **role_id**  string | The ID of the role to which the role permission belongs.  **Returned:** success  **Sample:** `"c6f7a5fc-43f8-11e5-a151-feff819cdc7f"` |

### Authors

- David Passante (@dpassante)

### Collection links

- [Issue Tracker](https://github.com/ngine-io/ansible-collection-cloudstack/issues)
- [Repository (Sources)](https://github.com/ngine-io/ansible-collection-cloudstack)
