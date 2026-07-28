---
collection: ansible
version: "6"
title: "arista.eos.eos_command module – Run arbitrary commands on an Arista EOS device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_command_module.html
fetched_at: 2026-07-27T16:45:09+00:00
---
# arista.eos.eos_command module – Run arbitrary commands on an Arista EOS device

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/arista/eos) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_command`.

New in arista.eos 1.0.0

- [Synopsis](eos_command_module.md#synopsis)
- [Parameters](eos_command_module.md#parameters)
- [Notes](eos_command_module.md#notes)
- [Examples](eos_command_module.md#examples)
- [Return Values](eos_command_module.md#return-values)

## [Synopsis](eos_command_module.md#id1)

- Sends an arbitrary set of commands to an EOS node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

## [Parameters](eos_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=any / required | The commands to send to the remote EOS device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of *retries* has been exceeded.  Commands may be represented either as simple strings or as dictionaries as described below. Refer to the Examples setion for some common uses. |
| **answer**  list / elements=string | The answer to reply with if *prompt* is matched. The value can be a single answer or a list of answer for multiple prompts. In case the command execution results in multiple prompts the sequence of the prompt and excepted answer should be in same order. |
| **check_all**  boolean | By default if any one of the prompts mentioned in `prompt` option is matched it won’t check for other prompts. This boolean flag, that when set to *True* will check for all the prompts mentioned in `prompt` option in the given order. If the option is set to *True* all the prompts should be received from remote host if not it will result in timeout.  Choices:   - `false` ← (default) - `true` |
| **command**  string / required | The command to send to the remote network device. The resulting output from the command is returned, unless *sendonly* is set. |
| **newline**  boolean | The boolean value, that when set to false will send *answer* to the device without a trailing newline.  Choices:   - `false` - `true` ← (default) |
| **output**  string | How the remote device should format the command response data.  Choices:   - `"text"` - `"json"` |
| **prompt**  list / elements=string | A single regex pattern or a sequence of patterns to evaluate the expected prompt from *command*. |
| **sendonly**  boolean | The boolean value, that when set to true will send *command* to the device but not wait for a result.  Choices:   - `false` ← (default) - `true` |
| **version**  string | Specifies the version of the JSON response returned when *output=json*.  Choices:   - `"1"` - `"latest"` ← (default) |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditional, the interval indicates how to long to wait before trying the command again.  Default: `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the *wait_for* must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  Choices:   - `"any"` - `"all"` ← (default) |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  Starting with Ansible 2.6 we recommend using `connection: httpapi` for eAPI.  This option will be removed in a release after 2022-06-01.  For more information please see the [EOS Platform Options guide](../network/user_guide/platform_eos.md).   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This is a common argument used for either *cli* or *eapi* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. This value applies to either *cli* or *eapi*.  The port value will default to the appropriate transport common port if none is provided in the task (cli=22, http=80, https=443).  Default: `0` |
| **ssh_keyfile**  path | Specifies the SSH keyfile to use to authenticate the connection to the remote device. This argument is only used for *cli* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` ← (default) - `"eapi"` |
| **use_proxy**  boolean | If `no`, the environment variables `http_proxy` and `https_proxy` will be ignored.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | Configures the *transport* to use SSL if set to `yes` only when the `transport=eapi`. If the transport argument is not eapi, this value is ignored.  Choices:   - `false` - `true` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate either the CLI login or the eAPI authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates. If the transport argument is not eapi, this value is ignored.  Choices:   - `false` - `true` ← (default) |
| **retries**  integer | Specifies the number of retries a command should be tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditionals.  Default: `10` |
| **wait_for**  aliases: waitfor  list / elements=string | Specifies what to evaluate from the output of the command and what conditionals to apply. This argument will cause the task to wait for a particular conditional to be true before moving forward. If the conditional is not true by the configured retries, the task fails. Note - With *wait_for* the value in `result['stdout']` can be accessed using `result`, that is to access `result['stdout'][0]` use `result[0]` See examples. |

## [Notes](eos_command_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - For information on using CLI, eAPI and privileged mode see the :ref:`EOS Platform Options guide <eos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Arista EOS devices see the `Arista integration page <<https://www.ansible.com/ansible-arista-networks>>`_.

## [Examples](eos_command_module.md#id4)

```yaml+jinja
- name: run show version on remote devices
  arista.eos.eos_command:
    commands: show version

- name: run show version and check to see if output contains Arista
  arista.eos.eos_command:
    commands: show version
    wait_for: result[0] contains Arista

- name: run multiple commands on remote nodes
  arista.eos.eos_command:
    commands:
    - show version
    - show interfaces

- name: run multiple commands and evaluate the output
  arista.eos.eos_command:
    commands:
    - show version
    - show interfaces
    wait_for:
    - result[0] contains Arista
    - result[1] contains Loopback0

- name: run commands and specify the output format
  arista.eos.eos_command:
    commands:
    - command: show version
      output: json

- name: check whether the switch is in maintenance mode
  arista.eos.eos_command:
    commands: show maintenance
    wait_for: result[0] contains 'Under Maintenance'

- name: check whether the switch is in maintenance mode using json output
  arista.eos.eos_command:
    commands:
    - command: show maintenance
      output: json
    wait_for: result[0].units.System.state eq 'underMaintenance'

- name: check whether the switch is in maintenance, with 8 retries
    and 2 second interval between retries
  arista.eos.eos_command:
    commands: show maintenance
    wait_for: result[0]['units']['System']['state'] eq 'underMaintenance'
    interval: 2
    retries: 8

- name: run a command that requires a confirmation. Note that prompt
    takes regexes, and so strings containing characters like brackets
    need to be escaped.
  arista.eos.eos_command:
    commands:
    - command: reload power
      prompt: \[confirm\]
      answer: y
      newline: false
```

## [Return Values](eos_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  Returned: failed  Sample: `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  Returned: always apart from low level errors (such as action plugin)  Sample: `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  Returned: always apart from low level errors (such as action plugin)  Sample: `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
