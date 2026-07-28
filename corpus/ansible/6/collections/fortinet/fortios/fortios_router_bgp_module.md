---
collection: ansible
version: "6"
title: "fortinet.fortios.fortios_router_bgp module – Configure BGP in Fortinet’s FortiOS and FortiGate."
source_url: https://docs.ansible.com/projects/ansible/6/collections/fortinet/fortios/fortios_router_bgp_module.html
fetched_at: 2026-07-27T17:43:01+00:00
---
# fortinet.fortios.fortios_router_bgp module – Configure BGP in Fortinet’s FortiOS and FortiGate.

> **Note:**
>
> This module is part of the [fortinet.fortios collection](https://galaxy.ansible.com/fortinet/fortios) (version 2.2.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortios`.
> You need further requirements to be able to use this module,
> see [Requirements](fortios_router_bgp_module.md#ansible-collections-fortinet-fortios-fortios-router-bgp-module-requirements) for details.
>
> To use it in a playbook, specify: `fortinet.fortios.fortios_router_bgp`.

New in fortinet.fortios 2.0.0

- [Synopsis](fortios_router_bgp_module.md#synopsis)
- [Requirements](fortios_router_bgp_module.md#requirements)
- [Parameters](fortios_router_bgp_module.md#parameters)
- [Notes](fortios_router_bgp_module.md#notes)
- [Examples](fortios_router_bgp_module.md#examples)
- [Return Values](fortios_router_bgp_module.md#return-values)

## [Synopsis](fortios_router_bgp_module.md#id5)

- This module is able to configure a FortiGate or FortiOS (FOS) device by allowing the user to set and modify router feature and bgp category. Examples include all parameters and values need to be adjusted to datasources before usage. Tested with FOS v6.0.0

## [Requirements](fortios_router_bgp_module.md#id6)

The below requirements are needed on the host that executes this module.

- ansible>=2.9

## [Parameters](fortios_router_bgp_module.md#id7)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | Token-based authentication. Generated from GUI of Fortigate. |
| **enable_log**  boolean | Enable/Disable logging for task.  Choices:   - `false` ← (default) - `true` |
| **member_path**  string | Member attribute path to operate on.  Delimited by a slash character if there are more than one attribute.  Parameter marked with member_path is legitimate for doing member operation. |
| **member_state**  string | Add or delete a member under specified attribute path.  When member_state is specified, the state option is ignored.  Choices:   - `"present"` - `"absent"` |
| **router_bgp**  dictionary | Configure BGP. |
| **additional_path**  string | Enable/disable selection of BGP IPv4 additional paths.  Choices:   - `"enable"` - `"disable"` |
| **additional_path6**  string | Enable/disable selection of BGP IPv6 additional paths.  Choices:   - `"enable"` - `"disable"` |
| **additional_path_select**  integer | Number of additional paths to be selected for each IPv4 NLRI. |
| **additional_path_select6**  integer | Number of additional paths to be selected for each IPv6 NLRI. |
| **additional_path_select_vpnv4**  integer | Number of additional paths to be selected for each VPNv4 NLRI. |
| **additional_path_vpnv4**  string | Enable/disable selection of BGP VPNv4 additional paths.  Choices:   - `"enable"` - `"disable"` |
| **admin_distance**  list / elements=dictionary | Administrative distance modifications. |
| **distance**  integer | Administrative distance to apply (1 - 255). |
| **id**  integer | ID. |
| **neighbour_prefix**  string | Neighbor address prefix. |
| **route_list**  string | Access list of routes to apply new distance to. Source router.access-list.name. |
| **aggregate_address**  list / elements=dictionary | BGP aggregate address table. |
| **as_set**  string | Enable/disable generate AS set path information.  Choices:   - `"enable"` - `"disable"` |
| **id**  integer | ID. |
| **prefix**  string | Aggregate prefix. |
| **summary_only**  string | Enable/disable filter more specific routes from updates.  Choices:   - `"enable"` - `"disable"` |
| **aggregate_address6**  list / elements=dictionary | BGP IPv6 aggregate address table. |
| **as_set**  string | Enable/disable generate AS set path information.  Choices:   - `"enable"` - `"disable"` |
| **id**  integer | ID. |
| **prefix6**  string | Aggregate IPv6 prefix. |
| **summary_only**  string | Enable/disable filter more specific routes from updates.  Choices:   - `"enable"` - `"disable"` |
| **always_compare_med**  string | Enable/disable always compare MED.  Choices:   - `"enable"` - `"disable"` |
| **as**  string | Router AS number, asplain/asdot/asdot+ format, 0 to disable BGP. |
| **bestpath_as_path_ignore**  string | Enable/disable ignore AS path.  Choices:   - `"enable"` - `"disable"` |
| **bestpath_cmp_confed_aspath**  string | Enable/disable compare federation AS path length.  Choices:   - `"enable"` - `"disable"` |
| **bestpath_cmp_routerid**  string | Enable/disable compare router ID for identical EBGP paths.  Choices:   - `"enable"` - `"disable"` |
| **bestpath_med_confed**  string | Enable/disable compare MED among confederation paths.  Choices:   - `"enable"` - `"disable"` |
| **bestpath_med_missing_as_worst**  string | Enable/disable treat missing MED as least preferred.  Choices:   - `"enable"` - `"disable"` |
| **client_to_client_reflection**  string | Enable/disable client-to-client route reflection.  Choices:   - `"enable"` - `"disable"` |
| **cluster_id**  string | Route reflector cluster ID. |
| **confederation_identifier**  integer | Confederation identifier. |
| **confederation_peers**  list / elements=dictionary | Confederation peers. |
| **peer**  string | Peer ID. |
| **dampening**  string | Enable/disable route-flap dampening.  Choices:   - `"enable"` - `"disable"` |
| **dampening_max_suppress_time**  integer | Maximum minutes a route can be suppressed. |
| **dampening_reachability_half_life**  integer | Reachability half-life time for penalty (min). |
| **dampening_reuse**  integer | Threshold to reuse routes. |
| **dampening_route_map**  string | Criteria for dampening. Source router.route-map.name. |
| **dampening_suppress**  integer | Threshold to suppress routes. |
| **dampening_unreachability_half_life**  integer | Unreachability half-life time for penalty (min). |
| **default_local_preference**  integer | Default local preference. |
| **deterministic_med**  string | Enable/disable enforce deterministic comparison of MED.  Choices:   - `"enable"` - `"disable"` |
| **distance_external**  integer | Distance for routes external to the AS. |
| **distance_internal**  integer | Distance for routes internal to the AS. |
| **distance_local**  integer | Distance for routes local to the AS. |
| **ebgp_multipath**  string | Enable/disable EBGP multi-path.  Choices:   - `"enable"` - `"disable"` |
| **enforce_first_as**  string | Enable/disable enforce first AS for EBGP routes.  Choices:   - `"enable"` - `"disable"` |
| **fast_external_failover**  string | Enable/disable reset peer BGP session if link goes down.  Choices:   - `"enable"` - `"disable"` |
| **graceful_end_on_timer**  string | Enable/disable to exit graceful restart on timer only.  Choices:   - `"enable"` - `"disable"` |
| **graceful_restart**  string | Enable/disable BGP graceful restart capabilities.  Choices:   - `"enable"` - `"disable"` |
| **graceful_restart_time**  integer | Time needed for neighbors to restart (sec). |
| **graceful_stalepath_time**  integer | Time to hold stale paths of restarting neighbor (sec). |
| **graceful_update_delay**  integer | Route advertisement/selection delay after restart (sec). |
| **holdtime_timer**  integer | Number of seconds to mark peer as dead. |
| **ibgp_multipath**  string | Enable/disable IBGP multi-path.  Choices:   - `"enable"` - `"disable"` |
| **ignore_optional_capability**  string | Do not send unknown optional capability notification message.  Choices:   - `"enable"` - `"disable"` |
| **keepalive_timer**  integer | Frequency to send keep alive requests. |
| **log_neighbour_changes**  string | Log BGP neighbor changes.  Choices:   - `"enable"` - `"disable"` |
| **multipath_recursive_distance**  string | Enable/disable use of recursive distance to select multipath.  Choices:   - `"enable"` - `"disable"` |
| **neighbor**  list / elements=dictionary | BGP neighbor table. |
| **activate**  string | Enable/disable address family IPv4 for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **activate6**  string | Enable/disable address family IPv6 for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **activate_vpnv4**  string | Enable/disable address family VPNv4 for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **additional_path**  string | Enable/disable IPv4 additional-path capability.  Choices:   - `"send"` - `"receive"` - `"both"` - `"disable"` |
| **additional_path6**  string | Enable/disable IPv6 additional-path capability.  Choices:   - `"send"` - `"receive"` - `"both"` - `"disable"` |
| **additional_path_vpnv4**  string | Enable/disable VPNv4 additional-path capability.  Choices:   - `"send"` - `"receive"` - `"both"` - `"disable"` |
| **adv_additional_path**  integer | Number of IPv4 additional paths that can be advertised to this neighbor. |
| **adv_additional_path6**  integer | Number of IPv6 additional paths that can be advertised to this neighbor. |
| **adv_additional_path_vpnv4**  integer | Number of VPNv4 additional paths that can be advertised to this neighbor. |
| **advertisement_interval**  integer | Minimum interval (sec) between sending updates. |
| **allowas_in**  integer | IPv4 The maximum number of occurrence of my AS number allowed. |
| **allowas_in6**  integer | IPv6 The maximum number of occurrence of my AS number allowed. |
| **allowas_in_enable**  string | Enable/disable IPv4 Enable to allow my AS in AS path.  Choices:   - `"enable"` - `"disable"` |
| **allowas_in_enable6**  string | Enable/disable IPv6 Enable to allow my AS in AS path.  Choices:   - `"enable"` - `"disable"` |
| **allowas_in_vpnv4**  integer | The maximum number of occurrence of my AS number allowed for VPNv4 route. |
| **as_override**  string | Enable/disable replace peer AS with own AS for IPv4.  Choices:   - `"enable"` - `"disable"` |
| **as_override6**  string | Enable/disable replace peer AS with own AS for IPv6.  Choices:   - `"enable"` - `"disable"` |
| **attribute_unchanged**  list / elements=string | IPv4 List of attributes that should be unchanged.  Choices:   - `"as-path"` - `"med"` - `"next-hop"` |
| **attribute_unchanged6**  list / elements=string | IPv6 List of attributes that should be unchanged.  Choices:   - `"as-path"` - `"med"` - `"next-hop"` |
| **attribute_unchanged_vpnv4**  list / elements=string | List of attributes that should be unchanged for VPNv4 route.  Choices:   - `"as-path"` - `"med"` - `"next-hop"` |
| **bfd**  string | Enable/disable BFD for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_default_originate**  string | Enable/disable advertise default IPv4 route to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_default_originate6**  string | Enable/disable advertise default IPv6 route to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_dynamic**  string | Enable/disable advertise dynamic capability to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_graceful_restart**  string | Enable/disable advertise IPv4 graceful restart capability to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_graceful_restart6**  string | Enable/disable advertise IPv6 graceful restart capability to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_graceful_restart_vpnv4**  string | Enable/disable advertise VPNv4 graceful restart capability to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_orf**  string | Accept/Send IPv4 ORF lists to/from this neighbor.  Choices:   - `"none"` - `"receive"` - `"send"` - `"both"` |
| **capability_orf6**  string | Accept/Send IPv6 ORF lists to/from this neighbor.  Choices:   - `"none"` - `"receive"` - `"send"` - `"both"` |
| **capability_route_refresh**  string | Enable/disable advertise route refresh capability to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **conditional_advertise**  list / elements=dictionary | Conditional advertisement. |
| **advertise_routemap**  string | Name of advertising route map. Source router.route-map.name. |
| **condition_routemap**  list / elements=dictionary | List of conditional route maps. Source router.route-map.name. |
| **name**  string | route map Source router.route-map.name. |
| **condition_type**  string | Type of condition.  Choices:   - `"exist"` - `"non-exist"` |
| **conditional_advertise6**  list / elements=dictionary | IPv6 conditional advertisement. |
| **advertise_routemap**  string | Name of advertising route map. Source router.route-map.name. |
| **condition_routemap**  list / elements=dictionary | List of conditional route maps. Source router.route-map.name. |
| **name**  string | route map Source router.route-map.name. |
| **condition_type**  string | Type of condition.  Choices:   - `"exist"` - `"non-exist"` |
| **connect_timer**  integer | Interval (sec) for connect timer. |
| **default_originate_routemap**  string | Route map to specify criteria to originate IPv4 default. Source router.route-map.name. |
| **default_originate_routemap6**  string | Route map to specify criteria to originate IPv6 default. Source router.route-map.name. |
| **description**  string | Description. |
| **distribute_list_in**  string | Filter for IPv4 updates from this neighbor. Source router.access-list.name. |
| **distribute_list_in6**  string | Filter for IPv6 updates from this neighbor. Source router.access-list6.name. |
| **distribute_list_in_vpnv4**  string | Filter for VPNv4 updates from this neighbor. Source router.access-list.name. |
| **distribute_list_out**  string | Filter for IPv4 updates to this neighbor. Source router.access-list.name. |
| **distribute_list_out6**  string | Filter for IPv6 updates to this neighbor. Source router.access-list6.name. |
| **distribute_list_out_vpnv4**  string | Filter for VPNv4 updates to this neighbor. Source router.access-list.name. |
| **dont_capability_negotiate**  string | Do not negotiate capabilities with this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **ebgp_enforce_multihop**  string | Enable/disable allow multi-hop EBGP neighbors.  Choices:   - `"enable"` - `"disable"` |
| **ebgp_multihop_ttl**  integer | EBGP multihop TTL for this peer. |
| **filter_list_in**  string | BGP filter for IPv4 inbound routes. Source router.aspath-list.name. |
| **filter_list_in6**  string | BGP filter for IPv6 inbound routes. Source router.aspath-list.name. |
| **filter_list_out**  string | BGP filter for IPv4 outbound routes. Source router.aspath-list.name. |
| **filter_list_out6**  string | BGP filter for IPv6 outbound routes. Source router.aspath-list.name. |
| **holdtime_timer**  integer | Interval (sec) before peer considered dead. |
| **interface**  string | Specify outgoing interface for peer connection. For IPv6 peer, the interface should have link-local address. Source system .interface.name. |
| **ip**  string | IP/IPv6 address of neighbor. |
| **keep_alive_timer**  integer | Keep alive timer interval (sec). |
| **link_down_failover**  string | Enable/disable failover upon link down.  Choices:   - `"enable"` - `"disable"` |
| **local_as**  string | Local AS number of neighbor. |
| **local_as_no_prepend**  string | Do not prepend local-as to incoming updates.  Choices:   - `"enable"` - `"disable"` |
| **local_as_replace_as**  string | Replace real AS with local-as in outgoing updates.  Choices:   - `"enable"` - `"disable"` |
| **maximum_prefix**  integer | Maximum number of IPv4 prefixes to accept from this peer. |
| **maximum_prefix6**  integer | Maximum number of IPv6 prefixes to accept from this peer. |
| **maximum_prefix_threshold**  integer | Maximum IPv4 prefix threshold value (1 - 100 percent). |
| **maximum_prefix_threshold6**  integer | Maximum IPv6 prefix threshold value (1 - 100 percent). |
| **maximum_prefix_threshold_vpnv4**  integer | Maximum VPNv4 prefix threshold value (1 - 100 percent). |
| **maximum_prefix_vpnv4**  integer | Maximum number of VPNv4 prefixes to accept from this peer. |
| **maximum_prefix_warning_only**  string | Enable/disable IPv4 Only give warning message when limit is exceeded.  Choices:   - `"enable"` - `"disable"` |
| **maximum_prefix_warning_only6**  string | Enable/disable IPv6 Only give warning message when limit is exceeded.  Choices:   - `"enable"` - `"disable"` |
| **maximum_prefix_warning_only_vpnv4**  string | Enable/disable only giving warning message when limit is exceeded for VPNv4 routes.  Choices:   - `"enable"` - `"disable"` |
| **next_hop_self**  string | Enable/disable IPv4 next-hop calculation for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **next_hop_self6**  string | Enable/disable IPv6 next-hop calculation for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **next_hop_self_rr**  string | Enable/disable setting nexthop”s address to interface”s IPv4 address for route-reflector routes.  Choices:   - `"enable"` - `"disable"` |
| **next_hop_self_rr6**  string | Enable/disable setting nexthop”s address to interface”s IPv6 address for route-reflector routes.  Choices:   - `"enable"` - `"disable"` |
| **next_hop_self_vpnv4**  string | Enable/disable setting VPNv4 next-hop to interface”s IP address for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **override_capability**  string | Enable/disable override result of capability negotiation.  Choices:   - `"enable"` - `"disable"` |
| **passive**  string | Enable/disable sending of open messages to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **password**  string | Password used in MD5 authentication. |
| **prefix_list_in**  string | IPv4 Inbound filter for updates from this neighbor. Source router.prefix-list.name. |
| **prefix_list_in6**  string | IPv6 Inbound filter for updates from this neighbor. Source router.prefix-list6.name. |
| **prefix_list_in_vpnv4**  string | Inbound filter for VPNv4 updates from this neighbor. Source router.prefix-list.name. |
| **prefix_list_out**  string | IPv4 Outbound filter for updates to this neighbor. Source router.prefix-list.name. |
| **prefix_list_out6**  string | IPv6 Outbound filter for updates to this neighbor. Source router.prefix-list6.name. |
| **prefix_list_out_vpnv4**  string | Outbound filter for VPNv4 updates to this neighbor. Source router.prefix-list.name. |
| **remote_as**  string | AS number of neighbor. |
| **remove_private_as**  string | Enable/disable remove private AS number from IPv4 outbound updates.  Choices:   - `"enable"` - `"disable"` |
| **remove_private_as6**  string | Enable/disable remove private AS number from IPv6 outbound updates.  Choices:   - `"enable"` - `"disable"` |
| **remove_private_as_vpnv4**  string | Enable/disable remove private AS number from VPNv4 outbound updates.  Choices:   - `"enable"` - `"disable"` |
| **restart_time**  integer | Graceful restart delay time (sec, 0 = global default). |
| **retain_stale_time**  integer | Time to retain stale routes. |
| **route_map_in**  string | IPv4 Inbound route map filter. Source router.route-map.name. |
| **route_map_in6**  string | IPv6 Inbound route map filter. Source router.route-map.name. |
| **route_map_in_vpnv4**  string | VPNv4 inbound route map filter. Source router.route-map.name. |
| **route_map_out**  string | IPv4 outbound route map filter. Source router.route-map.name. |
| **route_map_out6**  string | IPv6 Outbound route map filter. Source router.route-map.name. |
| **route_map_out6_preferable**  string | IPv6 outbound route map filter if the peer is preferred. Source router.route-map.name. |
| **route_map_out_preferable**  string | IPv4 outbound route map filter if the peer is preferred. Source router.route-map.name. |
| **route_map_out_vpnv4**  string | VPNv4 outbound route map filter. Source router.route-map.name. |
| **route_map_out_vpnv4_preferable**  string | VPNv4 outbound route map filter if the peer is preferred. Source router.route-map.name. |
| **route_reflector_client**  string | Enable/disable IPv4 AS route reflector client.  Choices:   - `"enable"` - `"disable"` |
| **route_reflector_client6**  string | Enable/disable IPv6 AS route reflector client.  Choices:   - `"enable"` - `"disable"` |
| **route_reflector_client_vpnv4**  string | Enable/disable VPNv4 AS route reflector client for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **route_server_client**  string | Enable/disable IPv4 AS route server client.  Choices:   - `"enable"` - `"disable"` |
| **route_server_client6**  string | Enable/disable IPv6 AS route server client.  Choices:   - `"enable"` - `"disable"` |
| **route_server_client_vpnv4**  string | Enable/disable VPNv4 AS route server client for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **send_community**  string | IPv4 Send community attribute to neighbor.  Choices:   - `"standard"` - `"extended"` - `"both"` - `"disable"` |
| **send_community6**  string | IPv6 Send community attribute to neighbor.  Choices:   - `"standard"` - `"extended"` - `"both"` - `"disable"` |
| **send_community_vpnv4**  string | Send community attribute to neighbor for VPNv4 address family.  Choices:   - `"standard"` - `"extended"` - `"both"` - `"disable"` |
| **shutdown**  string | Enable/disable shutdown this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **soft_reconfiguration**  string | Enable/disable allow IPv4 inbound soft reconfiguration.  Choices:   - `"enable"` - `"disable"` |
| **soft_reconfiguration6**  string | Enable/disable allow IPv6 inbound soft reconfiguration.  Choices:   - `"enable"` - `"disable"` |
| **soft_reconfiguration_vpnv4**  string | Enable/disable allow VPNv4 inbound soft reconfiguration.  Choices:   - `"enable"` - `"disable"` |
| **stale_route**  string | Enable/disable stale route after neighbor down.  Choices:   - `"enable"` - `"disable"` |
| **strict_capability_match**  string | Enable/disable strict capability matching.  Choices:   - `"enable"` - `"disable"` |
| **unsuppress_map**  string | IPv4 Route map to selectively unsuppress suppressed routes. Source router.route-map.name. |
| **unsuppress_map6**  string | IPv6 Route map to selectively unsuppress suppressed routes. Source router.route-map.name. |
| **update_source**  string | Interface to use as source IP/IPv6 address of TCP connections. Source system.interface.name. |
| **weight**  integer | Neighbor weight. |
| **neighbor_group**  list / elements=dictionary | BGP neighbor group table. |
| **activate**  string | Enable/disable address family IPv4 for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **activate6**  string | Enable/disable address family IPv6 for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **activate_vpnv4**  string | Enable/disable address family VPNv4 for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **additional_path**  string | Enable/disable IPv4 additional-path capability.  Choices:   - `"send"` - `"receive"` - `"both"` - `"disable"` |
| **additional_path6**  string | Enable/disable IPv6 additional-path capability.  Choices:   - `"send"` - `"receive"` - `"both"` - `"disable"` |
| **additional_path_vpnv4**  string | Enable/disable VPNv4 additional-path capability.  Choices:   - `"send"` - `"receive"` - `"both"` - `"disable"` |
| **adv_additional_path**  integer | Number of IPv4 additional paths that can be advertised to this neighbor. |
| **adv_additional_path6**  integer | Number of IPv6 additional paths that can be advertised to this neighbor. |
| **adv_additional_path_vpnv4**  integer | Number of VPNv4 additional paths that can be advertised to this neighbor. |
| **advertisement_interval**  integer | Minimum interval (sec) between sending updates. |
| **allowas_in**  integer | IPv4 The maximum number of occurrence of my AS number allowed. |
| **allowas_in6**  integer | IPv6 The maximum number of occurrence of my AS number allowed. |
| **allowas_in_enable**  string | Enable/disable IPv4 Enable to allow my AS in AS path.  Choices:   - `"enable"` - `"disable"` |
| **allowas_in_enable6**  string | Enable/disable IPv6 Enable to allow my AS in AS path.  Choices:   - `"enable"` - `"disable"` |
| **allowas_in_vpnv4**  integer | The maximum number of occurrence of my AS number allowed for VPNv4 route. |
| **as_override**  string | Enable/disable replace peer AS with own AS for IPv4.  Choices:   - `"enable"` - `"disable"` |
| **as_override6**  string | Enable/disable replace peer AS with own AS for IPv6.  Choices:   - `"enable"` - `"disable"` |
| **attribute_unchanged**  list / elements=string | IPv4 List of attributes that should be unchanged.  Choices:   - `"as-path"` - `"med"` - `"next-hop"` |
| **attribute_unchanged6**  list / elements=string | IPv6 List of attributes that should be unchanged.  Choices:   - `"as-path"` - `"med"` - `"next-hop"` |
| **attribute_unchanged_vpnv4**  list / elements=string | List of attributes that should be unchanged for VPNv4 route.  Choices:   - `"as-path"` - `"med"` - `"next-hop"` |
| **bfd**  string | Enable/disable BFD for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_default_originate**  string | Enable/disable advertise default IPv4 route to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_default_originate6**  string | Enable/disable advertise default IPv6 route to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_dynamic**  string | Enable/disable advertise dynamic capability to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_graceful_restart**  string | Enable/disable advertise IPv4 graceful restart capability to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_graceful_restart6**  string | Enable/disable advertise IPv6 graceful restart capability to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_graceful_restart_vpnv4**  string | Enable/disable advertise VPNv4 graceful restart capability to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **capability_orf**  string | Accept/Send IPv4 ORF lists to/from this neighbor.  Choices:   - `"none"` - `"receive"` - `"send"` - `"both"` |
| **capability_orf6**  string | Accept/Send IPv6 ORF lists to/from this neighbor.  Choices:   - `"none"` - `"receive"` - `"send"` - `"both"` |
| **capability_route_refresh**  string | Enable/disable advertise route refresh capability to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **connect_timer**  integer | Interval (sec) for connect timer. |
| **default_originate_routemap**  string | Route map to specify criteria to originate IPv4 default. Source router.route-map.name. |
| **default_originate_routemap6**  string | Route map to specify criteria to originate IPv6 default. Source router.route-map.name. |
| **description**  string | Description. |
| **distribute_list_in**  string | Filter for IPv4 updates from this neighbor. Source router.access-list.name. |
| **distribute_list_in6**  string | Filter for IPv6 updates from this neighbor. Source router.access-list6.name. |
| **distribute_list_in_vpnv4**  string | Filter for VPNv4 updates from this neighbor. Source router.access-list.name. |
| **distribute_list_out**  string | Filter for IPv4 updates to this neighbor. Source router.access-list.name. |
| **distribute_list_out6**  string | Filter for IPv6 updates to this neighbor. Source router.access-list6.name. |
| **distribute_list_out_vpnv4**  string | Filter for VPNv4 updates to this neighbor. Source router.access-list.name. |
| **dont_capability_negotiate**  string | Do not negotiate capabilities with this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **ebgp_enforce_multihop**  string | Enable/disable allow multi-hop EBGP neighbors.  Choices:   - `"enable"` - `"disable"` |
| **ebgp_multihop_ttl**  integer | EBGP multihop TTL for this peer. |
| **filter_list_in**  string | BGP filter for IPv4 inbound routes. Source router.aspath-list.name. |
| **filter_list_in6**  string | BGP filter for IPv6 inbound routes. Source router.aspath-list.name. |
| **filter_list_out**  string | BGP filter for IPv4 outbound routes. Source router.aspath-list.name. |
| **filter_list_out6**  string | BGP filter for IPv6 outbound routes. Source router.aspath-list.name. |
| **holdtime_timer**  integer | Interval (sec) before peer considered dead. |
| **interface**  string | Specify outgoing interface for peer connection. For IPv6 peer, the interface should have link-local address. Source system .interface.name. |
| **keep_alive_timer**  integer | Keep alive timer interval (sec). |
| **link_down_failover**  string | Enable/disable failover upon link down.  Choices:   - `"enable"` - `"disable"` |
| **local_as**  string | Local AS number of neighbor. |
| **local_as_no_prepend**  string | Do not prepend local-as to incoming updates.  Choices:   - `"enable"` - `"disable"` |
| **local_as_replace_as**  string | Replace real AS with local-as in outgoing updates.  Choices:   - `"enable"` - `"disable"` |
| **maximum_prefix**  integer | Maximum number of IPv4 prefixes to accept from this peer. |
| **maximum_prefix6**  integer | Maximum number of IPv6 prefixes to accept from this peer. |
| **maximum_prefix_threshold**  integer | Maximum IPv4 prefix threshold value (1 - 100 percent). |
| **maximum_prefix_threshold6**  integer | Maximum IPv6 prefix threshold value (1 - 100 percent). |
| **maximum_prefix_threshold_vpnv4**  integer | Maximum VPNv4 prefix threshold value (1 - 100 percent). |
| **maximum_prefix_vpnv4**  integer | Maximum number of VPNv4 prefixes to accept from this peer. |
| **maximum_prefix_warning_only**  string | Enable/disable IPv4 Only give warning message when limit is exceeded.  Choices:   - `"enable"` - `"disable"` |
| **maximum_prefix_warning_only6**  string | Enable/disable IPv6 Only give warning message when limit is exceeded.  Choices:   - `"enable"` - `"disable"` |
| **maximum_prefix_warning_only_vpnv4**  string | Enable/disable only giving warning message when limit is exceeded for VPNv4 routes.  Choices:   - `"enable"` - `"disable"` |
| **name**  string | Neighbor group name. |
| **next_hop_self**  string | Enable/disable IPv4 next-hop calculation for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **next_hop_self6**  string | Enable/disable IPv6 next-hop calculation for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **next_hop_self_rr**  string | Enable/disable setting nexthop”s address to interface”s IPv4 address for route-reflector routes.  Choices:   - `"enable"` - `"disable"` |
| **next_hop_self_rr6**  string | Enable/disable setting nexthop”s address to interface”s IPv6 address for route-reflector routes.  Choices:   - `"enable"` - `"disable"` |
| **next_hop_self_vpnv4**  string | Enable/disable setting VPNv4 next-hop to interface”s IP address for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **override_capability**  string | Enable/disable override result of capability negotiation.  Choices:   - `"enable"` - `"disable"` |
| **passive**  string | Enable/disable sending of open messages to this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **prefix_list_in**  string | IPv4 Inbound filter for updates from this neighbor. Source router.prefix-list.name. |
| **prefix_list_in6**  string | IPv6 Inbound filter for updates from this neighbor. Source router.prefix-list6.name. |
| **prefix_list_in_vpnv4**  string | Inbound filter for VPNv4 updates from this neighbor. Source router.prefix-list.name. |
| **prefix_list_out**  string | IPv4 Outbound filter for updates to this neighbor. Source router.prefix-list.name. |
| **prefix_list_out6**  string | IPv6 Outbound filter for updates to this neighbor. Source router.prefix-list6.name. |
| **prefix_list_out_vpnv4**  string | Outbound filter for VPNv4 updates to this neighbor. Source router.prefix-list.name. |
| **remote_as**  string | AS number of neighbor. |
| **remove_private_as**  string | Enable/disable remove private AS number from IPv4 outbound updates.  Choices:   - `"enable"` - `"disable"` |
| **remove_private_as6**  string | Enable/disable remove private AS number from IPv6 outbound updates.  Choices:   - `"enable"` - `"disable"` |
| **remove_private_as_vpnv4**  string | Enable/disable remove private AS number from VPNv4 outbound updates.  Choices:   - `"enable"` - `"disable"` |
| **restart_time**  integer | Graceful restart delay time (sec, 0 = global default). |
| **retain_stale_time**  integer | Time to retain stale routes. |
| **route_map_in**  string | IPv4 Inbound route map filter. Source router.route-map.name. |
| **route_map_in6**  string | IPv6 Inbound route map filter. Source router.route-map.name. |
| **route_map_in_vpnv4**  string | VPNv4 inbound route map filter. Source router.route-map.name. |
| **route_map_out**  string | IPv4 outbound route map filter. Source router.route-map.name. |
| **route_map_out6**  string | IPv6 Outbound route map filter. Source router.route-map.name. |
| **route_map_out6_preferable**  string | IPv6 outbound route map filter if the peer is preferred. Source router.route-map.name. |
| **route_map_out_preferable**  string | IPv4 outbound route map filter if the peer is preferred. Source router.route-map.name. |
| **route_map_out_vpnv4**  string | VPNv4 outbound route map filter. Source router.route-map.name. |
| **route_map_out_vpnv4_preferable**  string | VPNv4 outbound route map filter if the peer is preferred. Source router.route-map.name. |
| **route_reflector_client**  string | Enable/disable IPv4 AS route reflector client.  Choices:   - `"enable"` - `"disable"` |
| **route_reflector_client6**  string | Enable/disable IPv6 AS route reflector client.  Choices:   - `"enable"` - `"disable"` |
| **route_reflector_client_vpnv4**  string | Enable/disable VPNv4 AS route reflector client for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **route_server_client**  string | Enable/disable IPv4 AS route server client.  Choices:   - `"enable"` - `"disable"` |
| **route_server_client6**  string | Enable/disable IPv6 AS route server client.  Choices:   - `"enable"` - `"disable"` |
| **route_server_client_vpnv4**  string | Enable/disable VPNv4 AS route server client for this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **send_community**  string | IPv4 Send community attribute to neighbor.  Choices:   - `"standard"` - `"extended"` - `"both"` - `"disable"` |
| **send_community6**  string | IPv6 Send community attribute to neighbor.  Choices:   - `"standard"` - `"extended"` - `"both"` - `"disable"` |
| **send_community_vpnv4**  string | Send community attribute to neighbor for VPNv4 address family.  Choices:   - `"standard"` - `"extended"` - `"both"` - `"disable"` |
| **shutdown**  string | Enable/disable shutdown this neighbor.  Choices:   - `"enable"` - `"disable"` |
| **soft_reconfiguration**  string | Enable/disable allow IPv4 inbound soft reconfiguration.  Choices:   - `"enable"` - `"disable"` |
| **soft_reconfiguration6**  string | Enable/disable allow IPv6 inbound soft reconfiguration.  Choices:   - `"enable"` - `"disable"` |
| **soft_reconfiguration_vpnv4**  string | Enable/disable allow VPNv4 inbound soft reconfiguration.  Choices:   - `"enable"` - `"disable"` |
| **stale_route**  string | Enable/disable stale route after neighbor down.  Choices:   - `"enable"` - `"disable"` |
| **strict_capability_match**  string | Enable/disable strict capability matching.  Choices:   - `"enable"` - `"disable"` |
| **unsuppress_map**  string | IPv4 Route map to selectively unsuppress suppressed routes. Source router.route-map.name. |
| **unsuppress_map6**  string | IPv6 Route map to selectively unsuppress suppressed routes. Source router.route-map.name. |
| **update_source**  string | Interface to use as source IP/IPv6 address of TCP connections. Source system.interface.name. |
| **weight**  integer | Neighbor weight. |
| **neighbor_range**  list / elements=dictionary | BGP neighbor range table. |
| **id**  integer | Neighbor range ID. |
| **max_neighbor_num**  integer | Maximum number of neighbors. |
| **neighbor_group**  string | Neighbor group name. Source router.bgp.neighbor-group.name. |
| **prefix**  string | Neighbor range prefix. |
| **neighbor_range6**  list / elements=dictionary | BGP IPv6 neighbor range table. |
| **id**  integer | IPv6 neighbor range ID. |
| **max_neighbor_num**  integer | Maximum number of neighbors. |
| **neighbor_group**  string | Neighbor group name. Source router.bgp.neighbor-group.name. |
| **prefix6**  string | IPv6 prefix. |
| **network**  list / elements=dictionary | BGP network table. |
| **backdoor**  string | Enable/disable route as backdoor.  Choices:   - `"enable"` - `"disable"` |
| **id**  integer | ID. |
| **network_import_check**  string | Configure insurance of BGP network route existence in IGP.  Choices:   - `"global"` - `"enable"` - `"disable"` |
| **prefix**  string | Network prefix. |
| **route_map**  string | Route map to modify generated route. Source router.route-map.name. |
| **network6**  list / elements=dictionary | BGP IPv6 network table. |
| **backdoor**  string | Enable/disable route as backdoor.  Choices:   - `"enable"` - `"disable"` |
| **id**  integer | ID. |
| **network_import_check**  string | Configure insurance of BGP network route existence in IGP.  Choices:   - `"global"` - `"enable"` - `"disable"` |
| **prefix6**  string | Network IPv6 prefix. |
| **route_map**  string | Route map to modify generated route. Source router.route-map.name. |
| **network_import_check**  string | Enable/disable ensure BGP network route exists in IGP.  Choices:   - `"enable"` - `"disable"` |
| **recursive_inherit_priority**  string | Enable/disable priority inheritance for recursive resolution.  Choices:   - `"enable"` - `"disable"` |
| **recursive_next_hop**  string | Enable/disable recursive resolution of next-hop using BGP route.  Choices:   - `"enable"` - `"disable"` |
| **redistribute**  list / elements=dictionary | BGP IPv4 redistribute table. |
| **name**  string | Distribute list entry name. |
| **route_map**  string | Route map name. Source router.route-map.name. |
| **status**  string | Status.  Choices:   - `"enable"` - `"disable"` |
| **redistribute6**  list / elements=dictionary | BGP IPv6 redistribute table. |
| **name**  string | Distribute list entry name. |
| **route_map**  string | Route map name. Source router.route-map.name. |
| **status**  string | Status.  Choices:   - `"enable"` - `"disable"` |
| **router_id**  string | Router ID. |
| **scan_time**  integer | Background scanner interval (sec), 0 to disable it. |
| **synchronization**  string | Enable/disable only advertise routes from iBGP if routes present in an IGP.  Choices:   - `"enable"` - `"disable"` |
| **tag_resolve_mode**  string | Configure tag-match mode. Resolves BGP routes with other routes containing the same tag.  Choices:   - `"disable"` - `"preferred"` - `"merge"` |
| **vrf**  list / elements=dictionary | BGP VRF leaking table. |
| **export_rt**  list / elements=dictionary | List of export route target. |
| **route_target**  string | Attribute: AA|AA:NN. |
| **import_route_map**  string | Import route map. Source router.route-map.name. |
| **import_rt**  list / elements=dictionary | List of import route target. |
| **route_target**  string | Attribute: AA|AA:NN. |
| **leak_target**  list / elements=dictionary | Target VRF table. |
| **interface**  string | Interface which is used to leak routes to target VRF. Source system.interface.name. |
| **route_map**  string | Route map of VRF leaking. Source router.route-map.name. |
| **vrf**  string | Target VRF ID (0 - 63). |
| **rd**  string | Route Distinguisher: AA|AA:NN. |
| **role**  string | VRF role.  Choices:   - `"standalone"` - `"ce"` - `"pe"` |
| **vrf**  string | Origin VRF ID (0 - 63). |
| **vrf6**  list / elements=dictionary | BGP IPv6 VRF leaking table. |
| **leak_target**  list / elements=dictionary | Target VRF table. |
| **interface**  string | Interface which is used to leak routes to target VRF. Source system.interface.name. |
| **route_map**  string | Route map of VRF leaking. Source router.route-map.name. |
| **vrf**  string | Target VRF ID (0 - 63). |
| **vrf**  string | Origin VRF ID (0 - 63). |
| **vrf_leak**  list / elements=dictionary | BGP VRF leaking table. |
| **target**  list / elements=dictionary | Target VRF table. |
| **interface**  string | Interface which is used to leak routes to target VRF. Source system.interface.name. |
| **route_map**  string | Route map of VRF leaking. Source router.route-map.name. |
| **vrf**  string | Target VRF ID (0 - 31). |
| **vrf**  string | Origin VRF ID (0 - 31). |
| **vrf_leak6**  list / elements=dictionary | BGP IPv6 VRF leaking table. |
| **target**  list / elements=dictionary | Target VRF table. |
| **interface**  string | Interface which is used to leak routes to target VRF. Source system.interface.name. |
| **route_map**  string | Route map of VRF leaking. Source router.route-map.name. |
| **vrf**  string | Target VRF ID (0 - 31). |
| **vrf**  string | Origin VRF ID (0 - 31). |
| **vdom**  string | Virtual domain, among those defined previously. A vdom is a virtual instance of the FortiGate that can be configured and used as a different unit.  Default: `"root"` |

## [Notes](fortios_router_bgp_module.md#id8)

> **Note:**
>
> - Legacy fortiosapi has been deprecated, httpapi is the preferred way to run playbooks

## [Examples](fortios_router_bgp_module.md#id9)

```yaml+jinja
- hosts: fortigates
  collections:
    - fortinet.fortios
  connection: httpapi
  vars:
   vdom: "root"
   ansible_httpapi_use_ssl: yes
   ansible_httpapi_validate_certs: no
   ansible_httpapi_port: 443
  tasks:
  - name: Configure BGP.
    fortios_router_bgp:
      vdom:  "{{ vdom }}"
      router_bgp:
        additional_path: "enable"
        additional_path_select: "2"
        additional_path_select_vpnv4: "2"
        additional_path_select6: "2"
        additional_path_vpnv4: "enable"
        additional_path6: "enable"
        admin_distance:
         -
            distance: "0"
            id:  "11"
            neighbour_prefix: "<your_own_value>"
            route_list: "<your_own_value> (source router.access-list.name)"
        aggregate_address:
         -
            as_set: "enable"
            id:  "16"
            prefix: "<your_own_value>"
            summary_only: "enable"
        aggregate_address6:
         -
            as_set: "enable"
            id:  "21"
            prefix6: "<your_own_value>"
            summary_only: "enable"
        always_compare_med: "enable"
        as: "<your_own_value>"
        bestpath_as_path_ignore: "enable"
        bestpath_cmp_confed_aspath: "enable"
        bestpath_cmp_routerid: "enable"
        bestpath_med_confed: "enable"
        bestpath_med_missing_as_worst: "enable"
        client_to_client_reflection: "enable"
        cluster_id: "<your_own_value>"
        confederation_identifier: "0"
        confederation_peers:
         -
            peer: "<your_own_value>"
        dampening: "enable"
        dampening_max_suppress_time: "60"
        dampening_reachability_half_life: "15"
        dampening_reuse: "750"
        dampening_route_map: "<your_own_value> (source router.route-map.name)"
        dampening_suppress: "2000"
        dampening_unreachability_half_life: "15"
        default_local_preference: "100"
        deterministic_med: "enable"
        distance_external: "20"
        distance_internal: "200"
        distance_local: "200"
        ebgp_multipath: "enable"
        enforce_first_as: "enable"
        fast_external_failover: "enable"
        graceful_end_on_timer: "enable"
        graceful_restart: "enable"
        graceful_restart_time: "120"
        graceful_stalepath_time: "360"
        graceful_update_delay: "120"
        holdtime_timer: "180"
        ibgp_multipath: "enable"
        ignore_optional_capability: "enable"
        keepalive_timer: "60"
        log_neighbour_changes: "enable"
        multipath_recursive_distance: "enable"
        neighbor:
         -
            activate: "enable"
            activate_vpnv4: "enable"
            activate6: "enable"
            additional_path: "send"
            additional_path_vpnv4: "send"
            additional_path6: "send"
            adv_additional_path: "2"
            adv_additional_path_vpnv4: "2"
            adv_additional_path6: "2"
            advertisement_interval: "30"
            allowas_in: "3"
            allowas_in_enable: "enable"
            allowas_in_enable6: "enable"
            allowas_in_vpnv4: "0"
            allowas_in6: "3"
            as_override: "enable"
            as_override6: "enable"
            attribute_unchanged: "as-path"
            attribute_unchanged_vpnv4: "as-path"
            attribute_unchanged6: "as-path"
            bfd: "enable"
            capability_default_originate: "enable"
            capability_default_originate6: "enable"
            capability_dynamic: "enable"
            capability_graceful_restart: "enable"
            capability_graceful_restart_vpnv4: "enable"
            capability_graceful_restart6: "enable"
            capability_orf: "none"
            capability_orf6: "none"
            capability_route_refresh: "enable"
            conditional_advertise:
             -
                advertise_routemap: "<your_own_value> (source router.route-map.name)"
                condition_routemap:
                 -
                    name: "default_name_96 (source router.route-map.name)"
                condition_type: "exist"
            conditional_advertise6:
             -
                advertise_routemap: "<your_own_value> (source router.route-map.name)"
                condition_routemap:
                 -
                    name: "default_name_101 (source router.route-map.name)"
                condition_type: "exist"
            connect_timer: "4294967295"
            default_originate_routemap: "<your_own_value> (source router.route-map.name)"
            default_originate_routemap6: "<your_own_value> (source router.route-map.name)"
            description: "<your_own_value>"
            distribute_list_in: "<your_own_value> (source router.access-list.name)"
            distribute_list_in_vpnv4: "<your_own_value> (source router.access-list.name)"
            distribute_list_in6: "<your_own_value> (source router.access-list6.name)"
            distribute_list_out: "<your_own_value> (source router.access-list.name)"
            distribute_list_out_vpnv4: "<your_own_value> (source router.access-list.name)"
            distribute_list_out6: "<your_own_value> (source router.access-list6.name)"
            dont_capability_negotiate: "enable"
            ebgp_enforce_multihop: "enable"
            ebgp_multihop_ttl: "255"
            filter_list_in: "<your_own_value> (source router.aspath-list.name)"
            filter_list_in6: "<your_own_value> (source router.aspath-list.name)"
            filter_list_out: "<your_own_value> (source router.aspath-list.name)"
            filter_list_out6: "<your_own_value> (source router.aspath-list.name)"
            holdtime_timer: "4294967295"
            interface: "<your_own_value> (source system.interface.name)"
            ip: "<your_own_value>"
            keep_alive_timer: "4294967295"
            link_down_failover: "enable"
            local_as: "<your_own_value>"
            local_as_no_prepend: "enable"
            local_as_replace_as: "enable"
            maximum_prefix: "0"
            maximum_prefix_threshold: "75"
            maximum_prefix_threshold_vpnv4: "75"
            maximum_prefix_threshold6: "75"
            maximum_prefix_vpnv4: "0"
            maximum_prefix_warning_only: "enable"
            maximum_prefix_warning_only_vpnv4: "enable"
            maximum_prefix_warning_only6: "enable"
            maximum_prefix6: "0"
            next_hop_self: "enable"
            next_hop_self_rr: "enable"
            next_hop_self_rr6: "enable"
            next_hop_self_vpnv4: "enable"
            next_hop_self6: "enable"
            override_capability: "enable"
            passive: "enable"
            password: "<your_own_value>"
            prefix_list_in: "<your_own_value> (source router.prefix-list.name)"
            prefix_list_in_vpnv4: "<your_own_value> (source router.prefix-list.name)"
            prefix_list_in6: "<your_own_value> (source router.prefix-list6.name)"
            prefix_list_out: "<your_own_value> (source router.prefix-list.name)"
            prefix_list_out_vpnv4: "<your_own_value> (source router.prefix-list.name)"
            prefix_list_out6: "<your_own_value> (source router.prefix-list6.name)"
            remote_as: "<your_own_value>"
            remove_private_as: "enable"
            remove_private_as_vpnv4: "enable"
            remove_private_as6: "enable"
            restart_time: "0"
            retain_stale_time: "0"
            route_map_in: "<your_own_value> (source router.route-map.name)"
            route_map_in_vpnv4: "<your_own_value> (source router.route-map.name)"
            route_map_in6: "<your_own_value> (source router.route-map.name)"
            route_map_out: "<your_own_value> (source router.route-map.name)"
            route_map_out_preferable: "<your_own_value> (source router.route-map.name)"
            route_map_out_vpnv4: "<your_own_value> (source router.route-map.name)"
            route_map_out_vpnv4_preferable: "<your_own_value> (source router.route-map.name)"
            route_map_out6: "<your_own_value> (source router.route-map.name)"
            route_map_out6_preferable: "<your_own_value> (source router.route-map.name)"
            route_reflector_client: "enable"
            route_reflector_client_vpnv4: "enable"
            route_reflector_client6: "enable"
            route_server_client: "enable"
            route_server_client_vpnv4: "enable"
            route_server_client6: "enable"
            send_community: "standard"
            send_community_vpnv4: "standard"
            send_community6: "standard"
            shutdown: "enable"
            soft_reconfiguration: "enable"
            soft_reconfiguration_vpnv4: "enable"
            soft_reconfiguration6: "enable"
            stale_route: "enable"
            strict_capability_match: "enable"
            unsuppress_map: "<your_own_value> (source router.route-map.name)"
            unsuppress_map6: "<your_own_value> (source router.route-map.name)"
            update_source: "<your_own_value> (source system.interface.name)"
            weight: "4294967295"
        neighbor_group:
         -
            activate: "enable"
            activate_vpnv4: "enable"
            activate6: "enable"
            additional_path: "send"
            additional_path_vpnv4: "send"
            additional_path6: "send"
            adv_additional_path: "2"
            adv_additional_path_vpnv4: "2"
            adv_additional_path6: "2"
            advertisement_interval: "30"
            allowas_in: "3"
            allowas_in_enable: "enable"
            allowas_in_enable6: "enable"
            allowas_in_vpnv4: "0"
            allowas_in6: "3"
            as_override: "enable"
            as_override6: "enable"
            attribute_unchanged: "as-path"
            attribute_unchanged_vpnv4: "as-path"
            attribute_unchanged6: "as-path"
            bfd: "enable"
            capability_default_originate: "enable"
            capability_default_originate6: "enable"
            capability_dynamic: "enable"
            capability_graceful_restart: "enable"
            capability_graceful_restart_vpnv4: "enable"
            capability_graceful_restart6: "enable"
            capability_orf: "none"
            capability_orf6: "none"
            capability_route_refresh: "enable"
            connect_timer: "4294967295"
            default_originate_routemap: "<your_own_value> (source router.route-map.name)"
            default_originate_routemap6: "<your_own_value> (source router.route-map.name)"
            description: "<your_own_value>"
            distribute_list_in: "<your_own_value> (source router.access-list.name)"
            distribute_list_in_vpnv4: "<your_own_value> (source router.access-list.name)"
            distribute_list_in6: "<your_own_value> (source router.access-list6.name)"
            distribute_list_out: "<your_own_value> (source router.access-list.name)"
            distribute_list_out_vpnv4: "<your_own_value> (source router.access-list.name)"
            distribute_list_out6: "<your_own_value> (source router.access-list6.name)"
            dont_capability_negotiate: "enable"
            ebgp_enforce_multihop: "enable"
            ebgp_multihop_ttl: "255"
            filter_list_in: "<your_own_value> (source router.aspath-list.name)"
            filter_list_in6: "<your_own_value> (source router.aspath-list.name)"
            filter_list_out: "<your_own_value> (source router.aspath-list.name)"
            filter_list_out6: "<your_own_value> (source router.aspath-list.name)"
            holdtime_timer: "4294967295"
            interface: "<your_own_value> (source system.interface.name)"
            keep_alive_timer: "4294967295"
            link_down_failover: "enable"
            local_as: "<your_own_value>"
            local_as_no_prepend: "enable"
            local_as_replace_as: "enable"
            maximum_prefix: "0"
            maximum_prefix_threshold: "75"
            maximum_prefix_threshold_vpnv4: "75"
            maximum_prefix_threshold6: "75"
            maximum_prefix_vpnv4: "0"
            maximum_prefix_warning_only: "enable"
            maximum_prefix_warning_only_vpnv4: "enable"
            maximum_prefix_warning_only6: "enable"
            maximum_prefix6: "0"
            name: "default_name_249"
            next_hop_self: "enable"
            next_hop_self_rr: "enable"
            next_hop_self_rr6: "enable"
            next_hop_self_vpnv4: "enable"
            next_hop_self6: "enable"
            override_capability: "enable"
            passive: "enable"
            prefix_list_in: "<your_own_value> (source router.prefix-list.name)"
            prefix_list_in_vpnv4: "<your_own_value> (source router.prefix-list.name)"
            prefix_list_in6: "<your_own_value> (source router.prefix-list6.name)"
            prefix_list_out: "<your_own_value> (source router.prefix-list.name)"
            prefix_list_out_vpnv4: "<your_own_value> (source router.prefix-list.name)"
            prefix_list_out6: "<your_own_value> (source router.prefix-list6.name)"
            remote_as: "<your_own_value>"
            remove_private_as: "enable"
            remove_private_as_vpnv4: "enable"
            remove_private_as6: "enable"
            restart_time: "0"
            retain_stale_time: "0"
            route_map_in: "<your_own_value> (source router.route-map.name)"
            route_map_in_vpnv4: "<your_own_value> (source router.route-map.name)"
            route_map_in6: "<your_own_value> (source router.route-map.name)"
            route_map_out: "<your_own_value> (source router.route-map.name)"
            route_map_out_preferable: "<your_own_value> (source router.route-map.name)"
            route_map_out_vpnv4: "<your_own_value> (source router.route-map.name)"
            route_map_out_vpnv4_preferable: "<your_own_value> (source router.route-map.name)"
            route_map_out6: "<your_own_value> (source router.route-map.name)"
            route_map_out6_preferable: "<your_own_value> (source router.route-map.name)"
            route_reflector_client: "enable"
            route_reflector_client_vpnv4: "enable"
            route_reflector_client6: "enable"
            route_server_client: "enable"
            route_server_client_vpnv4: "enable"
            route_server_client6: "enable"
            send_community: "standard"
            send_community_vpnv4: "standard"
            send_community6: "standard"
            shutdown: "enable"
            soft_reconfiguration: "enable"
            soft_reconfiguration_vpnv4: "enable"
            soft_reconfiguration6: "enable"
            stale_route: "enable"
            strict_capability_match: "enable"
            unsuppress_map: "<your_own_value> (source router.route-map.name)"
            unsuppress_map6: "<your_own_value> (source router.route-map.name)"
            update_source: "<your_own_value> (source system.interface.name)"
            weight: "4294967295"
        neighbor_range:
         -
            id:  "298"
            max_neighbor_num: "0"
            neighbor_group: "<your_own_value> (source router.bgp.neighbor-group.name)"
            prefix: "<your_own_value>"
        neighbor_range6:
         -
            id:  "303"
            max_neighbor_num: "0"
            neighbor_group: "<your_own_value> (source router.bgp.neighbor-group.name)"
            prefix6: "<your_own_value>"
        network:
         -
            backdoor: "enable"
            id:  "309"
            network_import_check: "global"
            prefix: "<your_own_value>"
            route_map: "<your_own_value> (source router.route-map.name)"
        network_import_check: "enable"
        network6:
         -
            backdoor: "enable"
            id:  "316"
            network_import_check: "global"
            prefix6: "<your_own_value>"
            route_map: "<your_own_value> (source router.route-map.name)"
        recursive_inherit_priority: "enable"
        recursive_next_hop: "enable"
        redistribute:
         -
            name: "default_name_323"
            route_map: "<your_own_value> (source router.route-map.name)"
            status: "enable"
        redistribute6:
         -
            name: "default_name_327"
            route_map: "<your_own_value> (source router.route-map.name)"
            status: "enable"
        router_id: "<your_own_value>"
        scan_time: "60"
        synchronization: "enable"
        tag_resolve_mode: "disable"
        vrf:
         -
            export_rt:
             -
                route_target: "<your_own_value>"
            import_route_map: "<your_own_value> (source router.route-map.name)"
            import_rt:
             -
                route_target: "<your_own_value>"
            leak_target:
             -
                interface: "<your_own_value> (source system.interface.name)"
                route_map: "<your_own_value> (source router.route-map.name)"
                vrf: "<your_own_value>"
            rd: "<your_own_value>"
            role: "standalone"
            vrf: "<your_own_value>"
        vrf_leak:
         -
            target:
             -
                interface: "<your_own_value> (source system.interface.name)"
                route_map: "<your_own_value> (source router.route-map.name)"
                vrf: "<your_own_value>"
            vrf: "<your_own_value>"
        vrf_leak6:
         -
            target:
             -
                interface: "<your_own_value> (source system.interface.name)"
                route_map: "<your_own_value> (source router.route-map.name)"
                vrf: "<your_own_value>"
            vrf: "<your_own_value>"
        vrf6:
         -
            leak_target:
             -
                interface: "<your_own_value> (source system.interface.name)"
                route_map: "<your_own_value> (source router.route-map.name)"
                vrf: "<your_own_value>"
            vrf: "<your_own_value>"
```

## [Return Values](fortios_router_bgp_module.md#id10)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **build**  string | Build number of the fortigate image  Returned: always  Sample: `"1547"` |
| **http_method**  string | Last method used to provision the content into FortiGate  Returned: always  Sample: `"PUT"` |
| **http_status**  string | Last result given by FortiGate on last operation applied  Returned: always  Sample: `"200"` |
| **mkey**  string | Master key (id) used in the last call to FortiGate  Returned: success  Sample: `"id"` |
| **name**  string | Name of the table used to fulfill the request  Returned: always  Sample: `"urlfilter"` |
| **path**  string | Path of the table used to fulfill the request  Returned: always  Sample: `"webfilter"` |
| **revision**  string | Internal revision number  Returned: always  Sample: `"17.0.2.10658"` |
| **serial**  string | Serial number of the unit  Returned: always  Sample: `"FGVMEVYYQT3AB5352"` |
| **status**  string | Indication of the operation’s result  Returned: always  Sample: `"success"` |
| **vdom**  string | Virtual domain used  Returned: always  Sample: `"root"` |
| **version**  string | Version of the FortiGate  Returned: always  Sample: `"v5.6.3"` |

### Authors

- Link Zheng (@chillancezen)
- Jie Xue (@JieX19)
- Hongbin Lu (@fgtdev-hblu)
- Frank Shen (@frankshen01)
- Miguel Angel Munoz (@mamunozgonzalez)
- Nicolas Thomas (@thomnico)

### Collection links

[Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection/issues)
[Homepage](https://www.fortinet.com)
[Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortios-collection)
