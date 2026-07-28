---
collection: ansible
version: "6"
title: "inspur.ispim.audit_log_info module – Get BMC audit log information"
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/ispim/audit_log_info_module.html
fetched_at: 2026-07-27T17:51:13+00:00
---
# inspur.ispim.audit_log_info module – Get BMC audit log information

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
> see [Requirements](audit_log_info_module.md#ansible-collections-inspur-ispim-audit-log-info-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.audit_log_info`.

New in inspur.ispim 1.0.0

- [Synopsis](audit_log_info_module.md#synopsis)
- [Requirements](audit_log_info_module.md#requirements)
- [Parameters](audit_log_info_module.md#parameters)
- [Notes](audit_log_info_module.md#notes)
- [Examples](audit_log_info_module.md#examples)
- [Return Values](audit_log_info_module.md#return-values)

## [Synopsis](audit_log_info_module.md#id1)

- Get BMC audit log information on Inspur server.

## [Requirements](audit_log_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](audit_log_info_module.md#id3)

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

## [Notes](audit_log_info_module.md#id4)

> **Note:**
>
> - Supports `check_mode`.

## [Examples](audit_log_info_module.md#id5)

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
    inspur.ispim.audit_log_info:
      log_time: "2020-06-01T12:30+08:00"
      provider: "{{ ism }}"

  - name: "Get bmc audit log information"
    inspur.ispim.audit_log_info:
      count: 30
      provider: "{{ ism }}"

  - name: "Get bmc audit log information"
    inspur.ispim.audit_log_info:
      audit_file: "/home/wbs/wbs.log"
      provider: "{{ ism }}"
```

## [Return Values](audit_log_info_module.md#id6)

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
