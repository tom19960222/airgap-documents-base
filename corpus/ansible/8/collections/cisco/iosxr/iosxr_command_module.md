---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_command module – Module to run commands on remote devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_command_module.html
fetched_at: 2026-07-28T01:26:39+00:00
---
# cisco.iosxr.iosxr_command module – Module to run commands on remote devices.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_command`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_command_module.md#synopsis)
- [Parameters](iosxr_command_module.md#parameters)
- [Notes](iosxr_command_module.md#notes)
- [Examples](iosxr_command_module.md#examples)
- [Return Values](iosxr_command_module.md#return-values)

## [Synopsis](iosxr_command_module.md#id1)

- Sends arbitrary commands to an IOS XR node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
- This module does not support running commands in configuration mode. Please use [cisco.iosxr.iosxr_config](iosxr_config_module.md#ansible-collections-cisco-iosxr-iosxr-config-module) to configure iosxr devices.

Aliases: command

## [Parameters](iosxr_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=any / required | List of commands to send to the remote iosxr device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired.  If a command sent to the device requires answering a prompt, it is possible to pass a dict containing command, answer and prompt. Common answers are ‘y’ or “\r” (carriage return, must be double quotes). See examples |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  **Default:** `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  **Choices:**   - `"any"` - `"all"` ← (default) |
| **retries**  integer | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  **Default:** `10` |
| **wait_for**  aliases: waitfor  list / elements=string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Notes](iosxr_command_module.md#id3)

> **Note:**
>
> - Make sure the user has been authorized to execute commands terminal length 0, terminal width 512 and terminal exec prompt no-timestamp.
> - This module works with `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).
> - This module does not support `netconf` connection.
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](iosxr_command_module.md#id4)

```yaml+jinja
- name: run show version on remote devices
  cisco.iosxr.iosxr_command:
    commands: show version

- name: run show version and check to see if output contains iosxr
  cisco.iosxr.iosxr_command:
    commands: show version
    wait_for: result[0] contains IOS-XR

- name: run multiple commands on remote nodes
  cisco.iosxr.iosxr_command:
    commands:
    - show version
    - show interfaces
    - {command: example command that prompts, prompt: expected prompt, answer: yes}

- name: run multiple commands and evaluate the output
  cisco.iosxr.iosxr_command:
    commands:
    - show version
    - show interfaces
    wait_for:
    - result[0] contains IOS-XR
    - result[1] contains Loopback0

- name: multiple prompt, multiple answer (mandatory check for all prompts)
  cisco.iosxr.iosxr_command:
    commands:
        - command: key config-key password-encryption
          prompt:
            - "Enter old key :"
            - "Enter new key :"
            - "Enter confirm key :"
          answer:
            - "test1234"
            - "test12345"
            - "test12345"
          check_all: true
```

## [Return Values](iosxr_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  **Returned:** failed  **Sample:** `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  **Returned:** always apart from low level errors (such as action plugin)  **Sample:** `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  **Returned:** always apart from low level errors (such as action plugin)  **Sample:** `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
