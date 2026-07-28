---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_l3_interfaces module – L3 interfaces resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_l3_interfaces_module.html
fetched_at: 2026-07-28T02:59:15+00:00
---
# vyos.vyos.vyos_l3_interfaces module – L3 interfaces resource module

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_l3_interfaces`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_l3_interfaces_module.md#synopsis)
- [Parameters](vyos_l3_interfaces_module.md#parameters)
- [Notes](vyos_l3_interfaces_module.md#notes)
- [Examples](vyos_l3_interfaces_module.md#examples)
- [Return Values](vyos_l3_interfaces_module.md#return-values)

## [Synopsis](vyos_l3_interfaces_module.md#id1)

- This module manages the L3 interface attributes on VyOS network devices.

Aliases: l3_interfaces

## [Parameters](vyos_l3_interfaces_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | The provided L3 interfaces configuration. |
| **ipv4**  list / elements=dictionary | List of IPv4 addresses of the interface. |
| **address**  string | IPv4 address of the interface. |
| **ipv6**  list / elements=dictionary | List of IPv6 addresses of the interface. |
| **address**  string | IPv6 address of the interface. |
| **name**  string / required | Full name of the interface, e.g. eth0, eth1. |
| **vifs**  list / elements=dictionary | Virtual sub-interfaces L3 configurations. |
| **ipv4**  list / elements=dictionary | List of IPv4 addresses of the virtual interface. |
| **address**  string | IPv4 address of the virtual interface. |
| **ipv6**  list / elements=dictionary | List of IPv6 addresses of the virtual interface. |
| **address**  string | IPv6 address of the virtual interface. |
| **vlan_id**  integer | Identifier for the virtual sub-interface. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VyOS device by executing the command **show configuration commands | grep -e eth[2,3]**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state of the configuration after module completion.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](vyos_l3_interfaces_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `ansible.netcommon.network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).

## [Examples](vyos_l3_interfaces_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# vyos:~$ show configuration commands | grep -e eth[2,3]
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 vif 101
# set interfaces ethernet eth3 vif 102

- name: Merge provided configuration with device configuration
  vyos.vyos.vyos_l3_interfaces:
    config:
    - name: eth2
      ipv4:
      - address: 192.0.2.10/28
      - address: 198.51.100.40/27
      ipv6:
      - address: 2001:db8:100::2/32
      - address: 2001:db8:400::10/32

    - name: eth3
      ipv4:
      - address: 203.0.113.65/26
      vifs:
      - vlan_id: 101
        ipv4:
        - address: 192.0.2.71/28
        - address: 198.51.100.131/25
      - vlan_id: 102
        ipv6:
        - address: 2001:db8:1000::5/38
        - address: 2001:db8:1400::3/38
    state: merged

# After state:
# -------------
#
# vyos:~$ show configuration commands | grep -e eth[2,3]
# set interfaces ethernet eth2 address '192.0.2.10/28'
# set interfaces ethernet eth2 address '198.51.100.40/27'
# set interfaces ethernet eth2 address '2001:db8:100::2/32'
# set interfaces ethernet eth2 address '2001:db8:400::10/32'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth3 address '203.0.113.65/26'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 vif 101 address '192.0.2.71/28'
# set interfaces ethernet eth3 vif 101 address '198.51.100.131/25'
# set interfaces ethernet eth3 vif 102 address '2001:db8:1000::5/38'
# set interfaces ethernet eth3 vif 102 address '2001:db8:1400::3/38'
# set interfaces ethernet eth3 vif 102 address '2001:db8:4000::2/34'

# Using replaced
#
# Before state:
# -------------
#
# vyos:~$ show configuration commands | grep eth
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:EA:0F:B9'
# set interfaces ethernet eth1 address '192.0.2.14/24'
# set interfaces ethernet eth2 address '192.0.2.10/24'
# set interfaces ethernet eth2 address '192.0.2.11/24'
# set interfaces ethernet eth2 address '2001:db8::10/32'
# set interfaces ethernet eth2 address '2001:db8::11/32'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth3 address '198.51.100.10/24'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 vif 101 address '198.51.100.130/25'
# set interfaces ethernet eth3 vif 101 address '198.51.100.131/25'
# set interfaces ethernet eth3 vif 102 address '2001:db8:4000::3/34'
# set interfaces ethernet eth3 vif 102 address '2001:db8:4000::2/34'
#
- name: Replace device configurations of listed interfaces with provided configurations
  vyos.vyos.vyos_l3_interfaces:
    config:
    - name: eth2
      ipv4:
      - address: 192.0.2.10/24

    - name: eth3
      ipv6:
      - address: 2001:db8::11/32
    state: replaced

