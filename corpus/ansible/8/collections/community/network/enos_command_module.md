---
collection: ansible
version: "8"
title: "community.network.enos_command module – Run arbitrary commands on Lenovo ENOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/enos_command_module.html
fetched_at: 2026-07-28T01:56:32+00:00
---
# community.network.enos_command module – Run arbitrary commands on Lenovo ENOS devices

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
> To use it in a playbook, specify: `community.network.enos_command`.

- [Synopsis](enos_command_module.md#synopsis)
- [Parameters](enos_command_module.md#parameters)
- [Examples](enos_command_module.md#examples)
- [Return Values](enos_command_module.md#return-values)

## [Synopsis](enos_command_module.md#id1)

- Sends arbitrary commands to an ENOS node and returns the results read from the device. The `enos_command` module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

Aliases: network.enos.enos_command

## [Parameters](enos_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  **Choices:**   - `false` ← (default) - `true` |
| **commands**  string / required | List of commands to send to the remote device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retires as expired. |
| **interval**  string | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  **Default:** `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  **Choices:**   - `"any"` - `"all"` ← (default) |
| **retries**  string | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  **Default:** `10` |
| **wait_for**  string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Examples](enos_command_module.md#id3)

```yaml+jinja
---
- name: Test contains operator
  community.network.enos_command:
    commands:
      - show version
      - show system memory
    wait_for:
      - "result[0] contains 'Lenovo'"
      - "result[1] contains 'MemFree'"
  register: result

- ansible.builtin.assert:
    that:
      - "result.changed == false"
      - "result.stdout is defined"

- name: Get output for single command
  community.network.enos_command:
    commands: ['show version']
  register: result

- ansible.builtin.assert:
    that:
      - "result.changed == false"
      - "result.stdout is defined"

- name: Get output for multiple commands
  community.network.enos_command:
    commands:
      - show version
      - show interface information
  register: result

- ansible.builtin.assert:
    that:
      - "result.changed == false"
      - "result.stdout is defined"
      - "result.stdout | length == 2"
```

## [Return Values](enos_command_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | the conditionals that failed  **Returned:** failed  **Sample:** `["...", "..."]` |
| **stdout**  list / elements=string | the set of responses from the commands  **Returned:** always  **Sample:** `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  **Returned:** always  **Sample:** `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
