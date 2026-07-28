---
collection: ansible
version: "8"
title: "inspur.ispim.edit_boot_option module – Set BIOS boot options"
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/ispim/edit_boot_option_module.html
fetched_at: 2026-07-28T02:36:34+00:00
---
# inspur.ispim.edit_boot_option module – Set BIOS boot options

> **Note:**
>
> This module is part of the [inspur.ispim collection](https://galaxy.ansible.com/ui/repo/published/inspur/ispim/) (version 1.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install inspur.ispim`.
> You need further requirements to be able to use this module,
> see [Requirements](edit_boot_option_module.md#ansible-collections-inspur-ispim-edit-boot-option-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.edit_boot_option`.

New in inspur.ispim 1.0.0

- [Synopsis](edit_boot_option_module.md#synopsis)
- [Requirements](edit_boot_option_module.md#requirements)
- [Parameters](edit_boot_option_module.md#parameters)
- [Notes](edit_boot_option_module.md#notes)
- [Examples](edit_boot_option_module.md#examples)
- [Return Values](edit_boot_option_module.md#return-values)

## [Synopsis](edit_boot_option_module.md#id1)

- Set BIOS boot options on Inspur server.

## [Requirements](edit_boot_option_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](edit_boot_option_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **device**  string | Boot device.  **Choices:**   - `"none"` - `"HDD"` - `"PXE"` - `"CD"` - `"BIOSSETUP"` |
| **effective**  string | Effective, once or continuous.  **Choices:**   - `"Once"` - `"Continuous"` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **mode**  string | Boot type.  **Choices:**   - `"Legacy"` - `"UEFI"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](edit_boot_option_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](edit_boot_option_module.md#id5)

```yaml+jinja
- name: Boot test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set bios boot option"
    inspur.ispim.edit_boot_option:
      device: "PXE"
      effective: "Once"
      mode: "Legacy"
      provider: "{{ ism }}"
```

## [Return Values](edit_boot_option_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  **Returned:** always |
| **message**  string | Messages returned after module execution.  **Returned:** always |
| **state**  string | Status after module execution.  **Returned:** always |

### Authors

- WangBaoshan (@ispim)

### Collection links

- [Issue Tracker](https://github.com/ispim/inspur.ispim/issues)
- [Repository (Sources)](https://github.com/ispim/inspur.ispim)