# After state:
# -------------
#
# vyos:~$ show configuration commands | grep eth
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:EA:0F:B9'
# set interfaces ethernet eth1 address '192.0.2.14/24'
# set interfaces ethernet eth2 address '192.0.2.10/24'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 address '2001:db8::11/32'
# set interfaces ethernet eth3 vif 101
# set interfaces ethernet eth3 vif 102

# Using overridden
#
# Before state
# --------------
#
# vyos@vyos-appliance:~$ show configuration commands | grep eth
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:EA:0F:B9'
# set interfaces ethernet eth1 address '192.0.2.14/24'
# set interfaces ethernet eth2 address '192.0.2.10/24'
# set interfaces ethernet eth2 address '192.0.2.11/24'
# set interfaces ethernet eth2 address '2001:db8::10/32'
# set interfaces ethernet eth2 address '2001:db8::11/32'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth3 address '198.51.100.10/24'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 vif 101 address '198.51.100.130/25'
# set interfaces ethernet eth3 vif 101 address '198.51.100.131/25'
# set interfaces ethernet eth3 vif 102 address '2001:db8:4000::3/34'
# set interfaces ethernet eth3 vif 102 address '2001:db8:4000::2/34'

- name: Overrides all device configuration with provided configuration
  vyos.vyos.vyos_l3_interfaces:
    config:
    - name: eth0
      ipv4:
      - address: dhcp
      ipv6:
      - address: dhcpv6
    state: overridden

# After state
# ------------
#
# vyos@vyos-appliance:~$ show configuration commands | grep eth
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 address 'dhcpv6'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:EA:0F:B9'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 vif 101
# set interfaces ethernet eth3 vif 102

# Using deleted
#
# Before state
# -------------
# vyos@vyos-appliance:~$ show configuration commands | grep eth
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:30:f0:22'
# set interfaces ethernet eth0 smp-affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:EA:0F:B9'
# set interfaces ethernet eth1 address '192.0.2.14/24'
# set interfaces ethernet eth2 address '192.0.2.10/24'
# set interfaces ethernet eth2 address '192.0.2.11/24'
# set interfaces ethernet eth2 address '2001:db8::10/32'
# set interfaces ethernet eth2 address '2001:db8::11/32'
# set interfaces ethernet eth2 hw-id '08:00:27:c2:98:23'
# set interfaces ethernet eth3 address '198.51.100.10/24'
# set interfaces ethernet eth3 hw-id '08:00:27:43:70:8c'
# set interfaces ethernet eth3 vif 101 address '198.51.100.130/25'
# set interfaces ethernet eth3 vif 101 address '198.51.100.131/25'
# set interfaces ethernet eth3 vif 102 address '2001:db8:4000::3/34'
# set interfaces ethernet eth3 vif 102 address '2001:db8:4000::2/34'

- name: Delete L3 attributes of given interfaces (Note - This won't delete the interface
    itself)
  vyos.vyos.vyos_l3_interfaces:
    config:
    - name: eth1
    - name: eth2
    - name: eth3
    state: deleted

# After state
# ------------
# vyos@vyos-appliance:~$ show configuration commands | grep eth
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:f3:6c:b5'
# set interfaces ethernet eth0 smp_affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 hw-id '08:00:27:ad:ef:65'
# set interfaces ethernet eth1 smp_affinity 'auto'
# set interfaces ethernet eth2 hw-id '08:00:27:ab:4e:79'
# set interfaces ethernet eth2 smp_affinity 'auto'
# set interfaces ethernet eth3 hw-id '08:00:27:17:3c:85'
# set interfaces ethernet eth3 smp_affinity 'auto'

