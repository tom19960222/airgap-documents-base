---
collection: ansible
version: "6"
title: "cisco.dnac.command_runner_run_command module – Resource module for Command Runner Run Command"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/dnac/command_runner_run_command_module.html
fetched_at: 2026-07-27T16:51:10+00:00
---
# cisco.dnac.command_runner_run_command module – Resource module for Command Runner Run Command

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/cisco/dnac) (version 6.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](command_runner_run_command_module.md#ansible-collections-cisco-dnac-command-runner-run-command-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.command_runner_run_command`.

New in cisco.dnac 3.1.0

- [Synopsis](command_runner_run_command_module.md#synopsis)
- [Requirements](command_runner_run_command_module.md#requirements)
- [Parameters](command_runner_run_command_module.md#parameters)
- [Notes](command_runner_run_command_module.md#notes)
- [See Also](command_runner_run_command_module.md#see-also)
- [Examples](command_runner_run_command_module.md#examples)
- [Return Values](command_runner_run_command_module.md#return-values)

## [Synopsis](command_runner_run_command_module.md#id1)

- Manage operation create of the resource Command Runner Run Command.
- Submit request for read-only CLIs.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](command_runner_run_command_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](command_runner_run_command_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=string | Command Runner Run Command’s commands. |
| **description**  string | Command Runner Run Command’s description. |
| **deviceUuids**  list / elements=string | Command Runner Run Command’s deviceUuids. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  Choices:   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  Default: `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  Default: `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  Choices:   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  Default: `"2.3.3.0"` |
| **name**  string | Command Runner Run Command’s name. |
| **timeout**  integer | Command Runner Run Command’s timeout. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  Choices:   - `false` - `true` ← (default) |

## [Notes](command_runner_run_command_module.md#id4)

> **Note:**
>
> - SDK Method used are command_runner.CommandRunner.run_read_only_commands_on_devices,
> - Paths used are post /dna/intent/api/v1/network-device-poller/cli/read-request,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](command_runner_run_command_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Command Runner RunReadOnlyCommandsOnDevicesToGetTheirRealTimeConfiguration](https://developer.cisco.com/docs/dna-center/#!run-read-only-commands-on-devices-to-get-their-real-time-configuration)
> :   Complete reference of the RunReadOnlyCommandsOnDevicesToGetTheirRealTimeConfiguration API.

## [Examples](command_runner_run_command_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.command_runner_run_command:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    commands:
    - string
    description: string
    deviceUuids:
    - string
    name: string
    timeout: 0
```

## [Return Values](command_runner_run_command_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  Returned: always  Sample: `{"response": {"taskId": "string", "url": "string"}, "version": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

[Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
[Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
