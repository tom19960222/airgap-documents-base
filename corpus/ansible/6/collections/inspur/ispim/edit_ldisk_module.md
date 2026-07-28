---
collection: ansible
version: "6"
title: "inspur.ispim.edit_ldisk module – Set logical disk"
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/ispim/edit_ldisk_module.html
fetched_at: 2026-07-27T17:51:37+00:00
---
# inspur.ispim.edit_ldisk module – Set logical disk

> **Note:**
>
> This module is part of the [inspur.ispim collection](https://galaxy.ansible.com/inspur/ispim) (version 1.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install inspur.ispim`.
> You need further requirements to be able to use this module,
> see [Requirements](edit_ldisk_module.md#ansible-collections-inspur-ispim-edit-ldisk-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.edit_ldisk`.

New in inspur.ispim 1.0.0

- [Synopsis](edit_ldisk_module.md#synopsis)
- [Requirements](edit_ldisk_module.md#requirements)
- [Parameters](edit_ldisk_module.md#parameters)
- [Notes](edit_ldisk_module.md#notes)
- [Examples](edit_ldisk_module.md#examples)
- [Return Values](edit_ldisk_module.md#return-values)

## [Synopsis](edit_ldisk_module.md#id1)

- Set logical disk on Inspur server.

## [Requirements](edit_ldisk_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](edit_ldisk_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ctrl_id**  integer | Raid controller ID.  Required when *Info=None*. |
| **duration**  integer | duration range is 1-255,physical drive under PMC raid controller.  Required when *option=LOC*.  Only the M6 model supports this parameter. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **info**  string | Show controller and ldisk info.  Choices:   - `"show"` |
| **ldisk_id**  integer | Logical disk ID.  Required when *Info=None*. |
| **option**  string | Set operation options fo logical disk,  LOC is Locate Logical Drive,STL is Stop Locate LogicalDrive,  FI is Fast Initialization,SFI is Slow/Full Initialization,  SI is Stop Initialization,DEL is Delete LogicalDrive.  Required when *Info=None*.  Choices:   - `"LOC"` - `"STL"` - `"FI"` - `"SFI"` - `"SI"` - `"DEL"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](edit_ldisk_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](edit_ldisk_module.md#id5)

```yaml+jinja
- name: Edit ldisk test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Show ldisk information"
    inspur.ispim.edit_ldisk:
      info: "show"
      provider: "{{ ism }}"

  - name: "Edit ldisk"
    inspur.ispim.edit_ldisk:
      ctrl_id: 0
      ldisk_id: 1
      option: "LOC"
      provider: "{{ ism }}"
```

## [Return Values](edit_ldisk_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  Returned: always |
| **message**  string | Messages returned after module execution.  Returned: always |
| **state**  string | Status after module execution.  Returned: always |

### Authors

- WangBaoshan (@ispim)

### Collection links

[Issue Tracker](https://github.com/ispim/inspur.ispim/issues)
[Repository (Sources)](https://github.com/ispim/inspur.ispim)
