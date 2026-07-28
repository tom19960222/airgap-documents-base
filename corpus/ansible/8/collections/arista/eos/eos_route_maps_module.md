---
collection: ansible
version: "8"
title: "arista.eos.eos_route_maps module – Manages Route Maps resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_route_maps_module.html
fetched_at: 2026-07-28T01:11:14+00:00
---
# arista.eos.eos_route_maps module – Manages Route Maps resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_route_maps`.

New in arista.eos 2.1.0

- [Synopsis](eos_route_maps_module.md#synopsis)
- [Parameters](eos_route_maps_module.md#parameters)
- [Notes](eos_route_maps_module.md#notes)
- [Examples](eos_route_maps_module.md#examples)

## [Synopsis](eos_route_maps_module.md#id1)

- This module configures and manages the attributes of Route Mapd on Arista EOS platforms.

Aliases: route_maps

## [Parameters](eos_route_maps_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of route-map options |
| **entries**  list / elements=dictionary | Route Map entries. |
| **action**  string | Action for matching routes  **Choices:**   - `"deny"` - `"permit"` |
| **continue_sequence**  integer | Route map entry sequence number. |
| **description**  string | Description for the route map. |
| **match**  dictionary | Route map match rules. |
| **aggregate_role**  dictionary | Role in BGP contributor-aggregate relation. |
| **contributor**  boolean | BGP aggregate’s contributor.  **Choices:**   - `false` - `true` |
| **route_map**  string | Route map to apply against the aggregate route. |
| **as**  integer | BGP AS number. |
| **as_path**  dictionary | Set as-path. |
| **length**  string | Specify as-path length ( with comparison operators like <= 60 and >= 40 ). |
| **path_list**  string | AS path list name. |
| **community**  dictionary | BGP community attribute. |
| **community_list**  string | list of community names (in csv format). |
| **exact_match**  boolean | Do exact matching of communities.  **Choices:**   - `false` - `true` |
| **instances**  string | Match number of community instances ( with comparison operators like <= 60 and >= 40 ). |
| **extcommunity**  dictionary | extended community list name. |
| **community_list**  string | list of community names (in csv format). |
| **exact_match**  boolean | Do exact matching of communities.  **Choices:**   - `false` - `true` |
| **interface**  string | interface name. |
| **invert_result**  dictionary | Invert match result. |
| **aggregate_role**  dictionary | Role in BGP contributor-aggregate relation. |
| **contributor**  boolean | BGP aggregate’s contributor.  **Choices:**   - `false` - `true` |
| **route_map**  string | Route map to apply against the aggregate route. |
| **as_path**  dictionary | Set as-path. |
| **length**  string | Specify as-path length ( with comparison operators like <= 60 and >= 40 ). |
| **path_list**  string | AS path list name. |
| **community**  dictionary | BGP community attribute. |
| **community_list**  string | list of community names (in csv format). |
| **exact_match**  boolean | Do exact matching of communities.  **Choices:**   - `false` - `true` |
| **instances**  string | Match number of community instances ( with comparison operators like <= 60 and >= 40 ). |
| **extcommunity**  dictionary | extended community list name. |
| **community_list**  string | list of community names (in csv format). |
| **exact_match**  boolean | Do exact matching of communities.  **Choices:**   - `false` - `true` |
| **large_community**  dictionary | extended community list name. |
| **community_list**  string | list of community names (in csv format). |
| **exact_match**  boolean | Do exact matching of communities.  **Choices:**   - `false` - `true` |
| **ip**  dictionary | Set IP specific information. |
| **address**  dictionary | next hop destination. |
| **access_list**  string | ip access-list. |
| **dynamic**  boolean | Configure dynamic prefix-list.  **Choices:**   - `false` - `true` |
| **prefix_list**  string | Prefix list. |
| **next_hop**  string | next hop prefix list. |
| **resolved_next_hop**  string | Route resolved prefix list. |
| **ipv6**  dictionary | Set IPv6 specific information. |
| **address**  dictionary | next hop destination. |
| **access_list**  string | ip access-list. |
| **dynamic**  boolean | Configure dynamic prefix-list.  **Choices:**   - `false` - `true` |
| **prefix_list**  string | Prefix list. |
| **next_hop**  string | next hop prefix list. |
| **resolved_next_hop**  string | Route resolved prefix list. |
| **isis_level**  string | IS-IS level. |
| **large_community**  dictionary | extended community list name. |
| **community_list**  string | list of community names (in csv format). |
| **exact_match**  boolean | Do exact matching of communities.  **Choices:**   - `false` - `true` |
| **local_preference**  integer | BGP local preference. |
| **metric**  integer | Route metric. |
| **metric_type**  string | Route metric type.  **Choices:**   - `"type-1"` - `"type-2"` |
| **route_type**  string | Route type |
| **router_id**  string | Router ID. |
| **source_protocol**  string | Source routing protocol, |
| **tag**  integer | Route tag |
| **sequence**  integer | Index in the sequence. |
| **set**  dictionary | set route attributes. |
| **as_path**  dictionary | Set as-path. |
| **match**  dictionary | Match the entire as-path. |
| **as_number**  string | as number to use (includes auto;in csv format) |
| **none**  boolean | Remove matching AS numbers  **Choices:**   - `false` - `true` |
| **prepend**  dictionary | Prepend to the as-path. |
| **as_number**  string | as number to prepend (includes auto;in csv format) |
| **last_as**  integer | The number of times to prepend the last AS number. |
| **bgp**  integer | BGP AS path multipath weight. |
| **community_attributes**  dictionary | BGP community attribute. |
| **community**  dictionary | community attributes. |
| **additive**  boolean | Add to existing community.  **Choices:**   - `false` - `true` |
| **delete**  boolean | Delete matching communities.  **Choices:**   - `false` - `true` |
| **graceful_shutdown**  boolean | Gracefully shutdown.  **Choices:**   - `false` - `true` |
| **internet**  boolean | Internet community  **Choices:**   - `false` - `true` |
| **list**  string | community list name. |
| **local_as**  boolean | Do not send outside local AS.  **Choices:**   - `false` - `true` |
| **no_advertise**  boolean | Do not advertise to any peer.  **Choices:**   - `false` - `true` |
| **no_export**  boolean | Do not export to next AS.  **Choices:**   - `false` - `true` |
| **number**  string | community number (in csv format). |
| **graceful_shutdown**  boolean | Graceful shutdown  **Choices:**   - `false` - `true` |
| **none**  boolean | No community attribute.  **Choices:**   - `false` - `true` |
| **distance**  integer | Set protocol independent distance. |
| **evpn**  boolean | Keep the next hop when advertising to eBGP peers.  **Choices:**   - `false` - `true` |
| **extcommunity**  dictionary | BGP extended community attribute. |
| **lbw**  dictionary | Link bandwith values. |
| **aggregate**  boolean | Aggregate Link Bandwidth.  **Choices:**   - `false` - `true` |
| **divide**  string | Divide Link Bandwidth.  **Choices:**   - `"equal"` - `"ration"` |
| **value**  string | Link Bandwidth extended community value. |
| **none**  boolean | No attribute.  **Choices:**   - `false` - `true` |
| **rt**  dictionary | Route target extended community |
| **additive**  boolean | Add to the existing community.  **Choices:**   - `false` - `true` |
| **delete**  boolean | Delete matching communities.  **Choices:**   - `false` - `true` |
| **vpn**  string | VPN extended community. |
| **soo**  dictionary | Site-of-Origin extended community. |
| **additive**  boolean | Add to the existing community.  **Choices:**   - `false` - `true` |
| **delete**  boolean | Delete matching communities.  **Choices:**   - `false` - `true` |
| **vpn**  string | VPN extended community. |
| **ip**  dictionary | Set IP specific information. |
| **address**  string | next hop address. |
| **peer_address**  boolean | Use BGP peering addr as next-hop.  **Choices:**   - `false` - `true` |
| **unchanged**  boolean | Keep the next hop when advertising to eBGP peer  **Choices:**   - `false` - `true` |
| **ipv6**  dictionary | Set IPv6 specific information. |
| **address**  string | next hop address. |
| **peer_address**  boolean | Use BGP peering addr as next-hop.  **Choices:**   - `false` - `true` |
| **unchanged**  boolean | Keep the next hop when advertising to eBGP peer  **Choices:**   - `false` - `true` |
| **isis_level**  string | IS-IS level. |
| **local_preference**  integer | BGP local preference. |
| **metric**  dictionary | Route metric. |
| **add**  string | Add igp-metric / igp-nexthop-cost  **Choices:**   - `"igp-metric"` - `"igp-nexthop-cost"` |
| **igp_param**  string | IGP parameter  **Choices:**   - `"igp-metric"` - `"igp-nexthop-cost"` |
| **value**  string | metric value to add or subtract(with +/- sign). |
| **metric_type**  string | Route metric type.  **Choices:**   - `"type-1"` - `"type-2"` |
| **nexthop**  dictionary | Route next hop. |
| **max_metric**  boolean | Set IGP max metric value.  **Choices:**   - `false` - `true` |
| **value**  integer | IGP metric value. |
| **origin**  string | Set bgp origin.  **Choices:**   - `"egp"` - `"igp"` - `"incomplete"` |
| **segment_index**  integer | MPLS Segment-routing Segment Index. |
| **tag**  integer | Route tag |
| **weight**  integer | BGP weight. |
| **source**  dictionary | Rename/Copy configuration |
| **action**  string | rename or copy configuration  **Choices:**   - `"rename"` - `"copy"` |
| **overwrite**  boolean | if true, overwrite existing config.  **Choices:**   - `false` - `true` |
| **source_map_name**  string | Source route map name. |
| **statement**  string | statement name |
| **sub_route_map**  dictionary | Sub route map |
| **invert_result**  boolean | Invert sub route map result  **Choices:**   - `false` - `true` |
| **name**  string | sub route map name |
| **route_map**  string | Route map name. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section route-map**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](eos_route_maps_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](eos_platform_options.md).

## [Examples](eos_route_maps_module.md#id4)

```yaml+jinja
# Using merged
# Before state
# veos#show running-config | section route-map
# veos#

- name: Merge provided configuration with device configuration
  arista.eos.eos_route_maps:
    config:
      - route_map: "mapmerge"
        entries:
          - description: "merged_map"
            action: "permit"
            sequence: 10
            match:
              router_id: 22
          - description: "newmap"
            action: "deny"
            sequence: 25
            continue_sequence: 45
            match:
              interface: "Ethernet1"
      - route_map: "mapmerge2"
        entries:
          - sub_route_map:
              name: "mapmerge"
            action: "deny"
            sequence: 45
            set:
              metric:
                value: 25
                add: "igp-metric"
              as_path:
                prepend:
                  last_as: 2
            match:
              ipv6:
                resolved_next_hop: "list1"
    state: merged

# After State:

# veos#show running-config | section route-map
# route-map mapmerge permit 10
#    description merged_map
#    match router-id prefix-list 22
# !
# route-map mapmerge deny 25
#    description newmap
#    match interface Ethernet1
#    continue 45
# !
# route-map mapmerge2 deny 45
#    match ipv6 resolved-next-hop prefix-list list1
#    sub-route-map mapmerge
#    set metric 25 +igp-metric
#    set as-path prepend last-as 2
# !
# route-map test permit 10
# veos#

# Module Execution:

#  "after": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "description": "merged_map",
#                     "match": {
#                         "router_id": "22"
#                     },
#                     "sequence": 10
#                 },
#                 {
#                     "action": "deny",
#                     "continue_sequence": 45,
#                     "description": "newmap",
#                     "match": {
#                         "interface": "Ethernet1"
#                     },
#                     "sequence": 25
#                 }
#             ],
#             "route_map": "mapmerge"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "list1"
#                         }
#                     },
#                     "sequence": 45,
#                     "set": {
#                         "as_path": {
#                             "prepend": {
#                                 "last_as": 2
#                             }
#                         },
#                         "metric": {
#                             "add": "igp-metric",
#                             "value": "25"
#                         }
#                     },
#                     "sub_route_map": {
#                         "name": "mapmerge"
#                     }
#                 }
#             ],
#             "route_map": "mapmerge2"
#         }
#     ],
#     "before": {},
#     "changed": true,
#     "commands": [
#         "route-map mapmerge permit 10",
#         "match router-id prefix-list 22",
#         "description merged_map",
#         "route-map mapmerge deny 25",
#         "match interface Ethernet1",
#         "description newmap",
#         "continue 45",
#         "route-map mapmerge2 deny 45",
#         "match ipv6 resolved-next-hop prefix-list list1",
#         "set metric 25 +igp-metric",
#         "set as-path prepend last-as 2",
#         "sub-route-map mapmerge"
#     ],
#

# Using replaced:

# Before State:

# veos#show running-config | section route-map
# route-map mapmerge permit 10
#    description merged_map
#    match router-id prefix-list 22
# !
# route-map mapmerge deny 25
#    description newmap
#    match interface Ethernet1
#    continue 45
# !
# route-map mapmerge2 deny 45
#    match ipv6 resolved-next-hop prefix-list list1
#    sub-route-map mapmerge
#    set metric 25 +igp-metric
#    set as-path prepend last-as 2
# !
# veos#

- name: Replace
  arista.eos.eos_route_maps:
    config:
      - route_map: "mapmerge"
        entries:
          - action: "permit"
            sequence: 10
            match:
              ipv6:
                resolved_next_hop: "listr"
          - action: "deny"
            sequence: 90
            set:
              extcommunity:
                rt:
                  vpn: "22:11"
                  delete: true
              ip:
                unchanged: true
    state: replaced

# After State:

# veos#show running-config | section route-map
# route-map mapmerge permit 10
#    match ipv6 resolved-next-hop prefix-list listr
# !
# route-map mapmerge deny 25
#    description newmap
#    match interface Ethernet1
#    continue 45
# !
# route-map mapmerge deny 90
#    set ip next-hop unchanged
#    set extcommunity rt 22:11 delete
# !
# route-map mapmerge2 deny 45
#    match ipv6 resolved-next-hop prefix-list list1
#    sub-route-map mapmerge
#    set metric 25 +igp-metric
#    set as-path prepend last-as 2
# !
#
# Module Execution:
#
#     "after": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "listr"
#                         }
#                     },
#                     "sequence": 10
#                 },
#                 {
#                     "action": "deny",
#                     "continue_sequence": 45,
#                     "description": "newmap",
#                     "match": {
#                         "interface": "Ethernet1"
#                     },
#                     "sequence": 25
#                 },
#                 {
#                     "action": "deny",
#                     "sequence": 90,
#                     "set": {
#                         "extcommunity": {
#                             "rt": {
#                                 "delete": true,
#                                 "vpn": "22:11"
#                             }
#                         },
#                         "ip": {
#                             "unchanged": true
#                         }
#                     }
#                 }
#             ],
#             "route_map": "mapmerge"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "list1"
#                         }
#                     },
#                     "sequence": 45,
#                     "set": {
#                         "as_path": {
#                             "prepend": {
#                                 "last_as": 2
#                             }
#                         },
#                         "metric": {
#                             "add": "igp-metric",
#                             "value": "25"
#                         }
#                     },
#                     "sub_route_map": {
#                         "name": "mapmerge"
#                     }
#                 }
#             ],
#             "route_map": "mapmerge2"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "sequence": 10
#                 }
#             ],
#             "route_map": "test"
#         }
#     ],
#     "before": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "description": "merged_map",
#                     "match": {
#                         "router_id": "22"
#                     },
#                     "sequence": 10
#                 },
#                 {
#                     "action": "deny",
#                     "continue_sequence": 45,
#                     "description": "newmap",
#                     "match": {
#                         "interface": "Ethernet1"
#                     },
#                     "sequence": 25
#                 }
#             ],
#             "route_map": "mapmerge"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "list1"
#                         }
#                     },
#                     "sequence": 45,
#                     "set": {
#                         "as_path": {
#                             "prepend": {
#                                 "last_as": 2
#                             }
#                         },
#                         "metric": {
#                             "add": "igp-metric",
#                             "value": "25"
#                         }
#                     },
#                     "sub_route_map": {
#                         "name": "mapmerge"
#                     }
#                 }
#             ],
#             "route_map": "mapmerge2"
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "route-map mapmerge permit 10",
#         "match ipv6 resolved-next-hop prefix-list listr",
#         "no match router-id prefix-list 22",
#         "no description",
#         "route-map mapmerge deny 90",
#         "set extcommunity rt 22:11 delete",
#         "set ip next-hop unchanged"
#     ],
#
#
# Using Overridden:

# Before state:
# veos#show running-config | section route-map
# route-map mapmerge permit 10
#    match ipv6 resolved-next-hop prefix-list listr
# !
# route-map mapmerge deny 25
#    description newmap
#    match interface Ethernet1
#    continue 45
# !
# route-map mapmerge deny 90
#    set ip next-hop unchanged
#    set extcommunity rt 22:11 delete
# !
# route-map mapmerge2 deny 45
#    match ipv6 resolved-next-hop prefix-list list1
#    sub-route-map mapmerge
#    set metric 25 +igp-metric
#    set as-path prepend last-as 2
# !
# route-map test permit 10
# veos#

- name: Override
  arista.eos.eos_route_maps:
    config:
      - route_map: "mapmerge"
        entries:
          - action: "permit"
            sequence: 10
            match:
              ipv6:
                resolved_next_hop: "listr"
          - action: "deny"
            sequence: 90
            set:
              metric:
                igp_param: "igp-nexthop-cost"
    state: overridden

# After State:

# veos#show running-config | section route-map
# route-map mapmerge permit 10
#    match ipv6 resolved-next-hop prefix-list listr
# !
# route-map mapmerge deny 90
#    set metric igp-nexthop-cost
# veos#
#
#
#    "after": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "listr"
#                         }
#                     },
#                     "sequence": 10
#                 },
#                 {
#                     "action": "deny",
#                     "sequence": 90,
#                     "set": {
#                         "metric": {
#                             "igp_param": "igp-nexthop-cost"
#                         }
#                     }
#                 }
#             ],
#             "route_map": "mapmerge"
#         }
#     ],
#     "before": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "listr"
#                         }
#                     },
#                     "sequence": 10
#                 },
#                 {
#                     "action": "deny",
#                     "continue_sequence": 45,
#                     "description": "newmap",
#                     "match": {
#                         "interface": "Ethernet1"
#                     },
#                     "sequence": 25
#                 },
#                 {
#                     "action": "deny",
#                     "sequence": 90,
#                     "set": {
#                         "extcommunity": {
#                             "rt": {
#                                 "delete": true,
#                                 "vpn": "22:11"
#                             }
#                         },
#                         "ip": {
#                             "unchanged": true
#                         }
#                     }
#                 }
#             ],
#             "route_map": "mapmerge"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "list1"
#                         }
#                     },
#                     "sequence": 45,
#                     "set": {
#                         "as_path": {
#                             "prepend": {
#                                 "last_as": 2
#                             }
#                         },
#                         "metric": {
#                             "add": "igp-metric",
#                             "value": "25"
#                         }
#                     },
#                     "sub_route_map": {
#                         "name": "mapmerge"
#                     }
#                 }
#             ],
#             "route_map": "mapmerge2"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "sequence": 10
#                 }
#             ],
#             "route_map": "test"
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "no route-map mapmerge deny 25",
#         "no route-map mapmerge2 deny 45",
#         "no route-map test permit 10",
#         "route-map mapmerge deny 90",
#         "set metric igp-nexthop-cost",
#         "no set ip next-hop unchanged",
#         "no set extcommunity rt 22:11 delete"
#     ],
#
# Using deleted:
# Before State:

# veos#show running-config | section route-map
# route-map mapmerge permit 10
#    description merged_map
#    match router-id prefix-list 22
#    match ipv6 resolved-next-hop prefix-list listr
# !
# route-map mapmerge deny 25
#    description newmap
#    match interface Ethernet1
#    continue 45
# !
# route-map mapmerge deny 90
#    set metric igp-nexthop-cost
# !
# route-map mapmerge2 deny 45
#    match ipv6 resolved-next-hop prefix-list list1
#    sub-route-map mapmerge
#    set metric 25 +igp-metric
#    set as-path prepend last-as 2
# veos#

- name: Delete route-map
  arista.eos.eos_route_maps:
    config:
      - route_map: "mapmerge"
    state: deleted
  become: true
  tags:
    - deleted1

# After State:

# veos#show running-config | section route-map
# route-map mapmerge2 deny 45
#    match ipv6 resolved-next-hop prefix-list list1
#    sub-route-map mapmerge
#    set metric 25 +igp-metric
#    set as-path prepend last-as 2
# veos#
#
# Module Execution:
#
# "after": [
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "list1"
#                         }
#                     },
#                     "sequence": 45,
#                     "set": {
#                         "as_path": {
#                             "prepend": {
#                                 "last_as": 2
#                             }
#                         },
#                         "metric": {
#                             "add": "igp-metric",
#                             "value": "25"
#                         }
#                     },
#                     "sub_route_map": {
#                         "name": "mapmerge"
#                     }
#                 }
#             ],
#             "route_map": "mapmerge2"
#         }
#     ],
#     "before": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "description": "merged_map",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "listr"
#                         },
#                         "router_id": "22"
#                     },
#                     "sequence": 10
#                 },
#                 {
#                     "action": "deny",
#                     "continue": 45,
#                     "description": "newmap",
#                     "match": {
#                         "interface": "Ethernet1"
#                     },
#                     "sequence": 25
#                 },
#                 {
#                     "action": "deny",
#                     "sequence": 90,
#                     "set": {
#                         "metric": {
#                             "igp_param": "igp-nexthop-cost"
#                         }
#                     }
#                 }
#             ],
#             "route_map": "mapmerge"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "list1"
#                         }
#                     },
#                     "sequence": 45,
#                     "set": {
#                         "as_path": {
#                             "prepend": {
#                                 "last_as": 2
#                             }
#                         },
#                         "metric": {
#                             "add": "igp-metric",
#                             "value": "25"
#                         }
#                     },
#                     "sub_route_map": {
#                         "name": "mapmerge"
#                     }
#                 }
#             ],
#             "route_map": "mapmerge2"
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "no route-map mapmerge"
#     ],

# Using deleted to delete all route-maps:

# Before State:

# veos#show running-config | section route-map
# route-map mapmerge permit 10
#    description merged_map
#    match router-id prefix-list 22
# !
# route-map mapmerge deny 25
#    description newmap
#    match interface Ethernet1
#    continue 45
# !
# route-map mapmerge2 deny 45
#    match ipv6 resolved-next-hop prefix-list list1
#    sub-route-map mapmerge
#    set metric 25 +igp-metric
#    set as-path prepend last-as 2
# veos#

- name: Delete all route-maps
  arista.eos.eos_route_maps:
    state: deleted

# After State:
# ------------

# veos#show running-config | section route-map
# veos#
#
# Module Execution:
#
# "after": {},
#     "before": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "description": "merged_map",
#                     "match": {
#                         "router_id": "22"
#                     },
#                     "sequence": 10
#                 },
#                 {
#                     "action": "deny",
#                     "continue": 45,
#                     "description": "newmap",
#                     "match": {
#                         "interface": "Ethernet1"
#                     },
#                     "sequence": 25
#                 }
#             ],
#             "route_map": "mapmerge"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "list1"
#                         }
#                     },
#                     "sequence": 45,
#                     "set": {
#                         "as_path": {
#                             "prepend": {
#                                 "last_as": 2
#                             }
#                         },
#                         "metric": {
#                             "add": "igp-metric",
#                             "value": "25"
#                         }
#                     },
#                     "sub_route_map": {
#                         "name": "mapmerge"
#                     }
#                 }
#             ],
#             "route_map": "mapmerge2"
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "no route-map mapmerge",
#         "no route-map mapmerge2"
#     ],

# Using gathered:

# Device configs:

# veos#show running-config | section route-map
# route-map mapmerge permit 10
#    description merged_map
#    match router-id prefix-list 22
# !
# route-map mapmerge deny 25
#    description newmap
#    match interface Ethernet1
#    continue 45
# !
# route-map mapmerge2 deny 45
#    match ipv6 resolved-next-hop prefix-list list1
#    sub-route-map mapmerge
#    set metric 25 +igp-metric
#    set as-path prepend last-as 2
# veos#

- name: gather configs
  arista.eos.eos_route_maps:
    state: gathered

# Module Execution:
#   "gathered": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "description": "merged_map",
#                     "match": {
#                         "router_id": "22"
#                     },
#                     "sequence": 10
#                 },
#                 {
#                     "action": "deny",
#                     "continue_sequence": 45,
#                     "description": "newmap",
#                     "match": {
#                         "interface": "Ethernet1"
#                     },
#                     "sequence": 25
#                 }
#             ],
#             "route_map": "mapmerge"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "list1"
#                         }
#                     },
#                     "sequence": 45,
#                     "set": {
#                         "as_path": {
#                             "prepend": {
#                                 "last_as": 2
#                             }
#                         },
#                         "metric": {
#                             "add": "igp-metric",
#                             "value": "25"
#                         }
#                     },
#                     "sub_route_map": {
#                         "name": "mapmerge"
#                     }
#                 }
#             ],
#             "route_map": "mapmerge2"
#         }
#     ],

# Using rendered:

- name: Render provided configuration
  arista.eos.eos_route_maps:
    config:
      - route_map: "mapmerge"
        entries:
          - description: "merged_map"
            action: "permit"
            sequence: 10
            match:
              router_id: 22
            set:
              bgp: 20
          - description: "newmap"
            action: "deny"
            sequence: 25
            continue_sequence: 45
            match:
              interface: "Ethernet1"
      - route_map: "mapmerge2"
        entries:
          - sub_route_map:
              name: "mapmerge"
            action: "deny"
            sequence: 45
            set:
              metric:
                value: 25
                add: "igp-metric"
              as_path:
                prepend:
                  last_as: 2
            match:
              ipv6:
                resolved_next_hop: "list1"
    state: rendered

# Task output:
# ------------

# "rendered": [
#         "route-map mapmerge permit 10",
#         "match router-id prefix-list 22",
#         "set bgp bestpath as-path weight 20",
#         "description merged_map",
#         "route-map mapmerge deny 25",
#         "match interface Ethernet1",
#         "description newmap",
#         "continue 45",
#         "route-map mapmerge2 deny 45",
#         "match ipv6 resolved-next-hop prefix-list list1",
#         "set metric 25 +igp-metric",
#         "set as-path prepend last-as 2",
#         "sub-route-map mapmerge"
#     ]

# Using parsed:

# parsed.cfg
# route-map mapmerge permit 10
#    description merged_map
#    match router-id prefix-list 22
#    set bgp bestpath as-path weight 20
# !
# route-map mapmerge deny 25
#    description newmap
#    match interface Ethernet1
#    continue 45
# !
# route-map mapmerge2 deny 45
#    match ipv6 resolved-next-hop prefix-list list1
#    sub-route-map mapmerge
#    set metric 25 +igp-metric
#    set as-path prepend last-as 2

- name: parse configs
  arista.eos.eos_route_maps:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# Module Execution:
# "parsed": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "description": "merged_map",
#                     "match": {
#                         "router_id": "22"
#                     },
#                     "sequence": 10,
#                     "set": {
#                         "bgp": 20
#                     }
#                 },
#                 {
#                     "action": "deny",
#                     "continue_sequence": 45,
#                     "description": "newmap",
#                     "match": {
#                         "interface": "Ethernet1"
#                     },
#                     "sequence": 25
#                 }
#             ],
#             "route_map": "mapmerge"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "match": {
#                         "ipv6": {
#                             "resolved_next_hop": "list1"
#                         }
#                     },
#                     "sequence": 45,
#                     "set": {
#                         "as_path": {
#                             "prepend": {
#                                 "last_as": 2
#                             }
#                         },
#                         "metric": {
#                             "add": "igp-metric",
#                             "value": "25"
#                         }
#                     },
#                     "sub_route_map": {
#                         "name": "mapmerge"
#                     }
#                 }
#             ],
#             "route_map": "mapmerge2"
#         }
#     ]
```

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