# Using gathered
#
# Before state:
# -------------
#
# vyos:~$ show configuration commands | grep -e eth[2,3,0]
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:50:5e:19'
# set interfaces ethernet eth0 smp_affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 address '192.0.2.14/24'
# set interfaces ethernet eth2 address '192.0.2.11/24'
# set interfaces ethernet eth2 address '192.0.2.10/24'
# set interfaces ethernet eth2 address '2001:db8::10/32'
# set interfaces ethernet eth2 address '2001:db8::12/32'
#
- name: Gather listed l3 interfaces with provided configurations
  vyos.vyos.vyos_l3_interfaces:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": [
#         {
#             "ipv4": [
#                 {
#                     "address": "192.0.2.11/24"
#                 },
#                 {
#                     "address": "192.0.2.10/24"
#                 }
#             ],
#             "ipv6": [
#                 {
#                     "address": "2001:db8::10/32"
#                 },
#                 {
#                     "address": "2001:db8::12/32"
#                 }
#             ],
#             "name": "eth2"
#         },
#         {
#             "ipv4": [
#                 {
#                     "address": "192.0.2.14/24"
#                 }
#             ],
#             "name": "eth1"
#         },
#         {
#             "ipv4": [
#                 {
#                     "address": "dhcp"
#                 }
#             ],
#             "name": "eth0"
#         }
#     ]
#
#
# After state:
# -------------
#
# vyos:~$ show configuration commands | grep -e eth[2,3]
# set interfaces ethernet eth0 address 'dhcp'
# set interfaces ethernet eth0 duplex 'auto'
# set interfaces ethernet eth0 hw-id '08:00:27:50:5e:19'
# set interfaces ethernet eth0 smp_affinity 'auto'
# set interfaces ethernet eth0 speed 'auto'
# set interfaces ethernet eth1 address '192.0.2.14/24'
# set interfaces ethernet eth2 address '192.0.2.11/24'
# set interfaces ethernet eth2 address '192.0.2.10/24'
# set interfaces ethernet eth2 address '2001:db8::10/32'
# set interfaces ethernet eth2 address '2001:db8::12/32'

# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_l3_interfaces:
    config:
    - name: eth1
      ipv4:
      - address: 192.0.2.14/24
    - name: eth2
      ipv4:
      - address: 192.0.2.10/24
      - address: 192.0.2.11/24
      ipv6:
      - address: 2001:db8::10/32
      - address: 2001:db8::12/32
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#         "set interfaces ethernet eth1 address '192.0.2.14/24'",
#         "set interfaces ethernet eth2 address '192.0.2.11/24'",
#         "set interfaces ethernet eth2 address '192.0.2.10/24'",
#         "set interfaces ethernet eth2 address '2001:db8::10/32'",
#         "set interfaces ethernet eth2 address '2001:db8::12/32'"
#     ]

# Using parsed
#
#
- name: parse the provided running configuration
  vyos.vyos.vyos_l3_interfaces:
    running_config:
      "set interfaces ethernet eth0 address 'dhcp'
       set interfaces ethernet eth1 address '192.0.2.14/24'
       set interfaces ethernet eth2 address '192.0.2.10/24'
       set interfaces ethernet eth2 address '192.0.2.11/24'
       set interfaces ethernet eth2 address '2001:db8::10/32'
       set interfaces ethernet eth2 address '2001:db8::12/32'"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": [
#         {
#             "ipv4": [
#                 {
#                     "address": "192.0.2.10/24"
#                 },
#                 {
#                     "address": "192.0.2.11/24"
#                 }
#             ],
#             "ipv6": [
#                 {
#                     "address": "2001:db8::10/32"
#                 },
#                 {
#                     "address": "2001:db8::12/32"
#                 }
#             ],
#             "name": "eth2"
#         },
#         {
#             "ipv4": [
#                 {
#                     "address": "192.0.2.14/24"
#                 }
#             ],
#             "name": "eth1"
#         },
#         {
#             "ipv4": [
#                 {
#                     "address": "dhcp"
#                 }
#             ],
#             "name": "eth0"
#         }
#     ]
```

## [Return Values](vyos_l3_interfaces_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["set interfaces ethernet eth1 192.0.2.14/2", "set interfaces ethernet eth3 vif 101 address 198.51.100.130/25"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)
- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
