---
collection: ansible
version: "8"
title: "community.network.edgeos_command module – Run one or more commands on EdgeOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/edgeos_command_module.html
fetched_at: 2026-07-28T01:56:28+00:00
---
# community.network.edgeos_command module – Run one or more commands on EdgeOS devices

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.edgeos_command`.

- [Synopsis](edgeos_command_module.md#synopsis)
- [Parameters](edgeos_command_module.md#parameters)
- [Notes](edgeos_command_module.md#notes)
- [Examples](edgeos_command_module.md#examples)
- [Return Values](edgeos_command_module.md#return-values)

## [Synopsis](edgeos_command_module.md#id1)

- This command module allows running one or more commands on a remote device running EdgeOS, such as the Ubiquiti EdgeRouter.
- This module does not support running commands in configuration mode.
- Certain `show` commands in EdgeOS produce many lines of output and use a custom pager that can cause this module to hang. If the value of the environment variable `ANSIBLE_EDGEOS_TERMINAL_LENGTH` is not set, the default number of 10000 is used.
- This is a network module and requires `connection: network_cli` in order to work properly.
- For more information please see the [Network Guide](getting_started/index.md).

Aliases: network.edgeos.edgeos_command

## [Parameters](edgeos_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  string / required | The commands or ordered set of commands that should be run against the remote device. The output of the command is returned to the playbook. If the `wait_for` argument is provided, the module is not returned until the condition is met or the number of retries is exceeded. |
| **interval**  string | The number of seconds to wait between `retries` of the command.  **Default:** `1` |
| **match**  string | Used in conjunction with `wait_for` to create match policy. If set to `all`, then all conditions in `wait_for` must be met. If set to `any`, then only one condition must match.  **Choices:**   - `"any"` - `"all"` ← (default) |
| **retries**  string | Number of times a command should be tried before it is considered failed. The command is run on the target device and evaluated against the `wait_for` conditionals.  **Default:** `10` |
| **wait_for**  string | Causes the task to wait for a specific condition to be met before moving forward. If the condition is not met before the specified number of retries is exceeded, the task will fail. |

## [Notes](edgeos_command_module.md#id3)

> **Note:**
>
> - Tested against EdgeOS 1.9.7
> - Running `show system boot-messages all` will cause the module to hang since EdgeOS is using a custom pager setting to display the output of that command.

## [Examples](edgeos_command_module.md#id4)

```yaml+jinja
tasks:
  - name: Reboot the device
    community.network.edgeos_command:
      commands: reboot now

  - name: Show the configuration for eth0 and eth1
    community.network.edgeos_command:
      commands: show interfaces ethernet {{ item }}
    loop:
      - eth0
      - eth1
```

## [Return Values](edgeos_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **stdout**  list / elements=string | The set of responses from the commands  **Returned:** always apart from low level errors (such as action plugin)  **Sample:** `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  **Returned:** always  **Sample:** `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Chad Norgan (@beardymcbeards)
- Sam Doran (@samdoran)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
