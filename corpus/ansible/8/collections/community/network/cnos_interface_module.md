---
collection: ansible
version: "8"
title: "community.network.cnos_interface module – Manage Interface on Lenovo CNOS network devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/cnos_interface_module.html
fetched_at: 2026-07-28T01:56:12+00:00
---
# community.network.cnos_interface module – Manage Interface on Lenovo CNOS network devices

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.cnos_interface`.

- [Synopsis](cnos_interface_module.md#synopsis)
- [Parameters](cnos_interface_module.md#parameters)
- [Notes](cnos_interface_module.md#notes)
- [Examples](cnos_interface_module.md#examples)
- [Return Values](cnos_interface_module.md#return-values)

## [Synopsis](cnos_interface_module.md#id1)

- This module provides declarative management of Interfaces on Lenovo CNOS network devices.

Aliases: network.cnos.cnos_interface

## [Parameters](cnos_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of Interfaces definitions. |
| **delay**  string | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down`, *tx_rate* and *rx_rate*  **Default:** `20` |
| **description**  string | Description of Interface. |
| **duplex**  string | Interface link status  **Choices:**   - `"full"` - `"half"` - `"auto"` ← (default) |
| **enabled**  boolean | Interface link status.  **Choices:**   - `false` - `true` ← (default) |
| **mtu**  string | Maximum size of transmit packet. |
| **name**  string / required | Name of the Interface. |
| **neighbors**  string | Check operational state of given interface `name` for LLDP neighbor.  The following suboptions are available. |
| **host**  string | LLDP neighbor host for given interface `name`. |
| **port**  string | LLDP neighbor port to which interface `name` is connected. |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](user_guide/network_working_with_command_output.md) |
| **speed**  string | Interface link speed. |
| **state**  string | State of the Interface configuration, `up` means present and operationally up and `down` means present and operationally `down`  **Choices:**   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](user_guide/network_working_with_command_output.md) |

## [Notes](cnos_interface_module.md#id3)

> **Note:**
>
> - Tested against CNOS 10.8.1

## [Examples](cnos_interface_module.md#id4)

```yaml+jinja
- name: Configure interface
  community.network.cnos_interface:
      name: Ethernet1/33
      description: test-interface
      speed: 100
      duplex: half
      mtu: 999

- name: Remove interface
  community.network.cnos_interface:
    name: loopback3
    state: absent

- name: Make interface up
  community.network.cnos_interface:
    name: Ethernet1/33
    enabled: true

- name: Make interface down
  community.network.cnos_interface:
    name: Ethernet1/33
    enabled: false

- name: Check intent arguments
  community.network.cnos_interface:
    name: Ethernet1/33
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

- name: Check neighbors intent arguments
  community.network.cnos_interface:
    name: Ethernet1/33
    neighbors:
    - port: eth0
      host: netdev

- name: Config + intent
  community.network.cnos_interface:
    name: Ethernet1/33
    enabled: false
    state: down

- name: Add interface using aggregate
  community.network.cnos_interface:
    aggregate:
    - { name: Ethernet1/33, mtu: 256, description: test-interface-1 }
    - { name: Ethernet1/44, mtu: 516, description: test-interface-2 }
    duplex: full
    speed: 100
    state: present

- name: Delete interface using aggregate
  community.network.cnos_interface:
    aggregate:
    - name: loopback3
    - name: loopback6
    state: absent
```

## [Return Values](cnos_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  **Returned:** always, except for the platforms that use Netconf transport to manage the device.  **Sample:** `["interface Ethernet1/33", "description test-interface", "duplex half", "mtu 512"]` |

### Authors

- Anil Kumar Muraleedharan(@amuraleedhar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
