---
collection: ansible
version: "6"
title: "ansible.netcommon.net_interface module – (deprecated, removed after 2022-06-01) Manage Interface on network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_interface_module.html
fetched_at: 2026-07-27T16:44:28+00:00
---
# ansible.netcommon.net_interface module – (deprecated, removed after 2022-06-01) Manage Interface on network devices

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.net_interface`.

New in ansible.netcommon 1.0.0

- [DEPRECATED](net_interface_module.md#deprecated)
- [Synopsis](net_interface_module.md#synopsis)
- [Parameters](net_interface_module.md#parameters)
- [Notes](net_interface_module.md#notes)
- [Examples](net_interface_module.md#examples)
- [Return Values](net_interface_module.md#return-values)
- [Status](net_interface_module.md#status)

## [DEPRECATED](net_interface_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use platform-specific “[netos]_interfaces” module

## [Synopsis](net_interface_module.md#id2)

- This module provides declarative management of Interfaces on network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](net_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of Interfaces definitions. |
| **delay**  string | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down`, *tx_rate* and *rx_rate*.  Default: `10` |
| **description**  string | Description of Interface. |
| **duplex**  string | Interface link status  Choices:   - `"full"` - `"half"` - `"auto"` ← (default) |
| **enabled**  string | Configure interface link status. |
| **mtu**  string | Maximum size of transmit packet. |
| **name**  string / required | Name of the Interface. |
| **purge**  string | Purge Interfaces not defined in the aggregate parameter. This applies only for logical interface.  Default: `false` |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](../network/user_guide/network_working_with_command_output.md) |
| **speed**  string | Interface link speed. |
| **state**  string | State of the Interface configuration, `up` indicates present and operationally up and `down` indicates present and operationally `down`  Choices:   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](../network/user_guide/network_working_with_command_output.md) |

## [Notes](net_interface_module.md#id4)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_interface_module.md#id5)

```yaml+jinja
- name: configure interface
  ansible.netcommon.net_interface:
    name: ge-0/0/1
    description: test-interface

- name: remove interface
  ansible.netcommon.net_interface:
    name: ge-0/0/1
    state: absent

- name: make interface up
  ansible.netcommon.net_interface:
    name: ge-0/0/1
    description: test-interface
    enabled: true

- name: make interface down
  ansible.netcommon.net_interface:
    name: ge-0/0/1
    description: test-interface
    enabled: false

- name: Create interface using aggregate
  ansible.netcommon.net_interface:
    aggregate:
    - {name: ge-0/0/1, description: test-interface-1}
    - {name: ge-0/0/2, description: test-interface-2}
    speed: 1g
    duplex: full
    mtu: 512

- name: Delete interface using aggregate
  ansible.netcommon.net_interface:
    aggregate:
    - {name: ge-0/0/1}
    - {name: ge-0/0/2}
    state: absent

- name: Check intent arguments
  ansible.netcommon.net_interface:
    name: fxp0
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

- name: Config + intent
  ansible.netcommon.net_interface:
    name: fxp0
    enabled: false
    state: down
```

## [Return Values](net_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["interface 20", "name test-interface"]` |

## [Status](net_interface_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](net_interface_module.md#deprecated).

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
