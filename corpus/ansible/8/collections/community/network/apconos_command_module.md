---
collection: ansible
version: "8"
title: "community.network.apconos_command module – Run arbitrary commands on APCON devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/apconos_command_module.html
fetched_at: 2026-07-28T01:54:19+00:00
---
# community.network.apconos_command module – Run arbitrary commands on APCON devices

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
> To use it in a playbook, specify: `community.network.apconos_command`.

New in community.network 0.2.0

- [Synopsis](apconos_command_module.md#synopsis)
- [Parameters](apconos_command_module.md#parameters)
- [Notes](apconos_command_module.md#notes)
- [Examples](apconos_command_module.md#examples)

## [Synopsis](apconos_command_module.md#id1)

- Sends arbitrary commands to an apcon device and returns the results read from the device. The module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

Aliases: network.apconos.apconos_command

## [Parameters](apconos_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=string / required | List of commands to send to the remote device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retires as expired. |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  **Default:** `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  **Choices:**   - `"any"` - `"all"` ← (default) |
| **retries**  integer | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  **Default:** `10` |
| **wait_for**  list / elements=string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Notes](apconos_command_module.md#id3)

> **Note:**
>
> - Tested against apcon iis+ii

## [Examples](apconos_command_module.md#id4)

```yaml+jinja
- name: Basic Configuration
  community.network.apconos_command:
    commands:
    - show version
    - enable ssh
  register: result

- name: Get output from single command
  community.network.apconos_command:
    commands: ['show version']
  register: result
```

### Authors

- David Lee (@davidlee-ap)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
