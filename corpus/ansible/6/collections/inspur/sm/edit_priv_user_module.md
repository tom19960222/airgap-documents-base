---
collection: ansible
version: "6"
title: "inspur.sm.edit_priv_user module – Change user privilege."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/edit_priv_user_module.html
fetched_at: 2026-07-27T17:53:22+00:00
---
# inspur.sm.edit_priv_user module – Change user privilege.

> **Note:**
>
> This module is part of the [inspur.sm collection](https://galaxy.ansible.com/inspur/sm) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install inspur.sm`.
>
> To use it in a playbook, specify: `inspur.sm.edit_priv_user`.

New in inspur.sm 0.1.0

- [DEPRECATED](edit_priv_user_module.md#deprecated)
- [Synopsis](edit_priv_user_module.md#synopsis)
- [Parameters](edit_priv_user_module.md#parameters)
- [Examples](edit_priv_user_module.md#examples)
- [Return Values](edit_priv_user_module.md#return-values)
- [Status](edit_priv_user_module.md#status)

## [DEPRECATED](edit_priv_user_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Merge functions into the [inspur.sm.user](user_module.md#ansible-collections-inspur-sm-user-module) module.

Alternative:
:   Use [inspur.sm.user](user_module.md#ansible-collections-inspur-sm-user-module) instead.

## [Synopsis](edit_priv_user_module.md#id2)

- Change user privilege on Inspur server.

## [Parameters](edit_priv_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **priv**  list / elements=string / required | User access, select one or more from None/KVM/VMM/SOL.  Choices:   - `"kvm"` - `"vmm"` - `"sol"` - `"none"` |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **role_id**  string / required | user group, default user group,’Administrator’, ‘Operator’, ‘Commonuser’,’OEM’,’NoAccess’,  use command `user_group_info` can get all group information. |
| **uname**  string / required | User name. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](edit_priv_user_module.md#id4)

```yaml+jinja
- name: Edit user privilege test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Change user privilege"
    inspur.sm.edit_priv_user:
      uname: "wbs"
      role_id: "Administrator"
      priv: "kvm,sol"
      provider: "{{ ism }}"
```

## [Return Values](edit_priv_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  Returned: always |
| **message**  string | Messages returned after module execution.  Returned: always |
| **state**  string | Status after module execution.  Returned: always |

## [Status](edit_priv_user_module.md#id6)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](edit_priv_user_module.md#deprecated).

### Authors

- WangBaoshan (@ISIB-group)

### Collection links

[Issue Tracker](https://github.com/ISIB-Group/inspur.sm/issues)
[Repository (Sources)](https://github.com/ISIB-Group/inspur.sm)
