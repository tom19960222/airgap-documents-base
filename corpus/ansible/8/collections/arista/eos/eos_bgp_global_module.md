---
collection: ansible
version: "8"
title: "arista.eos.eos_bgp_global module – Manages BGP global resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_bgp_global_module.html
fetched_at: 2026-07-28T01:11:00+00:00
---
# arista.eos.eos_bgp_global module – Manages BGP global resource module

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_bgp_global`.

New in arista.eos 1.4.0

- [Synopsis](eos_bgp_global_module.md#synopsis)
- [Parameters](eos_bgp_global_module.md#parameters)
- [Notes](eos_bgp_global_module.md#notes)
- [Examples](eos_bgp_global_module.md#examples)
- [Return Values](eos_bgp_global_module.md#return-values)

## [Synopsis](eos_bgp_global_module.md#id1)

- This module configures and manages the attributes of BGP global on Arista EOS platforms.

Aliases: bgp_global

## [Parameters](eos_bgp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of configurations for BGP global. |
| **access_group**  list / elements=dictionary | ip/ipv6 access list configuration. |
| **acl_name**  string | access list name. |
| **afi**  string | Specify ip/ipv6.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **direction**  string | direction of packets. |
| **aggregate_address**  list / elements=dictionary | Configure aggregate address. |
| **address**  string | ipv4/ipv6 address prefix. |
| **advertise_only**  boolean | Advertise without installing the generated blackhole route in FIB.  **Choices:**   - `false` - `true` |
| **as_set**  boolean | Generate autonomous system set path information.  **Choices:**   - `false` - `true` |
| **attribute_map**  string | Name of the route map used to set the attribute of the aggregate route. |
| **match_map**  string | Name of the route map used to filter the contributors of the aggregate route. |
| **summary_only**  boolean | Filters all more-specific routes from updates.  **Choices:**   - `false` - `true` |
| **as_number**  string | Autonomous system number. |
| **bgp_params**  dictionary | BGP parameters. |
| **additional_paths**  string | BGP additional-paths commands  **Choices:**   - `"install"` - `"send"` - `"receive"` |
| **advertise_inactive**  boolean | Advertise BGP routes even if they are inactive in RIB.  **Choices:**   - `false` - `true` |
| **allowas_in**  dictionary | Allow local-as in updates. |
| **count**  integer | Number of local ASNs allowed in a BGP update. |
| **set**  boolean | When true, it is set.  **Choices:**   - `false` - `true` |
| **always_compare_med**  boolean | BGP Always Compare MED  **Choices:**   - `false` - `true` |
| **asn**  string | AS Number notation.  **Choices:**   - `"asdot"` - `"asplain"` |
| **auto_local_addr**  boolean | Automatically determine the local address to be used for the non-transport AF.  **Choices:**   - `false` - `true` |
| **bestpath**  dictionary | Select the bestpath selection algorithim for BGP routes. |
| **as_path**  string | Select the bestpath selection based on as-path.  **Choices:**   - `"ignore"` - `"multipath_relax"` |
| **ecmp_fast**  boolean | Tie-break BGP paths in a ECMP group based on the order of arrival.  **Choices:**   - `false` - `true` |
| **med**  dictionary | MED attribute |
| **confed**  boolean | MED Confed.  **Choices:**   - `false` - `true` |
| **missing_as_worst**  boolean | MED missing-as-worst.  **Choices:**   - `false` - `true` |
| **skip**  boolean | skip one of the tie breaking rules in the bestpath selection.  **Choices:**   - `false` - `true` |
| **tie_break**  string | Configure the tie-break option for BGP bestpath selection.  **Choices:**   - `"cluster_list_length"` - `"router_id"` |
| **client_to_client**  boolean | client to client configuration.  **Choices:**   - `false` - `true` |
| **cluster_id**  string | Cluster ID of this router acting as a route reflector. |
| **confederation**  dictionary | confederation. |
| **identifier**  string | Confederation identifier. |
| **peers**  string | Confederation peers. |
| **control_plane_filter**  boolean | Control plane filter for BGP.  **Choices:**   - `false` - `true` |
| **convergence**  dictionary | Bgp convergence parameters. |
| **slow_peer**  boolean | Maximum amount of time to wait for slow peers to estabilsh session.  **Choices:**   - `false` - `true` |
| **time**  integer | time in secs |
| **default**  string | Default neighbor configuration commands.  **Choices:**   - `"ipv4_unicast"` - `"ipv6_unicast"` |
| **enforce_first_as**  boolean | Enforce the First AS for EBGP routes(default).  **Choices:**   - `false` - `true` |
| **host_routes**  boolean | BGP host routes configuration.  **Choices:**   - `false` - `true` |
| **labeled_unicast**  string | Labeled Unicast.  **Choices:**   - `"ip"` - `"tunnel"` |
| **listen**  dictionary | BGP listen. |
| **limit**  integer | Set limit on the number of dynamic BGP peers allowed. |
| **range**  dictionary | Subnet Range to be associated with the peer group. |
| **address**  string | Address prefix |
| **peer_group**  dictionary | Name of peer group. |
| **name**  string | name. |
| **peer_filter**  string | Name of peer filter. |
| **remote_as**  string | Neighbor AS number |
| **log_neighbor_changes**  boolean | Log neighbor up/down events.  **Choices:**   - `false` - `true` |
| **missing_policy**  dictionary | Missing policy override configuration commands. |
| **action**  string | Missing policy action options.  **Choices:**   - `"deny"` - `"permit"` - `"deny-in-out"` |
| **direction**  string | Missing policy direction options.  **Choices:**   - `"in"` - `"out"` |
| **monitoring**  boolean | Enable Bgp monitoring for all/specified stations.  **Choices:**   - `false` - `true` |
| **next_hop_unchanged**  boolean | Preserve original nexthop while advertising routes to eBGP peers.  **Choices:**   - `false` - `true` |
| **redistribute_internal**  boolean | Redistribute internal BGP routes.  **Choices:**   - `false` - `true` |
| **route**  string | Configure route-map for route installation. |
| **route_reflector**  dictionary | Configure route reflector options |
| **preserve**  boolean | preserve route attributes, overwriting route-map changes  **Choices:**   - `false` - `true` |
| **set**  boolean | When true route_reflector is set.  **Choices:**   - `false` - `true` |
| **transport**  integer | Configure transport port for TCP session |
| **default_metric**  integer | Default metric. |
| **distance**  dictionary | Define an administrative distance. |
| **external**  integer | distance for external routes. |
| **internal**  integer | distance for internal routes. |
| **local**  integer | distance for local routes. |
| **graceful_restart**  dictionary | Enable graceful restart mode. |
| **restart_time**  integer | Set the max time needed to restart and come back up. |
| **set**  boolean | When true, graceful restart is set.  **Choices:**   - `false` - `true` |
| **stalepath_time**  integer | Set the max time to hold onto restarting peer stale paths. |
| **graceful_restart_helper**  boolean | Enable graceful restart helper mode.  **Choices:**   - `false` - `true` |
| **maximum_paths**  dictionary | Maximum number of equal cost paths. |
| **max_equal_cost_paths**  integer | Value for maximum number of equal cost paths. |
| **max_installed_ecmp_paths**  integer | Value for maximum number of installed ECMP routes. |
| **monitoring**  dictionary | BGP monitoring protocol configuration. |
| **port**  integer | Configure the BGP monitoring protocol port number <1024-65535>. |
| **received**  string | BGP monitoring protocol received route selection.  **Choices:**   - `"post_policy"` - `"pre_policy"` |
| **station**  string | BGP monitoring station configuration. |
| **timestamp**  string | BGP monitoring protocol Per-Peer Header timestamp behavior.  **Choices:**   - `"none"` - `"send_time"` |
| **neighbor**  aliases: neighbors  list / elements=dictionary | Configure routing for a network. |
| **additional_paths**  string | BGP additional-paths commands.  **Choices:**   - `"send"` - `"receive"` |
| **allowas_in**  dictionary | Allow local-as in updates. |
| **count**  integer | Number of local ASNs allowed in a BGP update. |
| **set**  boolean | When true, it is set.  **Choices:**   - `false` - `true` |
| **auto_local_addr**  boolean | Automatically determine the local address to be used for the non-transport AF.  **Choices:**   - `false` - `true` |
| **bfd**  string | Configure BFD fallover for this peer  **Choices:**   - `"enable"` - `"c_bit"` |
| **default_originate**  dictionary | Originate default route to this neighbor. |
| **always**  boolean | Always originate default route to this neighbor.  **Choices:**   - `false` - `true` |
| **route_map**  string | Route map reference. |
| **description**  string | Text describing the neighbor. |
| **dont_capability_negotiate**  boolean | Donot perform Capability Negotiation with this neighbor.  **Choices:**   - `false` - `true` |
| **ebgp_multihop**  dictionary | Allow BGP connections to indirectly connected external peers. |
| **set**  boolean | If true, ttl is not set.  **Choices:**   - `false` - `true` |
| **ttl**  integer | Time-to-live in the range 1-255 hops. |
| **encryption_password**  dictionary | Password to use in computation of MD5 hash. |
| **password**  string | password (up to 80 chars). |
| **type**  integer | Encryption type.  **Choices:**   - `0` - `7` |
| **enforce_first_as**  boolean | Enforce the First AS for EBGP routes(default).  **Choices:**   - `false` - `true` |
| **export_localpref**  integer | Override localpref when exporting to an internal peer. |
| **fall_over**  boolean | Configure BFD protocol options for this peer.  **Choices:**   - `false` - `true` |
| **graceful_restart**  boolean | Enable graceful restart mode.  **Choices:**   - `false` - `true` |
| **graceful_restart_helper**  boolean | Enable graceful restart helper mode.  **Choices:**   - `false` - `true` |
| **idle_restart_timer**  integer | Neighbor idle restart timer. |
| **import_localpref**  integer | Override localpref when importing from an external peer. |
| **link_bandwidth**  dictionary | Enable link bandwidth community for routes to this peer. |
| **auto**  boolean | Enable link bandwidth auto generation for routes from this peer.  **Choices:**   - `false` - `true` |
| **default**  string | Enable link bandwidth default generation for routes from this peer. |
| **set**  boolean | If true, set link bandwidth  **Choices:**   - `false` - `true` |
| **update_delay**  integer | Delay outbound route updates. |
| **local_as**  dictionary | Configure local AS number advertised to peer. |
| **as_number**  string | AS number. |
| **fallback**  boolean | Prefer router AS Number over local AS Number.  **Choices:**   - `false` - `true` |
| **local_v6_addr**  string | The local IPv6 address of the neighbor in A:B:C:D:E:F:G:H format. |
| **maximum_accepted_routes**  dictionary | Maximum number of routes accepted from this peer. |
| **count**  integer | Maximum number of accepted routes (0 means unlimited). |
| **warning_limit**  integer | Maximum number of accepted routes after which a warning is issued. (0 means never warn) |
| **maximum_received_routes**  dictionary | Maximum number of routes received from this peer. |
| **count**  integer | Maximum number of routes (0 means unlimited). |
| **warning_limit**  dictionary | Percentage of maximum-routes at which warning is to be issued. |
| **limit_count**  integer | Number of routes at which to warn. |
| **limit_percent**  integer | Percentage of maximum number of routes at which to warn( 1-100). |
| **warning_only**  boolean | Only warn, no restart, if max route limit exceeded.  **Choices:**   - `false` - `true` |
| **metric_out**  integer | MED value to advertise to peer. |
| **monitoring**  boolean | Enable BGP Monitoring Protocol for this peer.  **Choices:**   - `false` - `true` |
| **neighbor_address**  aliases: peer  string | Neighbor address or peer group. |
| **next_hop_self**  boolean | Always advertise this router address as the BGP next hop  **Choices:**   - `false` - `true` |
| **next_hop_unchanged**  boolean | Preserve original nexthop while advertising routes to eBGP peers.  **Choices:**   - `false` - `true` |
| **next_hop_v6_address**  string | IPv6 next-hop address for the neighbor |
| **out_delay**  integer | Delay outbound route updates. |
| **peer_group**  string | Name of the peer group. |
| **prefix_list**  dictionary | Prefix list reference. |
| **direction**  string | Configure an inbound/outbound prefix-list.  **Choices:**   - `"in"` - `"out"` |
| **name**  string | prefix list name. |
| **remote_as**  string | Neighbor Autonomous System. |
| **remove_private_as**  dictionary | Remove private AS number from updates to this peer. |
| **all**  boolean | Remove private AS number.  **Choices:**   - `false` - `true` |
| **replace_as**  boolean | Replace private AS number with local AS number.  **Choices:**   - `false` - `true` |
| **set**  boolean | If true, set remove_private_as.  **Choices:**   - `false` - `true` |
| **route_map**  dictionary | Route map reference. |
| **direction**  string | Configure an inbound/outbound route-map.  **Choices:**   - `"in"` - `"out"` |
| **name**  string | Route map name. |
| **route_reflector_client**  boolean | Configure peer as a route reflector client.  **Choices:**   - `false` - `true` |
| **route_to_peer**  boolean | Use routing table information to reach the peer.  **Choices:**   - `false` - `true` |
| **send_community**  dictionary | Send community attribute to this neighbor. |
| **community_attribute**  string | Type of community attributes to send to this neighbor. |
| **divide**  string | link-bandwidth divide attribute.  **Choices:**   - `"equal"` - `"ratio"` |
| **link_bandwidth_attribute**  string | cumulative/aggregate attribute to be sent.  **Choices:**   - `"aggregate"` - `"divide"` |
| **set**  boolean | Enable send-community  **Choices:**   - `false` - `true` |
| **speed**  string | Reference link speed in bits/second |
| **sub_attribute**  string | Attribute to be sent to the neighbor.  **Choices:**   - `"extended"` - `"link-bandwidth"` - `"standard"` |
| **shutdown**  boolean | Administratively shut down this neighbor.  **Choices:**   - `false` - `true` |
| **soft_recognition**  string | Configure how to handle routes that fail import.  **Choices:**   - `"all"` - `"None"` |
| **timers**  dictionary | Timers. |
| **holdtime**  integer | Hold time in secs. |
| **keepalive**  integer | Keep Alive Interval in secs. |
| **transport**  dictionary | Configure transport options for TCP session. |
| **connection_mode**  string | Configure connection-mode for TCP session. |
| **remote_port**  integer | Configure BGP peer TCP port to connect to. |
| **ttl**  integer | BGP ttl security check |
| **update_source**  string | Specify the local source interface for peer BGP sessions. |
| **weight**  integer | Weight to assign. |
| **network**  aliases: networks  list / elements=dictionary | Configure routing for a network. |
| **address**  string | address prefix. |
| **route_map**  string | Name of route map. |
| **redistribute**  list / elements=dictionary | Redistribute routes in to BGP. |
| **isis_level**  string | Applicable for isis routes. Specify isis route level.  **Choices:**   - `"level-1"` - `"level-2"` - `"level-1-2"` |
| **ospf_route**  string | ospf route options.  **Choices:**   - `"internal"` - `"external"` - `"nssa_external_1"` - `"nssa_external_2"` |
| **protocol**  string | Routes to be redistributed.  **Choices:**   - `"isis"` - `"ospfv3"` - `"ospf"` - `"attached-host"` - `"connected"` - `"rip"` - `"static"` |
| **route_map**  string | Route map reference. |
| **route_target**  dictionary | Route target. |
| **action**  string | Route action.  **Choices:**   - `"both"` - `"import"` - `"export"` |
| **target**  string | Route Target. |
| **router_id**  string | Router id. |
| **shutdown**  boolean | When true, shut down BGP.  **Choices:**   - `false` - `true` |
| **timers**  dictionary | Timers. |
| **holdtime**  integer | Hold time in secs. |
| **keepalive**  integer | Keep Alive Interval in secs. |
| **ucmp**  dictionary | Configure unequal cost multipathing. |
| **fec**  dictionary | Configure UCMP fec utilization threshold. |
| **clear**  integer | UCMP FEC utilization Clear thresholds. |
| **trigger**  integer | UCMP fec utilization too high threshold. |
| **link_bandwidth**  dictionary | Configure link-bandwidth propagation delay. |
| **mode**  string | UCMP link bandwidth mode  **Choices:**   - `"encoding_weighted"` - `"recursive"` |
| **update_delay**  integer | Link Bandwidth Advertisement delay. |
| **mode**  dictionary | UCMP mode. |
| **nexthops**  integer | Value for total number UCMP nexthops. |
| **set**  boolean | If true, ucmp mode is set to 1.  **Choices:**   - `false` - `true` |
| **update**  dictionary | Configure BGP update generation. |
| **batch_size**  integer | batch size for FIB route acknowledgements. |
| **wait_for**  string | wait for options before converge or synchronize.  **Choices:**   - `"wait_for_convergence"` - `"wait_install"` |
| **vlan**  integer | Configure MAC VRF BGP for single VLAN support. |
| **vlan_aware_bundle**  string | Configure MAC VRF BGP for multiple VLAN support. |
| **vrfs**  list / elements=dictionary | Configure BGP in a VRF. |
| **access_group**  list / elements=dictionary | ip/ipv6 access list configuration. |
| **acl_name**  string | access list name. |
| **afi**  string | Specify ip/ipv6.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **direction**  string | direction of packets. |
| **aggregate_address**  list / elements=dictionary | Configure aggregate address. |
| **address**  string | ipv4/ipv6 address prefix. |
| **advertise_only**  boolean | Advertise without installing the generated blackhole route in FIB.  **Choices:**   - `false` - `true` |
| **as_set**  boolean | Generate autonomous system set path information.  **Choices:**   - `false` - `true` |
| **attribute_map**  string | Name of the route map used to set the attribute of the aggregate route. |
| **match_map**  string | Name of the route map used to filter the contributors of the aggregate route. |
| **summary_only**  boolean | Filters all more-specific routes from updates.  **Choices:**   - `false` - `true` |
| **bgp_params**  dictionary | BGP parameters. |
| **additional_paths**  string | BGP additional-paths commands  **Choices:**   - `"install"` - `"send"` - `"receive"` |
| **advertise_inactive**  boolean | Advertise BGP routes even if they are inactive in RIB.  **Choices:**   - `false` - `true` |
| **allowas_in**  dictionary | Allow local-as in updates. |
| **count**  integer | Number of local ASNs allowed in a BGP update. |
| **set**  boolean | When true, it is set.  **Choices:**   - `false` - `true` |
| **always_compare_med**  boolean | BGP Always Compare MED  **Choices:**   - `false` - `true` |
| **asn**  string | AS Number notation.  **Choices:**   - `"asdot"` - `"asplain"` |
| **auto_local_addr**  boolean | Automatically determine the local address to be used for the non-transport AF.  **Choices:**   - `false` - `true` |
| **bestpath**  dictionary | Select the bestpath selection algorithim for BGP routes. |
| **as_path**  string | Select the bestpath selection based on as-path.  **Choices:**   - `"ignore"` - `"multipath_relax"` |
| **ecmp_fast**  boolean | Tie-break BGP paths in a ECMP group based on the order of arrival.  **Choices:**   - `false` - `true` |
| **med**  dictionary | MED attribute |
| **confed**  boolean | MED Confed.  **Choices:**   - `false` - `true` |
| **missing_as_worst**  boolean | MED missing-as-worst.  **Choices:**   - `false` - `true` |
| **skip**  boolean | skip one of the tie breaking rules in the bestpath selection.  **Choices:**   - `false` - `true` |
| **tie_break**  string | Configure the tie-break option for BGP bestpath selection.  **Choices:**   - `"cluster_list_length"` - `"router_id"` |
| **client_to_client**  boolean | client to client configuration.  **Choices:**   - `false` - `true` |
| **cluster_id**  string | Cluster ID of this router acting as a route reflector. |
| **confederation**  dictionary | confederation. |
| **identifier**  string | Confederation identifier. |
| **peers**  string | Confederation peers. |
| **control_plane_filter**  boolean | Control plane filter for BGP.  **Choices:**   - `false` - `true` |
| **convergence**  dictionary | Bgp convergence parameters. |
| **slow_peer**  boolean | Maximum amount of time to wait for slow peers to estabilsh session.  **Choices:**   - `false` - `true` |
| **time**  integer | time in secs |
| **default**  string | Default neighbor configuration commands.  **Choices:**   - `"ipv4_unicast"` - `"ipv6_unicast"` |
| **enforce_first_as**  boolean | Enforce the First AS for EBGP routes(default).  **Choices:**   - `false` - `true` |
| **host_routes**  boolean | BGP host routes configuration.  **Choices:**   - `false` - `true` |
| **labeled_unicast**  string | Labeled Unicast.  **Choices:**   - `"ip"` - `"tunnel"` |
| **listen**  dictionary | BGP listen. |
| **limit**  integer | Set limit on the number of dynamic BGP peers allowed. |
| **range**  dictionary | Subnet Range to be associated with the peer group. |
| **address**  string | Address prefix |
| **peer_group**  dictionary | Name of peer group. |
| **name**  string | name. |
| **peer_filter**  string | Name of peer filter. |
| **remote_as**  string | Neighbor AS number |
| **log_neighbor_changes**  boolean | Log neighbor up/down events.  **Choices:**   - `false` - `true` |
| **missing_policy**  dictionary | Missing policy override configuration commands. |
| **action**  string | Missing policy action options.  **Choices:**   - `"deny"` - `"permit"` - `"deny-in-out"` |
| **direction**  string | Missing policy direction options.  **Choices:**   - `"in"` - `"out"` |
| **monitoring**  boolean | Enable Bgp monitoring for all/specified stations.  **Choices:**   - `false` - `true` |
| **next_hop_unchanged**  boolean | Preserve original nexthop while advertising routes to eBGP peers.  **Choices:**   - `false` - `true` |
| **redistribute_internal**  boolean | Redistribute internal BGP routes.  **Choices:**   - `false` - `true` |
| **route**  string | Configure route-map for route installation. |
| **route_reflector**  dictionary | Configure route reflector options |
| **preserve**  boolean | preserve route attributes, overwriting route-map changes  **Choices:**   - `false` - `true` |
| **set**  boolean | When true route_reflector is set.  **Choices:**   - `false` - `true` |
| **transport**  integer | Configure transport port for TCP session |
| **default_metric**  integer | Default metric. |
| **distance**  dictionary | Define an administrative distance. |
| **external**  integer | distance for external routes. |
| **internal**  integer | distance for internal routes. |
| **local**  integer | distance for local routes. |
| **graceful_restart**  dictionary | Enable graceful restart mode. |
| **restart_time**  integer | Set the max time needed to restart and come back up. |
| **set**  boolean | When true, graceful restart is set.  **Choices:**   - `false` - `true` |
| **stalepath_time**  integer | Set the max time to hold onto restarting peer stale paths. |
| **graceful_restart_helper**  boolean | Enable graceful restart helper mode.  **Choices:**   - `false` - `true` |
| **maximum_paths**  dictionary | Maximum number of equal cost paths. |
| **max_equal_cost_paths**  integer | Value for maximum number of equal cost paths. |
| **max_installed_ecmp_paths**  integer | Value for maximum number of installed ECMP routes. |
| **neighbor**  aliases: neighbors  list / elements=dictionary | Configure routing for a network. |
| **additional_paths**  string | BGP additional-paths commands.  **Choices:**   - `"send"` - `"receive"` |
| **allowas_in**  dictionary | Allow local-as in updates. |
| **count**  integer | Number of local ASNs allowed in a BGP update. |
| **set**  boolean | When true, it is set.  **Choices:**   - `false` - `true` |
| **auto_local_addr**  boolean | Automatically determine the local address to be used for the non-transport AF.  **Choices:**   - `false` - `true` |
| **bfd**  string | Configure BFD fallover for this peer  **Choices:**   - `"enable"` - `"c_bit"` |
| **default_originate**  dictionary | Originate default route to this neighbor. |
| **always**  boolean | Always originate default route to this neighbor.  **Choices:**   - `false` - `true` |
| **route_map**  string | Route map reference. |
| **description**  string | Text describing the neighbor. |
| **dont_capability_negotiate**  boolean | Donot perform Capability Negotiation with this neighbor.  **Choices:**   - `false` - `true` |
| **ebgp_multihop**  dictionary | Allow BGP connections to indirectly connected external peers. |
| **set**  boolean | If true, ttl is not set.  **Choices:**   - `false` - `true` |
| **ttl**  integer | Time-to-live in the range 1-255 hops. |
| **encryption_password**  dictionary | Password to use in computation of MD5 hash. |
| **password**  string | password (up to 80 chars). |
| **type**  integer | Encryption type.  **Choices:**   - `0` - `7` |
| **enforce_first_as**  boolean | Enforce the First AS for EBGP routes(default).  **Choices:**   - `false` - `true` |
| **export_localpref**  integer | Override localpref when exporting to an internal peer. |
| **fall_over**  boolean | Configure BFD protocol options for this peer.  **Choices:**   - `false` - `true` |
| **graceful_restart**  boolean | Enable graceful restart mode.  **Choices:**   - `false` - `true` |
| **graceful_restart_helper**  boolean | Enable graceful restart helper mode.  **Choices:**   - `false` - `true` |
| **idle_restart_timer**  integer | Neighbor idle restart timer. |
| **import_localpref**  integer | Override localpref when importing from an external peer. |
| **link_bandwidth**  dictionary | Enable link bandwidth community for routes to this peer. |
| **auto**  boolean | Enable link bandwidth auto generation for routes from this peer.  **Choices:**   - `false` - `true` |
| **default**  string | Enable link bandwidth default generation for routes from this peer. |
| **set**  boolean | If true, set link bandwidth  **Choices:**   - `false` - `true` |
| **update_delay**  integer | Delay outbound route updates. |
| **local_as**  dictionary | Configure local AS number advertised to peer. |
| **as_number**  string | AS number. |
| **fallback**  boolean | Prefer router AS Number over local AS Number.  **Choices:**   - `false` - `true` |
| **local_v6_addr**  string | The local IPv6 address of the neighbor in A:B:C:D:E:F:G:H format. |
| **maximum_accepted_routes**  dictionary | Maximum number of routes accepted from this peer. |
| **count**  integer | Maximum number of accepted routes (0 means unlimited). |
| **warning_limit**  integer | Maximum number of accepted routes after which a warning is issued. (0 means never warn) |
| **maximum_received_routes**  dictionary | Maximum number of routes received from this peer. |
| **count**  integer | Maximum number of routes (0 means unlimited). |
| **warning_limit**  dictionary | Percentage of maximum-routes at which warning is to be issued. |
| **limit_count**  integer | Number of routes at which to warn. |
| **limit_percent**  integer | Percentage of maximum number of routes at which to warn( 1-100). |
| **warning_only**  boolean | Only warn, no restart, if max route limit exceeded.  **Choices:**   - `false` - `true` |
| **metric_out**  integer | MED value to advertise to peer. |
| **monitoring**  boolean | Enable BGP Monitoring Protocol for this peer.  **Choices:**   - `false` - `true` |
| **neighbor_address**  aliases: peer  string | Neighbor address or peer group. |
| **next_hop_self**  boolean | Always advertise this router address as the BGP next hop  **Choices:**   - `false` - `true` |
| **next_hop_unchanged**  boolean | Preserve original nexthop while advertising routes to eBGP peers.  **Choices:**   - `false` - `true` |
| **next_hop_v6_address**  string | IPv6 next-hop address for the neighbor |
| **out_delay**  integer | Delay outbound route updates. |
| **peer_group**  string | Name of the peer group. |
| **prefix_list**  dictionary | Prefix list reference. |
| **direction**  string | Configure an inbound/outbound prefix-list.  **Choices:**   - `"in"` - `"out"` |
| **name**  string | prefix list name. |
| **remote_as**  string | Neighbor Autonomous System. |
| **remove_private_as**  dictionary | Remove private AS number from updates to this peer. |
| **all**  boolean | Remove private AS number.  **Choices:**   - `false` - `true` |
| **replace_as**  boolean | Replace private AS number with local AS number.  **Choices:**   - `false` - `true` |
| **set**  boolean | If true, set remove_private_as.  **Choices:**   - `false` - `true` |
| **route_map**  dictionary | Route map reference. |
| **direction**  string | Configure an inbound/outbound route-map.  **Choices:**   - `"in"` - `"out"` |
| **name**  string | Route map name. |
| **route_reflector_client**  boolean | Configure peer as a route reflector client.  **Choices:**   - `false` - `true` |
| **route_to_peer**  boolean | Use routing table information to reach the peer.  **Choices:**   - `false` - `true` |
| **send_community**  dictionary | Send community attribute to this neighbor. |
| **community_attribute**  string | Type of community attributes to send to this neighbor. |
| **divide**  string | link-bandwidth divide attribute.  **Choices:**   - `"equal"` - `"ratio"` |
| **link_bandwidth_attribute**  string | cumulative/aggregate attribute to be sent.  **Choices:**   - `"aggregate"` - `"divide"` |
| **speed**  string | Reference link speed in bits/second |
| **sub_attribute**  string | Attribute to be sent to the neighbor.  **Choices:**   - `"extended"` - `"link-bandwidth"` - `"standard"` |
| **shutdown**  boolean | Administratively shut down this neighbor.  **Choices:**   - `false` - `true` |
| **soft_recognition**  string | Configure how to handle routes that fail import.  **Choices:**   - `"all"` - `"None"` |
| **timers**  dictionary | Timers. |
| **holdtime**  integer | Hold time in secs. |
| **keepalive**  integer | Keep Alive Interval in secs. |
| **transport**  dictionary | Configure transport options for TCP session. |
| **connection_mode**  string | Configure connection-mode for TCP session. |
| **remote_port**  integer | Configure BGP peer TCP port to connect to. |
| **ttl**  integer | BGP ttl security check |
| **update_source**  string | Specify the local source interface for peer BGP sessions. |
| **weight**  integer | Weight to assign. |
| **network**  aliases: networks  list / elements=dictionary | Configure routing for a network. |
| **address**  string | address prefix. |
| **route_map**  string | Name of route map. |
| **redistribute**  list / elements=dictionary | Redistribute routes in to BGP. |
| **isis_level**  string | Applicable for isis routes. Specify isis route level.  **Choices:**   - `"level-1"` - `"level-2"` - `"level-1-2"` |
| **ospf_route**  string | ospf route options.  **Choices:**   - `"internal"` - `"external"` - `"nssa_external_1"` - `"nssa_external_2"` |
| **protocol**  string | Routes to be redistributed.  **Choices:**   - `"isis"` - `"ospfv3"` - `"ospf"` - `"attached-host"` - `"connected"` - `"rip"` - `"static"` |
| **route_map**  string | Route map reference. |
| **route_target**  dictionary | Route target. |
| **action**  string | Route action.  **Choices:**   - `"both"` - `"import"` - `"export"` |
| **imported_route**  boolean | Export routes imported from the same Afi/Safi.  **Choices:**   - `false` - `true` |
| **route_map**  string | Name of a route map. |
| **target**  string | Route Target. |
| **type**  string | Type of address fmaily  **Choices:**   - `"evpn"` - `"vpn-ipv4"` - `"vpn-ipv6"` |
| **router_id**  string | Router id. |
| **shutdown**  boolean | When true, shut down BGP.  **Choices:**   - `false` - `true` |
| **timers**  dictionary | Timers. |
| **holdtime**  integer | Hold time in secs. |
| **keepalive**  integer | Keep Alive Interval in secs. |
| **ucmp**  dictionary | Configure unequal cost multipathing. |
| **fec**  dictionary | Configure UCMP fec utilization threshold. |
| **clear**  integer | UCMP FEC utilization Clear thresholds. |
| **trigger**  integer | UCMP fec utilization too high threshold. |
| **link_bandwidth**  dictionary | Configure link-bandwidth propagation delay. |
| **mode**  string | UCMP link bandwidth mode  **Choices:**   - `"encoding_weighted"` - `"recursive"` - `"update_delay"` |
| **update_delay**  integer | Link Bandwidth Advertisement delay. |
| **mode**  dictionary | UCMP mode. |
| **nexthops**  integer | Value for total number UCMP nexthops. |
| **set**  boolean | If true, ucmp mode is set to 1.  **Choices:**   - `false` - `true` |
| **update**  dictionary | Configure BGP update generation. |
| **batch_size**  integer | batch size for FIB route acknowledgements. |
| **wait_for**  string | wait for options before converge or synchronize.  **Choices:**   - `"wait_for_convergence"` - `"wait_install"` |
| **vrf**  string | VRF name. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the EOS device by executing the command **show running-config | section bgp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  State *purged* removes all the BGP configurations from the target device. Use caution with this state.(‘no router bgp <x>’)  State *deleted* only removes BGP attributes that this modules manages and does not negate the BGP process completely. Thereby, preserving address-family related configurations under BGP context.  Running states *deleted* and *replaced* will result in an error if there are address-family configuration lines present under vrf context that is is to be removed. Please use the [arista.eos.eos_bgp_address_family](eos_bgp_address_family_module.md#ansible-collections-arista-eos-eos-bgp-address-family-module) module for prior cleanup.  Refer to examples for more details.  **Choices:**   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"purged"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](eos_bgp_global_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - This module works with connection `network_cli`. See the [EOS Platform Options](eos_platform_options.md).

## [Examples](eos_bgp_global_module.md#id4)

```yaml+jinja
# Using Merged

