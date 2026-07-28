---
collection: ansible
version: "8"
title: "cisco.ios.ios_bgp_address_family module – Resource module to configure BGP Address family."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_bgp_address_family_module.html
fetched_at: 2026-07-28T01:26:06+00:00
---
# cisco.ios.ios_bgp_address_family module – Resource module to configure BGP Address family.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/ui/repo/published/cisco/ios/) (version 4.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_bgp_address_family`.

New in cisco.ios 1.2.0

- [Synopsis](ios_bgp_address_family_module.md#synopsis)
- [Parameters](ios_bgp_address_family_module.md#parameters)
- [Notes](ios_bgp_address_family_module.md#notes)
- [Examples](ios_bgp_address_family_module.md#examples)
- [Return Values](ios_bgp_address_family_module.md#return-values)

## [Synopsis](ios_bgp_address_family_module.md#id1)

- This module configures and manages the attributes of bgp address family on Cisco IOS.

## [Parameters](ios_bgp_address_family_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of configurations for bgp address family. |
| **address_family**  list / elements=dictionary | A list of configurations for bgp address family. |
| **afi**  string | Address Family  **Choices:**   - `"ipv4"` - `"ipv6"` - `"l2vpn"` - `"nsap"` - `"rtfilter"` - `"vpnv4"` - `"vpnv6"` |
| **aggregate_addresses**  aliases: aggregate_address  list / elements=dictionary | Configure BGP aggregate entries |
| **address**  string | Aggregate address(A.B.C.D) |
| **advertise_map**  string | Set condition to advertise attribute |
| **as_confed_set**  boolean | Generate AS confed set path information  **Choices:**   - `false` - `true` |
| **as_set**  boolean | Generate AS set path information  **Choices:**   - `false` - `true` |
| **attribute_map**  string | Set attributes of aggregate |
| **netmask**  string | Aggregate mask(A.B.C.D) |
| **summary_only**  boolean | Filter more specific routes from updates  **Choices:**   - `false` - `true` |
| **suppress_map**  string | Conditionally filter more specific routes from updates |
| **auto_summary**  boolean | Enable automatic network number summarization  **Choices:**   - `false` - `true` |
| **bgp**  dictionary | Configure BGP aggregate entries |
| **additional_paths**  dictionary | Additional paths in the BGP table |
| **install**  boolean | Additional paths to install into RIB  **Choices:**   - `false` - `true` |
| **receive**  boolean | Receive additional paths from neighbors  **Choices:**   - `false` - `true` |
| **select**  dictionary | Selection criteria to pick the paths |
| **all**  boolean | Select all available paths  **Choices:**   - `false` - `true` |
| **backup**  boolean | Select backup path  **Choices:**   - `false` - `true` |
| **best**  integer | Select best N paths (2-3). |
| **best_external**  boolean | Select best-external path  **Choices:**   - `false` - `true` |
| **group_best**  boolean | Select group-best path  **Choices:**   - `false` - `true` |
| **send**  boolean | Send additional paths to neighbors  **Choices:**   - `false` - `true` |
| **aggregate_timer**  integer | Configure Aggregation Timer  Please refer vendor documentation for valid values |
| **dampening**  dictionary | Enable route-flap dampening |
| **max_suppress**  integer | Maximum duration to suppress a stable route  Please refer vendor documentation for valid values |
| **penalty_half_time**  integer | Half-life time for the penalty  Please refer vendor documentation for valid values |
| **reuse_route_val**  integer | Value to start reusing a route  Please refer vendor documentation for valid values |
| **route_map**  string | Route-map to specify criteria for dampening |
| **suppress_route_val**  integer | Value to start suppressing a route  Please refer vendor documentation for valid values |
| **dmzlink_bw**  boolean | Use DMZ Link Bandwidth as weight for BGP multipaths  **Choices:**   - `false` - `true` |
| **nexthop**  dictionary | Nexthop tracking commands |
| **route_map**  string | Route map for valid nexthops |
| **trigger**  dictionary | Nexthop triggering |
| **delay**  integer | Set the delay to tigger nexthop tracking  Please refer vendor documentation for valid values |
| **enable**  boolean | Enable nexthop tracking  **Choices:**   - `false` - `true` |
| **redistribute_internal**  boolean | Allow redistribution of iBGP into IGPs (dangerous)  **Choices:**   - `false` - `true` |
| **route_map**  boolean | route-map control commands  Have route-map set commands take priority over BGP commands such as next-hop unchanged  **Choices:**   - `false` - `true` |
| **scan_time**  integer | Configure background scanner interval  Please refer vendor documentation for valid values |
| **slow_peer**  list / elements=dictionary | Nexthop triggering  This option is DEPRECATED and replaced with slow_peer_options, this attribute will be removed after 2025-01-01. |
| **detection**  dictionary | Slow-peer detection |
| **enable**  boolean | Enable slow-peer detection  **Choices:**   - `false` - `true` |
| **threshold**  integer | Set the slow-peer detection threshold  Threshold value (seconds)  Please refer vendor documentation for valid values |
| **split_update_group**  dictionary | Configure slow-peer split-update-group |
| **dynamic**  boolean | Dynamically split the slow peer to slow-update group  **Choices:**   - `false` - `true` |
| **permanent**  boolean | Keep the slow-peer permanently in slow-update group  **Choices:**   - `false` - `true` |
| **slow_peer_options**  dictionary | Nexthop triggering |
| **detection**  dictionary | Slow-peer detection |
| **enable**  boolean | Enable slow-peer detection  **Choices:**   - `false` - `true` |
| **threshold**  integer | Set the slow-peer detection threshold  Threshold value (seconds)  Please refer vendor documentation for valid values |
| **split_update_group**  dictionary | Configure slow-peer split-update-group |
| **dynamic**  boolean | Dynamically split the slow peer to slow-update group  **Choices:**   - `false` - `true` |
| **permanent**  boolean | Keep the slow-peer permanently in slow-update group  **Choices:**   - `false` - `true` |
| **soft_reconfig_backup**  boolean | Use soft-reconfiguration inbound only when route-refresh is not negotiated  **Choices:**   - `false` - `true` |
| **update_group**  boolean | Manage peers in bgp update groups  Split update groups based on Policy  Keep peers with as-override in different update groups  **Choices:**   - `false` - `true` |
| **default**  boolean | Set a command to its defaults  **Choices:**   - `false` - `true` |
| **default_information**  boolean | Distribution of default information  Distribute default route  **Choices:**   - `false` - `true` |
| **default_metric**  integer | Set metric of redistributed routes |
| **distance**  dictionary | Define an administrative distance |
| **external**  integer | Distance for routes external to the AS |
| **internal**  integer | Distance for routes internal to the AS |
| **local**  integer | Distance for local routes |
| **neighbors**  aliases: neighbor  list / elements=dictionary | Specify a neighbor router |
| **activate**  boolean | Enable the Address Family for this Neighbor  **Choices:**   - `false` - `true` |
| **additional_paths**  dictionary | Negotiate additional paths capabilities with this neighbor |
| **disable**  boolean | Disable additional paths for this neighbor  **Choices:**   - `false` - `true` |
| **receive**  boolean | Receive additional paths from neighbors  **Choices:**   - `false` - `true` |
| **send**  boolean | Send additional paths to this neighbor  **Choices:**   - `false` - `true` |
| **address**  string | Neighbor address (A.B.C.D)  This option is DEPRECATED and replaced with neighbor_address, this attribute will be removed after 2025-01-01. |
| **advertise**  dictionary | Advertise to this neighbor  Advertise additional paths |
| **all**  boolean | Select all available paths  **Choices:**   - `false` - `true` |
| **best**  integer | Select best N paths (2-3). |
| **group_best**  boolean | Select group-best path  **Choices:**   - `false` - `true` |
| **advertise_map**  dictionary | specify route-map for conditional advertisement |
| **exist_map**  string | advertise prefix only if prefix is in the condition exists  condition route-map name |
| **name**  string | advertise route-map name |
| **non_exist_map**  string | advertise prefix only if prefix in the condition does not exist  condition route-map name |
| **advertisement_interval**  integer | Minimum interval between sending BGP routing updates |
| **advertises**  dictionary | Advertise to this neighbor |
| **additional_paths**  dictionary | Advertise additional paths |
| **all**  boolean | Select all available paths  **Choices:**   - `false` - `true` |
| **best**  integer | Select best N paths (2-3). |
| **group_best**  boolean | Select group-best path  **Choices:**   - `false` - `true` |
| **best_external**  boolean | Advertise best-external (at RRs best-internal) path  **Choices:**   - `false` - `true` |
| **diverse_path**  dictionary | Advertise additional paths |
| **backup**  boolean | Diverse path can be backup path  **Choices:**   - `false` - `true` |
| **mpath**  boolean | Diverse path can be multipath  **Choices:**   - `false` - `true` |
| **aigp**  dictionary | Enable a AIGP on neighbor |
| **enable**  string | Enable a AIGP on neighbor |
| **send**  dictionary | Cost community or MED carrying AIGP VALUE |
| **cost_community**  dictionary | Cost extended community carrying AIGP Value |
| **id**  integer | Community ID  Please refer vendor documentation for valid values |
| **poi**  dictionary | Point of Insertion |
| **igp_cost**  boolean | Point of Insertion After IGP  **Choices:**   - `false` - `true` |
| **pre_bestpath**  boolean | Point of Insertion At Beginning  **Choices:**   - `false` - `true` |
| **transitive**  boolean | Cost community is Transitive  **Choices:**   - `false` - `true` |
| **med**  boolean | Med carrying AIGP Value  **Choices:**   - `false` - `true` |
| **allow_policy**  boolean | Enable the policy support for this IBGP Neighbor  **Choices:**   - `false` - `true` |
| **allowas_in**  integer | Accept as-path with my AS present in it  Please refer vendor documentation for valid values |
| **as_override**  dictionary | Override matching AS-number while sending update |
| **set**  boolean | Enable AS override  **Choices:**   - `false` - `true` |
| **split_horizon**  boolean | Maintain Split Horizon while sending update  **Choices:**   - `false` - `true` |
| **bmp_activate**  dictionary | Activate the BMP monitoring for a BGP peer |
| **all**  boolean | Activate BMP monitoring for all servers  **Choices:**   - `false` - `true` |
| **server**  integer | Activate BMP for server  BMP Server Number  Please refer vendor documentation for valid values |
| **capability**  dictionary | Advertise capability to the peer  Advertise ORF capability to the peer  Advertise prefixlist ORF capability to this neighbor |
| **both**  boolean | Capability to SEND and RECEIVE the ORF to/from this neighbor  **Choices:**   - `false` - `true` |
| **receive**  boolean | Capability to RECEIVE the ORF from this neighbor  **Choices:**   - `false` - `true` |
| **send**  boolean | Capability to SEND the ORF to this neighbor  **Choices:**   - `false` - `true` |
| **cluster_id**  string | Configure Route-Reflector Cluster-id (peers may reset)  Route-Reflector Cluster-id as 32 bit quantity, or Route-Reflector Cluster-id in IP address format (A.B.C.D) |
| **default_originate**  dictionary | Originate default route to this neighbor |
| **route_map**  string | Route-map to specify criteria to originate default |
| **set**  boolean | Set default route to this neighbor  **Choices:**   - `false` - `true` |
| **description**  string | Neighbor specific description |
| **disable_connected_check**  boolean | one-hop away EBGP peer using loopback address  **Choices:**   - `false` - `true` |
| **distribute_list**  dictionary | Filter updates to/from this neighbor |
| **acl**  string | ACL id/name |
| **in**  boolean | Filter incoming updates  **Choices:**   - `false` - `true` |
| **out**  boolean | Filter outgoing updates  **Choices:**   - `false` - `true` |
| **dmzlink_bw**  boolean | Propagate the DMZ link bandwidth  **Choices:**   - `false` - `true` |
| **ebgp_multihop**  dictionary | Allow EBGP neighbors not on directly connected networks |
| **enable**  boolean | Allow EBGP neighbors not on directly connected networks  **Choices:**   - `false` - `true` |
| **hop_count**  integer | Maximum hop count  Please refer vendor documentation for valid values |
| **fall_over**  dictionary | Session fall on peer route lost |
| **bfd**  dictionary | Use BFD to detect failure |
| **multi_hop**  boolean | Force BFD multi-hop to detect failure  **Choices:**   - `false` - `true` |
| **set**  boolean | set bfd  **Choices:**   - `false` - `true` |
| **single_hop**  boolean | Force BFD single-hop to detect failure  **Choices:**   - `false` - `true` |
| **route_map**  string | Route map for peer route |
| **filter_list**  dictionary | Establish BGP filters |
| **as_path_acl**  integer | AS path access list  Please refer vendor documentation for valid values |
| **in**  boolean | Filter incoming updates  **Choices:**   - `false` - `true` |
| **out**  boolean | Filter outgoing updates  **Choices:**   - `false` - `true` |
| **ha_mode**  dictionary | high availability mode |
| **disable**  boolean | disable graceful-restart  **Choices:**   - `false` - `true` |
| **set**  boolean | set ha-mode and graceful-restart for this peer  **Choices:**   - `false` - `true` |
| **inherit**  string | Inherit a template  Inherit a peer-policy template |
| **internal_vpn_client**  boolean | Stack iBGP-CE Neighbor Path in ATTR_SET for vpn update  **Choices:**   - `false` - `true` |
| **ipv6_address**  aliases: ipv6_adddress  string | Neighbor ipv6 address (X:X:X:X::X)  This option is DEPRECATED and replaced with neighbor_address, this attribute will be removed after 2025-01-01. |
| **local_as**  dictionary | Specify a local-as number |
| **dual_as**  boolean | Accept either real AS or local AS from the ebgp peer  **Choices:**   - `false` - `true` |
| **no_prepend**  dictionary | Do not prepend local-as to updates from ebgp peers |
| **replace_as**  boolean | Replace real AS with local AS in the EBGP updates  **Choices:**   - `false` - `true` |
| **set**  boolean | Set prepend  **Choices:**   - `false` - `true` |
| **number**  integer | AS number used as local AS  Please refer vendor documentation for valid values |
| **set**  boolean | set local-as number  **Choices:**   - `false` - `true` |
| **log_neighbor_changes**  dictionary | Log neighbor up/down and reset reason |
| **disable**  boolean | disable Log neighbor up/down and reset  **Choices:**   - `false` - `true` |
| **set**  boolean | set Log neighbor up/down and reset  **Choices:**   - `false` - `true` |
| **maximum_prefix**  dictionary | Establish BGP filters |
| **number**  integer | maximum no. of prefix limit  Please refer vendor documentation for valid values |
| **restart**  integer | Restart bgp connection after limit is exceeded |
| **threshold_value**  integer | Threshold value (%) at which to generate a warning msg  Please refer vendor documentation for valid values |
| **warning_only**  boolean | Only give warning message when limit is exceeded  **Choices:**   - `false` - `true` |
| **neighbor_address**  string | Neighbor address (A.B.C.D)  Neighbor tag  Neighbor ipv6 address (X:X:X:X::X) |
| **next_hop_self**  boolean | Disable the next hop calculation for this neighbor  This option is DEPRECATED and is replaced with nexthop_self which accepts dict as input this attribute will be removed after 2023-06-01.  **Choices:**   - `false` - `true` |
| **next_hop_unchanged**  dictionary | Propagate next hop unchanged for iBGP paths to this neighbor  Propagate next hop unchanged for all paths (iBGP and eBGP) to this neighbor |
| **allpaths**  boolean | Propagate next hop unchanged for all paths (iBGP and eBGP) to this neighbor  **Choices:**   - `false` - `true` |
| **set**  boolean | Enable next-hop-unchanged  **Choices:**   - `false` - `true` |
| **nexthop_self**  dictionary | Disable the next hop calculation for this neighbor |
| **all**  boolean | Enable next-hop-self for both eBGP and iBGP received paths  **Choices:**   - `false` - `true` |
| **set**  boolean | set the next hop self  **Choices:**   - `false` - `true` |
| **password**  string | Set a password  This option is DEPRECATED and is replaced with password_options which accepts dict as input, this attribute will be removed after 2024-06-01. |
| **password_options**  dictionary | Set a password with encryption type |
| **encryption**  integer | Encryption type (0 to disable encryption, 7 for proprietary) |
| **pass_key**  string | The password |
| **path_attribute**  dictionary | BGP optional attribute filtering |
| **discard**  dictionary | Discard matching path-attribute for this neighbor |
| **in**  boolean | Perform inbound path-attribute filtering  **Choices:**   - `false` - `true` |
| **range**  dictionary | path attribute range |
| **end**  integer | path attribute range end value  Please refer vendor documentation for valid values |
| **start**  integer | path attribute range start value  Please refer vendor documentation for valid values |
| **type**  integer | path attribute type  Please refer vendor documentation for valid values |
| **treat_as_withdraw**  dictionary | Treat-as-withdraw matching path-attribute for this neighbor |
| **in**  boolean | Perform inbound path-attribute filtering  **Choices:**   - `false` - `true` |
| **range**  dictionary | path attribute range |
| **end**  integer | path attribute range end value  Please refer vendor documentation for valid values |
| **start**  integer | path attribute range start value  Please refer vendor documentation for valid values |
| **type**  integer | path attribute type  Please refer vendor documentation for valid values |
| **peer_group**  boolean | Member of the peer-group  **Choices:**   - `false` - `true` |
| **peer_group_name**  string | Member of the peer-group |
| **prefix_list**  dictionary | Filter updates to/from this neighbor  This option is DEPRECATED and is replaced with prefix_lists which accepts list of dict as input |
| **in**  boolean | Filter incoming updates  **Choices:**   - `false` - `true` |
| **name**  string | Name of a prefix list |
| **out**  boolean | Filter outgoing updates  **Choices:**   - `false` - `true` |
| **prefix_lists**  list / elements=dictionary | Filter updates to/from this neighbor |
| **in**  boolean | Filter incoming updates  **Choices:**   - `false` - `true` |
| **name**  string | Name of a prefix list |
| **out**  boolean | Filter outgoing updates  **Choices:**   - `false` - `true` |
| **remote_as**  integer | Specify a BGP neighbor  AS of remote neighbor |
| **remove_private_as**  dictionary | Remove private AS number from outbound updates |
| **all**  boolean | Remove all private AS numbers  **Choices:**   - `false` - `true` |
| **replace_as**  boolean | Replace all private AS numbers with local AS  **Choices:**   - `false` - `true` |
| **set**  boolean | Remove private AS number from outbound updates  **Choices:**   - `false` - `true` |
| **route_map**  dictionary | Apply route map to neighbor  This option is DEPRECATED and is replaced with route_maps which accepts list of dict as input |
| **in**  boolean | Apply map to incoming routes  **Choices:**   - `false` - `true` |
| **name**  string | Name of route map |
| **out**  boolean | Apply map to outbound routes  **Choices:**   - `false` - `true` |
| **route_maps**  list / elements=dictionary | Apply route map to neighbor |
| **in**  boolean | Apply map to incoming routes  **Choices:**   - `false` - `true` |
| **name**  string | Name of route map |
| **out**  boolean | Apply map to outbound routes  **Choices:**   - `false` - `true` |
| **route_reflector_client**  boolean | Configure a neighbor as Route Reflector client  **Choices:**   - `false` - `true` |
| **route_server_client**  boolean | Configure a neighbor as Route Server client  **Choices:**   - `false` - `true` |
| **send_community**  dictionary | Send Community attribute to this neighbor |
| **both**  boolean | Send Standard and Extended Community attributes  **Choices:**   - `false` - `true` |
| **extended**  boolean | Send Extended Community attribute  **Choices:**   - `false` - `true` |
| **set**  boolean | Send Standard Community attribute.  Maintains backwards compatibility for configurations that do not specify a send-community type.  **Choices:**   - `false` - `true` |
| **standard**  boolean | Send Standard Community attribute  **Choices:**   - `false` - `true` |
| **shutdown**  dictionary | Administratively shut down this neighbor |
| **graceful**  integer | Gracefully shut down this neighbor  time in seconds  Please refer vendor documentation for valid values |
| **set**  boolean | shut down  **Choices:**   - `false` - `true` |
| **slow_peer**  list / elements=dictionary | Configure slow-peer  This option is DEPRECATED and replaced with slow_peer_options, this attribute will be removed after 2025-01-01. |
| **detection**  dictionary | Configure slow-peer |
| **disable**  boolean | Disable slow-peer detection  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable slow-peer detection  **Choices:**   - `false` - `true` |
| **threshold**  integer | Set the slow-peer detection threshold |
| **split_update_group**  dictionary | Configure slow-peer |
| **dynamic**  dictionary | Configure slow-peer |
| **disable**  boolean | Configure slow-peer  **Choices:**   - `false` - `true` |
| **enable**  boolean | Configure slow-peer  **Choices:**   - `false` - `true` |
| **permanent**  boolean | Configure slow-peer  **Choices:**   - `false` - `true` |
| **static**  boolean | Configure slow-peer  **Choices:**   - `false` - `true` |
| **slow_peer_options**  dictionary | Configure slow-peer options |
| **detection**  dictionary | Configure slow-peer |
| **disable**  boolean | Disable slow-peer detection  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable slow-peer detection  **Choices:**   - `false` - `true` |
| **threshold**  integer | Set the slow-peer detection threshold |
| **split_update_group**  dictionary | Configure slow-peer |
| **dynamic**  dictionary | Configure slow-peer |
| **disable**  boolean | Configure slow-peer  **Choices:**   - `false` - `true` |
| **enable**  boolean | Configure slow-peer  **Choices:**   - `false` - `true` |
| **permanent**  boolean | Configure slow-peer  **Choices:**   - `false` - `true` |
| **static**  boolean | Configure slow-peer  **Choices:**   - `false` - `true` |
| **soft_reconfiguration**  boolean | Per neighbor soft reconfiguration  Allow inbound soft reconfiguration for this neighbor  **Choices:**   - `false` - `true` |
| **soo**  string | Site-of-Origin extended community |
| **tag**  string | Neighbor tag  This option is DEPRECATED and replaced with neighbor_address, this attribute will be removed after 2025-01-01. |
| **timers**  dictionary | BGP per neighbor timers |
| **holdtime**  integer | Holdtime |
| **interval**  integer | Keepalive interval |
| **min_holdtime**  integer | Minimum hold time from neighbor |
| **transport**  dictionary | Transport options |
| **connection_mode**  dictionary | Specify passive or active connection |
| **active**  boolean | Actively establish the TCP session  **Choices:**   - `false` - `true` |
| **passive**  boolean | Passively establish the TCP session  **Choices:**   - `false` - `true` |
| **multi_session**  boolean | Use Multi-session for transport  **Choices:**   - `false` - `true` |
| **path_mtu_discovery**  dictionary | Use transport path MTU discovery |
| **disable**  boolean | disable  **Choices:**   - `false` - `true` |
| **set**  boolean | Use path MTU discovery  **Choices:**   - `false` - `true` |
| **ttl_security**  integer | BGP ttl security check  maximum number of hops  Please refer vendor documentation for valid values |
| **unsuppress_map**  string | Route-map to selectively unsuppress suppressed routes |
| **version**  integer | Set the BGP version to match a neighbor  Neighbor’s BGP version  Please refer vendor documentation for valid values |
| **weight**  integer | Set default weight for routes from this neighbor |
| **networks**  aliases: network  list / elements=dictionary | Specify a network to announce via BGP |
| **address**  string | Network number (A.B.C.D) |
| **backdoor**  boolean | Specify a BGP backdoor route  **Choices:**   - `false` - `true` |
| **evpn**  boolean | Advertise or Export to EVPN address-family  **Choices:**   - `false` - `true` |
| **mask**  string | Network mask (A.B.C.D) |
| **route_map**  string | Route-map to modify the attributes |
| **redistribute**  list / elements=dictionary | Redistribute information from another routing protocol |
| **application**  dictionary | Application |
| **metric**  integer | Metric for redistributed routes |
| **name**  string | Application name |
| **route_map**  string | Route map reference |
| **bgp**  dictionary | Border Gateway Protocol (BGP) |
| **as_number**  string | Autonomous system number |
| **metric**  integer | Metric for redistributed routes |
| **route_map**  string | Route map reference |
| **connected**  dictionary | Connected |
| **metric**  integer | Metric for redistributed routes |
| **route_map**  string | Route map reference |
| **set**  boolean | Redistribute automatically established IP connected routes.  This only needs to be set if metric or route_map aren’t used.  **Choices:**   - `false` - `true` |
| **eigrp**  dictionary | Enhanced Interior Gateway Routing Protocol (EIGRP) |
| **as_number**  string | Autonomous system number |
| **metric**  integer | Metric for redistributed routes |
| **route_map**  string | Route map reference |
| **isis**  dictionary | ISO IS-IS |
| **area_tag**  string | ISO routing area tag |
| **clns**  boolean | Redistribution of OSI dynamic routes  **Choices:**   - `false` - `true` |
| **ip**  boolean | Redistribution of IP dynamic routes  **Choices:**   - `false` - `true` |
| **metric**  integer | Metric for redistributed routes |
| **route_map**  string | Route map reference |
| **iso_igrp**  dictionary | IGRP for OSI networks |
| **area_tag**  string | ISO routing area tag |
| **route_map**  string | Route map reference |
| **lisp**  dictionary | Locator ID Separation Protocol (LISP) |
| **metric**  integer | Metric for redistributed routes |
| **route_map**  string | Route map reference |
| **set**  boolean | Set the top level attribute  **Choices:**   - `false` - `true` |
| **mobile**  dictionary | Mobile routes |
| **metric**  integer | Metric for redistributed routes |
| **route_map**  string | Route map reference |
| **set**  boolean | Set the top level attribute  **Choices:**   - `false` - `true` |
| **odr**  dictionary | On Demand stub Routes |
| **metric**  integer | Metric for redistributed routes |
| **route_map**  string | Route map reference |
| **set**  boolean | Set the top level attribute  **Choices:**   - `false` - `true` |
| **ospf**  dictionary | Open Shortest Path First (OSPF) |
| **include_connected**  boolean | Include connected. Only applicable under IPv6 AFI  **Choices:**   - `false` - `true` |
| **match**  dictionary | Redistribute matched routes |
| **external**  boolean | Redistribute OSPF external routes  This option is DEPRECATED and replaced with externals option, this attribute will be removed after 2025-01-01.  **Choices:**   - `false` - `true` |
| **externals**  dictionary | Redistribute OSPF external routes |
| **type_1**  boolean | Redistribute OSPF External type 1 routes  **Choices:**   - `false` - `true` |
| **type_2**  boolean | Redistribute OSPF External type 1 routes  **Choices:**   - `false` - `true` |
| **internal**  boolean | Redistribute OSPF internal routes  **Choices:**   - `false` - `true` |
| **nssa_external**  boolean | Redistribute OSPF NSSA external routes  This option is DEPRECATED and replaced with nssa_externals option, this attribute will be removed after 2025-01-01.  **Choices:**   - `false` - `true` |
| **nssa_externals**  dictionary | Redistribute OSPF NSSA external routes |
| **type_1**  boolean | Redistribute NSSA external type 1 routes  **Choices:**   - `false` - `true` |
| **type_2**  boolean | Redistribute NSSA external type 2 routes  **Choices:**   - `false` - `true` |
| **type_1**  boolean | Redistribute NSSA external type 1 routes  This option is DEPRECATED and replaced with nssa_externals.type_1 option, this attribute will be removed after 2025-01-01.  **Choices:**   - `false` - `true` |
| **type_2**  boolean | Redistribute NSSA external type 2 routes  This option is DEPRECATED and replaced with nssa_externals.type_2 option, this attribute will be removed after 2025-01-01.  **Choices:**   - `false` - `true` |
| **metric**  integer | Metric for redistributed routes |
| **process_id**  integer | Process ID |
| **route_map**  string | Route map reference |
| **vrf**  string | VPN Routing/Forwarding Instance |
| **ospfv3**  dictionary | OSPFv3 |
| **match**  dictionary | Redistribute matched routes |
| **external**  boolean | Redistribute OSPF external routes  This option is DEPRECATED and replaced with externals, this attribute will be removed after 2025-01-01.  **Choices:**   - `false` - `true` |
| **externals**  dictionary | Redistribute OSPF external routes |
| **type_1**  boolean | Redistribute OSPF External type 1 routes  **Choices:**   - `false` - `true` |
| **type_2**  boolean | Redistribute OSPF External type 1 routes  **Choices:**   - `false` - `true` |
| **internal**  boolean | Redistribute OSPF internal routes  **Choices:**   - `false` - `true` |
| **nssa_external**  boolean | Redistribute OSPF internal routes  This option is DEPRECATED and replaced with nssa_externals, this attribute will be removed after 2025-01-01.  **Choices:**   - `false` - `true` |
| **nssa_externals**  dictionary | Redistribute OSPF NSSA external routes |
| **type_1**  boolean | Redistribute NSSA external type 1 routes  **Choices:**   - `false` - `true` |
| **type_2**  boolean | Redistribute NSSA external type 2 routes  **Choices:**   - `false` - `true` |
| **type_1**  boolean | Redistribute NSSA external type 1 routes  This option is DEPRECATED and replaced with nssa_externals.type_1 option, this attribute will be removed after 2025-01-01.  **Choices:**   - `false` - `true` |
| **type_2**  boolean | Redistribute NSSA external type 2 routes  This option is DEPRECATED and replaced with nssa_externals.type_2 option, this attribute will be removed after 2025-01-01.  **Choices:**   - `false` - `true` |
| **metric**  integer | Metric for redistributed routes |
| **process_id**  integer | Process ID |
| **route_map**  string | Route map reference |
| **rip**  dictionary | Routing Information Protocol (RIP) |
| **metric**  integer | Metric for redistributed routes |
| **route_map**  string | Route map reference |
| **set**  boolean | Set the top level attribute  **Choices:**   - `false` - `true` |
| **static**  dictionary | Static routes |
| **clns**  boolean | Redistribution of OSI static routes  **Choices:**   - `false` - `true` |
| **ip**  boolean | Redistribution of IP static routes  **Choices:**   - `false` - `true` |
| **metric**  integer | Metric for redistributed routes |
| **route_map**  string | Route map reference |
| **set**  boolean | Set the top level attribute  **Choices:**   - `false` - `true` |
| **vrf**  dictionary | Specify a source VRF |
| **global**  boolean | global VRF  **Choices:**   - `false` - `true` |
| **name**  string | Source VRF name |
| **safi**  string | Address Family modifier  **Choices:**   - `"flowspec"` - `"mdt"` - `"multicast"` - `"mvpn"` - `"evpn"` - `"unicast"` |
| **snmp**  dictionary | Modify snmp parameters |
| **context**  dictionary | Configure a SNMP context  Context Name |
| **community**  dictionary | Configure a SNMP v2c Community string and access privs |
| **acl**  string | Standard IP accesslist allowing access with this community string  Expanded IP accesslist allowing access with this community string  Access-list name |
| **ipv6**  string | Specify IPv6 Named Access-List  IPv6 Access-list name |
| **ro**  boolean | Read-only access with this community string  **Choices:**   - `false` - `true` |
| **rw**  boolean | Read-write access with this community string  **Choices:**   - `false` - `true` |
| **snmp_community**  string | SNMP community string |
| **name**  string | Context Name |
| **user**  dictionary | Configure a SNMP v3 user |
| **access**  dictionary | specify an access-list associated with this group |
| **acl**  string | SNMP community string |
| **ipv6**  string | Specify IPv6 Named Access-List  IPv6 Access-list name |
| **auth**  dictionary | authentication parameters for the user |
| **md5**  string | Use HMAC MD5 algorithm for authentication  authentication password for user |
| **sha**  string | Use HMAC SHA algorithm for authentication  authentication password for user |
| **credential**  boolean | If the user password is already configured and saved  **Choices:**   - `false` - `true` |
| **encrypted**  boolean | specifying passwords as MD5 or SHA digests  **Choices:**   - `false` - `true` |
| **name**  string | SNMP community string |
| **priv**  dictionary | encryption parameters for the user |
| **aes128**  string | Use 128 bit AES algorithm for encryption |
| **aes192**  string | Use 192 bit 3DES algorithm for encryption |
| **aes256**  string | Use 256 bit DES algorithm for encryption |
| **des**  string | Use 56 bit DES algorithm for encryption |
| **des56**  string | Use 56 bit DES algorithm for encryption |
| **table_map**  dictionary | Map external entry attributes into routing table |
| **filter**  boolean | Selective route download  **Choices:**   - `false` - `true` |
| **name**  string | route-map name |
| **vrf**  string | Specify parameters for a VPN Routing/Forwarding instance |
| **as_number**  string | Autonomous system number. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **sh running-config | section ^router bgp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](ios_bgp_address_family_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - The module examples uses callback plugin (stdout_callback = yaml) to generate task output in yaml format.

## [Examples](ios_bgp_address_family_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp nopeerup-delay cold-boot 20

- name: Merge provided configuration with device configuration
  cisco.ios.ios_bgp_address_family:
    config:
      as_number: 65000
      address_family:
        - afi: ipv4
          safi: multicast
          vrf: blue
          aggregate_address:
            - address: 192.0.2.1
              netmask: 255.255.255.255
              as_confed_set: true
          bgp:
            aggregate_timer: 10
            dampening:
              penalty_half_time: 1
              reuse_route_val: 1
              suppress_route_val: 1
              max_suppress: 1
            slow_peer:
              - detection:
                  threshold: 150
          neighbor:
            - address: 198.51.100.1
              aigp:
                send:
                  cost_community:
                    id: 100
                    poi:
                      igp_cost: true
                      transitive: true
              slow_peer:
                - detection:
                    threshold: 150
              remote_as: 10
              route_map:
                - name: test-route-out
                  out: true
                - name: test-route-in
                  in: true
              route_server_client: true
          network:
            - address: 198.51.110.10
              mask: 255.255.255.255
              backdoor: true
          snmp:
            context:
              name: snmp_con
              community:
                snmp_community: community
                ro: true
                acl: 10
        - afi: ipv4
          safi: mdt
          bgp:
            dmzlink_bw: true
            dampening:
              penalty_half_time: 1
              reuse_route_val: 10
              suppress_route_val: 100
              max_suppress: 5
            soft_reconfig_backup: true
        - afi: ipv4
          safi: multicast
          aggregate_address:
            - address: 192.0.3.1
              netmask: 255.255.255.255
              as_confed_set: true
          default_metric: 12
          distance:
            external: 10
            internal: 10
            local: 100
          network:
            - address: 198.51.111.11
              mask: 255.255.255.255
              route_map: test
          table_map:
            name: test_tableMap
            filter: true
    state: merged

# Task Output:
# ------------
#
# before: {}
# commands:
#   - router bgp 65000
#   - address-family ipv4 multicast vrf blue
#   - bgp aggregate-timer 10
#   - bgp dampening 1 1 1 1
#   - bgp slow-peer detection threshold 150
#   - snmp context snmp_con community community ro 10
#   - neighbor 198.51.100.1 remote-as 10
#   - neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive
#   - neighbor 198.51.100.1 slow-peer detection threshold 150
#   - network 198.51.110.10 mask 255.255.255.255 backdoor
#   - aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
#   - address-family ipv4 multicast
#   - default-metric 12
#   - distance bgp 10 10 100
#   - table-map test_tableMap filter
#   - network 198.51.111.11 mask 255.255.255.255 route-map test
#   - aggregate-address 192.0.3.1 255.255.255.255 as-confed-set
#   - address-family ipv4 mdt
#   - bgp dmzlink-bw
#   - bgp soft-reconfig-backup
#   - bgp dampening 1 10 100 5
# after:
#   address_family:
#   - afi: ipv4
#     aggregate_addresses:
#     - address: 192.0.2.1
#       as_confed_set: true
#       netmask: 255.255.255.255
#     bgp:
#       aggregate_timer: 10
#       dampening:
#         max_suppress: 1
#         penalty_half_time: 1
#         reuse_route_val: 1
#         suppress_route_val: 1
#       slow_peer_options:
#         detection:
#           threshold: 150
#     neighbors:
#     - activate: true
#       aigp:
#         send:
#           cost_community:
#             id: 100
#             poi:
#               igp_cost: true
#               transitive: true
#       neighbor_address: 198.51.100.1
#       slow_peer_options:
#         detection:
#           threshold: 150
#     networks:
#     - address: 198.51.110.10
#       backdoor: true
#       mask: 255.255.255.255
#     snmp:
#       context:
#         community:
#           acl: '10'
#           ro: true
#           snmp_community: community
#         name: snmp_con
#   - afi: ipv4
#     aggregate_addresses:
#     - address: 192.0.3.1
#       as_confed_set: true
#       netmask: 255.255.255.255
#     default_metric: 12
#     distance:
#       external: 10
#       internal: 10
#       local: 100
#     networks:
#     - address: 198.51.111.11
#       mask: 255.255.255.255
#       route_map: test
#     safi: multicast
#     table_map:
#       filter: true
#       name: test_tableMap
#   - afi: ipv4
#     bgp:
#       dampening:
#         max_suppress: 5
#         penalty_half_time: 1
#         reuse_route_val: 10
#         suppress_route_val: 100
#       dmzlink_bw: true
#       soft_reconfig_backup: true
#     safi: mdt
#   as_number: '65000'

# After state:
# ------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  snmp context snmp_con community community RO 10
#  neighbor 198.51.100.1 remote-as 10
#  !
#  address-family ipv4
#   snmp context snmp_con community community RO 10
#   bgp aggregate-timer 10
#   bgp slow-peer detection threshold 150
#   bgp dampening 1 1 1 1
#   network 198.51.110.10 mask 255.255.255.255 backdoor
#   aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
#   neighbor 198.51.100.1 activate
#   neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive
#   neighbor 198.51.100.1 slow-peer detection threshold 150
#  exit-address-family
#  !
#  address-family ipv4 multicast
#   table-map test_tableMap filter
#   network 198.51.111.11 mask 255.255.255.255 route-map test
#   aggregate-address 192.0.3.1 255.255.255.255 as-confed-set
#   default-metric 12
#   distance bgp 10 10 100
#  exit-address-family
#  !
#  address-family ipv4 mdt
#   bgp dampening 1 10 100 5
#   bgp dmzlink-bw
#   bgp soft-reconfig-backup
#  exit-address-family

# Using replaced

# Before state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  snmp context snmp_con community community RO 10
#  neighbor 198.51.100.1 remote-as 10
#  !
#  address-family ipv4
#   snmp context snmp_con community community RO 10
#   bgp aggregate-timer 10
#   bgp slow-peer detection threshold 150
#   bgp dampening 1 1 1 1
#   network 198.51.110.10 mask 255.255.255.255 backdoor
#   aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
#   neighbor 198.51.100.1 activate
#   neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive
#   neighbor 198.51.100.1 slow-peer detection threshold 150
#  exit-address-family
#  !
#  address-family ipv4 multicast
#   table-map test_tableMap filter
#   network 198.51.111.11 mask 255.255.255.255 route-map test
#   aggregate-address 192.0.3.1 255.255.255.255 as-confed-set
#   default-metric 12
#   distance bgp 10 10 100
#  exit-address-family
#  !
#  address-family ipv4 mdt
#   bgp dampening 1 10 100 5
#   bgp dmzlink-bw
#   bgp soft-reconfig-backup
#  exit-address-family

- name: Replaces device configuration of listed AF BGP with provided configuration
  cisco.ios.ios_bgp_address_family:
    config:
      as_number: 65000
      address_family:
        - afi: ipv4
          safi: multicast
          vrf: blue
          aggregate_address:
            - address: 192.0.2.1
              netmask: 255.255.255.255
              as_confed_set: true
          bgp:
            aggregate_timer: 10
            dampening:
              penalty_half_time: 1
              reuse_route_val: 1
              suppress_route_val: 1
              max_suppress: 1
            slow_peer:
              - detection:
                  threshold: 150
          neighbor:
            - address: 198.51.110.1
              activate: true
              aigp:
                send:
                  cost_community:
                    id: 200
                    poi:
                      igp_cost: true
                      transitive: true
              slow_peer:
                - detection:
                    threshold: 150
              remote_as: 10
          network:
            - address: 198.51.110.10
              mask: 255.255.255.255
              backdoor: true
        - afi: ipv4
          safi: multicast
          bgp:
            aggregate_timer: 10
            dampening:
              penalty_half_time: 10
              reuse_route_val: 10
              suppress_route_val: 10
              max_suppress: 10
            slow_peer:
              - detection:
                  threshold: 200
          network:
            - address: 192.0.2.1
              mask: 255.255.255.255
              route_map: test
    state: replaced

# Task Output:
# ------------
# before:
#     address_family:
#     - afi: ipv4
#       aggregate_addresses:
#       - address: 192.0.2.1
#         as_confed_set: true
#         netmask: 255.255.255.255
#       bgp:
#         aggregate_timer: 10
#         dampening:
#           max_suppress: 1
#           penalty_half_time: 1
#           reuse_route_val: 1
#           suppress_route_val: 1
#         slow_peer_options:
#           detection:
#             threshold: 150
#       neighbors:
#       - activate: true
#         aigp:
#           send:
#             cost_community:
#               id: 100
#               poi:
#                 igp_cost: true
#                 transitive: true
#         neighbor_address: 198.51.100.1
#         slow_peer_options:
#           detection:
#             threshold: 150
#       networks:
#       - address: 198.51.110.10
#         backdoor: true
#         mask: 255.255.255.255
#       snmp:
#         context:
#           community:
#             acl: '10'
#             ro: true
#             snmp_community: community
#           name: snmp_con
#     - afi: ipv4
#       aggregate_addresses:
#       - address: 192.0.3.1
#         as_confed_set: true
#         netmask: 255.255.255.255
#       default_metric: 12
#       distance:
#         external: 10
#         internal: 10
#         local: 100
#       networks:
#       - address: 198.51.111.11
#         mask: 255.255.255.255
#         route_map: test
#       safi: multicast
#       table_map:
#         filter: true
#         name: test_tableMap
#     - afi: ipv4
#       bgp:
#         dampening:
#           max_suppress: 5
#           penalty_half_time: 1
#           reuse_route_val: 10
#           suppress_route_val: 100
#         dmzlink_bw: true
#         soft_reconfig_backup: true
#       safi: mdt
#     as_number: '65000'
# commands:
# - router bgp 65000
# - address-family ipv4 multicast vrf blue
# - bgp aggregate-timer 10
# - bgp dampening 1 1 1 1
# - bgp slow-peer detection threshold 150
# - neighbor 198.51.110.1 remote-as 10
# - neighbor 198.51.110.1 activate
# - neighbor 198.51.110.1 aigp send cost-community 200 poi igp-cost transitive
# - neighbor 198.51.110.1 slow-peer detection threshold 150
# - network 198.51.110.10 mask 255.255.255.255 backdoor
# - aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
# - address-family ipv4 multicast
# - no default-metric 12
# - no distance bgp 10 10 100
# - no table-map test_tableMap filter
# - bgp aggregate-timer 10
# - bgp dampening 10 10 10 10
# - bgp slow-peer detection threshold 200
# - network 192.0.2.1 mask 255.255.255.255 route-map test
# - no network 198.51.111.11 mask 255.255.255.255 route-map test
# - no aggregate-address 192.0.3.1 255.255.255.255 as-confed-set
# after:
#   address_family:
#   - afi: ipv4
#     aggregate_addresses:
#     - address: 192.0.2.1
#       as_confed_set: true
#       netmask: 255.255.255.255
#     bgp:
#       aggregate_timer: 10
#       dampening:
#         max_suppress: 1
#         penalty_half_time: 1
#         reuse_route_val: 1
#         suppress_route_val: 1
#       slow_peer_options:
#         detection:
#           threshold: 150
#     neighbors:
#     - activate: true
#       aigp:
#         send:
#           cost_community:
#             id: 100
#             poi:
#               igp_cost: true
#               transitive: true
#       neighbor_address: 198.51.100.1
#       slow_peer_options:
#         detection:
#           threshold: 150
#     - activate: true
#       aigp:
#         send:
#           cost_community:
#             id: 200
#             poi:
#               igp_cost: true
#               transitive: true
#       neighbor_address: 198.51.110.1
#       slow_peer_options:
#         detection:
#           threshold: 150
#     networks:
#     - address: 198.51.110.10
#       backdoor: true
#       mask: 255.255.255.255
#     snmp:
#       context:
#         community:
#           acl: '10'
#           ro: true
#           snmp_community: community
#         name: snmp_con
#   - afi: ipv4
#     bgp:
#       aggregate_timer: 10
#       dampening:
#         max_suppress: 10
#         penalty_half_time: 10
#         reuse_route_val: 10
#         suppress_route_val: 10
#       slow_peer_options:
#         detection:
#           threshold: 200
#     networks:
#     - address: 192.0.2.1
#       mask: 255.255.255.255
#       route_map: test
#     safi: multicast
#   - afi: ipv4
#     bgp:
#       dampening:
#         max_suppress: 5
#         penalty_half_time: 1
#         reuse_route_val: 10
#         suppress_route_val: 100
#       dmzlink_bw: true
#       soft_reconfig_backup: true
#     safi: mdt
#   as_number: '65000'

# After state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  snmp context snmp_con community community RO 10
#  neighbor 198.51.100.1 remote-as 10
#  neighbor 198.51.110.1 remote-as 10
#  !
#  address-family ipv4
#   snmp context snmp_con community community RO 10
#   bgp aggregate-timer 10
#   bgp slow-peer detection threshold 150
#   bgp dampening 1 1 1 1
#   network 198.51.110.10 mask 255.255.255.255 backdoor
#   aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
#   neighbor 198.51.100.1 activate
#   neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive
#   neighbor 198.51.100.1 slow-peer detection threshold 150
#   neighbor 198.51.110.1 activate
#   neighbor 198.51.110.1 aigp send cost-community 200 poi igp-cost transitive
#   neighbor 198.51.110.1 slow-peer detection threshold 150
#  exit-address-family
#  !
#  address-family ipv4 multicast
#   bgp aggregate-timer 10
#   bgp slow-peer detection threshold 200
#   bgp dampening 10 10 10 10
#   network 192.0.2.1 mask 255.255.255.255 route-map test
#  exit-address-family
#  !
#  address-family ipv4 mdt
#   bgp dampening 1 10 100 5
#   bgp dmzlink-bw
#   bgp soft-reconfig-backup
#  exit-address-family

# Using overridden

# Before state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  snmp context snmp_con community community RO 10
#  neighbor 198.51.100.1 remote-as 10
#  neighbor 198.51.110.1 remote-as 10
#  !
#  address-family ipv4
#   snmp context snmp_con community community RO 10
#   bgp aggregate-timer 10
#   bgp slow-peer detection threshold 150
#   bgp dampening 1 1 1 1
#   network 198.51.110.10 mask 255.255.255.255 backdoor
#   aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
#   neighbor 198.51.100.1 activate
#   neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive
#   neighbor 198.51.100.1 slow-peer detection threshold 150
#   neighbor 198.51.110.1 activate
#   neighbor 198.51.110.1 aigp send cost-community 200 poi igp-cost transitive
#   neighbor 198.51.110.1 slow-peer detection threshold 150
#  exit-address-family
#  !
#  address-family ipv4 multicast
#   bgp aggregate-timer 10
#   bgp slow-peer detection threshold 200
#   bgp dampening 10 10 10 10
#   network 192.0.2.1 mask 255.255.255.255 route-map test
#  exit-address-family
#  !
#  address-family ipv4 mdt
#   bgp dampening 1 10 100 5
#   bgp dmzlink-bw
#   bgp soft-reconfig-backup
#  exit-address-family

- name: Override device configuration of all AF BGP with provided configuration
  cisco.ios.ios_bgp_address_family:
    config:
      as_number: 65000
      address_family:
        - afi: ipv4
          safi: multicast
          vrf: blue
          aggregate_address:
            - address: 192.0.2.1
              netmask: 255.255.255.255
              as_confed_set: true
          bgp:
            aggregate_timer: 10
            dampening:
              penalty_half_time: 10
              reuse_route_val: 10
              suppress_route_val: 100
              max_suppress: 50
            slow_peer:
              - detection:
                  threshold: 150
          neighbor:
            - address: 198.51.110.1
              activate: true
              log_neighbor_changes:
                disable: true
              maximum_prefix:
                number: 1
                threshold_value: 10
                restart: 100
              slow_peer:
                - detection:
                    threshold: 150
              remote_as: 100
              version: 4
          network:
            - address: 198.51.110.10
              mask: 255.255.255.255
              backdoor: true
        - afi: ipv6
          safi: multicast
          default_information: true
          bgp:
            aggregate_timer: 10
            dampening:
              penalty_half_time: 10
              reuse_route_val: 10
              suppress_route_val: 10
              max_suppress: 10
            slow_peer:
              - detection:
                  threshold: 200
          network:
            - address: 2001:DB8:0:3::/64
              route_map: test_ipv6
    state: overridden

# Task Output:
# ------------
#
# before:
#     address_family:
#     - afi: ipv4
#       aggregate_addresses:
#       - address: 192.0.2.1
#         as_confed_set: true
#         netmask: 255.255.255.255
#       bgp:
#         aggregate_timer: 10
#         dampening:
#           max_suppress: 10
#           penalty_half_time: 10
#           reuse_route_val: 10
#           suppress_route_val: 10
#         slow_peer_options:
#           detection:
#             threshold: 200
#       default_information: true
#       neighbors:
#       - activate: true
#         aigp:
#           send:
#             cost_community:
#               id: 100
#               poi:
#                 igp_cost: true
#                 transitive: true
#         neighbor_address: 198.51.100.1
#         slow_peer_options:
#           detection:
#             threshold: 150
#       - activate: true
#         aigp:
#           send:
#             cost_community:
#               id: 200
#               poi:
#                 igp_cost: true
#                 transitive: true
#         maximum_prefix:
#           number: 1
#           restart: 100
#           threshold_value: 10
#         neighbor_address: 198.51.110.1
#         slow_peer_options:
#           detection:
#             threshold: 150
#       networks:
#       - address: 198.51.110.10
#         backdoor: true
#         mask: 255.255.255.255
#     - afi: ipv4
#       safi: multicast
#     - afi: ipv4
#       safi: mdt
#     - afi: ipv6
#       safi: multicast
#     as_number: '65000'
# commands:
# - router bgp 65000
# - address-family ipv4
# - no default-information originate
# - no bgp aggregate-timer 10
# - no bgp dampening 10 10 10 10
# - no bgp slow-peer detection threshold 200
# - no neighbor 198.51.100.1
# - no neighbor 198.51.110.1
# - no network 198.51.110.10 mask 255.255.255.255 backdoor
# - no aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
# - address-family ipv4 multicast vrf blue
# - bgp aggregate-timer 10
# - bgp dampening 10 10 100 50
# - bgp slow-peer detection threshold 150
# - neighbor 198.51.110.1 remote-as 100
# - neighbor 198.51.110.1 activate
# - neighbor 198.51.110.1 disable
# - neighbor 198.51.110.1 maximum-prefix 1 10 restart 100
# - neighbor 198.51.110.1 slow-peer detection threshold 150
# - neighbor 198.51.110.1 version 4
# - network 198.51.110.10 mask 255.255.255.255 backdoor
# - aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
# - address-family ipv6 multicast
# - default-information originate
# - bgp aggregate-timer 10
# - bgp dampening 10 10 10 10
# - bgp slow-peer detection threshold 200
# after:
#   address_family:
#   - afi: ipv4
#     aggregate_addresses:
#     - address: 192.0.2.1
#       as_confed_set: true
#       netmask: 255.255.255.255
#     bgp:
#       aggregate_timer: 10
#       dampening:
#         max_suppress: 10
#         penalty_half_time: 10
#         reuse_route_val: 10
#         suppress_route_val: 10
#       slow_peer_options:
#         detection:
#           threshold: 200
#     default_information: true
#     neighbors:
#     - activate: true
#       aigp:
#         send:
#           cost_community:
#             id: 100
#             poi:
#               igp_cost: true
#               transitive: true
#       neighbor_address: 198.51.100.1
#       slow_peer_options:
#         detection:
#           threshold: 150
#     - activate: true
#       aigp:
#         send:
#           cost_community:
#             id: 200
#             poi:
#               igp_cost: true
#               transitive: true
#       maximum_prefix:
#         number: 1
#         restart: 100
#         threshold_value: 10
#       neighbor_address: 198.51.110.1
#       slow_peer_options:
#         detection:
#           threshold: 150
#     networks:
#     - address: 198.51.110.10
#       backdoor: true
#       mask: 255.255.255.255
#   - afi: ipv4
#     safi: multicast
#   - afi: ipv4
#     safi: mdt
#   - afi: ipv6
#     safi: multicast
#   as_number: '65000'

# After state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  neighbor 198.51.100.1 remote-as 10
#  neighbor 198.51.110.1 remote-as 100
#  neighbor 198.51.110.1 disable-connected-check
#  neighbor 198.51.110.1 version 4
#  !
#  address-family ipv4
#   bgp aggregate-timer 10
#   bgp slow-peer detection threshold 200
#   bgp dampening 10 10 10 10
#   network 198.51.110.10 mask 255.255.255.255 backdoor
#   aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
#   neighbor 198.51.100.1 activate
#   neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive
#   neighbor 198.51.100.1 slow-peer detection threshold 150
#   neighbor 198.51.110.1 activate
#   neighbor 198.51.110.1 aigp send cost-community 200 poi igp-cost transitive
#   neighbor 198.51.110.1 slow-peer detection threshold 150
#   neighbor 198.51.110.1 maximum-prefix 1 10 restart 100
#   default-information originate
#  exit-address-family
#  !
#  address-family ipv4 multicast
#  exit-address-family
#  !
#  address-family ipv4 mdt
#  exit-address-family
#  !
#  address-family ipv6 multicast
#  exit-address-family

# Using deleted

# Before state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  neighbor 198.51.100.1 remote-as 10
#  neighbor 198.51.110.1 remote-as 100
#  neighbor 198.51.110.1 disable-connected-check
#  neighbor 198.51.110.1 version 4
#  !
#  address-family ipv4
#   bgp aggregate-timer 10
#   bgp slow-peer detection threshold 200
#   bgp dampening 10 10 10 10
#   network 198.51.110.10 mask 255.255.255.255 backdoor
#   aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
#   neighbor 198.51.100.1 activate
#   neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive
#   neighbor 198.51.100.1 slow-peer detection threshold 150
#   neighbor 198.51.110.1 activate
#   neighbor 198.51.110.1 aigp send cost-community 200 poi igp-cost transitive
#   neighbor 198.51.110.1 slow-peer detection threshold 150
#   neighbor 198.51.110.1 maximum-prefix 1 10 restart 100
#   default-information originate
#  exit-address-family
#  !
#  address-family ipv4 multicast
#  exit-address-family
#  !
#  address-family ipv4 mdt
#  exit-address-family
#  !
#  address-family ipv6 multicast
#  exit-address-family

- name: "Delete AF BGP (Note: This won't delete the all configured AF BGP)"
  cisco.ios.ios_bgp_address_family:
    config:
      as_number: 65000
      address_family:
        - afi: ipv4
          safi: multicast
        - afi: ipv4
          safi: mdt
    state: deleted

# Task Output:
# ------------
#
# before:
#     address_family:
#     - afi: ipv4
#       aggregate_addresses:
#       - address: 192.0.2.1
#         as_confed_set: true
#         netmask: 255.255.255.255
#       bgp:
#         aggregate_timer: 10
#         dampening:
#           max_suppress: 10
#           penalty_half_time: 10
#           reuse_route_val: 10
#           suppress_route_val: 10
#         slow_peer_options:
#           detection:
#             threshold: 200
#       default_information: true
#       neighbors:
#       - activate: true
#         aigp:
#           send:
#             cost_community:
#               id: 100
#               poi:
#                 igp_cost: true
#                 transitive: true
#         neighbor_address: 198.51.100.1
#         slow_peer_options:
#           detection:
#             threshold: 150
#       - activate: true
#         aigp:
#           send:
#             cost_community:
#               id: 200
#               poi:
#                 igp_cost: true
#                 transitive: true
#         maximum_prefix:
#           number: 1
#           restart: 100
#           threshold_value: 10
#         neighbor_address: 198.51.110.1
#         slow_peer_options:
#           detection:
#             threshold: 150
#       networks:
#       - address: 198.51.110.10
#         backdoor: true
#         mask: 255.255.255.255
#     - afi: ipv4
#       safi: multicast
#     - afi: ipv4
#       safi: mdt
#     - afi: ipv6
#       safi: multicast
#     as_number: '65000'
# commands:
# - router bgp 65000
# - no address-family ipv4 multicast
# - no address-family ipv4 mdt
# after:
#   address_family:
#   - afi: ipv4
#     aggregate_addresses:
#     - address: 192.0.2.1
#       as_confed_set: true
#       netmask: 255.255.255.255
#     bgp:
#       aggregate_timer: 10
#       dampening:
#         max_suppress: 10
#         penalty_half_time: 10
#         reuse_route_val: 10
#         suppress_route_val: 10
#       slow_peer_options:
#         detection:
#           threshold: 200
#     default_information: true
#     neighbors:
#     - activate: true
#       aigp:
#         send:
#           cost_community:
#             id: 100
#             poi:
#               igp_cost: true
#               transitive: true
#       neighbor_address: 198.51.100.1
#       slow_peer_options:
#         detection:
#           threshold: 150
#     - activate: true
#       aigp:
#         send:
#           cost_community:
#             id: 200
#             poi:
#               igp_cost: true
#               transitive: true
#       maximum_prefix:
#         number: 1
#         restart: 100
#         threshold_value: 10
#       neighbor_address: 198.51.110.1
#       slow_peer_options:
#         detection:
#           threshold: 150
#     networks:
#     - address: 198.51.110.10
#       backdoor: true
#       mask: 255.255.255.255
#   - afi: ipv6
#     safi: multicast
#   as_number: '65000'

# After state:
# -------------
#
# vios#sh running-config | section ^router bg
# hostname#show running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  neighbor 198.51.100.1 remote-as 10
#  neighbor 198.51.110.1 remote-as 100
#  neighbor 198.51.110.1 disable-connected-check
#  neighbor 198.51.110.1 version 4
#  !
#  address-family ipv4
#   bgp aggregate-timer 10
#   bgp slow-peer detection threshold 200
#   bgp dampening 10 10 10 10
#   network 198.51.110.10 mask 255.255.255.255 backdoor
#   aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
#   neighbor 198.51.100.1 activate
#   neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive
#   neighbor 198.51.100.1 slow-peer detection threshold 150
#   neighbor 198.51.110.1 activate
#   neighbor 198.51.110.1 aigp send cost-community 200 poi igp-cost transitive
#   neighbor 198.51.110.1 slow-peer detection threshold 150
#   neighbor 198.51.110.1 maximum-prefix 1 10 restart 100
#   default-information originate
#  exit-address-family
#  !
#  address-family ipv6 multicast
#  exit-address-family

# Using Deleted without any config passed (delete all)

# Before state:
# -------------
#
# vios#sh running-config | section ^router bg
# hostname#show running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  neighbor 198.51.100.1 remote-as 10
#  neighbor 198.51.110.1 remote-as 100
#  neighbor 198.51.110.1 disable-connected-check
#  neighbor 198.51.110.1 version 4
#  !
#  address-family ipv4
#   bgp aggregate-timer 10
#   bgp slow-peer detection threshold 200
#   bgp dampening 10 10 10 10
#   network 198.51.110.10 mask 255.255.255.255 backdoor
#   aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
#   neighbor 198.51.100.1 activate
#   neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive
#   neighbor 198.51.100.1 slow-peer detection threshold 150
#   neighbor 198.51.110.1 activate
#   neighbor 198.51.110.1 aigp send cost-community 200 poi igp-cost transitive
#   neighbor 198.51.110.1 slow-peer detection threshold 150
#   neighbor 198.51.110.1 maximum-prefix 1 10 restart 100
#   default-information originate
#  exit-address-family
#  !
#  address-family ipv6 multicast
#  exit-address-family

- name: "Delete ALL of configured AF BGP"
  cisco.ios.ios_bgp_address_family:
    state: deleted

# Task Output:
# ------------
#
# before:
#   address_family:
#   - afi: ipv4
#     aggregate_addresses:
#     - address: 192.0.2.1
#       as_confed_set: true
#       netmask: 255.255.255.255
#     bgp:
#       aggregate_timer: 10
#       dampening:
#         max_suppress: 10
#         penalty_half_time: 10
#         reuse_route_val: 10
#         suppress_route_val: 10
#       slow_peer_options:
#         detection:
#           threshold: 200
#     default_information: true
#     neighbors:
#     - activate: true
#       aigp:
#         send:
#           cost_community:
#             id: 100
#             poi:
#               igp_cost: true
#               transitive: true
#       neighbor_address: 198.51.100.1
#       slow_peer_options:
#         detection:
#           threshold: 150
#     - activate: true
#       aigp:
#         send:
#           cost_community:
#             id: 200
#             poi:
#               igp_cost: true
#               transitive: true
#       maximum_prefix:
#         number: 1
#         restart: 100
#         threshold_value: 10
#       neighbor_address: 198.51.110.1
#       slow_peer_options:
#         detection:
#           threshold: 150
#     networks:
#     - address: 198.51.110.10
#       backdoor: true
#       mask: 255.255.255.255
#   - afi: ipv6
#     safi: multicast
#   as_number: '65000'
# commands:
# - router bgp 65000
# - no address-family ipv4
# - no address-family ipv6 multicast
# after:
#   address_family:
#   - afi: ipv4
#     bgp:
#       aggregate_timer: 10
#   as_number: '65000'

# After state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  neighbor 198.51.100.1 remote-as 10
#  neighbor 198.51.110.1 remote-as 100
#  neighbor 198.51.110.1 disable-connected-check
#  neighbor 198.51.110.1 version 4
#  !
#  address-family ipv4
#   bgp aggregate-timer 10
#   no neighbor 198.51.100.1 activate
#   no neighbor 198.51.110.1 activate
#  exit-address-family

# Using gathered

# Before state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  snmp context snmp_con community community RO 10
#  neighbor 198.51.100.1 remote-as 10
#  !
#  address-family ipv4
#   snmp context snmp_con community community RO 10
#   bgp aggregate-timer 10
#   bgp slow-peer detection threshold 150
#   bgp dampening 1 1 1 1
#   network 198.51.110.10 mask 255.255.255.255 backdoor
#   aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
#   neighbor 198.51.100.1 activate
#   neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive
#   neighbor 198.51.100.1 slow-peer detection threshold 150
#  exit-address-family
#  !
#  address-family ipv4 multicast
#   table-map test_tableMap filter
#   network 198.51.111.11 mask 255.255.255.255 route-map test
#   aggregate-address 192.0.3.1 255.255.255.255 as-confed-set
#   default-metric 12
#   distance bgp 10 10 100
#  exit-address-family
#  !
#  address-family ipv4 mdt
#   bgp dampening 1 10 100 5
#   bgp dmzlink-bw
#   bgp soft-reconfig-backup
#  exit-address-family

- name: Gather listed AF BGP with provided configurations
  cisco.ios.ios_bgp_address_family:
    config:
    state: gathered

# Task Output:
# ------------
#
# gathered:
#     address_family:
#     - afi: ipv4
#       aggregate_addresses:
#       - address: 192.0.2.1
#         as_confed_set: true
#         netmask: 255.255.255.255
#       bgp:
#         aggregate_timer: 10
#         dampening:
#           max_suppress: 1
#           penalty_half_time: 1
#           reuse_route_val: 1
#           suppress_route_val: 1
#         slow_peer_options:
#           detection:
#             threshold: 150
#       neighbors:
#       - activate: true
#         aigp:
#           send:
#             cost_community:
#               id: 100
#               poi:
#                 igp_cost: true
#                 transitive: true
#         neighbor_address: 198.51.100.1
#         slow_peer_options:
#           detection:
#             threshold: 150
#       networks:
#       - address: 198.51.110.10
#         backdoor: true
#         mask: 255.255.255.255
#       snmp:
#         context:
#           community:
#             acl: '10'
#             ro: true
#             snmp_community: community
#           name: snmp_con
#     - afi: ipv4
#       aggregate_addresses:
#       - address: 192.0.3.1
#         as_confed_set: true
#         netmask: 255.255.255.255
#       default_metric: 12
#       distance:
#         external: 10
#         internal: 10
#         local: 100
#       networks:
#       - address: 198.51.111.11
#         mask: 255.255.255.255
#         route_map: test
#       safi: multicast
#       table_map:
#         filter: true
#         name: test_tableMap
#     - afi: ipv4
#       bgp:
#         dampening:
#           max_suppress: 5
#           penalty_half_time: 1
#           reuse_route_val: 10
#           suppress_route_val: 100
#         dmzlink_bw: true
#         soft_reconfig_backup: true
#       safi: mdt
#     as_number: '65000'

# Using rendered

- name: Rendered the provided configuration with the existing running configuration
  cisco.ios.ios_bgp_address_family:
    config:
      as_number: 65000
      address_family:
        - afi: ipv4
          safi: multicast
          vrf: blue
          aggregate_address:
            - address: 192.0.2.1
              netmask: 255.255.255.255
              as_confed_set: true
          bgp:
            aggregate_timer: 10
            dampening:
              penalty_half_time: 1
              reuse_route_val: 1
              suppress_route_val: 1
              max_suppress: 1
            slow_peer:
              - detection:
                  threshold: 150
          neighbor:
            - address: 198.51.100.1
              aigp:
                send:
                  cost_community:
                    id: 100
                    poi:
                      igp_cost: true
                      transitive: true
              slow_peer:
                - detection:
                    threshold: 150
              remote_as: 10
              route_maps:
                - name: test-route
                  out: true
              route_server_client: true
          network:
            - address: 198.51.110.10
              mask: 255.255.255.255
              backdoor: true
          snmp:
            context:
              name: snmp_con
              community:
                snmp_community: community
                ro: true
                acl: 10
        - afi: ipv4
          safi: mdt
          bgp:
            dmzlink_bw: true
            dampening:
              penalty_half_time: 1
              reuse_route_val: 10
              suppress_route_val: 100
              max_suppress: 5
            soft_reconfig_backup: true
    state: rendered

# Task Output:
# ------------
#
# rendered:
# - router bgp 65000
# - address-family ipv4 multicast vrf blue
# - bgp aggregate-timer 10
# - bgp dampening 1 1 1 1
# - bgp slow-peer detection threshold 150
# - snmp context snmp_con community community ro 10
# - neighbor 198.51.100.1 remote-as 10
# - neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive
# - neighbor 198.51.100.1 slow-peer detection threshold 150
# - network 198.51.110.10 mask 255.255.255.255 backdoor
# - aggregate-address 192.0.2.1 255.255.255.255 as-confed-set
# - address-family ipv4 mdt
# - bgp dmzlink-bw
# - bgp soft-reconfig-backup
# - bgp dampening 1 10 100 5

# Using parsed

# File: parsed.cfg
# ----------------
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp nopeerup-delay cold-boot 20
#  !
#  address-family ipv4 multicast
#   table-map test_tableMap filter
#   network 1.1.1.1 mask 255.255.255.255 route-map test
#   aggregate-address 192.0.3.1 255.255.255.255 as-confed-set
#   default-metric 12
#   distance bgp 10 10 100
#  exit-address-family
#  !
#  address-family ipv4 mdt
#   bgp dampening 1 10 100 5
#   bgp dmzlink-bw
#   bgp soft-reconfig-backup
#  exit-address-family
#  !

- name: Parse the commands for provided configuration
  cisco.ios.ios_bgp_address_family:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task Output:
# ------------
#
# parsed:
#     address_family:
#     - afi: ipv4
#       aggregate_addresses:
#       - address: 192.0.2.1
#         as_confed_set: true
#         netmask: 255.255.255.255
#       bgp:
#         aggregate_timer: 10
#         dampening:
#           max_suppress: 1
#           penalty_half_time: 1
#           reuse_route_val: 1
#           suppress_route_val: 1
#         slow_peer_options:
#           detection:
#             threshold: 150
#       neighbors:
#       - activate: true
#         aigp:
#           send:
#             cost_community:
#               id: 100
#               poi:
#                 igp_cost: true
#                 transitive: true
#         neighbor_address: 198.51.100.1
#         slow_peer_options:
#           detection:
#             threshold: 150
#       networks:
#       - address: 198.51.110.10
#         backdoor: true
#         mask: 255.255.255.255
#       snmp:
#         context:
#           community:
#             acl: '10'
#             ro: true
#             snmp_community: community
#           name: snmp_con
#     - afi: ipv4
#       aggregate_addresses:
#       - address: 192.0.3.1
#         as_confed_set: true
#         netmask: 255.255.255.255
#       default_metric: 12
#       distance:
#         external: 10
#         internal: 10
#         local: 100
#       networks:
#       - address: 198.51.111.11
#         mask: 255.255.255.255
#         route_map: test
#       safi: multicast
#       table_map:
#         filter: true
#         name: test_tableMap
#     - afi: ipv4
#       bgp:
#         dampening:
#           max_suppress: 5
#           penalty_half_time: 1
#           reuse_route_val: 10
#           suppress_route_val: 100
#         dmzlink_bw: true
#         soft_reconfig_backup: true
#       safi: mdt
#     as_number: '65000'
```

## [Return Values](ios_bgp_address_family_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["router bgp 65000", "address-family ipv4 multicast", "table-map test_tableMap filter", "network 1.1.1.1 mask 255.255.255.255 route-map test", "aggregate-address 192.0.3.1 255.255.255.255 as-confed-set"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["router bgp 65000", "address-family ipv4 multicast", "table-map test_tableMap filter", "network 1.1.1.1 mask 255.255.255.255 route-map test", "aggregate-address 192.0.3.1 255.255.255.255 as-confed-set"]` |

### Authors

- Sagar Paul (@KB-perByte)
- Sumit Jaiswal (@justjais)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
