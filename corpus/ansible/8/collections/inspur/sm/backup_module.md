---
collection: ansible
version: "8"
title: "inspur.sm.backup module – Backup server settings."
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/sm/backup_module.html
fetched_at: 2026-07-28T02:37:55+00:00
---
# inspur.sm.backup module – Backup server settings.

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
> To use it in a playbook, specify: `inspur.sm.backup`.

New in inspur.sm 0.1.0

- [Synopsis](backup_module.md#synopsis)
- [Parameters](backup_module.md#parameters)
- [Examples](backup_module.md#examples)
- [Return Values](backup_module.md#return-values)

## [Synopsis](backup_module.md#id1)

- Backup server settings on Inspur server.

## [Parameters](backup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bak_file**  string / required | Backup file or bak folder. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **item**  string / required | Export item.  The values for M5 modules are ‘all’, ‘network’, ‘service’, ‘ntp’, ‘snmptrap’, ‘dns’, ‘smtp’, ‘ad’, ‘ldap’, ‘user’,’bios’.  The values for M6 modules are ‘all’, ‘network’, ‘service’, ‘ntp’, ‘snmptrap’, ‘kvm’, ‘ipmi’, ‘authentication’, ‘syslog’.  **Choices:**   - `"all"` - `"network"` - `"service"` - `"ntp"` - `"snmptrap"` - `"dns"` - `"smtp"` - `"ad"` - `"ldap"` - `"user"` - `"bios"` - `"kvm"` - `"ipmi"` - `"authentication"` - `"syslog"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](backup_module.md#id3)

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
    inspur.sm.backup:
      bak_file: "/home/wbs/"
      item: "all"
      provider: "{{ ism }}"
```

## [Return Values](backup_module.md#id4)

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