# Before state:
# -------------
# veos(config)#show running-config | section bgp
# veos(config)#

- name: Merge provided configuration with device configuration
  arista.eos.eos_bgp_global:
    config:
      as_number: "100"
      bgp_params:
        host_routes: true
        convergence:
          slow_peer: true
          time: 6
        additional_paths: "send"
        log_neighbor_changes: true
      maximum_paths:
        max_equal_cost_paths: 55
      aggregate_address:
        - address: "1.2.1.0/24"
          as_set: true
          match_map: "match01"
        - address: "5.2.1.0/24"
          attribute_map: "attrmatch01"
          advertise_only: true
      redistribute:
        - protocol: "static"
          route_map: "map_static"
        - protocol: "attached-host"
      distance:
        internal: 50
      neighbor:
        - peer: "10.1.3.2"
          allowas_in:
            set: true
          default_originate:
            always: true
          dont_capability_negotiate: true
          export_localpref: 4000
          maximum_received_routes:
            count: 500
            warning_limit:
              limit_percent: 5
          next_hop_unchanged: true
          prefix_list:
            name: "prefix01"
            direction: "out"
        - neighbor_address: "peer1"
          fall_over: true
          link_bandwidth:
            update_delay: 5
          monitoring: true
          send_community:
            community_attribute: "extended"
            sub_attribute: "link-bandwidth"
            link_bandwidth_attribute: "aggregate"
            speed: "600"
      vlan: 5
    state: merged

