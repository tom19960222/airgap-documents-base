---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_bgp_global module – Manages BGP Global configuration on devices running Juniper JUNOS."
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_bgp_global_module.html
fetched_at: 2026-07-27T17:54:12+00:00
---
# junipernetworks.junos.junos_bgp_global module – Manages BGP Global configuration on devices running Juniper JUNOS.

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_bgp_global_module.md#ansible-collections-junipernetworks-junos-junos-bgp-global-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_bgp_global`.

New in junipernetworks.junos 1.3.0

- [Synopsis](junos_bgp_global_module.md#synopsis)
- [Requirements](junos_bgp_global_module.md#requirements)
- [Parameters](junos_bgp_global_module.md#parameters)
- [Notes](junos_bgp_global_module.md#notes)
- [Examples](junos_bgp_global_module.md#examples)
- [Return Values](junos_bgp_global_module.md#return-values)

## [Synopsis](junos_bgp_global_module.md#id1)

- This module manages global bgp configuration on devices running Juniper JUNOS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_bgp_global_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_bgp_global_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of BGP process configuration. |
| **accept_remote_nexthop**  boolean | Allow import policy to specify a non-directly connected next-hop.  Choices:   - `false` - `true` |
| **add_path_display_ipv4_address**  boolean | Display add-path path-id in IPv4 address format.  Choices:   - `false` - `true` |
| **advertise_bgp_static**  dictionary | Advertise bgp-static routes. |
| **policy**  string | Specify static route advertisement policy. |
| **set**  boolean | Set Advertise bgp-static routes.  Choices:   - `false` - `true` |
| **advertise_external**  dictionary | Advertise best external routes. |
| **conditional**  boolean | Route matches active route upto med-comparison rule.  Choices:   - `false` - `true` |
| **set**  boolean | Set Advertise best external routes.  Choices:   - `false` - `true` |
| **advertise_from_main_vpn_tables**  boolean | Advertise VPN routes from bgp.Xvpn.0 tables in master instance.  Choices:   - `false` - `true` |
| **advertise_inactive**  boolean | Advertise inactive routes.  Choices:   - `false` - `true` |
| **advertise_peer_as**  boolean | Advertise routes received from the same autonomous system.  Choices:   - `false` - `true` |
| **as_number**  string | Specify Autonomous system number. |
| **asdot_notation**  boolean | Enable AS-Dot notation to display true 4 byte AS numbers.  Choices:   - `false` - `true` |
| **authentication_algorithm**  string | Specify authentication algorithm name.  Choices:   - `"aes-128-cmac-96"` - `"hmac-sha-1-96"` - `"md5"` |
| **authentication_key**  string | Specify MD5 authentication key. |
| **authentication_key_chain**  string | Specify authentication key chain name. |
| **bfd_liveness_detection**  dictionary | Bidirectional Forwarding Detection (BFD) options. |
| **authentication**  dictionary | Authentication options. |
| **algorithm**  string | Specify algorithm name.  Choices:   - `"keyed-md5"` - `"keyed-sha-1"` - `"meticulous-keyed-md5"` - `"meticulous-keyed-sha-1"` - `"simple-password"` |
| **key_chain**  string | Specify Key chain name. |
| **loose_check**  boolean | Verify authentication only if authentication is negotiated.  Choices:   - `false` - `true` |
| **detection_time**  dictionary | Specify Detection-time optionss. |
| **threshold**  integer | Specify high detection-time triggering a trap (milliseconds). |
| **holddown_interval**  integer | Specify time to hold the session-UP notification to the client. |
| **minimum_interval**  integer | Specify minimum transmit and receive interval. |
| **minimum_receive_interval**  integer | Specify minimum receive interval. |
| **multiplier**  integer | Specify detection time multiplier. |
| **no_adaptation**  boolean | Disable adaptation.  Choices:   - `false` - `true` |
| **session_mode**  string | BFD single-hop or multihop session-mode.  Choices:   - `"automatic"` - `"multihop"` - `"single-hop"` |
| **transmit_interval**  dictionary | Transmit-interval options. |
| **minimum_interval**  integer | Specify Minimum transmit interval. |
| **threshold**  integer | Specify high transmit interval triggering a trap. |
| **version**  string | Specify BFD protocol version number.  Choices:   - `"0"` - `"1"` - `"automatic"` |
| **bgp_error_tolerance**  dictionary | Handle BGP malformed updates softly. |
| **malformed_route_limit**  integer | Maximum number of malformed routes from a peer. |
| **malformed_update_log_interval**  integer | Time used when logging malformed update. |
| **no_malformed_route_limit**  boolean | Specify no malformed route limit.  Choices:   - `false` - `true` |
| **set**  boolean | Set BGP malformed updates softly.  Choices:   - `false` - `true` |
| **bmp**  dictionary | Specific settings to override the routing-options settings. |
| **monitor**  boolean | Enable/Disable monitoring.  Choices:   - `false` - `true` |
| **route_monitoring**  dictionary | Control route monitoring settings. |
| **none**  boolean | Do not send route montoring messages.  Choices:   - `false` - `true` |
| **post_policy**  boolean | Send post policy route montoring messages.  Choices:   - `false` - `true` |
| **post_policy_exclude_non_eligible**  boolean | Send post policy route montoring messages and exclude unresolved routes, etc.  Choices:   - `false` - `true` |
| **post_policy_exclude_non_feasible**  boolean | Send pre policy route montoring messages and exclude looped routes, etc.  Choices:   - `false` - `true` |
| **pre_policy**  boolean | Send pre policy route montoring messages.  Choices:   - `false` - `true` |
| **cluster_id**  string | Specify cluster identifier. |
| **damping**  boolean | Enable route flap damping.  Choices:   - `false` - `true` |
| **description**  string | Specify text description. |
| **disable**  boolean | Disable BGP.  Choices:   - `false` - `true` |
| **egress_te**  dictionary | Use Egress Peering traffic engineering. |
| **backup_path**  string | The ‘egress-te-backup-paths template’ to use for this peer. |
| **set**  boolean | Set the attribute.  Choices:   - `false` - `true` |
| **egress_te_backup_paths**  dictionary | Backup-path for Egress-TE peer interface failure. |
| **templates**  list / elements=dictionary | Specify Backup-path template. |
| **ip_forward**  dictionary | Use IP-forward backup path for Egress TE. |
| **rti_name**  string | Routing-instance to use as IP forward backup-path. |
| **set**  boolean | Set use IP-forward backup path for Egress TE.  Choices:   - `false` - `true` |
| **path_name**  string / required | Name of Egress-TE backup path. |
| **peers**  list / elements=string | Specify address of BGP peer to use as backup next-hop. |
| **remote_nexthop**  string | Specify address of remote-nexthop to use as backup path. |
| **egress_te_set_segment**  list / elements=dictionary | Configure BGP-Peer-Set segment. |
| **egress_te_backup_segment_label**  integer | BGP-Peer-Set SID label value from static label pool. |
| **label**  integer | Backup segment label value from static label pool. |
| **name**  string / required | The BGP-Peer-Set segment name. |
| **egress_te_sid_stats**  boolean | Create BGP-Peer-SID sensor.  Choices:   - `false` - `true` |
| **enforce_first_as**  boolean | Enforce neighbor AS is the first AS in AS-PATH attribute (EBGP).  Choices:   - `false` - `true` |
| **export**  string | Specify export policy. |
| **forwarding_context**  string | Specify routing-instance used for data-forwarding and transport-session. |
| **graceful_restart**  dictionary | BGP graceful restart options. |
| **disable**  boolean | Disable graceful restart.  Choices:   - `false` - `true` |
| **dont_help_shared_fate_bfd_down**  boolean | Honor BFD-Down(C=0) if GR-restart not in progress.  Choices:   - `false` - `true` |
| **forwarding_state_bit**  dictionary | Control forwarding-state flag negotiation. |
| **as_rr_client**  boolean | As for a route reflector client.  Choices:   - `false` - `true` |
| **from_fib**  boolean | Always use state of associated FIB(s).  Choices:   - `false` - `true` |
| **long_lived**  dictionary | Long-lived graceful restart options. |
| **advertise_to_non_llgr_neighbor**  dictionary | Advertise stale routes to non-LLGR neighbors. |
| **omit_no_export**  boolean | Set Advertise stale routes to non-LLGR neighbors.  Choices:   - `false` - `true` |
| **set**  boolean | Set Advertise stale routes to non-LLGR neighbors.  Choices:   - `false` - `true` |
| **receiver_disable**  boolean | Disable receiver (helper) functionality.  Choices:   - `false` - `true` |
| **restart_time**  integer | Restart time used when negotiating with a peer. |
| **set**  boolean | Set BGP graceful restart options.  Choices:   - `false` - `true` |
| **stale_routes_time**  integer | Maximum time for which stale routes are kept. |
| **groups**  list / elements=dictionary | Specify name of the group. |
| **accept_remote_nexthop**  boolean | Allow import policy to specify a non-directly connected next-hop.  Choices:   - `false` - `true` |
| **add_path_display_ipv4_address**  boolean | Display add-path path-id in IPv4 address format.  Choices:   - `false` - `true` |
| **advertise_bgp_static**  dictionary | Advertise bgp-static routes. |
| **policy**  string | Specify static route advertisement policy. |
| **set**  boolean | Set Advertise bgp-static routes.  Choices:   - `false` - `true` |
| **advertise_external**  dictionary | Advertise best external routes. |
| **conditional**  boolean | Route matches active route upto med-comparison rule.  Choices:   - `false` - `true` |
| **set**  boolean | Set Advertise best external routes.  Choices:   - `false` - `true` |
| **advertise_inactive**  boolean | Advertise inactive routes.  Choices:   - `false` - `true` |
| **advertise_peer_as**  boolean | Advertise routes received from the same autonomous system.  Choices:   - `false` - `true` |
| **allow**  list / elements=string | Configure peer connections for specific networks. |
| **as_override**  boolean | Replace neighbor AS number with our AS number  Choices:   - `false` - `true` |
| **authentication_algorithm**  string | Specify authentication algorithm name.  Choices:   - `"aes-128-cmac-96"` - `"hmac-sha-1-96"` - `"md5"` |
| **authentication_key**  string | Specify MD5 authentication key. |
| **authentication_key_chain**  string | Specify authentication key chain name. |
| **bfd_liveness_detection**  dictionary | Bidirectional Forwarding Detection (BFD) options. |
| **authentication**  dictionary | Authentication options. |
| **algorithm**  string | Specify algorithm name.  Choices:   - `"keyed-md5"` - `"keyed-sha-1"` - `"meticulous-keyed-md5"` - `"meticulous-keyed-sha-1"` - `"simple-password"` |
| **key_chain**  string | Specify Key chain name. |
| **loose_check**  boolean | Verify authentication only if authentication is negotiated.  Choices:   - `false` - `true` |
| **detection_time**  dictionary | Specify Detection-time optionss. |
| **threshold**  integer | Specify high detection-time triggering a trap (milliseconds). |
| **holddown_interval**  integer | Specify time to hold the session-UP notification to the client. |
| **minimum_interval**  integer | Specify minimum transmit and receive interval. |
| **minimum_receive_interval**  integer | Specify minimum receive interval. |
| **multiplier**  integer | Specify detection time multiplier. |
| **no_adaptation**  boolean | Disable adaptation.  Choices:   - `false` - `true` |
| **session_mode**  string | BFD single-hop or multihop session-mode.  Choices:   - `"automatic"` - `"multihop"` - `"single-hop"` |
| **transmit_interval**  dictionary | Transmit-interval options. |
| **minimum_interval**  integer | Specify Minimum transmit interval. |
| **threshold**  integer | Specify high transmit interval triggering a trap. |
| **version**  string | Specify BFD protocol version number.  Choices:   - `"0"` - `"1"` - `"automatic"` |
| **bgp_error_tolerance**  dictionary | Handle BGP malformed updates softly. |
| **malformed_route_limit**  integer | Maximum number of malformed routes from a peer. |
| **malformed_update_log_interval**  integer | Time used when logging malformed update. |
| **no_malformed_route_limit**  boolean | Specify no malformed route limit.  Choices:   - `false` - `true` |
| **set**  boolean | Set BGP malformed updates softly.  Choices:   - `false` - `true` |
| **bmp**  dictionary | Specific settings to override the routing-options settings. |
| **monitor**  boolean | Enable/Disable monitoring.  Choices:   - `false` - `true` |
| **route_monitoring**  dictionary | Control route monitoring settings. |
| **none**  boolean | Do not send route montoring messages.  Choices:   - `false` - `true` |
| **post_policy**  boolean | Send post policy route montoring messages.  Choices:   - `false` - `true` |
| **post_policy_exclude_non_eligible**  boolean | Send post policy route montoring messages and exclude unresolved routes, etc.  Choices:   - `false` - `true` |
| **post_policy_exclude_non_feasible**  boolean | Send pre policy route montoring messages and exclude looped routes, etc.  Choices:   - `false` - `true` |
| **pre_policy**  boolean | Send pre policy route montoring messages.  Choices:   - `false` - `true` |
| **cluster_id**  string | Specify cluster identifier. |
| **damping**  boolean | Enable route flap damping.  Choices:   - `false` - `true` |
| **description**  string | Specify text description. |
| **egress_te**  dictionary | Use Egress Peering traffic engineering. |
| **backup_path**  string | The ‘egress-te-backup-paths template’ to use for this peer. |
| **set**  boolean | Set the attribute.  Choices:   - `false` - `true` |
| **enforce_first_as**  boolean | Enforce neighbor AS is the first AS in AS-PATH attribute (EBGP).  Choices:   - `false` - `true` |
| **export**  string | Specify export policy. |
| **forwarding_context**  string | Specify routing-instance used for data-forwarding and transport-session. |
| **graceful_restart**  dictionary | BGP graceful restart options. |
| **disable**  boolean | Disable graceful restart.  Choices:   - `false` - `true` |
| **dont_help_shared_fate_bfd_down**  boolean | Honor BFD-Down(C=0) if GR-restart not in progress.  Choices:   - `false` - `true` |
| **forwarding_state_bit**  dictionary | Control forwarding-state flag negotiation. |
| **as_rr_client**  boolean | As for a route reflector client.  Choices:   - `false` - `true` |
| **from_fib**  boolean | Always use state of associated FIB(s).  Choices:   - `false` - `true` |
| **long_lived**  dictionary | Long-lived graceful restart options. |
| **advertise_to_non_llgr_neighbor**  dictionary | Advertise stale routes to non-LLGR neighbors. |
| **omit_no_export**  boolean | Set Advertise stale routes to non-LLGR neighbors.  Choices:   - `false` - `true` |
| **set**  boolean | Set Advertise stale routes to non-LLGR neighbors.  Choices:   - `false` - `true` |
| **receiver_disable**  boolean | Disable receiver (helper) functionality.  Choices:   - `false` - `true` |
| **restart_time**  integer | Restart time used when negotiating with a peer. |
| **set**  boolean | Set BGP graceful restart options.  Choices:   - `false` - `true` |
| **stale_routes_time**  integer | Maximum time for which stale routes are kept. |
| **hold_time**  integer | Specify hold time used when negotiating with a peer. |
| **idle_after_switch_over**  dictionary | Stop peer session from coming up after nonstop-routing switch-over. |
| **forever**  boolean | Idle the peer until the user intervenes.  Choices:   - `false` - `true` |
| **timeout**  integer | Specify timeout value, in seconds, for starting peer after switch over. |
| **import**  list / elements=string | Specify import policy. |
| **include_mp_next_hop**  boolean | Include NEXT-HOP attribute in multiprotocol updates.  Choices:   - `false` - `true` |
| **ipsec_sa**  string | Specify IPSec SA name. |
| **keep**  string | Specify how to retain routes in the routing table.  Choices:   - `"all"` - `"none"` |
| **local_address**  string | Specify Address of local end of BGP session. |
| **local_as**  dictionary | Local autonomous system number. |
| **alias**  boolean | Treat this AS as an alias to the system AS.  Choices:   - `false` - `true` |
| **as_num**  string / required | Autonomous system number in plain number or (asdot notation) format. |
| **loops**  integer | Maximum number of times this AS can be in an AS path. |
| **no_prepend_global_as**  boolean | Maximum number of times this AS can be in an AS path.  Choices:   - `false` - `true` |
| **private**  boolean | Hide this local AS in paths learned from this peering.  Choices:   - `false` - `true` |
| **local_interface**  string | Specify Local interface for IPv6 link local EBGP peering. |
| **local_preference**  string | Specify value of LOCAL_PREF path attribute. |
| **log_updown**  boolean | Enable log a message for peer state transitions.  Choices:   - `false` - `true` |
| **metric_out**  dictionary | Specify route metric sent in MED. |
| **igp**  dictionary | Track the IGP metric. |
| **delay_med_update**  boolean | Delay updating MED when IGP metric increases.  Choices:   - `false` - `true` |
| **metric_offset**  integer | Specify metric offset for MED. |
| **set**  boolean | Set track the IGP metric.  Choices:   - `false` - `true` |
| **metric_value**  integer | Specify metric value. |
| **minimum_igp**  dictionary | Track the minimum IGP metric. |
| **metric_offset**  integer | Specify metric offset for MED. |
| **set**  boolean | Set track the minimum IGP metric.  Choices:   - `false` - `true` |
| **mtu_discovery**  boolean | Enable TCP path MTU discovery.  Choices:   - `false` - `true` |
| **multihop**  dictionary | Configure an EBGP multihop session. |
| **no_nexthop_change**  boolean | Do not change next hop to self in advertisements.  Choices:   - `false` - `true` |
| **set**  boolean | Set an EBGP multihop session.  Choices:   - `false` - `true` |
| **ttl**  integer | TTL value for the session. |
| **multipath**  dictionary | Allow load sharing among multiple BGP paths. |
| **disable**  boolean | Disable Multipath.  Choices:   - `false` - `true` |
| **multiple_as**  boolean | Use paths received from different ASs.  Choices:   - `false` - `true` |
| **multiple_as_disable**  boolean | Disable multipath.  Choices:   - `false` - `true` |
| **set**  boolean | Set allow load sharing among multiple BGP paths.  Choices:   - `false` - `true` |
| **name**  string | Specify the name of the group |
| **neighbors**  list / elements=dictionary | Specify list of neighbors. |
| **accept_remote_nexthop**  boolean | Allow import policy to specify a non-directly connected next-hop.  Choices:   - `false` - `true` |
| **add_path_display_ipv4_address**  boolean | Display add-path path-id in IPv4 address format.  Choices:   - `false` - `true` |
| **advertise_bgp_static**  dictionary | Advertise bgp-static routes. |
| **policy**  string | Specify static route advertisement policy. |
| **set**  boolean | Set Advertise bgp-static routes.  Choices:   - `false` - `true` |
| **advertise_external**  dictionary | Advertise best external routes. |
| **conditional**  boolean | Route matches active route upto med-comparison rule.  Choices:   - `false` - `true` |
| **set**  boolean | Set Advertise best external routes.  Choices:   - `false` - `true` |
| **advertise_inactive**  boolean | Advertise inactive routes.  Choices:   - `false` - `true` |
| **advertise_peer_as**  boolean | Advertise routes received from the same autonomous system.  Choices:   - `false` - `true` |
| **as_override**  boolean | Replace neighbor AS number with our AS number  Choices:   - `false` - `true` |
| **authentication_algorithm**  string | Specify authentication algorithm name.  Choices:   - `"aes-128-cmac-96"` - `"hmac-sha-1-96"` - `"md5"` |
| **authentication_key**  string | Specify MD5 authentication key. |
| **authentication_key_chain**  string | Specify authentication key chain name. |
| **bfd_liveness_detection**  dictionary | Bidirectional Forwarding Detection (BFD) options. |
| **authentication**  dictionary | Authentication options. |
| **algorithm**  string | Specify algorithm name.  Choices:   - `"keyed-md5"` - `"keyed-sha-1"` - `"meticulous-keyed-md5"` - `"meticulous-keyed-sha-1"` - `"simple-password"` |
| **key_chain**  string | Specify Key chain name. |
| **loose_check**  boolean | Verify authentication only if authentication is negotiated.  Choices:   - `false` - `true` |
| **detection_time**  dictionary | Specify Detection-time optionss. |
| **threshold**  integer | Specify high detection-time triggering a trap (milliseconds). |
| **holddown_interval**  integer | Specify time to hold the session-UP notification to the client. |
| **minimum_interval**  integer | Specify minimum transmit and receive interval. |
| **minimum_receive_interval**  integer | Specify minimum receive interval. |
| **multiplier**  integer | Specify detection time multiplier. |
| **no_adaptation**  boolean | Disable adaptation.  Choices:   - `false` - `true` |
| **session_mode**  string | BFD single-hop or multihop session-mode.  Choices:   - `"automatic"` - `"multihop"` - `"single-hop"` |
| **transmit_interval**  dictionary | Transmit-interval options. |
| **minimum_interval**  integer | Specify Minimum transmit interval. |
| **threshold**  integer | Specify high transmit interval triggering a trap. |
| **version**  string | Specify BFD protocol version number.  Choices:   - `"0"` - `"1"` - `"automatic"` |
| **bgp_error_tolerance**  dictionary | Handle BGP malformed updates softly. |
| **malformed_route_limit**  integer | Maximum number of malformed routes from a peer. |
| **malformed_update_log_interval**  integer | Time used when logging malformed update. |
| **no_malformed_route_limit**  boolean | Specify no malformed route limit.  Choices:   - `false` - `true` |
| **set**  boolean | Set BGP malformed updates softly.  Choices:   - `false` - `true` |
| **bmp**  dictionary | Specific settings to override the routing-options settings. |
| **monitor**  boolean | Enable/Disable monitoring.  Choices:   - `false` - `true` |
| **route_monitoring**  dictionary | Control route monitoring settings. |
| **none**  boolean | Do not send route montoring messages.  Choices:   - `false` - `true` |
| **post_policy**  boolean | Send post policy route montoring messages.  Choices:   - `false` - `true` |
| **post_policy_exclude_non_eligible**  boolean | Send post policy route montoring messages and exclude unresolved routes, etc.  Choices:   - `false` - `true` |
| **post_policy_exclude_non_feasible**  boolean | Send pre policy route montoring messages and exclude looped routes, etc.  Choices:   - `false` - `true` |
| **pre_policy**  boolean | Send pre policy route montoring messages.  Choices:   - `false` - `true` |
| **cluster_id**  string | Specify cluster identifier. |
| **damping**  boolean | Enable route flap damping.  Choices:   - `false` - `true` |
| **description**  string | Specify neighbor description. |
| **egress_te**  dictionary | Use Egress Peering traffic engineering. |
| **backup_path**  string | The ‘egress-te-backup-paths template’ to use for this peer. |
| **set**  boolean | Set the attribute.  Choices:   - `false` - `true` |
| **enforce_first_as**  boolean | Enforce neighbor AS is the first AS in AS-PATH attribute (EBGP).  Choices:   - `false` - `true` |
| **export**  string | Specify export policy. |
| **forwarding_context**  string | Specify routing-instance used for data-forwarding and transport-session. |
| **graceful_restart**  dictionary | BGP graceful restart options. |
| **disable**  boolean | Disable graceful restart.  Choices:   - `false` - `true` |
| **dont_help_shared_fate_bfd_down**  boolean | Honor BFD-Down(C=0) if GR-restart not in progress.  Choices:   - `false` - `true` |
| **forwarding_state_bit**  dictionary | Control forwarding-state flag negotiation. |
| **as_rr_client**  boolean | As for a route reflector client.  Choices:   - `false` - `true` |
| **from_fib**  boolean | Always use state of associated FIB(s).  Choices:   - `false` - `true` |
| **long_lived**  dictionary | Long-lived graceful restart options. |
| **advertise_to_non_llgr_neighbor**  dictionary | Advertise stale routes to non-LLGR neighbors. |
| **omit_no_export**  boolean | Set Advertise stale routes to non-LLGR neighbors.  Choices:   - `false` - `true` |
| **set**  boolean | Set Advertise stale routes to non-LLGR neighbors.  Choices:   - `false` - `true` |
| **receiver_disable**  boolean | Disable receiver (helper) functionality.  Choices:   - `false` - `true` |
| **restart_time**  integer | Restart time used when negotiating with a peer. |
| **set**  boolean | Set BGP graceful restart options.  Choices:   - `false` - `true` |
| **stale_routes_time**  integer | Maximum time for which stale routes are kept. |
| **hold_time**  integer | Specify hold time used when negotiating with a peer. |
| **idle_after_switch_over**  dictionary | Stop peer session from coming up after nonstop-routing switch-over. |
| **forever**  boolean | Idle the peer until the user intervenes.  Choices:   - `false` - `true` |
| **timeout**  integer | Specify timeout value, in seconds, for starting peer after switch over. |
| **import**  list / elements=string | Specify import policy. |
| **include_mp_next_hop**  boolean | Include NEXT-HOP attribute in multiprotocol updates.  Choices:   - `false` - `true` |
| **ipsec_sa**  string | Specify IPSec SA name. |
| **keep**  string | Specify how to retain routes in the routing table.  Choices:   - `"all"` - `"none"` |
| **local_address**  string | Specify Address of local end of BGP session. |
| **local_as**  dictionary | Local autonomous system number. |
| **alias**  boolean | Treat this AS as an alias to the system AS.  Choices:   - `false` - `true` |
| **as_num**  string / required | Autonomous system number in plain number or (asdot notation) format. |
| **loops**  integer | Maximum number of times this AS can be in an AS path. |
| **no_prepend_global_as**  boolean | Maximum number of times this AS can be in an AS path.  Choices:   - `false` - `true` |
| **private**  boolean | Hide this local AS in paths learned from this peering.  Choices:   - `false` - `true` |
| **local_interface**  string | Specify Local interface for IPv6 link local EBGP peering. |
| **local_preference**  string | Specify value of LOCAL_PREF path attribute. |
| **log_updown**  boolean | Enable log a message for peer state transitions.  Choices:   - `false` - `true` |
| **metric_out**  dictionary | Specify route metric sent in MED. |
| **igp**  dictionary | Track the IGP metric. |
| **delay_med_update**  boolean | Delay updating MED when IGP metric increases.  Choices:   - `false` - `true` |
| **metric_offset**  integer | Specify metric offset for MED. |
| **set**  boolean | Set track the IGP metric.  Choices:   - `false` - `true` |
| **metric_value**  integer | Specify metric value. |
| **minimum_igp**  dictionary | Track the minimum IGP metric. |
| **metric_offset**  integer | Specify metric offset for MED. |
| **set**  boolean | Set track the minimum IGP metric.  Choices:   - `false` - `true` |
| **mtu_discovery**  boolean | Enable TCP path MTU discovery.  Choices:   - `false` - `true` |
| **multihop**  dictionary | Configure an EBGP multihop session. |
| **no_nexthop_change**  boolean | Do not change next hop to self in advertisements.  Choices:   - `false` - `true` |
| **set**  boolean | Set an EBGP multihop session.  Choices:   - `false` - `true` |
| **ttl**  integer | TTL value for the session. |
| **multipath**  dictionary | Allow load sharing among multiple BGP paths. |
| **disable**  boolean | Disable Multipath.  Choices:   - `false` - `true` |
| **multiple_as**  boolean | Use paths received from different ASs.  Choices:   - `false` - `true` |
| **multiple_as_disable**  boolean | Disable multipath.  Choices:   - `false` - `true` |
| **set**  boolean | Set allow load sharing among multiple BGP paths.  Choices:   - `false` - `true` |
| **neighbor_address**  string | Specify neighbor address. |
| **no_advertise_peer_as**  boolean | Allows to not advertise routes received from the same autonomous system.  Choices:   - `false` - `true` |
| **no_aggregator_id**  boolean | Set router ID in aggregator path attribute to 0.  Choices:   - `false` - `true` |
| **no_client_reflect**  boolean | Disable intracluster route redistribution.  Choices:   - `false` - `true` |
| **out_delay**  integer | Specify how long before exporting routes from routing table. |
| **outbound_route_filter**  dictionary | Dynamically negotiated cooperative route filtering. |
| **bgp_orf_cisco_mode**  boolean | Using BGP ORF capability code 130 and Prefix ORF type 128.  Choices:   - `false` - `true` |
| **prefix_based**  dictionary | Prefix-based outbound route filtering. |
| **accept**  dictionary | Honor Prefix-based ORFs from remote peers. |
| **inet**  boolean | Honor IPv4 prefix filters.  Choices:   - `false` - `true` |
| **inet6**  boolean | Honor IPv6 prefix filters.  Choices:   - `false` - `true` |
| **set**  boolean | Set honor Prefix-based ORFs from remote peers.  Choices:   - `false` - `true` |
| **set**  boolean | Set prefix-based outbound route filtering.  Choices:   - `false` - `true` |
| **passive**  boolean | Specify to not send open messages to a peer.  Choices:   - `false` - `true` |
| **peer_as**  string | Specify Autonomous system number in plain number or ‘higher 16bits’.’Lower 16 bits’ format. |
| **preference**  string | Specify preference value. |
| **remove_private**  dictionary | Remove well-known private AS numbers. |
| **all**  boolean | Remove all private AS numbers and do not stop at the first public AS number.  Choices:   - `false` - `true` |
| **all_replace**  boolean | Specify private AS replacement.  Choices:   - `false` - `true` |
| **all_replace_nearest**  boolean | Use closest public AS number to replace a private AS number.  Choices:   - `false` - `true` |
| **no_peer_loop_check**  boolean | Remove peer loop-check.  Choices:   - `false` - `true` |
| **set**  boolean | Remove well-known private AS numbers.  Choices:   - `false` - `true` |
| **rfc6514_compliant_safi129**  boolean | Specify Compliance with RFC6514 SAFI129 format.  Choices:   - `false` - `true` |
| **route_server_client**  boolean | Enable route server client behavior.  Choices:   - `false` - `true` |
| **tcp_aggressive_transmission**  boolean | Enable aggressive transmission of pure TCP ACKs and retransmissions.  Choices:   - `false` - `true` |
| **tcp_mss**  integer | Specify maximum TCP segment size. |
| **traceoptions**  dictionary | Configure trace options for BGP. |
| **file**  dictionary | Specify trace file options. |
| **filename**  string / required | Specify name of file in which to write trace information. |
| **files**  integer | Specify maximum number of trace files. |
| **no_world_readable**  boolean | Don’t allow any user to read the log file.  Choices:   - `false` - `true` |
| **size**  integer | Specify maximum trace file size. |
| **world_readable**  boolean | Allow any user to read the log file.  Choices:   - `false` - `true` |
| **flag**  list / elements=dictionary | Specify tracing parameters. |
| **detail**  boolean | Trace detailed information.  Choices:   - `false` - `true` |
| **disable**  boolean | Disable this trace flag.  Choices:   - `false` - `true` |
| **filter**  dictionary | Filter to apply to this flag. |
| **match_on_prefix**  boolean | Specify filter based on prefix.  Choices:   - `false` - `true` |
| **policy**  string | Specify filter policy. |
| **set**  boolean | Set filter to apply to this flag.  Choices:   - `false` - `true` |
| **name**  string / required | specify event name  Choices:   - `"4byte-as"` - `"add-path"` - `"all"` - `"bfd"` - `"damping"` - `"egress-te"` - `"general"` - `"graceful-restart"` - `"keepalive"` - `"normal"` - `"nsr-synchronization"` - `"open"` - `"packets"` - `"policy"` - `"refresh"` - `"route"` - `"state"` - `"task"` - `"thread-io"` - `"thread-update-io"` - `"timer"` - `"update"` |
| **receive**  boolean | Trace received packets.  Choices:   - `false` - `true` |
| **send**  boolean | Trace transmitted packets.  Choices:   - `false` - `true` |
| **ttl**  integer | Specify TTL value for the single-hop peer. |
| **unconfigured_peer_graceful_restart**  boolean | Specify BGP unconfigured peer graceful restart options.  Choices:   - `false` - `true` |
| **vpn_apply_export**  boolean | Apply BGP export policy when exporting VPN routes.  Choices:   - `false` - `true` |
| **no_advertise_peer_as**  boolean | Allows to not advertise routes received from the same autonomous system.  Choices:   - `false` - `true` |
| **no_aggregator_id**  boolean | Set router ID in aggregator path attribute to 0.  Choices:   - `false` - `true` |
| **no_client_reflect**  boolean | Disable intracluster route redistribution.  Choices:   - `false` - `true` |
| **optimal_route_reflection**  dictionary | Enable optimal route reflection for this client group. |
| **igp_backup**  string | Backup node identifier for this client group. |
| **igp_primary**  string | Primary node identifier for this client group. |
| **out_delay**  integer | Specify how long before exporting routes from routing table. |
| **outbound_route_filter**  dictionary | Dynamically negotiated cooperative route filtering. |
| **bgp_orf_cisco_mode**  boolean | Using BGP ORF capability code 130 and Prefix ORF type 128.  Choices:   - `false` - `true` |
| **prefix_based**  dictionary | Prefix-based outbound route filtering. |
| **accept**  dictionary | Honor Prefix-based ORFs from remote peers. |
| **inet**  boolean | Honor IPv4 prefix filters.  Choices:   - `false` - `true` |
| **inet6**  boolean | Honor IPv6 prefix filters.  Choices:   - `false` - `true` |
| **set**  boolean | Set honor Prefix-based ORFs from remote peers.  Choices:   - `false` - `true` |
| **set**  boolean | Set prefix-based outbound route filtering.  Choices:   - `false` - `true` |
| **passive**  boolean | Specify to not send open messages to a peer.  Choices:   - `false` - `true` |
| **peer_as**  string | Specify Autonomous system number in plain number or ‘higher 16bits’.’Lower 16 bits’ format. |
| **preference**  string | Specify preference value. |
| **remove_private**  dictionary | Remove well-known private AS numbers. |
| **all**  boolean | Remove all private AS numbers and do not stop at the first public AS number.  Choices:   - `false` - `true` |
| **all_replace**  boolean | Specify private AS replacement.  Choices:   - `false` - `true` |
| **all_replace_nearest**  boolean | Use closest public AS number to replace a private AS number.  Choices:   - `false` - `true` |
| **no_peer_loop_check**  boolean | Remove peer loop-check.  Choices:   - `false` - `true` |
| **set**  boolean | Remove well-known private AS numbers.  Choices:   - `false` - `true` |
| **rfc6514_compliant_safi129**  boolean | Specify Compliance with RFC6514 SAFI129 format.  Choices:   - `false` - `true` |
| **route_server_client**  boolean | Enable route server client behavior.  Choices:   - `false` - `true` |
| **tcp_aggressive_transmission**  boolean | Enable aggressive transmission of pure TCP ACKs and retransmissions.  Choices:   - `false` - `true` |
| **tcp_mss**  integer | Specify maximum TCP segment size. |
| **traceoptions**  dictionary | Configure trace options for BGP. |
| **file**  dictionary | Specify trace file options. |
| **filename**  string / required | Specify name of file in which to write trace information. |
| **files**  integer | Specify maximum number of trace files. |
| **no_world_readable**  boolean | Don’t allow any user to read the log file.  Choices:   - `false` - `true` |
| **size**  integer | Specify maximum trace file size. |
| **world_readable**  boolean | Allow any user to read the log file.  Choices:   - `false` - `true` |
| **flag**  list / elements=dictionary | Specify tracing parameters. |
| **detail**  boolean | Trace detailed information.  Choices:   - `false` - `true` |
| **disable**  boolean | Disable this trace flag.  Choices:   - `false` - `true` |
| **filter**  dictionary | Filter to apply to this flag. |
| **match_on_prefix**  boolean | Specify filter based on prefix.  Choices:   - `false` - `true` |
| **policy**  string | Specify filter policy. |
| **set**  boolean | Set filter to apply to this flag.  Choices:   - `false` - `true` |
| **name**  string / required | specify event name  Choices:   - `"4byte-as"` - `"add-path"` - `"all"` - `"bfd"` - `"damping"` - `"egress-te"` - `"general"` - `"graceful-restart"` - `"keepalive"` - `"normal"` - `"nsr-synchronization"` - `"open"` - `"packets"` - `"policy"` - `"refresh"` - `"route"` - `"state"` - `"task"` - `"thread-io"` - `"thread-update-io"` - `"timer"` - `"update"` |
| **receive**  boolean | Trace received packets.  Choices:   - `false` - `true` |
| **send**  boolean | Trace transmitted packets.  Choices:   - `false` - `true` |
| **ttl**  integer | Specify TTL value for the single-hop peer. |
| **type**  string | Specify BGP group type.  Choices:   - `"external"` - `"internal"` |
| **unconfigured_peer_graceful_restart**  boolean | Specify BGP unconfigured peer graceful restart options.  Choices:   - `false` - `true` |
| **vpn_apply_export**  boolean | Apply BGP export policy when exporting VPN routes.  Choices:   - `false` - `true` |
| **hold_time**  integer | Specify hold time used when negotiating with a peer. |
| **holddown_all_stale_labels**  boolean | Hold all BGP stale-labels, facilating make-before-break for new label advertisements.  Choices:   - `false` - `true` |
| **idle_after_switch_over**  dictionary | Stop peer session from coming up after nonstop-routing switch-over. |
| **forever**  boolean | Idle the peer until the user intervenes.  Choices:   - `false` - `true` |
| **timeout**  integer | Specify timeout value, in seconds, for starting peer after switch over. |
| **import**  list / elements=string | Specify import policy. |
| **include_mp_next_hop**  boolean | Include NEXT-HOP attribute in multiprotocol updates.  Choices:   - `false` - `true` |
| **ipsec_sa**  string | Specify IPSec SA name. |
| **keep**  string | Specify how to retain routes in the routing table.  Choices:   - `"all"` - `"none"` |
| **local_address**  string | Specify Address of local end of BGP session. |
| **local_as**  dictionary | Local autonomous system number. |
| **alias**  boolean | Treat this AS as an alias to the system AS.  Choices:   - `false` - `true` |
| **as_num**  string / required | Autonomous system number in plain number or (asdot notation) format. |
| **loops**  integer | Maximum number of times this AS can be in an AS path. |
| **no_prepend_global_as**  boolean | Maximum number of times this AS can be in an AS path.  Choices:   - `false` - `true` |
| **private**  boolean | Hide this local AS in paths learned from this peering.  Choices:   - `false` - `true` |
| **local_interface**  string | Specify Local interface for IPv6 link local EBGP peering. |
| **local_preference**  string | Specify value of LOCAL_PREF path attribute. |
| **log_updown**  boolean | Enable log a message for peer state transitions.  Choices:   - `false` - `true` |
| **loops**  integer | Specify maximum number of times this AS can be in an AS path. |
| **metric_out**  dictionary | Specify route metric sent in MED. |
| **igp**  dictionary | Track the IGP metric. |
| **delay_med_update**  boolean | Delay updating MED when IGP metric increases.  Choices:   - `false` - `true` |
| **metric_offset**  integer | Specify metric offset for MED. |
| **set**  boolean | Set track the IGP metric.  Choices:   - `false` - `true` |
| **metric_value**  integer | Specify metric value. |
| **minimum_igp**  dictionary | Track the minimum IGP metric. |
| **metric_offset**  integer | Specify metric offset for MED. |
| **set**  boolean | Set track the minimum IGP metric.  Choices:   - `false` - `true` |
| **mtu_discovery**  boolean | Enable TCP path MTU discovery.  Choices:   - `false` - `true` |
| **multihop**  dictionary | Configure an EBGP multihop session. |
| **no_nexthop_change**  boolean | Do not change next hop to self in advertisements.  Choices:   - `false` - `true` |
| **set**  boolean | Set an EBGP multihop session.  Choices:   - `false` - `true` |
| **ttl**  integer | TTL value for the session. |
| **multipath**  dictionary | Allow load sharing among multiple BGP paths. |
| **disable**  boolean | Disable Multipath.  Choices:   - `false` - `true` |
| **multiple_as**  boolean | Use paths received from different ASs.  Choices:   - `false` - `true` |
| **multiple_as_disable**  boolean | Disable multipath.  Choices:   - `false` - `true` |
| **set**  boolean | Set allow load sharing among multiple BGP paths.  Choices:   - `false` - `true` |
| **multipath_build_priority**  string | Configure the multipath build priority.  Choices:   - `"low"` - `"medium"` |
| **no_advertise_peer_as**  boolean | Allows to not advertise routes received from the same autonomous system.  Choices:   - `false` - `true` |
| **no_aggregator_id**  boolean | Set router ID in aggregator path attribute to 0.  Choices:   - `false` - `true` |
| **no_client_reflect**  boolean | Disable intracluster route redistribution.  Choices:   - `false` - `true` |
| **no_precision_timers**  boolean | Specify not to use precision timers for scheduling keepalives.  Choices:   - `false` - `true` |
| **out_delay**  integer | Specify how long before exporting routes from routing table. |
| **outbound_route_filter**  dictionary | Dynamically negotiated cooperative route filtering. |
| **bgp_orf_cisco_mode**  boolean | Using BGP ORF capability code 130 and Prefix ORF type 128.  Choices:   - `false` - `true` |
| **prefix_based**  dictionary | Prefix-based outbound route filtering. |
| **accept**  dictionary | Honor Prefix-based ORFs from remote peers. |
| **inet**  boolean | Honor IPv4 prefix filters.  Choices:   - `false` - `true` |
| **inet6**  boolean | Honor IPv6 prefix filters.  Choices:   - `false` - `true` |
| **set**  boolean | Set honor Prefix-based ORFs from remote peers.  Choices:   - `false` - `true` |
| **set**  boolean | Set prefix-based outbound route filtering.  Choices:   - `false` - `true` |
| **output_queue_priority**  dictionary | BGP output queue priority scheduler for updates. |
| **defaults**  dictionary | Map policy’s priority class and BGP output-queue. |
| **high**  dictionary | Assign the ‘high’ priority class to this output-queue. |
| **expedited**  boolean | Expedited queue; highest priority.  Choices:   - `false` - `true` |
| **priority**  integer | Specify output queue priorit. |
| **low**  dictionary | Assign the ‘low’ priority class to this output-queue. |
| **expedited**  boolean | Expedited queue; highest priority.  Choices:   - `false` - `true` |
| **priority**  integer | Specify output queue priorit. |
| **medium**  dictionary | Assign the ‘medium’ priority class to this output-queue. |
| **expedited**  boolean | Expedited queue; highest priority.  Choices:   - `false` - `true` |
| **priority**  integer | Specify output queue priorit. |
| **expedited_update_tokens**  integer | Expedited queue; highest priority for number of tokens. |
| **priority_update_tokens**  list / elements=dictionary | Output queue priority; higher is better. |
| **priority**  integer / required | Specify the priority. |
| **update_tokens**  integer / required | Specify update_tokens. |
| **passive**  boolean | Specify to not send open messages to a peer.  Choices:   - `false` - `true` |
| **path_selection**  dictionary | Configure path selection strategy. |
| **always_compare_med**  boolean | Compare MED on paths from different AS.  Choices:   - `false` - `true` |
| **as_path_ignore**  boolean | Ignore AS path comparison during path selection.  Choices:   - `false` - `true` |
| **cisco_non_deterministic**  boolean | Use Cisco IOS nondeterministic path selection algorithm.  Choices:   - `false` - `true` |
| **external_router_id**  boolean | Compare router ID on BGP externals.  Choices:   - `false` - `true` |
| **l2vpn_use_bgp_rules**  boolean | Use standard BGP rules during L2VPN path selection.  Choices:   - `false` - `true` |
| **med_plus_igp**  dictionary | Add IGP cost to next-hop to MED before comparing MED values. |
| **igp_multiplier**  integer | Specify multiplier for IGP cost to next-hop. |
| **med_multiplier**  integer | Specify Multiplier for MED. |
| **set**  boolean | Set med-plus-igp attribute.  Choices:   - `false` - `true` |
| **peer_as**  string | Specify Autonomous system number in plain number or ‘higher 16bits’.’Lower 16 bits’ format. |
| **precision_timers**  boolean | Use precision timers for scheduling keepalives.  Choices:   - `false` - `true` |
| **preference**  string | Specify preference value. |
| **remove_private**  dictionary | Remove well-known private AS numbers. |
| **all**  boolean | Remove all private AS numbers and do not stop at the first public AS number.  Choices:   - `false` - `true` |
| **all_replace**  boolean | Specify private AS replacement.  Choices:   - `false` - `true` |
| **all_replace_nearest**  boolean | Use closest public AS number to replace a private AS number.  Choices:   - `false` - `true` |
| **no_peer_loop_check**  boolean | Remove peer loop-check.  Choices:   - `false` - `true` |
| **set**  boolean | Remove well-known private AS numbers.  Choices:   - `false` - `true` |
| **rfc6514_compliant_safi129**  boolean | Specify Compliance with RFC6514 SAFI129 format.  Choices:   - `false` - `true` |
| **route_server_client**  boolean | Enable route server client behavior.  Choices:   - `false` - `true` |
| **send_addpath_optimization**  boolean | Enable BGP addpath advertisement optimization.  Choices:   - `false` - `true` |
| **snmp_options**  dictionary | Customize SNMP behaviors specifically for BGP MIBs. |
| **backward_traps_only_from_established**  boolean | Limit traps for backward transitions to only those moving from Established state.  Choices:   - `false` - `true` |
| **emit_inet_address_length_in_oid**  boolean | Emit Length in OID for InetAddress MIB type.  Choices:   - `false` - `true` |
| **sr_preference_override**  string | Replace received segment routing traffic engineering preference value with override value. |
| **stale_labels_holddown_period**  integer | Specify duration (sec) MPLS labels allocated by BGP are kept after they go stale. |
| **tcp_aggressive_transmission**  boolean | Enable aggressive transmission of pure TCP ACKs and retransmissions.  Choices:   - `false` - `true` |
| **tcp_mss**  integer | Specify maximum TCP segment size. |
| **traceoptions**  dictionary | Configure trace options for BGP. |
| **file**  dictionary | Specify trace file options. |
| **filename**  string / required | Specify name of file in which to write trace information. |
| **files**  integer | Specify maximum number of trace files. |
| **no_world_readable**  boolean | Don’t allow any user to read the log file.  Choices:   - `false` - `true` |
| **size**  integer | Specify maximum trace file size. |
| **world_readable**  boolean | Allow any user to read the log file.  Choices:   - `false` - `true` |
| **flag**  list / elements=dictionary | Specify tracing parameters. |
| **detail**  boolean | Trace detailed information.  Choices:   - `false` - `true` |
| **disable**  boolean | Disable this trace flag.  Choices:   - `false` - `true` |
| **filter**  dictionary | Filter to apply to this flag. |
| **match_on_prefix**  boolean | Specify filter based on prefix.  Choices:   - `false` - `true` |
| **policy**  string | Specify filter policy. |
| **set**  boolean | Set filter to apply to this flag.  Choices:   - `false` - `true` |
| **name**  string / required | specify event name  Choices:   - `"4byte-as"` - `"add-path"` - `"all"` - `"bfd"` - `"damping"` - `"egress-te"` - `"general"` - `"graceful-restart"` - `"keepalive"` - `"normal"` - `"nsr-synchronization"` - `"open"` - `"packets"` - `"policy"` - `"refresh"` - `"route"` - `"state"` - `"task"` - `"thread-io"` - `"thread-update-io"` - `"timer"` - `"update"` |
| **receive**  boolean | Trace received packets.  Choices:   - `false` - `true` |
| **send**  boolean | Trace transmitted packets.  Choices:   - `false` - `true` |
| **traffic_statistics_labeled_path**  dictionary | Collect periodic ingress labeled statistics for BGP label-switched paths. |
| **file**  dictionary | Specify statistics file options. |
| **filename**  string | Specify name of file in which to write trace information. |
| **files**  integer | Specify maximum number of trace files. |
| **no_world_readable**  boolean | Don’t allow any user to read the log file.  Choices:   - `false` - `true` |
| **size**  integer | Specify maximum trace file size. |
| **world_readable**  boolean | Allow any user to read the log file.  Choices:   - `false` - `true` |
| **interval**  integer | Specify time interval to collect statistics. |
| **ttl**  integer | Specify TTL value for the single-hop peer. |
| **unconfigured_peer_graceful_restart**  boolean | Specify BGP unconfigured peer graceful restart options.  Choices:   - `false` - `true` |
| **vpn_apply_export**  boolean | Apply BGP export policy when exporting VPN routes.  Choices:   - `false` - `true` |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show protocols bgp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state the configuration should be left in.  State *purged* removes all (routing-options autonomous-system, bgp global, bgp groups, bgp neighbors, bgp family and bgp group and neighbor family) the BGP configurations from the target device. Use caution with this state.  State *deleted* only removes BGP attributes that this modules manages and does not negate the BGP process completely. Thereby, preserving address-family related configurations under BGP context.  Running states *deleted* and *replaced* will result in an error if there are address-family configuration lines present under a neighbor.Please use the [junipernetworks.junos.junos_bgp_address_family](junos_bgp_address_family_module.md#ansible-collections-junipernetworks-junos-junos-bgp-address-family-module) modules for prior cleanup.  Refer to examples for more details.  Choices:   - `"purged"` - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](junos_bgp_global_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - Tested against JunOS v18.4R1

## [Examples](junos_bgp_global_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# admin# show protocols bgp
# [edit]

# admin# show routing-options autonomous-system
# [edit]

- name: Merge Junos BGP config
  junipernetworks.junos.junos_bgp_global:
    config:
      as_number: "65534"
      loops: 3
      asdot_notation: true
      accept_remote_nexthop: true
      add_path_display_ipv4_address: true
      advertise_bgp_static:
        policy: "static-to-bgp"
      advertise_from_main_vpn_tables: true
      advertise_inactive: true
      authentication_algorithm: "md5"
      bgp_error_tolerance:
        malformed_route_limit: 20000000
      bmp:
        monitor: true
      damping: true
      description: "This is configured with Junos_bgp resource module"
      egress_te_sid_stats: true
      hold_time: 5
      holddown_all_stale_labels: true
      include_mp_next_hop: true
      log_updown: true
      no_advertise_peer_as: true
      no_aggregator_id: true
      no_client_reflect: true
      out_delay: 10
      precision_timers: true
      preference: 2
    state: merged

# After state
# -----------
#
# admin# show routing-options autonomous-system
# 65534 loops 3 asdot-notation;

# admin# show protocols bgp
# precision-timers;
# advertise-from-main-vpn-tables;
# holddown-all-stale-labels;
# description "This is configured with Junos_bgp resource module";
# accept-remote-nexthop;
# preference 2;
# hold-time 5;
# advertise-inactive;
# no-advertise-peer-as;
# no-aggregator-id;
# out-delay 10;
# log-updown;
# damping;
# bgp-error-tolerance {
#     malformed-route-limit 20000000;
# }
# authentication-algorithm md5;
# no-client-reflect;
# include-mp-next-hop;
# bmp {
#     monitor enable;
# }
# advertise-bgp-static {
#     policy static-to-bgp;
# }
# add-path-display-ipv4-address;
# egress-te-sid-stats;

# Using merged
#
# Before state
# ------------
#
# admin# show routing-options autonomous-system
# 65534 loops 3 asdot-notation;

# admin# show protocols bgp
# precision-timers;
# advertise-from-main-vpn-tables;
# holddown-all-stale-labels;
# description "This is configured with Junos_bgp resource module";
# accept-remote-nexthop;
# preference 2;
# hold-time 5;
# advertise-inactive;
# no-advertise-peer-as;
# no-aggregator-id;
# out-delay 10;
# log-updown;
# damping;
# bgp-error-tolerance {
#     malformed-route-limit 20000000;
# }
# authentication-algorithm md5;
# no-client-reflect;
# include-mp-next-hop;
# bmp {
#     monitor enable;
# }
# advertise-bgp-static {
#     policy static-to-bgp;
# }
# add-path-display-ipv4-address;
# egress-te-sid-stats;

- name: Update running Junos BGP config
  junipernetworks.junos.junos_bgp_global:
    config:
      egress_te_backup_paths:
        templates:
          - path_name: customer1
            peers:
              - '11.11.11.11'
              - '11.11.11.12'
              - '11.11.11.13'
            remote_nexthop: '2.2.2.2'
      groups:
        - name: 'internal'
          type: 'internal'
          vpn_apply_export: true
          out_delay: 30
          accept_remote_nexthop: true
          add_path_display_ipv4_address: true
          peer_as: '65534'
          allow:
            - 'all'
            - '1.1.1.0/24'
          neighbors:
            - neighbor_address: '11.11.11.11'
              peer_as: '65534'
              out_delay: 11
            - neighbor_address: '11.11.11.12'
              peer_as: '65534'
              out_delay: 12

        - name: 'external'
          out_delay: 20
          peer_as: '65534'
          accept_remote_nexthop: true
          add_path_display_ipv4_address: true
          neighbors:
            - neighbor_address: '12.12.12.12'
              peer_as: '65534'
              out_delay: 21
              accept_remote_nexthop: true
              add_path_display_ipv4_address: true
            - neighbor_address: '11.11.11.13'
              peer_as: '65534'
              out_delay: 31
              accept_remote_nexthop: true
              add_path_display_ipv4_address: true
    state: merged

# After state
# -----------
#
# admin# show routing-options autonomous-system
# 65534 loops 3 asdot-notation;

# admin# show protocols bgp
# precision-timers;
# advertise-from-main-vpn-tables;
# holddown-all-stale-labels;
# egress-te-backup-paths {
#     template customer1 {
#         peer 11.11.11.11;
#         peer 11.11.11.12;
#         peer 11.11.11.13;
#         remote-nexthop {
#             2.2.2.2;
#         }
#     }
# }
# description "This is configured with Junos_bgp resource module";
# accept-remote-nexthop;
# preference 2;
# hold-time 5;
# advertise-inactive;
# no-advertise-peer-as;
# no-aggregator-id;
# out-delay 10;
# log-updown;
# damping;
# bgp-error-tolerance {
#     malformed-route-limit 20000000;
# }
# authentication-algorithm md5;
# no-client-reflect;
# include-mp-next-hop;
# bmp {
#     monitor enable;
# }
# add-path-display-ipv4-address;
# egress-te-sid-stats;
# group internal {
#     type internal;
#     accept-remote-nexthop;
#     out-delay 30;
#     vpn-apply-export;
#     peer-as 65534;
#     add-path-display-ipv4-address;
#     allow [ 0.0.0.0/0 1.1.1.0/24 ];
#     neighbor 11.11.11.11 {
#         out-delay 11;
#         peer-as 65534;
#     }
#     neighbor 11.11.11.12 {
#         out-delay 12;
#         peer-as 65534;
#     }
# }
# group external {
#     accept-remote-nexthop;
#     out-delay 20;
#     peer-as 65534;
#     add-path-display-ipv4-address;
#     neighbor 12.12.12.12 {
#         accept-remote-nexthop;
#         out-delay 21;
#         peer-as 65534;
#         add-path-display-ipv4-address;
#     }
#     neighbor 11.11.11.13 {
#         accept-remote-nexthop;
#         out-delay 31;
#         peer-as 65534;
#         add-path-display-ipv4-address;
#     }
# }

# Using replaced
#
# Before state
# ------------
#
# admin# show routing-options autonomous-system
# [edit]
# admin# show protocols bgp
# precision-timers;
# advertise-from-main-vpn-tables;
# holddown-all-stale-labels;
# description "This is configured with Junos_bgp resource module";
# accept-remote-nexthop;
# preference 2;
# hold-time 5;
# advertise-inactive;
# no-advertise-peer-as;
# no-aggregator-id;
# out-delay 10;
# log-updown;
# damping;
# bgp-error-tolerance {
#     malformed-route-limit 20000000;
# }
# authentication-algorithm md5;
# no-client-reflect;
# include-mp-next-hop;
# bmp {
#     monitor enable;
# }
# advertise-bgp-static {
#     policy static-to-bgp;
# }
# add-path-display-ipv4-address;
# egress-te-sid-stats;

- name: Replace Junos BGP global config
  junipernetworks.junos.junos_bgp_global:
   config:
     advertise_bgp_static:
       policy: "static-to-bgp"
     advertise_inactive: true
     authentication_algorithm: "md5"
     bfd_liveness_detection:
       minimum_receive_interval: 8
       multiplier: 30
       no_adaptation: true
       transmit_interval:
         minimum_interval: 4
       version: "automatic"
     bgp_error_tolerance:
       malformed_route_limit: 40000000
     description: "This is configured with Junos_bgp resource module replace"
     egress_te_sid_stats: true
     hold_time: 5
     out_delay: 10
     preference: "2"
   state: replaced

# After state
# -----------
#
# admin# show protocols bgp
# description "This is configured with Junos_bgp resource module replace";
# preference 2;
# hold-time 5;
# advertise-inactive;
# out-delay 10;
# bgp-error-tolerance {
#     malformed-route-limit 40000000;
# }
# authentication-algorithm md5;
# advertise-bgp-static {
#     policy static-to-bgp;
# }
# bfd-liveness-detection {
#     version automatic;
#     minimum-receive-interval 8;
#     multiplier 30;
#     no-adaptation;
#     transmit-interval {
#         minimum-interval 4;
#     }
# }
# egress-te-sid-stats;

# admin# show routing-options autonomous-system
# [edit]

#
# Using deleted
#
# Before state
# ------------
#
# admin# show protocols bgp
# precision-timers;
# advertise-from-main-vpn-tables;
# holddown-all-stale-labels;
# description "This is configured with Junos_bgp resource module";
# accept-remote-nexthop;
# preference 2;
# hold-time 5;
# advertise-inactive;
# no-advertise-peer-as;
# no-aggregator-id;
# out-delay 10;
# log-updown;
# damping;
# bgp-error-tolerance {
#     malformed-route-limit 20000000;
# }
# authentication-algorithm md5;
# no-client-reflect;
# include-mp-next-hop;
# bmp {
#     monitor enable;
# }
# add-path-display-ipv4-address;
# egress-te-sid-stats;
# group internal {
#     out-delay 12;
# }
# admin# show routing-options autonomous-system
# 65534 loops 3 asdot-notation;

- name: Delete Junos BGP global config
  junipernetworks.junos.junos_bgp_global:
    config:
    state: deleted

# After state
# -----------
# admin# show protocols bgp
# group internal {
#     out-delay 12;
# }

# admin# show protocols bgp
# [edit]

# admin# show routing-options autonomous-system
# [edit]
# Using gathered
#
# Before state
# ------------
#
# admin# show protocols bgp
# description "This is configured with Junos_bgp resource module replace";
# preference 2;
# hold-time 5;
# advertise-inactive;
# out-delay 10;
# bgp-error-tolerance {
#     malformed-route-limit 40000000;
# }
# authentication-algorithm md5;
# advertise-bgp-static {
#     policy static-to-bgp;
# }
# bfd-liveness-detection {
#     version automatic;
#     minimum-receive-interval 8;
#     multiplier 30;
#     no-adaptation;
#     transmit-interval {
#         minimum-interval 4;
#     }
# }
# egress-te-sid-stats;

- name: Gather Junos BGP global config
  junipernetworks.junos.junos_bgp_global:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": {
#         "advertise_bgp_static": {
#             "policy": "static-to-bgp"
#         },
#         "advertise_inactive": true,
#         "authentication_algorithm": "md5",
#         "bfd_liveness_detection": {
#             "minimum_receive_interval": 8,
#             "multiplier": 30,
#             "no_adaptation": true,
#             "transmit_interval": {
#                 "minimum_interval": 4
#             },
#             "version": "automatic"
#         },
#         "bgp_error_tolerance": {
#             "malformed_route_limit": 40000000
#         },
#         "description": "This is configured with Junos_bgp resource module replace",
#         "egress_te_sid_stats": true,
#         "hold_time": 5,
#         "out_delay": 10,
#         "preference": "2"
#     }
#
#
# Using purged
#
# Before state
# ------------
#
# admin# show protocols bgp
# precision-timers;
# advertise-from-main-vpn-tables;
# holddown-all-stale-labels;
# description "This is configured with Junos_bgp resource module";
# accept-remote-nexthop;
# preference 2;
# hold-time 5;
# advertise-inactive;
# no-advertise-peer-as;
# no-aggregator-id;
# out-delay 10;
# log-updown;
# damping;
# bgp-error-tolerance {
#     malformed-route-limit 20000000;
# }
# authentication-algorithm md5;
# no-client-reflect;
# include-mp-next-hop;
# bmp {
#     monitor enable;
# }
# add-path-display-ipv4-address;
# egress-te-sid-stats;
# group internal {
#     out-delay 12;
# }
# admin# show routing-options autonomous-system
# 65534 loops 3 asdot-notation;

- name: Purge Junos BGP global config
  junipernetworks.junos.junos_bgp_global:
    config:
    state: purged

# After state
# ----------
# admin# show protocols bgp
#
# [edit]
# admin# show routing-options autonomous-system
#
#[edit]

# Using rendered
#
#
- name: Render the commands for provided  configuration
  junipernetworks.junos.junos_bgp_global:
    config:
      authentication_algorithm: "md5"
      bfd_liveness_detection:
        minimum_receive_interval: 4
        multiplier: 10
        no_adaptation: true
        transmit_interval:
          minimum_interval: 2
        version: "automatic"
      bgp_error_tolerance:
        malformed_route_limit: 20000000
      bmp:
        monitor: true
      damping: true
      description: "This is configured with Junos_bgp resource module"
      egress_te_sid_stats: true
      hold_time: 5
    state: rendered

#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": "
# <nc:protocols
#     xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
#     <nc:bgp>
#         <nc:damping/>
#         <nc:egress-te-sid-stats/>
#         <nc:authentication-algorithm>md5</nc:authentication-algorithm>
#         <nc:description>This is configured with Junos_bgp resource module</nc:description>
#         <nc:hold-time>5</nc:hold-time>
#         <nc:bfd-liveness-detection>
#             <nc:transmit-interval>
#                 <nc:minimum-interval>2</nc:minimum-interval>
#             </nc:transmit-interval>
#             <nc:minimum-receive-interval>4</nc:minimum-receive-interval>
#             <nc:multiplier>10</nc:multiplier>
#             <nc:no-adaptation/>
#             <nc:version>automatic</nc:version>
#         </nc:bfd-liveness-detection>
#         <nc:bgp-error-tolerance>
#             <nc:malformed-route-limit>20000000</nc:malformed-route-limit>
#         </nc:bgp-error-tolerance>
#         <nc:bmp>
#             <nc:monitor>enable</nc:monitor>
#         </nc:bmp>
#     </nc:bgp>
# </nc:protocols>"
#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#    <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#       <version>18.4R1-S2.4</version>
#       <protocols>
#          <bgp>
#             <precision-timers />
#             <advertise-from-main-vpn-tables />
#             <holddown-all-stale-labels />
#             <description>This is configured with Junos_bgp resource module</description>
#             <accept-remote-nexthop />
#             <preference>2</preference>
#             <hold-time>5</hold-time>
#             <advertise-inactive />
#             <no-advertise-peer-as />
#             <no-aggregator-id />
#             <out-delay>10</out-delay>
#             <log-updown />
#             <damping />
#             <bgp-error-tolerance>
#                <malformed-route-limit>20000000</malformed-route-limit>
#             </bgp-error-tolerance>
#             <authentication-algorithm>md5</authentication-algorithm>
#             <remove-private />
#             <no-client-reflect />
#             <include-mp-next-hop />
#             <bmp>
#                <monitor>disable</monitor>
#                <route-monitoring>
#                   <none />
#                </route-monitoring>
#             </bmp>
#             <advertise-bgp-static>
#                <policy>static-to-bgp</policy>
#             </advertise-bgp-static>
#             <add-path-display-ipv4-address />
#             <bfd-liveness-detection>
#                <version>automatic</version>
#                <minimum-receive-interval>4</minimum-receive-interval>
#                <multiplier>10</multiplier>
#                <no-adaptation />
#                <transmit-interval>
#                   <minimum-interval>2</minimum-interval>
#                </transmit-interval>
#                <detection-time>
#                   <threshold>300000</threshold>
#                </detection-time>
#             </bfd-liveness-detection>
#             <egress-te-sid-stats />
#             <group>
#                <name>internal</name>
#                <out-delay>8</out-delay>
#             </group>
#             <group>
#                <name>external</name>
#                <out-delay>9</out-delay>
#             </group>
#             <group>
#                <name>inboun</name>
#                <type>internal</type>
#             </group>
#             <group>
#                <name>ibgp</name>
#                <type>internal</type>
#                <local-address>10.2.2.2</local-address>
#                <export>static-to-bgp</export>
#                <neighbor>
#                   <name>10.1.1.1</name>
#                </neighbor>
#             </group>
#          </bgp>
#          <ospf3>
#             <area>
#                <name>0.0.0.100</name>
#                <stub>
#                   <default-metric>200</default-metric>
#                </stub>
#                <interface>
#                   <name>so-0/0/0.0</name>
#                   <metric>5</metric>
#                   <priority>3</priority>
#                </interface>
#             </area>
#          </ospf3>
#       </protocols>
#       <routing-options>
#          <static>
#             <route>
#                <name>172.16.17.0/24</name>
#                <discard />
#             </route>
#          </static>
#          <router-id>10.200.16.75</router-id>
#          <autonomous-system>
#             <as-number>65432</as-number>
#          </autonomous-system>
#       </routing-options>
#    </configuration>
# </rpc-reply>

- name: Parsed the device configuration to get output commands
  junipernetworks.junos.junos_bgp_global:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed":  {
#         "accept_remote_nexthop": true,
#         "add_path_display_ipv4_address": true,
#         "advertise_bgp_static": {
#             "policy": "static-to-bgp"
#         },
#         "advertise_from_main_vpn_tables": true,
#         "advertise_inactive": true,
#         "as_number": "65432",
#         "authentication_algorithm": "md5",
#         "bfd_liveness_detection": {
#             "detection_time": {
#                 "threshold": 300000
#             },
#             "minimum_receive_interval": 4,
#             "multiplier": 10,
#             "no_adaptation": true,
#             "transmit_interval": {
#                 "minimum_interval": 2
#             },
#             "version": "automatic"
#         },
#         "bgp_error_tolerance": {
#             "malformed_route_limit": 20000000
#         },
#         "bmp": {
#             "monitor": false,
#             "route_monitoring": {
#                 "none": true
#             }
#         },
#         "damping": true,
#         "description": "This is configured with Junos_bgp resource module",
#         "egress_te_sid_stats": true,
#         "hold_time": 5,
#         "holddown_all_stale_labels": true,
#         "include_mp_next_hop": true,
#         "log_updown": true,
#         "no_advertise_peer_as": true,
#         "no_aggregator_id": true,
#         "no_client_reflect": true,
#         "out_delay": 10,
#         "precision_timers": true,
#         "preference": "2"
#     }
#
```

## [Return Values](junos_bgp_global_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `[" <nc:protocols xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:bgp> <nc:damping/> <nc:egress-te-sid-stats/> <nc:authentication-algorithm>md5</nc:authentication-algorithm> <nc:description>This is configured with Junos_bgp resource module</nc:description> <nc:hold-time>5</nc:hold-time> <nc:bfd-liveness-detection> <nc:transmit-interval> <nc:minimum-interval>2</nc:minimum-interval> </nc:transmit-interval> <nc:minimum-receive-interval>4</nc:minimum-receive-interval> <nc:multiplier>10</nc:multiplier> <nc:no-adaptation/> <nc:version>automatic</nc:version> </nc:bfd-liveness-detection> <nc:bgp-error-tolerance> <nc:malformed-route-limit>20000000</nc:malformed-route-limit> </nc:bgp-error-tolerance> <nc:bmp> <nc:monitor>enable</nc:monitor> </nc:bmp> </nc:bgp> </nc:protocols>", "xml 2", "xml 3"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
