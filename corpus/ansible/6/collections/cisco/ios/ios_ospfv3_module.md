---
collection: ansible
version: "6"
title: "cisco.ios.ios_ospfv3 module – Resource module to configure OSPFv3."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_ospfv3_module.html
fetched_at: 2026-07-27T16:55:25+00:00
---
# cisco.ios.ios_ospfv3 module – Resource module to configure OSPFv3.

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
> To use it in a playbook, specify: `cisco.ios.ios_ospfv3`.

New in cisco.ios 1.1.0

- [Synopsis](ios_ospfv3_module.md#synopsis)
- [Parameters](ios_ospfv3_module.md#parameters)
- [Notes](ios_ospfv3_module.md#notes)
- [Examples](ios_ospfv3_module.md#examples)
- [Return Values](ios_ospfv3_module.md#return-values)

## [Synopsis](ios_ospfv3_module.md#id1)

- This module configures and manages the Open Shortest Path First (OSPF) version 3 on IOS platforms.

## [Parameters](ios_ospfv3_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of configurations for ospfv3. |
| **processes**  list / elements=dictionary | List of OSPF instance configurations. |
| **address_family**  list / elements=dictionary | Enter Address Family command mode |
| **adjacency**  dictionary | Control adjacency formation |
| **disable**  boolean | Disable adjacency staggering  Choices:   - `false` - `true` |
| **max_adjacency**  integer | Maximum number of adjacencies allowed to be forming  Please refer vendor documentation for valid values |
| **min_adjacency**  integer | Initial number of adjacencies allowed to be forming in an area  Please refer vendor documentation for valid values |
| **none**  boolean | No initial  Choices:   - `false` - `true` |
| **afi**  string | Enter Address Family command mode  Choices:   - `"ipv4"` - `"ipv6"` |
| **areas**  list / elements=dictionary | OSPF area parameters |
| **area_id**  string | OSPF area ID as a decimal value. Please refer vendor documentation of Valid values.  OSPF area ID in IP address format(e.g. A.B.C.D) |
| **authentication**  dictionary | Authentication parameters |
| **key_chain**  string | Use a key-chain for cryptographic authentication keys |
| **null**  boolean | Use no authentication  Choices:   - `false` - `true` |
| **default_cost**  integer | Set the summary default-cost of a NSSA/stub area  Stub’s advertised external route metric  Note, please refer vendor documentation for respective valid values |
| **filter_list**  list / elements=dictionary | Filter networks between OSPFv3 areas |
| **direction**  string / required | The direction to apply on the filter networks sent to and from this area.  Choices:   - `"in"` - `"out"` |
| **name**  string | Name of an IP prefix-list |
| **normal**  boolean | Specify a normal area type  Choices:   - `false` - `true` |
| **nssa**  dictionary | Specify a NSSA area |
| **default_information_originate**  dictionary | Originate Type 7 default into NSSA area |
| **metric**  integer | OSPF default metric |
| **metric_type**  integer | OSPF metric type for default routes  OSPF Link State type  Choices:   - `1` - `2` |
| **nssa_only**  boolean | Limit default advertisement to this NSSA area  Choices:   - `false` - `true` |
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
| **authentication**  dictionary | Authentication parameters |
| **key_chain**  string | Use a key-chain for cryptographic authentication keys |
| **null**  boolean | Use no authentication  Choices:   - `false` - `true` |
| **cost**  integer | Associate a cost with the sham-link  Cost of the sham-link |
| **destination**  string | IPv6 address associated with sham-link destination (X:X:X:X::X) |
| **source**  string | IPv6 address associated with sham-link source (X:X:X:X::X) |
| **ttl_security**  integer | TTL security check  maximum number of hops allowed |
| **stub**  dictionary | Specify a stub area  Backbone can not be configured as stub area |
| **no_summary**  boolean | Do not send summary LSA into stub area  Choices:   - `false` - `true` |
| **set**  boolean | Enable a stub area  Choices:   - `false` - `true` |
| **authentication**  dictionary | Authentication parameters  Authentication operation mode |
| **deployment**  boolean | Deployment mode of operation  Choices:   - `false` - `true` |
| **normal**  boolean | Normal mode of operation  Choices:   - `false` - `true` |
| **auto_cost**  dictionary | Calculate OSPF interface cost according to bandwidth |
| **reference_bandwidth**  integer | Use reference bandwidth method to assign OSPF cost  Note, refer vendor documentation for respective valid values |
| **set**  boolean | Enable OSPF auto-cost  Choices:   - `false` - `true` |
| **bfd**  dictionary | BFD configuration commands |
| **all_interfaces**  boolean | Enable BFD on all interfaces  Choices:   - `false` - `true` |
| **disable**  boolean | Disable BFD on all interfaces  Choices:   - `false` - `true` |
| **capability**  boolean | Enable a specific feature  Do not perform PE specific checks  Choices:   - `false` - `true` |
| **compatible**  dictionary | OSPFv3 router compatibility list |
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
| **external**  boolean | Discard route for summarised redistributed routes  Choices:   - `false` - `true` |
| **internal**  boolean | Discard route for summarised inter-area routes  Choices:   - `false` - `true` |
| **sham_link**  boolean | Discard route for sham-link routes  Choices:   - `false` - `true` |
| **distance**  integer | Define an administrative distance  Note, please refer vendor documentation for respective valid range |
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
| **event_log**  dictionary | Event Logging |
| **enable**  boolean | Enable event Logging  Choices:   - `false` - `true` |
| **one_shot**  boolean | Disable Logging When Log Buffer Becomes Full  Choices:   - `false` - `true` |
| **pause**  boolean | Pause Event Logging  Choices:   - `false` - `true` |
| **size**  integer | Maximum Number of Events Stored in the Event Log  Note, refer vendor documentation for respective valid values |
| **graceful_restart**  dictionary | Graceful-restart options  helper support |
| **disable**  boolean | disable helper support  Choices:   - `false` - `true` |
| **enable**  boolean | helper support enabled  Choices:   - `false` - `true` |
| **strict_lsa_checking**  boolean | enable helper strict LSA checking  Choices:   - `false` - `true` |
| **interface_id**  dictionary | Source of the interface ID |
| **ios_if_index**  boolean | IOS interface number  Choices:   - `false` - `true` |
| **snmp_if_index**  boolean | SNMP MIB ifIndex  Choices:   - `false` - `true` |
| **limit**  dictionary | Limit a specific OSPF feature |
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
| **manet**  dictionary | Specify MANET OSPF parameters |
| **cache**  dictionary | Specify MANET cache sizes |
| **acknowledgement**  integer | Specify MANET acknowledgement cache size  Maximum number of acknowledgements in cache |
| **update**  integer | Specify MANET LSA cache size  Maximum number of LSAs in cache |
| **hello**  dictionary | Unicast Hellos rather than multicast |
| **multicast**  boolean | Multicast Hello requests and responses rather than unicast  Choices:   - `false` - `true` |
| **unicast**  boolean | Unicast Hello requests and responses rather than multicast  Choices:   - `false` - `true` |
| **peering**  dictionary | MANET OSPF Smart Peering |
| **disable**  boolean | Disable selective peering  Choices:   - `false` - `true` |
| **per_interface**  boolean | Select peers per interface rather than per node  Choices:   - `false` - `true` |
| **redundancy**  integer | Redundant paths  Number of redundant OSPF paths |
| **set**  boolean | Enable selective peering  Choices:   - `false` - `true` |
| **willingness**  integer | Specify and Relay willingness value |
| **max_lsa**  dictionary | Maximum number of non self-generated LSAs to accept |
| **ignore_count**  integer | Maximum number of times adjacencies can be suppressed  Note, refer vendor documentation for respective valid values |
| **ignore_time**  integer | Number of minutes during which all adjacencies are suppressed  Note, refer vendor documentation for respective valid values |
| **number**  integer | Maximum number of non self-generated LSAs to accept  Note, refer vendor documentation for respective valid values |
| **reset_time**  integer | Number of minutes after which ignore-count is reset to zero  Note, refer vendor documentation for respective valid values |
| **threshold_value**  integer | Threshold value (%) at which to generate a warning msg  Note, refer vendor documentation for respective valid values |
| **warning_only**  boolean | Only give a warning message when limit is exceeded  Choices:   - `false` - `true` |
| **max_metric**  dictionary | Set maximum metric  Maximum metric in self-originated router-LSAs |
| **disable**  boolean | disable maximum metric in self-originated router-LSAs  Choices:   - `false` - `true` |
| **external_lsa**  integer | Override external-lsa metric with max-metric value  Overriding metric in external-LSAs  Note, refer vendor documentation for respective valid values |
| **inter_area_lsas**  integer | Override inter-area-lsas metric with max-metric value  Overriding metric in inter-area-LSAs  Note, refer vendor documentation for respective valid values |
| **on_startup**  dictionary | Set maximum metric temporarily after reboot |
| **time**  integer | Time, in seconds, router-LSAs are originated with max-metric  Note, please refer vendor documentation for respective valid range |
| **wait_for_bgp**  boolean | Let BGP decide when to originate router-LSA with normal metric  Choices:   - `false` - `true` |
| **stub_prefix_lsa**  boolean | Set maximum metric for stub links in prefix LSAs  Choices:   - `false` - `true` |
| **maximum_paths**  integer | Forward packets over multiple paths  Number of paths |
| **passive_interface**  string | Suppress routing updates on an interface |
| **prefix_suppression**  dictionary | Prefix suppression |
| **disable**  boolean | Disable prefix suppression  Choices:   - `false` - `true` |
| **enable**  boolean | Enable prefix suppression  Choices:   - `false` - `true` |
| **queue_depth**  dictionary | Hello/Router process queue depth |
| **hello**  dictionary | OSPF Hello process queue depth |
| **max_packets**  integer | maximum number of packets in the queue |
| **unlimited**  boolean | Unlimited queue depth  Choices:   - `false` - `true` |
| **update**  dictionary | OSPF Router process queue depth |
| **max_packets**  integer | maximum number of packets in the queue |
| **unlimited**  boolean | Unlimited queue depth  Choices:   - `false` - `true` |
| **router_id**  string | Router-id address for this OSPF process  OSPF router-id in IP address format (A.B.C.D) |
| **shutdown**  dictionary | Shutdown the router process |
| **disable**  boolean | Disable Shutdown  Choices:   - `false` - `true` |
| **enable**  boolean | Shutdown the router process  Choices:   - `false` - `true` |
| **summary_prefix**  dictionary | Configure IP address summaries |
| **address**  string | IP summary address (A.B.C.D)  IP prefix <network>/<length> (A.B.C.D/nn) |
| **mask**  string | IP Summary mask |
| **not_advertise**  boolean | Do not advertise or translate  Choices:   - `false` - `true` |
| **nssa_only**  boolean | Limit summary to NSSA areas  Choices:   - `false` - `true` |
| **tag**  integer | Set tag |
| **timers**  dictionary | Adjust routing timers |
| **lsa**  integer | OSPF LSA timers, arrival timer  The minimum interval in milliseconds between accepting the same LSA  Note, refer vendor documentation for respective valid values |
| **manet**  dictionary | OSPF MANET timers |
| **cache**  dictionary | Specify MANET cache sizes |
| **acknowledgement**  integer | Specify MANET acknowledgement cache size |
| **redundancy**  integer | Specify MANET LSA cache size |
| **hello**  boolean | Unicast Hellos rather than multicast  Unicast Hello requests and responses rather than multicast  Choices:   - `false` - `true` |
| **peering**  dictionary | MANET OSPF Smart Peering |
| **per_interface**  boolean | Select peers per interface rather than per node  Choices:   - `false` - `true` |
| **redundancy**  integer | Redundant paths  Number of redundant OSPF paths |
| **set**  boolean | Enable selective peering  Choices:   - `false` - `true` |
| **willingness**  integer | Specify and Relay willingness value |
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
| **unicast**  boolean | Address Family modifier  Choices:   - `false` - `true` |
| **vrf**  string | Specify parameters for a VPN Routing/Forwarding instance |
| **adjacency**  dictionary | Control adjacency formation |
| **max_adjacency**  integer | Maximum number of adjacencies allowed to be forming  Please refer vendor documentation for valid values |
| **min_adjacency**  integer | Initial number of adjacencies allowed to be forming in an area  Please refer vendor documentation for valid values |
| **none**  boolean | No initial  Choices:   - `false` - `true` |
| **areas**  list / elements=dictionary | OSPF area parameters |
| **area_id**  string | OSPF area ID as a decimal value. Please refer vendor documentation of Valid values.  OSPF area ID in IP address format(e.g. A.B.C.D) |
| **authentication**  dictionary | Authentication parameters |
| **ipsec**  dictionary | Use IPsec authentication |
| **hex_string**  string | SHA-1 key (40 chars) |
| **md5**  integer | Use MD5 authentication |
| **sha1**  integer | Use SHA-1 authentication |
| **spi**  integer | Set the SPI (Security Parameters Index) |
| **key_chain**  string | Use a key-chain for cryptographic authentication keys |
| **default_cost**  integer | Set the summary default-cost of a NSSA/stub area  Stub’s advertised external route metric  Note, please refer vendor documentation for respective valid values |
| **nssa**  dictionary | Specify a NSSA area |
| **default_information_originate**  dictionary | Originate Type 7 default into NSSA area |
| **metric**  integer | OSPF default metric |
| **metric_type**  integer | OSPF metric type for default routes  OSPF Link State type  Choices:   - `1` - `2` |
| **nssa_only**  boolean | Limit default advertisement to this NSSA area  Choices:   - `false` - `true` |
| **no_redistribution**  boolean | No redistribution into this NSSA area  Choices:   - `false` - `true` |
| **no_summary**  boolean | Do not send summary LSA into NSSA  Choices:   - `false` - `true` |
| **set**  boolean | Enable a NSSA area  Choices:   - `false` - `true` |
| **translate**  string | Translate LSA  Always translate LSAs on this ABR  Suppress forwarding address in translated LSAs  Choices:   - `"always"` - `"suppress-fa"` |
| **stub**  dictionary | Specify a stub area  Backbone can not be configured as stub area |
| **no_summary**  boolean | Do not send summary LSA into stub area  Choices:   - `false` - `true` |
| **set**  boolean | Enable a stub area  Choices:   - `false` - `true` |
| **authentication**  boolean | Authentication parameter mode  Deployment mode of operation  Choices:   - `false` - `true` |
| **auto_cost**  dictionary | Calculate OSPF interface cost according to bandwidth |
| **reference_bandwidth**  integer | Use reference bandwidth method to assign OSPF cost  Note, refer vendor documentation for respective valid values |
| **set**  boolean | Enable OSPF auto-cost  Choices:   - `false` - `true` |
| **bfd**  boolean | BFD configuration commands  Enable BFD on all interfaces  Choices:   - `false` - `true` |
| **compatible**  dictionary | OSPFv3 router compatibility list |
| **rfc1583**  boolean | compatible with RFC 1583  Choices:   - `false` - `true` |
| **rfc1587**  boolean | compatible with RFC 1587  Choices:   - `false` - `true` |
| **rfc5243**  boolean | supports DBD exchange optimization  Choices:   - `false` - `true` |
| **event_log**  dictionary | Event Logging |
| **enable**  boolean | Enable event Logging  Choices:   - `false` - `true` |
| **one_shot**  boolean | Disable Logging When Log Buffer Becomes Full  Choices:   - `false` - `true` |
| **pause**  boolean | Pause Event Logging  Choices:   - `false` - `true` |
| **size**  integer | Maximum Number of Events Stored in the Event Log  Note, refer vendor documentation for respective valid values |
| **graceful_restart**  dictionary | Graceful-restart options for helper support |
| **disable**  boolean | disable helper support  Choices:   - `false` - `true` |
| **strict_lsa_checking**  boolean | enable helper strict LSA checking  Choices:   - `false` - `true` |
| **help**  boolean | Description of the interactive help system  Choices:   - `false` - `true` |
| **interface_id**  boolean | Source of the interface ID  SNMP MIB ifIndex  Choices:   - `false` - `true` |
| **limit**  dictionary | Limit a specific OSPF feature and LS update, DBD, and LS request retransmissions |
| **dc**  dictionary | Demand circuit retransmissions |
| **disable**  boolean | Disable the feature  Choices:   - `false` - `true` |
| **number**  integer | The maximum number of retransmissions |
| **non_dc**  dictionary | Non-demand-circuit retransmissions |
| **disable**  boolean | Disable the feature  Choices:   - `false` - `true` |
| **number**  integer | The maximum number of retransmissions |
| **local_rib_criteria**  dictionary | Enable or disable usage of local RIB as route criteria |
| **enable**  boolean | Enable usage of local RIB as route criteria  Choices:   - `false` - `true` |
| **forwarding_address**  boolean | Local RIB used to validate external/NSSA forwarding addresses  Choices:   - `false` - `true` |
| **inter_area_summary**  boolean | Local RIB used as criteria for inter-area summaries  Choices:   - `false` - `true` |
| **nssa_translation**  boolean | Local RIB used as criteria for NSSA translation  Choices:   - `false` - `true` |
| **log_adjacency_changes**  dictionary | Log changes in adjacency state |
| **detail**  boolean | Log all state changes  Choices:   - `false` - `true` |
| **set**  boolean | Log changes in adjacency state  Choices:   - `false` - `true` |
| **manet**  dictionary | Specify MANET OSPF parameters |
| **cache**  dictionary | Specify MANET cache sizes |
| **acknowledgement**  integer | Specify MANET acknowledgement cache size |
| **redundancy**  integer | Specify MANET LSA cache size |
| **hello**  boolean | Unicast Hellos rather than multicast  Unicast Hello requests and responses rather than multicast  Choices:   - `false` - `true` |
| **peering**  dictionary | MANET OSPF Smart Peering |
| **per_interface**  boolean | Select peers per interface rather than per node  Choices:   - `false` - `true` |
| **redundancy**  integer | Redundant paths  Number of redundant OSPF paths |
| **set**  boolean | Enable selective peering  Choices:   - `false` - `true` |
| **willingness**  integer | Specify and Relay willingness value |
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
| **passive_interface**  string | Suppress routing updates on an interface |
| **prefix_suppression**  boolean | Enable prefix suppression  Choices:   - `false` - `true` |
| **process_id**  integer / required | Process ID |
| **queue_depth**  dictionary | Hello/Router process queue depth |
| **hello**  dictionary | OSPF Hello process queue depth |
| **max_packets**  integer | maximum number of packets in the queue |
| **unlimited**  boolean | Unlimited queue depth  Choices:   - `false` - `true` |
| **router_id**  string | Router-id address for this OSPF process  OSPF router-id in IP address format (A.B.C.D) |
| **shutdown**  boolean | Shutdown the router process  Choices:   - `false` - `true` |
| **timers**  dictionary | Adjust routing timers |
| **lsa**  integer | OSPF LSA timers, arrival timer  The minimum interval in milliseconds between accepting the same LSA  Note, refer vendor documentation for respective valid values |
| **manet**  dictionary | OSPF MANET timers |
| **cache**  dictionary | Specify MANET cache sizes |
| **acknowledgement**  integer | Specify MANET acknowledgement cache size |
| **redundancy**  integer | Specify MANET LSA cache size |
| **hello**  boolean | Unicast Hellos rather than multicast  Unicast Hello requests and responses rather than multicast  Choices:   - `false` - `true` |
| **peering**  dictionary | MANET OSPF Smart Peering |
| **per_interface**  boolean | Select peers per interface rather than per node  Choices:   - `false` - `true` |
| **redundancy**  integer | Redundant paths  Number of redundant OSPF paths |
| **set**  boolean | Enable selective peering  Choices:   - `false` - `true` |
| **willingness**  integer | Specify and Relay willingness value |
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
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **sh running-config | section ^router ospfv3**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](ios_ospfv3_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSv Version 15.2 on VIRL.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_ospfv3_module.md#id4)

```yaml+jinja
# Using deleted

# Before state:
# -------------
#
# router-ios#sh running-config | section ^router ospfv3
# router ospfv3 1
#  max-metric router-lsa on-startup 110
#  area 10 nssa default-information-originate metric 10
#  !
#  address-family ipv4 unicast vrf blue
#   adjacency stagger 50 50
#   area 25 nssa default-information-originate metric 25 nssa-only
#  exit-address-family
# router ospfv3 200
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  !
#  address-family ipv4 unicast
#   adjacency stagger 200 200
#  exit-address-family

- name: Delete provided OSPF V3 processes
  cisco.ios.ios_ospfv3:
    config:
      processes:
      - process_id: 1
    state: deleted

# Commands Fired:
# ---------------
#
# "commands": [
#        "no router ospfv3 1"
#    ]

# After state:
# -------------
# router-ios#sh running-config | section ^router ospfv3
# router ospfv3 200
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  !
#  address-family ipv4 unicast
#   adjacency stagger 200 200
#  exit-address-family

# Using deleted without any config passed (NOTE: This will delete all OSPFV3 configuration from device)

# Before state:
# -------------
#
# router-ios#sh running-config | section ^router ospfv3
# router ospfv3 1
#  max-metric router-lsa on-startup 110
#  area 10 nssa default-information-originate metric 10
#  !
#  address-family ipv4 unicast vrf blue
#   adjacency stagger 50 50
#   area 25 nssa default-information-originate metric 25 nssa-only
#  exit-address-family
# router ospfv3 200
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  !
#  address-family ipv4 unicast
#   adjacency stagger 200 200
#  exit-address-family

- name: Delete all OSPF processes
  cisco.ios.ios_ospfv3:
    state: deleted

# Commands Fired:
# ---------------
#
# "commands": [
#        "no router ospfv3 200",
#        "no router ospfv3 1"
#    ]

# After state:
# -------------
# router-ios#sh running-config | section ^router ospfv3
# router-ios#

# Using merged

# Before state:
# -------------
#
# router-ios#sh running-config | section ^router ospfv3
# router-ios#

- name: Merge provided OSPFV3 configuration
  cisco.ios.ios_ospfv3:
    config:
      processes:
      - process_id: 1
        max_metric:
          router_lsa: true
          on_startup:
            time: 110
        address_family:
          - afi: ipv4
            unicast: true
            vrf: blue
            adjacency:
              min_adjacency: 50
              max_adjacency: 50
            areas:
              - area_id: 25
                nssa:
                  default_information_originate:
                    metric: 25
                    nssa_only: true
        areas:
          - area_id: "10"
            nssa:
              default_information_originate:
                metric: 10
        timers:
          throttle:
            lsa:
              first_delay: 12
              min_delay: 14
              max_delay: 16
      - process_id: 200
        address_family:
          - afi: ipv4
            unicast: true
            adjacency:
              min_adjacency: 200
              max_adjacency: 200
        max_metric:
          router_lsa: true
          on_startup:
            time: 100
        auto_cost:
          reference_bandwidth: 4
    state: merged

# Commands Fired:
# ---------------
#
#  "commands": [
#         "router ospfv3 1",
#         "max-metric router-lsa on-startup 110",
#         "area 10 nssa default-information-originate metric 10",
#         "address-family ipv4 unicast vrf blue",
#         "adjacency stagger 50 50",
#         "area 25 nssa default-information-originate metric 25 nssa-only",
#         "exit-address-family",
#         "router ospfv3 200",
#         "auto-cost reference-bandwidth 4",
#         "max-metric router-lsa on-startup 100",
#         "address-family ipv4 unicast",
#         "adjacency stagger 200 200",
#         "exit-address-family"
#     ]

# After state:
# -------------
#
# router-ios#sh running-config | section ^router ospfv3
# router ospfv3 1
#  max-metric router-lsa on-startup 110
#  area 10 nssa default-information-originate metric 10
#  !
#  address-family ipv4 unicast vrf blue
#   adjacency stagger 50 50
#   area 25 nssa default-information-originate metric 25 nssa-only
#  exit-address-family
# router ospfv3 200
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  !
#  address-family ipv4 unicast
#   adjacency stagger 200 200
#  exit-address-family

# Using overridden

# Before state:
# -------------
#
# router ospfv3 1
#  max-metric router-lsa on-startup 110
#  area 10 nssa default-information-originate metric 10
#  !
#  address-family ipv4 unicast vrf blue
#   adjacency stagger 50 50
#   area 25 nssa default-information-originate metric 25 nssa-only
#  exit-address-family
# router ospfv3 200
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  !
#  address-family ipv4 unicast
#   adjacency stagger 200 200
#  exit-address-family

- name: Override provided OSPFV3 configuration
  cisco.ios.ios_ospfv3:
    config:
      processes:
        - process_id: 200
          max_metric:
            router_lsa: true
            on_startup:
              time: 200
          address_family:
            - afi: ipv4
              unicast: true
              adjacency:
                min_adjacency: 50
                max_adjacency: 50
              areas:
                - area_id: 200
                  nssa:
                    default_information_originate:
                      metric: 200
                      nssa_only: true
          areas:
            - area_id: "10"
              nssa:
                default_information_originate:
                  metric: 10
    state: overridden

# Commands Fired:
# ---------------
#
# "commands": [
#         "no router ospfv3 1",
#         "router ospfv3 200",
#         "no auto-cost reference-bandwidth 4",
#         "max-metric router-lsa on-startup 200",
#         "area 10 nssa default-information-originate metric 10",
#         "address-family ipv4 unicast",
#         "adjacency stagger 50 50",
#         "area 200 nssa default-information-originate metric 200 nssa-only",
#         "exit-address-family"
#     ]

# After state:
# -------------
#
# router-ios#sh running-config | section ^router ospfv3
# router ospfv3 200
#  max-metric router-lsa on-startup 200
#  area 10 nssa default-information-originate metric 10
#  !
#  address-family ipv4 unicast
#   adjacency stagger 50 50
#   area 200 nssa default-information-originate metric 200 nssa-only
#  exit-address-family

# Using replaced

# Before state:
# -------------
#
# router-ios#sh running-config | section ^router ospfv3
# router ospfv3 1
#  max-metric router-lsa on-startup 110
#  area 10 nssa default-information-originate metric 10
#  !
#  address-family ipv4 unicast vrf blue
#   adjacency stagger 50 50
#   area 25 nssa default-information-originate metric 25 nssa-only
#  exit-address-family
# router ospfv3 200
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  !
#  address-family ipv4 unicast
#   adjacency stagger 200 200
#  exit-address-family

- name: Replaced provided OSPFV3 configuration
  cisco.ios.ios_ospfv3:
    config:
      processes:
        - process_id: 200
          max_metric:
            router_lsa: true
            on_startup:
              time: 200
          address_family:
            - afi: ipv4
              unicast: true
              adjacency:
                min_adjacency: 50
                max_adjacency: 50
              areas:
                - area_id: 200
                  nssa:
                    default_information_originate:
                      metric: 200
                      nssa_only: true
          areas:
            - area_id: "10"
              nssa:
                default_information_originate:
                  metric: 10
    state: replaced

# Commands Fired:
# ---------------
# "commands": [
#         "router ospfv3 200",
#         "no auto-cost reference-bandwidth 4",
#         "max-metric router-lsa on-startup 200",
#         "area 10 nssa default-information-originate metric 10",
#         "address-family ipv4 unicast",
#         "adjacency stagger 50 50",
#         "area 200 nssa default-information-originate metric 200 nssa-only",
#         "exit-address-family"
#     ]

# After state:
# -------------
# router-ios#sh running-config | section ^router ospfv3
# router ospfv3 1
#  max-metric router-lsa on-startup 110
#  area 10 nssa default-information-originate metric 10
#  !
#  address-family ipv4 unicast vrf blue
#   adjacency stagger 50 50
#   area 25 nssa default-information-originate metric 25 nssa-only
#  exit-address-family
# router ospfv3 200
#  max-metric router-lsa on-startup 200
#  area 10 nssa default-information-originate metric 10
#  !
#  address-family ipv4 unicast
#   adjacency stagger 50 50
#   area 200 nssa default-information-originate metric 200 nssa-only
#  exit-address-family

# Using Gathered

# Before state:
# -------------
#
# router-ios#sh running-config | section ^router ospfv3
# router ospfv3 1
#  max-metric router-lsa on-startup 110
#  area 10 nssa default-information-originate metric 10
#  !
#  address-family ipv4 unicast vrf blue
#   adjacency stagger 50 50
#   area 25 nssa default-information-originate metric 25 nssa-only
#  exit-address-family
# router ospfv3 200
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  !
#  address-family ipv4 unicast
#   adjacency stagger 200 200
#  exit-address-family

- name: Gather OSPFV3 provided configurations
  cisco.ios.ios_ospfv3:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": {
#         "processes": [
#             {
#                 "address_family": [
#                     {
#                         "adjacency": {
#                             "max_adjacency": 50,
#                             "min_adjacency": 50
#                         },
#                         "afi": "ipv4",
#                         "areas": [
#                             {
#                                 "area_id": "25",
#                                 "nssa": {
#                                     "default_information_originate": {
#                                         "metric": 25,
#                                         "nssa_only": true
#                                     }
#                                 }
#                             }
#                         ],
#                         "unicast": true,
#                         "vrf": "blue"
#                     }
#                 ],
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "nssa": {
#                             "default_information_originate": {
#                                 "metric": 10
#                             }
#                         }
#                     }
#                 ],
#                 "max_metric": {
#                     "on_startup": {
#                         "time": 110
#                     },
#                     "router_lsa": true
#                 },
#                 "process_id": 1
#             },
#             {
#                 "address_family": [
#                     {
#                         "adjacency": {
#                             "max_adjacency": 200,
#                             "min_adjacency": 200
#                         },
#                         "afi": "ipv4",
#                         "unicast": true
#                     }
#                 ],
#                 "auto_cost": {
#                     "reference_bandwidth": 4
#                 },
#                 "max_metric": {
#                     "on_startup": {
#                         "time": 100
#                     },
#                     "router_lsa": true
#                 },
#                 "process_id": 200
#             }
#         ]
#     }

# After state:
# ------------
#
# router-ios#sh running-config | section ^router ospfv3
# router ospfv3 1
#  max-metric router-lsa on-startup 110
#  area 10 nssa default-information-originate metric 10
#  !
#  address-family ipv4 unicast vrf blue
#   adjacency stagger 50 50
#   area 25 nssa default-information-originate metric 25 nssa-only
#  exit-address-family
# router ospfv3 200
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  !
#  address-family ipv4 unicast
#   adjacency stagger 200 200
#  exit-address-family

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_ospfv3:
    config:
      processes:
      - process_id: 1
        max_metric:
          router_lsa: true
          on_startup:
            time: 110
        address_family:
          - afi: ipv4
            unicast: true
            vrf: blue
            adjacency:
              min_adjacency: 50
              max_adjacency: 50
            areas:
              - area_id: 25
                nssa:
                  default_information_originate:
                    metric: 25
                    nssa_only: true
        areas:
          - area_id: "10"
            nssa:
              default_information_originate:
                metric: 10
        timers:
          throttle:
            lsa:
              first_delay: 12
              min_delay: 14
              max_delay: 16
      - process_id: 200
        address_family:
          - afi: ipv4
            unicast: true
            adjacency:
              min_adjacency: 200
              max_adjacency: 200
        max_metric:
          router_lsa: true
          on_startup:
            time: 100
        auto_cost:
          reference_bandwidth: 4
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "router ospfv3 1",
#         "max-metric router-lsa on-startup 110",
#         "area 10 nssa default-information-originate metric 10",
#         "address-family ipv4 unicast vrf blue",
#         "adjacency stagger 50 50",
#         "area 25 nssa default-information-originate metric 25 nssa-only",
#         "exit-address-family",
#         "router ospfv3 200",
#         "auto-cost reference-bandwidth 4",
#         "max-metric router-lsa on-startup 100",
#         "address-family ipv4 unicast",
#         "adjacency stagger 200 200",
#         "exit-address-family"
#     ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# router ospfv3 1
#  max-metric router-lsa on-startup 110
#  area 10 nssa default-information-originate metric 10
#  !
#  address-family ipv4 unicast vrf blue
#   adjacency stagger 50 50
#   area 25 nssa default-information-originate metric 25 nssa-only
#  exit-address-family
# router ospfv3 200
#  max-metric router-lsa on-startup 100
#  auto-cost reference-bandwidth 4
#  !
#  address-family ipv4 unicast
#   adjacency stagger 200 200
#  exit-address-family

- name: Parse the provided configuration with the existing running configuration
  cisco.ios.ios_ospfv3:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": {
#         "processes": [
#             {
#                 "address_family": [
#                     {
#                         "adjacency": {
#                             "max_adjacency": 50,
#                             "min_adjacency": 50
#                         },
#                         "afi": "ipv4",
#                         "areas": [
#                             {
#                                 "area_id": "25",
#                                 "nssa": {
#                                     "default_information_originate": {
#                                         "metric": 25,
#                                         "nssa_only": true
#                                     }
#                                 }
#                             }
#                         ],
#                         "unicast": true,
#                         "vrf": "blue"
#                     }
#                 ],
#                 "areas": [
#                     {
#                         "area_id": "10",
#                         "nssa": {
#                             "default_information_originate": {
#                                 "metric": 10
#                             }
#                         }
#                     }
#                 ],
#                 "max_metric": {
#                     "on_startup": {
#                         "time": 110
#                     },
#                     "router_lsa": true
#                 },
#                 "process_id": 1
#             }
#         ]
#     }
```

## [Return Values](ios_ospfv3_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["router ospfv3 1", "address-family ipv4 unicast vrf blue", "adjacency stagger 50 50"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