# Task output:
# ------------
# before: {}
#
# commands:
# - router bgp 100
#   - neighbor 10.1.3.2 allowas-in
#   - neighbor 10.1.3.2 default-originate always
#   - neighbor 10.1.3.2 dont-capability-negotiate
#   - neighbor 10.1.3.2 export-localpref 4000
#   - neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
#   - neighbor 10.1.3.2 next-hop-unchanged
#   - neighbor 10.1.3.2 prefix-list prefix01 out
#   - neighbor peer1 fall-over bfd
#   - neighbor peer1 link-bandwidth update-delay 5
#   - neighbor peer1 monitoring
#   - neighbor peer1 send-community extended link-bandwidth aggregate 600
#   - redistribute static route-map map_static
#   - redistribute attached-host
#   - aggregate-address 1.2.1.0/24 as-set match-map match01
#   - aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
#   - bgp host-routes fib direct-install
#   - bgp convergence slow-peer time 6
#   - bgp additional-paths send any
#   - bgp log-neighbor-changes
#   - maximum-paths 55
#   - distance bgp 50
#   - vlan 5
#
# after:
#     aggregate_address:
#     - address: 1.2.1.0/24
#       as_set: true
#       match_map: match01
#     - address: 5.2.1.0/24
#       advertise_only: true
#       attribute_map: attrmatch01
#     as_number: '100'
#     bgp_params:
#       additional_paths: send
#       convergence:
#         slow_peer: true
#         time: 6
#     distance:
#       external: 50
#       internal: 50
#       local: 50
#     maximum_paths:
#       max_equal_cost_paths: 55
#     neighbor:
#     - fall_over: true
#       link_bandwidth:
#         set: true
#         update_delay: 5
#       maximum_received_routes:
#         count: 12000
#       monitoring: true
#       neighbor_address: peer1
#       peer_group: peer1
#       send_community:
#         community_attribute: extended
#         link_bandwidth_attribute: aggregate
#         speed: '600'
#         sub_attribute: link-bandwidth
#     - allowas_in:
#         count: 3
#       default_originate:
#         always: true
#       dont_capability_negotiate: true
#       export_localpref: 4000
#       maximum_received_routes:
#         count: 500
#         warning_limit:
#           limit_percent: 5
#       neighbor_address: 10.1.3.2
#       next_hop_unchanged: true
#     redistribute:
#     - protocol: static
#       route_map: map_static
#     - protocol: attached-host
#     vlan: 5

