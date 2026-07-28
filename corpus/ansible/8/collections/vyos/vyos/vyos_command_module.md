---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_command module – Run one or more commands on VyOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_command_module.html
fetched_at: 2026-07-28T02:59:10+00:00
---
# vyos.vyos.vyos_command module – Run one or more commands on VyOS devices

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_command`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_command_module.md#synopsis)
- [Parameters](vyos_command_module.md#parameters)
- [Notes](vyos_command_module.md#notes)
- [Examples](vyos_command_module.md#examples)
- [Return Values](vyos_command_module.md#return-values)

## [Synopsis](vyos_command_module.md#id1)

- The command module allows running one or more commands on remote devices running VyOS. This module can also be introspected to validate key parameters before returning successfully. If the conditional statements are not met in the wait period, the task fails.
- Certain `show` commands in VyOS produce many lines of output and use a custom pager that can cause this module to hang. If the value of the environment variable `ANSIBLE_VYOS_TERMINAL_LENGTH` is not set, the default number of 10000 is used.

Aliases: command

## [Parameters](vyos_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=any / required | The ordered set of commands to execute on the remote device running VyOS. The output from the command execution is returned to the playbook. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has been exceeded.  If a command sent to the device requires answering a prompt, it is possible to pass a dict containing command, answer and prompt. Common answers are ‘y’ or “\r” (carriage return, must be double quotes). Refer below examples. |
| **interval**  integer | Configures the interval in seconds to wait between *retries* of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  **Default:** `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  **Choices:**   - `"any"` - `"all"` ← (default) |
| **retries**  integer | Specifies the number of retries a command should be tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditionals.  The commands are run once when *retries* is set to `0`.  **Default:** `9` |
| **wait_for**  aliases: waitfor  list / elements=string | Specifies what to evaluate from the output of the command and what conditionals to apply. This argument will cause the task to wait for a particular conditional to be true before moving forward. If the conditional is not true by the configured *retries*, the task fails. See examples. |

## [Notes](vyos_command_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - Running `show system boot-messages all` will cause the module to hang since VyOS is using a custom pager setting to display the output of that command.
> - If a command sent to the device requires answering a prompt, it is possible to pass a dict containing *command*, *answer* and *prompt*. See examples.
> - This module works with connection `ansible.netcommon.network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_command_module.md#id4)

```yaml+jinja
- name: show configuration on ethernet devices eth0 and eth1
  vyos.vyos.vyos_command:
    commands:
    - show interfaces ethernet {{ item }}
  with_items:
  - eth0
  - eth1

- name: run multiple commands and check if version output contains specific version
    string
  vyos.vyos.vyos_command:
    commands:
    - show version
    - show hardware cpu
    wait_for:
    - result[0] contains 'VyOS 1.1.7'

- name: run command that requires answering a prompt
  vyos.vyos.vyos_command:
    commands:
    - command: rollback 1
      prompt: Proceed with reboot? [confirm][y]
      answer: y
```

## [Return Values](vyos_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  **Returned:** failed  **Sample:** `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  **Returned:** always apart from low level errors (such as action plugin)  **Sample:** `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  **Returned:** always  **Sample:** `[["...", "..."], ["..."], ["..."]]` |
| **warnings**  list / elements=string | The list of warnings (if any) generated by module based on arguments  **Returned:** always  **Sample:** `["...", "..."]` |

### Authors

- Nathaniel Case (@Qalthos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
