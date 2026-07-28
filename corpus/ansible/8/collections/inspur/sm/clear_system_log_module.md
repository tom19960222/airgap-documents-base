---
collection: ansible
version: "8"
title: "inspur.sm.clear_system_log module – Clear BMC system log."
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/sm/clear_system_log_module.html
fetched_at: 2026-07-28T02:38:01+00:00
---
# inspur.sm.clear_system_log module – Clear BMC system log.

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
> To use it in a playbook, specify: `inspur.sm.clear_system_log`.

New in inspur.sm 0.1.0

- [Synopsis](clear_system_log_module.md#synopsis)
- [Parameters](clear_system_log_module.md#parameters)
- [Examples](clear_system_log_module.md#examples)
- [Return Values](clear_system_log_module.md#return-values)

## [Synopsis](clear_system_log_module.md#id1)

- Clear BMC system log on Inspur server.

## [Parameters](clear_system_log_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **level**  string | Log level.  **Choices:**   - `"alert"` ← (default) - `"critical"` - `"error"` - `"notice"` - `"warning"` - `"debug"` - `"emergency"` - `"info"` - `"all"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](clear_system_log_module.md#id3)

```yaml+jinja
- name: Clear BMC system log test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Clear BMC system log"
    inspur.sm.clear_system_log:
      level: "alert"
      provider: "{{ ism }}"

  - name: "Clear BMC system log"
    inspur.sm.clear_system_log:
      level: "all"
      provider: "{{ ism }}"
```

## [Return Values](clear_system_log_module.md#id4)

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
