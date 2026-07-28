---
collection: ansible
version: "6"
title: "dellemc.os9.os9_command module – Run commands on remote devices running Dell OS9"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/os9/os9_command_module.html
fetched_at: 2026-07-27T17:26:07+00:00
---
# dellemc.os9.os9_command module – Run commands on remote devices running Dell OS9

> **Note:**
>
> This module is part of the [dellemc.os9 collection](https://galaxy.ansible.com/dellemc/os9) (version 1.0.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.os9`.
>
> To use it in a playbook, specify: `dellemc.os9.os9_command`.

- [Synopsis](os9_command_module.md#synopsis)
- [Parameters](os9_command_module.md#parameters)
- [Notes](os9_command_module.md#notes)
- [Examples](os9_command_module.md#examples)
- [Return Values](os9_command_module.md#return-values)

## [Synopsis](os9_command_module.md#id1)

- Sends arbitrary commands to a Dell OS9 node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
- This module does not support running commands in configuration mode. Please use **ERROR while parsing**: While parsing M() at index 81: Module name “dellemc_os9_os9_config” is not a FQCN to configure Dell OS9 devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](os9_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=string / required | List of commands to send to the remote os9 device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired. |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  Default: `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  Choices:   - `"all"` ← (default) - `"any"` |
| **provider**  dictionary | A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Password to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Path to an ssh key used to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies idle timeout (in seconds) for the connection. Useful if the console freezes before continuing. For example when saving configurations. |
| **username**  string | User to authenticate the SSH session to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **retries**  integer | Specifies the number of retries a command should be tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  Default: `10` |
| **wait_for**  list / elements=string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of *retries*, the task fails. See examples. |

## [Notes](os9_command_module.md#id3)

> **Note:**
>
> - This module requires Dell OS9 version 9.10.0.1P13 or above.
> - This module requires to increase the ssh connection rate limit. Use the following command *ip ssh connection-rate-limit 60* to configure the same. This can be done via **ERROR while parsing**: While parsing M() at index 170: Module name “os9_config” is not a FQCN module as well.
> - For more information on using Ansible to manage Dell EMC Network devices see <https://www.ansible.com/ansible-dell-networking>.

## [Examples](os9_command_module.md#id4)

```yaml+jinja
tasks:
  - name: run show version on remote devices
    os9_command:
      commands: show version
  - name: run show version and check to see if output contains OS9
    os9_command:
      commands: show version
      wait_for: result[0] contains OS9
  - name: run multiple commands on remote nodes
    os9_command:
      commands:
        - show version
        - show interfaces
  - name: run multiple commands and evaluate the output
    os9_command:
      commands:
        - show version
        - show interfaces
      wait_for:
        - result[0] contains OS9
        - result[1] contains Loopback
```

## [Return Values](os9_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  Returned: failed  Sample: `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  Returned: always apart from low level errors (such as action plugin)  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  Returned: always apart from low level errors (such as action plugin)  Sample: `[["...", "..."], ["..."], ["..."]]` |
| **warnings**  list / elements=string | The list of warnings (if any) generated by module based on arguments  Returned: always  Sample: `["...", "..."]` |

### Authors

- Dhivya P (@dhivyap)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.os9/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.os9)
