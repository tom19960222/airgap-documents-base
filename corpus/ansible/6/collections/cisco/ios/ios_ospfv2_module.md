---
collection: ansible
version: "6"
title: "cisco.ios.ios_ospfv2 module – Resource module to configure OSPFv2."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_ospfv2_module.html
fetched_at: 2026-07-27T16:55:24+00:00
---
# cisco.ios.ios_ospfv2 module – Resource module to configure OSPFv2.

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
> To use it in a playbook, specify: `cisco.ios.ios_ospfv2`.

New in cisco.ios 1.0.0

- [Synopsis](ios_ospfv2_module.md#synopsis)
- [Parameters](ios_ospfv2_module.md#parameters)
- [Notes](ios_ospfv2_module.md#notes)
- [Examples](ios_ospfv2_module.md#examples)
- [Return Values](ios_ospfv2_module.md#return-values)

## [Synopsis](ios_ospfv2_module.md#id1)

- This module configures and manages the Open Shortest Path First (OSPF) version 2 on IOS platforms.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](ios_ospfv2_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of OSPF options. |
| **processes**  list / elements=dictionary | List of OSPF instance configurations. |
| **address_family**  dictionary | Router Address Family configuration mode |
| **default**  boolean | Set a command to its defaults  Choices:   - `false` - `true` |
| **snmp_context**  string | Modify snmp parameters  Configure SNMP context name |
| **topology**  dictionary | Associate the routing protocol to a topology instance |
| **base**  boolean | Entering router topology sub mode  Choices:   - `false` - `true` |
| **name**  string | Routing topology instance name |
| **tid**  boolean | Configuring the routing protocol topology tid  Note, please refer vendor documentation for valid values  Choices:   - `false` - `true` |
| **adjacency**  dictionary | To configure control adjacency formation |
| **max_adjacency**  integer | Maximum number of adjacencies allowed to be forming  Please refer vendor documentation for valid values |
| **min_adjacency**  integer | Initial number of adjacencies allowed to be forming in an area  Please refer vendor documentation for valid values |
| **none**  boolean | No initial  Choices:   - `false` - `true` |
| **areas**  list / elements=dictionary | OSPF area parameters |
| **area_id**  string | OSPF area ID as a decimal value. Please refer vendor documentation of Valid values.  OSPF area ID in IP address format(e.g. A.B.C.D) |
| **authentication**  dictionary | Area authentication |
| **enable**  boolean | Enable area authentication  Choices:   - `false` - `true` |
| **message_digest**  boolean | Use IPsec authentication  Choices:   - `false` - `true` |
| **capability**  boolean | Enable area specific capability  Enable exclusion of links from base topology  Choices:   - `false` - `true` |
| **default_cost**  integer | Set the summary default-cost of a NSSA/stub area  Stub’s advertised external route metric  Note, please refer vendor documentation for respective valid values |
| **filter_list**  list / elements=dictionary | Filter networks between OSPF areas |
| **direction**  string / required | The direction to apply on the filter networks sent to and from this area.  Choices:   - `"in"` - `"out"` |
| **name**  string | Name of an IP prefix-list |
| **nssa**  dictionary | Specify a NSSA area |
| **default_information_originate**  dictionary | Originate Type 7 default into NSSA area |
| **metric**  integer | OSPF default metric |
| **metric_type**  integer | OSPF metric type for default routes  OSPF Link State type  Choices:   - `1` - `2` |
| **nssa_only**  boolean | Limit default advertisement to this NSSA area  Choices:   - `false` - `true` |
| **no_ext_capability**  boolean | Do not send domain specific capabilities into NSSA  Choices:   - `false` - `true` |
| **no_redistribution**  boolean | No redistribution into this NSSA area  Choices:   - `false` - `true` |
| **no_summary**  boolean | Do not send summary LSA into NSSA  Choices:   - `false` - `true` |
| **set**  boolean | Enable a NSSA area  Choices:   - `false` - `true` |
| **translate**  string | Translate LSA  Always translate LSAs on this ABR  Suppress forwarding address in translated LSAs  Choices:   - `"always"` - `"suppress-fa"` |
| **ranges**  list / elements=dictionary | Summarize routes matching address/mask (border routers only) |
| **address**  string | IP address to match |
| **advertise**  boolean | Advertise this range (default)  Since, advertise when enabled is not shown in running-config idempotency won’t be maintained for the play in the second or next run of the play.  Choices:   - `false` - `true` |
| **cost**  integer | User specified metric for this range |
| **netmask**  string | IP mask for address |
| **not_advertise**  boolean | DoNotAdvertise this range  Choices:   - `false` - `true` |
| **sham_link**  dictionary | Define a sham link and its parameters |
| **cost**  integer | Associate a cost with the sham-link  Cost of the sham-link  Note, please refer vendor documentation for respective valid values |
| **destination**  string | IP addr associated with sham-link destination (A.B.C.D) |
| **source**  string | IP addr associated with sham-link source (A.B.C.D) |
| **ttl_security**  integer | TTL security check  Maximum number of IP hops allowed |
| **stub**  dictionary | Specify a stub area  Backbone can not be configured as stub area |
| **no_ext_capability**  boolean | Do not send domain specific capabilities into stub area  Choices:   - `false` - `true` |
| **no_summary**  boolean | Do not send summary LSA into stub area  Choices:   - `false` - `true` |
| **set**  boolean | Enable a stub area  Choices:   - `false` - `true` |
| **auto_cost**  dictionary | Calculate OSPF interface cost according to bandwidth |
| **reference_bandwidth**  integer | Use reference bandwidth method to assign OSPF cost  Note, refer vendor documentation for respective valid values |
| **set**  boolean | Enable OSPF auto-cost  Choices:   - `false` - `true` |
| **bfd**  boolean | BFD configuration commands  Enable BFD on all interfaces  Choices:   - `false` - `true` |
| **capability**  dictionary | Enable specific OSPF feature |
| **lls**  boolean | Link-local Signaling (LLS) support  Choices:   - `false` - `true` |
| **opaque**  boolean | Opaque LSA  Choices:   - `false` - `true` |
| **transit**  boolean | Transit Area  Choices:   - `false` - `true` |
| **vrf_lite**  boolean | Do not perform PE specific checks  Choices:   - `false` - `true` |
| **compatible**  dictionary | OSPF router compatibility list |
| **rfc1583**  boolean | compatible with RFC 1583  Choices:   - `false` - `true` |
| **rfc1587**  boolean | compatible with RFC 1587  Choices:   - `false` - `true` |
| **rfc5243**  boolean | supports DBD exchange optimization  Choices:   - `false` - `true` |
| **default_information**  dictionary | Control distribution of default information |
| **always**  boolean | Always advertise default route  Choices:   - `false` - `true` |
| **metric**  integer | OSPF default metric  Note, refer vendor documentation for respective valid values |
| **metric_type**  integer | OSPF metric type for default routes  Note, please refer vendor documentation for respective valid range |
| **originate**  boolean | Distribute a default route  Choices:   - `false` - `true` |
| **route_map**  string | Route-map reference name |
| **default_metric**  integer | Set metric of redistributed routes |
| **discard_route**  dictionary | Enable or disable discard-route installation |
| **external**  integer | Discard route for redistributed summarised routes  Administrative distance for redistributed summarised routes  Note, please refer vendor documentation for respective valid range |
| **internal**  integer | Discard route for summarised internal routes  Administrative distance for summarised internal routes  Note, please refer vendor documentation for respective valid range |
| **set**  boolean | Enable discard-route installation  Choices:   - `false` - `true` |
| **distance**  dictionary | Define an administrative distance |
| **admin_distance**  dictionary | OSPF Administrative distance |
| **acl**  string | Access-list name/number |
| **address**  string | IP Source address |
| **distance**  integer | Administrative distance |
| **wildcard_bits**  string | Wildcard bits |
| **ospf**  dictionary | OSPF distance |
| **external**  integer | External type 5 and type 7 routes |
| **inter_area**  integer | Inter-area routes |
| **intra_area**  integer | Intra-area routes |
| **distribute_list**  dictionary | Filter networks in routing updates |
| **acls**  list / elements=dictionary | IP access list |
| **direction**  string / required | Filter incoming and outgoing routing updates.  Choices:   - `"in"` - `"out"` |
| **interface**  string | Interface configuration (GigabitEthernet A/B)  Valid with incoming traffic |
| **name**  string / required | IP access list name/number |
| **protocol**  string | Protocol config (bgp 1).  Valid with outgoing traffic |
| **prefix**  dictionary | Filter prefixes in routing updates |
| **direction**  string / required | Filter incoming and outgoing routing updates.  Choices:   - `"in"` - `"out"` |
| **gateway_name**  string | Gateway name for filtering incoming updates based on gateway |
| **interface**  string | Interface configuration (GigabitEthernet A/B)  Valid with incoming traffic |
| **name**  string / required | Name of an IP prefix-list |
| **protocol**  string | Protocol config (bgp 1).  Valid with outgoing traffic |
| **route_map**  dictionary | Filter prefixes in routing updates |
| **name**  string / required | Route-map name |
| **domain_id**  dictionary | OSPF domain-id |
| **ip_address**  dictionary | IP address |
| **address**  string | OSPF domain ID in IP address format |
| **secondary**  boolean | Secondary Domain-ID  Choices:   - `false` - `true` |
| **null**  boolean | Null Domain-ID  Choices:   - `false` - `true` |
| **domain_tag**  integer | OSPF domain-tag which is OSPF domain tag - 32-bit value  Note, please refer vendor documentation for respective valid range |
| **event_log**  dictionary | Event Logging |
| **enable**  boolean | Enable event Logging  Choices:   - `false` - `true` |
| **one_shot**  boolean | Disable Logging When Log Buffer Becomes Full  Choices:   - `false` - `true` |
| **pause**  boolean | Pause Event Logging  Choices:   - `false` - `true` |
| **size**  integer | Maximum Number of Events Stored in the Event Log  Note, refer vendor documentation for respective valid values |
| **help**  boolean | Description of the interactive help system  Choices:   - `false` - `true` |
| **ignore**  boolean | Do not complain about specific event  Do not complain upon receiving LSA of the specified type, MOSPF Type 6 LSA  Choices:   - `false` - `true` |
| **interface_id**  boolean | Source of the interface ID  SNMP MIB ifIndex  Choices:   - `false` - `true` |
| **ispf**  boolean | Enable incremental SPF computation  Choices:   - `false` - `true` |
| **limit**  dictionary | Limit a specific OSPF feature and LS update, DBD, and LS request retransmissions |
| **dc**  dictionary | Demand circuit retransmissions |
| **disable**  boolean | Disble the feature  Choices:   - `false` - `true` |
| **number**  integer | The maximum number of retransmissions |
| **non_dc**  dictionary | Non-demand-circuit retransmissions |
| **disable**  boolean | Disble the feature  Choices:   - `false` - `true` |
| **number**  integer | The maximum number of retransmissions |
| **local_rib_criteria**  dictionary | Enable or disable usage of local RIB as route criteria |
| **enable**  boolean | Enable usage of local RIB as route criteria  Choices:   - `false` - `true` |
| **forwarding_address**  boolean | Local RIB used to validate external/NSSA forwarding addresses  Choices:   - `false` - `true` |
| **inter_area_summary**  boolean | Local RIB used as criteria for inter-area summaries  Choices:   - `false` - `true` |
| **nssa_translation**  boolean | Local RIB used as criteria for NSSA translation  Choices:   - `false` - `true` |
| **log_adjacency_changes**  dictionary | Log changes in adjacency state |
| **detail**  boolean | Log all state changes  Choices:   - `false` - `true` |
| **set**  boolean | Log changes in adjacency state  Choices:   - `false` - `true` |
| **max_lsa**  dictionary | Maximum number of non self-generated LSAs to accept |
| **ignore_count**  integer | Maximum number of times adjacencies can be suppressed  Note, refer vendor documentation for respective valid values |
| **ignore_time**  integer | Number of minutes during which all adjacencies are suppressed  Note, refer vendor documentation for respective valid values |
| **number**  integer | Maximum number of non self-generated LSAs to accept  Note, refer vendor documentation for respective valid values |
| **reset_time**  integer | Number of minutes after which ignore-count is reset to zero  Note, refer vendor documentation for respective valid values |
| **threshold_value**  integer | Threshold value (%) at which to generate a warning msg  Note, refer vendor documentation for respective valid values |
| **warning_only**  boolean | Only give a warning message when limit is exceeded  Choices:   - `false` - `true` |
| **max_metric**  dictionary | Set maximum metric |
| **external_lsa**  integer | Override external-lsa metric with max-metric value  Overriding metric in external-LSAs  Note, refer vendor documentation for respective valid values |
| **include_stub**  boolean | Set maximum metric for stub links in router-LSAs  Choices:   - `false` - `true` |
| **on_startup**  dictionary | Set maximum metric temporarily after reboot |
| **time**  integer | Time, in seconds, router-LSAs are originated with max-metric  Note, please refer vendor documentation for respective valid range |
| **wait_for_bgp**  boolean | Let BGP decide when to originate router-LSA with normal metric  Choices:   - `false` - `true` |
| **router_lsa**  boolean / required | Maximum metric in self-originated router-LSAs  Choices:   - `false` - `true` |
| **summary_lsa**  integer | Override summary-lsa metric with max-metric value  Note, please refer vendor documentation for respective valid range |
| **maximum_paths**  integer | Forward packets over multiple paths  Number of paths |
| **mpls**  dictionary | Configure MPLS routing protocol parameters |
| **ldp**  dictionary | routing protocol commands for MPLS LDP |
| **autoconfig**  dictionary | routing protocol commands for MPLS LDP |
| **area**  string | Configure an OSPF area to run MPLS LDP |
| **set**  boolean | Configure LDP automatic configuration and set the config  Choices:   - `false` - `true` |
| **sync**  boolean | Configure LDP-IGP Synchronization  Choices:   - `false` - `true` |
| **traffic_eng**  dictionary | Let BGP decide when to originate router-LSA with normal metric |
| **area**  string | Configure an ospf area to run MPLS Traffic Engineering  OSPF area ID as a decimal value or in IP address format |
| **autoroute_exclude**  string | MPLS TE autoroute exclude  Filter prefixes based on name of an IP prefix-list |
| **interface**  dictionary | MPLS TE interface configuration for this OSPF process |
| **area**  integer | Advertise MPLS TE information for this interface into area  OSPF area ID as a decimal value |
| **interface_type**  string | TE Interface configuration (GigabitEthernet A/B) |
| **mesh_group**  dictionary | Traffic Engineering Mesh-Group advertisement |
| **area**  string | configure flooding scope as area |
| **id**  integer | Mesh Group Id |
| **interface**  string | Interface configuration (GigabitEthernet A/B) |
| **multicast_intact**  boolean | MPLS TE and PIM interaction  Choices:   - `false` - `true` |
| **router_id_interface**  string | Router Interface configuration (GigabitEthernet A/B) |
| **neighbor**  dictionary | Specify a neighbor router |
| **address**  string | Neighbor address (A.B.C.D) |
| **cost**  integer | OSPF cost for point-to-multipoint neighbor metric  Note, please refer vendor documentation for respective valid range |
| **database_filter**  boolean | Filter OSPF LSA during synchronization and flooding for point-to-multipoint neighbor  Filter all outgoing LSA  Choices:   - `false` - `true` |
| **poll_interval**  integer | OSPF dead-router polling interval of non-broadcast neighbor in Seconds |
| **priority**  integer | OSPF priority of non-broadcast neighbor priority |
| **network**  list / elements=dictionary | Enable routing on an IP network |
| **address**  string | Network number |
| **area**  string | Set the OSPF area ID |
| **wildcard_bits**  string | OSPF wild card bits |
| **nsf**  dictionary | Non-stop forwarding |
| **cisco**  dictionary | Cisco Non-stop forwarding |
| **disable**  boolean | disable helper support  Choices:   - `false` - `true` |
| **helper**  boolean | helper support  Choices:   - `false` - `true` |
| **ietf**  dictionary | IETF graceful restart |
| **disable**  boolean | disable helper support  Choices:   - `false` - `true` |
| **helper**  boolean | helper support  Choices:   - `false` - `true` |
| **strict_lsa_checking**  boolean | enable helper strict LSA checking  Choices:   - `false` - `true` |
| **passive_interface**  string | passive_interface param is deprecated and a newer param passive_interfaces with added functionality’s is introduced, please meke use of the new available passive_interfaces instead.  Suppress routing updates on an interface (GigabitEthernet A/B)  Interface name with respective interface number |
| **passive_interfaces**  dictionary | Suppress routing updates on an interface |
| **default**  boolean | Suppress routing updates on all interfaces  Choices:   - `false` - `true` |
| **interface**  dictionary | Suppress/Un-Suppress routing updates on interface |
| **name**  list / elements=string | Name of interface (GigabitEthernet A/B) |
| **set_interface**  boolean | Suppress/Un-Suppress routing updates  Choices:   - `false` - `true` |
| **prefix_suppression**  boolean | Enable prefix suppression  Choices:   - `false` - `true` |
| **priority**  integer | OSPF topology priority  Note, refer vendor documentation for respective valid values |
| **process_id**  integer / required | Process ID |
| **queue_depth**  dictionary | Hello/Router process queue depth |
| **hello**  dictionary | OSPF Hello process queue depth |
| **max_packets**  integer | maximum number of packets in the queue |
| **unlimited**  boolean | Unlimited queue depth  Choices:   - `false` - `true` |
| **update**  dictionary | OSPF Router process queue depth |
| **max_packets**  integer | maximum number of packets in the queue |
| **unlimited**  boolean | Unlimited queue depth  Choices:   - `false` - `true` |
| **router_id**  string | Router-id address for this OSPF process  OSPF router-id in IP address format (A.B.C.D) |
| **shutdown**  boolean | Shutdown the router process  Choices:   - `false` - `true` |
| **summary_address**  dictionary | Configure IP address summaries |
| **address**  string | IP summary address |
| **mask**  string | IP Summary mask |
| **not_advertise**  boolean | Do not advertise or translate  Choices:   - `false` - `true` |
| **nssa_only**  boolean | Limit summary to NSSA areas  Choices:   - `false` - `true` |
| **tag**  integer | Set tag |
| **timers**  dictionary | Adjust routing timers |
| **lsa**  integer | OSPF LSA timers, arrival timer  The minimum interval in milliseconds between accepting the same LSA  Note, refer vendor documentation for respective valid values |
| **pacing**  dictionary | OSPF pacing timers |
| **flood**  integer | OSPF flood pacing timer  The minimum interval in msec to pace limit flooding on interface  Note, refer vendor documentation for respective valid values |
| **lsa_group**  integer | OSPF LSA group pacing timer  Interval in sec between group of LSA being refreshed or maxaged  Note, refer vendor documentation for respective valid values |
| **retransmission**  integer | OSPF retransmission pacing timer  The minimum interval in msec between neighbor retransmissions  Note, refer vendor documentation for respective valid values |
| **throttle**  dictionary | OSPF throttle timers |
| **lsa**  dictionary | OSPF LSA throttle timers |
| **first_delay**  integer | Delay to generate first occurrence of LSA in milliseconds  Note, refer vendor documentation for respective valid values |
| **max_delay**  integer | Maximum delay between originating the same LSA in milliseconds  Note, refer vendor documentation for respective valid values |
| **min_delay**  integer | Minimum delay between originating the same LSA in milliseconds  Note, refer vendor documentation for respective valid values |
| **spf**  dictionary | OSPF SPF throttle timers - Delay between receiving a change to SPF calculation in milliseconds - Note, refer vendor documentation for respective valid values |
| **between_delay**  integer | Delay between first and second SPF calculation in milliseconds  Note, refer vendor documentation for respective valid values |
| **max_delay**  integer | Maximum wait time in milliseconds for SPF calculations  Note, refer vendor documentation for respective valid values |
| **receive_delay**  integer | Delay between receiving a change to SPF calculation in milliseconds  Note, refer vendor documentation for respective valid values |
| **traffic_share**  boolean | How to compute traffic share over alternate paths  All traffic shared among min metric paths  Use different interfaces for equal-cost paths  Choices:   - `false` - `true` |
| **ttl_security**  dictionary | TTL security check |
| **hops**  integer | Maximum number of IP hops allowed  Note, refer vendor documentation for respective valid values |
| **set**  boolean | Enable TTL Security on all interfaces  Choices:   - `false` - `true` |
| **vrf**  string | Specify parameters for a VPN Routing/Forwarding instance |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **sh running-config | section ^router ospf**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](ios_ospfv2_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSv Version 15.2 on VIRL.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_ospfv2_module.md#id4)

```yaml+jinja
# Using deleted

# Before state:
# -------------
#
# router-ios#sh running-config | section ^router ospf
# router ospf 200 vrf blue
#  domain-id 192.0.3.1
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  area 10 capability default-exclusion
#  distribute-list 10 out
#  distribute-list 123 in
# router ospf 1
#  max-metric router-lsa on-startup 110
#  area 10 authentication message-digest
#  area 10 nssa default-information-originate metric 10
#  area 10 nssa translate type7 suppress-fa
#  area 10 default-cost 10
#  area 10 filter-list prefix test_prefix_out out
#  network 198.51.100.0 0.0.0.255 area 5
#  default-information originate

- name: Delete provided OSPF V2 processes
  cisco.ios.ios_ospfv2:
    config:
      processes:
      - process_id: 1
      - process_id: 200
        vrf: blue
    state: deleted

# Commands Fired:
# ---------------
#
# "commands": [
#        "no router ospf 1"
#    ]

# After state:
# -------------
# router-ios#sh running-config | section ^router ospf
# router ospf 200 vrf blue
#  domain-id 192.0.3.1
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  area 10 capability default-exclusion
#  distribute-list 10 out
#  distribute-list 123 in

# Using deleted without any config passed (NOTE: This will delete all OSPFV2 configuration from device)

# Before state:
# -------------
#
# router-ios#sh running-config | section ^router ospf
# router ospf 200 vrf blue
#  domain-id 192.0.3.1
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  area 10 capability default-exclusion
#  distribute-list 10 out
#  distribute-list 123 in
# router ospf 1
#  max-metric router-lsa on-startup 110
#  area 10 authentication message-digest
#  area 10 nssa default-information-originate metric 10
#  area 10 nssa translate type7 suppress-fa
#  area 10 default-cost 10
#  area 10 filter-list prefix test_prefix_out out
#  network 198.51.100.0 0.0.0.255 area 5
#  default-information originate

- name: Delete all OSPF processes
  cisco.ios.ios_ospfv2:
    state: deleted

# Commands Fired:
# ---------------
#
# "commands": [
#        "no router ospf 200 vrf blue",
#        "no router ospf 1"
#    ]

# After state:
# -------------
# router-ios#sh running-config | section ^router ospf
# router-ios#

# Using merged

# Before state:
# -------------
#
# router-ios#sh running-config | section ^router ospf
# router-ios#

- name: Merge provided OSPF V2 configuration
  cisco.ios.ios_ospfv2:
    config:
      processes:
      - process_id: 1
        max_metric:
          router_lsa: true
          on_startup:
            time: 110
        areas:
        - area_id: '5'
          capability: true
          authentication:
            enable: true
        - area_id: '10'
          authentication:
            message_digest: true
          nssa:
            default_information_originate:
              metric: 10
            translate: suppress-fa
          default_cost: 10
          filter_list:
          - name: test_prefix_in
            direction: in
          - name: test_prefix_out
            direction: out
        network:
          address: 198.51.100.0
          wildcard_bits: 0.0.0.255
          area: 5
        default_information:
          originate: true
        passive_interfaces:
          default: true
          interface:
            set_interface: False
            name:
              - GigabitEthernet0/1
              - GigabitEthernet0/2
      - process_id: 200
        vrf: blue
        domain_id:
          ip_address:
            address: 192.0.3.1
        max_metric:
          router_lsa: true
          on_startup:
            time: 100
        auto_cost:
          reference_bandwidth: 4
        areas:
        - area_id: '10'
          capability: true
        distribute_list:
          acls:
          - name: 10
            direction: out
          - name: 123
            direction: in
    state: merged

# Commands Fired:
# ---------------
#
#  "commands": [
#         "router ospf 200 vrf blue",
#         "auto-cost reference-bandwidth 4",
#         "distribute-list 10 out",
#         "distribute-list 123 in",
#         "domain-id 192.0.3.1",
#         "max-metric router-lsa on-startup 100",
#         "area 10 capability default-exclusion",
#         "router ospf 1",
#         "default-information originate",
#         "max-metric router-lsa on-startup 110",
#         "network 198.51.100.0 0.0.0.255 area 5",
#         "area 10 authentication message-digest",
#         "area 10 default-cost 10",
#         "area 10 nssa translate type7 suppress-fa",
#         "area 10 nssa default-information-originate metric 10",
#         "area 10 filter-list prefix test_prefix_out out",
#         "area 10 filter-list prefix test_prefix_in in",
#         "area 5 authentication",
#         "area 5 capability default-exclusion"
#         "passive-interface default"
#         "no passive-interface GigabitEthernet0/1"
#     ]

# After state:
# -------------
#
# router-ios#sh running-config | section ^router ospf
# router ospf 200 vrf blue
#  domain-id 192.0.3.1
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  area 10 capability default-exclusion
#  distribute-list 10 out
#  distribute-list 123 in
# router ospf 1
#  max-metric router-lsa on-startup 110
#  area 10 authentication message-digest
#  area 10 nssa default-information-originate metric 10
#  area 10 nssa translate type7 suppress-fa
#  area 10 default-cost 10
#  area 10 filter-list prefix test_prefix_out out
#  network 198.51.100.0 0.0.0.255 area 5
#  default-information originate
#  passive-interface default
#  no passive-interface GigabitEthernet0/1
#  no passive-interface GigabitEthernet0/2

# Using overridden

# Before state:
# -------------
#
# router-ios#sh running-config | section ^router ospf
# router ospf 200 vrf blue
#  domain-id 192.0.3.1
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  area 10 capability default-exclusion
#  distribute-list 10 out
#  distribute-list 123 in
# router ospf 1
#  max-metric router-lsa on-startup 110
#  area 10 authentication message-digest
#  area 10 nssa default-information-originate metric 10
#  area 10 nssa translate type7 suppress-fa
#  area 10 default-cost 10
#  area 10 filter-list prefix test_prefix_out out
#  network 198.51.100.0 0.0.0.255 area 5
#  default-information originate

- name: Override provided OSPF V2 configuration
  cisco.ios.ios_ospfv2:
    config:
      processes:
      - process_id: 200
        vrf: blue
        domain_id:
          ip_address:
            address: 192.0.4.1
        max_metric:
          router_lsa: true
          on_startup:
            time: 200
        maximum_paths: 15
        ttl_security:
          hops: 7
        areas:
        - area_id: '10'
          default_cost: 10
          authentication:
            message_digest: true
      - process_id: 100
        vrf: ospf_vrf
        domain_id:
          ip_address:
            address: 192.0.5.1
        auto_cost:
          reference_bandwidth: 5
        areas:
        - area_id: '5'
          authentication:
            message_digest: true
          nssa:
            default_information_originate:
              metric: 10
            translate: suppress-fa
    state: overridden

# Commands Fired:
# ---------------
#
# "commands": [
#         "no router ospf 1",
#         "router ospf 100 vrf ospf_vrf",
#         "auto-cost reference-bandwidth 5",
#         "domain-id 192.0.5.1",
#         "area 5 authentication message-digest",
#         "area 5 nssa translate type7 suppress-fa",
#         "area 5 nssa default-information-originate metric 10",
#         "router ospf 200 vrf blue",
#         "no auto-cost reference-bandwidth 4",
#         "no distribute-list 10 out",
#         "no distribute-list 123 in",
#         "domain-id 192.0.4.1",
#         "max-metric router-lsa on-startup 200",
#         "maximum-paths 15",
#         "ttl-security all-interfaces hops 7",
#         "area 10 authentication message-digest",
#         "no area 10 capability default-exclusion",
#         "area 10 default-cost 10"
#     ]

# After state:
# -------------
#
# router-ios#sh running-config | section ^router ospf
# router ospf 200 vrf blue
#  domain-id 192.0.4.1
#  max-metric router-lsa on-startup 200
#  ttl-security all-interfaces hops 7
#  area 10 authentication message-digest
#  area 10 default-cost 10
#  maximum-paths 15
# router ospf 100 vrf ospf_vrf
#  domain-id 192.0.5.1
#  auto-cost reference-bandwidth 5
#  area 5 authentication message-digest
#  area 5 nssa default-information-originate metric 10
#  area 5 nssa translate type7 suppress-fa

# Using replaced

# Before state:
# -------------
#
# router-ios#sh running-config | section ^router ospf
# router ospf 200 vrf blue
#  domain-id 192.0.3.1
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  area 10 capability default-exclusion
#  distribute-list 10 out
#  distribute-list 123 in
# router ospf 1
#  max-metric router-lsa on-startup 110
#  area 10 authentication message-digest
#  area 10 nssa default-information-originate metric 10
#  area 10 nssa translate type7 suppress-fa
#  area 10 default-cost 10
#  area 10 filter-list prefix test_prefix_out out
#  network 198.51.100.0 0.0.0.255 area 5
#  default-information originate

- name: Replaced provided OSPF V2 configuration
  cisco.ios.ios_ospfv2:
    config:
      processes:
      - process_id: 200
        vrf: blue
        domain_id:
          ip_address:
            address: 192.0.4.1
        max_metric:
          router_lsa: true
          on_startup:
            time: 200
        maximum_paths: 15
        ttl_security:
          hops: 7
        areas:
        - area_id: '10'
          default_cost: 10
          authentication:
            message_digest: true
      - process_id: 100
        vrf: ospf_vrf
        domain_id:
          ip_address:
            address: 192.0.5.1
        auto_cost:
          reference_bandwidth: 5
        areas:
        - area_id: '5'
          authentication:
            message_digest: true
          nssa:
            default_information_originate:
              metric: 10
            translate: suppress-fa
    state: replaced

# Commands Fired:
# ---------------
# "commands": [
#         "router ospf 100 vrf ospf_vrf",
#         "auto-cost reference-bandwidth 5",
#         "domain-id 192.0.5.1",
#         "area 5 authentication message-digest",
#         "area 5 nssa translate type7 suppress-fa",
#         "area 5 nssa default-information-originate metric 10",
#         "router ospf 200 vrf blue",
#         "no auto-cost reference-bandwidth 4",
#         "no distribute-list 10 out",
#         "no distribute-list 123 in",
#         "domain-id 192.0.4.1",
#         "max-metric router-lsa on-startup 200",
#         "maximum-paths 15",
#         "ttl-security all-interfaces hops 7",
#         "area 10 authentication message-digest",
#         "no area 10 capability default-exclusion",
#         "area 10 default-cost 10"
#     ]

# After state:
# -------------
# router-ios#sh running-config | section ^router ospf
# router ospf 200 vrf blue
#  domain-id 192.0.4.1
#  max-metric router-lsa on-startup 200
#  ttl-security all-interfaces hops 7
#  area 10 authentication message-digest
#  area 10 default-cost 10
#  maximum-paths 15
# router ospf 100 vrf ospf_vrf
#  domain-id 192.0.5.1
#  auto-cost reference-bandwidth 5
#  area 5 authentication message-digest
#  area 5 nssa default-information-originate metric 10
#  area 5 nssa translate type7 suppress-fa
# router ospf 1
#  max-metric router-lsa on-startup 110
#  area 5 capability default-exclusion
#  area 5 authentication
#  area 10 authentication message-digest
#  area 10 nssa default-information-originate metric 10
#  area 10 nssa translate type7 suppress-fa
#  area 10 default-cost 10
#  area 10 filter-list prefix test_prefix_in in
#  area 10 filter-list prefix test_prefix_out out
#  network 198.51.100.0 0.0.0.255 area 5
#  default-information originate

# Using Gathered

# Before state:
# -------------
#
# router-ios#sh running-config | section ^router ospf
# router ospf 200 vrf blue
#  domain-id 192.0.3.1
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  area 10 capability default-exclusion
#  distribute-list 10 out
#  distribute-list 123 in
# router ospf 1
#  max-metric router-lsa on-startup 110
#  area 10 authentication message-digest
#  area 10 nssa default-information-originate metric 10
#  area 10 nssa translate type7 suppress-fa
#  area 10 default-cost 10
#  area 10 filter-list prefix test_prefix_out out
#  network 198.51.100.0 0.0.0.255 area 5
#  default-information originate

- name: Gather OSPFV2 provided configurations
  cisco.ios.ios_ospfv2:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": {
#         "processes": [
#             {
#                 "areas": [
#                     {
#                         "area_id": "5",
#                         "authentication": {
#                             "enable": true
#                         },
#                         "capability": true
#                     },
#                     {
#                         "area_id": "10",
#                         "authentication": {
#                             "message_digest": true
#                         },
#                         "default_cost": 10,
#                         "filter_list": [
#                             {
#                                 "direction": "in",
#                                 "name": "test_prefix_in"
#                             },
#                             {
#                                 "direction": "out",
#                                 "name": "test_prefix_out"
#                             }
#                         ],
#                         "nssa": {
#                             "default_information_originate": {
#                                 "metric": 10
#                             },
#                             "translate": "suppress-fa"
#                         }
#                     }
#                 ],
#                 "default_information": {
#                     "originate": true
#                 },
#                 "max_metric": {
#                     "on_startup": {
#                         "time": 110
#                     },
#                     "router_lsa": true
#                 },
#                 "network": {
#                     "address": "198.51.100.0",
#                     "area": "5",
#                     "wildcard_bits": "0.0.0.255"
#                 },
#                 "process_id": 1
#             },
#             {
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "capability": true
#                     }
#                 ],
#                 "auto_cost": {
#                     "reference_bandwidth": 4
#                 },
#                 "distribute_list": {
#                     "acls": [
#                         {
#                             "direction": "out",
#                             "name": "10"
#                         },
#                         {
#                             "direction": "in",
#                             "name": "123"
#                         }
#                     ]
#                 },
#                 "domain_id": {
#                     "ip_address": {
#                         "address": "192.0.3.1"
#                     }
#                 },
#                 "max_metric": {
#                     "on_startup": {
#                         "time": 100
#                     },
#                     "router_lsa": true
#                 },
#                 "process_id": 200,
#                 "vrf": "blue"
#             }
#         ]
#      }

# After state:
# ------------
#
# router-ios#sh running-config | section ^router ospf
# router ospf 200 vrf blue
#  domain-id 192.0.3.1
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  area 10 capability default-exclusion
#  distribute-list 10 out
#  distribute-list 123 in
# router ospf 1
#  max-metric router-lsa on-startup 110
#  area 10 authentication message-digest
#  area 10 nssa default-information-originate metric 10
#  area 10 nssa translate type7 suppress-fa
#  area 10 default-cost 10
#  area 10 filter-list prefix test_prefix_out out
#  network 198.51.100.0 0.0.0.255 area 5
#  default-information originate

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_ospfv2:
    config:
      processes:
      - process_id: 1
        max_metric:
          router_lsa: true
          on_startup:
            time: 110
        areas:
        - area_id: '5'
          capability: true
          authentication:
            enable: true
        - area_id: '10'
          authentication:
            message_digest: true
          nssa:
            default_information_originate:
              metric: 10
            translate: suppress-fa
          default_cost: 10
          filter_list:
          - name: test_prefix_in
            direction: in
          - name: test_prefix_out
            direction: out
        network:
          address: 198.51.100.0
          wildcard_bits: 0.0.0.255
          area: 5
        default_information:
          originate: true
      - process_id: 200
        vrf: blue
        domain_id:
          ip_address:
            address: 192.0.3.1
        max_metric:
          router_lsa: true
          on_startup:
            time: 100
        auto_cost:
          reference_bandwidth: 4
        areas:
        - area_id: '10'
          capability: true
        distribute_list:
          acls:
          - name: 10
            direction: out
          - name: 123
            direction: in
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "router ospf 200 vrf blue",
#         "auto-cost reference-bandwidth 4",
#         "distribute-list 10 out",
#         "distribute-list 123 in",
#         "domain-id 192.0.3.1",
#         "max-metric router-lsa on-startup 100",
#         "area 10 capability default-exclusion",
#         "router ospf 1",
#         "default-information originate",
#         "max-metric router-lsa on-startup 110",
#         "network 198.51.100.0 0.0.0.255 area 5",
#         "area 10 authentication message-digest",
#         "area 10 default-cost 10",
#         "area 10 nssa translate type7 suppress-fa",
#         "area 10 nssa default-information-originate metric 10",
#         "area 10 filter-list prefix test_prefix_out out",
#         "area 10 filter-list prefix test_prefix_in in",
#         "area 5 authentication",
#         "area 5 capability default-exclusion"
#     ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# router ospf 100
#  auto-cost reference-bandwidth 5
#  domain-id 192.0.5.1
#  area 5 authentication message-digest
#  area 5 nssa translate type7 suppress-fa
#  area 5 nssa default-information-originate metric 10

- name: Parse the provided configuration with the existing running configuration
  cisco.ios.ios_ospfv2:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": {
#         "processes": [
#             {
#                 "areas": [
#                     {
#                         "area_id": "5",
#                         "authentication": {
#                             "message_digest": true
#                         },
#                         "nssa": {
#                             "default_information_originate": {
#                                 "metric": 10
#                             },
#                             "translate": "suppress-fa"
#                         }
#                     }
#                 ],
#                 "auto_cost": {
#                     "reference_bandwidth": 5
#                 },
#                 "domain_id": {
#                     "ip_address": {
#                         "address": "192.0.5.1"
#                     }
#                 },
#                 "process_id": 100
#             }
#         ]
#     }
```

## [Return Values](ios_ospfv2_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["router ospf 200 vrf blue", "auto-cost reference-bandwidth 5", "domain-id 192.0.4.1"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
