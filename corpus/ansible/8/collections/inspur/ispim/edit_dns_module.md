---
collection: ansible
version: "8"
title: "inspur.ispim.edit_dns module – Set dns information"
source_url: https://docs.ansible.com/projects/ansible/8/collections/inspur/ispim/edit_dns_module.html
fetched_at: 2026-07-28T02:36:36+00:00
---
# inspur.ispim.edit_dns module – Set dns information

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
> see [Requirements](edit_dns_module.md#ansible-collections-inspur-ispim-edit-dns-module-requirements) for details.
>
> To use it in a playbook, specify: `inspur.ispim.edit_dns`.

New in inspur.ispim 1.0.0

- [Synopsis](edit_dns_module.md#synopsis)
- [Requirements](edit_dns_module.md#requirements)
- [Parameters](edit_dns_module.md#parameters)
- [Notes](edit_dns_module.md#notes)
- [Examples](edit_dns_module.md#examples)
- [Return Values](edit_dns_module.md#return-values)

## [Synopsis](edit_dns_module.md#id1)

- Set dns information on Inspur server.

## [Requirements](edit_dns_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python 3.7+
- inspursmsdk

## [Parameters](edit_dns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dns_iface**  string | DNS Interface,input like ‘eth0’, ‘eth1’, ‘bond0’.  Required when *dns_manual=auto*. |
| **dns_manual**  string | DNS Settings.  **Choices:**   - `"manual"` - `"auto"` |
| **dns_priority**  string | IP Priority.  Required when *dns_manual=auto*.  **Choices:**   - `"4"` - `"6"` |
| **dns_server1**  string | DNS Server1 IPv4 or IPv6 address.  Required when *dns_manual=manual*. |
| **dns_server2**  string | DNS Server2 IPv4 or IPv6 address.  Required when *dns_manual=manual*. |
| **dns_server3**  string | DNS Server3 IPv4 or IPv6 address.  Required when *dns_manual=manual*. |
| **dns_status**  string | DNS status.  **Choices:**   - `"enable"` - `"disable"` |
| **domain_iface**  string | Network Interface,input like ‘eth0_v4’, ‘eth0_v6’, ‘eth1_v4’, ‘eth1_v6’, ‘bond0_v4’, ‘bond0_v6’.  Required when *domain_manual=auto*. |
| **domain_manual**  string | Domain Settings.  **Choices:**   - `"manual"` - `"auto"` |
| **domain_name**  string | Domain Name.  Required when *domain_manual=manual*. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **host_cfg**  string | Host Settings.  **Choices:**   - `"manual"` - `"auto"` |
| **host_name**  string | Host Name.  Required when *host_cfg=manual*. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **register_status1**  string | BMC register status 1.  Only the M6 model supports this parameter.  **Choices:**   - `"enable"` - `"disable"` |
| **register_status2**  string | BMC register status 2.  Only the M6 model supports this parameter.  **Choices:**   - `"enable"` - `"disable"` |
| **registration_method1**  string | Registration method 1.  Only the M6 model supports this parameter.  Required when *register_status1=enable*.  **Choices:**   - `"nsupdate"` - `"dhcp"` - `"hostname"` |
| **registration_method2**  string | Registration method 2.  Only the M6 model supports this parameter.  Required when *register_status2=enable*.  **Choices:**   - `"nsupdate"` - `"dhcp"` - `"hostname"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Notes](edit_dns_module.md#id4)

> **Note:**
>
> - Does not support `check_mode`.

## [Examples](edit_dns_module.md#id5)

```yaml+jinja
- name: DNS test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set dns information"
    inspur.ispim.edit_dns:
      dns_status: "disable"
      provider: "{{ ism }}"

  - name: "Set dns information"
    inspur.ispim.edit_dns:
      dns_status: "enable"
      host_cfg: "manual"
      host_name: "123456789"
      domain_manual: "auto"
      domain_iface: "eth0_v4"
      dns_manual: "manual"
      dns_server1: "100.2.2.2"
      dns_server2: "100.2.2.3"
      dns_server3: "100.2.2.4"
      provider: "{{ ism }}"

  - name: "Set dns information"
    inspur.ispim.edit_dns:
      dns_status: "enable"
      host_cfg: "manual"
      host_name: "123456789"
      domain_manual: "manual"
      domain_name: "inspur.com"
      dns_manual: "auto"
      dns_iface: "eth0"
      dns_priority: "4"
      provider: "{{ ism }}"
```

## [Return Values](edit_dns_module.md#id6)

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
