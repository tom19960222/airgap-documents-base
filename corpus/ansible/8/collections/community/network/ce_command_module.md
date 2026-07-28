---
collection: ansible
version: "8"
title: "community.network.ce_command module – Run arbitrary command on HUAWEI CloudEngine devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/ce_command_module.html
fetched_at: 2026-07-28T01:55:19+00:00
---
# community.network.ce_command module – Run arbitrary command on HUAWEI CloudEngine devices.

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
> To use it in a playbook, specify: `community.network.ce_command`.

- [Synopsis](ce_command_module.md#synopsis)
- [Parameters](ce_command_module.md#parameters)
- [Notes](ce_command_module.md#notes)
- [Examples](ce_command_module.md#examples)
- [Return Values](ce_command_module.md#return-values)

## [Synopsis](ce_command_module.md#id1)

- Sends an arbitrary command to an HUAWEI CloudEngine node and returns the results read from the device. The ce_command module includes an argument that will cause the module to wait for a specific condition before returning or timing out if the condition is not met.

Aliases: network.cloudengine.ce_command

## [Parameters](ce_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **commands**  string / required | The commands to send to the remote HUAWEI CloudEngine device over the configured provider. The resulting output from the command is returned. If the *wait_for* argument is provided, the module is not returned until the condition is satisfied or the number of *retries* has been exceeded. |
| **interval**  string | Configures the interval in seconds to wait between retries of the command. If the command does not pass the specified conditional, the interval indicates how to long to wait before trying the command again.  **Default:** `1` |
| **match**  string | The *match* argument is used in conjunction with the *wait_for* argument to specify the match policy. Valid values are `all` or `any`. If the value is set to `all` then all conditionals in the *wait_for* must be satisfied. If the value is set to `any` then only one of the values must be satisfied.  **Default:** `"all"` |
| **retries**  string | Specifies the number of retries a command should by tried before it is considered failed. The command is run on the target device every retry and evaluated against the *wait_for* conditionals.  **Default:** `10` |
| **wait_for**  string | Specifies what to evaluate from the output of the command and what conditionals to apply. This argument will cause the task to wait for a particular conditional to be true before moving forward. If the conditional is not true by the configured retries, the task fails. See examples. |

## [Notes](ce_command_module.md#id3)

> **Note:**
>
> - Recommended connection is `network_cli`.
> - This module also works with `local` connections for legacy playbooks.

## [Examples](ce_command_module.md#id4)

```yaml+jinja
# Note: examples below use the following provider dict to handle
#       transport and authentication to the node.

- name: CloudEngine command test
  hosts: cloudengine
  connection: local
  gather_facts: false
  vars:
    cli:
      host: "{{ inventory_hostname }}"
      port: "{{ ansible_ssh_port }}"
      username: "{{ username }}"
      password: "{{ password }}"
      transport: cli

  tasks:
  - name: "Run display version on remote devices"
    community.network.ce_command:
      commands: display version
      provider: "{{ cli }}"

  - name: "Run display version and check to see if output contains HUAWEI"
    community.network.ce_command:
      commands: display version
      wait_for: result[0] contains HUAWEI
      provider: "{{ cli }}"

  - name: "Run multiple commands on remote nodes"
    community.network.ce_command:
      commands:
        - display version
        - display device
      provider: "{{ cli }}"

  - name: "Run multiple commands and evaluate the output"
    community.network.ce_command:
      commands:
        - display version
        - display device
      wait_for:
        - result[0] contains HUAWEI
        - result[1] contains Device
      provider: "{{ cli }}"
```

## [Return Values](ce_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **failed_conditions**  list / elements=string | the conditionals that failed  **Returned:** failed  **Sample:** `["...", "..."]` |
| **stdout**  list / elements=string | the set of responses from the commands  **Returned:** always  **Sample:** `["...", "..."]` |
| **stdout_lines**  list / elements=string | The value of stdout split into a list  **Returned:** always  **Sample:** `[["...", "..."], ["..."], ["..."]]` |

### Authors

- JackyGao2016 (@CloudEngine-Ansible)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
