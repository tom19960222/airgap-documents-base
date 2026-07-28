---
collection: ansible
version: "6"
title: "arista.eos.eos_bgp module – (deprecated, removed after 2023-01-29) Configure global BGP protocol settings on Arista EOS."
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_bgp_module.html
fetched_at: 2026-07-27T16:45:07+00:00
---
# arista.eos.eos_bgp module – (deprecated, removed after 2023-01-29) Configure global BGP protocol settings on Arista EOS.

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/arista/eos) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_bgp`.

New in arista.eos 1.0.0

- [DEPRECATED](eos_bgp_module.md#deprecated)
- [Synopsis](eos_bgp_module.md#synopsis)
- [Parameters](eos_bgp_module.md#parameters)
- [Notes](eos_bgp_module.md#notes)
- [Examples](eos_bgp_module.md#examples)
- [Return Values](eos_bgp_module.md#return-values)
- [Status](eos_bgp_module.md#status)

## [DEPRECATED](eos_bgp_module.md#id1)

Removed in:
:   major release after 2023-01-01

Why:
:   Updated module released with more functionality.

Alternative:
:   eos_bgp_global

## [Synopsis](eos_bgp_module.md#id2)

- This module provides configuration management of global BGP parameters on Arista EOS devices.

## [Parameters](eos_bgp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Specifies the BGP related configuration. |
| **address_family**  list / elements=dictionary | Specifies BGP address family related configurations. |
| **afi**  string / required | Type of address family to configure.  Choices:   - `"ipv4"` - `"ipv6"` |
| **neighbors**  list / elements=dictionary | Specifies BGP neighbor related configurations in Address Family configuration mode. |
| **activate**  boolean | Enable the Address Family for this Neighbor.  Choices:   - `false` - `true` |
| **default_originate**  boolean | Originate default route to this neighbor.  Choices:   - `false` - `true` |
| **graceful_restart**  boolean | Enable/disable graceful restart mode for this neighbor.  Choices:   - `false` - `true` |
| **neighbor**  string / required | Neighbor router address. |
| **weight**  integer | Assign weight for routes learnt from this neighbor.  The range is from 0 to 65535 |
| **networks**  list / elements=dictionary | Specify Networks to announce via BGP.  For operation replace, this option is mutually exclusive with root level networks option. |
| **masklen**  integer | Subnet mask length for the Network to announce(e.g, 8, 16, 24, etc.). |
| **prefix**  string / required | Network ID to announce via BGP. |
| **route_map**  string | Route map to modify the attributes. |
| **redistribute**  list / elements=dictionary | Specifies the redistribute information from another routing protocol. |
| **protocol**  string / required | Specifies the protocol for configuring redistribute information.  Choices:   - `"ospfv3"` - `"ospf"` - `"isis"` - `"static"` - `"connected"` - `"rip"` |
| **route_map**  string | Specifies the route map reference. |
| **bgp_as**  integer / required | Specifies the BGP Autonomous System (AS) number to configure on the device. |
| **log_neighbor_changes**  boolean | Enable/disable logging neighbor up/down and reset reason.  Choices:   - `false` - `true` |
| **neighbors**  list / elements=dictionary | Specifies BGP neighbor related configurations. |
| **description**  string | Neighbor specific description. |
| **ebgp_multihop**  integer | Specifies the maximum hop count for EBGP neighbors not on directly connected networks.  The range is from 1 to 255. |
| **enabled**  boolean | Administratively shutdown or enable a neighbor.  Choices:   - `false` - `true` |
| **maximum_prefix**  integer | Maximum number of prefixes to accept from this peer.  The range is from 0 to 4294967294. |
| **neighbor**  string / required | Neighbor router address. |
| **password**  string | Password to authenticate the BGP peer connection. |
| **peer_group**  string | Name of the peer group that the neighbor is a member of. |
| **remote_as**  integer / required | Remote AS of the BGP neighbor to configure. |
| **remove_private_as**  boolean | Remove the private AS number from outbound updates.  Choices:   - `false` - `true` |
| **route_reflector_client**  integer | Specify a neighbor as a route reflector client. |
| **timers**  dictionary | Specifies BGP neighbor timer related configurations. |
| **holdtime**  integer / required | Interval (in seconds) after not receiving a keepalive message that device declares a peer dead.  The range is from 3 to 7200.  Setting this value to 0 will not send keep-alives (hold forever). |
| **keepalive**  integer / required | Frequency (in seconds) with which the device sends keepalive messages to its peer.  The range is from 0 to 3600. |
| **update_source**  string | Source of the routing updates. |
| **networks**  list / elements=dictionary | Specify Networks to announce via BGP.  For operation replace, this option is mutually exclusive with networks option under address_family.  For operation replace, if the device already has an address family activated, this option is not allowed. |
| **masklen**  integer | Subnet mask length for the Network to announce(e.g, 8, 16, 24, etc.). |
| **prefix**  string / required | Network ID to announce via BGP. |
| **route_map**  string | Route map to modify the attributes. |
| **redistribute**  list / elements=dictionary | Specifies the redistribute information from another routing protocol. |
| **protocol**  string / required | Specifies the protocol for configuring redistribute information.  Choices:   - `"ospf"` - `"ospfv3"` - `"static"` - `"connected"` - `"rip"` - `"isis"` |
| **route_map**  string | Specifies the route map reference. |
| **router_id**  string | Configures the BGP routing process router-id value. |
| **operation**  string | Specifies the operation to be performed on the BGP process configured on the device.  In case of merge, the input configuration will be merged with the existing BGP configuration on the device.  In case of replace, if there is a diff between the existing configuration and the input configuration, the existing configuration will be replaced by the input configuration for every option that has the diff.  In case of override, all the existing BGP configuration will be removed from the device and replaced with the input configuration.  In case of delete the existing BGP configuration will be removed from the device.  Choices:   - `"merge"` ← (default) - `"replace"` - `"override"` - `"delete"` |

## [Notes](eos_bgp_module.md#id4)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F

## [Examples](eos_bgp_module.md#id5)

```yaml+jinja
- name: configure global bgp as 64496
  arista.eos.eos_bgp:
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
        - protocol: isis
          route_map: RMAP_1
    operation: merge
