---
collection: ansible
version: "6"
title: "community.network.exos_command module – Run commands on remote devices running Extreme EXOS"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/exos_command_module.html
fetched_at: 2026-07-27T17:18:31+00:00
---
# community.network.exos_command module – Run commands on remote devices running Extreme EXOS

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
> To use it in a playbook, specify: `community.network.exos_command`.

- [Synopsis](exos_command_module.md#synopsis)
- [Parameters](exos_command_module.md#parameters)
- [Notes](exos_command_module.md#notes)
- [Examples](exos_command_module.md#examples)
- [Return Values](exos_command_module.md#return-values)

## [Synopsis](exos_command_module.md#id1)

- Sends arbitrary commands to an Extreme EXOS device and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
- This module does not support running configuration commands. Please use [community.network.exos_config](exos_config_module.md#ansible-collections-community-network-exos-config-module) to configure EXOS devices.

## [Parameters](exos_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  string / required | List of commands to send to the remote EXOS device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired. |
| **interval**  string | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  Default: `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  Choices:   - `"any"` - `"all"` ← (default) |
| **retries**  string | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  Default: `10` |
| **wait_for**  string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Notes](exos_command_module.md#id3)

> **Note:**
>
> - If a command sent to the device requires answering a prompt, it is possible to pass a dict containing *command*, *answer* and *prompt*. See examples.

## [Examples](exos_command_module.md#id4)

```yaml+jinja
tasks:
  - name: Run show version on remote devices
    community.network.exos_command:
      commands: show version
  - name: Run show version and check to see if output contains ExtremeXOS
    community.network.exos_command:
      commands: show version
      wait_for: result[0] contains ExtremeXOS
  - name: Run multiple commands on remote nodes
    community.network.exos_command:
      commands:
        - show version
        - show ports no-refresh
  - name: Run multiple commands and evaluate the output
    community.network.exos_command:
      commands:
        - show version
        - show ports no-refresh
      wait_for:
        - result[0] contains ExtremeXOS
        - result[1] contains 20
  - name: Run command that requires answering a prompt
    community.network.exos_command:
      commands:
        - command: 'clear license-info'
          prompt: 'Are you sure.*'
          answer: 'Yes'
```

## [Return Values](exos_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  Returned: failed  Sample: `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  Returned: always apart from low level errors (such as action plugin)  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  Returned: always apart from low level errors (such as action plugin)  Sample: `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Rafael D. Vencioneck (@rdvencioneck)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