# After state:
# ------------
# veos(config)#show running-config | section bgp
# router bgp 100
#    bgp convergence slow-peer time 6
#    distance bgp 50 50 50
#    maximum-paths 55
#    bgp additional-paths send any
#    neighbor peer1 peer group
#    neighbor peer1 link-bandwidth update-delay 5
#    neighbor peer1 fall-over bfd
#    neighbor peer1 monitoring
#    neighbor peer1 send-community extended link-bandwidth aggregate 600
#    neighbor peer1 maximum-routes 12000
#    neighbor 10.1.3.2 export-localpref 4000
#    neighbor 10.1.3.2 next-hop-unchanged
#    neighbor 10.1.3.2 dont-capability-negotiate
#    neighbor 10.1.3.2 allowas-in 3
#    neighbor 10.1.3.2 default-originate always
#    neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
#    aggregate-address 1.2.1.0/24 as-set match-map match01
#    aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
#    redistribute static route-map map_static
#    redistribute attached-host
#    !
#    vlan 5
#    !
#    address-family ipv4
#       neighbor 10.1.3.2 prefix-list prefix01 out

# Using replaced:

# Before state:
# -------------
# veos(config)#show running-config | section bgp
# router bgp 100
#    bgp convergence slow-peer time 6
#    distance bgp 50 50 50
#    maximum-paths 55
#    bgp additional-paths send any
#    neighbor peer1 peer group
#    neighbor peer1 link-bandwidth update-delay 5
#    neighbor peer1 fall-over bfd
#    neighbor peer1 monitoring
#    neighbor peer1 send-community extended link-bandwidth aggregate 600
#    neighbor peer1 maximum-routes 12000
#    neighbor 10.1.3.2 export-localpref 4000
#    neighbor 10.1.3.2 next-hop-unchanged
#    neighbor 10.1.3.2 dont-capability-negotiate
#    neighbor 10.1.3.2 allowas-in 3
#    neighbor 10.1.3.2 default-originate always
#    neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
#    aggregate-address 1.2.1.0/24 as-set match-map match01
#    aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
#    redistribute static route-map map_static
#    redistribute attached-host
#    !
#    vlan 5
#    !
#    address-family ipv4
#       neighbor 10.1.3.2 prefix-list prefix01 out
#    !
#    vrf vrf01
#       route-target import 54:11
#       neighbor 12.1.3.2 dont-capability-negotiate
#       neighbor 12.1.3.2 allowas-in 3
#       neighbor 12.1.3.2 default-originate always
#       neighbor 12.1.3.2 maximum-routes 12000

