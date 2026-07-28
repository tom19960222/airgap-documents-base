---
collection: ansible
version: "8"
title: "community.routeros.command module – Run commands on remote devices running MikroTik RouterOS"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/routeros/command_module.html
fetched_at: 2026-07-28T01:59:03+00:00
---
# community.routeros.command module – Run commands on remote devices running MikroTik RouterOS

> **Note:**
>
> This module is part of the [community.routeros collection](https://galaxy.ansible.com/ui/repo/published/community/routeros/) (version 2.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.routeros`.
>
> To use it in a playbook, specify: `community.routeros.command`.

- [Synopsis](command_module.md#synopsis)
- [Parameters](command_module.md#parameters)
- [Attributes](command_module.md#attributes)
- [Notes](command_module.md#notes)
- [See Also](command_module.md#see-also)
- [Examples](command_module.md#examples)
- [Return Values](command_module.md#return-values)

## [Synopsis](command_module.md#id1)

- Sends arbitrary commands to an RouterOS node and returns the results read from the device. This module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.
- The module always indicates a (changed) status. You can use [the changed_when task property](../../../playbook_guide/playbooks_error_handling.md#override-the-changed-result) to determine whether a command task actually resulted in a change or not.

## [Parameters](command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  list / elements=string / required | List of commands to send to the remote RouterOS device over the configured provider. The resulting output from the command is returned. If the `wait_for` argument is provided, the module is not returned until the condition is satisfied or the number of retries has expired. |
| **interval**  integer | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditions, the interval indicates how long to wait before trying the command again.  **Default:** `1` |
| **match**  string | The `match` argument is used in conjunction with the `wait_for` argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the wait_for must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  **Choices:**   - `"any"` - `"all"` ← (default) |
| **retries**  integer | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the `wait_for` conditions.  **Default:** `10` |
| **wait_for**  list / elements=string | List of conditions to evaluate against the output of the command. The task will wait for each condition to be true before moving forward. If the conditional is not true within the configured number of retries, the task fails. See examples. |

## [Attributes](command_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **partial**  The module claims to support check mode, but it simply always executes the command. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **platform** | **Platform:** **RouterOS** | Target OS/families that can be operated against. |

## [Notes](command_module.md#id4)

> **Note:**
>
> - The module declares that it **supports check mode**. This is a bug and will be changed in community.routeros 3.0.0.

## [See Also](command_module.md#id5)

> **See also:**
>
> [How to connect to RouterOS devices with SSH](docsite/ssh-guide.md#ansible-collections-community-routeros-docsite-ssh-guide)
> :   How to connect to RouterOS devices with SSH
>
> [How to quote and unquote commands and arguments](docsite/quoting.md#ansible-collections-community-routeros-docsite-quoting)
> :   How to quote and unquote commands and arguments

## [Examples](command_module.md#id6)

```yaml+jinja
- name: Run command on remote devices
  community.routeros.command:
    commands: /system routerboard print

- name: Run command and check to see if output contains routeros
  community.routeros.command:
    commands: /system resource print
    wait_for: result[0] contains MikroTik

- name: Run multiple commands on remote nodes
  community.routeros.command:
    commands:
      - /system routerboard print
      - /system identity print

- name: Run multiple commands and evaluate the output
  community.routeros.command:
    commands:
      - /system routerboard print
      - /interface ethernet print
    wait_for:
      - result[0] contains x86
      - result[1] contains ether1
```

## [Return Values](command_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | The list of conditionals that have failed  **Returned:** failed  **Sample:** `["...", "..."]` |
| **stdout**  list / elements=string | The set of responses from the commands  **Returned:** always apart from low level errors (such as action plugin)  **Sample:** `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  **Returned:** always apart from low level errors (such as action plugin)  **Sample:** `[["...", "..."], ["..."], ["..."]]` |

### Authors

- Egor Zaitsev (@heuels)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.routeros/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.routeros)
- [Submit a bug report](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-routeros)
