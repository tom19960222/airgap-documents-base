---
collection: ansible
version: "6"
title: "cisco.asa.asa_command module – Run arbitrary commands on Cisco ASA devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/asa/asa_command_module.html
fetched_at: 2026-07-27T16:50:46+00:00
---
# cisco.asa.asa_command module – Run arbitrary commands on Cisco ASA devices

> **Note:**
>
> This module is part of the [cisco.asa collection](https://galaxy.ansible.com/cisco/asa) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.asa`.
>
> To use it in a playbook, specify: `cisco.asa.asa_command`.

New in cisco.asa 1.0.0

- [Synopsis](asa_command_module.md#synopsis)
- [Parameters](asa_command_module.md#parameters)
- [Notes](asa_command_module.md#notes)
- [Examples](asa_command_module.md#examples)
- [Return Values](asa_command_module.md#return-values)

## [Synopsis](asa_command_module.md#id1)

- Sends arbitrary commands to an ASA node and returns the results read from the device. The `asa_command` module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](asa_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **authorize**  boolean | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` and `become: yes`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` - `true` |
| **commands**  list / elements=string / required | List of commands to send to the remote device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retires as expired. |
| **context**  string | Specifies which context to target if you are running in the ASA in multiple context mode. Defaults to the current context you login to. |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  Default: `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  Choices:   - `"any"` - `"all"` ← (default) |
| **passwords**  boolean | Saves running-config passwords in clear-text when set to True. Defaults to False  Choices:   - `false` - `true` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies idle timeout in seconds for the connection, in seconds. Useful if the console freezes before continuing. For example when saving configurations. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **retries**  integer | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  Default: `10` |
| **wait_for**  aliases: waitfor  list / elements=string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Notes](asa_command_module.md#id3)

> **Note:**
>
> - When processing wait_for, each commands’ output is stored as an element of the *result* array. The allowed operators for conditional evaluation are *eq*, *==*, *neq*, *ne*, *!=*, *gt*, *>*, *ge*, *>=*, *lt*, *<*, *le*, *<=*, *contains*, *matches*. Operators can be prefaced by *not* to negate their meaning. The *contains* operator searches for a substring match (like the Python *in* operator). The *matches* operator searches using a regex search operation.
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](asa_command_module.md#id4)

```yaml+jinja
- name: Show the ASA version
  cisco.asa.asa_command:
    commands:
    - show version

- name: Show ASA drops and memory
  cisco.asa.asa_command:
    commands:
    - show asp drop
    - show memory

- name: Send repeat pings and wait for the result to pass 100%
  cisco.asa.asa_command:
    commands:
    - ping 8.8.8.8 repeat 20 size 350
    wait_for:
    - result[0] contains 100
    retries: 2
```

## [Return Values](asa_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | the conditionals that failed  Returned: failed  Sample: `["...", "..."]` |
| **stdout**  list / elements=string | the set of responses from the commands  Returned: always  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  Returned: always  Sample: `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Peter Sprygada (@privateip), Patrick Ogenstad (@ogenstad)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.asa/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.asa)
