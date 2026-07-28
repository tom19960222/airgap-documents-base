---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_l3_interface module – (deprecated, removed after 2022-06-01) Manage L3 interfaces on VyOS network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_l3_interface_module.html
fetched_at: 2026-07-28T00:23:19+00:00
---
# vyos.vyos.vyos_l3_interface module – (deprecated, removed after 2022-06-01) Manage L3 interfaces on VyOS network devices

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/vyos/vyos) (version 3.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_l3_interface`.

New in vyos.vyos 1.0.0

- [DEPRECATED](vyos_l3_interface_module.md#deprecated)
- [Synopsis](vyos_l3_interface_module.md#synopsis)
- [Parameters](vyos_l3_interface_module.md#parameters)
- [Notes](vyos_l3_interface_module.md#notes)
- [Examples](vyos_l3_interface_module.md#examples)
- [Return Values](vyos_l3_interface_module.md#return-values)
- [Status](vyos_l3_interface_module.md#status)

## [DEPRECATED](vyos_l3_interface_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality.

Alternative:
:   vyos_l3_interfaces

## [Synopsis](vyos_l3_interface_module.md#id2)

- This module provides declarative management of L3 interfaces on VyOS network devices.

## [Parameters](vyos_l3_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of L3 interfaces definitions |
| **ipv4**  string | IPv4 of the L3 interface. |
| **ipv6**  string | IPv6 of the L3 interface. |
| **name**  string / required | Name of the L3 interface. |
| **state**  string | State of the L3 interface configuration.  Choices:   - `"present"` - `"absent"` |
| **ipv4**  string | IPv4 of the L3 interface. |
| **ipv6**  string | IPv6 of the L3 interface. |
| **name**  string | Name of the L3 interface. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **state**  string | State of the L3 interface configuration.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](vyos_l3_interface_module.md#id4)

> **Note:**
>
> - Tested against VYOS 1.1.7
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_l3_interface_module.md#id5)

```yaml+jinja
- name: Set eth0 IPv4 address
  vyos.vyos.vyos_l3_interface:
    name: eth0
    ipv4: 192.168.0.1/24

- name: Remove eth0 IPv4 address
  vyos.vyos.vyos_l3_interface:
    name: eth0
    state: absent

- name: Set IP addresses on aggregate
  vyos.vyos.vyos_l3_interface:
    aggregate:
    - {name: eth1, ipv4: 192.168.2.10/24}
    - {name: eth2, ipv4: 192.168.3.10/24, ipv6: "fd5d:12c9:2201:1::1/64"}

- name: Remove IP addresses on aggregate
  vyos.vyos.vyos_l3_interface:
    aggregate:
    - {name: eth1, ipv4: 192.168.2.10/24}
    - {name: eth2, ipv4: 192.168.3.10/24, ipv6: "fd5d:12c9:2201:1::1/64"}
    state: absent
```

## [Return Values](vyos_l3_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["set interfaces ethernet eth0 address '192.168.0.1/24'"]` |

## [Status](vyos_l3_interface_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](vyos_l3_interface_module.md#deprecated).

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
