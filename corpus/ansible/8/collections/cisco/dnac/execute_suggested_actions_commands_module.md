---
collection: ansible
version: "8"
title: "cisco.dnac.execute_suggested_actions_commands module – Resource module for Execute Suggested Actions Commands"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/execute_suggested_actions_commands_module.html
fetched_at: 2026-07-28T01:22:42+00:00
---
# cisco.dnac.execute_suggested_actions_commands module – Resource module for Execute Suggested Actions Commands

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
> see [Requirements](execute_suggested_actions_commands_module.md#ansible-collections-cisco-dnac-execute-suggested-actions-commands-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.execute_suggested_actions_commands`.

New in cisco.dnac 6.7.0

- [Synopsis](execute_suggested_actions_commands_module.md#synopsis)
- [Requirements](execute_suggested_actions_commands_module.md#requirements)
- [Parameters](execute_suggested_actions_commands_module.md#parameters)
- [Notes](execute_suggested_actions_commands_module.md#notes)
- [See Also](execute_suggested_actions_commands_module.md#see-also)
- [Examples](execute_suggested_actions_commands_module.md#examples)
- [Return Values](execute_suggested_actions_commands_module.md#return-values)

## [Synopsis](execute_suggested_actions_commands_module.md#id1)

- Manage operation create of the resource Execute Suggested Actions Commands.
- This API triggers the execution of the suggested actions for an issue, given the Issue Id. It will return an execution Id. At the completion of the execution, the output of the commands associated with the suggested actions will be provided.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](execute_suggested_actions_commands_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](execute_suggested_actions_commands_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **entity_type**  string | Commands provided as part of the suggested actions for an issue can be executed based on issue id. The value here must be issue_id. |
| **entity_value**  string | Contains the actual value for the entity type that has been defined. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](execute_suggested_actions_commands_module.md#id4)

> **Note:**
>
> - SDK Method used are issues.Issues.execute_suggested_actions_commands,
> - Paths used are post /dna/intent/api/v1/execute-suggested-actions-commands,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](execute_suggested_actions_commands_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Issues ExecuteSuggestedActionsCommands](https://developer.cisco.com/docs/dna-center/#!execute-suggested-actions-commands)
> :   Complete reference of the ExecuteSuggestedActionsCommands API.

## [Examples](execute_suggested_actions_commands_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.execute_suggested_actions_commands:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    entity_type: string
    entity_value: string
```

## [Return Values](execute_suggested_actions_commands_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  list / elements=string | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `["[\n  {\n    \"actionInfo\": \"string\"", "\n    \"stepsCount\": 0", "\n    \"entityId\": \"string\"", "\n    \"hostname\": \"string\"", "\n    \"stepsDescription\": \"string\"", "\n    \"command\": \"string\"", "\n    \"commandOutput\": {}\n  }\n]\n"]` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