- name: replace provided configuration with device configuration
  arista.eos.eos_bgp_global:
    config:
      as_number: "100"
      bgp_params:
        host_routes: true
        convergence:
          slow_peer: true
          time: 6
        additional_paths: "send"
        log_neighbor_changes: true
      vrfs:
        - vrf: "vrf01"
          maximum_paths:
            max_equal_cost_paths: 55
          aggregate_address:
            - address: "1.2.1.0/24"
              as_set: true
              match_map: "match01"
            - address: "5.2.1.0/24"
              attribute_map: "attrmatch01"
              advertise_only: true
          redistribute:
            - protocol: "static"
              route_map: "map_static"
            - protocol: "attached-host"
          distance:
            internal: 50
          neighbor:
            - neighbor_address: "10.1.3.2"
              allowas_in:
                set: true
              default_originate:
                always: true
              dont_capability_negotiate: true
              export_localpref: 4000
              maximum_received_routes:
                count: 500
                warning_limit:
                  limit_percent: 5
              next_hop_unchanged: true
              prefix_list:
                name: "prefix01"
                direction: "out"
            - neighbor_address: "peer1"
              fall_over: true
              link_bandwidth:
                update_delay: 5
              monitoring: true
              send_community:
                community_attribute: "extended"
                sub_attribute: "link-bandwidth"
                link_bandwidth_attribute: "aggregate"
                speed: "600"
    state: replaced

# Task output:
# ------------

