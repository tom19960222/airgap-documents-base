---
collection: ansible
version: "8"
title: "cisco.ios.ios_command module – Module to run commands on remote devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_command_module.html
fetched_at: 2026-07-28T01:04:36+00:00
---
# cisco.ios.ios_command module – Module to run commands on remote devices.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_command`.

New in cisco.ios 1.0.0

- [Synopsis](ios_command_module.md#synopsis)
- [Parameters](ios_command_module.md#parameters)
- [Notes](ios_command_module.md#notes)
- [Examples](ios_command_module.md#examples)
- [Return Values](ios_command_module.md#return-values)

## [Synopsis](ios_command_module.md#id1)

- Sends arbitrary commands to an ios node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
- This module does not support running commands in configuration mode. Please use [ios_config](https://docs.ansible.com/ansible/latest/collections/cisco/ios/ios_config_module.html#ansible-collections-cisco-ios-ios-config-module) to configure IOS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: command

## [Parameters](ios_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=any / required | List of commands to send to the remote ios device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired. If a command sent to the device requires answering a prompt, it is possible to pass a dict containing *command*, *answer* and *prompt*. Common answers are ‘y’ or “\r” (carriage return, must be double quotes). See examples. |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  **Default:** `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  **Choices:**   - `"any"` - `"all"` ← (default) |
| **retries**  integer | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditions.  **Default:** `9` |
| **wait_for**  aliases: waitfor  list / elements=string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Notes](ios_command_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_command_module.md#id4)

```yaml+jinja
- name: Run show version on remote devices
  cisco.ios.ios_command:
    commands: show version'

# output-

# ok: [iosxeappliance] => {
#     "changed": false,
#     "invocation": {
#         "module_args": {
#             "commands": [
#                 "show version"
#             ],
#             "interval": 1,
#             "match": "all",
#             "retries": 10,
#             "wait_for": null
#         }
#     },
#     "stdout": [
#         "Cisco IOS XE Software, Version 17.03.04a\nCisco IOS Software [Amsterdam], Virtual XE Software ... register is 0x2102"
#     ],
#     "stdout_lines": [
#         [
#             "Cisco IOS XE Software, Version 17.03.04a",
#             "Cisco IOS Software [Amsterdam], Virtual XE Software",
#             "..."
#             "Configuration register is 0x2102"
#         ]
#     ]
# }

- name: Run show version and check to see if output contains IOS
  cisco.ios.ios_command:
    commands: show version
    wait_for: result[0] contains IOS

# output-

# ok: [iosxeappliance] => {
#     "changed": false,
#     "invocation": {
#         "module_args": {
#             "commands": [
#                 "show version"
#             ],
#             "interval": 1,
#             "match": "all",
#             "retries": 10,
#             "wait_for": [
#                 "result[0] contains IOS"
#             ]
#         }
#     },
#     "stdout": [
#         "Cisco IOS XE Software, Version 17.03.04a\nCisco IOS Software [Amsterdam], Virtual XE Software ... register is 0x2102"
#     ],
#     "stdout_lines": [
#         [
#             "Cisco IOS XE Software, Version 17.03.04a",
#             "Cisco IOS Software [Amsterdam], Virtual XE Software",
#             "..."
#             "Configuration register is 0x2102"
#         ]
#     ]
# }

- name: Run multiple commands on remote nodes
  cisco.ios.ios_command:
    commands:
      - show version
      - show interfaces

# output-

# ok: [iosxeappliance] => {
#     "changed": false,
#     "invocation": {
#         "module_args": {
#             "commands": [
#                 "show version",
#                 "show interfaces"
#             ],
#             "interval": 1,
#             "match": "all",
#             "retries": 10,
#             "wait_for": null
#         }
#     },
#     "stdout": [
#         "Cisco IOS XE Software, Version 17.03.04a\nCisco IOS Software [Amsterdam], Virtual XE Software Configuration register is 0x2102",
#         "Loopback999 is up, line protocol is up ...failures, 0 output buffers swapped out"
#     ],
#     "stdout_lines": [
#         [
#             "Cisco IOS XE Software, Version 17.03.04a",
#             "Cisco IOS Software [Amsterdam], Virtual XE Software",
#             "..."
#             "Configuration register is 0x2102"
#         ],
#         [
#             "Loopback999 is up, line protocol is up ",
#             "  Hardware is Loopback",
#             "  Description: this is a test",
#             "  MTU 1514 bytes, BW 8000000 Kbit/sec, DLY 5000 usec, ",
#             "     reliability 255/255, txload 1/255, rxload 1/255",
#             "  Encapsulation LOOPBACK, loopback not set",
#             "  Keepalive set (10 sec)",
#             "  Last input never, output never, output hang never",
#             "  Last clearing of \"show interface\" counters never",
#             "  Input queue: 0/75/0/0 (size/max/drops/flushes); Total output drops: 0",
#             "  Queueing strategy: fifo",
#             "  Output queue: 0/0 (size/max)",
#             "  5 minute input rate 0 bits/sec, 0 packets/sec",
#             "  5 minute output rate 0 bits/sec, 0 packets/sec",
#             "     0 packets input, 0 bytes, 0 no buffer",
#             "     Received 0 broadcasts (0 IP multicasts)",
#             "     0 runts, 0 giants, 0 throttles ",
#             "     0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort",
#             "     0 packets output, 0 bytes, 0 underruns",
#             "     Output 0 broadcasts (0 IP multicasts)",
#             "     0 output errors, 0 collisions, 0 interface resets",
#             "     0 unknown protocol drops",
#             "     0 output buffer failures, 0 output buffers swapped out"
#         ]
#     ]
# }

- name: Run multiple commands and evaluate the output
  cisco.ios.ios_command:
    commands:
      - show version
      - show interfaces
    wait_for:
      - result[0] contains IOS
      - result[1] contains Loopback0

# output-
# failed play as result[1] contains Loopback0 is false

# fatal: [iosxeappliance]: FAILED! => {
#     "changed": false,
#     "failed_conditions": [
#         "result[1] contains Loopback0"
#     ],
#     "invocation": {
#         "module_args": {
#             "commands": [
#                 "show version",
#                 "show interfaces"
#             ],
#             "interval": 1,
#             "match": "all",
#             "retries": 10,
#             "wait_for": [
#                 "result[0] contains IOS",
#                 "result[1] contains Loopback0"
#             ]
#         }
#     },
#     "msg": "One or more conditional statements have not been satisfied"
# }

- name: Run commands that require answering a prompt
  cisco.ios.ios_command:
    commands:
      - command: "clear counters GigabitEthernet2"
        prompt: 'Clear "show interface" counters on this interface \[confirm\]'
        answer: "y"
      - command: "clear counters GigabitEthernet3"
        prompt: "[confirm]"
        answer: "\r"

# output-

# ok: [iosxeappliance] => {
#     "changed": false,
#     "invocation": {
#         "module_args": {
#             "commands": [
#                 {
#                     "answer": "y",
#                     "check_all": false,
#                     "command": "clear counters GigabitEthernet2",
#                     "newline": true,
#                     "output": null,
#                     "prompt": "Clear \"show interface\" counters on this interface \\[confirm\\]",
#                     "sendonly": false
#                 },
#                 {
#                     "answer": "\r",
#                     "check_all": false,
#                     "command": "clear counters GigabitEthernet3",
#                     "newline": true,
#                     "output": null,
#                     "prompt": "[confirm]",
#                     "sendonly": false
#                 }
#             ],
#             "interval": 1,
#             "match": "all",
#             "retries": 10,
#             "wait_for": null
#         }
#     },
#     "stdout": [
#         "Clear \"show interface\" counters on this interface [confirm]y",
#         "Clear \"show interface\" counters on this interface [confirm]"
#     ],
#     "stdout_lines": [
#         [
#             "Clear \"show interface\" counters on this interface [confirm]y"
#         ],
#         [
#             "Clear \"show interface\" counters on this interface [confirm]"
#         ]
#     ]
# }

- name: Run commands with complex values like special characters in variables
  cisco.ios.ios_command:
    commands:
      ["{{ 'test aaa group TEST ' ~ user ~ ' ' ~ password ~ ' new-code' }}"]
  vars:
    user: "dummy"
    password: "!dummy"

# ok: [iosxeappliance] => {
#     "changed": false,
#     "invocation": {
#         "module_args": {
#             "commands": [
#                 "test aaa group group test !dummy new-code"
#             ],
#             "interval": 1,
#             "match": "all",
#             "retries": 10,
#             "wait_for": null
#         }
#     },
#     "stdout": [
#         "User was successfully authenticated."
#     ],
#     "stdout_lines": [
#         [
#             "User was successfully authenticated."
#         ]
#     ]
# }
```

## [Return Values](ios_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  **Returned:** failed  **Sample:** `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  **Returned:** always apart from low level errors (such as action plugin)  **Sample:** `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  **Returned:** always apart from low level errors (such as action plugin)  **Sample:** `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
