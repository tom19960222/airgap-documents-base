---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_dhcp_relay module – Manage DHCP and DHCPv6 relay configurations on SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_dhcp_relay_module.html
fetched_at: 2026-07-28T02:03:35+00:00
---
# dellemc.enterprise_sonic.sonic_dhcp_relay module – Manage DHCP and DHCPv6 relay configurations on SONiC

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_dhcp_relay`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_dhcp_relay_module.md#synopsis)
- [Parameters](sonic_dhcp_relay_module.md#parameters)
- [Examples](sonic_dhcp_relay_module.md#examples)
- [Return Values](sonic_dhcp_relay_module.md#return-values)

## [Synopsis](sonic_dhcp_relay_module.md#id1)

- This module provides configuration management of DHCP and DHCPv6 relay parameters on Layer 3 interfaces of devices running SONiC.
- Layer 3 interface and VRF name need to be created earlier in the device.

## [Parameters](sonic_dhcp_relay_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies the DHCP and DHCPv6 relay configurations. |
| **ipv4**  dictionary | DHCP relay configurations to be set for the interface mentioned in name option. |
| **circuit_id**  string | Specifies the DHCP relay circuit-id format.  `%h:%p` - Hostname followed by interface name eg. sonic:Vlan100  `%i` - Name of the physical interface eg. Eth1/2  `%p` - Name of the interface eg. Vlan100  **Choices:**   - `"%h:%p"` - `"%i"` - `"%p"` |
| **link_select**  boolean | Enable link selection suboption.  **Choices:**   - `false` - `true` |
| **max_hop_count**  integer | Specifies the maximum hop count for DHCP relay packets.  The range is from 1 to 16. |
| **policy_action**  string | Specifies the policy for handling of DHCP relay options.  **Choices:**   - `"append"` - `"discard"` - `"replace"` |
| **server_addresses**  list / elements=dictionary | List of DHCP server IPv4 addresses. |
| **address**  string | IPv4 address of the DHCP server. |
| **source_interface**  string | Specifies the DHCP relay source interface. |
| **vrf_name**  string | Specifies name of the VRF in which the DHCP server resides.  This option is not used with state *deleted*. |
| **vrf_select**  boolean | Enable VRF selection suboption.  **Choices:**   - `false` - `true` |
| **ipv6**  dictionary | DHCPv6 relay configurations to be set for the interface mentioned in name option. |
| **max_hop_count**  integer | Specifies the maximum hop count for DHCPv6 relay packets.  The range is from 1 to 16. |
| **server_addresses**  list / elements=dictionary | List of DHCPv6 server IPv6 addresses. |
| **address**  string | IPv6 address of the DHCPv6 server. |
| **source_interface**  string | Specifies the DHCPv6 relay source interface. |
| **vrf_name**  string | Specifies name of the VRF in which the DHCPv6 server resides.  This option is used only with state *merged*. |
| **vrf_select**  boolean | Enable VRF selection suboption.  **Choices:**   - `false` - `true` |
| **name**  string / required | Full name of the Layer 3 interface, i.e. Eth1/1. |
| **state**  string | The state of the configuration after module completion.  `merged` - Merges provided DHCP and DHCPv6 relay configuration with on-device configuration.  `deleted` - Deletes on-device DHCP and DHCPv6 relay configuration.  `replaced` - Replaces on-device DHCP and DHCPv6 relay configuration of the specified interfaces with provided configuration.  `overridden` - Overrides all on-device DHCP and DHCPv6 relay configurations with the provided configuration.  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"replaced"` - `"overridden"` |

## [Examples](sonic_dhcp_relay_module.md#id3)

