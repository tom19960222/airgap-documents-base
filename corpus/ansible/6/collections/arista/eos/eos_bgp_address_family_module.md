---
collection: ansible
version: "6"
title: "arista.eos.eos_bgp_address_family module – Manages BGP address family resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_bgp_address_family_module.html
fetched_at: 2026-07-27T16:45:08+00:00
---
# arista.eos.eos_bgp_address_family module – Manages BGP address family resource module

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
> To use it in a playbook, specify: `arista.eos.eos_bgp_address_family`.

New in arista.eos 1.4.0

- [Synopsis](eos_bgp_address_family_module.md#synopsis)
- [Parameters](eos_bgp_address_family_module.md#parameters)
- [Notes](eos_bgp_address_family_module.md#notes)
- [Examples](eos_bgp_address_family_module.md#examples)

## [Synopsis](eos_bgp_address_family_module.md#id1)

- This module configures and manages the attributes of BGP AF on Arista EOS platforms.

## [Parameters](eos_bgp_address_family_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | Configurations for BGP address family. |
| **address_family**  list / elements=dictionary | Enable address family and enter its config mode |
| **afi**  string | address family.  Choices:   - `"ipv4"` - `"ipv6"` - `"evpn"` |
| **bgp_params**  dictionary | BGP parameters. |
| **additional_paths**  string | BGP additional-paths commands  Choices:   - `"install"` - `"send"` - `"receive"` |
| **next_hop_address_family**  string | Next-hop address-family configuration  Choices:   - `"ipv6"` |
| **next_hop_unchanged**  boolean | Preserve original nexthop while advertising routes to eBGP peers.  Choices:   - `false` - `true` |
| **redistribute_internal**  boolean | Redistribute internal BGP routes.  Choices:   - `false` - `true` |
| **route**  string | Configure route-map for route installation. |
| **graceful_restart**  boolean | Enable graceful restart mode.  Choices:   - `false` - `true` |
| **neighbor**  list / elements=dictionary | Configure routing for a network. |
| **activate**  boolean | Activate neighbor in the address family.  Choices:   - `false` - `true` |
| **additional_paths**  string | BGP additional-paths commands.  Choices:   - `"send"` - `"receive"` |
| **default_originate**  dictionary | Originate default route to this neighbor. |
| **always**  boolean | Always originate default route to this neighbor.  Choices:   - `false` - `true` |
| **route_map**  string | Route map reference. |
| **encapsulation**  dictionary | Default transport encapsulation for neighbor. Applicable for evpn address-family. |
| **source_interface**  string | Source interface to update BGP next hop address. Applicable for mpls transport. |
| **transport**  string | MPLS/VXLAN transport.  Choices:   - `"mpls"` - `"vxlan"` |
| **graceful_restart**  boolean | Enable graceful restart mode.  Choices:   - `false` - `true` |
| **next_hop_address_family**  string | Next-hop address-family configuration  Choices:   - `"ipv6"` |
| **next_hop_unchanged**  boolean | Preserve original nexthop while advertising routes to eBGP peers.  Choices:   - `false` - `true` |
| **peer**  string | Neighbor address/ peer group name. |
| **prefix_list**  dictionary | Prefix list reference. |
| **direction**  string | Configure an inbound/outbound prefix-list.  Choices:   - `"in"` - `"out"` |
| **name**  string | prefix list name. |
| **route_map**  dictionary | Route map reference. |
| **direction**  string | Configure an inbound/outbound route-map.  Choices:   - `"in"` - `"out"` |
| **name**  string | Route map name. |
| **weight**  integer | Weight to assign. |
| **network**  list / elements=dictionary | configure routing for network. |
| **address**  string | network address. |
| **route_map**  string | Route map reference. |
| **redistribute**  list / elements=dictionary | Redistribute routes in to BGP. |
| **isis_level**  string | Applicable for isis routes. Specify isis route level.  Choices:   - `"level-1"` - `"level-2"` - `"level-1-2"` |
| **ospf_route**  string | ospf route options.  Choices:   - `"internal"` - `"external"` - `"nssa_external_1"` - `"nssa_external_2"` |
| **protocol**  string | Routes to be redistributed.  Choices:   - `"isis"` - `"ospfv3"` - `"dhcp"` |
| **route_map**  string | Route map reference. |
| **route_target**  dictionary | Route target. |
| **action**  string | Route action.  Choices:   - `"both"` - `"import"` - `"export"` |
| **imported_route**  boolean | Export routes imported from the same Afi/Safi  Choices:   - `false` - `true` |
| **route_map**  string | Name of a route map. |
| **target**  string | Route Target. |
| **type**  aliases: mode  string | Type of address fmaily  Choices:   - `"evpn"` - `"vpn-ipv4"` - `"vpn-ipv6"` |
| **safi**  string | Address family type for ipv4.  Choices:   - `"labeled-unicast"` - `"multicast"` |
| **vrf**  string | name of the VRF in which BGP will be configured. |
| **as_number**  string | Autonomous system number. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section bgp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Choices:   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](eos_bgp_address_family_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](eos_platform_options.md).

## [Examples](eos_bgp_address_family_module.md#id4)

```yaml+jinja
# Using merged

# Before state

# veos(config)#show running-config | section bgp
# veos(config)#

  - name: Merge provided configuration with device configuration
    arista.eos.eos_bgp_address_family:
      config:
        as_number: "10"
        address_family:
          - afi: "ipv4"
            redistribute:
              - protocol: "ospfv3"
                ospf_route: "external"
            network:
              - address: "1.1.1.0/24"
              - address: "1.5.1.0/24"
                route_map: "MAP01"
          - afi: "ipv6"
            bgp_params:
              additional_paths: "receive"
            neighbor:
              - peer: "peer2"
                default_originate:
                  always: True
          - afi: "ipv6"
            redistribute:
              - protocol: "isis"
                isis_level: "level-2"
            route_target:
              mode: "export"
              target: "33:11"
            vrf: "vrft"
      state: merged

# After state:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer group
#    neighbor peer2 maximum-routes 12000
#    neighbor 1.1.1.1 maximum-routes 12000
#    !
#    address-family ipv4
#       neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospfv3 match external
#    !
#    address-family ipv6
#       bgp additional-paths receive
#       neighbor peer2 activate
#       neighbor peer2 default-originate always
#    !
#    vrf vrft
#       address-family ipv6
#          route-target export 33:11
#          redistribute isis level-2
# veos(config-router-bgp)#

# Module Execution:

# "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "isis_level": "level-2",
#                         "protocol": "isis"
#                     }
#                 ],
#                 "route_target": {
#                     "mode": "export",
#                     "target": "33:11"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#         "router bgp 10",
#         "address-family ipv4",
#         "redistribute ospfv3 match external",
#         "network 1.1.1.0/24",
#         "network 1.5.1.0/24 route-map MAP01",
#         "exit",
#         "address-family ipv6",
#         "neighbor peer2 default-originate always",
#         "bgp additional-paths receive",
#         "exit",
#         "vrf vrft",
#         "address-family ipv6",
#         "redistribute isis level-2",
#         "route-target export 33:11",
#         "exit",
#         "exit"
#     ],

# Using replaced:

# Before State:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer group
#    neighbor peer2 maximum-routes 12000
#    neighbor 1.1.1.1 maximum-routes 12000
#    !
#    address-family ipv4
#       neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospfv3 match external
#    !
#    address-family ipv6
#       bgp additional-paths receive
#       neighbor peer2 activate
#       neighbor peer2 default-originate always
#    !
#    vrf vrft
#       address-family ipv6
#          route-target export 33:11
#          redistribute isis level-2
# veos(config-router-bgp)#
#

  - name: Replace
    arista.eos.eos_bgp_address_family:
      config:
        as_number: "10"
        address_family:
          - afi: "ipv6"
            vrf: "vrft"
            redistribute:
              - protocol: "ospfv3"
                ospf_route: "external"
          - afi: "ipv6"
            redistribute:
              - protocol: "isis"
                isis_level: "level-2"
      state: replaced

# After State:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer group
#    neighbor peer2 maximum-routes 12000
#    neighbor 1.1.1.1 maximum-routes 12000
#    !
#    address-family ipv4
#       neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospfv3 match external
#    !
#    address-family ipv6
#       neighbor peer2 default-originate always
#       redistribute isis level-2
#    !
#    vrf vrft
#       address-family ipv6
#          redistribute ospfv3 match external
# veos(config-router-bgp)#
#
#
# # Module Execution:
#
#     "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "neighbor": [
#                     {
#                         "activate": true,
#                         "peer": "1.1.1.1"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "isis_level": "level-2",
#                         "protocol": "isis"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ],
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "before": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "neighbor": [
#                     {
#                         "activate": true,
#                         "peer": "1.1.1.1"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "activate": true,
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "isis_level": "level-2",
#                         "protocol": "isis"
#                     }
#                 ],
#                 "route_target": {
#                     "mode": "export",
#                     "target": "33:11"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "changed": true,
#     "commands": [
#         "router bgp 10",
#         "vrf vrft",
#         "address-family ipv6",
#         "redistribute ospfv3 match external",
#         "no redistribute isis level-2",
#         "no route-target export 33:11",
#         "exit",
#         "exit",
#         "address-family ipv6",
#         "redistribute isis level-2",
#         "no neighbor peer2 activate",
#         "no bgp additional-paths receive",
#         "exit"
#     ],

# Using overridden (overriding af at global context):
# Before state:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer group
#    neighbor peer2 maximum-routes 12000
#    neighbor 1.1.1.1 maximum-routes 12000
#    !
#    address-family ipv4
#       neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospfv3 match external
#    !
#    address-family ipv6
#       neighbor peer2 default-originate always
#       redistribute isis level-2
#    !
#    vrf vrft
#       address-family ipv6
#          redistribute ospfv3 match external
# veos(config-router-bgp)#

  - name: Overridden
    arista.eos.eos_bgp_address_family:
      config:
        as_number: "10"
        address_family:
          - afi: "ipv4"
            bgp_params:
              additional_paths: "receive"
            neighbor:
              - peer: "peer2"
                default_originate:
                  always: True
      state: overridden

# After State:
# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer group
#    neighbor peer2 maximum-routes 12000
#    neighbor 1.1.1.1 maximum-routes 12000
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#    !
#    vrf vrft
#       address-family ipv6
#          redistribute ospfv3 match external
# veos(config-router-bgp)#
#
# Module Execution:
#
# "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ],
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "before": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "neighbor": [
#                     {
#                         "activate": true,
#                         "peer": "1.1.1.1"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "isis_level": "level-2",
#                         "protocol": "isis"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ],
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "changed": true,
#     "commands": [
#         "router bgp 10",
#         "address-family ipv4",
#         "no redistribute ospfv3 match external",
#         "no network 1.1.1.0/24",
#         "no network 1.5.1.0/24 route-map MAP01",
#         "neighbor peer2 default-originate always",
#         "no neighbor 1.1.1.1 activate",
#         "bgp additional-paths receive",
#         "exit",
#         "no address-family ipv6"
#     ],

# using Overridden (overridding af in vrf context):

# Before State:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer group
#    neighbor peer2 maximum-routes 12000
#    neighbor 1.1.1.1 maximum-routes 12000
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#       no neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospfv3 match external
#    !
#    address-family ipv6
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#    !
#    vrf vrft
#       address-family ipv6
#          route-target export 33:11
#          redistribute isis level-2
#          redistribute ospfv3 match external
# veos(config-router-bgp)#

  - name: Overridden
    arista.eos.eos_bgp_address_family:
      config:
        as_number: "10"
        address_family:
          - afi: "ipv4"
            bgp_params:
              additional_paths: "receive"
            neighbor:
              - peer: "peer2"
                default_originate:
                  always: True
            vrf: vrft
      state: overridden

# After State:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer group
#    neighbor peer2 maximum-routes 12000
#    neighbor 1.1.1.1 maximum-routes 12000
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospfv3 match external
#    !
#    address-family ipv6
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#    !
#    vrf vrft
#       address-family ipv4
#          bgp additional-paths receive
# veos(config-router-bgp)#
#
# Module Execution:
#
# "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "before": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "isis_level": "level-2",
#                         "protocol": "isis"
#                     },
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ],
#                 "route_target": {
#                     "mode": "export",
#                     "target": "33:11"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "changed": true,
#     "commands": [
#         "router bgp 10",
#         "vrf vrft",
#         "address-family ipv4",
#         "neighbor peer2 default-originate always",
#         "bgp additional-paths receive",
#         "exit",
#         "exit",
#         " vrf vrft",
#         "no address-family ipv6"
#     ],

# Using Deleted:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer group
#    neighbor peer2 maximum-routes 12000
#    neighbor 1.1.1.1 maximum-routes 12000
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#       no neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospfv3 match external
#    !
#    address-family ipv6
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#    !
#    vrf vrft
#       address-family ipv4
#          bgp additional-paths receive
# veos(config-router-bgp)#

  - name: Delete
    arista.eos.eos_bgp_address_family:
      config:
        as_number: "10"
        address_family:
          - afi: "ipv6"
            vrf: "vrft"
          - afi: "ipv6"
      state: deleted

# After State:

# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer group
#    neighbor peer2 maximum-routes 12000
#    neighbor 1.1.1.1 maximum-routes 12000
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#       no neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospfv3 match external
#    !
#    vrf vrft
#       address-family ipv4
#          bgp additional-paths receive
# veos(config-router-bgp)#
#
# Module Execution:
#
# "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },
#     "before": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },

# Using parsed:

# parsed_bgp_address_family.cfg :

# router bgp 10
#    neighbor n2 peer group
#    neighbor n2 next-hop-unchanged
#    neighbor n2 maximum-routes 12000
#    neighbor peer2 peer group
#    neighbor peer2 maximum-routes 12000
#    network 1.1.1.0/24
#    network 1.5.1.0/24 route-map MAP01
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#       redistribute ospfv3 match external
#    !
#    address-family ipv6
#       no bgp additional-paths receive
#       neighbor n2 next-hop-unchanged
#       redistribute isis level-2
#    !
#    vrf bgp_10
#       ip access-group acl01
#       ucmp fec threshold trigger 33 clear 22 warning-only
#       !
#       address-family ipv4
#          route-target import 20:11
#    !
#    vrf vrft
#       address-family ipv4
#          bgp additional-paths receive
#       !
#       address-family ipv6
#          redistribute ospfv3 match external

  - name: parse configs
    arista.eos.eos_bgp_address_family:
      running_config: "{{ lookup('file', './parsed_bgp_address_family.cfg') }}"
      state: parsed

# Module Execution:
# "parsed": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "neighbor": [
#                     {
#                         "next_hop_unchanged": true,
#                         "peer": "n2"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "isis_level": "level-2",
#                         "protocol": "isis"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv4",
#                 "route_target": {
#                     "mode": "import",
#                     "target": "20:11"
#                 },
#                 "vrf": "bgp_10"
#             },
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "vrf": "vrft"
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ],
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     }
# }

# Using gathered:

# Device config:
# veos(config-router-bgp)#show running-config | section bgp
# router bgp 10
#    neighbor peer2 peer group
#    neighbor peer2 maximum-routes 12000
#    neighbor 1.1.1.1 maximum-routes 12000
#    !
#    address-family ipv4
#       bgp additional-paths receive
#       neighbor peer2 default-originate always
#       no neighbor 1.1.1.1 activate
#       network 1.1.1.0/24
#       network 1.5.1.0/24 route-map MAP01
#       redistribute ospfv3 match external
#    !
#    vrf vrft
#       address-family ipv4
#          bgp additional-paths receive
# veos(config-router-bgp)#

  - name: gather configs
    arista.eos.eos_bgp_address_family:
      state: gathered

# Module Execution:
# "gathered": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "neighbor": [
#                     {
#                         "default_originate": {
#                             "always": true
#                         },
#                         "peer": "peer2"
#                     }
#                 ],
#                 "network": [
#                     {
#                         "address": "1.1.1.0/24"
#                     },
#                     {
#                         "address": "1.5.1.0/24",
#                         "route_map": "MAP01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "ospf_route": "external",
#                         "protocol": "ospfv3"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv4",
#                 "bgp_params": {
#                     "additional_paths": "receive"
#                 },
#                 "vrf": "vrft"
#             }
#         ],
#         "as_number": "10"
#     },

# using rendered:

  - name:  Render
    arista.eos.eos_bgp_address_family:
      config:
        as_number: "10"
        address_family:
          - afi: "ipv4"
            redistribute:
              - protocol: "ospfv3"
                ospf_route: "external"
            network:
              - address: "1.1.1.0/24"
              - address: "1.5.1.0/24"
                route_map: "MAP01"
          - afi: "ipv6"
            bgp_params:
              additional_paths: "receive"
            neighbor:
              - peer: "peer2"
                default_originate:
                  always: True
          - afi: "ipv6"
            redistribute:
              - protocol: "isis"
                isis_level: "level-2"
            route_target:
              mode: "export"
              target: "33:11"
            vrf: "vrft"

      state: rendered

# Module Execution:

# "rendered": [
#         "router bgp 10",
#         "address-family ipv4",
#         "redistribute ospfv3 match external",
#         "network 1.1.1.0/24",
#         "network 1.5.1.0/24 route-map MAP01",
#         "exit",
#         "address-family ipv6",
#         "neighbor peer2 default-originate always",
#         "bgp additional-paths receive",
#         "exit",
#         "vrf vrft",
#         "address-family ipv6",
#         "redistribute isis level-2",
#         "route-target export 33:11",
#         "exit",
#         "exit"
#     ]
#
```

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
