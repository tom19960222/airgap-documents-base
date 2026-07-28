---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_command module – Module to run commands on remote devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_command_module.html
fetched_at: 2026-07-27T16:55:40+00:00
---
# cisco.iosxr.iosxr_command module – Module to run commands on remote devices.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/cisco/iosxr) (version 3.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_command`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_command_module.md#synopsis)
- [Parameters](iosxr_command_module.md#parameters)
- [Notes](iosxr_command_module.md#notes)
- [Examples](iosxr_command_module.md#examples)
- [Return Values](iosxr_command_module.md#return-values)

## [Synopsis](iosxr_command_module.md#id1)

- Sends arbitrary commands to an IOS XR node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
- This module does not support running commands in configuration mode. Please use [cisco.iosxr.iosxr_config](iosxr_config_module.md#ansible-collections-cisco-iosxr-iosxr-config-module) to configure iosxr devices.

## [Parameters](iosxr_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=any / required | List of commands to send to the remote iosxr device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired.  If a command sent to the device requires answering a prompt, it is possible to pass a dict containing command, answer and prompt. Common answers are ‘y’ or “\r” (carriage return, must be double quotes). See examples |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  Default: `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  Choices:   - `"any"` - `"all"` ← (default) |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Specifies the type of connection based transport.  Choices:   - `"cli"` ← (default) - `"netconf"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **retries**  integer | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  Default: `10` |
| **wait_for**  aliases: waitfor  list / elements=string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Notes](iosxr_command_module.md#id3)

> **Note:**
>
> - Make sure the user has been authorized to execute commands terminal length 0, terminal width 512 and terminal exec prompt no-timestamp.
> - This module works with `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).
> - This module does not support `netconf` connection.
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](iosxr_command_module.md#id4)

```yaml+jinja
- name: run show version on remote devices
  cisco.iosxr.iosxr_command:
    commands: show version

- name: run show version and check to see if output contains iosxr
  cisco.iosxr.iosxr_command:
    commands: show version
    wait_for: result[0] contains IOS-XR

- name: run multiple commands on remote nodes
  cisco.iosxr.iosxr_command:
    commands:
    - show version
    - show interfaces
    - {command: example command that prompts, prompt: expected prompt, answer: yes}

- name: run multiple commands and evaluate the output
  cisco.iosxr.iosxr_command:
    commands:
    - show version
    - show interfaces
    wait_for:
    - result[0] contains IOS-XR
    - result[1] contains Loopback0
```

## [Return Values](iosxr_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  Returned: failed  Sample: `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  Returned: always apart from low level errors (such as action plugin)  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  Returned: always apart from low level errors (such as action plugin)  Sample: `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
