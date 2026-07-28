---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_command module – Run arbitrary command on Cisco NXOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_command_module.html
fetched_at: 2026-07-28T01:04:37+00:00
---
# cisco.nxos.nxos_command module – Run arbitrary command on Cisco NXOS devices

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_command`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_command_module.md#synopsis)
- [Parameters](nxos_command_module.md#parameters)
- [Notes](nxos_command_module.md#notes)
- [Examples](nxos_command_module.md#examples)
- [Return Values](nxos_command_module.md#return-values)

## [Synopsis](nxos_command_module.md#id1)

- Sends an arbitrary command to an NXOS node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: command

## [Parameters](nxos_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=any / required | The commands to send to the remote NXOS device. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retires as expired.  The *commands* argument also accepts an alternative form that allows for complex values that specify the command to run and the output format to return. This can be done on a command by command basis. The complex argument supports the keywords `command` and `output` where `command` is the command to run and `output` is one of ‘text’ or ‘json’.  If a command sent to the device requires answering a prompt, it is possible to pass a dict containing command, answer and prompt. Common answers are ‘y’ or “\r” (carriage return, must be double quotes). See examples. |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditional, the interval indicates how to long to wait before trying the command again.  **Default:** `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the *wait_for* must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  **Choices:**   - `"any"` - `"all"` ← (default) |
| **retries**  integer | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditionals.  The commands are run once when *retries* is set to `0`.  **Default:** `9` |
| **wait_for**  aliases: waitfor  list / elements=string | Specifies what to evaluate from the output of the command and what conditionals to apply. This argument will cause the task to wait for a particular conditional to be true before moving forward. If the conditional is not true by the configured retries, the task fails. See examples. |

## [Notes](nxos_command_module.md#id3)

> **Note:**
>
> - Limited Support for Cisco MDS
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_command_module.md#id4)

```yaml+jinja
- name: run show version on remote devices
  cisco.nxos.nxos_command:
    commands: show version

- name: run show version and check to see if output contains Cisco
  cisco.nxos.nxos_command:
    commands: show version
    wait_for: result[0] contains Cisco

- name: run multiple commands on remote nodes
  cisco.nxos.nxos_command:
    commands:
    - show version
    - show interfaces

- name: run multiple commands and evaluate the output
  cisco.nxos.nxos_command:
    commands:
    - show version
    - show interfaces
    wait_for:
    - result[0] contains Cisco
    - result[1] contains loopback0

- name: run commands and specify the output format
  cisco.nxos.nxos_command:
    commands:
    - command: show version
      output: json

- name: run commands that require answering a prompt
  cisco.nxos.nxos_command:
    commands:
    - configure terminal
    - command: no feature npv
      prompt: Do you want to continue
      answer: y
```

## [Return Values](nxos_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  **Returned:** failed  **Sample:** `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  **Returned:** always apart from low level errors (such as action plugin)  **Sample:** `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  **Returned:** always apart from low level errors (such as action plugin)  **Sample:** `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