# before:
#     aggregate_address:
#     - address: 1.2.1.0/24
#       as_set: true
#       match_map: match01
#     - address: 5.2.1.0/24
#       advertise_only: true
#       attribute_map: attrmatch01
#     as_number: '100'
#     bgp_params:
#       additional_paths: send
#       convergence:
#         slow_peer: true
#         time: 6
#     distance:
#       external: 50
#       internal: 50
#       local: 50
#     maximum_paths:
#       max_equal_cost_paths: 55
#     neighbor:
#     - fall_over: true
#       link_bandwidth:
#         set: true
#         update_delay: 5
#       maximum_received_routes:
#         count: 12000
#       monitoring: true
#       neighbor_address: peer1
#       peer_group: peer1
#       send_community:
#         community_attribute: extended
#         link_bandwidth_attribute: aggregate
#         speed: '600'
#         sub_attribute: link-bandwidth
#     - allowas_in:
#         count: 3
#       default_originate:
#         always: true
#       dont_capability_negotiate: true
#       export_localpref: 4000
#       maximum_received_routes:
#         count: 500
#         warning_limit:
#           limit_percent: 5
#       neighbor_address: 10.1.3.2
#       next_hop_unchanged: true
#     redistribute:
#     - protocol: static
#       route_map: map_static
#     - protocol: attached-host
#     vlan: 5
#     vrfs:
#     - neighbor:
#       - allowas_in:
#           count: 3
#         default_originate:
#           always: true
#         dont_capability_negotiate: true
#         maximum_received_routes:
#           count: 12000
#         neighbor_address: 12.1.3.2
#       route_target:
#         action: import
#         target: '54:11'
#       vrf: vrf01
#
# commands:
# - router bgp 100
# - vrf vrf01
# - no route-target import 54:11
# - neighbor 10.1.3.2 allowas-in
# - neighbor 10.1.3.2 default-originate always
# - neighbor 10.1.3.2 dont-capability-negotiate
# - neighbor 10.1.3.2 export-localpref 4000
# - neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
# - neighbor 10.1.3.2 next-hop-unchanged
# - neighbor 10.1.3.2 prefix-list prefix01 out
# - neighbor peer1 fall-over bfd
# - neighbor peer1 link-bandwidth update-delay 5
# - neighbor peer1 monitoring
# - neighbor peer1 send-community extended link-bandwidth aggregate 600
# - no neighbor 12.1.3.2
# - redistribute static route-map map_static
# - redistribute attached-host
# - aggregate-address 1.2.1.0/24 as-set match-map match01
# - aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
# - maximum-paths 55
# - distance bgp 50
# - exit
# - no neighbor peer1 peer group
# - no neighbor peer1 link-bandwidth update-delay 5
# - no neighbor peer1 fall-over bfd
# - no neighbor peer1 monitoring
# - no neighbor peer1 send-community extended link-bandwidth aggregate 600
# - no neighbor peer1 maximum-routes 12000
# - no neighbor 10.1.3.2
# - no redistribute static route-map map_static
# - no redistribute attached-host
# - no aggregate-address 1.2.1.0/24 as-set match-map match01
# - no aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
# - bgp host-routes fib direct-install
# - bgp log-neighbor-changes
# - no distance bgp 50 50 50
# - no maximum-paths 55
# - no vlan 5
#
# after:
#     as_number: '100'
#     bgp_params:
#       additional_paths: send
#       convergence:
#         slow_peer: true
#         time: 6
#     vrfs:
#     - aggregate_address:
#       - address: 1.2.1.0/24
#         as_set: true
#         match_map: match01
#       - address: 5.2.1.0/24
#         advertise_only: true
#         attribute_map: attrmatch01
#       distance:
#         external: 50
#         internal: 50
#         local: 50
#       maximum_paths:
#         max_equal_cost_paths: 55
#       neighbor:
#       - allowas_in:
#           count: 3
#         default_originate:
#           always: true
#         dont_capability_negotiate: true
#         export_localpref: 4000
#         maximum_received_routes:
#           count: 500
#           warning_limit:
#             limit_percent: 5
#         neighbor_address: 10.1.3.2
#         next_hop_unchanged: true
#       redistribute:
#       - protocol: static
#         route_map: map_static
#       - protocol: attached-host
#       vrf: vrf01
#
# After state:
# ------------
# veos(config)#show running-config | section bgp
# router bgp 100
#    bgp convergence slow-peer time 6
#    bgp additional-paths send any
#    !
#    vrf vrf01
#       distance bgp 50 50 50
#       maximum-paths 55
#       neighbor 10.1.3.2 export-localpref 4000
#       neighbor 10.1.3.2 next-hop-unchanged
#       neighbor 10.1.3.2 dont-capability-negotiate
#       neighbor 10.1.3.2 allowas-in 3
#       neighbor 10.1.3.2 default-originate always
#       neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
#       aggregate-address 1.2.1.0/24 as-set match-map match01
#       aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
#       redistribute static route-map map_static
#       redistribute attached-host
#       !
#       address-family ipv4
#          neighbor 10.1.3.2 prefix-list prefix01 out

# Using overridden:
# (Note: Overridden and replaced operations are identitical)

# Before state:
# -------------
# veos(config)#show running-config | section bgp
# router bgp 100
#    bgp convergence slow-peer time 6
#    distance bgp 50 50 50
#    maximum-paths 55
#    bgp additional-paths send any
#    neighbor peer1 peer group
#    neighbor peer1 link-bandwidth update-delay 5
#    neighbor peer1 fall-over bfd
#    neighbor peer1 monitoring
#    neighbor peer1 send-community extended link-bandwidth aggregate 600
#    neighbor peer1 maximum-routes 12000
#    neighbor 10.1.3.2 export-localpref 4000
#    neighbor 10.1.3.2 next-hop-unchanged
#    neighbor 10.1.3.2 dont-capability-negotiate
#    neighbor 10.1.3.2 allowas-in 3
#    neighbor 10.1.3.2 default-originate always
#    neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
#    aggregate-address 1.2.1.0/24 as-set match-map match01
#    aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
#    redistribute static route-map map_static
#    redistribute attached-host
#    !
#    vlan 5
#    !
#    address-family ipv4
#       neighbor 10.1.3.2 prefix-list prefix01 out
#    !
#    vrf vrf01
#       route-target import 54:11
#       neighbor 12.1.3.2 dont-capability-negotiate
#       neighbor 12.1.3.2 allowas-in 3
#       neighbor 12.1.3.2 default-originate always
#       neighbor 12.1.3.2 maximum-routes 12000

- name: override running configuration with configuration
  arista.eos.eos_bgp_global:
    config:
      as_number: "100"
      bgp_params:
        host_routes: true
        convergence:
          slow_peer: true
          time: 6
        additional_paths: "send"
        log_neighbor_changes: true
      vrfs:
        - vrf: "vrf01"
          maximum_paths:
            max_equal_cost_paths: 55
          aggregate_address:
            - address: "1.2.1.0/24"
              as_set: true
              match_map: "match01"
            - address: "5.2.1.0/24"
              attribute_map: "attrmatch01"
              advertise_only: true
          redistribute:
            - protocol: "static"
              route_map: "map_static"
            - protocol: "attached-host"
          distance:
            internal: 50
          neighbor:
            - neighbor_address: "10.1.3.2"
              allowas_in:
                set: true
              default_originate:
                always: true
              dont_capability_negotiate: true
              export_localpref: 4000
              maximum_received_routes:
                count: 500
                warning_limit:
                  limit_percent: 5
              next_hop_unchanged: true
              prefix_list:
                name: "prefix01"
                direction: "out"
            - neighbor_address: "peer1"
              fall_over: true
              link_bandwidth:
                update_delay: 5
              monitoring: true
              send_community:
                community_attribute: "extended"
                sub_attribute: "link-bandwidth"
                link_bandwidth_attribute: "aggregate"
                speed: "600"
    state: overridden

# Task output:
# ------------
# before:
#     aggregate_address:
#     - address: 1.2.1.0/24
#       as_set: true
#       match_map: match01
#     - address: 5.2.1.0/24
#       advertise_only: true
#       attribute_map: attrmatch01
#     as_number: '100'
#     bgp_params:
#       additional_paths: send
#       convergence:
#         slow_peer: true
#         time: 6
#     distance:
#       external: 50
#       internal: 50
#       local: 50
#     maximum_paths:
#       max_equal_cost_paths: 55
#     neighbor:
#     - fall_over: true
#       link_bandwidth:
#         set: true
#         update_delay: 5
#       maximum_received_routes:
#         count: 12000
#       monitoring: true
#       neighbor_address: peer1
#       peer_group: peer1
#       send_community:
#         community_attribute: extended
#         link_bandwidth_attribute: aggregate
#         speed: '600'
#         sub_attribute: link-bandwidth
#     - allowas_in:
#         count: 3
#       default_originate:
#         always: true
#       dont_capability_negotiate: true
#       export_localpref: 4000
#       maximum_received_routes:
#         count: 500
#         warning_limit:
#           limit_percent: 5
#       neighbor_address: 10.1.3.2
#       next_hop_unchanged: true
#     redistribute:
#     - protocol: static
#       route_map: map_static
#     - protocol: attached-host
#     vlan: 5
#     vrfs:
#     - neighbor:
#       - allowas_in:
#           count: 3
#         default_originate:
#           always: true
#         dont_capability_negotiate: true
#         maximum_received_routes:
#           count: 12000
#         neighbor_address: 12.1.3.2
#       route_target:
#         action: import
#         target: '54:11'
#       vrf: vrf01
#
# commands:
# - router bgp 100
# - vrf vrf01
# - no route-target import 54:11
# - neighbor 10.1.3.2 allowas-in
# - neighbor 10.1.3.2 default-originate always
# - neighbor 10.1.3.2 dont-capability-negotiate
# - neighbor 10.1.3.2 export-localpref 4000
# - neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
# - neighbor 10.1.3.2 next-hop-unchanged
# - neighbor 10.1.3.2 prefix-list prefix01 out
# - neighbor peer1 fall-over bfd
# - neighbor peer1 link-bandwidth update-delay 5
# - neighbor peer1 monitoring
# - neighbor peer1 send-community extended link-bandwidth aggregate 600
# - no neighbor 12.1.3.2
# - redistribute static route-map map_static
# - redistribute attached-host
# - aggregate-address 1.2.1.0/24 as-set match-map match01
# - aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
# - maximum-paths 55
# - distance bgp 50
# - exit
# - no neighbor peer1 peer group
# - no neighbor peer1 link-bandwidth update-delay 5
# - no neighbor peer1 fall-over bfd
# - no neighbor peer1 monitoring
# - no neighbor peer1 send-community extended link-bandwidth aggregate 600
# - no neighbor peer1 maximum-routes 12000
# - no neighbor 10.1.3.2
# - no redistribute static route-map map_static
# - no redistribute attached-host
# - no aggregate-address 1.2.1.0/24 as-set match-map match01
# - no aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
# - bgp host-routes fib direct-install
# - bgp log-neighbor-changes
# - no distance bgp 50 50 50
# - no maximum-paths 55
# - no vlan 5
#
# after:
#     as_number: '100'
#     bgp_params:
#       additional_paths: send
#       convergence:
#         slow_peer: true
#         time: 6
#     vrfs:
#     - aggregate_address:
#       - address: 1.2.1.0/24
#         as_set: true
#         match_map: match01
#       - address: 5.2.1.0/24
#         advertise_only: true
#         attribute_map: attrmatch01
#       distance:
#         external: 50
#         internal: 50
#         local: 50
#       maximum_paths:
#         max_equal_cost_paths: 55
#       neighbor:
#       - allowas_in:
#           count: 3
#         default_originate:
#           always: true
#         dont_capability_negotiate: true
#         export_localpref: 4000
#         maximum_received_routes:
#           count: 500
#           warning_limit:
#             limit_percent: 5
#         neighbor_address: 10.1.3.2
#         next_hop_unchanged: true
#       redistribute:
#       - protocol: static
#         route_map: map_static
#       - protocol: attached-host
#       vrf: vrf01
#
# After state:
# ------------
# veos(config)#show running-config | section bgp
# router bgp 100
#    bgp convergence slow-peer time 6
#    bgp additional-paths send any
#    !
#    vrf vrf01
#       distance bgp 50 50 50
#       maximum-paths 55
#       neighbor 10.1.3.2 export-localpref 4000
#       neighbor 10.1.3.2 next-hop-unchanged
#       neighbor 10.1.3.2 dont-capability-negotiate
#       neighbor 10.1.3.2 allowas-in 3
#       neighbor 10.1.3.2 default-originate always
#       neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
#       aggregate-address 1.2.1.0/24 as-set match-map match01
#       aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
#       redistribute static route-map map_static
#       redistribute attached-host
#       !
#       address-family ipv4
#          neighbor 10.1.3.2 prefix-list prefix01 out

