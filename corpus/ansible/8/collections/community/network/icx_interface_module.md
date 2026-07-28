---
collection: ansible
version: "8"
title: "community.network.icx_interface module – Manage Interface on Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/icx_interface_module.html
fetched_at: 2026-07-28T01:56:48+00:00
---
# community.network.icx_interface module – Manage Interface on Ruckus ICX 7000 series switches

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
> To use it in a playbook, specify: `community.network.icx_interface`.

- [Synopsis](icx_interface_module.md#synopsis)
- [Parameters](icx_interface_module.md#parameters)
- [Notes](icx_interface_module.md#notes)
- [Examples](icx_interface_module.md#examples)
- [Return Values](icx_interface_module.md#return-values)

## [Synopsis](icx_interface_module.md#id1)

- This module provides declarative management of Interfaces on ruckus icx devices.

Aliases: network.icx.icx_interface

## [Parameters](icx_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of Interfaces definitions. |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable.  Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  **Choices:**   - `false` - `true` |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down`, *tx_rate* and *rx_rate*. |
| **description**  string | Name of the description. |
| **enabled**  boolean | Interface link status  **Choices:**   - `false` - `true` |
| **name**  string | Name of the Interface. |
| **neighbors**  list / elements=dictionary | Check the operational state of given interface `name` for CDP/LLDP neighbor.  The following suboptions are available. |
| **host**  string | CDP/LLDP neighbor host for given interface `name`. |
| **port**  string | CDP/LLDP neighbor port to which given interface `name` is connected. |
| **power**  dictionary | Inline power on Power over Ethernet (PoE) ports. |
| **by_class**  string | The range is 0-4  The power limit based on class value for given interface `name`  **Choices:**   - `"0"` - `"1"` - `"2"` - `"3"` - `"4"` |
| **enabled**  boolean | enable/disable the poe of the given interface `name`  **Choices:**   - `false` - `true` |
| **limit**  string | The range is 1000-15400|30000mW. For PoH ports the range is 1000-95000mW  The power limit based on actual power value for given interface `name` |
| **priority**  string | The range is 1 (highest) to 3 (lowest)  The priority for power management or given interface `name`  **Choices:**   - `"1"` - `"2"` - `"3"` |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](user_guide/network_working_with_command_output.md) |
| **speed**  string | Interface link speed/duplex  **Choices:**   - `"10-full"` - `"10-half"` - `"100-full"` - `"100-half"` - `"1000-full"` - `"1000-full-master"` - `"1000-full-slave"` - `"10g-full"` - `"10g-full-master"` - `"10g-full-slave"` - `"2500-full"` - `"2500-full-master"` - `"2500-full-slave"` - `"5g-full"` - `"5g-full-master"` - `"5g-full-slave"` - `"auto"` |
| **state**  string | State of the Interface configuration, `up` means present and operationally up and `down` means present and operationally `down`  **Choices:**   - `"present"` - `"absent"` - `"up"` - `"down"` |
| **stp**  boolean | enable/disable stp for the interface  **Choices:**   - `false` - `true` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](user_guide/network_working_with_command_output.md) |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable.  Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  **Choices:**   - `false` - `true` ← (default) |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state argument which are *state* with values `up`/`down`, *tx_rate* and *rx_rate*.  **Default:** `10` |
| **description**  string | Name of the description. |
| **enabled**  boolean | Interface link status  **Choices:**   - `false` - `true` ← (default) |
| **name**  string | Name of the Interface. |
| **neighbors**  list / elements=dictionary | Check the operational state of given interface `name` for CDP/LLDP neighbor.  The following suboptions are available. |
| **host**  string | CDP/LLDP neighbor host for given interface `name`. |
| **port**  string | CDP/LLDP neighbor port to which given interface `name` is connected. |
| **power**  dictionary | Inline power on Power over Ethernet (PoE) ports. |
| **by_class**  string | The range is 0-4  The power limit based on class value for given interface `name`  **Choices:**   - `"0"` - `"1"` - `"2"` - `"3"` - `"4"` |
| **enabled**  boolean | enable/disable the poe of the given interface `name`  Default is false.  **Choices:**   - `false` - `true` |
| **limit**  string | The range is 1000-15400|30000mW. For PoH ports the range is 1000-95000mW  The power limit based on actual power value for given interface `name` |
| **priority**  string | The range is 1 (highest) to 3 (lowest)  The priority for power management or given interface `name`  **Choices:**   - `"1"` - `"2"` - `"3"` |
| **rx_rate**  string | Receiver rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](user_guide/network_working_with_command_output.md) |
| **speed**  string | Interface link speed/duplex  **Choices:**   - `"10-full"` - `"10-half"` - `"100-full"` - `"100-half"` - `"1000-full"` - `"1000-full-master"` - `"1000-full-slave"` - `"10g-full"` - `"10g-full-master"` - `"10g-full-slave"` - `"2500-full"` - `"2500-full-master"` - `"2500-full-slave"` - `"5g-full"` - `"5g-full-master"` - `"5g-full-slave"` - `"auto"` |
| **state**  string | State of the Interface configuration, `up` means present and operationally up and `down` means present and operationally `down`  **Choices:**   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |
| **stp**  boolean | enable/disable stp for the interface  **Choices:**   - `false` - `true` |
| **tx_rate**  string | Transmit rate in bits per second (bps).  This is state check parameter only.  Supports conditionals, see [Conditionals in Networking Modules](user_guide/network_working_with_command_output.md) |

## [Notes](icx_interface_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1.
> - For information on using ICX platform, see [the ICX OS Platform Options guide](user_guide/platform_icx.md).

## [Examples](icx_interface_module.md#id4)

```yaml+jinja
- name: Enable ethernet port and set name
  community.network.icx_interface:
    name: ethernet 1/1/1
    description: interface-1
    stp: true
    enabled: true

- name: Disable ethernet port 1/1/1
  community.network.icx_interface:
      name: ethernet 1/1/1
      enabled: false

- name: Enable ethernet port range, set name and speed
  community.network.icx_interface:
      name: ethernet 1/1/1 to 1/1/10
      description: interface-1
      speed: 100-full
      enabled: true

- name: Enable poe. Set class
  community.network.icx_interface:
      name: ethernet 1/1/1
      power:
       by_class: 2

- name: Configure poe limit of interface
  community.network.icx_interface:
      name: ethernet 1/1/1
      power:
       limit: 10000

- name: Disable poe of interface
  community.network.icx_interface:
      name: ethernet 1/1/1
      power:
       enabled: false

- name: Set lag name for a range of lags
  community.network.icx_interface:
      name: lag 1 to 10
      description: test lags

- name: Disable lag
  community.network.icx_interface:
      name: lag 1
      enabled: false

- name: Enable management interface
  community.network.icx_interface:
      name: management 1
      enabled: true

- name: Enable loopback interface
  community.network.icx_interface:
      name: loopback 10
      enabled: true

- name: Add interface using aggregate
  community.network.icx_interface:
      aggregate:
      - { name: ethernet 1/1/1, description: test-interface-1, power: { by_class: 2 } }
      - { name: ethernet 1/1/3, description: test-interface-3}
      speed: 10-full
      enabled: true

- name: Check tx_rate, rx_rate intent arguments
  community.network.icx_interface:
    name: ethernet 1/1/10
    state: up
    tx_rate: ge(0)
    rx_rate: le(0)

- name: Check neighbors intent arguments
  community.network.icx_interface:
    name: ethernet 1/1/10
    neighbors:
    - port: 1/1/5
      host: netdev
```

## [Return Values](icx_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  **Returned:** always  **Sample:** `["interface ethernet 1/1/1", "port-name interface-1", "state present", "speed-duplex 100-full", "inline power priority 1"]` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
