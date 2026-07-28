---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_route_maps module – Route Map Resource Module."
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_route_maps_module.html
fetched_at: 2026-07-28T00:23:31+00:00
---
# vyos.vyos.vyos_route_maps module – Route Map Resource Module.

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/vyos/vyos) (version 3.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_route_maps`.

New in vyos.vyos 2.3.0

- [Synopsis](vyos_route_maps_module.md#synopsis)
- [Parameters](vyos_route_maps_module.md#parameters)
- [Notes](vyos_route_maps_module.md#notes)
- [Examples](vyos_route_maps_module.md#examples)

## [Synopsis](vyos_route_maps_module.md#id1)

- This module manages route map configurations on devices running VYOS.

## [Parameters](vyos_route_maps_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of route-map configuration. |
| **entries**  aliases: rules  list / elements=dictionary | Route Map rules. |
| **action**  string | Action for matching routes  Choices:   - `"deny"` - `"permit"` |
| **call**  string | Route map name |
| **continue_sequence**  integer | Continue on a different entry within the route-map. |
| **description**  string | Description for the rule. |
| **match**  dictionary | Route parameters to match. |
| **as_path**  string | Set as-path. |
| **community**  dictionary | BGP community attribute. |
| **community_list**  string | BGP community-list to match |
| **exact_match**  boolean | BGP community-list to match  Choices:   - `false` - `true` |
| **extcommunity**  string | Extended community name. |
| **interface**  string | First hop interface of a route to match. |
| **ip**  dictionary | IP prefix parameters to match. |
| **address**  dictionary | IP address of route to match. |
| **list_type**  string | type of list  Choices:   - `"access-list"` - `"prefix-list"` |
| **value**  string | value of access-list and prefix list |
| **next_hop**  dictionary | next hop prefix list. |
| **list_type**  string | type of list  Choices:   - `"access-list"` - `"prefix-list"` |
| **value**  string | value of access-list and prefix list |
| **route_source**  dictionary | IP route-source to match |
| **list_type**  string | type of list  Choices:   - `"access-list"` - `"prefix-list"` |
| **value**  string | value of access-list and prefix list |
| **ipv6**  dictionary | IPv6 prefix parameters to match. |
| **address**  dictionary | IPv6 address of route to match. |
| **list_type**  string | type of list  Choices:   - `"access-list"` - `"prefix-list"` |
| **value**  string | value of access-list and prefix list |
| **next_hop**  string | next-hop ipv6 address IPv6 <h:h:h:h:h:h:h:h>. |
| **large_community_large_community_list**  string | BGP large-community-list to match. |
| **metric**  integer | Route metric <1-65535>. |
| **origin**  string | bgp origin.  Choices:   - `"ebgp"` - `"ibgp"` - `"incomplete"` |
| **peer**  string | Peer IP address <x.x.x.x>. |
| **rpki**  string | RPKI validation value.  Choices:   - `"notfound"` - `"invalid"` - `"valid"` |
| **on_match**  dictionary | Exit policy on matches. |
| **goto**  integer | Rule number to goto on match <1-65535>. |
| **next**  boolean | Next sequence number to goto on match.  Choices:   - `false` - `true` |
| **sequence**  integer | Route map rule number <1-65535>. |
| **set**  dictionary | Route parameters. |
| **aggregator**  dictionary | Border Gateway Protocol (BGP) aggregator attribute. |
| **as**  string | AS number of an aggregation. |
| **ip**  string | IP address. |
| **as_path_exclude**  string | BGP AS path exclude string ex “456 64500 45001” |
| **as_path_prepend**  string | Prepend string for a Border Gateway Protocol (BGP) AS-path attribute. |
| **atomic_aggregate**  boolean | Border Gateway Protocol (BGP) atomic aggregate attribute.  Choices:   - `false` - `true` |
| **bgp_extcommunity_rt**  string | ExtCommunity in format AS:value |
| **comm_list**  dictionary | Border Gateway Protocol (BGP) communities matching a community-list. |
| **comm_list**  string | BGP communities with a community-list. |
| **delete**  boolean | Delete BGP communities matching the community-list.  Choices:   - `false` - `true` |
| **community**  dictionary | Border Gateway Protocol (BGP) community attribute. |
| **value**  string | Community in 4 octet AS:value format or it can be from local-AS, no-advertise,no-expert,internet,additive,none. |
| **extcommunity_rt**  string | Set route target value.ASN:nn_or_IP_address:nn VPN extended community. |
| **extcommunity_soo**  string | Set Site of Origin value. ASN:nn_or_IP_address:nn VPN extended community |
| **ip_next_hop**  string | IP address. |
| **ipv6_next_hop**  dictionary | Nexthop IPv6 address. |
| **ip_type**  string | Global or Local  Choices:   - `"global"` - `"local"` |
| **value**  string | ipv6 address |
| **large_community**  string | Set BGP large community value. |
| **local_preference**  string | Border Gateway Protocol (BGP) local preference attribute.Example <0-4294967295>. |
| **metric**  string | Destination routing protocol metric. Example <0-4294967295>. |
| **metric_type**  string | Open Shortest Path First (OSPF) external metric-type.  Choices:   - `"type-1"` - `"type-2"` |
| **origin**  string | Set bgp origin.  Choices:   - `"egp"` - `"igp"` - `"incomplete"` |
| **originator_id**  string | Border Gateway Protocol (BGP) originator ID attribute. Originator IP address. |
| **src**  string | Source address for route. Example <x.x.x.x> IP address. |
| **tag**  string | Tag value for routing protocol. Example <1-65535> |
| **weight**  string | Border Gateway Protocol (BGP) weight attribute. Example <0-4294967295> |
| **route_map**  string | Route map name. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VYOS device by executing the command **show configuration commands | grep route-map**.  The state *parsed* reads the configuration from `show configuration commands | grep route-map` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Choices:   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](vyos_route_maps_module.md#id3)

> **Note:**
>
> - Tested against vyos 1.2.
> - This module works with connection `network_cli`.

## [Examples](vyos_route_maps_module.md#id4)

```yaml+jinja
# Using merged
# Before state

# vyos@vyos:~$ show configuration commands |  match "set policy route-map"
# vyos@vyos:~$
    - name: Merge the provided configuration with the existing running configuration
      register: result
      vyos.vyos.vyos_route_maps: &id001
        config:
          - route_map: test1
            entries:
              - sequence: 1
                description: "test"
                action: permit
                continue: 2
                on_match:
                  next: True
          - route_map: test3
            entries:
              - sequence: 1
                action: permit
                match:
                  rpki: invalid
                  metric: 1
                  peer: 192.0.2.32
                set:
                  local_preference: 4
                  metric: 5
                  metric_type: "type-1"
                  origin: egp
                  originator_id: 192.0.2.34
                  tag: 5
                  weight: 4
        state: merged
# After State
# vyos@vyos:~$ show configuration commands |  match "set policy route-maps"
#   set policy route-map test1 rule 1 description test
#   set policy route-map test1 rule 1 action permit
#   set policy route-map test1 rule 1 continue 2
#   set policy route-map test1 rule 1 on-match next
#   set policy route-map test3 rule 1 action permit
#   set policy route-map test3 rule 1 set local-preference 4
#   set policy route-map test3 rule 1 set metric 5
#   set policy route-map test3 rule 1 set metric-type type-1
#   set policy route-map test3 rule 1 set origin egp
#   set policy route-map test3 rule 1 set originator-id 192.0.2.34
#   set policy route-map test3 rule 1 set tag 5
#   set policy route-map test3 rule 1 set weight 4
#   set policy route-map test3 rule 1 match metric 1
#   set policy route-map test3 rule 1 match peer 192.0.2.32
#   set policy route-map test3 rule 1 match rpki invalid

# "after": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "continue_sequence": 2,
#                     "description": "test",
#                     "on_match": {
#                         "next": true
#                     },
#                     "sequence": 1
#                 }
#             ],
#             "route_map": "test1"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "match": {
#                         "metric": 1,
#                         "peer": "192.0.2.32",
#                         "rpki": "invalid"
#                     },
#                     "sequence": 1,
#                     "set": {
#                         "local_preference": "4",
#                         "metric": "5",
#                         "metric_type": "type-1",
#                         "origin": "egp",
#                         "originator_id": "192.0.2.34",
#                         "tag": "5",
#                         "weight": "4"
#                     }
#                 }
#             ],
#             "route_map": "test3"
#         }
#     ],
#     "before": [],
#     "changed": true,
#     "commands": [
#         "set policy route-map test1 rule 1 description test",
#         "set policy route-map test1 rule 1 action permit",
#         "set policy route-map test1 rule 1 continue 2",
#         "set policy route-map test1 rule 1 on-match next",
#         "set policy route-map test3 rule 1 action permit",
#         "set policy route-map test3 rule 1 set local-preference 4",
#         "set policy route-map test3 rule 1 set metric 5",
#         "set policy route-map test3 rule 1 set metric-type type-1",
#         "set policy route-map test3 rule 1 set origin egp",
#         "set policy route-map test3 rule 1 set originator-id 192.0.2.34",
#         "set policy route-map test3 rule 1 set tag 5",
#         "set policy route-map test3 rule 1 set weight 4",
#         "set policy route-map test3 rule 1 match metric 1",
#         "set policy route-map test3 rule 1 match peer 192.0.2.32",
#         "set policy route-map test3 rule 1 match rpki invalid"
#     ],

# Using replaced:
# --------------

# Before state:
# vyos@vyos:~$ show configuration commands |  match "set route-map policy"
# set policy route-map test2 rule 1 action 'permit'
# set policy route-map test2 rule 1 description 'test'
# set policy route-map test2 rule 1 on-match next
# set policy route-map test2 rule 2 action 'permit'
# set policy route-map test2 rule 2 on-match goto '4'
# set policy route-map test3 rule 1 action 'permit'
# set policy route-map test3 rule 1 match metric '1'
# set policy route-map test3 rule 1 match peer '192.0.2.32'
# set policy route-map test3 rule 1 match rpki 'invalid'
# set policy route-map test3 rule 1 set community 'internet'
# set policy route-map test3 rule 1 set ip-next-hop '192.0.2.33'
# set policy route-map test3 rule 1 set local-preference '4'
# set policy route-map test3 rule 1 set metric '5'
# set policy route-map test3 rule 1 set metric-type 'type-1'
# set policy route-map test3 rule 1 set origin 'egp'
# set policy route-map test3 rule 1 set originator-id '192.0.2.34'
# set policy route-map test3 rule 1 set tag '5'
# set policy route-map test3 rule 1 set weight '4'
#
#     - name: Replace  the provided configuration with the existing running configuration
#       register: result
#       vyos.vyos.vyos_route_maps: &id001
#         config:
#           - route_map: test3
#             entries:
#               - sequence: 1
#                 action: permit
#                 match:
#                   rpki: invalid
#                   metric: 3
#                   peer: 192.0.2.35
#                 set:
#                   local_preference: 6
#                   metric: 4
#                   metric_type: "type-1"
#                   origin: egp
#                   originator_id: 192.0.2.34
#                   tag: 4
#                   weight: 4
#         state: replaced
# After state:

# vyos@vyos:~$ show configuration commands |  match "set policy route-map"
# set policy route-map test3 rule 1 set local-preference 6
# set policy route-map test3 rule 1 set metric 4
# set policy route-map test3 rule 1 set tag 4
# set policy route-map test3 rule 1 match metric 3
# set policy route-map test3 rule 1 match peer 192.0.2.35
# vyos@vyos:~$
#
#
# Module Execution:
#
# "after": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "description": "test",
#                     "on_match": {
#                         "next": true
#                     },
#                     "sequence": 1
#                 },
#                 {
#                     "action": "permit",
#                     "on_match": {
#                         "goto": 4
#                     },
#                     "sequence": 2
#                 }
#             ],
#             "route_map": "test2"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "match": {
#                         "metric": 3,
#                         "peer": "192.0.2.35",
#                         "rpki": "invalid"
#                     },
#                     "sequence": 1,
#                     "set": {
#                         "local_preference": "6",
#                         "metric": "4",
#                         "metric_type": "type-1",
#                         "origin": "egp",
#                         "originator_id": "192.0.2.34",
#                         "tag": "4",
#                         "weight": "4"
#                     }
#                 }
#             ],
#             "route_map": "test3"
#         }
#     ],
#     "before": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "description": "test",
#                     "on_match": {
#                         "next": true
#                     },
#                     "sequence": 1
#                 },
#                 {
#                     "action": "permit",
#                     "on_match": {
#                         "goto": 4
#                     },
#                     "sequence": 2
#                 }
#             ],
#             "route_map": "test2"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "match": {
#                         "metric": 1,
#                         "peer": "192.0.2.32",
#                         "rpki": "invalid"
#                     },
#                     "sequence": 1,
#                     "set": {
#                         "community": {
#                             "value": "internet"
#                         },
#                         "ip_next_hop": "192.0.2.33",
#                         "local_preference": "4",
#                         "metric": "5",
#                         "metric_type": "type-1",
#                         "origin": "egp",
#                         "originator_id": "192.0.2.34",
#                         "tag": "5",
#                         "weight": "4"
#                     }
#                 }
#             ],
#             "route_map": "test3"
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "delete policy route-map test3 rule 1 set ip-next-hop 192.0.2.33",
#         "set policy route-map test3 rule 1 set local-preference 6",
#         "set policy route-map test3 rule 1 set metric 4",
#         "set policy route-map test3 rule 1 set tag 4",
#         "delete policy route-map test3 rule 1 set community internet",
#         "set policy route-map test3 rule 1 match metric 3",
#         "set policy route-map test3 rule 1 match peer 192.0.2.35"
#     ],
#
# Using deleted:
# -------------

# Before state:
# vyos@vyos:~$ show configuration commands |  match "set policy route-map"
# set policy route-map test3 rule 1 set local-preference 6
# set policy route-map test3 rule 1 set metric 4
# set policy route-map test3 rule 1 set tag 4
# set policy route-map test3 rule 1 match metric 3
# set policy route-map test3 rule 1 match peer 192.0.2.35
# vyos@vyos:~$
#
# - name: Delete the provided configuration
#   register: result
#   vyos.vyos.vyos_route_maps:
#     config:
#     state: deleted
# After state:

# vyos@vyos:~$ show configuration commands |  match "set policy route-map"
# vyos@vyos:~$
#
#
# Module Execution:
#
# "after": [],
#     "before": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "match": {
#                         "metric": 3,
#                         "peer": "192.0.2.35",
#                     },
#                     "sequence": 1,
#                     "set": {
#                         "local_preference": "6",
#                         "metric": "4",
#                         "tag": "4",
#                     }
#                 }
#             ],
#             "route_map": "test3"
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "delete policy route-map test3"
#     ],
#
# using gathered:
# --------------
#
# Before state:
# vyos@vyos:~$ show configuration commands |  match "set policy route-maps"
#   set policy route-map test1 rule 1 description test
#   set policy route-map test1 rule 1 action permit
#   set policy route-map test1 rule 1 continue 2
#   set policy route-map test1 rule 1 on-match next
#   set policy route-map test3 rule 1 action permit
#   set policy route-map test3 rule 1 set local-preference 4
#   set policy route-map test3 rule 1 set metric 5
#   set policy route-map test3 rule 1 set metric-type type-1
#   set policy route-map test3 rule 1 set origin egp
#   set policy route-map test3 rule 1 set originator-id 192.0.2.34
#   set policy route-map test3 rule 1 set tag 5
#   set policy route-map test3 rule 1 set weight 4
#   set policy route-map test3 rule 1 match metric 1
#   set policy route-map test3 rule 1 match peer 192.0.2.32
#   set policy route-map test3 rule 1 match rpki invalid
#
# - name: gather configs
#     vyos.vyos.vyos_route_maps:
#       state: gathered

# "gathered": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "continue_sequence": 2,
#                     "description": "test",
#                     "on_match": {
#                         "next": true
#                     },
#                     "sequence": 1
#                 }
#             ],
#             "route_map": "test1"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "match": {
#                         "metric": 1,
#                         "peer": "192.0.2.32",
#                         "rpki": "invalid"
#                     },
#                     "sequence": 1,
#                     "set": {
#                         "local_preference": "4",
#                         "metric": "5",
#                         "metric_type": "type-1",
#                         "origin": "egp",
#                         "originator_id": "192.0.2.34",
#                         "tag": "5",
#                         "weight": "4"
#                     }
#                 }
#             ],
#             "route_map": "test3"
#         }
#     ]

# Using parsed:
# ------------

# parsed.cfg
# set policy route-map test1 rule 1 description test
# set policy route-map test1 rule 1 action permit
# set policy route-map test1 rule 1 continue 2
# set policy route-map test1 rule 1 on-match next
# set policy route-map test3 rule 1 action permit
# set policy route-map test3 rule 1 set local-preference 4
# set policy route-map test3 rule 1 set metric 5
# set policy route-map test3 rule 1 set metric-type type-1
# set policy route-map test3 rule 1 set origin egp
# set policy route-map test3 rule 1 set originator-id 192.0.2.34
# set policy route-map test3 rule 1 set tag 5
# set policy route-map test3 rule 1 set weight 4
# set policy route-map test3 rule 1 match metric 1
# set policy route-map test3 rule 1 match peer 192.0.2.32
# set policy route-map test3 rule 1 match rpki invalid
#
# - name: parse configs
#   vyos.vyos.vyos_route_maps:
#     running_config: "{{ lookup('file', './parsed.cfg') }}"
#     state: parsed
#   tags:
#     - parsed
#
# Module execution:
# "parsed": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "continue_sequence": 2,
#                     "description": "test",
#                     "on_match": {
#                         "next": true
#                     },
#                     "sequence": 1
#                 }
#             ],
#             "route_map": "test1"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "match": {
#                         "metric": 1,
#                         "peer": "192.0.2.32",
#                         "rpki": "invalid"
#                     },
#                     "sequence": 1,
#                     "set": {
#                         "local_preference": "4",
#                         "metric": "5",
#                         "metric_type": "type-1",
#                         "origin": "egp",
#                         "originator_id": "192.0.2.34",
#                         "tag": "5",
#                         "weight": "4"
#                     }
#                 }
#             ],
#             "route_map": "test3"
#         }
#     ]
#
#
# Using rendered:
# --------------
# - name: Structure provided configuration into device specific commands
#       register: result
#       vyos.vyos.vyos_route_maps: &id001
#         config:
#           - route_map: test1
#             entries:
#               - sequence: 1
#                 description: "test"
#                 action: permit
#                 continue_sequence: 2
#                 on_match:
#                   next: True
#           - route_map: test3
#             entries:
#               - sequence: 1
#                 action: permit
#                 match:
#                   rpki: invalid
#                   metric: 1
#                   peer: 192.0.2.32
#                 set:
#                   local_preference: 4
#                   metric: 5
#                   metric_type: "type-1"
#                   origin: egp
#                   originator_id: 192.0.2.34
#                   tag: 5
#                   weight: 4
#         state: rendered
# Module Execution:
# "rendered": [
#         "set policy route-map test1 rule 1 description test",
#         "set policy route-map test1 rule 1 action permit",
#         "set policy route-map test1 rule 1 continue 2",
#         "set policy route-map test1 rule 1 on-match next",
#         "set policy route-map test3 rule 1 action permit",
#         "set policy route-map test3 rule 1 set local-preference 4",
#         "set policy route-map test3 rule 1 set metric 5",
#         "set policy route-map test3 rule 1 set metric-type type-1",
#         "set policy route-map test3 rule 1 set origin egp",
#         "set policy route-map test3 rule 1 set originator-id 192.0.2.34",
#         "set policy route-map test3 rule 1 set tag 5",
#         "set policy route-map test3 rule 1 set weight 4",
#         "set policy route-map test3 rule 1 match metric 1",
#         "set policy route-map test3 rule 1 match peer 192.0.2.32",
#         "set policy route-map test3 rule 1 match rpki invalid"
#     ]
#
#
# Using overridden:
# --------------
# Before state:
# vyos@vyos:~$ show configuration commands |  match "set policy route-map"
# set policy route-map test2 rule 1 action 'permit'
# set policy route-map test2 rule 1 description 'test'
# set policy route-map test2 rule 1 on-match next
# set policy route-map test2 rule 2 action 'permit'
# set policy route-map test2 rule 2 on-match goto '4'
# set policy route-map test3 rule 1 action 'permit'
# set policy route-map test3 rule 1 match metric '1'
# set policy route-map test3 rule 1 match peer '192.0.2.32'
# set policy route-map test3 rule 1 match rpki 'invalid'
# set policy route-map test3 rule 1 set community 'internet'
# set policy route-map test3 rule 1 set ip-next-hop '192.0.2.33'
# set policy route-map test3 rule 1 set local-preference '4'
# set policy route-map test3 rule 1 set metric '5'
# set policy route-map test3 rule 1 set metric-type 'type-1'
# set policy route-map test3 rule 1 set origin 'egp'
# set policy route-map test3 rule 1 set originator-id '192.0.2.34'
# set policy route-map test3 rule 1 set tag '5'
# set policy route-map test3 rule 1 set weight '4'
#
#     - name: Override the existing configuration with the provided running configuration
#       register: result
#       vyos.vyos.vyos_route_maps: &id001
#         config:
#           - route_map: test3
#             entries:
#               - sequence: 1
#                 action: permit
#                 match:
#                   rpki: invalid
#                   metric: 3
#                   peer: 192.0.2.35
#                 set:
#                   local_preference: 6
#                   metric: 4
#                   metric_type: "type-1"
#                   origin: egp
#                   originator_id: 192.0.2.34
#                   tag: 4
#                   weight: 4
#         state: overridden
# After state:

# vyos@vyos:~$ show configuration commands |  match "set policy route-map"
# set policy route-map test3 rule 1 set metric-type 'type-1'
# set policy route-map test3 rule 1 set origin 'egp'
# set policy route-map test3 rule 1 set originator-id '192.0.2.34'
# set policy route-map test3 rule 1 set weight '4'
# set policy route-map test3 rule 1 set local-preference 6
# set policy route-map test3 rule 1 set metric 4
# set policy route-map test3 rule 1 set tag 4
# set policy route-map test3 rule 1 match metric 3
# set policy route-map test3 rule 1 match peer 192.0.2.35
# set policy route-map test3 rule 1 match rpki 'invalid'

# Module Execution:
# "after": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "match": {
#                         "metric": 3,
#                         "peer": "192.0.2.35",
#                         "rpki": "invalid"
#                     },
#                     "sequence": 1,
#                     "set": {
#                         "local_preference": "6",
#                         "metric": "4",
#                         "metric_type": "type-1",
#                         "origin": "egp",
#                         "originator_id": "192.0.2.34",
#                         "tag": "4",
#                         "weight": "4"
#                     }
#                 }
#             ],
#             "route_map": "test3"
#         }
#     ],
#     "before": [
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "description": "test",
#                     "on_match": {
#                         "next": true
#                     },
#                     "sequence": 1
#                 },
#                 {
#                     "action": "permit",
#                     "on_match": {
#                         "goto": 4
#                     },
#                     "sequence": 2
#                 }
#             ],
#             "route_map": "test2"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "permit",
#                     "match": {
#                         "metric": 1,
#                         "peer": "192.0.2.32",
#                         "rpki": "invalid"
#                     },
#                     "sequence": 1,
#                     "set": {
#                         "community": {
#                             "value": "internet"
#                         },
#                         "ip_next_hop": "192.0.2.33",
#                         "local_preference": "4",
#                         "metric": "5",
#                         "metric_type": "type-1",
#                         "origin": "egp",
#                         "originator_id": "192.0.2.34",
#                         "tag": "5",
#                         "weight": "4"
#                     }
#                 }
#             ],
#             "route_map": "test3"
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "delete policy route-map test2",
#         "delete policy route-map test3 rule 1 set ip-next-hop 192.0.2.33",
#         "set policy route-map test3 rule 1 set local-preference 6",
#         "set policy route-map test3 rule 1 set metric 4",
#         "set policy route-map test3 rule 1 set tag 4",
#         "delete policy route-map test3 rule 1 set community internet",
#         "set policy route-map test3 rule 1 match metric 3",
#         "set policy route-map test3 rule 1 match peer 192.0.2.35"
#     ],
#
```

### Authors

- Ashwini Mhatre (@amhatre)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
