---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_ospfv2 module – OSPFv2 resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_ospfv2_module.html
fetched_at: 2026-07-28T00:23:28+00:00
---
# vyos.vyos.vyos_ospfv2 module – OSPFv2 resource module

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
> To use it in a playbook, specify: `vyos.vyos.vyos_ospfv2`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_ospfv2_module.md#synopsis)
- [Parameters](vyos_ospfv2_module.md#parameters)
- [Notes](vyos_ospfv2_module.md#notes)
- [Examples](vyos_ospfv2_module.md#examples)
- [Return Values](vyos_ospfv2_module.md#return-values)

## [Synopsis](vyos_ospfv2_module.md#id1)

- This resource module configures and manages attributes of OSPFv2 routes on VyOS network devices.

## [Parameters](vyos_ospfv2_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A provided OSPFv2 route configuration. |
| **areas**  list / elements=dictionary | OSPFv2 area. |
| **area_id**  string | OSPFv2 area identity. |
| **area_type**  dictionary | Area type. |
| **normal**  boolean | Normal OSPFv2 area.  Choices:   - `false` - `true` |
| **nssa**  dictionary | NSSA OSPFv2 area. |
| **default_cost**  integer | Summary-default cost of NSSA area. |
| **no_summary**  boolean | Do not inject inter-area routes into stub.  Choices:   - `false` - `true` |
| **set**  boolean | Enabling NSSA.  Choices:   - `false` - `true` |
| **translate**  string | NSSA-ABR.  Choices:   - `"always"` - `"candidate"` - `"never"` |
| **stub**  dictionary | Stub OSPFv2 area. |
| **default_cost**  integer | Summary-default cost of stub area. |
| **no_summary**  boolean | Do not inject inter-area routes into stub.  Choices:   - `false` - `true` |
| **set**  boolean | Enabling stub.  Choices:   - `false` - `true` |
| **authentication**  string | OSPFv2 area authentication type.  Choices:   - `"plaintext-password"` - `"md5"` |
| **network**  list / elements=dictionary | OSPFv2 network. |
| **address**  string / required | OSPFv2 IPv4 network address. |
| **range**  list / elements=dictionary | Summarize routes matching prefix (border routers only). |
| **address**  string | border router IPv4 address. |
| **cost**  integer | Metric for this range. |
| **not_advertise**  boolean | Don’t advertise this range.  Choices:   - `false` - `true` |
| **substitute**  string | Announce area range (IPv4 address) as another prefix. |
| **shortcut**  string | Area’s shortcut mode.  Choices:   - `"default"` - `"disable"` - `"enable"` |
| **virtual_link**  list / elements=dictionary | Virtual link address. |
| **address**  string | virtual link address. |
| **authentication**  dictionary | OSPFv2 area authentication type. |
| **md5**  list / elements=dictionary | MD5 key id based authentication. |
| **key_id**  integer | MD5 key id. |
| **md5_key**  string | MD5 key. |
| **plaintext_password**  string | Plain text password. |
| **dead_interval**  integer | Interval after which a neighbor is declared dead. |
| **hello_interval**  integer | Interval between hello packets. |
| **retransmit_interval**  integer | Interval between retransmitting lost link state advertisements. |
| **transmit_delay**  integer | Link state transmit delay. |
| **auto_cost**  dictionary | Calculate OSPFv2 interface cost according to bandwidth. |
| **reference_bandwidth**  integer | Reference bandwidth cost in Mbits/sec. |
| **default_information**  dictionary | Control distribution of default information. |
| **originate**  dictionary | Distribute a default route. |
| **always**  boolean | Always advertise default route.  Choices:   - `false` - `true` |
| **metric**  integer | OSPFv2 default metric. |
| **metric_type**  integer | OSPFv2 Metric types for default routes. |
| **route_map**  string | Route map references. |
| **default_metric**  integer | Metric of redistributed routes |
| **distance**  dictionary | Administrative distance. |
| **global**  integer | Global OSPFv2 administrative distance. |
| **ospf**  dictionary | OSPFv2 administrative distance. |
| **external**  integer | Distance for external routes. |
| **inter_area**  integer | Distance for inter-area routes. |
| **intra_area**  integer | Distance for intra-area routes. |
| **log_adjacency_changes**  string | Log changes in adjacency state.  Choices:   - `"detail"` |
| **max_metric**  dictionary | OSPFv2 maximum/infinite-distance metric. |
| **router_lsa**  dictionary | Advertise own Router-LSA with infinite distance (stub router). |
| **administrative**  boolean | Administratively apply, for an indefinite period.  Choices:   - `false` - `true` |
| **on_shutdown**  integer | Time to advertise self as stub-router. |
| **on_startup**  integer | Time to advertise self as stub-router |
| **mpls_te**  dictionary | MultiProtocol Label Switching-Traffic Engineering (MPLS-TE) parameters. |
| **enabled**  boolean | Enable MPLS-TE functionality.  Choices:   - `false` - `true` |
| **router_address**  string | Stable IP address of the advertising router. |
| **neighbor**  list / elements=dictionary | Neighbor IP address. |
| **neighbor_id**  string | Identity (number/IP address) of neighbor. |
| **poll_interval**  integer | Seconds between dead neighbor polling interval. |
| **priority**  integer | Neighbor priority. |
| **parameters**  dictionary | OSPFv2 specific parameters. |
| **abr_type**  string | OSPFv2 ABR Type.  Choices:   - `"cisco"` - `"ibm"` - `"shortcut"` - `"standard"` |
| **opaque_lsa**  boolean | Enable the Opaque-LSA capability (rfc2370).  Choices:   - `false` - `true` |
| **rfc1583_compatibility**  boolean | Enable rfc1583 criteria for handling AS external routes.  Choices:   - `false` - `true` |
| **router_id**  string | Override the default router identifier. |
| **passive_interface**  list / elements=string | Suppress routing updates on an interface. |
| **passive_interface_exclude**  list / elements=string | Interface to exclude when using passive-interface default. |
| **redistribute**  list / elements=dictionary | Redistribute information from another routing protocol. |
| **metric**  integer | Metric for redistribution routes. |
| **metric_type**  integer | OSPFv2 Metric types. |
| **route_map**  string | Route map references. |
| **route_type**  string | Route type to redistribute.  Choices:   - `"bgp"` - `"connected"` - `"kernel"` - `"rip"` - `"static"` |
| **route_map**  list / elements=string | Filter routes installed in local route map. |
| **timers**  dictionary | Adjust routing timers. |
| **refresh**  dictionary | Adjust refresh parameters. |
| **timers**  integer | refresh timer. |
| **throttle**  dictionary | Throttling adaptive timers. |
| **spf**  dictionary | OSPFv2 SPF timers. |
| **delay**  integer | Delay (msec) from first change received till SPF calculation. |
| **initial_holdtime**  integer | Initial hold time(msec) between consecutive SPF calculations. |
| **max_holdtime**  integer | maximum hold time (sec). |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the VyOS device by executing the command **show configuration commands | grep ospf**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](vyos_ospfv2_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).

## [Examples](vyos_ospfv2_module.md#id4)

```yaml+jinja
# Using merged
#
# Before state:
# -------------
#
# vyos@vyos# run show  configuration commands | grep ospf
#
#
- name: Merge the provided configuration with the existing running configuration
  vyos.vyos.vyos_ospfv2:
    config:
      log_adjacency_changes: detail
      max_metric:
        router_lsa:
          administrative: true
          on_shutdown: 10
          on_startup: 10
        default_information:
          originate:
            always: true
            metric: 10
            metric_type: 2
            route_map: ingress
        mpls_te:
          enabled: true
          router_address: 192.0.11.11
        auto_cost:
          reference_bandwidth: 2
        neighbor:
        - neighbor_id: 192.0.11.12
          poll_interval: 10
          priority: 2
        redistribute:
        - route_type: bgp
          metric: 10
          metric_type: 2
        passive_interface:
        - eth1
        - eth2
        parameters:
          router_id: 192.0.1.1
          opaque_lsa: true
          rfc1583_compatibility: true
          abr_type: cisco
        areas:
        - area_id: '2'
          area_type:
            normal: true
            authentication: plaintext-password
            shortcut: enable
        - area_id: '3'
          area_type:
            nssa:
              set: true
        - area_id: '4'
          area_type:
            stub:
              default_cost: 20
          network:
          - address: 192.0.2.0/24
          range:
          - address: 192.0.3.0/24
            cost: 10
          - address: 192.0.4.0/24
          cost: 12
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# before": {}
#
#    "commands": [
#       "set protocols ospf mpls-te enable",
#       "set protocols ospf mpls-te router-address '192.0.11.11'",
#       "set protocols ospf redistribute bgp",
#       "set protocols ospf redistribute bgp metric-type 2",
#       "set protocols ospf redistribute bgp metric 10",
#       "set protocols ospf default-information originate metric-type 2",
#       "set protocols ospf default-information originate always",
#       "set protocols ospf default-information originate metric 10",
#       "set protocols ospf default-information originate route-map ingress",
#       "set protocols ospf auto-cost reference-bandwidth '2'",
#       "set protocols ospf parameters router-id '192.0.1.1'",
#       "set protocols ospf parameters opaque-lsa",
#       "set protocols ospf parameters abr-type 'cisco'",
#       "set protocols ospf parameters rfc1583-compatibility",
#       "set protocols ospf passive-interface eth1",
#       "set protocols ospf passive-interface eth2",
#       "set protocols ospf max-metric router-lsa on-shutdown 10",
#       "set protocols ospf max-metric router-lsa administrative",
#       "set protocols ospf max-metric router-lsa on-startup 10",
#       "set protocols ospf log-adjacency-changes 'detail'",
#       "set protocols ospf neighbor 192.0.11.12 priority 2",
#       "set protocols ospf neighbor 192.0.11.12 poll-interval 10",
#       "set protocols ospf neighbor 192.0.11.12",
#       "set protocols ospf area '2'",
#       "set protocols ospf area 2 authentication plaintext-password",
#       "set protocols ospf area 2 shortcut enable",
#       "set protocols ospf area 2 area-type normal",
#       "set protocols ospf area '3'",
#       "set protocols ospf area 3 area-type nssa",
#       "set protocols ospf area 4 range 192.0.3.0/24 cost 10",
#       "set protocols ospf area 4 range 192.0.3.0/24",
#       "set protocols ospf area 4 range 192.0.4.0/24 cost 12",
#       "set protocols ospf area 4 range 192.0.4.0/24",
#       "set protocols ospf area 4 area-type stub default-cost 20",
#       "set protocols ospf area '4'",
#       "set protocols ospf area 4 network 192.0.2.0/24"
#    ]
#
# "after": {
#        "areas": [
#            {
#                "area_id": "2",
#                "area_type": {
#                    "normal": true
#                },
#                "authentication": "plaintext-password",
#                "shortcut": "enable"
#            },
#            {
#                "area_id": "3",
#                "area_type": {
#                    "nssa": {
#                        "set": true
#                    }
#                }
#            },
#            {
#                "area_id": "4",
#                "area_type": {
#                    "stub": {
#                        "default_cost": 20,
#                        "set": true
#                    }
#                },
#                "network": [
#                    {
#                        "address": "192.0.2.0/24"
#                    }
#                ],
#                "range": [
#                    {
#                        "address": "192.0.3.0/24",
#                        "cost": 10
#                    },
#                    {
#                        "address": "192.0.4.0/24",
#                        "cost": 12
#                    }
#                ]
#            }
#        ],
#        "auto_cost": {
#            "reference_bandwidth": 2
#        },
#        "default_information": {
#            "originate": {
#                "always": true,
#                "metric": 10,
#                "metric_type": 2,
#                "route_map": "ingress"
#            }
#        },
#        "log_adjacency_changes": "detail",
#        "max_metric": {
#            "router_lsa": {
#                "administrative": true,
#                "on_shutdown": 10,
#                "on_startup": 10
#            }
#        },
#        "mpls_te": {
#            "enabled": true,
#            "router_address": "192.0.11.11"
#        },
#        "neighbor": [
#            {
#                "neighbor_id": "192.0.11.12",
#                "poll_interval": 10,
#                "priority": 2
#            }
#        ],
#        "parameters": {
#            "abr_type": "cisco",
#            "opaque_lsa": true,
#            "rfc1583_compatibility": true,
#            "router_id": "192.0.1.1"
#        },
#        "passive_interface": [
#            "eth2",
#            "eth1"
#        ],
#        "redistribute": [
#            {
#                "metric": 10,
#                "metric_type": 2,
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep ospf
# set protocols ospf area 2 area-type 'normal'
# set protocols ospf area 2 authentication 'plaintext-password'
# set protocols ospf area 2 shortcut 'enable'
# set protocols ospf area 3 area-type 'nssa'
# set protocols ospf area 4 area-type stub default-cost '20'
# set protocols ospf area 4 network '192.0.2.0/24'
# set protocols ospf area 4 range 192.0.3.0/24 cost '10'
# set protocols ospf area 4 range 192.0.4.0/24 cost '12'
# set protocols ospf auto-cost reference-bandwidth '2'
# set protocols ospf default-information originate 'always'
# set protocols ospf default-information originate metric '10'
# set protocols ospf default-information originate metric-type '2'
# set protocols ospf default-information originate route-map 'ingress'
# set protocols ospf log-adjacency-changes 'detail'
# set protocols ospf max-metric router-lsa 'administrative'
# set protocols ospf max-metric router-lsa on-shutdown '10'
# set protocols ospf max-metric router-lsa on-startup '10'
# set protocols ospf mpls-te 'enable'
# set protocols ospf mpls-te router-address '192.0.11.11'
# set protocols ospf neighbor 192.0.11.12 poll-interval '10'
# set protocols ospf neighbor 192.0.11.12 priority '2'
# set protocols ospf parameters abr-type 'cisco'
# set protocols ospf parameters 'opaque-lsa'
# set protocols ospf parameters 'rfc1583-compatibility'
# set protocols ospf parameters router-id '192.0.1.1'
# set protocols ospf passive-interface 'eth1'
# set protocols ospf passive-interface 'eth2'
# set protocols ospf redistribute bgp metric '10'
# set protocols ospf redistribute bgp metric-type '2'

# Using merged
#
# Before state:
# -------------
#
# vyos@vyos# run show  configuration commands | grep ospf
#
#
- name: Merge the provided configuration to update existing running configuration
  vyos.vyos.vyos_ospfv2:
    config:
      areas:
      - area_id: '2'
        area_type:
          normal: true
        authentication: plaintext-password
        shortcut: enable
      - area_id: '3'
        area_type:
          nssa:
            set: false
      - area_id: '4'
        area_type:
          stub:
            default_cost: 20
        network:
        - address: 192.0.2.0/24
        - address: 192.0.22.0/24
        - address: 192.0.32.0/24
    state: merged
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
# "before": {
#        "areas": [
#            {
#                "area_id": "2",
#                "area_type": {
#                    "normal": true
#                },
#                "authentication": "plaintext-password",
#                "shortcut": "enable"
#            },
#            {
#                "area_id": "3",
#                "area_type": {
#                    "nssa": {
#                        "set": true
#                    }
#                }
#            },
#            {
#                "area_id": "4",
#                "area_type": {
#                    "stub": {
#                        "default_cost": 20,
#                        "set": true
#                    }
#                },
#                "network": [
#                    {
#                        "address": "192.0.2.0/24"
#                    }
#                ],
#                "range": [
#                    {
#                        "address": "192.0.3.0/24",
#                        "cost": 10
#                    },
#                    {
#                        "address": "192.0.4.0/24",
#                        "cost": 12
#                    }
#                ]
#            }
#        ],
#        "auto_cost": {
#            "reference_bandwidth": 2
#        },
#        "default_information": {
#            "originate": {
#                "always": true,
#                "metric": 10,
#                "metric_type": 2,
#                "route_map": "ingress"
#            }
#        },
#        "log_adjacency_changes": "detail",
#        "max_metric": {
#            "router_lsa": {
#                "administrative": true,
#                "on_shutdown": 10,
#                "on_startup": 10
#            }
#        },
#        "mpls_te": {
#            "enabled": true,
#            "router_address": "192.0.11.11"
#        },
#        "neighbor": [
#            {
#                "neighbor_id": "192.0.11.12",
#                "poll_interval": 10,
#                "priority": 2
#            }
#        ],
#        "parameters": {
#            "abr_type": "cisco",
#            "opaque_lsa": true,
#            "rfc1583_compatibility": true,
#            "router_id": "192.0.1.1"
#        },
#        "passive_interface": [
#            "eth2",
#            "eth1"
#        ],
#        "redistribute": [
#            {
#                "metric": 10,
#                "metric_type": 2,
#                "route_type": "bgp"
#            }
#        ]
#    }
#
#    "commands": [
#       "delete protocols ospf area 4 area-type stub",
#       "set protocols ospf area 4 network 192.0.22.0/24"
#       "set protocols ospf area 4 network 192.0.32.0/24"
#    ]
#
# "after": {
#        "areas": [
#            {
#                "area_id": "2",
#                "area_type": {
#                    "normal": true
#                },
#                "authentication": "plaintext-password",
#                "shortcut": "enable"
#            },
#            {
#                "area_id": "3",
#                "area_type": {
#                    "nssa": {
#                        "set": true
#                    }
#                }
#            },
#            {
#                "area_id": "4",
#                },
#                "network": [
#                    {
#                        "address": "192.0.2.0/24"
#                    },
#                    {
#                        "address": "192.0.22.0/24"
#                    },
#                    {
#                        "address": "192.0.32.0/24"
#                    }
#                ],
#                "range": [
#                    {
#                        "address": "192.0.3.0/24",
#                        "cost": 10
#                    },
#                    {
#                        "address": "192.0.4.0/24",
#                        "cost": 12
#                    }
#                ]
#            }
#        ],
#        "auto_cost": {
#            "reference_bandwidth": 2
#        },
#        "default_information": {
#            "originate": {
#                "always": true,
#                "metric": 10,
#                "metric_type": 2,
#                "route_map": "ingress"
#            }
#        },
#        "log_adjacency_changes": "detail",
#        "max_metric": {
#            "router_lsa": {
#                "administrative": true,
#                "on_shutdown": 10,
#                "on_startup": 10
#            }
#        },
#        "mpls_te": {
#            "enabled": true,
#            "router_address": "192.0.11.11"
#        },
#        "neighbor": [
#            {
#                "neighbor_id": "192.0.11.12",
#                "poll_interval": 10,
#                "priority": 2
#            }
#        ],
#        "parameters": {
#            "abr_type": "cisco",
#            "opaque_lsa": true,
#            "rfc1583_compatibility": true,
#            "router_id": "192.0.1.1"
#        },
#        "passive_interface": [
#            "eth2",
#            "eth1"
#        ],
#        "redistribute": [
#            {
#                "metric": 10,
#                "metric_type": 2,
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep ospf
# set protocols ospf area 2 area-type 'normal'
# set protocols ospf area 2 authentication 'plaintext-password'
# set protocols ospf area 2 shortcut 'enable'
# set protocols ospf area 3 area-type 'nssa'
# set protocols ospf area 4 network '192.0.2.0/24'
# set protocols ospf area 4 network '192.0.22.0/24'
# set protocols ospf area 4 network '192.0.32.0/24'
# set protocols ospf area 4 range 192.0.3.0/24 cost '10'
# set protocols ospf area 4 range 192.0.4.0/24 cost '12'
# set protocols ospf auto-cost reference-bandwidth '2'
# set protocols ospf default-information originate 'always'
# set protocols ospf default-information originate metric '10'
# set protocols ospf default-information originate metric-type '2'
# set protocols ospf default-information originate route-map 'ingress'
# set protocols ospf log-adjacency-changes 'detail'
# set protocols ospf max-metric router-lsa 'administrative'
# set protocols ospf max-metric router-lsa on-shutdown '10'
# set protocols ospf max-metric router-lsa on-startup '10'
# set protocols ospf mpls-te 'enable'
# set protocols ospf mpls-te router-address '192.0.11.11'
# set protocols ospf neighbor 192.0.11.12 poll-interval '10'
# set protocols ospf neighbor 192.0.11.12 priority '2'
# set protocols ospf parameters abr-type 'cisco'
# set protocols ospf parameters 'opaque-lsa'
# set protocols ospf parameters 'rfc1583-compatibility'
# set protocols ospf parameters router-id '192.0.1.1'
# set protocols ospf passive-interface 'eth1'
# set protocols ospf passive-interface 'eth2'
# set protocols ospf redistribute bgp metric '10'
# set protocols ospf redistribute bgp metric-type '2'

# Using replaced
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep ospf
# set protocols ospf area 2 area-type 'normal'
# set protocols ospf area 2 authentication 'plaintext-password'
# set protocols ospf area 2 shortcut 'enable'
# set protocols ospf area 3 area-type 'nssa'
# set protocols ospf area 4 area-type stub default-cost '20'
# set protocols ospf area 4 network '192.0.2.0/24'
# set protocols ospf area 4 range 192.0.3.0/24 cost '10'
# set protocols ospf area 4 range 192.0.4.0/24 cost '12'
# set protocols ospf auto-cost reference-bandwidth '2'
# set protocols ospf default-information originate 'always'
# set protocols ospf default-information originate metric '10'
# set protocols ospf default-information originate metric-type '2'
# set protocols ospf default-information originate route-map 'ingress'
# set protocols ospf log-adjacency-changes 'detail'
# set protocols ospf max-metric router-lsa 'administrative'
# set protocols ospf max-metric router-lsa on-shutdown '10'
# set protocols ospf max-metric router-lsa on-startup '10'
# set protocols ospf mpls-te 'enable'
# set protocols ospf mpls-te router-address '192.0.11.11'
# set protocols ospf neighbor 192.0.11.12 poll-interval '10'
# set protocols ospf neighbor 192.0.11.12 priority '2'
# set protocols ospf parameters abr-type 'cisco'
# set protocols ospf parameters 'opaque-lsa'
# set protocols ospf parameters 'rfc1583-compatibility'
# set protocols ospf parameters router-id '192.0.1.1'
# set protocols ospf passive-interface 'eth1'
# set protocols ospf passive-interface 'eth2'
# set protocols ospf redistribute bgp metric '10'
# set protocols ospf redistribute bgp metric-type '2'
#
- name: Replace ospfv2 routes attributes configuration.
  vyos.vyos.vyos_ospfv2:
    config:
      log_adjacency_changes: detail
      max_metric:
        router_lsa:
          administrative: true
          on_shutdown: 10
          on_startup: 10
        default_information:
          originate:
            always: true
            metric: 10
            metric_type: 2
            route_map: ingress
        mpls_te:
          enabled: true
          router_address: 192.0.22.22
        auto_cost:
          reference_bandwidth: 2
        neighbor:
        - neighbor_id: 192.0.11.12
          poll_interval: 10
          priority: 2
        redistribute:
        - route_type: bgp
          metric: 10
          metric_type: 2
        passive_interface:
        - eth1
        parameters:
          router_id: 192.0.1.1
          opaque_lsa: true
          rfc1583_compatibility: true
          abr_type: cisco
        areas:
        - area_id: '2'
          area_type:
            normal: true
          authentication: plaintext-password
          shortcut: enable
        - area_id: '4'
          area_type:
            stub:
              default_cost: 20
          network:
          - address: 192.0.2.0/24
          - address: 192.0.12.0/24
          - address: 192.0.22.0/24
          - address: 192.0.32.0/24
          range:
          - address: 192.0.42.0/24
            cost: 10
    state: replaced
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "before": {
#        "areas": [
#            {
#                "area_id": "2",
#                "area_type": {
#                    "normal": true
#                },
#                "authentication": "plaintext-password",
#                "shortcut": "enable"
#            },
#            {
#                "area_id": "3",
#                "area_type": {
#                    "nssa": {
#                        "set": true
#                    }
#                }
#            },
#            {
#                "area_id": "4",
#                "area_type": {
#                    "stub": {
#                        "default_cost": 20,
#                        "set": true
#                    }
#                },
#                "network": [
#                    {
#                        "address": "192.0.2.0/24"
#                    }
#                ],
#                "range": [
#                    {
#                        "address": "192.0.3.0/24",
#                        "cost": 10
#                    },
#                    {
#                        "address": "192.0.4.0/24",
#                        "cost": 12
#                    }
#                ]
#            }
#        ],
#        "auto_cost": {
#            "reference_bandwidth": 2
#        },
#        "default_information": {
#            "originate": {
#                "always": true,
#                "metric": 10,
#                "metric_type": 2,
#                "route_map": "ingress"
#            }
#        },
#        "log_adjacency_changes": "detail",
#        "max_metric": {
#            "router_lsa": {
#                "administrative": true,
#                "on_shutdown": 10,
#                "on_startup": 10
#            }
#        },
#        "mpls_te": {
#            "enabled": true,
#            "router_address": "192.0.11.11"
#        },
#        "neighbor": [
#            {
#                "neighbor_id": "192.0.11.12",
#                "poll_interval": 10,
#                "priority": 2
#            }
#        ],
#        "parameters": {
#            "abr_type": "cisco",
#            "opaque_lsa": true,
#            "rfc1583_compatibility": true,
#            "router_id": "192.0.1.1"
#        },
#        "passive_interface": [
#            "eth2",
#            "eth1"
#        ],
#        "redistribute": [
#            {
#                "metric": 10,
#                "metric_type": 2,
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# "commands": [
#     "delete protocols ospf passive-interface eth2",
#     "delete protocols ospf area 3",
#     "delete protocols ospf area 4 range 192.0.3.0/24 cost",
#     "delete protocols ospf area 4 range 192.0.3.0/24",
#     "delete protocols ospf area 4 range 192.0.4.0/24 cost",
#     "delete protocols ospf area 4 range 192.0.4.0/24",
#     "set protocols ospf mpls-te router-address '192.0.22.22'",
#     "set protocols ospf area 4 range 192.0.42.0/24 cost 10",
#     "set protocols ospf area 4 range 192.0.42.0/24",
#     "set protocols ospf area 4 network 192.0.12.0/24",
#     "set protocols ospf area 4 network 192.0.22.0/24",
#     "set protocols ospf area 4 network 192.0.32.0/24"
#    ]
#
#    "after": {
#        "areas": [
#            {
#                "area_id": "2",
#                "area_type": {
#                    "normal": true
#                },
#                "authentication": "plaintext-password",
#                "shortcut": "enable"
#            },
#            {
#                "area_id": "4",
#                "area_type": {
#                    "stub": {
#                        "default_cost": 20,
#                        "set": true
#                    }
#                },
#                "network": [
#                    {
#                        "address": "192.0.12.0/24"
#                    },
#                    {
#                        "address": "192.0.2.0/24"
#                    },
#                    {
#                        "address": "192.0.22.0/24"
#                    },
#                    {
#                        "address": "192.0.32.0/24"
#                    }
#                ],
#                "range": [
#                    {
#                        "address": "192.0.42.0/24",
#                        "cost": 10
#                    }
#                ]
#            }
#        ],
#        "auto_cost": {
#            "reference_bandwidth": 2
#        },
#        "default_information": {
#            "originate": {
#                "always": true,
#                "metric": 10,
#                "metric_type": 2,
#                "route_map": "ingress"
#            }
#        },
#        "log_adjacency_changes": "detail",
#        "max_metric": {
#            "router_lsa": {
#                "administrative": true,
#                "on_shutdown": 10,
#                "on_startup": 10
#            }
#        },
#        "mpls_te": {
#            "enabled": true,
#            "router_address": "192.0.22.22"
#        },
#        "neighbor": [
#            {
#                "neighbor_id": "192.0.11.12",
#                "poll_interval": 10,
#                "priority": 2
#            }
#        ],
#        "parameters": {
#            "abr_type": "cisco",
#            "opaque_lsa": true,
#            "rfc1583_compatibility": true,
#            "router_id": "192.0.1.1"
#        },
#        "passive_interface": [
#            "eth1"
#        ],
#        "redistribute": [
#            {
#                "metric": 10,
#                "metric_type": 2,
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep ospf
# set protocols ospf area 2 area-type 'normal'
# set protocols ospf area 2 authentication 'plaintext-password'
# set protocols ospf area 2 shortcut 'enable'
# set protocols ospf area 4 area-type stub default-cost '20'
# set protocols ospf area 4 network '192.0.2.0/24'
# set protocols ospf area 4 network '192.0.12.0/24'
# set protocols ospf area 4 network '192.0.22.0/24'
# set protocols ospf area 4 network '192.0.32.0/24'
# set protocols ospf area 4 range 192.0.42.0/24 cost '10'
# set protocols ospf auto-cost reference-bandwidth '2'
# set protocols ospf default-information originate 'always'
# set protocols ospf default-information originate metric '10'
# set protocols ospf default-information originate metric-type '2'
# set protocols ospf default-information originate route-map 'ingress'
# set protocols ospf log-adjacency-changes 'detail'
# set protocols ospf max-metric router-lsa 'administrative'
# set protocols ospf max-metric router-lsa on-shutdown '10'
# set protocols ospf max-metric router-lsa on-startup '10'
# set protocols ospf mpls-te 'enable'
# set protocols ospf mpls-te router-address '192.0.22.22'
# set protocols ospf neighbor 192.0.11.12 poll-interval '10'
# set protocols ospf neighbor 192.0.11.12 priority '2'
# set protocols ospf parameters abr-type 'cisco'
# set protocols ospf parameters 'opaque-lsa'
# set protocols ospf parameters 'rfc1583-compatibility'
# set protocols ospf parameters router-id '192.0.1.1'
# set protocols ospf passive-interface 'eth1'
# set protocols ospf redistribute bgp metric '10'
# set protocols ospf redistribute bgp metric-type '2'

# Using rendered
#
#
- name: Render the commands for provided  configuration
  vyos.vyos.vyos_ospfv2:
    config:
      log_adjacency_changes: detail
      max_metric:
        router_lsa:
          administrative: true
          on_shutdown: 10
          on_startup: 10
        default_information:
          originate:
            always: true
            metric: 10
            metric_type: 2
            route_map: ingress
        mpls_te:
          enabled: true
          router_address: 192.0.11.11
        auto_cost:
          reference_bandwidth: 2
        neighbor:
        - neighbor_id: 192.0.11.12
          poll_interval: 10
          priority: 2
        redistribute:
        - route_type: bgp
          metric: 10
          metric_type: 2
        passive_interface:
        - eth1
        - eth2
        parameters:
          router_id: 192.0.1.1
          opaque_lsa: true
          rfc1583_compatibility: true
          abr_type: cisco
        areas:
        - area_id: '2'
          area_type:
            normal: true
          authentication: plaintext-password
          shortcut: enable
        - area_id: '3'
          area_type:
            nssa:
              set: true
        - area_id: '4'
          area_type:
            stub:
              default_cost: 20
          network:
          - address: 192.0.2.0/24
          range:
          - address: 192.0.3.0/24
            cost: 10
          - address: 192.0.4.0/24
            cost: 12
    state: rendered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#        [
#       "set protocols ospf mpls-te enable",
#       "set protocols ospf mpls-te router-address '192.0.11.11'",
#       "set protocols ospf redistribute bgp",
#       "set protocols ospf redistribute bgp metric-type 2",
#       "set protocols ospf redistribute bgp metric 10",
#       "set protocols ospf default-information originate metric-type 2",
#       "set protocols ospf default-information originate always",
#       "set protocols ospf default-information originate metric 10",
#       "set protocols ospf default-information originate route-map ingress",
#       "set protocols ospf auto-cost reference-bandwidth '2'",
#       "set protocols ospf parameters router-id '192.0.1.1'",
#       "set protocols ospf parameters opaque-lsa",
#       "set protocols ospf parameters abr-type 'cisco'",
#       "set protocols ospf parameters rfc1583-compatibility",
#       "set protocols ospf passive-interface eth1",
#       "set protocols ospf passive-interface eth2",
#       "set protocols ospf max-metric router-lsa on-shutdown 10",
#       "set protocols ospf max-metric router-lsa administrative",
#       "set protocols ospf max-metric router-lsa on-startup 10",
#       "set protocols ospf log-adjacency-changes 'detail'",
#       "set protocols ospf neighbor 192.0.11.12 priority 2",
#       "set protocols ospf neighbor 192.0.11.12 poll-interval 10",
#       "set protocols ospf neighbor 192.0.11.12",
#       "set protocols ospf area '2'",
#       "set protocols ospf area 2 authentication plaintext-password",
#       "set protocols ospf area 2 shortcut enable",
#       "set protocols ospf area 2 area-type normal",
#       "set protocols ospf area '3'",
#       "set protocols ospf area 3 area-type nssa",
#       "set protocols ospf area 4 range 192.0.3.0/24 cost 10",
#       "set protocols ospf area 4 range 192.0.3.0/24",
#       "set protocols ospf area 4 range 192.0.4.0/24 cost 12",
#       "set protocols ospf area 4 range 192.0.4.0/24",
#       "set protocols ospf area 4 area-type stub default-cost 20",
#       "set protocols ospf area '4'",
#       "set protocols ospf area 4 network 192.0.2.0/24"
#    ]

# Using parsed
#
#
- name: Parse the commands for provided  structured configuration
  vyos.vyos.vyos_ospfv2:
    running_config:
      "set protocols ospf area 2 area-type 'normal'
       set protocols ospf area 2 authentication 'plaintext-password'
       set protocols ospf area 2 shortcut 'enable'
       set protocols ospf area 3 area-type 'nssa'
       set protocols ospf area 4 area-type stub default-cost '20'
       set protocols ospf area 4 network '192.0.2.0/24'
       set protocols ospf area 4 range 192.0.3.0/24 cost '10'
       set protocols ospf area 4 range 192.0.4.0/24 cost '12'
       set protocols ospf auto-cost reference-bandwidth '2'
       set protocols ospf default-information originate 'always'
       set protocols ospf default-information originate metric '10'
       set protocols ospf default-information originate metric-type '2'
       set protocols ospf default-information originate route-map 'ingress'
       set protocols ospf log-adjacency-changes 'detail'
       set protocols ospf max-metric router-lsa 'administrative'
       set protocols ospf max-metric router-lsa on-shutdown '10'
       set protocols ospf max-metric router-lsa on-startup '10'
       set protocols ospf mpls-te 'enable'
       set protocols ospf mpls-te router-address '192.0.11.11'
       set protocols ospf neighbor 192.0.11.12 poll-interval '10'
       set protocols ospf neighbor 192.0.11.12 priority '2'
       set protocols ospf parameters abr-type 'cisco'
       set protocols ospf parameters 'opaque-lsa'
       set protocols ospf parameters 'rfc1583-compatibility'
       set protocols ospf parameters router-id '192.0.1.1'
       set protocols ospf passive-interface 'eth1'
       set protocols ospf passive-interface 'eth2'
       set protocols ospf redistribute bgp metric '10'
       set protocols ospf redistribute bgp metric-type '2'"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": {
#        "areas": [
#            {
#                "area_id": "2",
#                "area_type": {
#                    "normal": true
#                },
#                "authentication": "plaintext-password",
#                "shortcut": "enable"
#            },
#            {
#                "area_id": "3",
#                "area_type": {
#                    "nssa": {
#                        "set": true
#                    }
#                }
#            },
#            {
#                "area_id": "4",
#                "area_type": {
#                    "stub": {
#                        "default_cost": 20,
#                        "set": true
#                    }
#                },
#                "network": [
#                    {
#                        "address": "192.0.2.0/24"
#                    }
#                ],
#                "range": [
#                    {
#                        "address": "192.0.3.0/24",
#                        "cost": 10
#                    },
#                    {
#                        "address": "192.0.4.0/24",
#                        "cost": 12
#                    }
#                ]
#            }
#        ],
#        "auto_cost": {
#            "reference_bandwidth": 2
#        },
#        "default_information": {
#            "originate": {
#                "always": true,
#                "metric": 10,
#                "metric_type": 2,
#                "route_map": "ingress"
#            }
#        },
#        "log_adjacency_changes": "detail",
#        "max_metric": {
#            "router_lsa": {
#                "administrative": true,
#                "on_shutdown": 10,
#                "on_startup": 10
#            }
#        },
#        "mpls_te": {
#            "enabled": true,
#            "router_address": "192.0.11.11"
#        },
#        "neighbor": [
#            {
#                "neighbor_id": "192.0.11.12",
#                "poll_interval": 10,
#                "priority": 2
#            }
#        ],
#        "parameters": {
#            "abr_type": "cisco",
#            "opaque_lsa": true,
#            "rfc1583_compatibility": true,
#            "router_id": "192.0.1.1"
#        },
#        "passive_interface": [
#            "eth2",
#            "eth1"
#        ],
#        "redistribute": [
#            {
#                "metric": 10,
#                "metric_type": 2,
#                "route_type": "bgp"
#            }
#        ]
#    }
# }

# Using gathered
#
# Before state:
# -------------
#
# vyos@192# run show configuration commands | grep ospf
# set protocols ospf area 2 area-type 'normal'
# set protocols ospf area 2 authentication 'plaintext-password'
# set protocols ospf area 2 shortcut 'enable'
# set protocols ospf area 3 area-type 'nssa'
# set protocols ospf area 4 area-type stub default-cost '20'
# set protocols ospf area 4 network '192.0.2.0/24'
# set protocols ospf area 4 range 192.0.3.0/24 cost '10'
# set protocols ospf area 4 range 192.0.4.0/24 cost '12'
# set protocols ospf auto-cost reference-bandwidth '2'
# set protocols ospf default-information originate 'always'
# set protocols ospf default-information originate metric '10'
# set protocols ospf default-information originate metric-type '2'
# set protocols ospf default-information originate route-map 'ingress'
# set protocols ospf log-adjacency-changes 'detail'
# set protocols ospf max-metric router-lsa 'administrative'
# set protocols ospf max-metric router-lsa on-shutdown '10'
# set protocols ospf max-metric router-lsa on-startup '10'
# set protocols ospf mpls-te 'enable'
# set protocols ospf mpls-te router-address '192.0.11.11'
# set protocols ospf neighbor 192.0.11.12 poll-interval '10'
# set protocols ospf neighbor 192.0.11.12 priority '2'
# set protocols ospf parameters abr-type 'cisco'
# set protocols ospf parameters 'opaque-lsa'
# set protocols ospf parameters 'rfc1583-compatibility'
# set protocols ospf parameters router-id '192.0.1.1'
# set protocols ospf passive-interface 'eth1'
# set protocols ospf passive-interface 'eth2'
# set protocols ospf redistribute bgp metric '10'
# set protocols ospf redistribute bgp metric-type '2'
#
- name: Gather ospfv2 routes config with provided configurations
  vyos.vyos.vyos_ospfv2:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": {
#        "areas": [
#            {
#                "area_id": "2",
#                "area_type": {
#                    "normal": true
#                },
#                "authentication": "plaintext-password",
#                "shortcut": "enable"
#            },
#            {
#                "area_id": "3",
#                "area_type": {
#                    "nssa": {
#                        "set": true
#                    }
#                }
#            },
#            {
#                "area_id": "4",
#                "area_type": {
#                    "stub": {
#                        "default_cost": 20,
#                        "set": true
#                    }
#                },
#                "network": [
#                    {
#                        "address": "192.0.2.0/24"
#                    }
#                ],
#                "range": [
#                    {
#                        "address": "192.0.3.0/24",
#                        "cost": 10
#                    },
#                    {
#                        "address": "192.0.4.0/24",
#                        "cost": 12
#                    }
#                ]
#            }
#        ],
#        "auto_cost": {
#            "reference_bandwidth": 2
#        },
#        "default_information": {
#            "originate": {
#                "always": true,
#                "metric": 10,
#                "metric_type": 2,
#                "route_map": "ingress"
#            }
#        },
#        "log_adjacency_changes": "detail",
#        "max_metric": {
#            "router_lsa": {
#                "administrative": true,
#                "on_shutdown": 10,
#                "on_startup": 10
#            }
#        },
#        "mpls_te": {
#            "enabled": true,
#            "router_address": "192.0.11.11"
#        },
#        "neighbor": [
#            {
#                "neighbor_id": "192.0.11.12",
#                "poll_interval": 10,
#                "priority": 2
#            }
#        ],
#        "parameters": {
#            "abr_type": "cisco",
#            "opaque_lsa": true,
#            "rfc1583_compatibility": true,
#            "router_id": "192.0.1.1"
#        },
#        "passive_interface": [
#            "eth2",
#            "eth1"
#        ],
#        "redistribute": [
#            {
#                "metric": 10,
#                "metric_type": 2,
#                "route_type": "bgp"
#            }
#        ]
#    }
#
# After state:
# -------------
#
# vyos@192# run show configuration commands | grep ospf
# set protocols ospf area 2 area-type 'normal'
# set protocols ospf area 2 authentication 'plaintext-password'
# set protocols ospf area 2 shortcut 'enable'
# set protocols ospf area 3 area-type 'nssa'
# set protocols ospf area 4 area-type stub default-cost '20'
# set protocols ospf area 4 network '192.0.2.0/24'
# set protocols ospf area 4 range 192.0.3.0/24 cost '10'
# set protocols ospf area 4 range 192.0.4.0/24 cost '12'
# set protocols ospf auto-cost reference-bandwidth '2'
# set protocols ospf default-information originate 'always'
# set protocols ospf default-information originate metric '10'
# set protocols ospf default-information originate metric-type '2'
# set protocols ospf default-information originate route-map 'ingress'
# set protocols ospf log-adjacency-changes 'detail'
# set protocols ospf max-metric router-lsa 'administrative'
# set protocols ospf max-metric router-lsa on-shutdown '10'
# set protocols ospf max-metric router-lsa on-startup '10'
# set protocols ospf mpls-te 'enable'
# set protocols ospf mpls-te router-address '192.0.11.11'
# set protocols ospf neighbor 192.0.11.12 poll-interval '10'
# set protocols ospf neighbor 192.0.11.12 priority '2'
# set protocols ospf parameters abr-type 'cisco'
# set protocols ospf parameters 'opaque-lsa'
# set protocols ospf parameters 'rfc1583-compatibility'
# set protocols ospf parameters router-id '192.0.1.1'
# set protocols ospf passive-interface 'eth1'
# set protocols ospf passive-interface 'eth2'
# set protocols ospf redistribute bgp metric '10'
# set protocols ospf redistribute bgp metric-type '2'

# Using deleted
#
# Before state
# -------------
#
# vyos@192# run show configuration commands | grep ospf
# set protocols ospf area 2 area-type 'normal'
# set protocols ospf area 2 authentication 'plaintext-password'
# set protocols ospf area 2 shortcut 'enable'
# set protocols ospf area 3 area-type 'nssa'
# set protocols ospf area 4 area-type stub default-cost '20'
# set protocols ospf area 4 network '192.0.2.0/24'
# set protocols ospf area 4 range 192.0.3.0/24 cost '10'
# set protocols ospf area 4 range 192.0.4.0/24 cost '12'
# set protocols ospf auto-cost reference-bandwidth '2'
# set protocols ospf default-information originate 'always'
# set protocols ospf default-information originate metric '10'
# set protocols ospf default-information originate metric-type '2'
# set protocols ospf default-information originate route-map 'ingress'
# set protocols ospf log-adjacency-changes 'detail'
# set protocols ospf max-metric router-lsa 'administrative'
# set protocols ospf max-metric router-lsa on-shutdown '10'
# set protocols ospf max-metric router-lsa on-startup '10'
# set protocols ospf mpls-te 'enable'
# set protocols ospf mpls-te router-address '192.0.11.11'
# set protocols ospf neighbor 192.0.11.12 poll-interval '10'
# set protocols ospf neighbor 192.0.11.12 priority '2'
# set protocols ospf parameters abr-type 'cisco'
# set protocols ospf parameters 'opaque-lsa'
# set protocols ospf parameters 'rfc1583-compatibility'
# set protocols ospf parameters router-id '192.0.1.1'
# set protocols ospf passive-interface 'eth1'
# set protocols ospf passive-interface 'eth2'
# set protocols ospf redistribute bgp metric '10'
# set protocols ospf redistribute bgp metric-type '2'
#
- name: Delete attributes of ospfv2 routes.
  vyos.vyos.vyos_ospfv2:
    config:
    state: deleted
#
#
# ------------------------
# Module Execution Results
# ------------------------
#
#    "before": {
#        "areas": [
#            {
#                "area_id": "2",
#                "area_type": {
#                    "normal": true
#                },
#                "authentication": "plaintext-password",
#                "shortcut": "enable"
#            },
#            {
#                "area_id": "3",
#                "area_type": {
#                    "nssa": {
#                        "set": true
#                    }
#                }
#            },
#            {
#                "area_id": "4",
#                "area_type": {
#                    "stub": {
#                        "default_cost": 20,
#                        "set": true
#                    }
#                },
#                "network": [
#                    {
#                        "address": "192.0.2.0/24"
#                    }
#                ],
#                "range": [
#                    {
#                        "address": "192.0.3.0/24",
#                        "cost": 10
#                    },
#                    {
#                        "address": "192.0.4.0/24",
#                        "cost": 12
#                    }
#                ]
#            }
#        ],
#        "auto_cost": {
#            "reference_bandwidth": 2
#        },
#        "default_information": {
#            "originate": {
#                "always": true,
#                "metric": 10,
#                "metric_type": 2,
#                "route_map": "ingress"
#            }
#        },
#        "log_adjacency_changes": "detail",
#        "max_metric": {
#            "router_lsa": {
#                "administrative": true,
#                "on_shutdown": 10,
#                "on_startup": 10
#            }
#        },
#        "mpls_te": {
#            "enabled": true,
#            "router_address": "192.0.11.11"
#        },
#        "neighbor": [
#            {
#                "neighbor_id": "192.0.11.12",
#                "poll_interval": 10,
#                "priority": 2
#            }
#        ],
#        "parameters": {
#            "abr_type": "cisco",
#            "opaque_lsa": true,
#            "rfc1583_compatibility": true,
#            "router_id": "192.0.1.1"
#        },
#        "passive_interface": [
#            "eth2",
#            "eth1"
#        ],
#        "redistribute": [
#            {
#                "metric": 10,
#                "metric_type": 2,
#                "route_type": "bgp"
#            }
#        ]
#    }
# "commands": [
#        "delete protocols ospf"
#    ]
#
# "after": {}
# After state
# ------------
# vyos@192# run show configuration commands | grep ospf
#
```

## [Return Values](vyos_ospfv2_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["set protocols ospf parameters router-id 192.0.1.1", "set protocols ospf passive-interface 'eth1'"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