- name: Configure BGP neighbors
  arista.eos.eos_bgp:
    config:
      bgp_as: 64496
      neighbors:
      - neighbor: 192.0.2.10
        remote_as: 64496
        description: IBGP_NBR_1
        ebgp_multihop: 100
        timers:
          keepalive: 300
          holdtime: 360
      - neighbor: 192.0.2.15
        remote_as: 64496
        description: IBGP_NBR_2
        ebgp_multihop: 150
    operation: merge
- name: Configure root-level networks for BGP
  arista.eos.eos_bgp:
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
  arista.eos.eos_bgp:
    config:
      bgp_as: 64496
      address_family:
      - afi: ipv4
        neighbors:
        - neighbor: 203.0.113.10
          activate: yes
          default_originate: true
        - neighbor: 192.0.2.15
          activate: yes
          graceful_restart: true
    operation: merge
- name: remove bgp as 64496 from config
  arista.eos.eos_bgp:
    config:
      bgp_as: 64496
    operation: delete
```

## [Return Values](eos_bgp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["router bgp 64496", "bgp router-id 192.0.2.1", "bgp log-neighbor-changes", "neighbor 203.0.113.5 remote-as 64511", "neighbor 203.0.113.5 timers 300 360", "neighbor 198.51.100.2 remote-as 64498", "network 198.51.100.0 route-map RMAP_1", "network 192.0.2.0 mask 255.255.254.0", "address-family ipv4", "redistribute isis route-map RMAP_1", "exit-address-family"]` |

## [Status](eos_bgp_module.md#id7)

- This module will be removed in a major release after 2023-01-01.
  *[deprecated]*
- For more information see [DEPRECATED](eos_bgp_module.md#deprecated).

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
