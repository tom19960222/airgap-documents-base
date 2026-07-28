---
collection: ansible
version: "6"
title: "cisco.ios.ios_l2_interface module – (deprecated, removed after 2022-06-01) Manage Layer-2 interface on Cisco IOS devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_l2_interface_module.html
fetched_at: 2026-07-27T16:55:13+00:00
---
# cisco.ios.ios_l2_interface module – (deprecated, removed after 2022-06-01) Manage Layer-2 interface on Cisco IOS devices.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/cisco/ios) (version 3.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_l2_interface`.

New in cisco.ios 1.0.0

- [DEPRECATED](ios_l2_interface_module.md#deprecated)
- [Synopsis](ios_l2_interface_module.md#synopsis)
- [Parameters](ios_l2_interface_module.md#parameters)
- [Notes](ios_l2_interface_module.md#notes)
- [Examples](ios_l2_interface_module.md#examples)
- [Return Values](ios_l2_interface_module.md#return-values)
- [Status](ios_l2_interface_module.md#status)

## [DEPRECATED](ios_l2_interface_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Newer and updated modules released with more functionality in Ansible 2.9

Alternative:
:   ios_l2_interfaces

## [Synopsis](ios_l2_interface_module.md#id2)

- This module provides declarative management of Layer-2 interfaces on Cisco IOS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_l2_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_vlan**  string | Configure given VLAN in access port. If `mode=access`, used as the access VLAN ID. |
| **aggregate**  list / elements=dictionary | List of Layer-2 interface definitions. |
| **access_vlan**  string | Configure given VLAN in access port. If `mode=access`, used as the access VLAN ID. |
| **mode**  string | Mode in which interface needs to be configured.  Choices:   - `"access"` - `"trunk"` |
| **name**  aliases: interface  string | Full name of the interface excluding any logical unit number, i.e. GigabitEthernet0/1. |
| **native_vlan**  string | Native VLAN to be configured in trunk port. If `mode=trunk`, used as the trunk native VLAN ID. |
| **state**  string | Manage the state of the Layer-2 Interface configuration.  Choices:   - `"present"` - `"absent"` - `"unconfigured"` |
| **trunk_allowed_vlans**  string | List of allowed VLANs in a given trunk port. If `mode=trunk`, these are the only VLANs that will be configured on the trunk, i.e. “2-10,15”. |
| **trunk_vlans**  string | List of VLANs to be configured in trunk port. If `mode=trunk`, used as the VLAN range to ADD or REMOVE from the trunk. |
| **mode**  string | Mode in which interface needs to be configured.  Choices:   - `"access"` - `"trunk"` |
| **name**  aliases: interface  string | Full name of the interface excluding any logical unit number, i.e. GigabitEthernet0/1. |
| **native_vlan**  string | Native VLAN to be configured in trunk port. If `mode=trunk`, used as the trunk native VLAN ID. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **state**  string | Manage the state of the Layer-2 Interface configuration.  Choices:   - `"present"` ← (default) - `"absent"` - `"unconfigured"` |
| **trunk_allowed_vlans**  string | List of allowed VLANs in a given trunk port. If `mode=trunk`, these are the only VLANs that will be configured on the trunk, i.e. “2-10,15”. |
| **trunk_vlans**  string | List of VLANs to be configured in trunk port. If `mode=trunk`, used as the VLAN range to ADD or REMOVE from the trunk. |

## [Notes](ios_l2_interface_module.md#id4)

> **Note:**
>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_l2_interface_module.md#id5)

```yaml+jinja
- name: Ensure GigabitEthernet0/5 is in its default l2 interface state
  ios.ios_l2_interface:
    name: GigabitEthernet0/5
    state: unconfigured
- name: Ensure GigabitEthernet0/5 is configured for access vlan 20
  ios.ios_l2_interface:
    name: GigabitEthernet0/5
    mode: access
    access_vlan: 20
- name: Ensure GigabitEthernet0/5 only has vlans 5-10 as trunk vlans
  ios.ios_l2_interface:
    name: GigabitEthernet0/5
    mode: trunk
    native_vlan: 10
    trunk_allowed_vlans: 5-10
- name: Ensure GigabitEthernet0/5 is a trunk port and ensure 2-50 are being tagged
    (doesn't mean others aren't also being tagged)
  ios.ios_l2_interface:
    name: GigabitEthernet0/5
    mode: trunk
    native_vlan: 10
    trunk_vlans: 2-50
- name: Ensure these VLANs are not being tagged on the trunk
  ios.ios_l2_interface:
    name: GigabitEthernet0/5
    mode: trunk
    trunk_vlans: 51-4094
    state: absent
```

## [Return Values](ios_l2_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["interface GigabitEthernet0/5", "switchport access vlan 20"]` |

## [Status](ios_l2_interface_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](ios_l2_interface_module.md#deprecated).

### Authors

- Nathaniel Case (@Qalthos)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
