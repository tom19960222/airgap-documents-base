---
collection: ansible
version: "8"
title: "cisco.dnac.user module – Resource module for User"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/user_module.html
fetched_at: 2026-07-28T01:25:39+00:00
---
# cisco.dnac.user module – Resource module for User

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/ui/repo/published/cisco/dnac/) (version 6.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](user_module.md#ansible-collections-cisco-dnac-user-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.user`.

New in cisco.dnac 6.7.0

- [Synopsis](user_module.md#synopsis)
- [Requirements](user_module.md#requirements)
- [Parameters](user_module.md#parameters)
- [Notes](user_module.md#notes)
- [See Also](user_module.md#see-also)
- [Examples](user_module.md#examples)
- [Return Values](user_module.md#return-values)

## [Synopsis](user_module.md#id1)

- Manage operations create and update of the resource User.
- Add a new user for Cisco DNA Center system.
- Update a user for Cisco DNA Center system.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](user_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **email**  string | Email. |
| **firstName**  string | First Name. |
| **lastName**  string | Last Name. |
| **password**  string | Password. |
| **roleList**  list / elements=string | Role id list. |
| **userId**  string | User Id. |
| **username**  string | Username. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](user_module.md#id4)

> **Note:**
>
> - SDK Method used are user_and_roles.UserandRoles.add_user_ap_i, user_and_roles.UserandRoles.update_user_ap_i,
> - Paths used are post /dna/system/api/v1/user, put /dna/system/api/v1/user,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](user_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for User and Roles AddUserAPI](https://developer.cisco.com/docs/dna-center/#!add-user-api)
> :   Complete reference of the AddUserAPI API.
>
> [Cisco DNA Center documentation for User and Roles UpdateUserAPI](https://developer.cisco.com/docs/dna-center/#!update-user-api)
> :   Complete reference of the UpdateUserAPI API.

## [Examples](user_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.user:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    email: string
    firstName: string
    lastName: string
    password: string
    roleList:
    - string
    username: string

- name: Update all
  cisco.dnac.user:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    email: string
    firstName: string
    lastName: string
    roleList:
    - string
    userId: string
    username: string
```

## [Return Values](user_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"message": "string", "userId": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
