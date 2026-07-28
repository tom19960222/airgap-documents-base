---
collection: ansible
version: "8"
title: "inspur.sm.edit_snmp_trap module – Set snmp trap."
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/sm/edit_snmp_trap_module.html
fetched_at: 2026-07-28T02:38:43+00:00
---
# inspur.sm.edit_snmp_trap module – Set snmp trap.

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
> To use it in a playbook, specify: `inspur.sm.edit_snmp_trap`.

New in inspur.sm 0.1.0

- [Synopsis](edit_snmp_trap_module.md#synopsis)
- [Parameters](edit_snmp_trap_module.md#parameters)
- [Examples](edit_snmp_trap_module.md#examples)
- [Return Values](edit_snmp_trap_module.md#return-values)

## [Synopsis](edit_snmp_trap_module.md#id1)

- Set snmp trap on Inspur server.

## [Parameters](edit_snmp_trap_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_password**  string | Set auth password of V3 trap, password is a string of 8 to 16 alpha-numeric characters.  Required when *auth_protocol* is either `SHA` or `MD5`. |
| **auth_protocol**  string | Choose authentication.  **Choices:**   - `"NONE"` - `"SHA"` - `"MD5"` |
| **community**  string | Community of v1/v2c. |
| **contact**  string | Set contact, can set NULL.  Only the M5 model supports this parameter. |
| **engine_id**  string | Set Engine ID of V3 trap, engine ID is a string of 10 to 48 hex characters, must even, can set NULL. |
| **event_severity**  string | Event Severity.  **Choices:**   - `"all"` - `"warning"` - `"critical"` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **host_id**  string | Host id.  Only the M6 model supports this parameter.  **Choices:**   - `"HostName"` - `"SerialNum"` - `"AssertTag"` |
| **location**  string | Set host Location, can set NULL.  Only the M5 model supports this parameter. |
| **os**  string | Set host OS, can set NULL.  Only the M5 model supports this parameter. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **priv_password**  string | Set privacy password of V3 trap, password is a string of 8 to 16 alpha-numeric characters.  Required when *priv_protocol* is either `DES` or `AES`. |
| **priv_protocol**  string | Choose Privacy.  **Choices:**   - `"NONE"` - `"DES"` - `"AES"` |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **system_id**  string | Set system ID, can set NULL.  Only the M5 model supports this parameter. |
| **system_name**  string | Set system name, can set NULL.  Only the M5 model supports this parameter. |
| **trap_port**  integer | Set SNMP trap Port(1-65535).  Only the M5 model supports this parameter. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **v3username**  string | Set user name of V3 trap. |
| **version**  integer | SNMP trap version.  Only the M6 model supports `0` Settings.  **Choices:**   - `0` - `1` - `2` - `3` |

## [Examples](edit_snmp_trap_module.md#id3)

```yaml+jinja
- name: Trap test
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

  - name: "Set snmp trap v2c"
    inspur.sm.edit_snmp_trap:
      version: 2
      event_severity: "warning"
      inspur: "test"
      system_name: "Inspur"
      provider: "{{ ism }}"

  - name: "Set snmp trap v3"
    inspur.sm.edit_snmp_trap:
      version: 3
      event_severity: "all"
      v3username: "Inspur"
      engine_id: "1234567890"
      auth_protocol: "SHA"
      auth_password: "12345678"
      priv_protocol: "AES"
      priv_password: "123454678"
      trap_port: 162
      provider: "{{ ism }}"
```

## [Return Values](edit_snmp_trap_module.md#id4)

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
