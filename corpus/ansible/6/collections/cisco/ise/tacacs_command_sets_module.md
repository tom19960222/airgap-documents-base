---
collection: ansible
version: "6"
title: "cisco.ise.tacacs_command_sets module – Resource module for TACACS Command Sets"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ise/tacacs_command_sets_module.html
fetched_at: 2026-07-27T16:59:54+00:00
---
# cisco.ise.tacacs_command_sets module – Resource module for TACACS Command Sets

> **Note:**
>
> This module is part of the [cisco.ise collection](https://galaxy.ansible.com/cisco/ise) (version 2.5.9).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ise`.
> You need further requirements to be able to use this module,
> see [Requirements](tacacs_command_sets_module.md#ansible-collections-cisco-ise-tacacs-command-sets-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ise.tacacs_command_sets`.

New in cisco.ise 1.0.0

- [Synopsis](tacacs_command_sets_module.md#synopsis)
- [Requirements](tacacs_command_sets_module.md#requirements)
- [Parameters](tacacs_command_sets_module.md#parameters)
- [Notes](tacacs_command_sets_module.md#notes)
- [Examples](tacacs_command_sets_module.md#examples)
- [Return Values](tacacs_command_sets_module.md#return-values)

## [Synopsis](tacacs_command_sets_module.md#id1)

- Manage operations create, update and delete of the resource TACACS Command Sets.
- This API creates TACACS command sets.
- This API deletes TACACS command sets.
- This API allows the client to update TACACS command sets.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](tacacs_command_sets_module.md#id2)

The below requirements are needed on the host that executes this module.

- ciscoisesdk >= 2.0.8
- python >= 3.5

## [Parameters](tacacs_command_sets_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **commands**  dictionary | TACACS Command Sets’s commands. |
| **commandList**  list / elements=dictionary | TACACS Command Sets’s commandList. |
| **arguments**  string | TACACS Command Sets’s arguments. |
| **command**  string | TACACS Command Sets’s command. |
| **grant**  string | Allowed values PERMIT, DENY, DENY_ALWAYS. |
| **description**  string | TACACS Command Sets’s description. |
| **id**  string | TACACS Command Sets’s id. |
| **ise_debug**  boolean | Flag for Identity Services Engine SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **ise_hostname**  string / required | The Identity Services Engine hostname. |
| **ise_password**  string / required | The Identity Services Engine password to authenticate. |
| **ise_username**  string / required | The Identity Services Engine username to authenticate. |
| **ise_uses_api_gateway**  boolean  added in cisco.ise 1.1.0 | Flag that informs the SDK whether to use the Identity Services Engine’s API Gateway to send requests.  If it is true, it uses the ISE’s API Gateway and sends requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}.  If it is false, it sends the requests to [https:/](https://docs.ansible.com/)/{{ise_hostname}}:{{port}}, where the port value depends on the Service used (ERS, Mnt, UI, PxGrid).  Choices:   - `false` - `true` ← (default) |
| **ise_uses_csrf_token**  boolean  added in cisco.ise 3.0.0 | Flag that informs the SDK whether we send the CSRF token to ISE’s ERS APIs.  If it is True, the SDK assumes that your ISE CSRF Check is enabled.  If it is True, it assumes you need the SDK to manage the CSRF token automatically for you.  Choices:   - `false` ← (default) - `true` |
| **ise_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **ise_version**  string | Informs the SDK which version of Identity Services Engine to use.  Default: `"3.1_Patch_1"` |
| **ise_wait_on_rate_limit**  boolean | Flag for Identity Services Engine SDK to enable automatic rate-limit handling.  Choices:   - `false` - `true` ← (default) |
| **name**  string | TACACS Command Sets’s name. |
| **permitUnmatched**  boolean | PermitUnmatched flag.  Choices:   - `false` - `true` |

## [Notes](tacacs_command_sets_module.md#id4)

> **Note:**
>
> - SDK Method used are tacacs_command_sets.TacacsCommandSets.create_tacacs_command_sets, tacacs_command_sets.TacacsCommandSets.delete_tacacs_command_sets_by_id, tacacs_command_sets.TacacsCommandSets.update_tacacs_command_sets_by_id,
> - Paths used are post /ers/config/tacacscommandsets, delete /ers/config/tacacscommandsets/{id}, put /ers/config/tacacscommandsets/{id},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco ISE SDK
> - The parameters starting with ise_ are used by the Cisco ISE Python SDK to establish the connection

## [Examples](tacacs_command_sets_module.md#id5)

```yaml+jinja
- name: Update by id
  cisco.ise.tacacs_command_sets:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    commands:
      commandList:
      - arguments: string
        command: string
        grant: string
    description: string
    id: string
    name: string
    permitUnmatched: true

- name: Delete by id
  cisco.ise.tacacs_command_sets:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: absent
    id: string

- name: Create
  cisco.ise.tacacs_command_sets:
    ise_hostname: "{{ise_hostname}}"
    ise_username: "{{ise_username}}"
    ise_password: "{{ise_password}}"
    ise_verify: "{{ise_verify}}"
    state: present
    commands:
      commandList:
      - arguments: string
        command: string
        grant: string
    description: string
    name: string
    permitUnmatched: true
```

## [Return Values](tacacs_command_sets_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ise_response**  dictionary | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"commands": {"commandList": [{"arguments": "string", "command": "string", "grant": "string"}]}, "description": "string", "id": "string", "link": {"href": "string", "rel": "string", "type": "string"}, "name": "string", "permitUnmatched": true}` |
| **ise_update_response**  dictionary  added in cisco.ise 1.1.0 | A dictionary or list with the response returned by the Cisco ISE Python SDK  Returned: always  Sample: `{"UpdatedFieldsList": {"field": "string", "newValue": "string", "oldValue": "string", "updatedField": [{"field": "string", "newValue": "string", "oldValue": "string"}]}}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/CiscoISE/ansible-ise/issues)
[Repository (Sources)](https://github.com/CiscoISE/ansible-ise)
