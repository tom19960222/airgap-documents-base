---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_interface module – (deprecated, removed after 2022-06-01) Manage Interface on Juniper JUNOS network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_interface_module.html
fetched_at: 2026-07-27T17:54:16+00:00
---
# junipernetworks.junos.junos_interface module – (deprecated, removed after 2022-06-01) Manage Interface on Juniper JUNOS network devices

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_interface_module.md#ansible-collections-junipernetworks-junos-junos-interface-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_interface`.

New in junipernetworks.junos 1.0.0

- [DEPRECATED](junos_interface_module.md#deprecated)
- [Synopsis](junos_interface_module.md#synopsis)
- [Requirements](junos_interface_module.md#requirements)
- [Parameters](junos_interface_module.md#parameters)
- [Notes](junos_interface_module.md#notes)
- [Examples](junos_interface_module.md#examples)
- [Return Values](junos_interface_module.md#return-values)
- [Status](junos_interface_module.md#status)

## [DEPRECATED](junos_interface_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use [junipernetworks.junos.junos_interfaces](junos_interfaces_module.md#ansible-collections-junipernetworks-junos-junos-interfaces-module) instead.

## [Synopsis](junos_interface_module.md#id2)

- This module provides declarative management of Interfaces on Juniper JUNOS network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_interface_module.md#id3)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)

## [Parameters](junos_interface_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  Choices:   - `false` - `true` ← (default) |
| **aggregate**  list / elements=dictionary | List of Interfaces definitions. |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  Choices:   - `false` - `true` |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down`, *tx_rate* and *rx_rate*. |
| **description**  string | Description of Interface. |
| **duplex**  string | Interface link status.  Choices:   - `"full"` - `"half"` - `"auto"` |
| **enabled**  boolean | Configure interface link status.  Choices:   - `false` - `true` |
| **mtu**  integer | Maximum size of transmit packet. |
| **name**  string / required | Name of the Interface. |
| **neighbors**  list / elements=dictionary | Check the operational state of given interface `name` for LLDP neighbor.  The following suboptions are available. |
| **host**  string | LLDP neighbor host for given interface `name`. |
| **port**  string | LLDP neighbor port to which given interface `name` is connected. |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](../network/user_guide/network_working_with_command_output.md) |
| **speed**  string | Interface link speed. |
| **state**  string | State of the Interface configuration, `up` indicates present and operationally up and `down` indicates present and operationally `down`  Choices:   - `"present"` - `"absent"` - `"up"` - `"down"` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](../network/user_guide/network_working_with_command_output.md) |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down`, *tx_rate* and *rx_rate*.  Default: `10` |
| **description**  string | Description of Interface. |
| **duplex**  string | Interface link status.  Choices:   - `"full"` - `"half"` - `"auto"` |
| **enabled**  boolean | Configure interface link status.  Choices:   - `false` - `true` ← (default) |
| **mtu**  integer | Maximum size of transmit packet. |
| **name**  string | Name of the Interface. |
| **neighbors**  list / elements=dictionary | Check the operational state of given interface `name` for LLDP neighbor.  The following suboptions are available. |
| **host**  string | LLDP neighbor host for given interface `name`. |
| **port**  string | LLDP neighbor port to which given interface `name` is connected. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` or `connection: netconf`.  For more information please see the [Junos OS Platform Options guide](../network/user_guide/platform_junos.md).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. The port value will default to the well known SSH port of 22 (for `transport=cli`) or port 830 (for `transport=netconf`) device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` - `"netconf"` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](../network/user_guide/network_working_with_command_output.md) |
| **speed**  string | Interface link speed. |
| **state**  string | State of the Interface configuration, `up` indicates present and operationally up and `down` indicates present and operationally `down`  Choices:   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](../network/user_guide/network_working_with_command_output.md) |

## [Notes](junos_interface_module.md#id5)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Recommended connection is `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - This module also works with `local` connections for legacy playbooks.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_interface_module.md#id6)

```yaml+jinja
- name: configure interface
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    description: test-interface

- name: remove interface
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    state: absent

- name: make interface down
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    enabled: false

- name: make interface up
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    enabled: true

- name: Deactivate interface config
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    state: present
    active: false

- name: Activate interface config
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    state: present
    active: true

- name: Configure interface speed, mtu, duplex
  junipernetworks.junos.junos_interface:
    name: ge-0/0/1
    state: present
    speed: 1g
    mtu: 256
    duplex: full

- name: Create interface using aggregate
  junipernetworks.junos.junos_interface:
    aggregate:
    - name: ge-0/0/1
      description: test-interface-1
    - name: ge-0/0/2
      description: test-interface-2
    speed: 1g
    duplex: full
    mtu: 512

- name: Delete interface using aggregate
  junipernetworks.junos.junos_interface:
    aggregate:
    - name: ge-0/0/1
    - name: ge-0/0/2
    state: absent

- name: Check intent arguments
  junipernetworks.junos.junos_interface:
    name: '{{ name }}'
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

- name: Check neighbor intent
  junipernetworks.junos.junos_interface:
    name: xe-0/1/1
    neighbors:
    - port: Ethernet1/0/1
      host: netdev

- name: Config + intent
  junipernetworks.junos.junos_interface:
    name: '{{ name }}'
    enabled: false
    state: down
```

## [Return Values](junos_interface_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff.prepared**  string | Configuration difference before and after applying change.  Returned: when configuration is changed and diff option is enabled.  Sample: `"[edit interfaces] +   ge-0/0/1 { +       description test-interface; +   }\n"` |

## [Status](junos_interface_module.md#id8)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](junos_interface_module.md#deprecated).

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
