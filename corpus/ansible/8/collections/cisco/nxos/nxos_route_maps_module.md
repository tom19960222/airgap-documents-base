---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_route_maps module – Route Maps resource module."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_route_maps_module.html
fetched_at: 2026-07-28T01:39:06+00:00
---
# cisco.nxos.nxos_route_maps module – Route Maps resource module.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_route_maps`.

New in cisco.nxos 2.2.0

- [Synopsis](nxos_route_maps_module.md#synopsis)
- [Parameters](nxos_route_maps_module.md#parameters)
- [Notes](nxos_route_maps_module.md#notes)
- [Examples](nxos_route_maps_module.md#examples)
- [Return Values](nxos_route_maps_module.md#return-values)

## [Synopsis](nxos_route_maps_module.md#id1)

- This module manages route maps configuration on devices running Cisco NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: route_maps

## [Parameters](nxos_route_maps_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of route-map configuration. |
| **entries**  list / elements=dictionary | List of entries (identified by sequence number) for this route-map. |
| **action**  string | Route map denies or permits set operations.  **Choices:**   - `"deny"` - `"permit"` |
| **continue_sequence**  integer | Continue on a different entry within the route-map. |
| **description**  string | Description of the route-map. |
| **match**  dictionary | Match values from routing table. |
| **as_number**  dictionary | Match BGP peer AS number. |
| **as_path_list**  list / elements=string | AS path access list name. |
| **asn**  list / elements=string | AS number. |
| **as_path**  list / elements=string | Match BGP AS path access-list. |
| **community**  dictionary | Match BGP community list. |
| **community_list**  list / elements=string | Community list. |
| **exact_match**  boolean | Do exact matching of communities.  **Choices:**   - `false` - `true` |
| **evpn**  dictionary | Match BGP EVPN Routes. |
| **route_types**  list / elements=string | Match route type for evpn route. |
| **extcommunity**  dictionary | Match BGP community list. |
| **exact_match**  boolean | Do exact matching of extended communities.  **Choices:**   - `false` - `true` |
| **extcommunity_list**  list / elements=string | Extended Community list. |
| **interfaces**  list / elements=string | Match first hop interface of route. |
| **ip**  dictionary | Configure IP specific information. |
| **address**  dictionary | Match address of route or match packet. |
| **access_list**  string | IP access-list name (for use in route-maps for PBR only). |
| **prefix_lists**  list / elements=string | Match entries of prefix-lists. |
| **multicast**  dictionary | Match multicast attributes. |
| **group**  dictionary | Multicast Group prefix.  Mutually exclusive with group_range. |
| **prefix**  string | IPv4 group prefix. |
| **group_range**  dictionary | Multicast Group address range.  Mutually exclusive with group. |
| **first**  string | First Group address. |
| **last**  string | Last Group address. |
| **rp**  dictionary | Rendezvous point. |
| **prefix**  string | IPv4 rendezvous prefix. |
| **rp_type**  string | Multicast rendezvous point type.  **Choices:**   - `"ASM"` - `"Bidir"` |
| **source**  string | Multicast source address. |
| **next_hop**  dictionary | Match next-hop address of route. |
| **prefix_lists**  list / elements=string | Match entries of prefix-lists. |
| **route_source**  dictionary | Match advertising source address of route. |
| **prefix_lists**  list / elements=string | Match entries of prefix-lists. |
| **ipv6**  dictionary | Configure IPv6 specific information. |
| **address**  dictionary | Match address of route or match packet. |
| **access_list**  string | IP access-list name (for use in route-maps for PBR only). |
| **prefix_lists**  list / elements=string | Match entries of prefix-lists. |
| **multicast**  dictionary | Match multicast attributes. |
| **group**  dictionary | Multicast Group prefix.  Mutually exclusive with group_range. |
| **prefix**  string | IPv4 group prefix. |
| **group_range**  dictionary | Multicast Group address range.  Mutually exclusive with group. |
| **first**  string | First Group address. |
| **last**  string | Last Group address. |
| **rp**  dictionary | Rendezvous point. |
| **prefix**  string | IPv4 rendezvous prefix. |
| **rp_type**  string | Multicast rendezvous point type.  **Choices:**   - `"ASM"` - `"Bidir"` |
| **source**  string | Multicast source address. |
| **next_hop**  dictionary | Match next-hop address of route. |
| **prefix_lists**  list / elements=string | Match entries of prefix-lists. |
| **route_source**  dictionary | Match advertising source address of route. |
| **prefix_lists**  list / elements=string | Match entries of prefix-lists. |
| **mac_list**  list / elements=string | Match entries of mac-lists. |
| **metric**  list / elements=integer | Match metric of route. |
| **ospf_area**  list / elements=integer | Match ospf area. |
| **route_types**  list / elements=string | Match route-type of route.  **Choices:**   - `"external"` - `"inter-area"` - `"internal"` - `"intra-area"` - `"level-1"` - `"level-2"` - `"local"` - `"nssa-external"` - `"type-1"` - `"type-2"` |
| **source_protocol**  list / elements=string | Match source protocol. |
| **tags**  list / elements=integer | Match tag of route. |
| **sequence**  integer | Sequence to insert to/delete from existing route-map entry. |
| **set**  dictionary | Set values in destination routing protocol. |
| **as_path**  dictionary | Prepend string for a BGP AS-path attribute. |
| **prepend**  dictionary | Prepend to the AS-Path. |
| **as_number**  list / elements=string | AS number. |
| **last_as**  integer | Number of last-AS prepends. |
| **tag**  boolean | Set the tag as an AS-path attribute.  **Choices:**   - `false` - `true` |
| **comm_list**  string | Set BGP community list (for deletion). |
| **community**  dictionary | Set BGP community attribute. |
| **additive**  boolean | Add to existing community.  **Choices:**   - `false` - `true` |
| **graceful_shutdown**  boolean | Graceful Shutdown (well-known community).  **Choices:**   - `false` - `true` |
| **internet**  boolean | Internet (well-known community).  **Choices:**   - `false` - `true` |
| **local_as**  boolean | Do not send outside local AS (well-known community).  **Choices:**   - `false` - `true` |
| **no_advertise**  boolean | Do not advertise to any peer (well-known community).  **Choices:**   - `false` - `true` |
| **no_export**  boolean | Do not export to next AS (well-known community).  **Choices:**   - `false` - `true` |
| **number**  list / elements=string | Community number aa:nn format |
| **dampening**  dictionary | Set BGP route flap dampening parameters. |
| **half_life**  integer | Half-life time for the penalty. |
| **max_suppress_time**  integer | Maximum suppress time for stable route. |
| **start_reuse_route**  integer | Value to start reusing a route. |
| **start_suppress_route**  integer | Value to start suppressing a route. |
| **distance**  dictionary | Configure administrative distance. |
| **igp_ebgp_routes**  integer | Administrative distance for IGP or EBGP routes |
| **internal_routes**  integer | Distance for internal routes. |
| **local_routes**  integer | Distance for local routes. |
| **evpn**  dictionary | Set BGP EVPN Routes. |
| **gateway_ip**  dictionary | Set gateway IP for type 5 EVPN routes.  Cannot set ip and use-nexthop in the same route-map sequence. |
| **ip**  string | Gateway IP address. |
| **use_nexthop**  boolean | Use nexthop address as gateway IP.  **Choices:**   - `false` - `true` |
| **extcomm_list**  string | Set BGP extcommunity list (for deletion). |
| **forwarding_address**  boolean | Set the forwarding address.  **Choices:**   - `false` - `true` |
| **ip**  dictionary | Configure IP features. |
| **address**  dictionary | Specify IP address. |
| **prefix_list**  string | Name of prefix list (Max Size 63). |
| **next_hop**  dictionary | Set next-hop IP address (for policy-based routing) |
| **address**  string | Set space-separated list of next-hop IP addresses. Address ordering is important. Also don`t use unnecessary spaces. |
| **drop_on_fail**  boolean | Drop packets instead of using default routing when the configured next hop becomes unreachable  **Choices:**   - `false` ← (default) - `true` |
| **force_order**  boolean | Enable next-hop ordering as specified in the address parameter.  **Choices:**   - `false` ← (default) - `true` |
| **load_share**  boolean | Enable traffic load balancing across a maximum of 32 next-hop addresses  **Choices:**   - `false` ← (default) - `true` |
| **peer_address**  boolean | BGP prefix next hop is set to the local address of the peer.  If no next hop is set in the route map, the next hop is set to the one stored in the path.  **Choices:**   - `false` - `true` |
| **redist_unchanged**  boolean | Set for next-hop address conservation for non-local generated routes.  Used with redistribute command. Available to maintain BGP routing compliant with RFC 4271 on Nexus OS.  **Choices:**   - `false` - `true` |
| **unchanged**  boolean | Set for next-hop address conservation in eBGP outgoing updates  **Choices:**   - `false` - `true` |
| **verify_availability**  list / elements=dictionary | Set next-hop ip address tracking with IP SLA |
| **address**  string / required | Set one next-hop address |
| **drop_on_fail**  boolean | Drop packets instead of using default routing when the configured next hop becomes unreachable  **Choices:**   - `false` ← (default) - `true` |
| **force_order**  boolean | Enable next-hop ordering as specified in the address parameter.  **Choices:**   - `false` ← (default) - `true` |
| **load_share**  boolean | Enable traffic load balancing across a maximum of 32 next-hop addresses  **Choices:**   - `false` ← (default) - `true` |
| **track**  integer / required | Set track number |
| **precedence**  string | Set precedence field. |
| **ipv6**  dictionary | Configure IPv6 features. |
| **address**  dictionary | Specify IP address. |
| **prefix_list**  string | Name of prefix list (Max Size 63). |
| **precedence**  string | Set precedence field. |
| **label_index**  integer | Set Segment Routing (SR) label index of route. |
| **level**  string | Where to import route.  **Choices:**   - `"level-1"` - `"level-1-2"` - `"level-2"` |
| **local_preference**  integer | BGP local preference path attribute. |
| **metric**  dictionary | Set metric for destination routing protocol. |
| **bandwidth**  integer | Metric value or Bandwidth in Kbits per second (Max Size 11). |
| **igrp_delay_metric**  integer | IGRP delay metric. |
| **igrp_effective_bandwidth_metric**  integer | IGRP Effective bandwidth metric (Loading) 255 is 100%. |
| **igrp_mtu**  integer | IGRP MTU of the path. |
| **igrp_reliability_metric**  integer | IGRP reliability metric where 255 is 100 percent reliable. |
| **metric_type**  string | Type of metric for destination routing protocol.  **Choices:**   - `"external"` - `"internal"` - `"type-1"` - `"type-2"` |
| **nssa_only**  boolean | OSPF NSSA Areas.  **Choices:**   - `false` - `true` |
| **null_interface**  string | Output Null interface. |
| **origin**  string | BGP origin code.  **Choices:**   - `"egp"` - `"igp"` - `"incomplete"` |
| **path_selection**  string | Path selection criteria for BGP.  **Choices:**   - `"all"` - `"backup"` - `"best2"` - `"multipaths"` |
| **tag**  integer | Tag value for destination routing protocol. |
| **weight**  integer | BGP weight for routing table. |
| **route_map**  string | Route-map name. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ‘^route-map’**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  With state *replaced*, for the listed route-maps, sequences that are in running-config but not in the task are negated.  With state *overridden*, all route-maps that are in running-config but not in the task are negated.  Please refer to examples for more details.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](nxos_route_maps_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 9.3.6.
> - Unsupported for Cisco MDS
> - This module works with connection `network_cli` and `httpapi`.

## [Examples](nxos_route_maps_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# nxos-9k-rdo# show running-config | section "^route-map"
# nxos-9k-rdo#

- name: Merge the provided configuration with the existing running configuration
  cisco.nxos.nxos_route_maps:
    config:
      - route_map: rmap1
        entries:
          - sequence: 10
            action: permit
            description: rmap1-10-permit
            match:
              ip:
                address:
                  access_list: acl_1
              as_path: Allow40
              as_number:
                asn: 65564

          - sequence: 20
            action: deny
            description: rmap1-20-deny
            match:
              community:
                community_list:
                  - BGPCommunity1
                  - BGPCommunity2
              ip:
                address:
                  prefix_lists:
                    - AllowPrefix1
                    - AllowPrefix2
            set:
              dampening:
                half_life: 30
                start_reuse_route: 1500
                start_suppress_route: 10000
                max_suppress_time: 120

      - route_map: rmap2
        entries:
          - sequence: 20
            action: permit
            description: rmap2-20-permit
            continue_sequence: 40
            match:
              ipv6:
                address:
                  prefix_lists: AllowIPv6Prefix
              interfaces: "{{ nxos_int1 }}"
            set:
              as_path:
                prepend:
                  as_number:
                    - 65563
                    - 65568
                    - 65569
              comm_list: BGPCommunity

          - sequence: 40
            action: deny
            description: rmap2-40-deny
            match:
              route_types:
                - level-1
                - level-2
              tags: 2
              ip:
                multicast:
                  rp:
                    prefix: 192.0.2.0/24
                    rp_type: ASM
                  source: 203.0.113.0/24
                  group_range:
                    first: 239.0.0.1
                    last: 239.255.255.255

      - route_map: rmap3
        entries:
        - sequence: 10
          description: "*** first stanza ***"
          action: permit
          set:
            ip:
              next_hop:
                verify_availability:
                - address: 3.3.3.3
                  track: 1
                - address: 4.4.4.4
                  track: 3

        - sequence: 20
          description: "*** second stanza ***"
          action: permit
          set:
            ip:
              next_hop:
                address: 6.6.6.6 2.2.2.2
                load_share: true
                drop_on_fail: true

        - sequence: 30
          description: "*** third stanza ***"
          action: permit
          set:
            ip:
              next_hop:
                peer_address: true

        - sequence: 40
          description: "*** fourth stanza ***"
          action: permit
          set:
            ip:
              next_hop:
                unchanged: true
                redist_unchanged: true
    state: merged

# Task output
# -------------
#  before: []
#
#  commands:
#    - "route-map rmap1 permit 10"
#    - "match as-number 65564"
#    - "match as-path Allow40"
#    - "match ip address acl_1"
#    - "description rmap1-10-permit"
#    - "route-map rmap1 deny 20"
#    - "match community BGPCommunity1 BGPCommunity2"
#    - "match ip address prefix-list AllowPrefix1 AllowPrefix2"
#    - "description rmap1-20-deny"
#    - "set dampening 30 1500 10000 120"
#    - "route-map rmap2 permit 20"
#    - "match interface Ethernet1/1"
#    - "match ipv6 address prefix-list AllowIPv6Prefix"
#    - "set as-path prepend 65563 65568 65569"
#    - "description rmap2-20-permit"
#    - "continue 40"
#    - "set comm-list BGPCommunity delete"
#    - "route-map rmap2 deny 40"
#    - "match ip multicast source 203.0.113.0/24 group-range 239.0.0.1 to 239.255.255.255 rp 192.0.2.0/24 rp-type ASM"
#    - "match route-type level-1 level-2"
#    - "match tag 2"
#    - "description rmap2-40-deny"
#    - "route-map rmap3 permit 10"
#    - "description *** first stanza ***"
#    - "set ip next-hop verify-availability 3.3.3.3 track 1"
#    - "set ip next-hop verify-availability 4.4.4.4 track 3"
#    - "route-map rmap3 permit 20"
#    - "description *** second stanza ***"
#    - "set ip next-hop 6.6.6.6 2.2.2.2 load-share  drop-on-fail"
#    - "route-map rmap3 permit 30"
#    - "description *** third stanza ***"
#    - "set ip next-hop peer-address"
#    - "route-map rmap3 permit 40"
#    - "description *** fourth stanza ***"
#    - "set ip next-hop unchanged"
#    - "set ip next-hop redist-unchanged"
#
#  after:
#   - route_map: rmap1
#     entries:
#     - action: permit
#       description: rmap1-10-permit
#       match:
#         as_number:
#           asn:
#           - '65564'
#         as_path:
#           - Allow40
#         ip:
#           address:
#             access_list: acl_1
#       sequence: 10
#
#     - action: deny
#       description: rmap1-20-deny
#       match:
#         community:
#           community_list:
#           - BGPCommunity1
#           - BGPCommunity2
#         ip:
#           address:
#             prefix_lists:
#             - AllowPrefix1
#             - AllowPrefix2
#       sequence: 20
#       set:
#         dampening:
#           half_life: 30
#           max_suppress_time: 120
#           start_reuse_route: 1500
#           start_suppress_route: 10000
#
#   - route_map: rmap2
#     entries:
#     - action: permit
#       continue_sequence: 40
#       description: rmap2-20-permit
#       match:
#         interfaces:
#         - Ethernet1/1
#         ipv6:
#           address:
#             prefix_lists:
#             - AllowIPv6Prefix
#         sequence: 20
#         set:
#           as_path:
#             prepend:
#               as_number:
#               - '65563'
#               - '65568'
#               - '65569'
#           comm_list: BGPCommunity
#
#     - action: deny
#       description: rmap2-40-deny
#       match:
#         ip:
#           multicast:
#             group_range:
#               first: 239.0.0.1
#               last: 239.255.255.255
#             rp:
#               prefix: 192.0.2.0/24
#               rp_type: ASM
#             source: 203.0.113.0/24
#         route_types:
#         - level-1
#         - level-2
#         tags:
#         - 2
#       sequence: 40
#
#   - route_map: rmap3
#     entries:
#     - sequence: 10
#       description: "*** first stanza ***"
#       action: permit
#       set:
#         ip:
#           next_hop:
#             verify_availability:
#             - address: 3.3.3.3
#               track: 1
#             - address: 4.4.4.4
#               track: 3
#
#     - sequence: 20
#       description: "*** second stanza ***"
#       action: permit
#       set:
#         ip:
#           next_hop:
#             address: 6.6.6.6 2.2.2.2
#             load_share: true
#             drop_on_fail: true
#
#     - sequence: 30
#       description: "*** third stanza ***"
#       action: permit
#       set:
#         ip:
#           next_hop:
#             peer_address: true
#
#     - sequence: 40
#       description: "*** fourth stanza ***"
#       action: permit
#       set:
#         ip:
#           next_hop:
#             unchanged: true
#             redist_unchanged: true

# After state:
# ------------
# nxos-9k-rdo# show running-config | section "^route-map"
# route-map rmap1 permit 10
#   match as-number 65564
#   match as-path Allow40
#   match ip address acl_1
#   description rmap1-10-permit
# route-map rmap1 deny 20
#   match community BGPCommunity1 BGPCommunity2
#   match ip address prefix-list AllowPrefix1 AllowPrefix2
#   description rmap1-20-deny
#   set dampening 30 1500 10000 120
# route-map rmap2 permit 20
#   match interface Ethernet1/1
#   match ipv6 address prefix-list AllowIPv6Prefix
#   set as-path prepend 65563 65568 65569
#   description rmap2-20-permit
#   continue 40
#   set comm-list BGPCommunity delete
# route-map rmap2 deny 40
#   match ip multicast source 203.0.113.0/24 group-range 239.0.0.1 to 239.255.255.255 rp 192.0.2.0/24 rp-type ASM
#   match route-type level-1 level-2
#   match tag 2
#   description rmap2-40-deny
# route-map rmap3 permit 10
#   description *** first stanza ***
#   set ip next-hop verify-availability 3.3.3.3 track 1
#   set ip next-hop verify-availability 4.4.4.4 track 3
# route-map rmap3 permit 20
#   description *** second stanza ***
#   set ip next-hop 6.6.6.6 2.2.2.2 load-share  drop-on-fail
# route-map rmap3 permit 30
#   description *** third stanza ***
#   set ip next-hop peer-address
# route-map rmap3 permit 40
#   description *** fourth stanza ***
#   set ip next-hop unchanged
#   set ip next-hop redist-unchanged
#
# Using replaced
# (for the listed route-map(s), sequences that are in running-config but not in the task are negated)

# Before state:
# ------------
# nxos-9k-rdo# show running-config | section "^route-map"
# route-map rmap1 permit 10
#   match as-number 65564
#   match as-path Allow40
#   match ip address acl_1
#   description rmap1-10-permit
# route-map rmap1 deny 20
#   match community BGPCommunity1 BGPCommunity2
#   match ip address prefix-list AllowPrefix1 AllowPrefix2
#   description rmap1-20-deny
#   set dampening 30 1500 10000 120
# route-map rmap2 permit 20
#   match interface Ethernet1/1
#   match ipv6 address prefix-list AllowIPv6Prefix
#   set as-path prepend 65563 65568 65569
#   description rmap2-20-permit
#   continue 40
#   set comm-list BGPCommunity delete
# route-map rmap2 deny 40
#   match ip multicast source 203.0.113.0/24 group-range 239.0.0.1 to 239.255.255.255 rp 192.0.2.0/24 rp-type ASM
#   match route-type level-1 level-2
#   match tag 2
#   description rmap2-40-deny
# route-map rmap3 permit 10
#   description *** first stanza ***
#   set ip next-hop verify-availability 3.3.3.3 track 1
#   set ip next-hop verify-availability 4.4.4.4 track 3
# route-map rmap3 permit 20
#   description *** second stanza ***
#   set ip next-hop 6.6.6.6 2.2.2.2 load-share  drop-on-fail
# route-map rmap3 permit 30
#   description *** third stanza ***
#   set ip next-hop peer-address
# route-map rmap3 permit 40
#   description *** fourth stanza ***
#   set ip next-hop unchanged
#   set ip next-hop redist-unchanged
#
- name: Replace route-maps configurations of listed route-maps with provided configurations
  cisco.nxos.nxos_route_maps:
    config:
      - route_map: rmap1
        entries:
          - sequence: 20
            action: deny
            description: rmap1-20-deny
            match:
              community:
                community_list:
                  - BGPCommunity4
                  - BGPCommunity5
              ip:
                address:
                  prefix_lists:
                    - AllowPrefix1
            set:
              community:
                local_as: True

      - route_map: rmap3
        entries:
        - sequence: 10
          description: "*** first stanza ***"
          action: permit
          set:
            ip:
              next_hop:
                verify_availability:
                - address: 3.3.3.3
                  track: 1
        - sequence: 20
          description: "*** second stanza ***"
          action: permit
          set:
            ip:
              next_hop:
                peer_address: true
        - sequence: 30
          description: "*** third stanza ***"
          action: permit
          set:
            ip:
              next_hop:
                address: 6.6.6.6 2.2.2.2
                load_share: true
                drop_on_fail: true
    state: replaced

# Task output
# -------------
#  before:
#   - route_map: rmap1
#     entries:
#     - action: permit
#       description: rmap1-10-permit
#       match:
#         as_number:
#           asn:
#           - '65564'
#         as_path:
#           - Allow40
#         ip:
#           address:
#             access_list: acl_1
#       sequence: 10
#
#     - action: deny
#       description: rmap1-20-deny
#       match:
#         community:
#           community_list:
#           - BGPCommunity1
#           - BGPCommunity2
#         ip:
#           address:
#             prefix_lists:
#             - AllowPrefix1
#             - AllowPrefix2
#       sequence: 20
#       set:
#         dampening:
#           half_life: 30
#           max_suppress_time: 120
#           start_reuse_route: 1500
#           start_suppress_route: 10000
#
#   - route_map: rmap2
#     entries:
#     - action: permit
#       continue_sequence: 40
#       description: rmap2-20-permit
#       match:
#         interfaces:
#         - Ethernet1/1
#         ipv6:
#           address:
#             prefix_lists:
#             - AllowIPv6Prefix
#         sequence: 20
#         set:
#           as_path:
#             prepend:
#               as_number:
#               - '65563'
#               - '65568'
#               - '65569'
#           comm_list: BGPCommunity
#
#     - action: deny
#       description: rmap2-40-deny
#       match:
#         ip:
#           multicast:
#             group_range:
#               first: 239.0.0.1
#               last: 239.255.255.255
#             rp:
#               prefix: 192.0.2.0/24
#               rp_type: ASM
#             source: 203.0.113.0/24
#         route_types:
#         - level-1
#         - level-2
#         tags:
#         - 2
#       sequence: 40
#
#   - route_map: rmap3
#     entries:
#     - sequence: 10
#       description: "*** first stanza ***"
#       action: permit
#       set:
#         ip:
#           next_hop:
#             verify_availability:
#             - address: 3.3.3.3
#               track: 1
#             - address: 4.4.4.4
#               track: 3
#
#     - sequence: 20
#       description: "*** second stanza ***"
#       action: permit
#       set:
#         ip:
#           next_hop:
#             address: 6.6.6.6 2.2.2.2
#             load_share: true
#             drop_on_fail: true
#
#     - sequence: 30
#       description: "*** third stanza ***"
#       action: permit
#       set:
#         ip:
#           next_hop:
#             peer_address: true
#
#     - sequence: 40
#       description: "*** fourth stanza ***"
#       action: permit
#       set:
#         ip:
#           next_hop:
#             unchanged: true
#             redist_unchanged: true
#
#  commands:
#    - no route-map rmap1 permit 10
#    - route-map rmap1 deny 20
#    - no match community BGPCommunity1 BGPCommunity2
#    - match community BGPCommunity4 BGPCommunity5
#    - no match ip address prefix-list AllowPrefix1 AllowPrefix2
#    - match ip address prefix-list AllowPrefix1
#    - no set dampening 30 1500 10000 120
#    - set community local-AS
#    - route-map rmap3 permit 10
#    - no set ip next-hop verify-availability 4.4.4.4 track 3
#    - route-map rmap3 permit 20
#    - no set ip next-hop 6.6.6.6 2.2.2.2 load-share drop-on-fail
#    - set ip next-hop peer-address
#    - route-map rmap3 permit 30
#    - no set ip next-hop peer-address
#    - set ip next-hop 6.6.6.6 2.2.2.2 load-share drop-on-fail
#    - no route-map rmap3 permit 40
#
#  after:
#    - route_map: rmap1
#      entries:
#        - sequence: 20
#          action: deny
#          description: rmap1-20-deny
#          match:
#            community:
#              community_list:
#                - BGPCommunity4
#                - BGPCommunity5
#            ip:
#              address:
#                prefix_lists:
#                  - AllowPrefix1
#          set:
#            community:
#              local_as: True
#
#    - route_map: rmap2
#      entries:
#        - action: permit
#          continue_sequence: 40
#          description: rmap2-20-permit
#          match:
#            interfaces:
#            - Ethernet1/1
#            ipv6:
#              address:
#                prefix_lists:
#                - AllowIPv6Prefix
#          sequence: 20
#          set:
#            as_path:
#              prepend:
#                as_number:
#                - '65563'
#                - '65568'
#                - '65569'
#            comm_list: BGPCommunity
#
#        - action: deny
#          description: rmap2-40-deny
#          match:
#            ip:
#              multicast:
#                group_range:
#                  first: 239.0.0.1
#                  last: 239.255.255.255
#                rp:
#                  prefix: 192.0.2.0/24
#                  rp_type: ASM
#                source: 203.0.113.0/24
#            route_types:
#            - level-1
#            - level-2
#            tags:
#            - 2
#          sequence: 40
#
#    - route_map: rmap3
#      entries:
#      - sequence: 10
#        description: "*** first stanza ***"
#        action: permit
#        set:
#          ip:
#            next_hop:
#              verify_availability:
#              - address: 3.3.3.3
#                track: 1
#      - sequence: 20
#        description: "*** second stanza ***"
#        action: permit
#        set:
#          ip:
#            next_hop:
#              peer_address: true
#      - sequence: 30
#        description: "*** third stanza ***"
#        action: permit
#        set:
#          ip:
#            next_hop:
#              address: 6.6.6.6 2.2.2.2
#              load_share: true
#              drop_on_fail: true

# After state:
# ------------
# nxos-9k-rdo# show running-config | section "^route-map"
# route-map rmap1 deny 20
#   description rmap1-20-deny
#   match community BGPCommunity4 BGPCommunity5
#   match ip address prefix-list AllowPrefix1
#   set community local-AS
# route-map rmap2 permit 20
#   match interface Ethernet1/1
#   match ipv6 address prefix-list AllowIPv6Prefix
#   set as-path prepend 65563 65568 65569
#   description rmap2-20-permit
#   continue 40
#   set comm-list BGPCommunity delete
# route-map rmap2 deny 40
#   match ip multicast source 203.0.113.0/24 group-range 239.0.0.1 to 239.255.255.255 rp 192.0.2.0/24 rp-type ASM
#   match route-type level-1 level-2
#   match tag 2
#   description rmap2-40-deny
# route-map rmap3 permit 10
#   description *** first stanza ***
#   set ip next-hop verify-availability 3.3.3.3 track 1
# route-map rmap3 permit 20
#   description *** second stanza ***
#   set ip next-hop peer-address
# route-map rmap3 permit 30
#   description *** third stanza ***
#   set ip next-hop 6.6.6.6 2.2.2.2 load-share  drop-on-fail

# Using overridden

# Before state:
# ------------
# nxos-9k-rdo# show running-config | section "^route-map"
# route-map rmap1 permit 10
#   match as-number 65564
#   match as-path Allow40
#   match ip address acl_1
#   description rmap1-10-permit
# route-map rmap1 deny 20
#   match community BGPCommunity1 BGPCommunity2
#   match ip address prefix-list AllowPrefix1 AllowPrefix2
#   description rmap1-20-deny
#   set dampening 30 1500 10000 120
# route-map rmap2 permit 20
#   match interface Ethernet1/1
#   match ipv6 address prefix-list AllowIPv6Prefix
#   set as-path prepend 65563 65568 65569
#   description rmap2-20-permit
#   continue 40
#   set comm-list BGPCommunity delete
# route-map rmap2 deny 40
#   match ip multicast source 203.0.113.0/24 group-range 239.0.0.1 to 239.255.255.255 rp 192.0.2.0/24 rp-type ASM
#   match route-type level-1 level-2
#   match tag 2
#   description rmap2-40-deny

- name: Override all route-maps configuration with provided configuration
  cisco.nxos.nxos_route_maps:
    config:
      - route_map: rmap1
        entries:
          - sequence: 20
            action: deny
            description: rmap1-20-deny
            match:
              community:
                community_list:
                  - BGPCommunity4
                  - BGPCommunity5
              ip:
                address:
                  prefix_lists:
                    - AllowPrefix1
            set:
              community:
                local_as: True
    state: overridden

# Task output
# -------------
#  before:
#   - route_map: rmap1
#     entries:
#     - action: permit
#       description: rmap1-10-permit
#       match:
#         as_number:
#           asn:
#           - '65564'
#         as_path:
#           - Allow40
#         ip:
#           address:
#             access_list: acl_1
#       sequence: 10
#
#     - action: deny
#       description: rmap1-20-deny
#       match:
#         community:
#           community_list:
#           - BGPCommunity1
#           - BGPCommunity2
#         ip:
#           address:
#             prefix_lists:
#             - AllowPrefix1
#             - AllowPrefix2
#       sequence: 20
#       set:
#         dampening:
#           half_life: 30
#           max_suppress_time: 120
#           start_reuse_route: 1500
#           start_suppress_route: 10000
#
#   - route_map: rmap2
#     entries:
#     - action: permit
#       continue_sequence: 40
#       description: rmap2-20-permit
#       match:
#         interfaces:
#         - Ethernet1/1
#         ipv6:
#           address:
#             prefix_lists:
#             - AllowIPv6Prefix
#         sequence: 20
#         set:
#           as_path:
#             prepend:
#               as_number:
#               - '65563'
#               - '65568'
#               - '65569'
#           comm_list: BGPCommunity
#
#     - action: deny
#       description: rmap2-40-deny
#       match:
#         ip:
#           multicast:
#             group_range:
#               first: 239.0.0.1
#               last: 239.255.255.255
#             rp:
#               prefix: 192.0.2.0/24
#               rp_type: ASM
#             source: 203.0.113.0/24
#         route_types:
#         - level-1
#         - level-2
#         tags:
#         - 2
#       sequence: 40
#
#  commands:
#    - no route-map rmap1 permit 10
#    - route-map rmap1 deny 20
#    - no match community BGPCommunity1 BGPCommunity2
#    - match community BGPCommunity4 BGPCommunity5
#    - no match ip address prefix-list AllowPrefix1 AllowPrefix2
#    - match ip address prefix-list AllowPrefix1
#    - no set dampening 30 1500 10000 120
#    - set community local-AS
#    - no route-map rmap2 permit 20
#    - no route-map rmap2 deny 40
#
#  after:
#  - route_map: rmap1
#    entries:
#    - sequence: 20
#      action: deny
#      description: rmap1-20-deny
#      match:
#        community:
#          community_list:
#          - BGPCommunity4
#          - BGPCommunity5
#        ip:
#          address:
#            prefix_lists:
#            - AllowPrefix1
#      set:
#        community:
#          local_as: True
#
# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^route-map"
# route-map rmap1 deny 20
#   description rmap1-20-deny
#   match community BGPCommunity4 BGPCommunity5
#   match ip address prefix-list AllowPrefix1
#   set community local-AS

# Using deleted to delete a single route-map

# Before state:
# ------------
# nxos-9k-rdo# show running-config | section "^route-map"
# route-map rmap1 permit 10
#   match as-number 65564
#   match as-path Allow40
#   match ip address acl_1
#   description rmap1-10-permit
# route-map rmap1 deny 20
#   match community BGPCommunity1 BGPCommunity2
#   match ip address prefix-list AllowPrefix1 AllowPrefix2
#   description rmap1-20-deny
#   set dampening 30 1500 10000 120
# route-map rmap2 permit 20
#   match interface Ethernet1/1
#   match ipv6 address prefix-list AllowIPv6Prefix
#   set as-path prepend 65563 65568 65569
#   description rmap2-20-permit
#   continue 40
#   set comm-list BGPCommunity delete
# route-map rmap2 deny 40
#   match ip multicast source 203.0.113.0/24 group-range 239.0.0.1 to 239.255.255.255 rp 192.0.2.0/24 rp-type ASM
#   match route-type level-1 level-2
#   match tag 2
#   description rmap2-40-deny

- name: Delete single route-map
  cisco.nxos.nxos_route_maps:
    config:
      - route_map: rmap1
    state: deleted

# Task output
# -------------
#  before:
#   - route_map: rmap1
#     entries:
#     - action: permit
#       description: rmap1-10-permit
#       match:
#         as_number:
#           asn:
#           - '65564'
#         as_path:
#           - Allow40
#         ip:
#           address:
#             access_list: acl_1
#       sequence: 10
#
#     - action: deny
#       description: rmap1-20-deny
#       match:
#         community:
#           community_list:
#           - BGPCommunity1
#           - BGPCommunity2
#         ip:
#           address:
#             prefix_lists:
#             - AllowPrefix1
#             - AllowPrefix2
#       sequence: 20
#       set:
#         dampening:
#           half_life: 30
#           max_suppress_time: 120
#           start_reuse_route: 1500
#           start_suppress_route: 10000
#
#   - route_map: rmap2
#     entries:
#     - action: permit
#       continue_sequence: 40
#       description: rmap2-20-permit
#       match:
#         interfaces:
#         - Ethernet1/1
#         ipv6:
#           address:
#             prefix_lists:
#             - AllowIPv6Prefix
#         sequence: 20
#         set:
#           as_path:
#             prepend:
#               as_number:
#               - '65563'
#               - '65568'
#               - '65569'
#           comm_list: BGPCommunity
#
#     - action: deny
#       description: rmap2-40-deny
#       match:
#         ip:
#           multicast:
#             group_range:
#               first: 239.0.0.1
#               last: 239.255.255.255
#             rp:
#               prefix: 192.0.2.0/24
#               rp_type: ASM
#             source: 203.0.113.0/24
#         route_types:
#         - level-1
#         - level-2
#         tags:
#         - 2
#       sequence: 40
#
#  commands:
#    - no route-map rmap1 permit 10
#    - no route-map rmap1 deny 20
#
#  after:
#   - route_map: rmap2
#     entries:
#     - action: permit
#       continue_sequence: 40
#       description: rmap2-20-permit
#       match:
#         interfaces:
#         - Ethernet1/1
#         ipv6:
#           address:
#             prefix_lists:
#             - AllowIPv6Prefix
#         sequence: 20
#         set:
#           as_path:
#             prepend:
#               as_number:
#               - '65563'
#               - '65568'
#               - '65569'
#           comm_list: BGPCommunity
#
#     - action: deny
#       description: rmap2-40-deny
#       match:
#         ip:
#           multicast:
#             group_range:
#               first: 239.0.0.1
#               last: 239.255.255.255
#             rp:
#               prefix: 192.0.2.0/24
#               rp_type: ASM
#             source: 203.0.113.0/24
#         route_types:
#         - level-1
#         - level-2
#         tags:
#         - 2
#       sequence: 40
#
# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^route-map"
# route-map rmap2 permit 20
#   match interface Ethernet1/1
#   match ipv6 address prefix-list AllowIPv6Prefix
#   set as-path prepend 65563 65568 65569
#   description rmap2-20-permit
#   continue 40
#   set comm-list BGPCommunity delete
# route-map rmap2 deny 40
#   match ip multicast source 203.0.113.0/24 group-range 239.0.0.1 to 239.255.255.255 rp 192.0.2.0/24 rp-type ASM
#   match route-type level-1 level-2
#   match tag 2
#   description rmap2-40-deny

# Using deleted to delete all route-maps from the device running-config

# Before state:
# ------------
# nxos-9k-rdo# show running-config | section "^route-map"
# route-map rmap1 permit 10
#   match as-number 65564
#   match as-path Allow40
#   match ip address acl_1
#   description rmap1-10-permit
# route-map rmap1 deny 20
#   match community BGPCommunity1 BGPCommunity2
#   match ip address prefix-list AllowPrefix1 AllowPrefix2
#   description rmap1-20-deny
#   set dampening 30 1500 10000 120
# route-map rmap2 permit 20
#   match interface Ethernet1/1
#   match ipv6 address prefix-list AllowIPv6Prefix
#   set as-path prepend 65563 65568 65569
#   description rmap2-20-permit
#   continue 40
#   set comm-list BGPCommunity delete
# route-map rmap2 deny 40
#   match ip multicast source 203.0.113.0/24 group-range 239.0.0.1 to 239.255.255.255 rp 192.0.2.0/24 rp-type ASM
#   match route-type level-1 level-2
#   match tag 2
#   description rmap2-40-deny

- name: Delete all route-maps
  cisco.nxos.nxos_route_maps:
    state: deleted

# Task output
# -------------
#  before:
#   - route_map: rmap1
#     entries:
#     - action: permit
#       description: rmap1-10-permit
#       match:
#         as_number:
#           asn:
#           - '65564'
#         as_path:
#           - Allow40
#         ip:
#           address:
#             access_list: acl_1
#       sequence: 10
#
#     - action: deny
#       description: rmap1-20-deny
#       match:
#         community:
#           community_list:
#           - BGPCommunity1
#           - BGPCommunity2
#         ip:
#           address:
#             prefix_lists:
#             - AllowPrefix1
#             - AllowPrefix2
#       sequence: 20
#       set:
#         dampening:
#           half_life: 30
#           max_suppress_time: 120
#           start_reuse_route: 1500
#           start_suppress_route: 10000
#
#   - route_map: rmap2
#     entries:
#     - action: permit
#       continue_sequence: 40
#       description: rmap2-20-permit
#       match:
#         interfaces:
#         - Ethernet1/1
#         ipv6:
#           address:
#             prefix_lists:
#             - AllowIPv6Prefix
#         sequence: 20
#         set:
#           as_path:
#             prepend:
#               as_number:
#               - '65563'
#               - '65568'
#               - '65569'
#           comm_list: BGPCommunity
#
#     - action: deny
#       description: rmap2-40-deny
#       match:
#         ip:
#           multicast:
#             group_range:
#               first: 239.0.0.1
#               last: 239.255.255.255
#             rp:
#               prefix: 192.0.2.0/24
#               rp_type: ASM
#             source: 203.0.113.0/24
#         route_types:
#         - level-1
#         - level-2
#         tags:
#         - 2
#       sequence: 40
#
#  commands:
#    - no route-map rmap1 permit 10
#    - no route-map rmap1 deny 20
#    - no route-map rmap2 permit 20
#    - no route-map rmap2 deny 40
#
#  after: []
#
# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^route-map"

- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.nxos.nxos_route_maps:
    config:
      - route_map: rmap1
        entries:
          - sequence: 10
            action: permit
            description: rmap1-10-permit
            match:
              ip:
                address:
                  access_list: acl_1
              as_path: Allow40
              as_number:
                asn: 65564

          - sequence: 20
            action: deny
            description: rmap1-20-deny
            match:
              community:
                community_list:
                  - BGPCommunity1
                  - BGPCommunity2
              ip:
                address:
                  prefix_lists:
                    - AllowPrefix1
                    - AllowPrefix2
            set:
              dampening:
                half_life: 30
                start_reuse_route: 1500
                start_suppress_route: 10000
                max_suppress_time: 120

      - route_map: rmap2
        entries:
          - sequence: 20
            action: permit
            description: rmap2-20-permit
            continue_sequence: 40
            match:
              ipv6:
                address:
                  prefix_lists: AllowIPv6Prefix
              interfaces: "{{ nxos_int1 }}"
            set:
              as_path:
                prepend:
                  as_number:
                    - 65563
                    - 65568
                    - 65569
              comm_list: BGPCommunity

          - sequence: 40
            action: deny
            description: rmap2-40-deny
            match:
              route_types:
                - level-1
                - level-2
              tags: 2
              ip:
                multicast:
                  rp:
                    prefix: 192.0.2.0/24
                    rp_type: ASM
                  source: 203.0.113.0/24
                  group_range:
                    first: 239.0.0.1
                    last: 239.255.255.255
    state: rendered

# Task Output (redacted)
# -----------------------
#  rendered:
#    - "route-map rmap1 permit 10"
#    - "match as-number 65564"
#    - "match as-path Allow40"
#    - "match ip address acl_1"
#    - "description rmap1-10-permit"
#    - "route-map rmap1 deny 20"
#    - "match community BGPCommunity1 BGPCommunity2"
#    - "match ip address prefix-list AllowPrefix1 AllowPrefix2"
#    - "description rmap1-20-deny"
#    - "set dampening 30 1500 10000 120"
#    - "route-map rmap2 permit 20"
#    - "match interface Ethernet1/1"
#    - "match ipv6 address prefix-list AllowIPv6Prefix"
#    - "set as-path prepend 65563 65568 65569"
#    - "description rmap2-20-permit"
#    - "continue 40"
#    - "set comm-list BGPCommunity delete"
#    - "route-map rmap2 deny 40"
#    - "match ip multicast source 203.0.113.0/24 group-range 239.0.0.1 to 239.255.255.255 rp 192.0.2.0/24 rp-type ASM"
#    - "match route-type level-1 level-2"
#    - "match tag 2"
#    - "description rmap2-40-deny"

# Using parsed

# parsed.cfg
# ------------
# route-map rmap1 permit 10
#   match as-number 65564
#   match as-path Allow40
#   match ip address acl_1
#   description rmap1-10-permit
# route-map rmap1 deny 20
#   match community BGPCommunity1 BGPCommunity2
#   match ip address prefix-list AllowPrefix1 AllowPrefix2
#   description rmap1-20-deny
#   set dampening 30 1500 10000 120
# route-map rmap2 permit 20
#   match interface Ethernet1/1
#   match ipv6 address prefix-list AllowIPv6Prefix
#   set as-path prepend 65563 65568 65569
#   description rmap2-20-permit
#   continue 40
#   set comm-list BGPCommunity delete
# route-map rmap2 deny 40
#   match ip multicast source 203.0.113.0/24 group-range 239.0.0.1 to 239.255.255.255 rp 192.0.2.0/24 rp-type ASM
#   match route-type level-1 level-2
#   match tag 2
#   description rmap2-40-deny

- name: Parse externally provided route-maps configuration
  cisco.nxos.nxos_route_maps:
    running_config: "{{ lookup('file', './fixtures/parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
#  parsed:
#   - route_map: rmap1
#     entries:
#     - action: permit
#       description: rmap1-10-permit
#       match:
#         as_number:
#           asn:
#           - '65564'
#         as_path:
#           - Allow40
#         ip:
#           address:
#             access_list: acl_1
#       sequence: 10
#
#     - action: deny
#       description: rmap1-20-deny
#       match:
#         community:
#           community_list:
#           - BGPCommunity1
#           - BGPCommunity2
#         ip:
#           address:
#             prefix_lists:
#             - AllowPrefix1
#             - AllowPrefix2
#       sequence: 20
#       set:
#         dampening:
#           half_life: 30
#           max_suppress_time: 120
#           start_reuse_route: 1500
#           start_suppress_route: 10000
#
#   - route_map: rmap2
#     entries:
#     - action: permit
#       continue_sequence: 40
#       description: rmap2-20-permit
#       match:
#         interfaces:
#         - Ethernet1/1
#         ipv6:
#           address:
#             prefix_lists:
#             - AllowIPv6Prefix
#         sequence: 20
#         set:
#           as_path:
#             prepend:
#               as_number:
#               - '65563'
#               - '65568'
#               - '65569'
#           comm_list: BGPCommunity
#
#     - action: deny
#       description: rmap2-40-deny
#       match:
#         ip:
#           multicast:
#             group_range:
#               first: 239.0.0.1
#               last: 239.255.255.255
#             rp:
#               prefix: 192.0.2.0/24
#               rp_type: ASM
#             source: 203.0.113.0/24
#         route_types:
#         - level-1
#         - level-2
#         tags:
#         - 2
#       sequence: 40

# Using gathered

# Existing route-map config
# ---------------------------
# nxos-9k-rdo# show running-config | section "^route-map"
# route-map rmap1 permit 10
#   match as-number 65564
#   match as-path Allow40
#   match ip address acl_1
#   description rmap1-10-permit
# route-map rmap2 permit 20
#   match interface Ethernet1/1
#   match ipv6 address prefix-list AllowIPv6Prefix
#   set as-path prepend 65563 65568 65569
#   description rmap2-20-permit
#   continue 40
#   set comm-list BGPCommunity delete

- name: Gather route-maps facts using gathered
  cisco.nxos.nxos_route_maps:
    state: gathered

#  gathered:
#   - route_map: rmap1
#     entries:
#     - action: permit
#       description: rmap1-10-permit
#       match:
#         as_number:
#           asn:
#           - '65564'
#         as_path:
#           - Allow40
#         ip:
#           address:
#             access_list: acl_1
#       sequence: 10
#
#   - route_map: rmap2
#     entries:
#     - action: permit
#       continue_sequence: 40
#       description: rmap2-20-permit
#       match:
#         interfaces:
#         - Ethernet1/1
#         ipv6:
#           address:
#             prefix_lists:
#             - AllowIPv6Prefix
#         sequence: 20
#         set:
#           as_path:
#             prepend:
#               as_number:
#               - '65563'
#               - '65568'
#               - '65569'
#           comm_list: BGPCommunity
#
```

## [Return Values](nxos_route_maps_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["route-map rmap1 permit 10", "match as-number 65564", "match as-path Allow40", "match ip address acl_1", "description rmap1-10-permit", "route-map rmap1 deny 20", "match community BGPCommunity1 BGPCommunity2"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
