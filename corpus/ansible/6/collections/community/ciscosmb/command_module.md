---
collection: ansible
version: "6"
title: "community.ciscosmb.command module – Run commands on remote Cisco SMB devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/ciscosmb/command_module.html
fetched_at: 2026-07-27T17:06:06+00:00
---
# community.ciscosmb.command module – Run commands on remote Cisco SMB devices

> **Note:**
>
> This module is part of the [community.ciscosmb collection](https://galaxy.ansible.com/community/ciscosmb) (version 1.0.5).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.ciscosmb`.
>
> To use it in a playbook, specify: `community.ciscosmb.command`.

- [Synopsis](command_module.md#synopsis)
- [Parameters](command_module.md#parameters)
- [Examples](command_module.md#examples)
- [Return Values](command_module.md#return-values)

## [Synopsis](command_module.md#id1)

- Sends arbitrary commands to an Cisco SMB node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

## [Parameters](command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=string / required | List of commands to send to the remote Cisco SMB device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired. |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  Default: `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  Choices:   - `"any"` - `"all"` ← (default) |
| **retries**  integer | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  Default: `10` |
| **wait_for**  list / elements=string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Examples](command_module.md#id3)

```yaml+jinja
- name: Run command on remote devices
  community.ciscosmb.command:
    commands: show version

- name: Run command and check to see if output contains PID
  community.ciscosmb.command:
    commands: show inventory
    wait_for: result[0] contains PID

- name: Run multiple commands on remote nodes
  community.ciscosmb.command:
    commands:
      - show version
      - show system

- name: Run multiple commands and evaluate the output
  community.ciscosmb.command:
    commands:
      - show version
      - show system
    wait_for:
      - result[0] contains Active-image
      - result[1] contains "System Up Time"
```

## [Return Values](command_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed.  Returned: failed  Sample: `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands.  Returned: always apart from low level errors (such as action plugin)  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list.  Returned: always apart from low level errors (such as action plugin)  Sample: `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Petr Klima (@qaxi)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.ciscosmb/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.ciscosmb)
