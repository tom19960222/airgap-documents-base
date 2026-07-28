---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_interface module – (deprecated, removed after 2022-06-01) Manage Interface on Cisco IOS XR network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_interface_module.html
fetched_at: 2026-07-27T16:55:43+00:00
---
# cisco.iosxr.iosxr_interface module – (deprecated, removed after 2022-06-01) Manage Interface on Cisco IOS XR network devices

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/cisco/iosxr) (version 3.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
> You need further requirements to be able to use this module,
> see [Requirements](iosxr_interface_module.md#ansible-collections-cisco-iosxr-iosxr-interface-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_interface`.

New in cisco.iosxr 1.0.0

- [DEPRECATED](iosxr_interface_module.md#deprecated)
- [Synopsis](iosxr_interface_module.md#synopsis)
- [Requirements](iosxr_interface_module.md#requirements)
- [Parameters](iosxr_interface_module.md#parameters)
- [Notes](iosxr_interface_module.md#notes)
- [Examples](iosxr_interface_module.md#examples)
- [Return Values](iosxr_interface_module.md#return-values)
- [Status](iosxr_interface_module.md#status)

## [DEPRECATED](iosxr_interface_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Newer and updated modules released with more functionality in Ansible 2.9

Alternative:
:   iosxr_interfaces

## [Synopsis](iosxr_interface_module.md#id2)

- This module provides declarative management of Interfaces on Cisco IOS XR network devices.

## [Requirements](iosxr_interface_module.md#id3)

The below requirements are needed on the host that executes this module.

- ncclient >= 0.5.3 when using netconf
- lxml >= 4.1.1 when using netconf

## [Parameters](iosxr_interface_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **active**  string | Whether the interface is `active` or `preconfigured`. Preconfiguration allows you to configure modular services cards before they are inserted into the router. When the cards are inserted, they are instantly configured. Active cards are the ones already inserted.  Choices:   - `"active"` ← (default) - `"preconfigure"` |
| **aggregate**  list / elements=dictionary | List of interfaces definition |
| **active**  string | Whether the interface is `active` or `preconfigured`. Preconfiguration allows you to configure modular services cards before they are inserted into the router. When the cards are inserted, they are instantly configured. Active cards are the ones already inserted.  Choices:   - `"active"` - `"preconfigure"` |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down`, *tx_rate* and *rx_rate*. |
| **description**  string | Description of Interface being configured. |
| **duplex**  string | Configures the interface duplex mode. Default is auto-negotiation when not configured.  Choices:   - `"full"` - `"half"` |
| **enabled**  boolean | Removes the shutdown configuration, which removes the forced administrative down on the interface, enabling it to move to an up or down state.  Choices:   - `false` - `true` |
| **mtu**  string | Sets the MTU value for the interface. Range is between 64 and 65535’ |
| **name**  string / required | Name of the interface to configure in `type + path` format. e.g. `GigabitEthernet0/0/0/0` |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](../network/user_guide/network_working_with_command_output.md) |
| **speed**  string | Configure the speed for an interface. Default is auto-negotiation when not configured.  Choices:   - `"10"` - `"100"` - `"1000"` |
| **state**  string | State of the Interface configuration, `up` means present and operationally up and `down` means present and operationally `down`  Choices:   - `"present"` - `"absent"` - `"up"` - `"down"` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](../network/user_guide/network_working_with_command_output.md) |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down`, *tx_rate* and *rx_rate*.  Default: `10` |
| **description**  string | Description of Interface being configured. |
| **duplex**  string | Configures the interface duplex mode. Default is auto-negotiation when not configured.  Choices:   - `"full"` - `"half"` |
| **enabled**  boolean | Removes the shutdown configuration, which removes the forced administrative down on the interface, enabling it to move to an up or down state.  Choices:   - `false` - `true` ← (default) |
| **mtu**  string | Sets the MTU value for the interface. Range is between 64 and 65535’ |
| **name**  string | Name of the interface to configure in `type + path` format. e.g. `GigabitEthernet0/0/0/0` |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Specifies the type of connection based transport.  Choices:   - `"cli"` ← (default) - `"netconf"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](../network/user_guide/network_working_with_command_output.md) |
| **speed**  string | Configure the speed for an interface. Default is auto-negotiation when not configured.  Choices:   - `"10"` - `"100"` - `"1000"` |
| **state**  string | State of the Interface configuration, `up` means present and operationally up and `down` means present and operationally `down`  Choices:   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](../network/user_guide/network_working_with_command_output.md) |

## [Notes](iosxr_interface_module.md#id5)

> **Note:**
>
> - This module works with connection `network_cli` and `netconf`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).
> - Tested against IOS XRv 6.1.3.
> - Preconfiguration of physical interfaces is not supported with `netconf` transport.
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](iosxr_interface_module.md#id6)

```yaml+jinja
- name: configure interface
  cisco.iosxr.iosxr_interface:
    name: GigabitEthernet0/0/0/2
    description: test-interface
    speed: 100
    duplex: half
    mtu: 512

- name: remove interface
  cisco.iosxr.iosxr_interface:
    name: GigabitEthernet0/0/0/2
    state: absent

- name: make interface up
  cisco.iosxr.iosxr_interface:
    name: GigabitEthernet0/0/0/2
    enabled: true

- name: make interface down
  cisco.iosxr.iosxr_interface:
    name: GigabitEthernet0/0/0/2
    enabled: false

- name: Create interface using aggregate
  cisco.iosxr.iosxr_interface:
    aggregate:
    - name: GigabitEthernet0/0/0/3
    - name: GigabitEthernet0/0/0/2
    speed: 100
    duplex: full
    mtu: 512
    state: present

- name: Create interface using aggregate along with additional params in aggregate
  cisco.iosxr.iosxr_interface:
    aggregate:
    - {name: GigabitEthernet0/0/0/3, description: test-interface 3}
    - {name: GigabitEthernet0/0/0/2, description: test-interface 2}
    speed: 100
    duplex: full
    mtu: 512
    state: present

- name: Delete interface using aggregate
  cisco.iosxr.iosxr_interface:
    aggregate:
    - name: GigabitEthernet0/0/0/3
    - name: GigabitEthernet0/0/0/2
    state: absent

- name: Check intent arguments
  cisco.iosxr.iosxr_interface:
    name: GigabitEthernet0/0/0/5
    state: up
    delay: 20

- name: Config + intent
  cisco.iosxr.iosxr_interface:
    name: GigabitEthernet0/0/0/5
    enabled: false
    state: down
    delay: 20
```

## [Return Values](iosxr_interface_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands sent to device with transport `cli`  Returned: always (empty list when no commands to send)  Sample: `["interface GigabitEthernet0/0/0/2", "description test-interface", "duplex half", "mtu 512"]` |
| **xml**  list / elements=string | NetConf rpc xml sent to device with transport `netconf`  Returned: always (empty list when no xml rpc to send)  Sample: `["<config xmlns:xc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <interface-configurations xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg\"> <interface-configuration xc:operation=\"merge\"> <active>act</active> <interface-name>GigabitEthernet0/0/0/0</interface-name> <description>test-interface-0</description> <mtus><mtu> <owner>GigabitEthernet</owner> <mtu>512</mtu> </mtu></mtus> <ethernet xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-drivers-media-eth-cfg\"> <speed>100</speed> <duplex>half</duplex> </ethernet> </interface-configuration> </interface-configurations></config>"]` |

## [Status](iosxr_interface_module.md#id8)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](iosxr_interface_module.md#deprecated).

### Authors

- Ganesh Nalawade (@ganeshrn)
- Kedar Kekan (@kedarX)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
