---
collection: ansible
version: "8"
title: "community.network.slxos_interface module – Manage Interfaces on Extreme SLX-OS network devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/slxos_interface_module.html
fetched_at: 2026-07-28T01:57:49+00:00
---
# community.network.slxos_interface module – Manage Interfaces on Extreme SLX-OS network devices

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
> To use it in a playbook, specify: `community.network.slxos_interface`.

- [Synopsis](slxos_interface_module.md#synopsis)
- [Parameters](slxos_interface_module.md#parameters)
- [Notes](slxos_interface_module.md#notes)
- [Examples](slxos_interface_module.md#examples)
- [Return Values](slxos_interface_module.md#return-values)

## [Synopsis](slxos_interface_module.md#id1)

- This module provides declarative management of Interfaces on Extreme SLX-OS network devices.

Aliases: network.slxos.slxos_interface

## [Parameters](slxos_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | List of Interfaces definitions. |
| **delay**  string | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down`, *tx_rate* and *rx_rate*.  **Default:** `10` |
| **description**  string | Description of Interface. |
| **enabled**  boolean | Interface link status.  **Choices:**   - `false` - `true` ← (default) |
| **mtu**  string | Maximum size of transmit packet. |
| **name**  string / required | Name of the Interface. |
| **neighbors**  string | Check the operational state of given interface `name` for LLDP neighbor.  The following suboptions are available. |
| **host**  string | LLDP neighbor host for given interface `name`. |
| **port**  string | LLDP neighbor port to which given interface `name` is connected. |
| **rx_rate**  string | Receiver rate in bits per second (bps). |
| **speed**  string | Interface link speed. |
| **state**  string | State of the Interface configuration, `up` means present and operationally up and `down` means present and operationally `down`  **Choices:**   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |
| **tx_rate**  string | Transmit rate in bits per second (bps). |

## [Notes](slxos_interface_module.md#id3)

> **Note:**
>
> - Tested against SLX-OS 17s.1.02

## [Examples](slxos_interface_module.md#id4)

```yaml+jinja
- name: Configure interface
  community.network.slxos_interface:
      name: Ethernet 0/2
      description: test-interface
      speed: 1000
      mtu: 9216

- name: Remove interface
  community.network.slxos_interface:
    name: Loopback 9
    state: absent

- name: Make interface up
  community.network.slxos_interface:
    name: Ethernet 0/2
    enabled: true

- name: Make interface down
  community.network.slxos_interface:
    name: Ethernet 0/2
    enabled: false

- name: Check intent arguments
  community.network.slxos_interface:
    name: Ethernet 0/2
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

- name: Check neighbors intent arguments
  community.network.slxos_interface:
    name: Ethernet 0/41
    neighbors:
    - port: Ethernet 0/41
      host: SLX

- name: Config + intent
  community.network.slxos_interface:
    name: Ethernet 0/2
    enabled: false
    state: down

- name: Add interface using aggregate
  community.network.slxos_interface:
    aggregate:
    - { name: Ethernet 0/1, mtu: 1548, description: test-interface-1 }
    - { name: Ethernet 0/2, mtu: 1548, description: test-interface-2 }
    speed: 10000
    state: present

- name: Delete interface using aggregate
  community.network.slxos_interface:
    aggregate:
    - name: Loopback 9
    - name: Loopback 10
    state: absent
```

## [Return Values](slxos_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  **Returned:** always, except for the platforms that use Netconf transport to manage the device.  **Sample:** `["interface Ethernet 0/2", "description test-interface", "mtu 1548"]` |

### Authors

- Lindsay Hill (@LindsayHill)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
