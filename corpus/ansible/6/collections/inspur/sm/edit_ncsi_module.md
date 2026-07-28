---
collection: ansible
version: "6"
title: "inspur.sm.edit_ncsi module – Set ncsi information."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/edit_ncsi_module.html
fetched_at: 2026-07-27T17:53:14+00:00
---
# inspur.sm.edit_ncsi module – Set ncsi information.

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
> To use it in a playbook, specify: `inspur.sm.edit_ncsi`.

New in inspur.sm 0.1.0

- [Synopsis](edit_ncsi_module.md#synopsis)
- [Parameters](edit_ncsi_module.md#parameters)
- [Examples](edit_ncsi_module.md#examples)
- [Return Values](edit_ncsi_module.md#return-values)

## [Synopsis](edit_ncsi_module.md#id1)

- Set ncsi information on Inspur server.

## [Parameters](edit_ncsi_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **channel_number**  integer | Channel number.  Choices:   - `0` - `1` - `2` - `3` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **interface_name**  string | Interface name, for example eth0.  Only the M5 model supports this parameter. |
| **mode**  string | NCSI mode, auto-Auto Failover, manual-Manual Switch.  Only M6 model supports `Disable` Settings  Choices:   - `"auto"` - `"manual"` - `"Disable"` |
| **nic_type**  string | Nic type.  Only NF3280A6 and NF3180A6 model supports `Disable` Settings, but not support `PHY` Settings.  M6 model only support `OCP`,`PCIE` settings.  Choices:   - `"PHY"` - `"OCP"` - `"PCIE"` - `"auto"` - `"Disable"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](edit_ncsi_module.md#id3)

```yaml+jinja
- name: NCSI test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set ncsi information"
    inspur.sm.edit_ncsi:
      mode: "manual"
      nic_type: "PCIE"
      interface_name: "eth0"
      channel_number: 1
      provider: "{{ ism }}"
```

## [Return Values](edit_ncsi_module.md#id4)

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
