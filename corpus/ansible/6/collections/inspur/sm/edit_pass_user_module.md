---
collection: ansible
version: "6"
title: "inspur.sm.edit_pass_user module – Change user password."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/edit_pass_user_module.html
fetched_at: 2026-07-27T17:53:18+00:00
---
# inspur.sm.edit_pass_user module – Change user password.

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
> To use it in a playbook, specify: `inspur.sm.edit_pass_user`.

New in inspur.sm 0.1.0

- [DEPRECATED](edit_pass_user_module.md#deprecated)
- [Synopsis](edit_pass_user_module.md#synopsis)
- [Parameters](edit_pass_user_module.md#parameters)
- [Examples](edit_pass_user_module.md#examples)
- [Return Values](edit_pass_user_module.md#return-values)
- [Status](edit_pass_user_module.md#status)

## [DEPRECATED](edit_pass_user_module.md#id1)

Removed in:
:   version 3.0.0

Why:
:   Merge functions into the [inspur.sm.user](user_module.md#ansible-collections-inspur-sm-user-module) module.

Alternative:
:   Use [inspur.sm.user](user_module.md#ansible-collections-inspur-sm-user-module) instead.

## [Synopsis](edit_pass_user_module.md#id2)

- Change user password on Inspur server.

## [Parameters](edit_pass_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **uname**  string / required | User name. |
| **upass**  string / required | User password. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](edit_pass_user_module.md#id4)

```yaml+jinja
- name: Edit user password test
  hosts: ism
  no_log: true
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Change user password"
    inspur.sm.edit_pass_user:
      uname: "wbs"
      upass: my_password
      provider: "{{ ism }}"
```

## [Return Values](edit_pass_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  Returned: always |
| **message**  string | Messages returned after module execution.  Returned: always |
| **state**  string | Status after module execution.  Returned: always |

## [Status](edit_pass_user_module.md#id6)

- This module will be removed in version 3.0.0.
  *[deprecated]*
- For more information see [DEPRECATED](edit_pass_user_module.md#deprecated).

### Authors

- WangBaoshan (@ISIB-group)

### Collection links

[Issue Tracker](https://github.com/ISIB-Group/inspur.sm/issues)
[Repository (Sources)](https://github.com/ISIB-Group/inspur.sm)
