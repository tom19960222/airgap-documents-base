---
collection: ansible
version: "6"
title: "ansible.netcommon.cli_command module – Run a cli command on cli-based network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/cli_command_module.html
fetched_at: 2026-07-27T16:43:00+00:00
---
# ansible.netcommon.cli_command module – Run a cli command on cli-based network devices

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.cli_command`.

New in ansible.netcommon 1.0.0

- [Synopsis](cli_command_module.md#synopsis)
- [Parameters](cli_command_module.md#parameters)
- [Notes](cli_command_module.md#notes)
- [Examples](cli_command_module.md#examples)
- [Return Values](cli_command_module.md#return-values)

## [Synopsis](cli_command_module.md#id1)

- Sends a command to a network device and returns the result read from the device.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](cli_command_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **answer**  list / elements=string | The answer to reply with if *prompt* is matched. The value can be a single answer or a list of answer for multiple prompts. In case the command execution results in multiple prompts the sequence of the prompt and excepted answer should be in same order. |
| **check_all**  boolean | By default if any one of the prompts mentioned in `prompt` option is matched it won’t check for other prompts. This boolean flag, that when set to *True* will check for all the prompts mentioned in `prompt` option in the given order. If the option is set to *True* all the prompts should be received from remote host if not it will result in timeout.  Choices:   - `false` ← (default) - `true` |
| **command**  string / required | The command to send to the remote network device. The resulting output from the command is returned, unless *sendonly* is set. |
| **newline**  boolean | The boolean value, that when set to false will send *answer* to the device without a trailing newline.  Choices:   - `false` - `true` ← (default) |
| **prompt**  list / elements=string | A single regex pattern or a sequence of patterns to evaluate the expected prompt from *command*. |
| **sendonly**  boolean | The boolean value, that when set to true will send *command* to the device but not wait for a result.  Choices:   - `false` ← (default) - `true` |

## [Notes](cli_command_module.md#id3)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](cli_command_module.md#id4)

```yaml+jinja
- name: run show version on remote devices
  ansible.netcommon.cli_command:
    command: show version

- name: run command with json formatted output
  ansible.netcommon.cli_command:
    command: show version | json

- name: run command expecting user confirmation
  ansible.netcommon.cli_command:
    command: commit replace
    prompt: This commit will replace or remove the entire running configuration
    answer: yes

- name: run command expecting user confirmation
  ansible.netcommon.cli_command:
    command: show interface summary
    prompt: Press any key to continue
    answer: y
    newline: false

- name: run config mode command and handle prompt/answer
  ansible.netcommon.cli_command:
    command: '{{ item }}'
    prompt:
    - Exit with uncommitted changes
    answer: y
  loop:
  - configure
  - set system syslog file test any any
  - exit

- name: multiple prompt, multiple answer (mandatory check for all prompts)
  ansible.netcommon.cli_command:
    command: copy sftp sftp://user@host//user/test.img
    check_all: true
    prompt:
    - Confirm download operation
    - Password
    - Do you want to change that to the standby image
    answer:
    - y
    - <password>
    - y
```

## [Return Values](cli_command_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **json**  dictionary | A dictionary representing a JSON-formatted response  Returned: when the device response is valid JSON  Sample: `"{\n  \"architecture\": \"i386\",\n  \"bootupTimestamp\": 1532649700.56,\n  \"modelName\": \"vEOS\",\n  \"version\": \"4.15.9M\"\n  [...]\n}\n"` |
| **stdout**  string | The response from the command  Returned: when sendonly is false  Sample: `"Version:      VyOS 1.1.7[...]"` |

### Authors

- Nathaniel Case (@Qalthos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
