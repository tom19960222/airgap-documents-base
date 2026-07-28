---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_bgp_address_family module – BGP Address Family Resource Module."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_bgp_address_family_module.html
fetched_at: 2026-07-28T02:59:08+00:00
---
# vyos.vyos.vyos_bgp_address_family module – BGP Address Family Resource Module.

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
> To use it in a playbook, specify: `vyos.vyos.vyos_bgp_address_family`.

New in vyos.vyos 2.1.0

- [Synopsis](vyos_bgp_address_family_module.md#synopsis)
- [Parameters](vyos_bgp_address_family_module.md#parameters)
- [Examples](vyos_bgp_address_family_module.md#examples)

## [Synopsis](vyos_bgp_address_family_module.md#id1)

- This module manages BGP address family configuration of interfaces on devices running VYOS.

Aliases: bgp_address_family

## [Parameters](vyos_bgp_address_family_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dict of BGP global configuration for interfaces. |
| **address_family**  list / elements=dictionary | BGP address-family parameters. |
| **afi**  string | BGP address family settings.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **aggregate_address**  list / elements=dictionary | BGP aggregate network. |
| **as_set**  boolean | Generate AS-set path information for this aggregate address.  **Choices:**   - `false` - `true` |
| **prefix**  string | BGP aggregate network. |
| **summary_only**  boolean | Announce the aggregate summary network only.  **Choices:**   - `false` - `true` |
| **networks**  list / elements=dictionary | BGP network |
| **backdoor**  boolean | Network as a backdoor route.  **Choices:**   - `false` - `true` |
| **path_limit**  integer | AS path hop count limit |
| **prefix**  string | BGP network address |
| **route_map**  string | Route-map to modify route attributes |
| **redistribute**  list / elements=dictionary | Redistribute routes from other protocols into BGP |
| **metric**  integer | Metric for redistributed routes. |
| **protocol**  string | types of routes to be redistributed.  **Choices:**   - `"connected"` - `"kernel"` - `"ospf"` - `"ospfv3"` - `"rip"` - `"ripng"` - `"static"` |
| **route_map**  string | Route map to filter redistributed routes |
| **table**  string | Redistribute non-main Kernel Routing Table. |
| **as_number**  integer | AS number. |
| **neighbors**  list / elements=dictionary | BGP neighbor |
| **address_family**  list / elements=dictionary | address family. |
| **afi**  string | BGP neighbor parameters.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **allowas_in**  integer | Number of occurrences of AS number. |
| **as_override**  boolean | AS for routes sent to this neighbor to be the local AS.  **Choices:**   - `false` - `true` |
| **attribute_unchanged**  dictionary | BGP attributes are sent unchanged. |
| **as_path**  boolean | as_path attribute  **Choices:**   - `false` - `true` |
| **med**  boolean | med attribute  **Choices:**   - `false` - `true` |
| **next_hop**  boolean | next_hop attribute  **Choices:**   - `false` - `true` |
| **capability**  dictionary | Advertise capabilities to this neighbor. |
| **dynamic**  boolean | Advertise dynamic capability to this neighbor.  **Choices:**   - `false` - `true` |
| **orf**  string | Advertise ORF capability to this neighbor.  **Choices:**   - `"send"` - `"receive"` |
| **default_originate**  string | Send default route to this neighbor |
| **distribute_list**  list / elements=dictionary | Access-list to filter route updates to/from this neighbor. |
| **acl**  integer | Access-list number. |
| **action**  string | Access-list to filter outgoing/incoming route updates to this neighbor  **Choices:**   - `"export"` - `"import"` |
| **filter_list**  list / elements=dictionary | As-path-list to filter route updates to/from this neighbor. |
| **action**  string | filter outgoing/incoming route updates  **Choices:**   - `"export"` - `"import"` |
| **path_list**  string | As-path-list to filter |
| **maximum_prefix**  integer | Maximum number of prefixes to accept from this neighbor nexthop-self Nexthop for routes sent to this neighbor to be the local router. |
| **nexthop_local**  boolean | Nexthop attributes.  **Choices:**   - `false` - `true` |
| **nexthop_self**  boolean | Nexthop for routes sent to this neighbor to be the local router.  **Choices:**   - `false` - `true` |
| **peer_group**  string | IPv4 peer group for this peer |
| **prefix_list**  list / elements=dictionary | Prefix-list to filter route updates to/from this neighbor. |
| **action**  string | filter outgoing/incoming route updates  **Choices:**   - `"export"` - `"import"` |
| **prefix_list**  string | Prefix-list to filter |
| **remove_private_as**  boolean | Remove private AS numbers from AS path in outbound route updates  **Choices:**   - `false` - `true` |
| **route_map**  list / elements=dictionary | Route-map to filter route updates to/from this neighbor. |
| **action**  string | filter outgoing/incoming route updates  **Choices:**   - `"export"` - `"import"` |
| **route_map**  string | route-map to filter |
| **route_reflector_client**  boolean | Neighbor as a route reflector client  **Choices:**   - `false` - `true` |
| **route_server_client**  boolean | Neighbor is route server client  **Choices:**   - `false` - `true` |
| **soft_reconfiguration**  boolean | Soft reconfiguration for neighbor  **Choices:**   - `false` - `true` |
| **unsupress_map**  string | Route-map to selectively unsuppress suppressed routes |
| **weight**  integer | Default weight for routes from this neighbor |
| **neighbor_address**  string | BGP neighbor address (v4/v6). |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VYOS device by executing the command **show configuration command | match bgp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` - `"purged"` - `"overridden"` |

## [Examples](vyos_bgp_address_family_module.md#id3)

```yaml+jinja
# Using merged
# Before state
# vyos@vyos:~$ show configuration commands |  match "set protocols bgp"
# vyos@vyos:~$

  - name: Merge provided configuration with device configuration
    vyos.vyos.vyos_bgp_address_family:
      config:
        as_number: "100"
        address_family:
          - afi: "ipv4"
            redistribute:
              - protocol: "static"
                metric: 50
        neighbors:
          - neighbor_address: "20.33.1.1/24"
            address_family:
              - afi: "ipv4"
                allowas_in: 4
                as_override: True
                attribute_unchanged:
                  med: True
              - afi: "ipv6"
                default_originate: "map01"
                distribute_list:
                  - action: "export"
                    acl: 10
          - neighbor_address: "100.11.34.12"
            address_family:
              - afi: "ipv4"
                maximum_prefix: 45
                nexthop_self: True
                route_map:
                  - action: "export"
                    route_map: "map01"
                  - action: "import"
                    route_map: "map01"
                weight: 50

# After State:
# vyos@vyos:~$ show configuration commands | match "set protocols bgp"
# set protocols bgp 100 address-family ipv4-unicast redistribute static metric '50'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number '4'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast as-override
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast default-originate route-map 'map01'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast distribute-list export '10'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast maximum-prefix '45'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast nexthop-self
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map export 'map01'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map import 'map01'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast weight '50'
# vyos@vyos:~$
#
# Module Execution:
#
# "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "redistribute": [
#                     {
#                         "metric": 50,
#                         "protocol": "static"
#                     }
#                 ]
#             }
#         ],
#         "as_number": 100,
#         "neighbors": [
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "maximum_prefix": 45,
#                         "nexthop_self": true,
#                         "route_map": [
#                             {
#                                 "action": "export",
#                                 "route_map": "map01"
#                             },
#                             {
#                                 "action": "import",
#                                 "route_map": "map01"
#                             }
#                         ],
#                         "weight": 50
#                     }
#                 ],
#                 "neighbor_address": "100.11.34.12"
#             },
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "allowas_in": 4,
#                         "as_override": true,
#                         "attribute_unchanged": {
#                             "med": true
#                         }
#                     },
#                     {
#                         "afi": "ipv6",
#                         "default_originate": "map01",
#                         "distribute_list": [
#                             {
#                                 "acl": 10,
#                                 "action": "export"
#                             }
#                         ]
#                     }
#                 ],
#                 "neighbor_address": "20.33.1.1/24"
#             }
#         ]
#     },
#     "before": {},
#     "changed": true,
#     "commands": [
#         "set protocols bgp 100 address-family ipv4-unicast redistribute static metric 50",
#         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number 4",
#         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast as-override",
#         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med",
#         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv6-unicast default-originate route-map map01",
#         "set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast distribute-list export 10",
#         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast maximum-prefix 45",
#         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast nexthop-self",
#         "set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map export map01",
#         "set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map import map01",
#         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast weight 50"
#     ],
#

# Using replaced:

# Before state:

# vyos@vyos:~$ show configuration commands | match "set protocols bgp"
# set protocols bgp 100 address-family ipv4-unicast redistribute static metric '50'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number '4'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast as-override
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast default-originate route-map 'map01'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast distribute-list export '10'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast maximum-prefix '45'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast nexthop-self
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map export 'map01'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map import 'map01'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast weight '50'
# vyos@vyos:~$

  - name: Replace provided configuration with device configuration
    vyos.vyos.vyos_bgp_address_family:
      config:
        as_number: "100"
        neighbors:
          - neighbor_address: "100.11.34.12"
            address_family:
              - afi: "ipv4"
                allowas_in: 4
                as_override: True
                attribute_unchanged:
                  med: True
              - afi: "ipv6"
                default_originate: "map01"
                distribute_list:
                  - action: "export"
                    acl: 10
          - neighbor_address: "20.33.1.1/24"
            address_family:
              - afi: "ipv6"
                maximum_prefix: 45
                nexthop_self: True

      state: replaced

# After State:

# vyos@vyos:~$ show configuration commands | match "set protocols bgp"
# set protocols bgp 100 address-family ipv4-unicast redistribute static metric '50'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast maximum-prefix '45'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast nexthop-self
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast allowas-in number '4'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast as-override
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast attribute-unchanged med
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast default-originate route-map 'map01'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast distribute-list export '10'
# vyos@vyos:~$
#
#
# # Module Execution:
# "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "redistribute": [
#                     {
#                         "metric": 50,
#                         "protocol": "static"
#                     }
#                 ]
#             }
#         ],
#         "as_number": 100,
#         "neighbors": [
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "allowas_in": 4,
#                         "as_override": true,
#                         "attribute_unchanged": {
#                             "med": true
#                         }
#                     },
#                     {
#                         "afi": "ipv6",
#                         "default_originate": "map01",
#                         "distribute_list": [
#                             {
#                                 "acl": 10,
#                                 "action": "export"
#                             }
#                         ]
#                     }
#                 ],
#                 "neighbor_address": "100.11.34.12"
#             },
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4"
#                     },
#                     {
#                         "afi": "ipv6",
#                         "maximum_prefix": 45,
#                         "nexthop_self": true
#                     }
#                 ],
#                 "neighbor_address": "20.33.1.1/24"
#             }
#         ]
#     },
#     "before": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "redistribute": [
#                     {
#                         "metric": 50,
#                         "protocol": "static"
#                     }
#                 ]
#             }
#         ],
#         "as_number": 100,
#         "neighbors": [
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "maximum_prefix": 45,
#                         "nexthop_self": true,
#                         "route_map": [
#                             {
#                                 "action": "export",
#                                 "route_map": "map01"
#                             },
#                             {
#                                 "action": "import",
#                                 "route_map": "map01"
#                             }
#                         ],
#                         "weight": 50
#                     }
#                 ],
#                 "neighbor_address": "100.11.34.12"
#             },
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "allowas_in": 4,
#                         "as_override": true,
#                         "attribute_unchanged": {
#                             "med": true
#                         }
#                     },
#                     {
#                         "afi": "ipv6",
#                         "default_originate": "map01",
#                         "distribute_list": [
#                             {
#                                 "acl": 10,
#                                 "action": "export"
#                             }
#                         ]
#                     }
#                 ],
#                 "neighbor_address": "20.33.1.1/24"
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#         "delete protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv6-unicast distribute-list",
#         "delete protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv6-unicast default-originate",
#         "delete protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged",
#         "delete protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast as-override",
#         "delete protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in",
#         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast weight",
#         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast route-map",
#         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast nexthop-self",
#         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast maximum-prefix",
#         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast allowas-in number 4",
#         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast as-override",
#         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast attribute-unchanged med",
#         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv6-unicast default-originate route-map map01",
#         "set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast distribute-list export 10",
#         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv6-unicast maximum-prefix 45",
#         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv6-unicast nexthop-self"
#     ],

# Using overridden
# vyos@vyos:~$ show configuration commands | match "set protocols bgp"
# set protocols bgp 100 address-family ipv4-unicast network 35.1.1.0/24 backdoor
# set protocols bgp 100 address-family ipv4-unicast redistribute static metric '50'
# set protocols bgp 100 address-family ipv6-unicast aggregate-address 6601:1:1:1::/64 summary-only
# set protocols bgp 100 address-family ipv6-unicast network 5001:1:1:1::/64 route-map 'map01'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast maximum-prefix '45'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast nexthop-self
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast allowas-in number '4'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast as-override
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast attribute-unchanged med
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast default-originate route-map 'map01'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast distribute-list export '10'
# vyos@vyos:~$

  - name: Override
    vyos.vyos.vyos_bgp_address_family:
      config:
        as_number: "100"
        neighbors:
          - neighbor_address: "100.11.34.12"
            address_family:
              - afi: "ipv6"
                maximum_prefix: 45
                nexthop_self: True
                route_map:
                  - action: "import"
                    route_map: "map01"
        address_family:
          - afi: "ipv4"
            aggregate_address:
              - prefix: "60.9.2.0/24"
                summary_only: True
          - afi: "ipv6"
            redistribute:
              - protocol: "static"
                metric: 50
      state: overridden

# Aft=validate-moduleser State

# vyos@vyos:~$ show configuration commands | match "set protocols bgp"
# set protocols bgp 100 address-family ipv4-unicast aggregate-address 60.9.2.0/24 summary-only
# set protocols bgp 100 address-family ipv6-unicast redistribute static metric '50'
# set protocols bgp 100 neighbor 20.33.1.1/24
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast maximum-prefix '45'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast nexthop-self
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast route-map import 'map01'
# vyos@vyos:~$

# Module Execution:

# "after": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "aggregate_address": [
#                     {
#                         "prefix": "60.9.2.0/24",
#                         "summary_only": true
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "metric": 50,
#                         "protocol": "static"
#                     }
#                 ]
#             }
#         ],
#         "as_number": 100,
#         "neighbors": [
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4"
#                     },
#                     {
#                         "afi": "ipv6",
#                         "maximum_prefix": 45,
#                         "nexthop_self": true,
#                         "route_map": [
#                             {
#                                 "action": "import",
#                                 "route_map": "map01"
#                             }
#                         ]
#                     }
#                 ],
#                 "neighbor_address": "100.11.34.12"
#             }
#         ]
#     },
#     "before": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "networks": [
#                     {
#                         "backdoor": true,
#                         "prefix": "35.1.1.0/24"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "metric": 50,
#                         "protocol": "static"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "aggregate_address": [
#                     {
#                         "prefix": "6601:1:1:1::/64",
#                         "summary_only": true
#                     }
#                 ],
#                 "networks": [
#                     {
#                         "prefix": "5001:1:1:1::/64",
#                         "route_map": "map01"
#                     }
#                 ]
#             }
#         ],
#         "as_number": 100,
#         "neighbors": [
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "allowas_in": 4,
#                         "as_override": true,
#                         "attribute_unchanged": {
#                             "med": true
#                         }
#                     },
#                     {
#                         "afi": "ipv6",
#                         "default_originate": "map01",
#                         "distribute_list": [
#                             {
#                                 "acl": 10,
#                                 "action": "export"
#                             }
#                         ]
#                     }
#                 ],
#                 "neighbor_address": "100.11.34.12"
#             },
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4"
#                     },
#                     {
#                         "afi": "ipv6",
#                         "maximum_prefix": 45,
#                         "nexthop_self": true
#                     }
#                 ],
#                 "neighbor_address": "20.33.1.1/24"
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#         "delete protocols bgp 100 neighbor 20.33.1.1/24 address-family",
#         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv6-unicast distribute-list",
#         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv6-unicast default-originate",
#         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast attribute-unchanged",
#         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast as-override",
#         "delete protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast allowas-in",
#         "delete protocols bgp 100 address-family ipv6 aggregate-address",
#         "delete protocols bgp 100 address-family ipv6 network",
#         "delete protocols bgp 100 address-family ipv4 network",
#         "delete protocols bgp 100 address-family ipv4 redistribute",
#         "set protocols bgp 100 address-family ipv4-unicast aggregate-address 60.9.2.0/24 summary-only",
#         "set protocols bgp 100 address-family ipv6-unicast redistribute static metric 50",
#         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv6-unicast maximum-prefix 45",
#         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv6-unicast nexthop-self",
#         "set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast route-map import map01"
#     ],
#

# Using deleted:

# Before State:

# vyos@vyos:~$ show configuration commands | match "set protocols bgp"
# set protocols bgp 100 address-family ipv4-unicast aggregate-address 60.9.2.0/24 summary-only
# set protocols bgp 100 address-family ipv4-unicast redistribute static metric '50'
# set protocols bgp 100 address-family ipv6-unicast redistribute static metric '50'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number '4'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast as-override
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast default-originate route-map 'map01'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast distribute-list export '10'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast maximum-prefix '45'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast nexthop-self
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map export 'map01'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map import 'map01'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast weight '50'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast maximum-prefix '45'
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast nexthop-self
# set protocols bgp 100 neighbor 100.11.34.12 address-family ipv6-unicast route-map import 'map01'
# vyos@vyos:~$

  - name: Delete
    vyos.vyos.vyos_bgp_address_family:
      config:
        as_number: "100"
        neighbors:
          - neighbor_address: "20.33.1.1/24"
            address_family:
              - afi: "ipv6"
          - neighbor_address: "100.11.34.12"
        address_family:
          - afi: "ipv4"
      state: deleted

# After State:

# vyos@vyos:~$ show configuration commands | match "set protocols bgp"
# set protocols bgp 100 address-family ipv6-unicast redistribute static metric '50'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number '4'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast as-override
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med
# set protocols bgp 100 neighbor 100.11.34.12
# vyos@vyos:~$
#
#
# Module Execution:
#
# "after": {
#         "address_family": [
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "metric": 50,
#                         "protocol": "static"
#                     }
#                 ]
#             }
#         ],
#         "as_number": 100,
#         "neighbors": [
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "allowas_in": 4,
#                         "as_override": true,
#                         "attribute_unchanged": {
#                             "med": true
#                         }
#                     }
#                 ],
#                 "neighbor_address": "20.33.1.1/24"
#             }
#         ]
#     },
#     "before": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "aggregate_address": [
#                     {
#                         "prefix": "60.9.2.0/24",
#                         "summary_only": true
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "metric": 50,
#                         "protocol": "static"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "metric": 50,
#                         "protocol": "static"
#                     }
#                 ]
#             }
#         ],
#         "as_number": 100,
#         "neighbors": [
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "maximum_prefix": 45,
#                         "nexthop_self": true,
#                         "route_map": [
#                             {
#                                 "action": "export",
#                                 "route_map": "map01"
#                             },
#                             {
#                                 "action": "import",
#                                 "route_map": "map01"
#                             }
#                         ],
#                         "weight": 50
#                     },
#                     {
#                         "afi": "ipv6",
#                         "maximum_prefix": 45,
#                         "nexthop_self": true,
#                         "route_map": [
#                             {
#                                 "action": "import",
#                                 "route_map": "map01"
#                             }
#                         ]
#                     }
#                 ],
#                 "neighbor_address": "100.11.34.12"
#             },
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "allowas_in": 4,
#                         "as_override": true,
#                         "attribute_unchanged": {
#                             "med": true
#                         }
#                     },
#                     {
#                         "afi": "ipv6",
#                         "default_originate": "map01",
#                         "distribute_list": [
#                             {
#                                 "acl": 10,
#                                 "action": "export"
#                             }
#                         ]
#                     }
#                 ],
#                 "neighbor_address": "20.33.1.1/24"
#             }
#         ]
#     },
#     "changed": true,
#     "commands": [
#         "delete protocols bgp 100 address-family ipv4-unicast",
#         "delete protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast",
#         "delete protocols bgp 100 neighbor 100.11.34.12 address-family"
#     ],
#

# using parsed:

# parsed.cfg
# set protocols bgp 65536 address-family ipv4-unicast aggregate-address 192.0.2.0/24 as-set
# set protocols bgp 65536 address-family ipv4-unicast network 192.1.13.0/24 route-map 'map01'
# set protocols bgp 65536 address-family ipv4-unicast network 192.2.13.0/24 backdoor
# set protocols bgp 65536 address-family ipv6-unicast redistribute ripng metric '20'
# set protocols bgp 65536 neighbor 192.0.2.25 address-family ipv4-unicast route-map export 'map01'
# set protocols bgp 65536 neighbor 192.0.2.25 address-family ipv4-unicast soft-reconfiguration inbound
# set protocols bgp 65536 neighbor 203.0.113.5 address-family ipv6-unicast attribute-unchanged next-hop

  - name: parse configs
    vyos.vyos.vyos_bgp_address_family:
      running_config: "{{ lookup('file', './parsed.cfg') }}"
      state: parsed

# Module Execution:
# "parsed": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "aggregate_address": [
#                     {
#                         "as_set": true,
#                         "prefix": "192.0.2.0/24"
#                     }
#                 ],
#                 "networks": [
#                     {
#                         "prefix": "192.1.13.0/24",
#                         "route_map": "map01"
#                     },
#                     {
#                         "backdoor": true,
#                         "prefix": "192.2.13.0/24"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "redistribute": [
#                     {
#                         "metric": 20,
#                         "protocol": "ripng"
#                     }
#                 ]
#             }
#         ],
#         "as_number": 65536,
#         "neighbors": [
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "route_map": [
#                             {
#                                 "action": "export",
#                                 "route_map": "map01"
#                             }
#                         ],
#                         "soft_reconfiguration": true
#                     }
#                 ],
#                 "neighbor_address": "192.0.2.25"
#             },
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv6",
#                         "attribute_unchanged": {
#                             "next_hop": true
#                         }
#                     }
#                 ],
#                 "neighbor_address": "203.0.113.5"
#             }
#         ]
#

# Using gathered:

# Native config:

# vyos@vyos:~$ show configuration commands | match "set protocols bgp"
# set protocols bgp 100 address-family ipv4-unicast network 35.1.1.0/24 backdoor
# set protocols bgp 100 address-family ipv4-unicast redistribute static metric '50'
# set protocols bgp 100 address-family ipv6-unicast aggregate-address 6601:1:1:1::/64 summary-only
# set protocols bgp 100 address-family ipv6-unicast network 5001:1:1:1::/64 route-map 'map01'
# set protocols bgp 100 address-family ipv6-unicast redistribute static metric '50'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number '4'
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast as-override
# set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med
# set protocols bgp 100 neighbor 100.11.34.12

  - name: gather configs
    vyos.vyos.vyos_bgp_address_family:
      state: gathered

# Module Execution:

# "gathered": {
#         "address_family": [
#             {
#                 "afi": "ipv4",
#                 "networks": [
#                     {
#                         "backdoor": true,
#                         "prefix": "35.1.1.0/24"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "metric": 50,
#                         "protocol": "static"
#                     }
#                 ]
#             },
#             {
#                 "afi": "ipv6",
#                 "aggregate_address": [
#                     {
#                         "prefix": "6601:1:1:1::/64",
#                         "summary_only": true
#                     }
#                 ],
#                 "networks": [
#                     {
#                         "prefix": "5001:1:1:1::/64",
#                         "route_map": "map01"
#                     }
#                 ],
#                 "redistribute": [
#                     {
#                         "metric": 50,
#                         "protocol": "static"
#                     }
#                 ]
#             }
#         ],
#         "as_number": 100,
#         "neighbors": [
#             {
#                 "address_family": [
#                     {
#                         "afi": "ipv4",
#                         "allowas_in": 4,
#                         "as_override": true,
#                         "attribute_unchanged": {
#                             "med": true
#                         }
#                     }
#                 ],
#                 "neighbor_address": "20.33.1.1/24"
#             }
#         ]

# Using rendered:

  - name: Render
    vyos.vyos.vyos_bgp_address_family:
      config:
        as_number: "100"
        address_family:
          - afi: "ipv4"
            redistribute:
              - protocol: "static"
                metric: 50
        neighbors:
          - neighbor_address: "20.33.1.1/24"
            address_family:
              - afi: "ipv4"
                allowas_in: 4
                as_override: True
                attribute_unchanged:
                  med: True
              - afi: "ipv6"
                default_originate: "map01"
                distribute_list:
                  - action: "export"
                    acl: 10
          - neighbor_address: "100.11.34.12"
            address_family:
              - afi: "ipv4"
                maximum_prefix: 45
                nexthop_self: True
                route_map:
                  - action: "export"
                    route_map: "map01"
                  - action: "import"
                    route_map: "map01"
                weight: 50
      state: rendered

# Module Execution:

# "rendered": [
#         "set protocols bgp 100 address-family ipv4-unicast redistribute static metric 50",
#         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast allowas-in number 4",
#         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast as-override",
#         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv4-unicast attribute-unchanged med",
#         "set protocols bgp 100  neighbor 20.33.1.1/24 address-family ipv6-unicast default-originate route-map map01",
#         "set protocols bgp 100 neighbor 20.33.1.1/24 address-family ipv6-unicast distribute-list export 10",
#         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast maximum-prefix 45",
#         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast nexthop-self",
#         "set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map export map01",
#         "set protocols bgp 100 neighbor 100.11.34.12 address-family ipv4-unicast route-map import map01",
#         "set protocols bgp 100  neighbor 100.11.34.12 address-family ipv4-unicast weight 50"
#     ]
```

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
