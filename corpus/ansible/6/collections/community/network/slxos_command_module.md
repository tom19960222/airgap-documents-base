---
collection: ansible
version: "6"
title: "community.network.slxos_command module – Run commands on remote devices running Extreme Networks SLX-OS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/slxos_command_module.html
fetched_at: 2026-07-27T17:19:41+00:00
---
# community.network.slxos_command module – Run commands on remote devices running Extreme Networks SLX-OS

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
> To use it in a playbook, specify: `community.network.slxos_command`.

- [Synopsis](slxos_command_module.md#synopsis)
- [Parameters](slxos_command_module.md#parameters)
- [Notes](slxos_command_module.md#notes)
- [Examples](slxos_command_module.md#examples)
- [Return Values](slxos_command_module.md#return-values)

## [Synopsis](slxos_command_module.md#id1)

- Sends arbitrary commands to an SLX node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
- This module does not support running commands in configuration mode. Please use [community.network.slxos_config](slxos_config_module.md#ansible-collections-community-network-slxos-config-module) to configure SLX-OS devices.

## [Parameters](slxos_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  string / required | List of commands to send to the remote SLX-OS device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired. |
| **interval**  string | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  Default: `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  Choices:   - `"any"` - `"all"` ← (default) |
| **retries**  string | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  Default: `10` |
| **wait_for**  string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Notes](slxos_command_module.md#id3)

> **Note:**
>
> - Tested against SLX-OS 17s.1.02
> - If a command sent to the device requires answering a prompt, it is possible to pass a dict containing *command*, *answer* and *prompt*. See examples.

## [Examples](slxos_command_module.md#id4)

```yaml+jinja
tasks:
  - name: Run show version on remote devices
    community.network.slxos_command:
      commands: show version

  - name: Run show version and check to see if output contains SLX
    community.network.slxos_command:
      commands: show version
      wait_for: result[0] contains SLX

  - name: Run multiple commands on remote nodes
    community.network.slxos_command:
      commands:
        - show version
        - show interfaces

  - name: Run multiple commands and evaluate the output
    community.network.slxos_command:
      commands:
        - show version
        - show interface status
      wait_for:
        - result[0] contains SLX
        - result[1] contains Eth
  - name: Run command that requires answering a prompt
    community.network.slxos_command:
      commands:
        - command: 'clear sessions'
          prompt: 'This operation will logout all the user sessions. Do you want to continue (yes/no)?:'
          answer: y
```

## [Return Values](slxos_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  Returned: failed  Sample: `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  Returned: always apart from low level errors (such as action plugin)  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  Returned: always apart from low level errors (such as action plugin)  Sample: `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Lindsay Hill (@LindsayHill)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
