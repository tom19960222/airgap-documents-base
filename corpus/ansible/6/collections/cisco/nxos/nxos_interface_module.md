---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_interface module – (deprecated, removed after 2022-06-01) Manages physical attributes of interfaces."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_interface_module.html
fetched_at: 2026-07-27T17:01:55+00:00
---
# cisco.nxos.nxos_interface module – (deprecated, removed after 2022-06-01) Manages physical attributes of interfaces.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/cisco/nxos) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_interface`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_interface_module.md#deprecated)
- [Synopsis](nxos_interface_module.md#synopsis)
- [Parameters](nxos_interface_module.md#parameters)
- [Notes](nxos_interface_module.md#notes)
- [Examples](nxos_interface_module.md#examples)
- [Return Values](nxos_interface_module.md#return-values)
- [Status](nxos_interface_module.md#status)

## [DEPRECATED](nxos_interface_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   nxos_interfaces

## [Synopsis](nxos_interface_module.md#id2)

- Manages physical attributes of interfaces of NX-OS switches.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_state**  string | Administrative state of the interface.  Choices:   - `"up"` ← (default) - `"down"` |
| **aggregate**  list / elements=dictionary | List of Interfaces definitions. |
| **admin_state**  string | Administrative state of the interface.  Choices:   - `"up"` - `"down"` |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state arguments. |
| **description**  string | Interface description. |
| **duplex**  string | Interface link status. Applicable for ethernet interface only.  Choices:   - `"full"` - `"half"` - `"auto"` |
| **fabric_forwarding_anycast_gateway**  boolean | Associate SVI with anycast gateway under VLAN configuration mode. Applicable for SVI interface only.  Choices:   - `false` - `true` |
| **interface_type**  string | Interface type to be unconfigured from the device.  Choices:   - `"loopback"` - `"portchannel"` - `"svi"` - `"nve"` |
| **ip_forward**  string | Enable/Disable ip forward feature on SVIs.  Choices:   - `"enable"` - `"disable"` |
| **mode**  string | Manage Layer 2 or Layer 3 state of the interface. This option is supported for ethernet and portchannel interface. Applicable for ethernet and portchannel interface only.  Choices:   - `"layer2"` - `"layer3"` |
| **mtu**  string | MTU for a specific interface. Must be an even number between 576 and 9216. Applicable for ethernet interface only. |
| **name**  string / required | Full name of interface, i.e. Ethernet1/1, port-channel10. |
| **neighbors**  list / elements=dictionary | Check the operational state of given interface `name` for LLDP neighbor.  The following suboptions are available. This is state check parameter only. |
| **host**  string | LLDP neighbor host for given interface `name`. |
| **port**  string | LLDP neighbor port to which given interface `name` is connected. |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see <https://docs.ansible.com/ansible/latest/network/user_guide/network_working_with_command_output.html#conditionals-in-networking-modules> |
| **speed**  string | Interface link speed. Applicable for ethernet interface only. |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` - `"absent"` - `"default"` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see <https://docs.ansible.com/ansible/latest/network/user_guide/network_working_with_command_output.html#conditionals-in-networking-modules> |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state arguments.  Default: `10` |
| **description**  string | Interface description. |
| **duplex**  string | Interface link status. Applicable for ethernet interface only.  Choices:   - `"full"` - `"half"` - `"auto"` |
| **fabric_forwarding_anycast_gateway**  boolean | Associate SVI with anycast gateway under VLAN configuration mode. Applicable for SVI interface only.  Choices:   - `false` - `true` |
| **interface_type**  string | Interface type to be unconfigured from the device.  Choices:   - `"loopback"` - `"portchannel"` - `"svi"` - `"nve"` |
| **ip_forward**  string | Enable/Disable ip forward feature on SVIs.  Choices:   - `"enable"` - `"disable"` |
| **mode**  string | Manage Layer 2 or Layer 3 state of the interface. This option is supported for ethernet and portchannel interface. Applicable for ethernet and portchannel interface only.  Choices:   - `"layer2"` - `"layer3"` |
| **mtu**  string | MTU for a specific interface. Must be an even number between 576 and 9216. Applicable for ethernet interface only. |
| **name**  aliases: interface  string | Full name of interface, i.e. Ethernet1/1, port-channel10. |
| **neighbors**  list / elements=dictionary | Check the operational state of given interface `name` for LLDP neighbor.  The following suboptions are available. This is state check parameter only. |
| **host**  string | LLDP neighbor host for given interface `name`. |
| **port**  string | LLDP neighbor port to which given interface `name` is connected. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  Starting with Ansible 2.6 we recommend using `connection: httpapi` for NX-API.  This option will be removed in a release after 2022-06-01.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_nxos.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This is a common argument used for either *cli* or *nxapi* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. This value applies to either *cli* or *nxapi*. The port value will default to the appropriate transport common port if none is provided in the task. (cli=22, http=80, https=443). |
| **ssh_keyfile**  string | Specifies the SSH key to use to authenticate the connection to the remote device. This argument is only used for the *cli* transport. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc). |
| **transport**  string | Configures the transport connection to use when connecting to the remote device. The transport argument supports connectivity to the device over cli (ssh) or nxapi.  Choices:   - `"cli"` ← (default) - `"nxapi"` |
| **use_proxy**  boolean | If `no`, the environment variables `http_proxy` and `https_proxy` will be ignored.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | Configures the *transport* to use SSL if set to `yes` only when the `transport=nxapi`, otherwise this value is ignored.  Choices:   - `false` ← (default) - `true` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates. If the transport argument is not nxapi, this value is ignored.  Choices:   - `false` ← (default) - `true` |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see <https://docs.ansible.com/ansible/latest/network/user_guide/network_working_with_command_output.html#conditionals-in-networking-modules> |
| **speed**  string | Interface link speed. Applicable for ethernet interface only. |
| **state**  string | Specify desired state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` - `"default"` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see <https://docs.ansible.com/ansible/latest/network/user_guide/network_working_with_command_output.html#conditionals-in-networking-modules> |

## [Notes](nxos_interface_module.md#id4)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - This module is also used to create logical interfaces such as svis and loopbacks.
> - Be cautious of platform specific idiosyncrasies. For example, when you default a loopback interface, the admin state toggles on certain versions of NX-OS.
> - The [cisco.nxos.nxos_overlay_global](nxos_overlay_global_module.md#ansible-collections-cisco-nxos-nxos-overlay-global-module) `anycast_gateway_mac` attribute must be set before setting the `fabric_forwarding_anycast_gateway` property.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_interface_module.md#id5)

```yaml+jinja
- name: Ensure an interface is a Layer 3 port and that it has the proper description
  cisco.nxos.nxos_interface:
    name: Ethernet1/1
    description: Configured by Ansible
    mode: layer3

- name: Admin down an interface
  cisco.nxos.nxos_interface:
    name: Ethernet2/1
    admin_state: down

- name: Remove all loopback interfaces
  cisco.nxos.nxos_interface:
    name: loopback
    state: absent

- name: Remove all logical interfaces
  cisco.nxos.nxos_interface:
    interface_type: '{{ item }} '
    state: absent
  loop:
  - loopback
  - portchannel
  - svi
  - nve

- name: Admin up all loopback interfaces
  cisco.nxos.nxos_interface:
    name: loopback 0-1023
    admin_state: up

- name: Admin down all loopback interfaces
  cisco.nxos.nxos_interface:
    name: loopback 0-1023
    admin_state: down

- name: Check neighbors intent arguments
  cisco.nxos.nxos_interface:
    name: Ethernet2/3
    neighbors:
    - port: Ethernet2/3
      host: abc.mycompany.com

- name: Add interface using aggregate
  cisco.nxos.nxos_interface:
    aggregate:
    - {name: Ethernet0/1, mtu: 256, description: test-interface-1}
    - {name: Ethernet0/2, mtu: 516, description: test-interface-2}
    duplex: full
    speed: 100
    state: present

- name: Delete interface using aggregate
  cisco.nxos.nxos_interface:
    aggregate:
    - name: Loopback9
    - name: Loopback10
    state: absent

- name: Check intent arguments
  cisco.nxos.nxos_interface:
    name: Ethernet0/2
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)
```

## [Return Values](nxos_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | command list sent to the device  Returned: always  Sample: `["interface Ethernet2/3", "mtu 1500", "speed 10"]` |

## [Status](nxos_interface_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_interface_module.md#deprecated).

### Authors

- Jason Edelman (@jedelman8)
- Trishna Guha (@trishnaguha)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
