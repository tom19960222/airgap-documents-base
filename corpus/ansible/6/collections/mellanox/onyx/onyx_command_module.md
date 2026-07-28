---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_command module – Run commands on remote devices running Mellanox ONYX"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_command_module.html
fetched_at: 2026-07-27T17:55:24+00:00
---
# mellanox.onyx.onyx_command module – Run commands on remote devices running Mellanox ONYX

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_command`.

- [Synopsis](onyx_command_module.md#synopsis)
- [Parameters](onyx_command_module.md#parameters)
- [Notes](onyx_command_module.md#notes)
- [Examples](onyx_command_module.md#examples)
- [Return Values](onyx_command_module.md#return-values)

## [Synopsis](onyx_command_module.md#id1)

- Sends arbitrary commands to an Mellanox ONYX network device and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
- This module does not support running commands in configuration mode. Please use **ERROR while parsing**: While parsing M() at index 81: Module name “onyx_config” is not a FQCN to configure Mellanox ONYX devices.

## [Parameters](onyx_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  string / required | List of commands to send to the remote Mellanox ONYX network device. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired. |
| **interval**  string | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  Default: `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  Choices:   - `"any"` - `"all"` ← (default) |
| **retries**  string | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  Default: `10` |
| **wait_for**  string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Notes](onyx_command_module.md#id3)

> **Note:**
>
> - Tested on ONYX 3.6.4000

## [Examples](onyx_command_module.md#id4)

```yaml+jinja
tasks:
  - name: Run show version on remote devices
    onyx_command:
      commands: show version

  - name: Run show version and check to see if output contains MLNXOS
    onyx_command:
      commands: show version
      wait_for: result[0] contains MLNXOS

  - name: Run multiple commands on remote nodes
    onyx_command:
      commands:
        - show version
        - show interfaces

  - name: Run multiple commands and evaluate the output
    onyx_command:
      commands:
        - show version
        - show interfaces
      wait_for:
        - result[0] contains MLNXOS
        - result[1] contains mgmt1
```

## [Return Values](onyx_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  Returned: failed  Sample: `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  Returned: always apart from low level errors (such as action plugin)  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  Returned: always apart from low level errors (such as action plugin)  Sample: `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Samer Deeb (@samerd)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
