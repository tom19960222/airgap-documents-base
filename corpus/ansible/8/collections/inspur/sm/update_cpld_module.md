---
collection: ansible
version: "8"
title: "inspur.sm.update_cpld module – Update CPLD."
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/sm/update_cpld_module.html
fetched_at: 2026-07-28T02:39:22+00:00
---
# inspur.sm.update_cpld module – Update CPLD.

> **Note:**
>
> This module is part of the [inspur.sm collection](https://galaxy.ansible.com/ui/repo/published/inspur/sm/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install inspur.sm`.
>
> To use it in a playbook, specify: `inspur.sm.update_cpld`.

New in inspur.sm 0.1.0

- [Synopsis](update_cpld_module.md#synopsis)
- [Parameters](update_cpld_module.md#parameters)
- [Examples](update_cpld_module.md#examples)
- [Return Values](update_cpld_module.md#return-values)

## [Synopsis](update_cpld_module.md#id1)

- Update CPLD on Inspur server.

## [Parameters](update_cpld_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **file_url**  string | CPLD image file path.  Required when *list=False*. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **id**  integer | CPLD id.  Required when *list=False*.  Only the M5 model supports this parameter. |
| **list**  boolean | Get cpld list.  Only the M5 model supports this parameter.  **Choices:**   - `false` ← (default) - `true` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](update_cpld_module.md#id3)

```yaml+jinja
- name: CPLD test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Get cpld list"
    inspur.sm.update_cpld:
      list: True
      provider: "{{ ism }}"

  - name: "Update cpld"
    update_cpld:
      id: 1
      file_url: "home/wbs/raw.bin"
      provider: "{{ ism }}"
```

## [Return Values](update_cpld_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  **Returned:** always |
| **message**  string | Messages returned after module execution.  **Returned:** always |
| **state**  string | Status after module execution.  **Returned:** always |

### Authors

- WangBaoshan (@ISIB-group)

### Collection links

- [Issue Tracker](https://github.com/ISIB-Group/inspur.sm/issues)
- [Repository (Sources)](https://github.com/ISIB-Group/inspur.sm)
