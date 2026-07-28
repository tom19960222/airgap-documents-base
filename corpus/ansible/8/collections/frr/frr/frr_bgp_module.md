---
collection: ansible
version: "8"
title: "frr.frr.frr_bgp module – Configure global BGP settings on Free Range Routing(FRR)."
source_url: https://docs.ansible.com/projects/ansible/8/collections/frr/frr/frr_bgp_module.html
fetched_at: 2026-07-28T02:31:36+00:00
---
# frr.frr.frr_bgp module – Configure global BGP settings on Free Range Routing(FRR).

> **Note:**
>
> This module is part of the [frr.frr collection](https://galaxy.ansible.com/ui/repo/published/frr/frr/) (version 2.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install frr.frr`.
>
> To use it in a playbook, specify: `frr.frr.frr_bgp`.

New in frr.frr 1.0.0

- [Synopsis](frr_bgp_module.md#synopsis)
- [Parameters](frr_bgp_module.md#parameters)
- [Notes](frr_bgp_module.md#notes)
- [Examples](frr_bgp_module.md#examples)
- [Return Values](frr_bgp_module.md#return-values)

## [Synopsis](frr_bgp_module.md#id1)

- This module provides configuration management of global BGP parameters on devices running Free Range Routing(FRR).

Aliases: bgp

## [Parameters](frr_bgp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies the BGP related configuration. |
| **address_family**  list / elements=dictionary | Specifies BGP address family related configurations. |
| **afi**  string / required | Type of address family to configure.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **neighbors**  list / elements=dictionary | Specifies BGP neighbor related configurations in Address Family configuration mode. |
| **activate**  boolean | Enable the address family for this neighbor.  **Choices:**   - `false` - `true` |
| **maximum_prefix**  integer | Maximum number of prefixes to accept from this peer.  The range is from 1 to 4294967295. |
| **neighbor**  string / required | Neighbor router address. |
| **next_hop_self**  boolean | Enable/disable the next hop calculation for this neighbor.  **Choices:**   - `false` - `true` |
| **remove_private_as**  boolean | Remove the private AS number from outbound updates.  **Choices:**   - `false` - `true` |
| **route_reflector_client**  boolean | Specify a neighbor as a route reflector client.  **Choices:**   - `false` - `true` |
| **route_server_client**  boolean | Specify a neighbor as a route server client.  **Choices:**   - `false` - `true` |
| **networks**  list / elements=dictionary | Specify networks to announce via BGP.  For operation replace, this option is mutually exclusive with root level networks option. |
| **masklen**  integer / required | Subnet mask length for the network to announce(e.g, 8, 16, 24, etc.). |
| **prefix**  string / required | Network ID to announce via BGP. |
| **route_map**  string | Route map to modify the attributes. |
| **redistribute**  list / elements=dictionary | Specifies the redistribute information from another routing protocol. |
| **id**  string | Specifies the instance ID/table ID for this protocol  Valid for ospf and table |
| **metric**  integer | Specifies the metric for redistributed routes. |
| **protocol**  string / required | Specifies the protocol for configuring redistribute information.  **Choices:**   - `"ospf"` - `"ospf6"` - `"eigrp"` - `"isis"` - `"table"` - `"static"` - `"connected"` - `"sharp"` - `"nhrp"` - `"kernel"` - `"babel"` - `"rip"` |
| **route_map**  string | Specifies the route map reference. |
| **safi**  string | Specifies the type of cast for the address family.  **Choices:**   - `"flowspec"` - `"unicast"` ← (default) - `"multicast"` - `"labeled-unicast"` |
| **bgp_as**  integer / required | Specifies the BGP Autonomous System (AS) number to configure on the device. |
| **log_neighbor_changes**  boolean | Enable/disable logging neighbor up/down and reset reason.  **Choices:**   - `false` - `true` |
| **neighbors**  list / elements=dictionary | Specifies BGP neighbor related configurations. |
| **advertisement_interval**  integer | Minimum interval between sending BGP routing updates for this neighbor. |
| **description**  string | Neighbor specific description. |
| **ebgp_multihop**  integer | Specifies the maximum hop count for EBGP neighbors not on directly connected networks.  The range is from 1 to 255. |
| **enabled**  boolean | Administratively shutdown or enable a neighbor.  **Choices:**   - `false` - `true` |
| **local_as**  integer | The local AS number for the neighbor. |
| **neighbor**  string / required | Neighbor router address. |
| **password**  string | Password to authenticate the BGP peer connection. |
| **peer_group**  string | Name of the peer group that the neighbor is a member of. |
| **port**  integer | The TCP Port number to use for this neighbor.  The range is from 0 to 65535. |
| **remote_as**  integer / required | Remote AS of the BGP neighbor to configure. |
| **timers**  dictionary | Specifies BGP neighbor timer related configurations. |
| **holdtime**  integer / required | Interval (in seconds) after not receiving a keepalive message that FRR declares a peer dead.  The range is from 0 to 65535. |
| **keepalive**  integer / required | Frequency (in seconds) with which the FRR sends keepalive messages to its peer.  The range is from 0 to 65535. |
| **update_source**  string | Source of the routing updates. |
| **networks**  list / elements=dictionary | Specify networks to announce via BGP.  For operation replace, this option is mutually exclusive with networks option under address_family.  For operation replace, if the device already has an address family activated, this option is not allowed. |
| **masklen**  integer / required | Subnet mask length for the network to announce(e.g, 8, 16, 24, etc.). |
| **prefix**  string / required | Network ID to announce via BGP. |
| **route_map**  string | Route map to modify the attributes. |
| **router_id**  string | Configures the BGP routing process router-id value. |
| **operation**  string | Specifies the operation to be performed on the BGP process configured on the device.  In case of merge, the input configuration will be merged with the existing BGP configuration on the device.  In case of replace, if there is a diff between the existing configuration and the input configuration, the existing configuration will be replaced by the input configuration for every option that has the diff.  In case of override, all the existing BGP configuration will be removed from the device and replaced with the input configuration.  In case of delete the existing BGP configuration will be removed from the device.  **Choices:**   - `"merge"` ← (default) - `"replace"` - `"override"` - `"delete"` |

## [Notes](frr_bgp_module.md#id3)

> **Note:**
>
> - Tested against FRRouting 6.0.

## [Examples](frr_bgp_module.md#id4)

```yaml+jinja
- name: configure global bgp as 64496
  frr.frr.frr_bgp:
    config:
      bgp_as: 64496
      router_id: 192.0.2.1
      log_neighbor_changes: true
      neighbors:
      - neighbor: 192.51.100.1
        remote_as: 64497
        timers:
          keepalive: 120
          holdtime: 360
      - neighbor: 198.51.100.2
        remote_as: 64498
      networks:
      - prefix: 192.0.2.0
        masklen: 24
        route_map: RMAP_1
      - prefix: 198.51.100.0
        masklen: 24
      address_family:
      - afi: ipv4
        safi: unicast
        redistribute:
        - protocol: ospf
          id: 223
          metric: 10
    operation: merge

- name: Configure BGP neighbors
  frr.frr.frr_bgp:
    config:
      bgp_as: 64496
      neighbors:
      - neighbor: 192.0.2.10
        remote_as: 64496
        password: ansible
        description: IBGP_NBR_1
        timers:
          keepalive: 120
          holdtime: 360
      - neighbor: 192.0.2.15
        remote_as: 64496
        description: IBGP_NBR_2
        advertisement_interval: 120
    operation: merge

- name: Configure BGP neighbors under address family mode
  frr.frr.frr_bgp:
    config:
      bgp_as: 64496
      address_family:
      - afi: ipv4
        safi: multicast
        neighbors:
        - neighbor: 203.0.113.10
          activate: true
          maximum_prefix: 250

        - neighbor: 192.0.2.15
          activate: true
          route_reflector_client: true
    operation: merge

- name: Configure root-level networks for BGP
  frr.frr.frr_bgp:
    config:
      bgp_as: 64496
      networks:
      - prefix: 203.0.113.0
        masklen: 27
        route_map: RMAP_1
      - prefix: 203.0.113.32
        masklen: 27
        route_map: RMAP_2
    operation: merge

- name: remove bgp as 64496 from config
  frr.frr.frr_bgp:
    config:
      bgp_as: 64496
    operation: delete
```

## [Return Values](frr_bgp_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["router bgp 64496", "bgp router-id 192.0.2.1", "neighbor 192.51.100.1 remote-as 64497", "neighbor 192.51.100.1 timers 120 360", "neighbor 198.51.100.2 remote-as 64498", "address-family ipv4 unicast", "redistribute ospf 223 metric 10", "exit-address-family", "bgp log-neighbor-changes", "network 192.0.2.0/24 route-map RMAP_1", "network 198.51.100.0/24", "exit"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/frr.frr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/frr.frr)
