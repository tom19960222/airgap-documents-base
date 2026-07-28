---
collection: ansible
version: "6"
title: "cisco.ios.ios_bgp module – Module to configure BGP protocol settings."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_bgp_module.html
fetched_at: 2026-07-27T16:55:07+00:00
---
# cisco.ios.ios_bgp module – Module to configure BGP protocol settings.

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
> To use it in a playbook, specify: `cisco.ios.ios_bgp`.

New in cisco.ios 1.0.0

- [DEPRECATED](ios_bgp_module.md#deprecated)
- [Synopsis](ios_bgp_module.md#synopsis)
- [Parameters](ios_bgp_module.md#parameters)
- [Notes](ios_bgp_module.md#notes)
- [Examples](ios_bgp_module.md#examples)
- [Return Values](ios_bgp_module.md#return-values)
- [Status](ios_bgp_module.md#status)

## [DEPRECATED](ios_bgp_module.md#id1)

Removed in:
:   major release after 2023-08-24

Why:
:   Newer and updated modules released with more functionality

Alternative:
:   ios_bgp_global

## [Synopsis](ios_bgp_module.md#id2)

- This module provides configuration management of global BGP parameters on devices running Cisco IOS

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_bgp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies the BGP related configuration. |
| **address_family**  list / elements=dictionary | Specifies BGP address family related configurations. |
| **afi**  string / required | Type of address family to configure.  Choices:   - `"ipv4"` - `"ipv6"` |
| **auto_summary**  boolean | Enable/disable automatic network number summarization.  Choices:   - `false` - `true` |
| **neighbors**  list / elements=dictionary | Specifies BGP neighbor related configurations in Address Family configuration mode. |
| **activate**  boolean | Enable the Address Family for this Neighbor.  Choices:   - `false` - `true` |
| **advertisement_interval**  integer | Minimum interval between sending BGP routing updates for this neighbor. |
| **maximum_prefix**  integer | Maximum number of prefixes to accept from this peer.  The range is from 1 to 2147483647. |
| **neighbor**  string / required | Neighbor router address. |
| **next_hop_self**  boolean | Enable/disable the next hop calculation for this neighbor.  Choices:   - `false` - `true` |
| **next_hop_unchanged**  boolean | Propagate next hop unchanged for iBGP paths to this neighbor.  Choices:   - `false` - `true` |
| **prefix_list_in**  string | Name of ip prefix-list to apply to incoming prefixes. |
| **prefix_list_out**  string | Name of ip prefix-list to apply to outgoing prefixes. |
| **remove_private_as**  boolean | Remove the private AS number from outbound updates.  Choices:   - `false` - `true` |
| **route_reflector_client**  boolean | Specify a neighbor as a route reflector client.  Choices:   - `false` - `true` |
| **route_server_client**  boolean | Specify a neighbor as a route server client.  Choices:   - `false` - `true` |
| **networks**  list / elements=dictionary | Specify Networks to announce via BGP.  For operation replace, this option is mutually exclusive with root level networks option. |
| **masklen**  integer | Subnet mask length for the Network to announce(e.g, 8, 16, 24, etc.). |
| **prefix**  string / required | Network ID to announce via BGP. |
| **route_map**  string | Route map to modify the attributes. |
| **redistribute**  list / elements=dictionary | Specifies the redistribute information from another routing protocol. |
| **id**  string | Identifier for the routing protocol for configuring redistribute information.  Valid for protocols ‘ospf’, ‘ospfv3’ and ‘eigrp’. |
| **metric**  integer | Specifies the metric for redistributed routes. |
| **protocol**  string / required | Specifies the protocol for configuring redistribute information.  Choices:   - `"ospf"` - `"ospfv3"` - `"eigrp"` - `"isis"` - `"static"` - `"connected"` - `"odr"` - `"lisp"` - `"mobile"` - `"rip"` |
| **route_map**  string | Specifies the route map reference. |
| **safi**  string | Specifies the type of cast for the address family.  Choices:   - `"flowspec"` - `"unicast"` ← (default) - `"multicast"` - `"labeled-unicast"` |
| **synchronization**  boolean | Enable/disable IGP synchronization.  Choices:   - `false` - `true` |
| **bgp_as**  integer / required | Specifies the BGP Autonomous System (AS) number to configure on the device. |
| **log_neighbor_changes**  boolean | Enable/disable logging neighbor up/down and reset reason.  Choices:   - `false` - `true` |
| **neighbors**  list / elements=dictionary | Specifies BGP neighbor related configurations. |
| **description**  string | Neighbor specific description. |
| **ebgp_multihop**  integer | Specifies the maximum hop count for EBGP neighbors not on directly connected networks.  The range is from 1 to 255. |
| **enabled**  boolean | Administratively shutdown or enable a neighbor.  Choices:   - `false` - `true` |
| **local_as**  integer | The local AS number for the neighbor. |
| **neighbor**  string / required | Neighbor router address. |
| **password**  string | Password to authenticate the BGP peer connection. |
| **peer_group**  string | Name of the peer group that the neighbor is a member of. |
| **remote_as**  integer / required | Remote AS of the BGP neighbor to configure. |
| **timers**  dictionary | Specifies BGP neighbor timer related configurations. |
| **holdtime**  integer / required | Interval (in seconds) after not receiving a keepalive message that IOS declares a peer dead.  The range is from 0 to 65535. |
| **keepalive**  integer / required | Frequency (in seconds) with which the device sends keepalive messages to its peer.  The range is from 0 to 65535. |
| **min_neighbor_holdtime**  integer | Interval (in seconds) specifying the minimum acceptable hold-time from a BGP neighbor.  The minimum acceptable hold-time must be less than, or equal to, the interval specified in the holdtime argument.  The range is from 0 to 65535. |
| **update_source**  string | Source of the routing updates. |
| **networks**  list / elements=dictionary | Specify Networks to announce via BGP.  For operation replace, this option is mutually exclusive with networks option under address_family.  For operation replace, if the device already has an address family activated, this option is not allowed. |
| **masklen**  integer | Subnet mask length for the Network to announce(e.g, 8, 16, 24, etc.). |
| **prefix**  string / required | Network ID to announce via BGP. |
| **route_map**  string | Route map to modify the attributes. |
| **router_id**  string | Configures the BGP routing process router-id value. |
| **operation**  string | Specifies the operation to be performed on the BGP process configured on the device.  In case of merge, the input configuration will be merged with the existing BGP configuration on the device.  In case of replace, if there is a diff between the existing configuration and the input configuration, the existing configuration will be replaced by the input configuration for every option that has the diff.  In case of override, all the existing BGP configuration will be removed from the device and replaced with the input configuration.  In case of delete the existing BGP configuration will be removed from the device.  Choices:   - `"merge"` ← (default) - `"replace"` - `"override"` - `"delete"` |

## [Notes](ios_bgp_module.md#id4)

> **Note:**
>
> - Tested against Cisco IOS Version 15.6(3)M2

## [Examples](ios_bgp_module.md#id5)

```yaml+jinja
- name: configure global bgp as 64496
  cisco.ios.ios_bgp:
    config:
      bgp_as: 64496
      router_id: 192.0.2.1
      log_neighbor_changes: true
      neighbors:
      - neighbor: 203.0.113.5
        remote_as: 64511
        timers:
          keepalive: 300
          holdtime: 360
          min_neighbor_holdtime: 360
      - neighbor: 198.51.100.2
        remote_as: 64498
      networks:
      - prefix: 198.51.100.0
        route_map: RMAP_1
      - prefix: 192.0.2.0
        masklen: 23
      address_family:
      - afi: ipv4
        safi: unicast
        redistribute:
        - protocol: ospf
          id: 223
          metric: 10
    operation: merge

- name: Configure BGP neighbors
  cisco.ios.ios_bgp:
    config:
      bgp_as: 64496
      neighbors:
      - neighbor: 192.0.2.10
        remote_as: 64496
        password: ansible
        description: IBGP_NBR_1
        ebgp_multihop: 100
        timers:
          keepalive: 300
          holdtime: 360
          min_neighbor_holdtime: 360
      - neighbor: 192.0.2.15
        remote_as: 64496
        description: IBGP_NBR_2
        ebgp_multihop: 150
    operation: merge

- name: Configure root-level networks for BGP
  cisco.ios.ios_bgp:
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

- name: Configure BGP neighbors under address family mode
  cisco.ios.ios_bgp:
    config:
      bgp_as: 64496
      address_family:
      - afi: ipv4
        safi: unicast
        neighbors:
        - neighbor: 203.0.113.10
          activate: yes
          maximum_prefix: 250
          advertisement_interval: 120
        - neighbor: 192.0.2.15
          activate: yes
          route_reflector_client: true
    operation: merge

- name: remove bgp as 64496 from config
  cisco.ios.ios_bgp:
    config:
      bgp_as: 64496
    operation: delete
```

## [Return Values](ios_bgp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["router bgp 64496", "bgp router-id 192.0.2.1", "bgp log-neighbor-changes", "neighbor 203.0.113.5 remote-as 64511", "neighbor 203.0.113.5 timers 300 360 360", "neighbor 198.51.100.2 remote-as 64498", "network 198.51.100.0 route-map RMAP_1", "network 192.0.2.0 mask 255.255.254.0", "address-family ipv4", "redistribute ospf 223 metric 70", "exit-address-family"]` |

## [Status](ios_bgp_module.md#id7)

- This module will be removed in a major release after 2023-08-24.
  *[deprecated]*
- For more information see [DEPRECATED](ios_bgp_module.md#deprecated).

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
