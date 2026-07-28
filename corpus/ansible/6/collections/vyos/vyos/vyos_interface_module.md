---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_interface module – (deprecated, removed after 2022-06-01) Manage Interface on VyOS network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_interface_module.html
fetched_at: 2026-07-28T00:23:18+00:00
---
# vyos.vyos.vyos_interface module – (deprecated, removed after 2022-06-01) Manage Interface on VyOS network devices

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
> To use it in a playbook, specify: `vyos.vyos.vyos_interface`.

New in vyos.vyos 1.0.0

- [DEPRECATED](vyos_interface_module.md#deprecated)
- [Synopsis](vyos_interface_module.md#synopsis)
- [Parameters](vyos_interface_module.md#parameters)
- [Notes](vyos_interface_module.md#notes)
- [Examples](vyos_interface_module.md#examples)
- [Return Values](vyos_interface_module.md#return-values)
- [Status](vyos_interface_module.md#status)

## [DEPRECATED](vyos_interface_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality.

Alternative:
:   vyos_interfaces

## [Synopsis](vyos_interface_module.md#id2)

- This module provides declarative management of Interfaces on VyOS network devices.

## [Parameters](vyos_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of Interfaces definitions. |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down` and *neighbors*. |
| **description**  string | Description of Interface. |
| **duplex**  string | Interface link status.  Choices:   - `"full"` - `"half"` - `"auto"` |
| **enabled**  boolean | Interface link status.  Choices:   - `false` - `true` |
| **mtu**  integer | Maximum size of transmit packet. |
| **name**  string / required | Name of the Interface. |
| **neighbors**  list / elements=dictionary | Check the operational state of given interface `name` for LLDP neighbor.  The following suboptions are available. |
| **host**  string | LLDP neighbor host for given interface `name`. |
| **port**  string | LLDP neighbor port to which given interface `name` is connected. |
| **speed**  string | Interface link speed. |
| **state**  string | State of the Interface configuration, `up` means present and operationally up and `down` means present and operationally `down`  Choices:   - `"present"` - `"absent"` - `"up"` - `"down"` |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down` and *neighbors*.  Default: `10` |
| **description**  string | Description of Interface. |
| **duplex**  string | Interface link status.  Choices:   - `"full"` - `"half"` - `"auto"` |
| **enabled**  boolean | Interface link status.  Choices:   - `false` - `true` ← (default) |
| **mtu**  integer | Maximum size of transmit packet. |
| **name**  string | Name of the Interface. |
| **neighbors**  list / elements=dictionary | Check the operational state of given interface `name` for LLDP neighbor.  The following suboptions are available. |
| **host**  string | LLDP neighbor host for given interface `name`. |
| **port**  string | LLDP neighbor port to which given interface `name` is connected. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **speed**  string | Interface link speed. |
| **state**  string | State of the Interface configuration, `up` means present and operationally up and `down` means present and operationally `down`  Choices:   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |

## [Notes](vyos_interface_module.md#id4)

> **Note:**
>
> - Tested against VYOS 1.1.7
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_interface_module.md#id5)

```yaml+jinja
- name: configure interface
  vyos.vyos.vyos_interface:
    name: eth0
    description: test-interface

- name: remove interface
  vyos.vyos.vyos_interface:
    name: eth0
    state: absent

- name: make interface down
  vyos.vyos.vyos_interface:
    name: eth0
    enabled: false

- name: make interface up
  vyos.vyos.vyos_interface:
    name: eth0
    enabled: true

- name: Configure interface speed, mtu, duplex
  vyos.vyos.vyos_interface:
    name: eth5
    state: present
    speed: 100
    mtu: 256
    duplex: full

- name: Set interface using aggregate
  vyos.vyos.vyos_interface:
    aggregate:
    - {name: eth1, description: test-interface-1, speed: 100, duplex: half, mtu: 512}
    - {name: eth2, description: test-interface-2, speed: 1000, duplex: full, mtu: 256}

- name: Disable interface on aggregate
  net_interface:
    aggregate:
    - name: eth1
    - name: eth2
    enabled: false

- name: Delete interface using aggregate
  net_interface:
    aggregate:
    - name: eth1
    - name: eth2
    state: absent

- name: Check lldp neighbors intent arguments
  vyos.vyos.vyos_interface:
    name: eth0
    neighbors:
    - port: eth0
      host: netdev

- name: Config + intent
  vyos.vyos.vyos_interface:
    name: eth1
    enabled: false
    state: down
```

## [Return Values](vyos_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["set interfaces ethernet eth0 description \"test-interface\"", "set interfaces ethernet eth0 speed 100", "set interfaces ethernet eth0 mtu 256", "set interfaces ethernet eth0 duplex full"]` |

## [Status](vyos_interface_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](vyos_interface_module.md#deprecated).

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
