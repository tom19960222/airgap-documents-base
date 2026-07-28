---
collection: ansible
version: "6"
title: "arista.eos.eos_ospfv2 module – OSPFv2 resource module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_ospfv2_module.html
fetched_at: 2026-07-27T16:45:16+00:00
---
# arista.eos.eos_ospfv2 module – OSPFv2 resource module

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
> To use it in a playbook, specify: `arista.eos.eos_ospfv2`.

New in arista.eos 1.0.0

- [Synopsis](eos_ospfv2_module.md#synopsis)
- [Parameters](eos_ospfv2_module.md#parameters)
- [Notes](eos_ospfv2_module.md#notes)
- [Examples](eos_ospfv2_module.md#examples)
- [Return Values](eos_ospfv2_module.md#return-values)

## [Synopsis](eos_ospfv2_module.md#id1)

- This module configures and manages the attributes of ospfv2 on Arista EOS platforms.

## [Parameters](eos_ospfv2_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of configurations for ospfv2. |
| **processes**  list / elements=dictionary | A list of dictionary specifying the ospfv2 processes. |
| **adjacency**  dictionary | Configure adjacency options for OSPF instance. |
| **exchange_start**  dictionary | Configure exchange-start options for OSPF instance. |
| **threshold**  integer | Number of peers to bring up simultaneously. |
| **areas**  list / elements=dictionary | Specifies the configuration for OSPF areas |
| **area_id**  string | Specifies a 32 bit number expressed in decimal or dotted-decimal notation. |
| **default_cost**  integer | Specify the cost for default summary route in stub/NSSA area. |
| **filter**  dictionary | Specify the filter for incoming summary LSAs. |
| **address**  string | IP address. |
| **prefix_list**  string | Specify list to filter for incoming LSAs. |
| **subnet_address**  string | IP address with mask length |
| **subnet_mask**  string | IP subnet mask |
| **not_so_stubby**  dictionary | Configures NSSA parameters. |
| **default_information_originate**  dictionary | Originate default Type 7 LSA. |
| **metric**  integer | Metric for default route. |
| **metric_type**  integer | Metric type for default route. |
| **nssa_only**  boolean | Limit default advertisement to this NSSA area.  Choices:   - `false` - `true` |
| **lsa**  boolean | lsa parameters  Choices:   - `false` - `true` |
| **no_summary**  boolean | Filter all type-3 LSAs in the nssa area.  Choices:   - `false` - `true` |
| **nssa_only**  boolean | Disable Type-7 LSA p-bit setting  Choices:   - `false` - `true` |
| **set**  boolean | Set config up to not-so-stubby  Choices:   - `false` - `true` |
| **nssa**  dictionary | Configures NSSA parameters. |
| **default_information_originate**  dictionary | Originate default Type 7 LSA. |
| **metric**  integer | Metric for default route. |
| **metric_type**  integer | Metric type for default route. |
| **nssa_only**  boolean | Limit default advertisement to this NSSA area.  Choices:   - `false` - `true` |
| **no_summary**  boolean | Filter all type-3 LSAs in the nssa area.  Choices:   - `false` - `true` |
| **nssa_only**  boolean | Disable Type-7 LSA p-bit setting  Choices:   - `false` - `true` |
| **set**  boolean | Set config up to nssa  Choices:   - `false` - `true` |
| **range**  dictionary | Configure route summarization. |
| **address**  string | IP address. |
| **advertise**  boolean | Enable Advertisement of the range.  Choices:   - `false` - `true` |
| **cost**  integer | Configures the metric. |
| **subnet_address**  string | IP address with mask length |
| **subnet_mask**  string | IP subnet mask |
| **stub**  dictionary | Stub area. |
| **no_summary**  boolean | If False , Filter all type-3 LSAs in the stub area.  Choices:   - `false` - `true` |
| **set**  boolean | When true sets the stub config alone.  Choices:   - `false` - `true` |
| **auto_cost**  dictionary | Set auto-cost. |
| **reference_bandwidth**  integer | reference bandwidth in megabits per sec. |
| **bfd**  dictionary | Enable BFD. |
| **all_interfaces**  boolean | Enable BFD on all interfaces.  Choices:   - `false` - `true` |
| **default_information**  dictionary | Control distribution of default information. |
| **always**  boolean | Always advertise default route.  Choices:   - `false` - `true` |
| **metric**  integer | Metric for default route. |
| **metric_type**  integer | Metric type for default route. |
| **originate**  boolean | Distribute a default route.  Choices:   - `false` - `true` |
| **route_map**  string | Specify which route-map to use. |
| **default_metric**  integer | Configure the default metric for redistributed routes |
| **distance**  dictionary | Specifies the administrative distance for routes. |
| **external**  integer | Routes external to the area |
| **inter_area**  integer | Routes from other areas |
| **intra_area**  integer | Routes with in an area |
| **distribute_list**  dictionary | Specifies the list of routes to be filtered. |
| **prefix_list**  string | prefix list to be filtered |
| **route_map**  string | route map to be filtered |
| **dn_bit_ignore**  boolean | If True, Disable dn-bit check for Type-3 LSAs in non-default VRFs.  Choices:   - `false` - `true` |
| **fips_restrictions**  string | Use FIPS compliant algorithms |
| **graceful_restart**  dictionary | Enable graceful restart mode. |
| **grace_period**  integer | Specify maximum time to wait for graceful-restart to complete. |
| **set**  boolean | When true sets the grace_fulrestart config alone.  Choices:   - `false` - `true` |
| **graceful_restart_helper**  boolean | If True, Enable graceful restart helper.  Choices:   - `false` - `true` |
| **log_adjacency_changes**  dictionary | To configure link-state changes and transitions of OSPFv2 neighbors. |
| **detail**  boolean | If true , configures the switch to log all link-state changes.  Choices:   - `false` - `true` |
| **max_lsa**  dictionary | Specifies the switch behavior on reaching max lsa count. |
| **count**  integer | maximum count of lsas. |
| **ignore_count**  integer | No. of times the switch can shut down temporarily on warning |
| **ignore_time**  integer | time in minutes, for which the switch shoud be shutdown on max-lsa warning |
| **reset_time**  integer | Time in minutes, after which the shutdown counter resets. |
| **threshold**  integer | percentage of <count> , when a warning should be raised. |
| **warning**  boolean | Only give warning message when limit is exceeded  Choices:   - `false` - `true` |
| **max_metric**  dictionary | Set maximum metric. |
| **router_lsa**  dictionary | Maximum metric in self-originated router-LSAs. |
| **external_lsa**  dictionary | Override external-lsa metric with max-metric value. |
| **max_metric_value**  integer | Set max metric value for external LSAs. |
| **set**  boolean | Set external-lsa attribute.  Choices:   - `false` - `true` |
| **include_stub**  boolean | Set maximum metric for stub links in router-LSAs.  Choices:   - `false` - `true` |
| **on_startup**  dictionary | Set maximum metric temporarily after reboot. |
| **wait_period**  integer | Wait period in seconds after startup. |
| **set**  boolean | Set router-lsa attribute.  Choices:   - `false` - `true` |
| **summary_lsa**  dictionary | Override summary-lsa metric with max-metric value. |
| **max_metric_value**  integer | Set max metric value for external LSAs. |
| **set**  boolean | Set external-lsa attribute.  Choices:   - `false` - `true` |
| **maximum_paths**  integer | Maximum number of next-hops in an ECMP route. |
| **mpls_ldp**  boolean | mpls ldp sync configuration.  Choices:   - `false` - `true` |
| **networks**  list / elements=dictionary | Configure routing for a network. |
| **area**  string | Configure OSPF area. |
| **mask**  string | Network Wildcard Mask. |
| **network_address**  string | Network Address. |
| **prefix**  string | Prefix. |
| **passive_interface**  dictionary | Include interface but without actively running OSPF. |
| **default**  boolean | If True, Set all interfaces to passive by default  Choices:   - `false` - `true` |
| **interface_list**  string | Interface range. |
| **point_to_point**  boolean | Configure Point-to-point specific features.  Choices:   - `false` - `true` |
| **process_id**  integer | ID of OSPFV2 process. |
| **redistribute**  list / elements=dictionary | Specifies the routes to be redistributed |
| **isis_level**  string | ISIS levels. |
| **route_map**  string | Specify which route map to use. |
| **routes**  string | Route types (BGP,isis,connected etc) |
| **retransmission_threshold**  integer | Configure threshold for retransmission. |
| **rfc1583compatibility**  boolean | Specifies different methods for calculating summary route metrics.  Choices:   - `false` - `true` |
| **router_id**  string | 32-bit number assigned to a router running OSPFv2. |
| **shutdown**  boolean | Disable the OSPF instance.  Choices:   - `false` - `true` |
| **summary_address**  dictionary | Summary route configuration. |
| **address**  string | IP summary address. |
| **attribute_map**  string | Set attributes of summary route. |
| **mask**  string | Summary Mask. |
| **not_advertise**  boolean | Do not advertise summary route.  Choices:   - `false` - `true` |
| **prefix**  string | Prefix. |
| **tag**  integer | Set tag. |
| **timers**  list / elements=dictionary | Configure OSPF timers. |
| **lsa**  dictionary | Configure OSPF LSA timers. |
| **rx**  dictionary | Configure OSPF LSA receiving timers |
| **min_interval**  integer | Configure OSPF LSA arrival timer. |
| **tx**  dictionary | Configure OSPF LSA transmission timers. |
| **delay**  dictionary | Configure OSPF LSA transmission delay. |
| **initial**  integer | Delay to generate first occurrence of LSA in msecs. |
| **max**  integer | Maximum delay between originating the same LSA in msecs. |
| **min**  integer | Min delay between originating the same LSA in msecs. |
| **out_delay**  integer | Configure out-delay timer. |
| **pacing**  integer | Configure OSPF packet pacing. |
| **spf**  dictionary | Configure SPF timers |
| **initial**  integer | Initial SPF schedule delay in msecs. |
| **max**  integer | Max wait time between two SPFs in msecs. |
| **min**  integer | Min Hold time between two SPFs in msecs |
| **seconds**  integer | Seconds. |
| **throttle**  dictionary | Configure throttle timers(valid only for eos version < 4.23). |
| **attr**  string | throttle attribute. |
| **initial**  integer | Initial schedule delay in msecs. |
| **max**  integer | Max wait time |
| **min**  integer | Min Hold time |
| **traffic_engineering**  boolean | Enter traffic engineering config mode  Choices:   - `false` - `true` |
| **vrf**  string | VRF name . |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section ospf**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Choices:   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](eos_ospfv2_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](../network/user_guide/platform_eos.md).

## [Examples](eos_ospfv2_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# ------------
# localhost#show running-config | section ospf
# localhost#

  - name: replace Ospf configs
    arista.eos.eos_ospfv2:
      config:
        - processes:
            - process_id: 1
              adjacency:
                exchange_start:
                    threshold: 20045623
              areas:
                - filter:
                    address: "10.1.1.0/24"
                  id: "0.0.0.2"
                - id: "0.0.0.50"
                  range:
                    address: "172.20.0.0/16"
                    cost: 34
              default_information:
                metric: 100
                metric_type: 1
                originate: True
              distance:
                intra_area: 85
              max_lsa:
                count: 8000
                ignore_count: 3
                ignore_time: 6
                reset_time: 20
                threshold: 40
              networks:
                - area: "0.0.0.0"
                  prefix: 10.10.2.0/24
                - area: "0.0.0.0"
                  prefix: "10.10.3.0/24"
              redistribute:
                - routes: "static"
              router_id: "170.21.0.4"
            - process_id: 2
              vrf: "vrf01"
              areas:
                - id: "0.0.0.9"
                  default_cost: 20
              max_lsa:
                count: 8000
                ignore_count: 3
                ignore_time: 6
                reset_time: 20
                threshold: 40
              networks:
                - area: "0.0.0.0"
                  prefix: 10.10.2.0/24
                - area: "0.0.0.0"
                  prefix: "10.10.3.0/24"
              redistribute:
                - routes: "static"
              router_id: "170.21.0.4"
            - process_id: 2
              vrf: "vrf01"
              areas:
                - id: "0.0.0.9"
                  default_cost: 20
              max_lsa:
                count: 8000
                ignore_count: 3
                ignore_time: 6
                reset_time: 20
                threshold: 40
            - process_id: 3
              vrf: "vrf02"
              redistribute:
                - routes: "connected"

# After state:
# localhost#show running-config | section ospf
# router ospf 1
#    router-id 170.21.0.4
#    distance ospf intra-area 85
#    redistribute static
#    area 0.0.0.2 filter 10.1.1.0/24
#    area 0.0.0.50 range 172.20.0.0/16 cost 34
#    network 10.10.2.0/24 area 0.0.0.0
#    network 10.10.3.0/24 area 0.0.0.0
#    max-lsa 8000 40 ignore-time 6 ignore-count 3 reset-time 20
#    adjacency exchange-start threshold 20045623
#    default-information originate metric 100 metric-type 1
#
# router ospf 2 vrf vrf01
#    area 0.0.0.9 default-cost 20
#    max-lsa 8000 40 ignore-time 6 ignore-count 3 reset-time 20
# !
# router ospf 3 vrf vrf02
#    redistribute connected
#    max-lsa 12000
# localhost#
#
# "processes": [
#                 {
#                     "adjacency": {
#                         "exchange_start": {
#                             "threshold": 20045623
#                         }
#                     },
#                     "areas": [
#                         {
#                             "filter": {
#                                 "address": "10.1.1.0/24"
#                             },
#                             "id": "0.0.0.2"
#                         },
#                         {
#                             "id": "0.0.0.50",
#                             "range": {
#                                 "address": "172.20.0.0/16",
#                                 "cost": 34
#                             }
#                         }
#                     ],
#                     "default_information": {
#                         "metric": 100,
#                         "metric_type": 1,
#                         "originate": true
#                     },
#                     "distance": {
#                         "intra_area": 85
#                     },
#                     "max_lsa": {
#                         "count": 8000,
#                         "ignore_count": 3,
#                         "ignore_time": 6,
#                         "reset_time": 20,
#                         "threshold": 40
#                     },
#                     "networks": [
#                         {
#                             "area": "0.0.0.0",
#                             "prefix": "10.10.2.0/24"
#                         },
#                         {
#                             "area": "0.0.0.0",
#                             "prefix": "10.10.3.0/24"
#                         }
#                     ],
#                     "process_id": 1,
#                     "redistribute": [
#                         {
#                             "routes": "static"
#                         }
#                     ],
#                     "router_id": "170.21.0.4"
#                 },
#                 {
#                     "areas": [
#                         {
#                             "default_cost": 20,
#                             "id": "0.0.0.9"
#                         }
#                     ],
#                     "max_lsa": {
#                         "count": 8000,
#                         "ignore_count": 3,
#                         "ignore_time": 6,
#                         "reset_time": 20,
#                         "threshold": 40
#                     },
#                     "process_id": 2,
#                     "vrf": "vrf01"
#                 },
#                 {
#                     "max_lsa": {
#                         "count": 12000
#                     },
#                     "process_id": 3,
#                     "redistribute": [
#                         {
#                             "routes": "connected"
#                         }
#                     ],
#                     "vrf": "vrf02"
#                 }
#             ]
#         }
#     ]
#

# Using replaced:
# --------------

# Before State:

# localhost#show running-config | section ospf
# router ospf 1
#    router-id 170.21.0.4
#    distance ospf intra-area 85
#    redistribute static
#    area 0.0.0.2 filter 10.1.1.0/24
#    area 0.0.0.50 range 172.20.0.0/16 cost 34
#    network 10.10.2.0/24 area 0.0.0.0
#    network 10.10.3.0/24 area 0.0.0.0
#    max-lsa 8000 40 ignore-time 6 ignore-count 3 reset-time 20
#    adjacency exchange-start threshold 20045623
#    default-information originate metric 100 metric-type 1
# !
# router ospf 2 vrf vrf01
#    area 0.0.0.9 default-cost 20
#    max-lsa 8000 40 ignore-time 6 ignore-count 3 reset-time 20
# !
# router ospf 3 vrf vrf02
#    redistribute connected
#    max-lsa 12000
# localhost#
#
# "before": [
#         {
#             "processes": [
#                 {
#                     "adjacency": {
#                         "exchange_start": {
#                             "threshold": 20045623
#                         }
#                     },
#                     "areas": [
#                         {
#                             "filter": {
#                                 "address": "10.1.1.0/24"
#                             },
#                             "id": "0.0.0.2"
#                         },
#                         {
#                             "id": "0.0.0.50",
#                             "range": {
#                                 "address": "172.20.0.0/16",
#                                 "cost": 34
#                             }
#                         }
#                     ],
#                     "default_information": {
#                         "metric": 100,
#                         "metric_type": 1,
#                         "originate": true
#                     },
#                     "distance": {
#                         "intra_area": 85
#                     },
#                     "max_lsa": {
#                         "count": 8000,
#                         "ignore_count": 3,
#                         "ignore_time": 6,
#                         "reset_time": 20,
#                         "threshold": 40
#                     },
#                     "networks": [
#                         {
#                             "area": "0.0.0.0",
#                             "prefix": "10.10.2.0/24"
#                         },
#                         {
#                             "area": "0.0.0.0",
#                             "prefix": "10.10.3.0/24"
#                         }
#                     ],
#                     "process_id": 1,
#                     "redistribute": [
#                         {
#                             "routes": "static"
#                         }
#                     ],
#                     "router_id": "170.21.0.4"
#                 },
#                 {
#                     "areas": [
#                         {
#                             "default_cost": 20,
#                             "id": "0.0.0.9"
#                         }
#                     ],
#                     "max_lsa": {
#                         "count": 8000,
#                         "ignore_count": 3,
#                         "ignore_time": 6,
#                         "reset_time": 20,
#                         "threshold": 40
#                     },
#                     "process_id": 2,
#                     "vrf": "vrf01"
#                 },
#                 {
#                     "max_lsa": {
#                         "count": 12000
#                     },
#                     "process_id": 3,
#                     "redistribute": [
#                         {
#                             "routes": "connected"
#                         }
#                     ],
#                     "vrf": "vrf02"
#                 }
#             ]
#         }
#     ]
#
  - name: replace Ospf configs
    arista.eos.eos_ospfv2:
          config:
            - processes:
                - process_id: 2
                  vrf: "vrf01"
                  point_to_point: True
                  redistribute:
                    - routes: "isis"
                      isis_level: "level-1"

          state: replaced

# After State:
# -----------
#         "router ospf 2 vrf vrf01",
#         "no area 0.0.0.9 default-cost 20",
#         "no max-lsa  8000 40 ignore-time 6  ignore-count 3  reset-time 20",
#         "point-to-point routes",
#         "redistribute isis level-1"
#
# "after": [
#         {
#             "processes": [
#                 {
#                     "adjacency": {
#                         "exchange_start": {
#                             "threshold": 20045623
#                         }
#                     },
#                     "areas": [
#                         {
#                             "filter": {
#                                 "address": "10.1.1.0/24"
#                             },
#                             "id": "0.0.0.2"
#                         },
#                         {
#                             "id": "0.0.0.50",
#                             "range": {
#                                 "address": "172.20.0.0/16",
#                                 "cost": 34
#                             }
#                         }
#                     ],
#                     "default_information": {
#                         "metric": 100,
#                         "metric_type": 1,
#                         "originate": true
#                     },
#                     "distance": {
#                         "intra_area": 85
#                     },
#                     "max_lsa": {
#                         "count": 8000,
#                         "ignore_count": 3,
#                         "ignore_time": 6,
#                         "reset_time": 20,
#                         "threshold": 40
#                     },
#                     "networks": [
#                         {
#                             "area": "0.0.0.0",
#                             "prefix": "10.10.2.0/24"
#                         },
#                         {
#                             "area": "0.0.0.0",
#                             "prefix": "10.10.3.0/24"
#                         }
#                     ],
#                     "process_id": 1,
#                     "redistribute": [
#                         {
#                             "routes": "static"
#                         }
#                     ],
#                     "router_id": "170.21.0.4"
#                 },
#                 {
#                     "max_lsa": {
#                         "count": 12000
#                     },
#                     "process_id": 2,
#                     "redistribute": [
#                         {
#                             "isis_level": "level-1",
#                             "routes": "isis"
#                         }
#                     ],
#                     "vrf": "vrf01"
#                 },
#                 {
#                     "max_lsa": {
#                         "count": 12000
#                     },
#                     "process_id": 3,
#                     "redistribute": [
#                         {
#                             "routes": "connected"
#                         }
#                     ],
#                     "vrf": "vrf02"
#                 }
#             ]
#         }
#     ]
#

# Using overridden:
# ----------------

# Before State:
# localhost#show running-config | section ospf
# router ospf 1
#    router-id 170.21.0.4
#    distance ospf intra-area 85
#    redistribute static
#    area 0.0.0.2 filter 10.1.1.0/24
#    area 0.0.0.50 range 172.20.0.0/16 cost 34
#    network 10.10.2.0/24 area 0.0.0.0
#    network 10.10.3.0/24 area 0.0.0.0
#    max-lsa 8000 40 ignore-time 6 ignore-count 3 reset-time 20
#    adjacency exchange-start threshold 20045623
#    default-information originate metric 100 metric-type 1
# !
# router ospf 2 vrf vrf01
#    redistribute isis level-1
#    max-lsa 12000
# !
# router ospf 3 vrf vrf02
#    redistribute connected
#    max-lsa 12000
# localhost#
#
# "before": [
#         {
#             "processes": [
#                 {
#                     "adjacency": {
#                         "exchange_start": {
#                             "threshold": 20045623
#                         }
#                     },
#                     "areas": [
#                         {
#                             "filter": {
#                                 "address": "10.1.1.0/24"
#                             },
#                             "id": "0.0.0.2"
#                         },
#                         {
#                             "id": "0.0.0.50",
#                             "range": {
#                                 "address": "172.20.0.0/16",
#                                 "cost": 34
#                             }
#                         }
#                     ],
#                     "default_information": {
#                         "metric": 100,
#                         "metric_type": 1,
#                         "originate": true
#                     },
#                     "distance": {
#                         "intra_area": 85
#                     },
#                     "max_lsa": {
#                         "count": 8000,
#                         "ignore_count": 3,
#                         "ignore_time": 6,
#                         "reset_time": 20,
#                         "threshold": 40
#                     },
#                     "networks": [
#                         {
#                             "area": "0.0.0.0",
#                             "prefix": "10.10.2.0/24"
#                         },
#                         {
#                             "area": "0.0.0.0",
#                             "prefix": "10.10.3.0/24"
#                         }
#                     ],
#                     "process_id": 1,
#                     "redistribute": [
#                         {
#                             "routes": "static"
#                         }
#                     ],
#                     "router_id": "170.21.0.4"
#                 },
#                 {
#                     "max_lsa": {
#                         "count": 12000
#                     },
#                     "process_id": 2,
#                     "redistribute": [
#                         {
#                             "isis_level": "level-1",
#                             "routes": "isis"
#                         }
#                     ],
#                     "vrf": "vrf01"
#                 },
#                 {
#                     "max_lsa": {
#                         "count": 12000
#                     },
#                     "process_id": 3,
#                     "redistribute": [
#                         {
#                             "routes": "connected"
#                         }
#                     ],
#                     "vrf": "vrf02"
#                 }
#             ]
#         }
#     ]

  - name: override Ospf configs
    arista.eos.eos_ospfv2:
          config:
            - processes:
                - process_id: 2
                  vrf: "vrf01"
                  redistribute:
                    - routes: "connected"

          state: override

# After State:

# "no router ospf 1",
# "no router ospf 3",
# "router ospf 2 vrf vrf01",
# "no max-lsa  12000",
# "no redistribute isis level-1",
# "redistribute connected"
#
# "after": [
#         {
#             "processes": [
#                 {
#                     "max_lsa": {
#                         "count": 12000
#                     },
#                     "process_id": 2,
#                     "redistribute": [
#                         {
#                             "routes": "connected"
#                         }
#                     ],
#                     "vrf": "vrf01"
#                 }
#             ]
#         }
#     ]

# Using Deleted:

# localhost#show running-config | section ospf
# router ospf 1
#    router-id 170.21.0.4
#    distance ospf intra-area 85
#    redistribute static
#    area 0.0.0.2 filter 10.1.1.0/24
#    area 0.0.0.50 range 172.20.0.0/16 cost 34
#    network 10.10.2.0/24 area 0.0.0.0
#    network 10.10.3.0/24 area 0.0.0.0
#    max-lsa 8000 40 ignore-time 6 ignore-count 3 reset-time 20
#    adjacency exchange-start threshold 20045623
#    default-information originate metric 100 metric-type 1
# !
# router ospf 2 vrf vrf01
#    redistribute connected
#    area 0.0.0.9 default-cost 20
#    max-lsa 8000 40 ignore-time 6 ignore-count 3 reset-time 20
# !
# router ospf 3 vrf vrf02
#    redistribute connected
#    max-lsa 12000
# localhost#
#
# "before": [
#         {
#             "processes": [
#                 {
#                     "adjacency": {
#                         "exchange_start": {
#                             "threshold": 20045623
#                         }
#                     },
#                     "areas": [
#                         {
#                             "filter": {
#                                 "address": "10.1.1.0/24"
#                             },
#                             "id": "0.0.0.2"
#                         },
#                         {
#                             "id": "0.0.0.50",
#                             "range": {
#                                 "address": "172.20.0.0/16",
#                                 "cost": 34
#                             }
#                         }
#                     ],
#                     "default_information": {
#                         "metric": 100,
#                         "metric_type": 1,
#                         "originate": true
#                     },
#                     "distance": {
#                         "intra_area": 85
#                     },
#                     "max_lsa": {
#                         "count": 8000,
#                         "ignore_count": 3,
#                         "ignore_time": 6,
#                         "reset_time": 20,
#                         "threshold": 40
#                     },
#                     "networks": [
#                         {
#                             "area": "0.0.0.0",
#                             "prefix": "10.10.2.0/24"
#                         },
#                         {
#                             "area": "0.0.0.0",
#                             "prefix": "10.10.3.0/24"
#                         }
#                     ],
#                     "process_id": 1,
#                     "redistribute": [
#                         {
#                             "routes": "static"
#                         }
#                     ],
#                     "router_id": "170.21.0.4"
#                 },
#                 {
#                     "areas": [
#                         {
#                             "default_cost": 20,
#                             "id": "0.0.0.9"
#                         }
#                     ],
#                     "max_lsa": {
#                         "count": 8000,
#                         "ignore_count": 3,
#                         "ignore_time": 6,
#                         "reset_time": 20,
#                         "threshold": 40
#                     },
#                     "process_id": 2,
#                     "redistribute": [
#                         {
#                             "routes": "connected"
#                         }
#                     ],
#                     "vrf": "vrf01"
#                 },
#                 {
#                     "max_lsa": {
#                         "count": 12000
#                     },
#                     "process_id": 3,
#                     "redistribute": [
#                         {
#                             "routes": "connected"
#                         }
#                     ],
#                     "vrf": "vrf02"
#                 }
#             ]
#         }
#     ]

  - name: Delete Ospf configs
    arista.eos.eos_ospfv2:
          config:
            - processes:
                - process_id: 1

          state: deleted

# After State:
# Commands:
# "no router ospf 1"

# "after": [
#         {
#             "processes": [
#                 {
#                     "areas": [
#                         {
#                             "default_cost": 20,
#                             "id": "0.0.0.9"
#                         }
#                     ],
#                     "max_lsa": {
#                         "count": 8000,
#                         "ignore_count": 3,
#                         "ignore_time": 6,
#                         "reset_time": 20,
#                         "threshold": 40
#                     },
#                     "process_id": 2,
#                     "redistribute": [
#                         {
#                             "routes": "connected"
#                         }
#                     ],
#                     "vrf": "vrf01"
#                 },
#                 {
#                     "max_lsa": {
#                         "count": 12000
#                     },
#                     "process_id": 3,
#                     "redistribute": [
#                         {
#                             "routes": "connected"
#                         }
#                     ],
#                     "vrf": "vrf02"
#                 }
#             ]
#         }
#     ]

# Using gathered:
# localhost#show running-config | section ospf
# router ospf 2 vrf vrf01
#    redistribute connected
#    area 0.0.0.9 default-cost 20
#    max-lsa 8000 40 ignore-time 6 ignore-count 3 reset-time 20
# !
# router ospf 3 vrf vrf02
#    redistribute connected
#    max-lsa 12000
# localhost#

  - name: replace Ospf configs
    arista.eos.eos_ospfv2:
          state: gathered

# "gathered": [
#         {
#             "processes": [
#                 {
#                     "areas": [
#                         {
#                             "default_cost": 20,
#                             "id": "0.0.0.9"
#                         }
#                     ],
#                     "max_lsa": {
#                         "count": 8000,
#                         "ignore_count": 3,
#                         "ignore_time": 6,
#                         "reset_time": 20,
#                         "threshold": 40
#                     },
#                     "process_id": 2,
#                     "redistribute": [
#                         {
#                             "routes": "connected"
#                         }
#                     ],
#                     "vrf": "vrf01"
#                 },
#                 {
#                     "max_lsa": {
#                         "count": 12000
#                     },
#                     "process_id": 3,
#                     "redistribute": [
#                         {
#                             "routes": "connected"
#                         }
#                     ],
#                     "vrf": "vrf02"
#                 }
#             ]
#         }
#     ]

# Using parsed:
# ------------

# parsed.cfg
# router ospf 1
#    adjacency exchange-start threshold 20045623
#    area 0.0.0.2 filter 10.1.1.0/24
#    area 0.0.0.50  range 172.20.0.0/16 cost 34
#    default-information originate  metric 100 metric-type 1
#    distance ospf intra-area 85
#    max-lsa  80000 40 ignore-count 3  ignore-time 6  reset-time 20
#    network 10.10.2.0/24 area 0.0.0.0
#    network 10.10.3.0/24 area 0.0.0.0
#    redistribute static
#    router-id 170.21.0.4
# router ospf 2 vrf vrf01,
#    area 0.0.0.9 default-cost 20
#    max-lsa  80000 40 ignore-count 3  ignore-time 6  reset-time 20
# router ospf 3 vrf vrf02
#    redistribute static

  - name: Parse Ospf configs
    arista.eos.eos_ospfv2:
          running_config: "{{ lookup('file', './parsed.cfg') }}"
          state: parsed

# "parsed": [
#         {
#             "processes": [
#                 {
#                     "adjacency": {
#                         "exchange_start": {
#                             "threshold": 20045623
#                         }
#                     },
#                     "areas": [
#                         {
#                             "filter": {
#                                 "address": "10.1.1.0/24"
#                             },
#                             "id": "0.0.0.2"
#                         },
#                         {
#                             "id": "0.0.0.50",
#                             "range": {
#                                 "address": "172.20.0.0/16",
#                                 "cost": 34
#                             }
#                         }
#                     ],
#                     "default_information": {
#                         "metric": 100,
#                         "metric_type": 1,
#                         "originate": true
#                     },
#                     "distance": {
#                         "intra_area": 85
#                     },
#                     "max_lsa": {
#                         "count": 80000,
#                         "ignore_count": 3,
#                         "ignore_time": 6,
#                         "reset_time": 20,
#                         "threshold": 40
#                     },
#                     "networks": [
#                         {
#                             "area": "0.0.0.0",
#                             "prefix": "10.10.2.0/24"
#                         },
#                         {
#                             "area": "0.0.0.0",
#                             "prefix": "10.10.3.0/24"
#                         }
#                     ],
#                     "process_id": 1,
#                     "redistribute": [
#                         {
#                             "routes": "static"
#                         }
#                     ],
#                     "router_id": "170.21.0.4"
#                 },
#                 {
#                     "areas": [
#                         {
#                             "default_cost": 20,
#                             "id": "0.0.0.9"
#                         }
#                     ],
#                     "max_lsa": {
#                         "count": 80000,
#                         "ignore_count": 3,
#                         "ignore_time": 6,
#                         "reset_time": 20,
#                         "threshold": 40
#                     },
#                     "process_id": 2,
#                     "vrf": "vrf01,"
#                 },
#                 {
#                     "process_id": 3,
#                     "redistribute": [
#                         {
#                             "routes": "static"
#                         }
#                     ],
#                     "vrf": "vrf02"
#                 }
#             ]
#         }
#     ]

# Using rendered:
# --------------

  - name: replace Ospf configs
    arista.eos.eos_ospfv2:
          config:
            - processes:
              - process_id: 1
                adjacency:
                  exchange_start:
                    threshold: 20045623
                areas:
                - filter:
                    address: 10.1.1.0/24
                  id: 0.0.0.2
                - id: 0.0.0.50
                  range:
                    address: 172.20.0.0/16
                    cost: 34
                default_information:
                  metric: 100
                  metric_type: 1
                  originate: true
                distance:
                  intra_area: 85
                max_lsa:
                  count: 8000
                  ignore_count: 3
                  ignore_time: 6
                  reset_time: 20
                  threshold: 40
                networks:
                - area: 0.0.0.0
                  prefix: 10.10.2.0/24
                - area: 0.0.0.0
                  prefix: 10.10.3.0/24
                redistribute:
                - routes: static
                router_id: 170.21.0.4
          state: rendered

# "rendered": [
#         "router ospf 1",
#         "adjacency exchange-start threshold 20045623",
#         "area 0.0.0.2 filter 10.1.1.0/24",
#         "area 0.0.0.50  range 172.20.0.0/16 cost 34",
#         "default-information originate metric 100 metric-type 1",
#         "distance ospf intra-area 85",
#         "max-lsa  8000 40 ignore-count 3  ignore-time 6  reset-time 20",
#         "network 10.10.2.0/24 area 0.0.0.0",
#         "network 10.10.3.0/24 area 0.0.0.0",
#         "redistribute static",
#         "router-id 170.21.0.4"
#     ]
#
```

## [Return Values](eos_ospfv2_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["router ospf 1", "adjacency exchange-start threshold 20045623", "area 0.0.0.2 filter 10.1.1.0/24", "area 0.0.0.50  range 172.20.0.0/16 cost 34", "default-information originate metric 100 metric-type 1", "distance ospf intra-area 85", "max-lsa  8000 40 ignore-count 3  ignore-time 6  reset-time 20", "network 10.10.2.0/24 area 0.0.0.0", "network 10.10.3.0/24 area 0.0.0.0", "redistribute static", "router-id 170.21.0.4"]` |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