# Using deleted:

# Before state:
# -------------
# veos(config)#show running-config | section bgp
# router bgp 100
#    bgp convergence slow-peer time 6
#    bgp additional-paths send any
#    !
#    vrf vrf01
#       distance bgp 50 50 50
#       maximum-paths 55
#       neighbor 10.1.3.2 export-localpref 4000
#       neighbor 10.1.3.2 next-hop-unchanged
#       neighbor 10.1.3.2 dont-capability-negotiate
#       neighbor 10.1.3.2 allowas-in 3
#       neighbor 10.1.3.2 default-originate always
#       neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
#       aggregate-address 1.2.1.0/24 as-set match-map match01
#       aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
#       redistribute static route-map map_static
#       redistribute attached-host
#       !

- name: Delete configuration
  arista.eos.eos_bgp_global:
    config:
      as_number: "100"
    state: deleted

# Task output:
# ------------
# before:
#     as_number: '100'
#     bgp_params:
#       additional_paths: send
#       convergence:
#         slow_peer: true
#         time: 6
#     vrfs:
#     - aggregate_address:
#       - address: 1.2.1.0/24
#         as_set: true
#         match_map: match01
#       - address: 5.2.1.0/24
#         advertise_only: true
#         attribute_map: attrmatch01
#       distance:
#         external: 50
#         internal: 50
#         local: 50
#       maximum_paths:
#         max_equal_cost_paths: 55
#       neighbor:
#       - allowas_in:
#           count: 3
#         default_originate:
#           always: true
#         dont_capability_negotiate: true
#         export_localpref: 4000
#         maximum_received_routes:
#           count: 500
#           warning_limit:
#             limit_percent: 5
#         neighbor_address: 10.1.3.2
#         next_hop_unchanged: true
#       redistribute:
#       - protocol: static
#         route_map: map_static
#       - protocol: attached-host
#       vrf: vrf01
#
# commands:
# - router bgp 100
# - no vrf vrf01
# - no bgp convergence slow-peer time 6
# - no bgp additional-paths send any
#
# after:
#  as_number: '100'

#
# After state:
# ------------
# veos(config)#show running-config | section bgp
# router bgp 100

# Using purged:

# Before state:
# -------------
# veos(config)#show running-config | section bgp
# router bgp 100
#    bgp convergence slow-peer time 6
#    distance bgp 50 50 50
#    maximum-paths 55
#    bgp additional-paths send any
#    neighbor peer1 peer group
#    neighbor peer1 link-bandwidth update-delay 5
#    neighbor peer1 fall-over bfd
#    neighbor peer1 monitoring
#    neighbor peer1 send-community extended link-bandwidth aggregate 600
#    neighbor peer1 maximum-routes 12000
#    neighbor 10.1.3.2 export-localpref 4000
#    neighbor 10.1.3.2 next-hop-unchanged
#    neighbor 10.1.3.2 dont-capability-negotiate
#    neighbor 10.1.3.2 allowas-in 3
#    neighbor 10.1.3.2 default-originate always
#    neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
#    aggregate-address 1.2.1.0/24 as-set match-map match01
#    aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
#    redistribute static route-map map_static
#    redistribute attached-host
#    !
#    vlan 5
#    !
#    address-family ipv4
#       neighbor 10.1.3.2 prefix-list prefix01 out
#    !
#    vrf vrf01
#       route-target import 54:11
#       neighbor 12.1.3.2 dont-capability-negotiate
#       neighbor 12.1.3.2 allowas-in 3
#       neighbor 12.1.3.2 default-originate always
#       neighbor 12.1.3.2 maximum-routes 12000

- name: Purge configuration
  arista.eos.eos_bgp_global:
    config:
      as_number: "100"
    state: purged

# Task output:
# ------------
# before:
#     aggregate_address:
#     - address: 1.2.1.0/24
#       as_set: true
#       match_map: match01
#     - address: 5.2.1.0/24
#       advertise_only: true
#       attribute_map: attrmatch01
#     as_number: '100'
#     bgp_params:
#       additional_paths: send
#       convergence:
#         slow_peer: true
#         time: 6
#     distance:
#       external: 50
#       internal: 50
#       local: 50
#     maximum_paths:
#       max_equal_cost_paths: 55
#     neighbor:
#     - fall_over: true
#       link_bandwidth:
#         set: true
#         update_delay: 5
#       maximum_received_routes:
#         count: 12000
#       monitoring: true
#       neighbor_address: peer1
#       peer_group: peer1
#       send_community:
#         community_attribute: extended
#         link_bandwidth_attribute: aggregate
#         speed: '600'
#         sub_attribute: link-bandwidth
#     - allowas_in:
#         count: 3
#       default_originate:
#         always: true
#       dont_capability_negotiate: true
#       export_localpref: 4000
#       maximum_received_routes:
#         count: 500
#         warning_limit:
#           limit_percent: 5
#       neighbor_address: 10.1.3.2
#       next_hop_unchanged: true
#     redistribute:
#     - protocol: static
#       route_map: map_static
#     - protocol: attached-host
#     vlan: 5
#     vrfs:
#     - neighbor:
#       - allowas_in:
#           count: 3
#         default_originate:
#           always: true
#         dont_capability_negotiate: true
#         maximum_received_routes:
#           count: 12000
#         neighbor_address: 12.1.3.2
#       route_target:
#         action: import
#         target: '54:11'
#       vrf: vrf01
#     "changed": true,
#
# commands:
# - no router bgp 100
#
# after: {}

# After state:
# ------------
# veos(config)#show running-config | section bgp
# veos(config)#

# Using rendered

- name: Render command lines for provided configuration
  arista.eos.eos_bgp_global:
    config:
      as_number: "100"
      bgp_params:
        host_routes: true
        convergence:
          slow_peer: true
          time: 6
        additional_paths: "send"
        log_neighbor_changes: true
      maximum_paths:
        max_equal_cost_paths: 55
      aggregate_address:
        - address: "1.2.1.0/24"
          as_set: true
          match_map: "match01"
        - address: "5.2.1.0/24"
          attribute_map: "attrmatch01"
          advertise_only: true
      redistribute:
        - protocol: "static"
          route_map: "map_static"
        - protocol: "attached-host"
      distance:
        internal: 50
      neighbor:
        - peer: "10.1.3.2"
          allowas_in:
            set: true
          default_originate:
            always: true
          dont_capability_negotiate: true
          export_localpref: 4000
          maximum_received_routes:
            count: 500
            warning_limit:
              limit_percent: 5
          next_hop_unchanged: true
          prefix_list:
            name: "prefix01"
            direction: "out"
        - neighbor_address: "peer1"
          fall_over: true
          link_bandwidth:
            update_delay: 5
          monitoring: true
          send_community:
            community_attribute: "extended"
            sub_attribute: "link-bandwidth"
            link_bandwidth_attribute: "aggregate"
            speed: "600"
      vlan: 5
    state: rendered

