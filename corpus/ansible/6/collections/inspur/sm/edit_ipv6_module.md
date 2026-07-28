---
collection: ansible
version: "6"
title: "inspur.sm.edit_ipv6 module – Set ipv6 information."
source_url: https://docs.ansible.com/projects/ansible/6/collections/inspur/sm/edit_ipv6_module.html
fetched_at: 2026-07-27T17:53:09+00:00
---
# inspur.sm.edit_ipv6 module – Set ipv6 information.

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
> To use it in a playbook, specify: `inspur.sm.edit_ipv6`.

New in inspur.sm 0.1.0

- [Synopsis](edit_ipv6_module.md#synopsis)
- [Parameters](edit_ipv6_module.md#parameters)
- [Examples](edit_ipv6_module.md#examples)
- [Return Values](edit_ipv6_module.md#return-values)

## [Synopsis](edit_ipv6_module.md#id1)

- Set ipv6 information on Inspur server.

## [Parameters](edit_ipv6_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **interface_name**  string / required | Set interface_name.  Choices:   - `"eth0"` - `"eth1"` - `"bond0"` |
| **ipv6_address**  string | If DHCP is disabled, specify a static IPv6 address to be configured for the selected interface.  Required when *ipv6_dhcp_enable=static*. |
| **ipv6_dhcp_enable**  string | Enable ‘Enable DHCP’ to dynamically configure IPv6 address using Dynamic Host Configuration Protocol (DHCP).  Choices:   - `"dhcp"` - `"static"` |
| **ipv6_gateway**  string | If DHCP is disabled, specify a static Default Gateway to be configured for the selected interface.  Required when *ipv6_dhcp_enable=static*. |
| **ipv6_index**  integer | Ipv6 index(0-15).  Required when *ipv6_dhcp_enable=static*. |
| **ipv6_prefix**  integer | The subnet prefix length for the IPv6 settings(0-128).  Required when *ipv6_dhcp_enable=static*. |
| **ipv6_status**  string | Enable or disable IPV6.  Choices:   - `"enable"` - `"disable"` |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **provider**  dictionary | A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |

## [Examples](edit_ipv6_module.md#id3)

```yaml+jinja
- name: Ipv6 test
  hosts: ism
  connection: local
  gather_facts: no
  vars:
    ism:
      host: "{{ ansible_ssh_host }}"
      username: "{{ username }}"
      password: "{{ password }}"

  tasks:

  - name: "Set ipv6 information"
    inspur.sm.edit_ipv6:
      interface_name: "eth0"
      ipv6_status: "disable"
      provider: "{{ ism }}"

  - name: "Set ipv6 information"
    inspur.sm.edit_ipv6:
      interface_name: "eth0"
      ipv6_status: "enable"
      ipv6_dhcp_enable: "dhcp"
      provider: "{{ ism }}"

  - name: "Set ipv6 information"
    inspur.sm.edit_ipv6:
      interface_name: "eth0"
      ipv6_status: "enable"
      ipv6_dhcp_enable: "static"
      ipv6_address: "::ffff:100:2:36:10"
      ipv6_index: 12
      ipv6_prefix: 16
      ipv6_gateway: "::"
      provider: "{{ ism }}"
```

## [Return Values](edit_ipv6_module.md#id4)

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
