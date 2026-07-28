---
collection: ansible
version: "6"
title: "inspur.ispim.user_group module – Manage user group"
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/ispim/user_group_module.html
fetched_at: 2026-07-27T17:52:32+00:00
---
# inspur.ispim.user_group module – Manage user group

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
> see [Requirements](user_group_module.md#ansible-collections-inspur-ispim-user-group-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.user_group`.

New in inspur.ispim 1.0.0

- [Synopsis](user_group_module.md#synopsis)
- [Requirements](user_group_module.md#requirements)
- [Parameters](user_group_module.md#parameters)
- [Notes](user_group_module.md#notes)
- [Examples](user_group_module.md#examples)
- [Return Values](user_group_module.md#return-values)

## [Synopsis](user_group_module.md#id1)

- Manage user group on Inspur server.

## [Requirements](user_group_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](user_group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **debug**  string | Debug diagnose privilege.  Required when *state=present*.  Only the M6 model supports this parameter.  Choices:   - `"enable"` - `"disable"` |
| **general**  string | General configuration privilege.  Required when *state=present*.  Only the M6 model supports this parameter.  Choices:   - `"enable"` - `"disable"` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **kvm**  string | Remote KVM configuration privilege.  Required when *state=present*.  Only the M6 model supports this parameter.  Choices:   - `"enable"` - `"disable"` |
| **media**  string | Remote media configuration privilege.  Required when *state=present*.  Only the M6 model supports this parameter.  Choices:   - `"enable"` - `"disable"` |
| **name**  string / required | Group name.  The range of group name for M6 model is OEM1,OEM2,OEM3,OEM4. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **power**  string | Power control privilege.  Required when *state=present*.  Only the M6 model supports this parameter.  Choices:   - `"enable"` - `"disable"` |
| **pri**  string | Group privilege.  Required when *state=present*.  Only the M5 model supports this parameter.  Choices:   - `"administrator"` - `"operator"` - `"user"` - `"oem"` - `"none"` |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **security**  string | Security configuration privilege.  Required when *state=present*.  Only the M6 model supports this parameter.  Choices:   - `"enable"` - `"disable"` |
| **self**  string | Itself configuration privilege.  Required when *state=present*.  Only the M6 model supports this parameter.  Choices:   - `"enable"` - `"disable"` |
| **state**  string | Whether the user group should exist or not, taking action if the state is different from what is stated.  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](user_group_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](user_group_module.md#id5)

```yaml+jinja
- name: User group test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Add user group"
    inspur.ispim.user_group:
      state: "present"
      name: "test"
      pri: "administrator"
      provider: "{{ ism }}"

  - name: "Set user group"
    inspur.ispim.user_group:
      state: "present"
      name: "test"
      pri: "user"
      provider: "{{ ism }}"

  - name: "Set m6 user group"
    inspur.ispim.user_group:
      state: "present"
      name: "OEM1"
      general: "enable"
      kvm: "enable"
      provider: "{{ ism }}"

  - name: "Delete user group"
    inspur.ispim.user_group:
      state: "absent"
      name: "test"
      provider: "{{ ism }}"
```

## [Return Values](user_group_module.md#id6)

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
