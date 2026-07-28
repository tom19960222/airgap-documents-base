---
collection: ansible
version: "8"
title: "ansible.netcommon.telnet module – Executes a low-down and dirty telnet command"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/netcommon/telnet_module.html
fetched_at: 2026-07-28T01:09:13+00:00
---
# ansible.netcommon.telnet module – Executes a low-down and dirty telnet command

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ui/repo/published/ansible/netcommon/) (version 5.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.telnet`.

New in ansible.netcommon 1.0.0

- [Synopsis](telnet_module.md#synopsis)
- [Parameters](telnet_module.md#parameters)
- [Notes](telnet_module.md#notes)
- [Examples](telnet_module.md#examples)
- [Return Values](telnet_module.md#return-values)

## [Synopsis](telnet_module.md#id1)

- Executes a low-down and dirty telnet command, not going through the module subsystem.
- This is mostly to be used for enabling ssh on devices that only have telnet enabled by default.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](telnet_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **command**  aliases: commands  list / elements=string / required | List of commands to be executed in the telnet session. |
| **crlf**  boolean | Sends a CRLF (Carrage Return) instead of just a LF (Line Feed).  **Choices:**   - `false` ← (default) - `true` |
| **host**  string | The host/target on which to execute the command  **Default:** `"remote_addr"` |
| **login_prompt**  string | Login or username prompt to expect  **Default:** `"login: "` |
| **password**  string | The password for login |
| **password_prompt**  string | Login or username prompt to expect  **Default:** `"Password: "` |
| **pause**  integer | Seconds to pause between each command issued  **Default:** `1` |
| **port**  integer | Remote port to use  **Default:** `23` |
| **prompts**  list / elements=string | List of prompts expected before sending next command  **Default:** `["$"]` |
| **send_newline**  boolean | Sends a newline character upon successful connection to start the terminal session.  **Choices:**   - `false` ← (default) - `true` |
| **timeout**  integer | timeout for remote operations  **Default:** `120` |
| **user**  string | The user for login  **Default:** `"remote_user"` |

## [Notes](telnet_module.md#id3)

> **Note:**
>
> - The `environment` keyword does not work with this task

## [Examples](telnet_module.md#id4)

```yaml+jinja
- name: send configuration commands to IOS
  ansible.netcommon.telnet:
    user: cisco
    password: cisco
    login_prompt: 'Username: '
    prompts:
    - '[>#]'
    command:
    - terminal length 0
    - configure terminal
    - hostname ios01

- name: run show commands
  ansible.netcommon.telnet:
    user: cisco
    password: cisco
    login_prompt: 'Username: '
    prompts:
    - '[>#]'
    command:
    - terminal length 0
    - show version
```

## [Return Values](telnet_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  list / elements=string | output of each command is an element in this list  **Returned:** always  **Sample:** `["success", "success", "", "warning .. something"]` |

### Authors

- Ansible Core Team

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
