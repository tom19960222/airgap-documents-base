---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_command module – Runs commands on devices running Enterprise SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_command_module.html
fetched_at: 2026-07-28T02:03:33+00:00
---
# dellemc.enterprise_sonic.sonic_command module – Runs commands on devices running Enterprise SONiC

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_command`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_command_module.md#synopsis)
- [Parameters](sonic_command_module.md#parameters)
- [Notes](sonic_command_module.md#notes)
- [Examples](sonic_command_module.md#examples)
- [Return Values](sonic_command_module.md#return-values)

## [Synopsis](sonic_command_module.md#id1)

- Runs commands on remote devices running Enterprise SONiC Distribution by Dell Technologies. Sends arbitrary commands to an Enterprise SONiC node and returns the results that are read from the device. This module includes an argument that causes the module to wait for a specific condition before returning or time out if the condition is not met.
- This module does not support running commands in configuration mode. To configure SONiC devices, use [dellemc.enterprise_sonic.sonic_config](sonic_config_module.md#ansible-collections-dellemc-enterprise-sonic-sonic-config-module).

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=string / required | List of commands to send to the remote Enterprise SONiC devices over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired. If a command sent to the device requires answering a prompt, it is possible to pass a dict containing *command*, *answer* and *prompt*. Common answers are ‘yes’ or “\r” (carriage return, must be double quotes). See examples. |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  **Default:** `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  **Choices:**   - `"all"` ← (default) - `"any"` |
| **retries**  integer | Specifies the number of retries a command should be run before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  **Default:** `10` |
| **wait_for**  list / elements=string | List of conditions to evaluate against the output of the command. The task waits for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Notes](sonic_command_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_command_module.md#id4)

```yaml+jinja
- name: Runs show version on remote devices
  dellemc.enterprise_sonic.sonic_command:
    commands: show version

- name: Runs show version and checks to see if output contains 'Dell'
  dellemc.enterprise_sonic.sonic_command:
    commands: show version
    wait_for: result[0] contains Dell

- name: Runs multiple commands on remote nodes
  dellemc.enterprise_sonic.sonic_command:
    commands:
      - show version
      - show interface

- name: Runs multiple commands and evaluate the output
  dellemc.enterprise_sonic.sonic_command:
    commands:
      - 'show version'
      - 'show system'
    wait_for:
      - result[0] contains Dell
      - result[1] contains Hostname

- name: Runs commands that require answering a prompt
  dellemc.enterprise_sonic.sonic_command:
    commands:
      - command: 'reload'
        prompt: '[confirm yes/no]: ?$'
        answer: 'no'
```

## [Return Values](sonic_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed.  **Returned:** failed  **Sample:** `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands.  **Returned:** always apart from low level errors (such as action plugin)  **Sample:** `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list.  **Returned:** always apart from low level errors (such as action plugin)  **Sample:** `[["...", "..."], ["..."], ["..."]]` |
| **warnings**  list / elements=string | The list of warnings (if any) generated by module based on arguments.  **Returned:** always  **Sample:** `["...", "..."]` |

### Authors

- Dhivya P (@dhivayp)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
