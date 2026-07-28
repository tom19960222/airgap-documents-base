---
collection: ansible
version: "6"
title: "inspur.sm.edit_log_setting module – Set bmc system and audit log setting."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/edit_log_setting_module.html
fetched_at: 2026-07-27T17:53:12+00:00
---
# inspur.sm.edit_log_setting module – Set bmc system and audit log setting.

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
> To use it in a playbook, specify: `inspur.sm.edit_log_setting`.

New in inspur.sm 0.1.0

- [Synopsis](edit_log_setting_module.md#synopsis)
- [Parameters](edit_log_setting_module.md#parameters)
- [Examples](edit_log_setting_module.md#examples)
- [Return Values](edit_log_setting_module.md#return-values)

## [Synopsis](edit_log_setting_module.md#id1)

- Set bmc system and audit log setting on Inspur server.

## [Parameters](edit_log_setting_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **audit_status**  string | Audit Log Status.  Choices:   - `"enable"` - `"disable"` |
| **audit_type**  string | Audit log type.  Choices:   - `"local"` - `"remote"` - `"both"` |
| **file_size**  integer | File Size(3-65535bytes), set when type is local(default 30000). |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **protocol_type**  string | Protocol Type, set when type is remote.  Choices:   - `"UDP"` - `"TCP"` |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **rotate_count**  integer | Rotate Count, set when type is local, 0-delete old files(default), 1-bak old files.  Choices:   - `0` - `1` |
| **server_addr**  string | Server Address, set when type is remote. |
| **server_port**  integer | Server Port(0-65535), set when type is remote. |
| **status**  string | System Log Status.  Choices:   - `"enable"` - `"disable"` |
| **type**  string | System log type.  Choices:   - `"local"` - `"remote"` - `"both"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](edit_log_setting_module.md#id3)

```yaml+jinja
- name: Edit log setting test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Edit bmc system log setting"
    inspur.sm.edit_log_setting:
      status: "enable"
      type: "both"
      provider: "{{ ism }}"

  - name: "Edit bmc audit log setting"
    inspur.sm.edit_log_setting:
      audit_status: "enable"
      audit_type: "remote"
      server_addr: "100.2.126.11"
      server_port: "514"
      provider: "{{ ism }}"
```

## [Return Values](edit_log_setting_module.md#id4)

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