```yaml+jinja
# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
#  ip dhcp-relay max-hop-count 5
#  ip dhcp-relay vrf-select
#  ip dhcp-relay policy-action append
#  ipv6 address 81::1/24
#  ipv6 dhcp-relay 91::1 92::1
#  ipv6 dhcp-relay max-hop-count 5
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
#  ip dhcp-relay source-interface Vlan100
#  ip dhcp-relay link-select
#  ip dhcp-relay circuit-id %h:%p
# !

  - name: Delete DHCP and DHCPv6 relay configurations
    dellemc.enterprise_sonic.sonic_dhcp_relay:
      config:
        - name: 'Eth1/1'
          ipv4:
            server_addresses:
              - address: '92.1.1.1'
            vrf_select: true
            max_hop_count: 5
          ipv6:
            server_addresses:
              - address: '91::1'
              - address: '92::1'
        - name: 'Eth1/2'
          ipv4:
            server_addresses:
              - address: '71.1.1.1'
              - address: '72.1.1.1'
            source_interface: 'Vlan100'
            link_select: true
            circuit_id: '%h:%p'
      state: deleted

# After State:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ip dhcp-relay 91.1.1.1 vrf VrfReg1
#  ip dhcp-relay policy-action append
#  ipv6 address 81::1/24
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 73.1.1.1
# !

# Using deleted
#
# NOTE: Support is provided in the dhcp_relay resource module for deletion of all attributes for a
# given address family (IPv4 or IPv6) by using a "special" YAML sequence specifying a server address list
# containing a single "blank" IP address under the target address family. The following example shows
# a task using this syntax for deletion of all DHCP (IPv4) configurations for an interface, but the
# equivalent syntax is supported for DHCPv6 (IPv6) as well.
#
# Before State:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
#  ip dhcp-relay max-hop-count 5
#  ip dhcp-relay vrf-select
#  ip dhcp-relay policy-action append
#  ipv6 address 81::1/24
#  ipv6 dhcp-relay 91::1 92::1
#  ipv6 dhcp-relay max-hop-count 5
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
#  ip dhcp-relay source-interface Vlan100
#  ip dhcp-relay link-select
#  ip dhcp-relay circuit-id %h:%p
# !

  - name: Delete all IPv4 DHCP relay configurations for interface Eth1/1
    dellemc.enterprise_sonic.sonic_dhcp_relay:
      config:
        - name: 'Eth1/1'
          ipv4:
            server_addresses:
              - address:
      state: deleted

# After State:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ipv6 address 81::1/24
#  ipv6 dhcp-relay 91::1 92::1
#  ipv6 dhcp-relay max-hop-count 5
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
#  ip dhcp-relay source-interface Vlan100
#  ip dhcp-relay link-select
#  ip dhcp-relay circuit-id %h:%p
# !

# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
#  ip dhcp-relay max-hop-count 5
#  ip dhcp-relay vrf-select
#  ip dhcp-relay policy-action append
#  ipv6 address 81::1/24
#  ipv6 dhcp-relay 91::1 92::1
#  ipv6 dhcp-relay max-hop-count 5
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
#  ip dhcp-relay source-interface Vlan100
#  ip dhcp-relay link-select
#  ip dhcp-relay circuit-id %h:%p
# !

  - name: Delete all DHCP and DHCPv6 relay configurations for interface Eth1/1
    dellemc.enterprise_sonic.sonic_dhcp_relay:
      config:
        - name: 'Eth1/1'
      state: deleted

# After State:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ipv6 address 81::1/24
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
#  ip dhcp-relay source-interface Vlan100
#  ip dhcp-relay link-select
#  ip dhcp-relay circuit-id %h:%p
# !

# Using deleted
#
# Before State:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
#  ip dhcp-relay max-hop-count 5
#  ip dhcp-relay vrf-select
#  ip dhcp-relay policy-action append
#  ipv6 address 81::1/24
#  ipv6 dhcp-relay 91::1 92::1
#  ipv6 dhcp-relay max-hop-count 5
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
#  ip dhcp-relay source-interface Vlan100
#  ip dhcp-relay link-select
#  ip dhcp-relay circuit-id %h:%p
# !

  - name: Delete all DHCP and DHCPv6 relay configurations
    dellemc.enterprise_sonic.sonic_dhcp_relay:
      config:
      state: deleted

# After State:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ipv6 address 81::1/24
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
# !

# Using merged
#
# Before State:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ipv6 address 81::1/24
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 71.1.1.1 72.1.1.1
# !

  - name: Add DHCP and DHCPv6 relay configurations
    dellemc.enterprise_sonic.sonic_dhcp_relay:
      config:
        - name: 'Eth1/1'
          ipv4:
            server_addresses:
              - address: '91.1.1.1'
              - address: '92.1.1.1'
            vrf_name: 'VrfReg1'
            vrf_select: true
            max_hop_count: 5
            policy_action: 'append'
          ipv6:
            server_addresses:
              - address: '91::1'
              - address: '92::1'
            max_hop_count: 5
        - name: 'Eth1/2'
          ipv4:
            server_addresses:
              - address: '73.1.1.1'
            source_interface: 'Vlan100'
            link_select: true
            circuit_id: '%h:%p'
      state: merged

# After State:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
#  ip dhcp-relay max-hop-count 5
#  ip dhcp-relay vrf-select
#  ip dhcp-relay policy-action append
#  ipv6 address 81::1/24
#  ipv6 dhcp-relay 91::1 92::1
#  ipv6 dhcp-relay max-hop-count 5
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
#  ip dhcp-relay source-interface Vlan100
#  ip dhcp-relay link-select
#  ip dhcp-relay circuit-id %h:%p
# !

# Using replaced
#
# Before State:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
#  ip dhcp-relay max-hop-count 5
#  ip dhcp-relay vrf-select
#  ip dhcp-relay policy-action append
#  ipv6 address 81::1/24
#  ipv6 dhcp-relay 91::1 92::1
#  ipv6 dhcp-relay max-hop-count 5
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
#  ip dhcp-relay source-interface Vlan100
#  ip dhcp-relay link-select
#  ip dhcp-relay circuit-id %h:%p
#  ipv6 address 61::1/24
#  ipv6 dhcp-relay 71::1 72::1
# !
# interface Eth1/3
#  mtu 9100
#  speed 400000
#  fec RS
#  shutdown
#  ip address 41.1.1.1/24
#  ip dhcp-relay 51.1.1.1 52.1.1.1
#  ip dhcp-relay circuit-id %h:%p
#  ipv6 address 41::1/24
#  ipv6 dhcp-relay 51::1 52::1
# !

  - name: Replace DHCP and DHCPv6 relay configurations of specified interfaces
    dellemc.enterprise_sonic.sonic_dhcp_relay:
      config:
        - name: 'Eth1/1'
          ipv4:
            server_addresses:
              - address: '91.1.1.1'
              - address: '93.1.1.1'
              - address: '95.1.1.1'
            vrf_name: 'VrfReg1'
            vrf_select: true
          ipv6:
            server_addresses:
              - address: '93::1'
              - address: '94::1'
            source_interface: 'Vlan100'
        - name: 'Eth1/2'
          ipv4:
            server_addresses:
              - address: '73.1.1.1'
            circuit_id: '%h:%p'
      state: replaced

# After State:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ip dhcp-relay 91.1.1.1 93.1.1.1 95.1.1.1 vrf VrfReg1
#  ip dhcp-relay vrf-select
#  ipv6 address 81::1/24
#  ipv6 dhcp-relay 93::1 94::1
#  ipv6 dhcp-relay source-interface Vlan100
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 73.1.1.1
#  ip dhcp-relay circuit-id %h:%p
#  ipv6 address 61::1/24
# !
# interface Eth1/3
#  mtu 9100
#  speed 400000
#  fec RS
#  shutdown
#  ip address 41.1.1.1/24
#  ip dhcp-relay 51.1.1.1 52.1.1.1
#  ip dhcp-relay circuit-id %h:%p
#  ipv6 address 41::1/24
#  ipv6 dhcp-relay 51::1 52::1
# !

# Using overridden
#
# Before State:
# -------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ip dhcp-relay 91.1.1.1 92.1.1.1 vrf VrfReg1
#  ip dhcp-relay max-hop-count 5
#  ip dhcp-relay vrf-select
#  ip dhcp-relay policy-action append
#  ipv6 address 81::1/24
#  ipv6 dhcp-relay 91::1 92::1
#  ipv6 dhcp-relay max-hop-count 5
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 71.1.1.1 72.1.1.1 73.1.1.1
#  ip dhcp-relay source-interface Vlan100
#  ip dhcp-relay link-select
#  ip dhcp-relay circuit-id %h:%p
#  ipv6 address 61::1/24
#  ipv6 dhcp-relay 71::1 72::1
# !
# interface Eth1/3
#  mtu 9100
#  speed 400000
#  fec RS
#  shutdown
#  ip address 41.1.1.1/24
#  ip dhcp-relay 51.1.1.1 52.1.1.1
#  ip dhcp-relay circuit-id %h:%p
#  ipv6 address 41::1/24
#  ipv6 dhcp-relay 51::1 52::1
# !

  - name: Override DHCP and DHCPv6 relay configurations
    dellemc.enterprise_sonic.sonic_dhcp_relay:
      config:
        - name: 'Eth1/1'
          ipv4:
            server_addresses:
              - address: '91.1.1.1'
              - address: '93.1.1.1'
              - address: '95.1.1.1'
            vrf_name: 'VrfReg1'
            vrf_select: true
          ipv6:
            server_addresses:
              - address: '93::1'
              - address: '94::1'
            source_interface: 'Vlan100'
        - name: 'Eth1/2'
          ipv4:
            server_addresses:
              - address: '73.1.1.1'
            circuit_id: '%h:%p'
      state: overridden

# After State:
# ------------
#
# sonic# show running-configuration interface
# !
# interface Eth1/1
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 81.1.1.1/24
#  ip dhcp-relay 91.1.1.1 93.1.1.1 95.1.1.1 vrf VrfReg1
#  ip dhcp-relay vrf-select
#  ipv6 address 81::1/24
#  ipv6 dhcp-relay 93::1 94::1
#  ipv6 dhcp-relay source-interface Vlan100
# !
# interface Eth1/2
#  mtu 9100
#  speed 400000
#  fec RS
#  no shutdown
#  ip address 61.1.1.1/24
#  ip dhcp-relay 73.1.1.1
#  ip dhcp-relay circuit-id %h:%p
#  ipv6 address 61::1/24
# !
# interface Eth1/3
#  mtu 9100
#  speed 400000
#  fec RS
#  shutdown
#  ip address 41.1.1.1/24
#  ipv6 address 41::1/24
# !
```

## [Return Values](sonic_dhcp_relay_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Arun Saravanan Balachandran (@ArunSaravananBalachandran)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
