---
collection: ansible
version: "8"
title: "inspur.ispim.edit_m6_log_setting module – Set bmc system and audit log setting"
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/ispim/edit_m6_log_setting_module.html
fetched_at: 2026-07-28T02:36:43+00:00
---
# inspur.ispim.edit_m6_log_setting module – Set bmc system and audit log setting

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
> see [Requirements](edit_m6_log_setting_module.md#ansible-collections-inspur-ispim-edit-m6-log-setting-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.edit_m6_log_setting`.

New in inspur.ispim 1.3.0

- [Synopsis](edit_m6_log_setting_module.md#synopsis)
- [Requirements](edit_m6_log_setting_module.md#requirements)
- [Parameters](edit_m6_log_setting_module.md#parameters)
- [Notes](edit_m6_log_setting_module.md#notes)
- [Examples](edit_m6_log_setting_module.md#examples)
- [Return Values](edit_m6_log_setting_module.md#return-values)

## [Synopsis](edit_m6_log_setting_module.md#id1)

- Set bmc system and audit log setting on Inspur server.
- Only the M6 models support this feature.

## [Requirements](edit_m6_log_setting_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](edit_m6_log_setting_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **host_tag**  string | System log host tag,set when *status=enable*.  **Choices:**   - `"HostName"` - `"SerialNum"` - `"AssertTag"` |
| **level**  string | Events Level,set when *status=enable*.  **Choices:**   - `"Critical"` - `"Warning"` - `"Info"` |
| **log_type**  string | Remote Log Type,set when server_id is not none.  **Choices:**   - `"idl"` - `"audit"` - `"both"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **protocol_type**  string | Protocol Type,set when *status=enable*.  **Choices:**   - `"UDP"` - `"TCP"` |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **server_addr**  string | Server Address,set when server_id is not none. |
| **server_id**  integer | Syslog Server ID,set when *status=enable*.  **Choices:**   - `0` - `1` - `2` - `3` |
| **server_port**  integer | Server Address,set when server_id is not none. |
| **status**  string | System Log Status.  **Choices:**   - `"enable"` - `"disable"` |
| **test**  boolean | Test remote log settings,set when server_id is not none.  **Choices:**   - `false` ← (default) - `true` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](edit_m6_log_setting_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](edit_m6_log_setting_module.md#id5)

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
    inspur.ispim.edit_m6_log_setting:
      status: "disable"
      provider: "{{ ism }}"

  - name: "Edit bmc audit log setting"
    inspur.ispim.edit_m6_log_setting:
      status: "enable"
      host_tag: "HostName"
      level: "Info"
      protocol_type: "TCP"
      server_id: 0
      server_addr: "100.2.126.11"
      server_port: 514
      log_type: "both"
      provider: "{{ ism }}"

  - name: "test bmc audit log"
    inspur.ispim.edit_m6_log_setting:
      server_id: 0
      test: True
      provider: "{{ ism }}"
```

## [Return Values](edit_m6_log_setting_module.md#id6)

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
