---
collection: ansible
version: "6"
title: "inspur.sm.edit_restore_factory_default module – Set preserver config."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/edit_restore_factory_default_module.html
fetched_at: 2026-07-27T17:53:24+00:00
---
# inspur.sm.edit_restore_factory_default module – Set preserver config.

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
> To use it in a playbook, specify: `inspur.sm.edit_restore_factory_default`.

New in inspur.sm 0.1.0

- [Synopsis](edit_restore_factory_default_module.md#synopsis)
- [Parameters](edit_restore_factory_default_module.md#parameters)
- [Examples](edit_restore_factory_default_module.md#examples)
- [Return Values](edit_restore_factory_default_module.md#return-values)

## [Synopsis](edit_restore_factory_default_module.md#id1)

- Set preserver config on Inspur server.

## [Parameters](edit_restore_factory_default_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **mode**  string / required | Restore factory defaults mode.  Choices:   - `"all"` - `"none"` - `"manual"` |
| **override**  list / elements=string | Configuration items that need to be retained.  Required when *mode=manual*.  Choices:   - `"authentication"` - `"dcmi"` - `"fru"` - `"hostname"` - `"ipmi"` - `"kvm"` - `"network"` - `"ntp"` - `"pef"` - `"sdr"` - `"sel"` - `"smtp"` - `"snmp"` - `"sol"` - `"ssh"` - `"syslog"` - `"user"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](edit_restore_factory_default_module.md#id3)

```yaml+jinja
- name: Restore default test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set restore default auto"
    inspur.sm.edit_restore_factory_default:
      mode: "all"
      provider: "{{ ism }}"

  - name: "Set restore default manual"
    inspur.sm.edit_restore_factory_default:
      mode: "manual"
      override:
        - fru
        - ntp
        - network
        - user
      provider: "{{ ism }}"
```

## [Return Values](edit_restore_factory_default_module.md#id4)

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
