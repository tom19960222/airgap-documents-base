---
collection: ansible
version: "6"
title: "cisco.ios.ios_interface module – (deprecated, removed after 2022-06-01) Manage Interface on Cisco IOS network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_interface_module.html
fetched_at: 2026-07-27T16:55:11+00:00
---
# cisco.ios.ios_interface module – (deprecated, removed after 2022-06-01) Manage Interface on Cisco IOS network devices

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
> To use it in a playbook, specify: `cisco.ios.ios_interface`.

New in cisco.ios 1.0.0

- [DEPRECATED](ios_interface_module.md#deprecated)
- [Synopsis](ios_interface_module.md#synopsis)
- [Parameters](ios_interface_module.md#parameters)
- [Notes](ios_interface_module.md#notes)
- [Examples](ios_interface_module.md#examples)
- [Return Values](ios_interface_module.md#return-values)
- [Status](ios_interface_module.md#status)

## [DEPRECATED](ios_interface_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Newer and updated modules released with more functionality in Ansible 2.9

Alternative:
:   ios_interfaces

## [Synopsis](ios_interface_module.md#id2)

- This module provides declarative management of Interfaces on Cisco IOS network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of Interfaces definitions. |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down`, *tx_rate* and *rx_rate*. |
| **description**  string | Description of Interface. |
| **duplex**  string | Interface link status  Choices:   - `"full"` - `"half"` - `"auto"` |
| **enabled**  boolean | Interface link status.  Choices:   - `false` - `true` |
| **mtu**  string | Maximum size of transmit packet. |
| **name**  string / required | Name of the Interface. |
| **neighbors**  list / elements=dictionary | Check the operational state of given interface `name` for CDP/LLDP neighbor.  The following suboptions are available. |
| **host**  string | CDP/LLDP neighbor host for given interface `name`. |
| **port**  string | CDP/LLDP neighbor port to which given interface `name` is connected. |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see <https://docs.ansible.com/ansible/latest/network/user_guide/network_working_with_command_output.html#conditionals-in-networking-modules> |
| **speed**  string | Interface link speed. |
| **state**  string | State of the Interface configuration, `up` means present and operationally up and `down` means present and operationally `down`  Choices:   - `"present"` - `"absent"` - `"up"` - `"down"` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see <https://docs.ansible.com/ansible/latest/network/user_guide/network_working_with_command_output.html#conditionals-in-networking-modules> |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down`, *tx_rate* and *rx_rate*.  Default: `10` |
| **description**  string | Description of Interface. |
| **duplex**  string | Interface link status  Choices:   - `"full"` - `"half"` - `"auto"` |
| **enabled**  boolean | Interface link status.  Choices:   - `false` - `true` ← (default) |
| **mtu**  string | Maximum size of transmit packet. |
| **name**  string | Name of the Interface. |
| **neighbors**  list / elements=dictionary | Check the operational state of given interface `name` for CDP/LLDP neighbor.  The following suboptions are available. |
| **host**  string | CDP/LLDP neighbor host for given interface `name`. |
| **port**  string | CDP/LLDP neighbor port to which given interface `name` is connected. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see <https://docs.ansible.com/ansible/latest/network/user_guide/network_working_with_command_output.html#conditionals-in-networking-modules> |
| **speed**  string | Interface link speed. |
| **state**  string | State of the Interface configuration, `up` means present and operationally up and `down` means present and operationally `down`  Choices:   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see <https://docs.ansible.com/ansible/latest/network/user_guide/network_working_with_command_output.html#conditionals-in-networking-modules> |

## [Notes](ios_interface_module.md#id4)

> **Note:**
>
> - Tested against IOS 15.6
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_interface_module.md#id5)

```yaml+jinja
- name: configure interface
  cisco.ios.ios_interface:
    name: GigabitEthernet0/2
    description: test-interface
    speed: 100
    duplex: half
    mtu: 512

- name: remove interface
  cisco.ios.ios_interface:
    name: Loopback9
    state: absent

- name: make interface up
  cisco.ios.ios_interface:
    name: GigabitEthernet0/2
    enabled: true

- name: make interface down
  cisco.ios.ios_interface:
    name: GigabitEthernet0/2
    enabled: false

- name: Check intent arguments
  cisco.ios.ios_interface:
    name: GigabitEthernet0/2
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

- name: Check neighbors intent arguments
  cisco.ios.ios_interface:
    name: Gi0/0
    neighbors:
    - port: eth0
      host: netdev

- name: Config + intent
  cisco.ios.ios_interface:
    name: GigabitEthernet0/2
    enabled: false
    state: down

- name: Add interface using aggregate
  cisco.ios.ios_interface:
    aggregate:
    - {name: GigabitEthernet0/1, mtu: 256, description: test-interface-1}
    - {name: GigabitEthernet0/2, mtu: 516, description: test-interface-2}
    duplex: full
    speed: 100
    state: present

- name: Delete interface using aggregate
  cisco.ios.ios_interface:
    aggregate:
    - name: Loopback9
    - name: Loopback10
    state: absent
```

## [Return Values](ios_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["interface GigabitEthernet0/2", "description test-interface", "duplex half", "mtu 512"]` |

## [Status](ios_interface_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](ios_interface_module.md#deprecated).

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
