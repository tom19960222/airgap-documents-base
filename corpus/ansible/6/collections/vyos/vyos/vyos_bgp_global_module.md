---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_bgp_global module – BGP Global Resource Module."
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_bgp_global_module.html
fetched_at: 2026-07-28T00:23:13+00:00
---
# vyos.vyos.vyos_bgp_global module – BGP Global Resource Module.

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
> To use it in a playbook, specify: `vyos.vyos.vyos_bgp_global`.

New in vyos.vyos 2.0.0

- [Synopsis](vyos_bgp_global_module.md#synopsis)
- [Parameters](vyos_bgp_global_module.md#parameters)
- [Examples](vyos_bgp_global_module.md#examples)

## [Synopsis](vyos_bgp_global_module.md#id1)

- This module manages BGP global configuration of interfaces on devices running VYOS.

## [Parameters](vyos_bgp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dict of BGP global configuration for interfaces. |
| **aggregate_address**  list / elements=dictionary | BGP aggregate network. |
| **as_set**  boolean | Generate AS-set path information for this aggregate address.  Choices:   - `false` - `true` |
| **prefix**  string | BGP aggregate network. |
| **summary_only**  boolean | Announce the aggregate summary network only.  Choices:   - `false` - `true` |
| **as_number**  integer | AS number. |
| **bgp_params**  dictionary | BGP parameters |
| **always_compare_med**  boolean | Always compare MEDs from different neighbors  Choices:   - `false` - `true` |
| **bestpath**  dictionary | Default bestpath selection mechanism |
| **as_path**  string | AS-path attribute comparison parameters  Choices:   - `"confed"` - `"ignore"` |
| **compare_routerid**  boolean | Compare the router-id for identical EBGP paths  Choices:   - `false` - `true` |
| **med**  string | MED attribute comparison parameters  Choices:   - `"confed"` - `"missing-as-worst"` |
| **cluster_id**  string | Route-reflector cluster-id |
| **confederation**  list / elements=dictionary | AS confederation parameters |
| **identifier**  integer | Confederation AS identifier |
| **peers**  integer | Peer ASs in the BGP confederation |
| **dampening**  dictionary | Enable route-flap dampening |
| **half_life**  integer | Half-life penalty in seconds |
| **max_suppress_time**  integer | Maximum duration to suppress a stable route |
| **re_use**  integer | Time to start reusing a route |
| **start_suppress_time**  integer | When to start suppressing a route |
| **default**  dictionary | BGP defaults |
| **local_pref**  integer | Default local preference |
| **no_ipv4_unicast**  boolean | Deactivate IPv4 unicast for a peer by default  Choices:   - `false` - `true` |
| **deterministic_med**  boolean | Compare MEDs between different peers in the same AS  Choices:   - `false` - `true` |
| **disable_network_import_check**  boolean | Disable IGP route check for network statements  Choices:   - `false` - `true` |
| **distance**  list / elements=dictionary | Administrative distances for BGP routes |
| **prefix**  integer | Administrative distance for a specific BGP prefix |
| **type**  string | Type of route  Choices:   - `"external"` - `"internal"` - `"local"` |
| **value**  integer | distance |
| **enforce_first_as**  boolean | Require first AS in the path to match peer’s AS  Choices:   - `false` - `true` |
| **graceful_restart**  integer | Maximum time to hold onto restarting peer’s stale paths |
| **log_neighbor_changes**  boolean | Log neighbor up/down changes and reset reason  Choices:   - `false` - `true` |
| **no_client_to_client_reflection**  boolean | Disable client to client route reflection  Choices:   - `false` - `true` |
| **no_fast_external_failover**  boolean | Disable immediate session reset if peer’s connected link goes down  Choices:   - `false` - `true` |
| **router_id**  string | BGP router-id |
| **scan_time**  integer | BGP route scanner interval |
| **maximum_paths**  list / elements=dictionary | BGP multipaths |
| **count**  integer | No. of paths. |
| **path**  string | BGP multipaths |
| **neighbor**  list / elements=dictionary | BGP neighbor |
| **address**  string | BGP neighbor address (v4/v6). |
| **advertisement_interval**  integer | Minimum interval for sending routing updates. |
| **allowas_in**  integer | Number of occurrences of AS number. |
| **as_override**  boolean | AS for routes sent to this neighbor to be the local AS.  Choices:   - `false` - `true` |
| **attribute_unchanged**  dictionary | BGP attributes are sent unchanged. |
| **as_path**  boolean | as_path  Choices:   - `false` - `true` |
| **med**  boolean | med  Choices:   - `false` - `true` |
| **next_hop**  boolean | next_hop  Choices:   - `false` - `true` |
| **capability**  dictionary | Advertise capabilities to this neighbor. |
| **dynamic**  boolean | Advertise dynamic capability to this neighbor.  Choices:   - `false` - `true` |
| **orf**  string | Advertise ORF capability to this neighbor.  Choices:   - `"send"` - `"receive"` |
| **default_originate**  string | Send default route to this neighbor |
| **description**  string | description text |
| **disable_capability_negotiation**  boolean | Disbale capability negotiation with the neighbor  Choices:   - `false` - `true` |
| **disable_connected_check**  boolean | Disable check to see if EBGP peer’s address is a connected route.  Choices:   - `false` - `true` |
| **disable_send_community**  string | Disable sending community attributes to this neighbor.  Choices:   - `"extended"` - `"standard"` |
| **distribute_list**  list / elements=dictionary | Access-list to filter route updates to/from this neighbor. |
| **acl**  integer | Access-list number. |
| **action**  string | Access-list to filter outgoing/incoming route updates to this neighbor  Choices:   - `"export"` - `"import"` |
| **ebgp_multihop**  integer | Allow this EBGP neighbor to not be on a directly connected network. Specify the number hops. |
| **filter_list**  list / elements=dictionary | As-path-list to filter route updates to/from this neighbor. |
| **action**  string | filter outgoing/incoming route updates  Choices:   - `"export"` - `"import"` |
| **path_list**  string | As-path-list to filter |
| **local_as**  integer | local as number not to be prepended to updates from EBGP peers |
| **maximum_prefix**  integer | Maximum number of prefixes to accept from this neighbor nexthop-self Nexthop for routes sent to this neighbor to be the local router. |
| **nexthop_self**  boolean | Nexthop for routes sent to this neighbor to be the local router.  Choices:   - `false` - `true` |
| **override_capability**  boolean | Ignore capability negotiation with specified neighbor.  Choices:   - `false` - `true` |
| **passive**  boolean | Do not initiate a session with this neighbor  Choices:   - `false` - `true` |
| **password**  string | BGP MD5 password |
| **peer_group**  boolean | True if all the configs under this neighbor key is for peer group template.  Choices:   - `false` - `true` |
| **peer_group_name**  string | IPv4 peer group for this peer |
| **port**  integer | Neighbor’s BGP port |
| **prefix_list**  list / elements=dictionary | Prefix-list to filter route updates to/from this neighbor. |
| **action**  string | filter outgoing/incoming route updates  Choices:   - `"export"` - `"import"` |
| **prefix_list**  string | Prefix-list to filter |
| **remote_as**  integer | Neighbor BGP AS number |
| **remove_private_as**  boolean | Remove private AS numbers from AS path in outbound route updates  Choices:   - `false` - `true` |
| **route_map**  list / elements=dictionary | Route-map to filter route updates to/from this neighbor. |
| **action**  string | filter outgoing/incoming route updates  Choices:   - `"export"` - `"import"` |
| **route_map**  string | route-map to filter |
| **route_reflector_client**  boolean | Neighbor as a route reflector client  Choices:   - `false` - `true` |
| **route_server_client**  boolean | Neighbor is route server client  Choices:   - `false` - `true` |
| **shutdown**  boolean | Administratively shut down neighbor  Choices:   - `false` - `true` |
| **soft_reconfiguration**  boolean | Soft reconfiguration for neighbor  Choices:   - `false` - `true` |
| **strict_capability_match**  boolean | Enable strict capability negotiation  Choices:   - `false` - `true` |
| **timers**  dictionary | Neighbor timers |
| **connect**  integer | BGP connect timer for this neighbor. |
| **holdtime**  integer | BGP hold timer for this neighbor |
| **keepalive**  integer | BGP keepalive interval for this neighbor |
| **ttl_security**  integer | Ttl security mechanism for this BGP peer |
| **unsuppress_map**  string | Route-map to selectively unsuppress suppressed routes |
| **update_source**  string | Source IP of routing updates |
| **weight**  integer | Default weight for routes from this neighbor |
| **network**  list / elements=dictionary | BGP network |
| **address**  string | BGP network address |
| **backdoor**  boolean | Network as a backdoor route  Choices:   - `false` - `true` |
| **route_map**  string | Route-map to modify route attributes |
| **redistribute**  list / elements=dictionary | Redistribute routes from other protocols into BGP |
| **metric**  integer | Metric for redistributed routes. |
| **protocol**  string | types of routes to be redistributed.  Choices:   - `"connected"` - `"kernel"` - `"ospf"` - `"rip"` - `"static"` |
| **route_map**  string | Route map to filter redistributed routes |
| **timers**  dictionary | BGP protocol timers |
| **holdtime**  integer | Hold time interval |
| **keepalive**  integer | Keepalive interval |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section bgp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  State *purged* removes all the BGP configurations from the target device. Use caution with this state.(‘delete protocols bgp <x>’)  State *deleted* only removes BGP attributes that this modules manages and does not negate the BGP process completely. Thereby, preserving address-family related configurations under BGP context.  Running states *deleted* and *replaced* will result in an error if there are address-family configuration lines present under neighbor context that is is to be removed. Please use the [vyos.vyos.vyos_bgp_address_family](vyos_bgp_address_family_module.md#ansible-collections-vyos-vyos-vyos-bgp-address-family-module) module for prior cleanup.  Refer to examples for more details.  Choices:   - `"deleted"` - `"merged"` ← (default) - `"purged"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Examples](vyos_bgp_global_module.md#id3)

```yaml+jinja
# Using merged
# Before state

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# vyos@vyos:~$

  - name: Merge provided configuration with device configuration
    vyos.vyos.vyos_bgp_global:
      config:
        as_number: "65536"
        aggregate_address:
          - prefix: "203.0.113.0/24"
            as_set: true
          - prefix: "192.0.2.0/24"
            summary_only: true
        network:
          - address: "192.1.13.0/24"
            backdoor: true
        redistribute:
          - protocol: "kernel"
            metric: 45
          - protocol: "connected"
            route_map: "map01"
        maximum_paths:
          - path: "ebgp"
            count: 20
          - path: "ibgp"
            count: 55
        timers:
          keepalive: 35
        bgp_params:
          bestpath:
            as_path: "confed"
            compare_routerid: true
          default:
            no_ipv4_unicast: true
          router_id: "192.1.2.9"
          confederation:
            - peers: 20
            - peers: 55
            - identifier: 66
        neighbor:
          - address: "192.0.2.25"
            disable_connected_check: true
            timers:
              holdtime: 30
              keepalive: 10
          - address: "203.0.113.5"
            attribute_unchanged:
              as_path: true
              med: true
            ebgp_multihop: 2
            remote_as: 101
            update_source: "192.0.2.25"
          - address: "5001::64"
            maximum_prefix: 34
            distribute_list:
              - acl: 20
                action: "export"
              - acl: 40
                action: "import"

      state: merged

# After State
# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp 65536 aggregate-address 192.0.2.0/24 'summary-only'
# set protocols bgp 65536 aggregate-address 203.0.113.0/24 'as-set'
# set protocols bgp 65536 maximum-paths ebgp '20'
# set protocols bgp 65536 maximum-paths ibgp '55'
# set protocols bgp 65536 neighbor 192.0.2.25 'disable-connected-check'
# set protocols bgp 65536 neighbor 192.0.2.25 timers holdtime '30'
# set protocols bgp 65536 neighbor 192.0.2.25 timers keepalive '10'
# set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'as-path'
# set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'med'
# set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'next-hop'
# set protocols bgp 65536 neighbor 203.0.113.5 ebgp-multihop '2'
# set protocols bgp 65536 neighbor 203.0.113.5 remote-as '101'
# set protocols bgp 65536 neighbor 203.0.113.5 update-source '192.0.2.25'
# set protocols bgp 65536 neighbor 5001::64 distribute-list export '20'
# set protocols bgp 65536 neighbor 5001::64 distribute-list import '40'
# set protocols bgp 65536 neighbor 5001::64 maximum-prefix '34'
# set protocols bgp 65536 network 192.1.13.0/24 'backdoor'
# set protocols bgp 65536 parameters bestpath as-path 'confed'
# set protocols bgp 65536 parameters bestpath 'compare-routerid'
# set protocols bgp 65536 parameters confederation identifier '66'
# set protocols bgp 65536 parameters confederation peers '20'
# set protocols bgp 65536 parameters confederation peers '55'
# set protocols bgp 65536 parameters default 'no-ipv4-unicast'
# set protocols bgp 65536 parameters router-id '192.1.2.9'
# set protocols bgp 65536 redistribute connected route-map 'map01'
# set protocols bgp 65536 redistribute kernel metric '45'
# set protocols bgp 65536 timers keepalive '35'
# vyos@vyos:~$
#
# # Module Execution:
#
# "after": {
#         "aggregate_address": [
#             {
#                 "prefix": "192.0.2.0/24",
#                 "summary_only": true
#             },
#             {
#                 "prefix": "203.0.113.0/24",
#                 "as_set": true
#             }
#         ],
#         "as_number": 65536,
#         "bgp_params": {
#             "bestpath": {
#                 "as_path": "confed",
#                 "compare_routerid": true
#             },
#             "confederation": [
#                 {
#                     "identifier": 66
#                 },
#                 {
#                     "peers": 20
#                 },
#                 {
#                     "peers": 55
#                 }
#             ],
#             "default": {
#                 "no_ipv4_unicast": true
#             },
#             "router_id": "192.1.2.9"
#         },
#         "maximum_paths": [
#             {
#                 "count": 20,
#                 "path": "ebgp"
#             },
#             {
#                 "count": 55,
#                 "path": "ibgp"
#             }
#         ],
#         "neighbor": [
#             {
#                 "address": "192.0.2.25",
#                 "disable_connected_check": true,
#                 "timers": {
#                     "holdtime": 30,
#                     "keepalive": 10
#                 }
#             },
#             {
#                 "address": "203.0.113.5",
#                 "attribute_unchanged": {
#                     "as_path": true,
#                     "med": true,
#                     "next_hop": true
#                 },
#                 "ebgp_multihop": 2,
#                 "remote_as": 101,
#                 "update_source": "192.0.2.25"
#             },
#             {
#                 "address": "5001::64",
#                 "distribute_list": [
#                     {
#                         "acl": 20,
#                         "action": "export"
#                     },
#                     {
#                         "acl": 40,
#                         "action": "import"
#                     }
#                 ],
#                 "maximum_prefix": 34
#             }
#         ],
#         "network": [
#             {
#                 "address": "192.1.13.0/24",
#                 "backdoor": true
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "connected",
#                 "route_map": "map01"
#             },
#             {
#                 "metric": 45,
#                 "protocol": "kernel"
#             }
#         ],
#         "timers": {
#             "keepalive": 35
#         }
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#         "set protocols bgp 65536 neighbor 192.0.2.25 disable-connected-check",
#         "set protocols bgp 65536 neighbor 192.0.2.25 timers holdtime 30",
#         "set protocols bgp 65536 neighbor 192.0.2.25 timers keepalive 10",
#         "set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged as-path",
#         "set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged med",
#         "set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged next-hop",
#         "set protocols bgp 65536 neighbor 203.0.113.5 ebgp-multihop 2",
#         "set protocols bgp 65536 neighbor 203.0.113.5 remote-as 101",
#         "set protocols bgp 65536 neighbor 203.0.113.5 update-source 192.0.2.25",
#         "set protocols bgp 65536 neighbor 5001::64 maximum-prefix 34",
#         "set protocols bgp 65536 neighbor 5001::64 distribute-list export 20",
#         "set protocols bgp 65536 neighbor 5001::64 distribute-list import 40",
#         "set protocols bgp 65536 redistribute kernel metric 45",
#         "set protocols bgp 65536 redistribute connected route-map map01",
#         "set protocols bgp 65536 network 192.1.13.0/24 backdoor",
#         "set protocols bgp 65536 aggregate-address 203.0.113.0/24 as-set",
#         "set protocols bgp 65536 aggregate-address 192.0.2.0/24 summary-only",
#         "set protocols bgp 65536 parameters bestpath as-path confed",
#         "set protocols bgp 65536 parameters bestpath compare-routerid",
#         "set protocols bgp 65536 parameters default no-ipv4-unicast",
#         "set protocols bgp 65536 parameters router-id 192.1.2.9",
#         "set protocols bgp 65536 parameters confederation peers 20",
#         "set protocols bgp 65536 parameters confederation peers 55",
#         "set protocols bgp 65536 parameters confederation identifier 66",
#         "set protocols bgp 65536 maximum-paths ebgp 20",
#         "set protocols bgp 65536 maximum-paths ibgp 55",
#         "set protocols bgp 65536 timers keepalive 35"
#     ],

# Using replaced:
# --------------

# Before state:

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp 65536 aggregate-address 192.0.2.0/24 'summary-only'
# set protocols bgp 65536 aggregate-address 203.0.113.0/24 'as-set'
# set protocols bgp 65536 maximum-paths ebgp '20'
# set protocols bgp 65536 maximum-paths ibgp '55'
# set protocols bgp 65536 neighbor 192.0.2.25 'disable-connected-check'
# set protocols bgp 65536 neighbor 192.0.2.25 timers holdtime '30'
# set protocols bgp 65536 neighbor 192.0.2.25 timers keepalive '10'
# set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'as-path'
# set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'med'
# set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'next-hop'
# set protocols bgp 65536 neighbor 203.0.113.5 ebgp-multihop '2'
# set protocols bgp 65536 neighbor 203.0.113.5 remote-as '101'
# set protocols bgp 65536 neighbor 203.0.113.5 update-source '192.0.2.25'
# set protocols bgp 65536 neighbor 5001::64 distribute-list export '20'
# set protocols bgp 65536 neighbor 5001::64 distribute-list import '40'
# set protocols bgp 65536 neighbor 5001::64 maximum-prefix '34'
# set protocols bgp 65536 network 192.1.13.0/24 'backdoor'
# set protocols bgp 65536 parameters bestpath as-path 'confed'
# set protocols bgp 65536 parameters bestpath 'compare-routerid'
# set protocols bgp 65536 parameters confederation identifier '66'
# set protocols bgp 65536 parameters confederation peers '20'
# set protocols bgp 65536 parameters confederation peers '55'
# set protocols bgp 65536 parameters default 'no-ipv4-unicast'
# set protocols bgp 65536 parameters router-id '192.1.2.9'
# set protocols bgp 65536 redistribute connected route-map 'map01'
# set protocols bgp 65536 redistribute kernel metric '45'
# set protocols bgp 65536 timers keepalive '35'
# vyos@vyos:~$

  - name: Replace
    vyos.vyos.vyos_bgp_global:
      config:
        as_number: "65536"
        network:
          - address: "203.0.113.0/24"
            route_map: map01
        redistribute:
          - protocol: "static"
            route_map: "map01"
        neighbor:
          - address: "192.0.2.40"
            advertisement_interval: 72
            capability:
              orf: "receive"
        bgp_params:
          bestpath:
            as_path: "confed"

      state: replaced
# After state:

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp 65536 neighbor 192.0.2.40 advertisement-interval '72'
# set protocols bgp 65536 neighbor 192.0.2.40 capability orf prefix-list 'receive'
# set protocols bgp 65536 network 203.0.113.0/24 route-map 'map01'
# set protocols bgp 65536 parameters bestpath as-path 'confed'
# set protocols bgp 65536 redistribute static route-map 'map01'
# vyos@vyos:~$
#
#
# Module Execution:
#
# "after": {
#         "as_number": 65536,
#         "bgp_params": {
#             "bestpath": {
#                 "as_path": "confed"
#             }
#         },
#         "neighbor": [
#             {
#                 "address": "192.0.2.40",
#                 "advertisement_interval": 72,
#                 "capability": {
#                     "orf": "receive"
#                 }
#             }
#         ],
#         "network": [
#             {
#                 "address": "203.0.113.0/24",
#                 "route_map": "map01"
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "static",
#                 "route_map": "map01"
#             }
#         ]
#     },
#     "before": {
#         "aggregate_address": [
#             {
#                 "prefix": "192.0.2.0/24",
#                 "summary_only": true
#             },
#             {
#                 "prefix": "203.0.113.0/24",
#                 "as_set": true
#             }
#         ],
#         "as_number": 65536,
#         "bgp_params": {
#             "bestpath": {
#                 "as_path": "confed",
#                 "compare_routerid": true
#             },
#             "confederation": [
#                 {
#                     "identifier": 66
#                 },
#                 {
#                     "peers": 20
#                 },
#                 {
#                     "peers": 55
#                 }
#             ],
#             "default": {
#                 "no_ipv4_unicast": true
#             },
#             "router_id": "192.1.2.9"
#         },
#         "maximum_paths": [
#             {
#                 "count": 20,
#                 "path": "ebgp"
#             },
#             {
#                 "count": 55,
#                 "path": "ibgp"
#             }
#         ],
#         "neighbor": [
#             {
#                 "address": "192.0.2.25",
#                 "disable_connected_check": true,
#                 "timers": {
#                     "holdtime": 30,
#                     "keepalive": 10
#                 }
#             },
#             {
#                 "address": "203.0.113.5",
#                 "attribute_unchanged": {
#                     "as_path": true,
#                     "med": true,
#                     "next_hop": true
#                 },
#                 "ebgp_multihop": 2,
#                 "remote_as": 101,
#                 "update_source": "192.0.2.25"
#             },
#             {
#                 "address": "5001::64",
#                 "distribute_list": [
#                     {
#                         "acl": 20,
#                         "action": "export"
#                     },
#                     {
#                         "acl": 40,
#                         "action": "import"
#                     }
#                 ],
#                 "maximum_prefix": 34
#             }
#         ],
#         "network": [
#             {
#                 "address": "192.1.13.0/24",
#                 "backdoor": true
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "connected",
#                 "route_map": "map01"
#             },
#             {
#                 "metric": 45,
#                 "protocol": "kernel"
#             }
#         ],
#         "timers": {
#             "keepalive": 35
#         }
#     },
#     "changed": true,
#     "commands": [
#         "delete protocols bgp 65536 timers",
#         "delete protocols bgp 65536 maximum-paths ",
#         "delete protocols bgp 65536 maximum-paths ",
#         "delete protocols bgp 65536 parameters router-id 192.1.2.9",
#         "delete protocols bgp 65536 parameters default",
#         "delete protocols bgp 65536 parameters confederation",
#         "delete protocols bgp 65536 parameters bestpath compare-routerid",
#         "delete protocols bgp 65536 aggregate-address",
#         "delete protocols bgp 65536 network 192.1.13.0/24",
#         "delete protocols bgp 65536 redistribute kernel",
#         "delete protocols bgp 65536 redistribute kernel",
#         "delete protocols bgp 65536 redistribute connected",
#         "delete protocols bgp 65536 redistribute connected",
#         "delete protocols bgp 65536 neighbor 5001::64",
#         "delete protocols bgp 65536 neighbor 203.0.113.5",
#         "delete protocols bgp 65536 neighbor 192.0.2.25",
#         "set protocols bgp 65536 neighbor 192.0.2.40 advertisement-interval 72",
#         "set protocols bgp 65536 neighbor 192.0.2.40 capability orf prefix-list receive",
#         "set protocols bgp 65536 redistribute static route-map map01",
#         "set protocols bgp 65536 network 203.0.113.0/24 route-map map01"
#     ],

# Using deleted:
# -------------

# Before state:

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp 65536 neighbor 192.0.2.40 advertisement-interval '72'
# set protocols bgp 65536 neighbor 192.0.2.40 capability orf prefix-list 'receive'
# set protocols bgp 65536 network 203.0.113.0/24 route-map 'map01'
# set protocols bgp 65536 parameters bestpath as-path 'confed'
# set protocols bgp 65536 redistribute static route-map 'map01'
# vyos@vyos:~$

  - name: Delete configuration
    vyos.vyos.vyos_bgp_global:
      config:
        as_number: "65536"
      state: deleted

# After state:

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp '65536'
# vyos@vyos:~$
#
#
# Module Execution:
#
# "after": {
#         "as_number": 65536
#     },
#     "before": {
#         "as_number": 65536,
#         "bgp_params": {
#             "bestpath": {
#                 "as_path": "confed"
#             }
#         },
#         "neighbor": [
#             {
#                 "address": "192.0.2.40",
#                 "advertisement_interval": 72,
#                 "capability": {
#                     "orf": "receive"
#                 }
#             }
#         ],
#         "network": [
#             {
#                 "address": "203.0.113.0/24",
#                 "route_map": "map01"
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "static",
#                 "route_map": "map01"
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#         "delete protocols bgp 65536 neighbor 192.0.2.40",
#         "delete protocols bgp 65536 redistribute",
#         "delete protocols bgp 65536 network",
#         "delete protocols bgp 65536 parameters"
#     ],

# Using purged:

# Before state:

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp 65536 aggregate-address 192.0.2.0/24 'summary-only'
# set protocols bgp 65536 aggregate-address 203.0.113.0/24 'as-set'
# set protocols bgp 65536 maximum-paths ebgp '20'
# set protocols bgp 65536 maximum-paths ibgp '55'
# set protocols bgp 65536 neighbor 192.0.2.25 'disable-connected-check'
# set protocols bgp 65536 neighbor 192.0.2.25 timers holdtime '30'
# set protocols bgp 65536 neighbor 192.0.2.25 timers keepalive '10'
# set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'as-path'
# set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'med'
# set protocols bgp 65536 neighbor 203.0.113.5 attribute-unchanged 'next-hop'
# set protocols bgp 65536 neighbor 203.0.113.5 ebgp-multihop '2'
# set protocols bgp 65536 neighbor 203.0.113.5 remote-as '101'
# set protocols bgp 65536 neighbor 203.0.113.5 update-source '192.0.2.25'
# set protocols bgp 65536 neighbor 5001::64 distribute-list export '20'
# set protocols bgp 65536 neighbor 5001::64 distribute-list import '40'
# set protocols bgp 65536 neighbor 5001::64 maximum-prefix '34'
# set protocols bgp 65536 network 192.1.13.0/24 'backdoor'
# set protocols bgp 65536 parameters bestpath as-path 'confed'
# set protocols bgp 65536 parameters bestpath 'compare-routerid'
# set protocols bgp 65536 parameters confederation identifier '66'
# set protocols bgp 65536 parameters confederation peers '20'
# set protocols bgp 65536 parameters confederation peers '55'
# set protocols bgp 65536 parameters default 'no-ipv4-unicast'
# set protocols bgp 65536 parameters router-id '192.1.2.9'
# set protocols bgp 65536 redistribute connected route-map 'map01'
# set protocols bgp 65536 redistribute kernel metric '45'
# set protocols bgp 65536 timers keepalive '35'
# vyos@vyos:~$

  - name: Purge configuration
    vyos.vyos.vyos_bgp_global:
      config:
        as_number: "65536"
      state: purged

# After state:

# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# vyos@vyos:~$
#
# Module Execution:
#
#     "after": {},
#     "before": {
#         "aggregate_address": [
#             {
#                 "prefix": "192.0.2.0/24",
#                 "summary_only": true
#             },
#             {
#                 "prefix": "203.0.113.0/24",
#                 "as_set": true
#             }
#         ],
#         "as_number": 65536,
#         "bgp_params": {
#             "bestpath": {
#                 "as_path": "confed",
#                 "compare_routerid": true
#             },
#             "confederation": [
#                 {
#                     "identifier": 66
#                 },
#                 {
#                     "peers": 20
#                 },
#                 {
#                     "peers": 55
#                 }
#             ],
#             "default": {
#                 "no_ipv4_unicast": true
#             },
#             "router_id": "192.1.2.9"
#         },
#         "maximum_paths": [
#             {
#                 "count": 20,
#                 "path": "ebgp"
#             },
#             {
#                 "count": 55,
#                 "path": "ibgp"
#             }
#         ],
#         "neighbor": [
#             {
#                 "address": "192.0.2.25",
#                 "disable_connected_check": true,
#                 "timers": {
#                     "holdtime": 30,
#                     "keepalive": 10
#                 }
#             },
#             {
#                 "address": "203.0.113.5",
#                 "attribute_unchanged": {
#                     "as_path": true,
#                     "med": true,
#                     "next_hop": true
#                 },
#                 "ebgp_multihop": 2,
#                 "remote_as": 101,
#                 "update_source": "192.0.2.25"
#             },
#             {
#                 "address": "5001::64",
#                 "distribute_list": [
#                     {
#                         "acl": 20,
#                         "action": "export"
#                     },
#                     {
#                         "acl": 40,
#                         "action": "import"
#                     }
#                 ],
#                 "maximum_prefix": 34
#             }
#         ],
#         "network": [
#             {
#                 "address": "192.1.13.0/24",
#                 "backdoor": true
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "connected",
#                 "route_map": "map01"
#             },
#             {
#                 "metric": 45,
#                 "protocol": "kernel"
#             }
#         ],
#         "timers": {
#             "keepalive": 35
#         }
#     },
#     "changed": true,
#     "commands": [
#         "delete protocols bgp 65536"
#     ],

# Deleted in presence of address family under neighbors:

# Before state:
# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp 65536 neighbor 192.0.2.43 advertisement-interval '72'
# set protocols bgp 65536 neighbor 192.0.2.43 capability 'dynamic'
# set protocols bgp 65536 neighbor 192.0.2.43 'disable-connected-check'
# set protocols bgp 65536 neighbor 192.0.2.43 timers holdtime '30'
# set protocols bgp 65536 neighbor 192.0.2.43 timers keepalive '10'
# set protocols bgp 65536 neighbor 203.0.113.0 address-family 'ipv6-unicast'
# set protocols bgp 65536 neighbor 203.0.113.0 capability orf prefix-list 'receive'
# set protocols bgp 65536 network 203.0.113.0/24 route-map 'map01'
# set protocols bgp 65536 parameters 'always-compare-med'
# set protocols bgp 65536 parameters bestpath as-path 'confed'
# set protocols bgp 65536 parameters bestpath 'compare-routerid'
# set protocols bgp 65536 parameters dampening half-life '33'
# set protocols bgp 65536 parameters dampening max-suppress-time '20'
# set protocols bgp 65536 parameters dampening re-use '60'
# set protocols bgp 65536 parameters dampening start-suppress-time '5'
# set protocols bgp 65536 parameters default 'no-ipv4-unicast'
# set protocols bgp 65536 parameters distance global external '66'
# set protocols bgp 65536 parameters distance global internal '20'
# set protocols bgp 65536 parameters distance global local '10'
# set protocols bgp 65536 redistribute static route-map 'map01'
# vyos@vyos:~$ ^C
# vyos@vyos:~$

  - name: Delete configuration
    vyos.vyos.vyos_bgp_global:
      config:
        as_number: "65536"
      state: deleted

# Module Execution:
#
# "changed": false,
#     "invocation": {
#         "module_args": {
#             "config": {
#                 "aggregate_address": null,
#                 "as_number": 65536,
#                 "bgp_params": null,
#                 "maximum_paths": null,
#                 "neighbor": null,
#                 "network": null,
#                 "redistribute": null,
#                 "timers": null
#             },
#             "running_config": null,
#             "state": "deleted"
#         }
#     },
#     "msg": "Use the _bgp_address_family module to delete the address_family under neighbor 203.0.113.0, before replacing/deleting the neighbor."
# }

# using gathered:
# --------------

# Before state:
# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# set protocols bgp 65536 neighbor 192.0.2.43 advertisement-interval '72'
# set protocols bgp 65536 neighbor 192.0.2.43 capability 'dynamic'
# set protocols bgp 65536 neighbor 192.0.2.43 'disable-connected-check'
# set protocols bgp 65536 neighbor 192.0.2.43 timers holdtime '30'
# set protocols bgp 65536 neighbor 192.0.2.43 timers keepalive '10'
# set protocols bgp 65536 neighbor 203.0.113.0 address-family 'ipv6-unicast'
# set protocols bgp 65536 neighbor 203.0.113.0 capability orf prefix-list 'receive'
# set protocols bgp 65536 network 203.0.113.0/24 route-map 'map01'
# set protocols bgp 65536 parameters 'always-compare-med'
# set protocols bgp 65536 parameters bestpath as-path 'confed'
# set protocols bgp 65536 parameters bestpath 'compare-routerid'
# set protocols bgp 65536 parameters dampening half-life '33'
# set protocols bgp 65536 parameters dampening max-suppress-time '20'
# set protocols bgp 65536 parameters dampening re-use '60'
# set protocols bgp 65536 parameters dampening start-suppress-time '5'
# set protocols bgp 65536 parameters default 'no-ipv4-unicast'
# set protocols bgp 65536 parameters distance global external '66'
# set protocols bgp 65536 parameters distance global internal '20'
# set protocols bgp 65536 parameters distance global local '10'
# set protocols bgp 65536 redistribute static route-map 'map01'
# vyos@vyos:~$ ^C

  - name: gather configs
    vyos.vyos.vyos_bgp_global:
      state: gathered

# Module Execution:
# "gathered": {
#         "as_number": 65536,
#         "bgp_params": {
#             "always_compare_med": true,
#             "bestpath": {
#                 "as_path": "confed",
#                 "compare_routerid": true
#             },
#             "default": {
#                 "no_ipv4_unicast": true
#             },
#             "distance": [
#                 {
#                     "type": "external",
#                     "value": 66
#                 },
#                 {
#                     "type": "internal",
#                     "value": 20
#                 },
#                 {
#                     "type": "local",
#                     "value": 10
#                 }
#             ]
#         },
#         "neighbor": [
#             {
#                 "address": "192.0.2.43",
#                 "advertisement_interval": 72,
#                 "capability": {
#                     "dynamic": true
#                 },
#                 "disable_connected_check": true,
#                 "timers": {
#                     "holdtime": 30,
#                     "keepalive": 10
#                 }
#             },
#             {
#                 "address": "203.0.113.0",
#                 "capability": {
#                     "orf": "receive"
#                 }
#             }
#         ],
#         "network": [
#             {
#                 "address": "203.0.113.0/24",
#                 "route_map": "map01"
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "static",
#                 "route_map": "map01"
#             }
#         ]
#     },
#

# Using parsed:
# ------------

# parsed.cfg

# set protocols bgp 65536 neighbor 192.0.2.43 advertisement-interval '72'
# set protocols bgp 65536 neighbor 192.0.2.43 capability 'dynamic'
# set protocols bgp 65536 neighbor 192.0.2.43 'disable-connected-check'
# set protocols bgp 65536 neighbor 192.0.2.43 timers holdtime '30'
# set protocols bgp 65536 neighbor 192.0.2.43 timers keepalive '10'
# set protocols bgp 65536 neighbor 203.0.113.0 address-family 'ipv6-unicast'
# set protocols bgp 65536 neighbor 203.0.113.0 capability orf prefix-list 'receive'
# set protocols bgp 65536 network 203.0.113.0/24 route-map 'map01'
# set protocols bgp 65536 parameters 'always-compare-med'
# set protocols bgp 65536 parameters bestpath as-path 'confed'
# set protocols bgp 65536 parameters bestpath 'compare-routerid'
# set protocols bgp 65536 parameters dampening half-life '33'
# set protocols bgp 65536 parameters dampening max-suppress-time '20'
# set protocols bgp 65536 parameters dampening re-use '60'
# set protocols bgp 65536 parameters dampening start-suppress-time '5'
# set protocols bgp 65536 parameters default 'no-ipv4-unicast'
# set protocols bgp 65536 parameters distance global external '66'
# set protocols bgp 65536 parameters distance global internal '20'
# set protocols bgp 65536 parameters distance global local '10'
# set protocols bgp 65536 redistribute static route-map 'map01'

  - name: parse configs
    vyos.vyos.vyos_bgp_global:
      running_config: "{{ lookup('file', './parsed.cfg') }}"
      state: parsed
    tags:
      - parsed

# Module execution:
# "parsed": {
#         "as_number": 65536,
#         "bgp_params": {
#             "always_compare_med": true,
#             "bestpath": {
#                 "as_path": "confed",
#                 "compare_routerid": true
#             },
#             "default": {
#                 "no_ipv4_unicast": true
#             },
#             "distance": [
#                 {
#                     "type": "external",
#                     "value": 66
#                 },
#                 {
#                     "type": "internal",
#                     "value": 20
#                 },
#                 {
#                     "type": "local",
#                     "value": 10
#                 }
#             ]
#         },
#         "neighbor": [
#             {
#                 "address": "192.0.2.43",
#                 "advertisement_interval": 72,
#                 "capability": {
#                     "dynamic": true
#                 },
#                 "disable_connected_check": true,
#                 "timers": {
#                     "holdtime": 30,
#                     "keepalive": 10
#                 }
#             },
#             {
#                 "address": "203.0.113.0",
#                 "capability": {
#                     "orf": "receive"
#                 }
#             }
#         ],
#         "network": [
#             {
#                 "address": "203.0.113.0/24",
#                 "route_map": "map01"
#             }
#         ],
#         "redistribute": [
#             {
#                 "protocol": "static",
#                 "route_map": "map01"
#             }
#         ]
#     }
#

# Using rendered:
# --------------

  - name: Render
    vyos.vyos.vyos_bgp_global:
      config:
        as_number: "65536"
        network:
          - address: "203.0.113.0/24"
            route_map: map01
        redistribute:
          - protocol: "static"
            route_map: "map01"
        bgp_params:
          always_compare_med: true
          dampening:
            start_suppress_time: 5
            max_suppress_time: 20
            half_life: 33
            re_use: 60
          distance:
            - type: "internal"
              value: 20
            - type: "local"
              value: 10
            - type: "external"
              value: 66
          bestpath:
            as_path: "confed"
            compare_routerid: true
          default:
            no_ipv4_unicast: true
        neighbor:
          - address: "192.0.2.43"
            disable_connected_check: true
            advertisement_interval: 72
            capability:
              dynamic: true
            timers:
              holdtime: 30
              keepalive: 10
          - address: "203.0.113.0"
            capability:
              orf: "receive"

      state: rendered

# Module Execution:
# "rendered": [
#         "set protocols bgp 65536 neighbor 192.0.2.43 disable-connected-check",
#         "set protocols bgp 65536 neighbor 192.0.2.43 advertisement-interval 72",
#         "set protocols bgp 65536 neighbor 192.0.2.43 capability dynamic",
#         "set protocols bgp 65536 neighbor 192.0.2.43 timers holdtime 30",
#         "set protocols bgp 65536 neighbor 192.0.2.43 timers keepalive 10",
#         "set protocols bgp 65536 neighbor 203.0.113.0 capability orf prefix-list receive",
#         "set protocols bgp 65536 redistribute static route-map map01",
#         "set protocols bgp 65536 network 203.0.113.0/24 route-map map01",
#         "set protocols bgp 65536 parameters always-compare-med",
#         "set protocols bgp 65536 parameters dampening half-life 33",
#         "set protocols bgp 65536 parameters dampening max-suppress-time 20",
#         "set protocols bgp 65536 parameters dampening re-use 60",
#         "set protocols bgp 65536 parameters dampening start-suppress-time 5",
#         "set protocols bgp 65536 parameters distance global internal 20",
#         "set protocols bgp 65536 parameters distance global local 10",
#         "set protocols bgp 65536 parameters distance global external 66",
#         "set protocols bgp 65536 parameters bestpath as-path confed",
#         "set protocols bgp 65536 parameters bestpath compare-routerid",
#         "set protocols bgp 65536 parameters default no-ipv4-unicast"
#     ]
```

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
