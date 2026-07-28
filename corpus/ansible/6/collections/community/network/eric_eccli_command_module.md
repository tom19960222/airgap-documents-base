---
collection: ansible
version: "6"
title: "community.network.eric_eccli_command module – Run commands on remote devices running ERICSSON ECCLI"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/eric_eccli_command_module.html
fetched_at: 2026-07-27T17:18:30+00:00
---
# community.network.eric_eccli_command module – Run commands on remote devices running ERICSSON ECCLI

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
> To use it in a playbook, specify: `community.network.eric_eccli_command`.

- [Synopsis](eric_eccli_command_module.md#synopsis)
- [Parameters](eric_eccli_command_module.md#parameters)
- [Notes](eric_eccli_command_module.md#notes)
- [Examples](eric_eccli_command_module.md#examples)
- [Return Values](eric_eccli_command_module.md#return-values)

## [Synopsis](eric_eccli_command_module.md#id1)

- Sends arbitrary commands to an ERICSSON eccli node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
- This module also support running commands in configuration mode in raw command style.

## [Parameters](eric_eccli_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=string / required | List of commands to send to the remote ECCLI device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired. If a command sent to the device requires answering a prompt, it is possible to pass a dict containing *command*, *answer* and *prompt*. Common answers are ‘y’ or “\r” (carriage return, must be double quotes). See examples. |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  Default: `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  Choices:   - `"any"` - `"all"` ← (default) |
| **retries**  integer | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  Default: `10` |
| **wait_for**  aliases: waitfor  list / elements=string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Notes](eric_eccli_command_module.md#id3)

> **Note:**
>
> - Tested against IPOS 19.3
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Ericsson devices see the Ericsson documents.
> - Starting with Ansible 2.5 we recommend using `connection: network_cli`.
> - For more information please see the [ERIC_ECCLI Platform Options guide](user_guide/platform_eric_eccli.md).

## [Examples](eric_eccli_command_module.md#id4)

```yaml+jinja
tasks:
  - name: Run show version on remote devices
    community.network.eric_eccli_command:
      commands: show version

  - name: Run show version and check to see if output contains IPOS
    community.network.eric_eccli_command:
      commands: show version
      wait_for: result[0] contains IPOS

  - name: Run multiple commands on remote nodes
    community.network.eric_eccli_command:
      commands:
        - show version
        - show running-config interfaces

  - name: Run multiple commands and evaluate the output
    community.network.eric_eccli_command:
      commands:
        - show version
        - show running-config interfaces
      wait_for:
        - result[0] contains IPOS
        - result[1] contains management
```

## [Return Values](eric_eccli_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  Returned: failed  Sample: `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  Returned: always apart from low level errors (such as action plugin)  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  Returned: always apart from low level errors (such as action plugin)  Sample: `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Ericsson IPOS OAM team (@itercheng)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
