---
collection: ansible
version: "6"
title: "community.network.icx_command module – Run arbitrary commands on remote Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/icx_command_module.html
fetched_at: 2026-07-27T17:18:41+00:00
---
# community.network.icx_command module – Run arbitrary commands on remote Ruckus ICX 7000 series switches

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.icx_command`.

- [Synopsis](icx_command_module.md#synopsis)
- [Parameters](icx_command_module.md#parameters)
- [Notes](icx_command_module.md#notes)
- [Examples](icx_command_module.md#examples)
- [Return Values](icx_command_module.md#return-values)

## [Synopsis](icx_command_module.md#id1)

- Sends arbitrary commands to an ICX node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

## [Parameters](icx_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=string / required | List of commands to send to the remote ICX device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired. If a command sent to the device requires answering a prompt, checkall and newline if multiple prompts, it is possible to pass a dict containing *command*, *answer*, *prompt*, *check_all* and *newline*.Common answers are ‘y’ or “\r” (carriage return, must be double quotes). See examples. |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  Default: `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  Choices:   - `"any"` - `"all"` ← (default) |
| **retries**  integer | Specifies the number of times a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  Default: `10` |
| **wait_for**  aliases: waitfor  list / elements=string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Notes](icx_command_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1

## [Examples](icx_command_module.md#id4)

```yaml+jinja
tasks:
  - name: Run show version on remote devices
    community.network.icx_command:
      commands: show version

  - name: Run show version and check to see if output contains ICX
    community.network.icx_command:
      commands: show version
      wait_for: result[0] contains ICX

  - name: Run multiple commands on remote nodes
    community.network.icx_command:
      commands:
        - show version
        - show interfaces

  - name: Run multiple commands and evaluate the output
    community.network.icx_command:
      commands:
        - show version
        - show interfaces
      wait_for:
        - result[0] contains ICX
        - result[1] contains GigabitEthernet1/1/1
  - name: Run commands that require answering a prompt
    community.network.icx_command:
      commands:
        - command: 'service password-encryption sha1'
          prompt: 'Warning: Moving to higher password-encryption type,.*'
          answer: 'y'
  - name: Run commands that require answering multiple prompt
    community.network.icx_command:
      commands:
        - command: 'username qqq password qqq'
          prompt:
            - 'User already exists. Do you want to modify:.*'
            - 'To modify or remove user, enter current password:'
          answer:
            - 'y'
            - 'qqq\
'
          check_all: True
          newline: False
```

## [Return Values](icx_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  Returned: failed  Sample: `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  Returned: always apart from low level errors  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  Returned: always apart from low level errors  Sample: `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
