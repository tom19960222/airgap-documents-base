---
collection: ansible
version: "6"
title: "inspur.sm.audit_log_info module – Get BMC audit log information."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/audit_log_info_module.html
fetched_at: 2026-07-27T17:52:43+00:00
---
# inspur.sm.audit_log_info module – Get BMC audit log information.

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
> To use it in a playbook, specify: `inspur.sm.audit_log_info`.

New in inspur.sm 0.1.0

- [Synopsis](audit_log_info_module.md#synopsis)
- [Parameters](audit_log_info_module.md#parameters)
- [Examples](audit_log_info_module.md#examples)
- [Return Values](audit_log_info_module.md#return-values)

## [Synopsis](audit_log_info_module.md#id1)

- Get BMC audit log information on Inspur server.

## [Parameters](audit_log_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **audit_file**  string | Store logs to a file. |
| **count**  integer | Get the most recent log of a specified number. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **log_time**  string | Get logs after the specified date, time should be YYYY-MM-DDTHH:MM+HH:MM, like 2019-06-27T12:30+08:00. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](audit_log_info_module.md#id3)

```yaml+jinja
- name: Bmc audit log test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Get bmc audit log information"
    inspur.sm.audit_log_info:
      log_time: "2020-06-01T12:30+08:00"
      provider: "{{ ism }}"

  - name: "Get bmc audit log information"
    inspur.sm.audit_log_info:
      count: 30
      provider: "{{ ism }}"

  - name: "Get bmc audit log information"
    inspur.sm.audit_log_info:
      audit_file: "/home/wbs/wbs.log"
      provider: "{{ ism }}"
```

## [Return Values](audit_log_info_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **changed**  boolean | Check to see if a change was made on the device.  Returned: always |
| **message**  string | Messages returned after module execution.  Returned: always |
| **state**  string | Status after module execution.  Returned: always |

### Authors

- WangBaoshan (@ISIB-group)

### Collection links

[Issue Tracker](https://github.com/ISIB-Group/inspur.sm/issues)
[Repository (Sources)](https://github.com/ISIB-Group/inspur.sm)