# Task output:
# ------------
# rendered:
#   - router bgp 100
#   - neighbor 10.1.3.2 allowas-in
#   - neighbor 10.1.3.2 default-originate always
#   - neighbor 10.1.3.2 dont-capability-negotiate
#   - neighbor 10.1.3.2 export-localpref 4000
#   - neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
#   - neighbor 10.1.3.2 next-hop-unchanged
#   - neighbor 10.1.3.2 prefix-list prefix01 out
#   - neighbor peer1 fall-over bfd
#   - neighbor peer1 link-bandwidth update-delay 5
#   - neighbor peer1 monitoring
#   - neighbor peer1 send-community extended link-bandwidth aggregate 600
#   - redistribute static route-map map_static
#   - redistribute attached-host
#   - aggregate-address 1.2.1.0/24 as-set match-map match01
#   - aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
#   - bgp host-routes fib direct-install
#   - bgp convergence slow-peer time 6
#   - bgp additional-paths send any
#   - bgp log-neighbor-changes
#   - maximum-paths 55
#   - distance bgp 50
#   - vlan 5

# Using parsed

# parsed.cfg
# ----------
# router bgp 100
#    bgp convergence slow-peer time 6
#    distance bgp 50 50 50
#    maximum-paths 55
#    bgp additional-paths send any
#    neighbor peer1 peer group
#    neighbor peer1 link-bandwidth update-delay 5
#    neighbor peer1 fall-over bfd
#    neighbor peer1 monitoring
#    neighbor peer1 send-community extended link-bandwidth aggregate 600
#    neighbor peer1 maximum-routes 12000
#    neighbor 10.1.3.2 export-localpref 4000
#    neighbor 10.1.3.2 next-hop-unchanged
#    neighbor 10.1.3.2 dont-capability-negotiate
#    neighbor 10.1.3.2 allowas-in 3
#    neighbor 10.1.3.2 default-originate always
#    neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
#    aggregate-address 1.2.1.0/24 as-set match-map match01
#    aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
#    redistribute static route-map map_static
#    redistribute attached-host
#    !
#    vlan 5
#    !
#    address-family ipv4
#       neighbor 10.1.3.2 prefix-list prefix01 out
#    !
#    vrf vrf01
#       route-target import 54:11
#       neighbor 12.1.3.2 dont-capability-negotiate
#       neighbor 12.1.3.2 allowas-in 3
#       neighbor 12.1.3.2 default-originate always
#       neighbor 12.1.3.2 maximum-routes 12000

- name: Parse externally provided BGP config
  arista.eos.eos_bgp_global:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output:
# ------------

# parsed:
#     aggregate_address:
#     - address: 1.2.1.0/24
#       as_set: true
#       match_map: match01
#     - address: 5.2.1.0/24
#       advertise_only: true
#       attribute_map: attrmatch01
#     as_number: '100'
#     bgp_params:
#       additional_paths: send
#       convergence:
#         slow_peer: true
#         time: 6
#     distance:
#       external: 50
#       internal: 50
#       local: 50
#     maximum_paths:
#       max_equal_cost_paths: 55
#     neighbor:
#     - fall_over: true
#       link_bandwidth:
#         set: true
#         update_delay: 5
#       maximum_received_routes:
#         count: 12000
#       monitoring: true
#       neighbor_address: peer1
#       peer_group: peer1
#       send_community:
#         community_attribute: extended
#         link_bandwidth_attribute: aggregate
#         speed: '600'
#         sub_attribute: link-bandwidth
#     - allowas_in:
#         count: 3
#       default_originate:
#         always: true
#       dont_capability_negotiate: true
#       export_localpref: 4000
#       maximum_received_routes:
#         count: 500
#         warning_limit:
#           limit_percent: 5
#       neighbor_address: 10.1.3.2
#       next_hop_unchanged: true
#     redistribute:
#     - protocol: static
#       route_map: map_static
#     - protocol: attached-host
#     vlan: 5
#     vrfs:
#     - neighbor:
#       - allowas_in:
#           count: 3
#         default_originate:
#           always: true
#         dont_capability_negotiate: true
#         maximum_received_routes:
#           count: 12000
#         neighbor_address: 12.1.3.2
#       route_target:
#         action: import
#         target: '54:11'
#       vrf: vrf01

# Using gathered

# existing config
# veos(config)#show running-config | section bgp
# router bgp 100
#    bgp convergence slow-peer time 6
#    distance bgp 50 50 50
#    maximum-paths 55
#    bgp additional-paths send any
#    neighbor peer1 peer group
#    neighbor peer1 link-bandwidth update-delay 5
#    neighbor peer1 fall-over bfd
#    neighbor peer1 monitoring
#    neighbor peer1 send-community extended link-bandwidth aggregate 600
#    neighbor peer1 maximum-routes 12000
#    neighbor 10.1.3.2 export-localpref 4000
#    neighbor 10.1.3.2 next-hop-unchanged
#    neighbor 10.1.3.2 dont-capability-negotiate
#    neighbor 10.1.3.2 allowas-in 3
#    neighbor 10.1.3.2 default-originate always
#    neighbor 10.1.3.2 maximum-routes 500 warning-limit 5 percent
#    aggregate-address 1.2.1.0/24 as-set match-map match01
#    aggregate-address 5.2.1.0/24 attribute-map attrmatch01 advertise-only
#    redistribute static route-map map_static
#    redistribute attached-host
#    !
#    vlan 5
#    !
#    address-family ipv4
#       neighbor 10.1.3.2 prefix-list prefix01 out
#    !
#    vrf vrf01
#       route-target import 54:11
#       neighbor 12.1.3.2 dont-capability-negotiate
#       neighbor 12.1.3.2 allowas-in 3
#       neighbor 12.1.3.2 default-originate always
#       neighbor 12.1.3.2 maximum-routes 12000

- name: Gather BGP facts using gathered
  arista.eos.eos_bgp_global:
    state: gathered

# Task output:
# ------------
# gathered:
#     aggregate_address:
#     - address: 1.2.1.0/24
#       as_set: true
#       match_map: match01
#     - address: 5.2.1.0/24
#       advertise_only: true
#       attribute_map: attrmatch01
#     as_number: '100'
#     bgp_params:
#       additional_paths: send
#       convergence:
#         slow_peer: true
#         time: 6
#     distance:
#       external: 50
#       internal: 50
#       local: 50
#     maximum_paths:
#       max_equal_cost_paths: 55
#     neighbor:
#     - fall_over: true
#       link_bandwidth:
#         set: true
#         update_delay: 5
#       maximum_received_routes:
#         count: 12000
#       monitoring: true
#       neighbor_address: peer1
#       peer_group: peer1
#       send_community:
#         community_attribute: extended
#         link_bandwidth_attribute: aggregate
#         speed: '600'
#         sub_attribute: link-bandwidth
#     - allowas_in:
#         count: 3
#       default_originate:
#         always: true
#       dont_capability_negotiate: true
#       export_localpref: 4000
#       maximum_received_routes:
#         count: 500
#         warning_limit:
#           limit_percent: 5
#       neighbor_address: 10.1.3.2
#       next_hop_unchanged: true
#     redistribute:
#     - protocol: static
#       route_map: map_static
#     - protocol: attached-host
#     vlan: 5
#     vrfs:
#     - neighbor:
#       - allowas_in:
#           count: 3
#         default_originate:
#           always: true
#         dont_capability_negotiate: true
#         maximum_received_routes:
#           count: 12000
#         neighbor_address: 12.1.3.2
#       route_target:
#         action: import
#         target: '54:11'
#       vrf: vrf01
```

## [Return Values](eos_bgp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["router bgp 100", "neighbor 10.1.3.2 allowas-in", "neighbor 10.1.3.2 default-originate always", "neighbor 10.1.3.2 dont-capability-negotiate"]` |
| **gathered**  dictionary | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **parsed**  dictionary | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["router bgp 100", "neighbor 10.1.3.2 allowas-in", "neighbor 10.1.3.2 default-originate always", "neighbor 10.1.3.2 dont-capability-negotiate"]` |

### Authors

- Gomathi Selvi Srinivasan (@GomathiselviS)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
