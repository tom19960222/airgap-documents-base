---
collection: ansible
version: "6"
title: "inspur.ispim.backup module – Backup server settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/ispim/backup_module.html
fetched_at: 2026-07-27T17:51:15+00:00
---
# inspur.ispim.backup module – Backup server settings

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
> see [Requirements](backup_module.md#ansible-collections-inspur-ispim-backup-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.backup`.

New in inspur.ispim 1.0.0

- [Synopsis](backup_module.md#synopsis)
- [Requirements](backup_module.md#requirements)
- [Parameters](backup_module.md#parameters)
- [Notes](backup_module.md#notes)
- [Examples](backup_module.md#examples)
- [Return Values](backup_module.md#return-values)

## [Synopsis](backup_module.md#id1)

- Backup server settings on Inspur server.

## [Requirements](backup_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](backup_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bak_file**  string / required | Backup file or bak folder. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **item**  string / required | Export item.  The values for M5 modules are ‘all’, ‘network’, ‘service’, ‘ntp’, ‘snmptrap’, ‘dns’, ‘smtp’, ‘ad’, ‘ldap’, ‘user’,’bios’.  The values for M6 modules are ‘all’, ‘network’, ‘service’, ‘ntp’, ‘snmptrap’, ‘kvm’, ‘ipmi’, ‘authentication’, ‘syslog’.  Choices:   - `"all"` - `"network"` - `"service"` - `"ntp"` - `"snmptrap"` - `"dns"` - `"smtp"` - `"ad"` - `"ldap"` - `"user"` - `"bios"` - `"kvm"` - `"ipmi"` - `"authentication"` - `"syslog"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](backup_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](backup_module.md#id5)

```yaml+jinja
- name: Backup test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Backup server settings"
    inspur.ispim.backup:
      bak_file: "/home/wbs/"
      item: "all"
      provider: "{{ ism }}"
```

## [Return Values](backup_module.md#id6)

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
