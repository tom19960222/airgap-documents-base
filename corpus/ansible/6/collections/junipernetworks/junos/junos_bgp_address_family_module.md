---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_bgp_address_family module – Manage BGP Address Family attributes of interfaces on Junos devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_bgp_address_family_module.html
fetched_at: 2026-07-27T17:54:11+00:00
---
# junipernetworks.junos.junos_bgp_address_family module – Manage BGP Address Family attributes of interfaces on Junos devices.

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
> see [Requirements](junos_bgp_address_family_module.md#ansible-collections-junipernetworks-junos-junos-bgp-address-family-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_bgp_address_family`.

New in junipernetworks.junos 1.3.0

- [Synopsis](junos_bgp_address_family_module.md#synopsis)
- [Requirements](junos_bgp_address_family_module.md#requirements)
- [Parameters](junos_bgp_address_family_module.md#parameters)
- [Notes](junos_bgp_address_family_module.md#notes)
- [Examples](junos_bgp_address_family_module.md#examples)
- [Return Values](junos_bgp_address_family_module.md#return-values)

## [Synopsis](junos_bgp_address_family_module.md#id1)

- Manage BGP Address Family attributes of interfaces on Junos network devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_bgp_address_family_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.6.4)
- xmltodict (>=0.12.0)

## [Parameters](junos_bgp_address_family_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | The provided link BGP address family dictionary. |
| **address_family**  list / elements=dictionary | Enable address family and enter its config mode. |
| **af_type**  list / elements=dictionary | Address family type for ipv4. |
| **accepted_prefix_limit**  dictionary | Specify limit for maximum number of prefixes accepted from a peer. |
| **forever**  boolean | Idle the peer until the user intervenes.  Choices:   - `false` - `true` |
| **idle_timeout**  boolean | Set idle timeout node.  Choices:   - `false` - `true` |
| **idle_timeout_value**  integer | Specify timeout before attempting to restart peer. |
| **limit_threshold**  integer | Specify teardown percentage of prefix-limit to start warnings. |
| **maximum**  integer | Specify maximum number of prefixes accepted from a peer. |
| **teardown**  boolean | Clear peer connection on reaching limit.  Choices:   - `false` - `true` |
| **add_path**  dictionary | Advertise multiple paths to peer. |
| **receive**  boolean | Receive multiple paths from peer.  Choices:   - `false` - `true` |
| **send**  dictionary | Send multiple paths to peer. |
| **include_backup_path**  integer | Specify number of backup paths to advertise. |
| **multipath**  boolean | Include only multipath contributor routes.  Choices:   - `false` - `true` |
| **path_count**  integer / required | Include only multipath contributor routes. |
| **path_selection_mode**  dictionary | Configure how to select add-path routes. |
| **all_paths**  boolean | Advertise all paths allowed by path count.  Choices:   - `false` - `true` |
| **equal_cost_paths**  boolean | Advertise equal cost paths.  Choices:   - `false` - `true` |
| **prefix_policy**  string | Perform add-path only for prefixes that match policy. |
| **aggregate_label**  dictionary | Aggregate labels of incoming routes with the same FEC. |
| **community**  string | Community to identify the FEC of incoming routesC. |
| **set**  boolean | Set Aggregate labels of incoming routes with the same FEC  Choices:   - `false` - `true` |
| **aigp**  dictionary | Allow sending and receiving of AIGP attribute. |
| **disable**  boolean | Dn not allow sending and receiving of AIGP attribute.  Choices:   - `false` - `true` |
| **set**  boolean | Set AIGP.  Choices:   - `false` - `true` |
| **damping**  boolean | Enable route flap damping.  Choices:   - `false` - `true` |
| **defer_initial_multipath_build**  dictionary | Defer initial multipath build until EOR is received. |
| **maximum_delay**  integer | Max delay(sec) multipath build after peer is up. |
| **set**  boolean | Set defer initial multipath build.  Choices:   - `false` - `true` |
| **delay_route_advertisements**  dictionary | Delay route updates for this family until FIB-sync. |
| **max_delay_route_age**  integer | Set max delay advertisement route age. |
| **max_delay_routing_uptime**  integer | Set max delay advertisement route age. |
| **min_delay_inbound_convergence**  integer | Set min delayadvertisement after source-peer sent all routes. |
| **min_delay_routing_uptime**  integer | Set min delay advertisement route age. |
| **set**  boolean | Set delay route advertisements.  Choices:   - `false` - `true` |
| **entropy_label**  dictionary | Use entropy label for entropy label capable BGP LSPs. |
| **import**  string | Policy to select BGP LSPs to use entropy label. |
| **no_next_hop_validation**  boolean | Don’t validate next hop field against route next hop.  Choices:   - `false` - `true` |
| **set**  boolean | Set entropy-label attribute.  Choices:   - `false` - `true` |
| **explicit_null**  dictionary | Advertise explicit null. |
| **connected_only**  boolean | Advertise explicit null only for connected routes.  Choices:   - `false` - `true` |
| **set**  boolean | Set explicit-null attribute.  Choices:   - `false` - `true` |
| **extended_nexthop**  boolean | Enable extended nexthop encoding.  Choices:   - `false` - `true` |
| **extended_nexthop_color**  boolean | Resolve using extended color nexthop.  Choices:   - `false` - `true` |
| **graceful_restart_forwarding_state_bit**  string | Specify BGP graceful restart options.  Choices:   - `"from-fib"` - `"set"` |
| **legacy_redirect_ip_action**  dictionary | Configure legacy redirect to IP support. |
| **receive**  boolean | Accept legacy encoded redirect-to-ip action attribute  Choices:   - `false` - `true` |
| **send**  boolean | Advertise Redirect action as legacy redirect attribute.  Choices:   - `false` - `true` |
| **set**  boolean | Set the legacy-redirect-ip-action.  Choices:   - `false` - `true` |
| **local_ipv4_address**  string | Specify local IPv4 address. |
| **loops**  integer | Allow local AS in received AS paths. |
| **no_install**  boolean | Dont install received routes in forwarding.  Choices:   - `false` - `true` |
| **no_validate**  string | Bypass validation procedure for routes that match policy. |
| **output_queue_priority_expedited**  boolean | Expedited queue; highest priority.  Choices:   - `false` - `true` |
| **output_queue_priority_priority**  integer | Output queue priority; higher is better. |
| **per_group_label**  boolean | Advertise prefixes with unique labels per group.  Choices:   - `false` - `true` |
| **per_prefix_label**  boolean | Allocate a unique label to each advertised prefix.  Choices:   - `false` - `true` |
| **prefix_limit**  dictionary | Limit maximum number of prefixes from a peer. |
| **forever**  boolean | Idle the peer until the user intervenes.  Choices:   - `false` - `true` |
| **idle_timeout**  boolean | Set idle timeout node.  Choices:   - `false` - `true` |
| **idle_timeout_value**  integer | Specify timeout before attempting to restart peer. |
| **limit_threshold**  integer | Percentage of prefix-limit to start warnings. |
| **maximum**  integer | Specify maximum number of prefixes from a peer. |
| **teardown**  boolean | Clear peer connection on reaching limit.  Choices:   - `false` - `true` |
| **resolve_vpn**  boolean | Install received NLRI in inet.3 also.  Choices:   - `false` - `true` |
| **rib**  string | Select table used by labeled unicast routes.  Choices:   - `"inet.3"` |
| **ribgroup_name**  string | Name of the routing table group. |
| **route_refresh_priority_expedited**  boolean | Expedited queue; highest priority.  Choices:   - `false` - `true` |
| **route_refresh_priority_priority**  integer | Output queue priority; higher is better. |
| **secondary_independent_resolution**  boolean | Resolve FLOW routes in VRF table independent of VPN FLOW route.  Choices:   - `false` - `true` |
| **set**  boolean | Set NLRI.  Choices:   - `false` - `true` |
| **strip_nexthop**  boolean | Strip the next-hop from the outgoing flow update.  Choices:   - `false` - `true` |
| **topology**  list / elements=dictionary | Multi topology routing tables. |
| **community**  list / elements=string | Community to identify multi topology routes. |
| **name**  string | Specify topology name. |
| **traffic_statistics**  dictionary | Collect statistics for BGP label-switched paths |
| **file**  dictionary | Statistics file options. |
| **filename**  string | Name of file in which to write trace information. |
| **files**  integer | Maximum number of trace files. |
| **no_world_readable**  boolean | Don’t allow any user to read the log file.  Choices:   - `false` - `true` |
| **size**  integer | Maximum trace file size. |
| **world_readable**  boolean | Don’t allow any user to read the log file.  Choices:   - `false` - `true` |
| **interval**  integer | Time to collect statistics (seconds). |
| **labeled_path**  boolean | Enable ingress labeled path statistics.  Choices:   - `false` - `true` |
| **set**  boolean | Set traffic-statistics.  Choices:   - `false` - `true` |
| **type**  string | Specify type of NLRI.  Choices:   - `"any"` - `"flow"` - `"labeled-unicast"` - `"multicast"` - `"segment-routing-te"` - `"unicast"` - `"signaling"` - `"auto-discovery-mspw"` - `"auto-discovery-only"` |
| **withdraw_priority_expedited**  boolean | Expedited queue; highest priority.  Choices:   - `false` - `true` |
| **withdraw_priority_priority**  integer | Output queue priority; higher is better. |
| **afi**  string | address family.  Choices:   - `"evpn"` - `"inet"` - `"inet-mdt"` - `"inet-mvpn"` - `"inet-vpn"` - `"inet6"` - `"inet6-mvpn"` - `"inet6-vpn"` - `"iso-vpn"` - `"l2vpn"` - `"route-target"` - `"traffic-engineering"` |
| **groups**  list / elements=dictionary | Specify address family config for groups. |
| **address_family**  list / elements=dictionary | Enable address family and enter its config mode. |
| **af_type**  list / elements=dictionary | Address family type for ipv4. |
| **accepted_prefix_limit**  dictionary | Specify limit for maximum number of prefixes accepted from a peer. |
| **forever**  boolean | Idle the peer until the user intervenes.  Choices:   - `false` - `true` |
| **idle_timeout**  boolean | Set idle timeout node.  Choices:   - `false` - `true` |
| **idle_timeout_value**  integer | Specify timeout before attempting to restart peer. |
| **limit_threshold**  integer | Specify teardown percentage of prefix-limit to start warnings. |
| **maximum**  integer | Specify maximum number of prefixes accepted from a peer. |
| **teardown**  boolean | Clear peer connection on reaching limit.  Choices:   - `false` - `true` |
| **add_path**  dictionary | Advertise multiple paths to peer. |
| **receive**  boolean | Receive multiple paths from peer.  Choices:   - `false` - `true` |
| **send**  dictionary | Send multiple paths to peer. |
| **include_backup_path**  integer | Specify number of backup paths to advertise. |
| **multipath**  boolean | Include only multipath contributor routes.  Choices:   - `false` - `true` |
| **path_count**  integer / required | Include only multipath contributor routes. |
| **path_selection_mode**  dictionary | Configure how to select add-path routes. |
| **all_paths**  boolean | Advertise all paths allowed by path count.  Choices:   - `false` - `true` |
| **equal_cost_paths**  boolean | Advertise equal cost paths.  Choices:   - `false` - `true` |
| **prefix_policy**  string | Perform add-path only for prefixes that match policy. |
| **aggregate_label**  dictionary | Aggregate labels of incoming routes with the same FEC. |
| **community**  string | Community to identify the FEC of incoming routesC. |
| **set**  boolean | Set Aggregate labels of incoming routes with the same FEC  Choices:   - `false` - `true` |
| **aigp**  dictionary | Allow sending and receiving of AIGP attribute. |
| **disable**  boolean | Dn not allow sending and receiving of AIGP attribute.  Choices:   - `false` - `true` |
| **set**  boolean | Set AIGP.  Choices:   - `false` - `true` |
| **damping**  boolean | Enable route flap damping.  Choices:   - `false` - `true` |
| **defer_initial_multipath_build**  dictionary | Defer initial multipath build until EOR is received. |
| **maximum_delay**  integer | Max delay(sec) multipath build after peer is up. |
| **set**  boolean | Set defer initial multipath build.  Choices:   - `false` - `true` |
| **delay_route_advertisements**  dictionary | Delay route updates for this family until FIB-sync. |
| **max_delay_route_age**  integer | Set max delay advertisement route age. |
| **max_delay_routing_uptime**  integer | Set max delay advertisement route age. |
| **min_delay_inbound_convergence**  integer | Set min delayadvertisement after source-peer sent all routes. |
| **min_delay_routing_uptime**  integer | Set min delay advertisement route age. |
| **set**  boolean | Set delay route advertisements.  Choices:   - `false` - `true` |
| **entropy_label**  dictionary | Use entropy label for entropy label capable BGP LSPs. |
| **import**  string | Policy to select BGP LSPs to use entropy label. |
| **no_next_hop_validation**  boolean | Don’t validate next hop field against route next hop.  Choices:   - `false` - `true` |
| **set**  boolean | Set entropy-label attribute.  Choices:   - `false` - `true` |
| **explicit_null**  dictionary | Advertise explicit null. |
| **connected_only**  boolean | Advertise explicit null only for connected routes.  Choices:   - `false` - `true` |
| **set**  boolean | Set explicit-null attribute.  Choices:   - `false` - `true` |
| **extended_nexthop**  boolean | Enable extended nexthop encoding.  Choices:   - `false` - `true` |
| **extended_nexthop_color**  boolean | Resolve using extended color nexthop.  Choices:   - `false` - `true` |
| **graceful_restart_forwarding_state_bit**  string | Specify BGP graceful restart options.  Choices:   - `"from-fib"` - `"set"` |
| **legacy_redirect_ip_action**  dictionary | Configure legacy redirect to IP support. |
| **receive**  boolean | Accept legacy encoded redirect-to-ip action attribute  Choices:   - `false` - `true` |
| **send**  boolean | Advertise Redirect action as legacy redirect attribute.  Choices:   - `false` - `true` |
| **set**  boolean | Set the legacy-redirect-ip-action.  Choices:   - `false` - `true` |
| **local_ipv4_address**  string | Specify local IPv4 address. |
| **loops**  integer | Allow local AS in received AS paths. |
| **no_install**  boolean | Dont install received routes in forwarding.  Choices:   - `false` - `true` |
| **no_validate**  string | Bypass validation procedure for routes that match policy. |
| **output_queue_priority_expedited**  boolean | Expedited queue; highest priority.  Choices:   - `false` - `true` |
| **output_queue_priority_priority**  integer | Output queue priority; higher is better. |
| **per_group_label**  boolean | Advertise prefixes with unique labels per group.  Choices:   - `false` - `true` |
| **per_prefix_label**  boolean | Allocate a unique label to each advertised prefix.  Choices:   - `false` - `true` |
| **prefix_limit**  dictionary | Limit maximum number of prefixes from a peer. |
| **forever**  boolean | Idle the peer until the user intervenes.  Choices:   - `false` - `true` |
| **idle_timeout**  boolean | Set idle timeout node.  Choices:   - `false` - `true` |
| **idle_timeout_value**  integer | Specify timeout before attempting to restart peer. |
| **limit_threshold**  integer | Percentage of prefix-limit to start warnings. |
| **maximum**  integer | Specify maximum number of prefixes from a peer. |
| **teardown**  boolean | Clear peer connection on reaching limit.  Choices:   - `false` - `true` |
| **resolve_vpn**  boolean | Install received NLRI in inet.3 also.  Choices:   - `false` - `true` |
| **rib**  string | Select table used by labeled unicast routes.  Choices:   - `"inet.3"` |
| **ribgroup_name**  string | Name of the routing table group. |
| **route_refresh_priority_expedited**  boolean | Expedited queue; highest priority.  Choices:   - `false` - `true` |
| **route_refresh_priority_priority**  integer | Output queue priority; higher is better. |
| **secondary_independent_resolution**  boolean | Resolve FLOW routes in VRF table independent of VPN FLOW route.  Choices:   - `false` - `true` |
| **set**  boolean | Set NLRI.  Choices:   - `false` - `true` |
| **strip_nexthop**  boolean | Strip the next-hop from the outgoing flow update.  Choices:   - `false` - `true` |
| **topology**  list / elements=dictionary | Multi topology routing tables. |
| **community**  list / elements=string | Community to identify multi topology routes. |
| **name**  string | Specify topology name. |
| **traffic_statistics**  dictionary | Collect statistics for BGP label-switched paths |
| **file**  dictionary | Statistics file options. |
| **filename**  string | Name of file in which to write trace information. |
| **files**  integer | Maximum number of trace files. |
| **no_world_readable**  boolean | Don’t allow any user to read the log file.  Choices:   - `false` - `true` |
| **size**  integer | Maximum trace file size. |
| **world_readable**  boolean | Don’t allow any user to read the log file.  Choices:   - `false` - `true` |
| **interval**  integer | Time to collect statistics (seconds). |
| **labeled_path**  boolean | Enable ingress labeled path statistics.  Choices:   - `false` - `true` |
| **set**  boolean | Set traffic-statistics.  Choices:   - `false` - `true` |
| **type**  string | Specify type of NLRI.  Choices:   - `"any"` - `"flow"` - `"labeled-unicast"` - `"multicast"` - `"segment-routing-te"` - `"unicast"` - `"signaling"` - `"auto-discovery-mspw"` - `"auto-discovery-only"` |
| **withdraw_priority_expedited**  boolean | Expedited queue; highest priority.  Choices:   - `false` - `true` |
| **withdraw_priority_priority**  integer | Output queue priority; higher is better. |
| **afi**  string | address family.  Choices:   - `"evpn"` - `"inet"` - `"inet-mdt"` - `"inet-mvpn"` - `"inet-vpn"` - `"inet6"` - `"inet6-mvpn"` - `"inet6-vpn"` - `"iso-vpn"` - `"l2vpn"` - `"route-target"` - `"traffic-engineering"` |
| **name**  string | Specify name of the group |
| **neighbors**  list / elements=dictionary | Specify address family config per neighbor. |
| **address_family**  list / elements=dictionary | Enable address family and enter its config mode. |
| **af_type**  list / elements=dictionary | Address family type for ipv4. |
| **accepted_prefix_limit**  dictionary | Specify limit for maximum number of prefixes accepted from a peer. |
| **forever**  boolean | Idle the peer until the user intervenes.  Choices:   - `false` - `true` |
| **idle_timeout**  boolean | Set idle timeout node.  Choices:   - `false` - `true` |
| **idle_timeout_value**  integer | Specify timeout before attempting to restart peer. |
| **limit_threshold**  integer | Specify teardown percentage of prefix-limit to start warnings. |
| **maximum**  integer | Specify maximum number of prefixes accepted from a peer. |
| **teardown**  boolean | Clear peer connection on reaching limit.  Choices:   - `false` - `true` |
| **add_path**  dictionary | Advertise multiple paths to peer. |
| **receive**  boolean | Receive multiple paths from peer.  Choices:   - `false` - `true` |
| **send**  dictionary | Send multiple paths to peer. |
| **include_backup_path**  integer | Specify number of backup paths to advertise. |
| **multipath**  boolean | Include only multipath contributor routes.  Choices:   - `false` - `true` |
| **path_count**  integer / required | Include only multipath contributor routes. |
| **path_selection_mode**  dictionary | Configure how to select add-path routes. |
| **all_paths**  boolean | Advertise all paths allowed by path count.  Choices:   - `false` - `true` |
| **equal_cost_paths**  boolean | Advertise equal cost paths.  Choices:   - `false` - `true` |
| **prefix_policy**  string | Perform add-path only for prefixes that match policy. |
| **aggregate_label**  dictionary | Aggregate labels of incoming routes with the same FEC. |
| **community**  string | Community to identify the FEC of incoming routesC. |
| **set**  boolean | Set Aggregate labels of incoming routes with the same FEC  Choices:   - `false` - `true` |
| **aigp**  dictionary | Allow sending and receiving of AIGP attribute. |
| **disable**  boolean | Dn not allow sending and receiving of AIGP attribute.  Choices:   - `false` - `true` |
| **set**  boolean | Set AIGP.  Choices:   - `false` - `true` |
| **damping**  boolean | Enable route flap damping.  Choices:   - `false` - `true` |
| **defer_initial_multipath_build**  dictionary | Defer initial multipath build until EOR is received. |
| **maximum_delay**  integer | Max delay(sec) multipath build after peer is up. |
| **set**  boolean | Set defer initial multipath build.  Choices:   - `false` - `true` |
| **delay_route_advertisements**  dictionary | Delay route updates for this family until FIB-sync. |
| **max_delay_route_age**  integer | Set max delay advertisement route age. |
| **max_delay_routing_uptime**  integer | Set max delay advertisement route age. |
| **min_delay_inbound_convergence**  integer | Set min delayadvertisement after source-peer sent all routes. |
| **min_delay_routing_uptime**  integer | Set min delay advertisement route age. |
| **set**  boolean | Set delay route advertisements.  Choices:   - `false` - `true` |
| **entropy_label**  dictionary | Use entropy label for entropy label capable BGP LSPs. |
| **import**  string | Policy to select BGP LSPs to use entropy label. |
| **no_next_hop_validation**  boolean | Don’t validate next hop field against route next hop.  Choices:   - `false` - `true` |
| **set**  boolean | Set entropy-label attribute.  Choices:   - `false` - `true` |
| **explicit_null**  dictionary | Advertise explicit null. |
| **connected_only**  boolean | Advertise explicit null only for connected routes.  Choices:   - `false` - `true` |
| **set**  boolean | Set explicit-null attribute.  Choices:   - `false` - `true` |
| **extended_nexthop**  boolean | Enable extended nexthop encoding.  Choices:   - `false` - `true` |
| **extended_nexthop_color**  boolean | Resolve using extended color nexthop.  Choices:   - `false` - `true` |
| **graceful_restart_forwarding_state_bit**  string | Specify BGP graceful restart options.  Choices:   - `"from-fib"` - `"set"` |
| **legacy_redirect_ip_action**  dictionary | Configure legacy redirect to IP support. |
| **receive**  boolean | Accept legacy encoded redirect-to-ip action attribute  Choices:   - `false` - `true` |
| **send**  boolean | Advertise Redirect action as legacy redirect attribute.  Choices:   - `false` - `true` |
| **set**  boolean | Set the legacy-redirect-ip-action.  Choices:   - `false` - `true` |
| **local_ipv4_address**  string | Specify local IPv4 address. |
| **loops**  integer | Allow local AS in received AS paths. |
| **no_install**  boolean | Dont install received routes in forwarding.  Choices:   - `false` - `true` |
| **no_validate**  string | Bypass validation procedure for routes that match policy. |
| **output_queue_priority_expedited**  boolean | Expedited queue; highest priority.  Choices:   - `false` - `true` |
| **output_queue_priority_priority**  integer | Output queue priority; higher is better. |
| **per_group_label**  boolean | Advertise prefixes with unique labels per group.  Choices:   - `false` - `true` |
| **per_prefix_label**  boolean | Allocate a unique label to each advertised prefix.  Choices:   - `false` - `true` |
| **prefix_limit**  dictionary | Limit maximum number of prefixes from a peer. |
| **forever**  boolean | Idle the peer until the user intervenes.  Choices:   - `false` - `true` |
| **idle_timeout**  boolean | Set idle timeout node.  Choices:   - `false` - `true` |
| **idle_timeout_value**  integer | Specify timeout before attempting to restart peer. |
| **limit_threshold**  integer | Percentage of prefix-limit to start warnings. |
| **maximum**  integer | Specify maximum number of prefixes from a peer. |
| **teardown**  boolean | Clear peer connection on reaching limit.  Choices:   - `false` - `true` |
| **resolve_vpn**  boolean | Install received NLRI in inet.3 also.  Choices:   - `false` - `true` |
| **rib**  string | Select table used by labeled unicast routes.  Choices:   - `"inet.3"` |
| **ribgroup_name**  string | Name of the routing table group. |
| **route_refresh_priority_expedited**  boolean | Expedited queue; highest priority.  Choices:   - `false` - `true` |
| **route_refresh_priority_priority**  integer | Output queue priority; higher is better. |
| **secondary_independent_resolution**  boolean | Resolve FLOW routes in VRF table independent of VPN FLOW route.  Choices:   - `false` - `true` |
| **set**  boolean | Set NLRI.  Choices:   - `false` - `true` |
| **strip_nexthop**  boolean | Strip the next-hop from the outgoing flow update.  Choices:   - `false` - `true` |
| **topology**  list / elements=dictionary | Multi topology routing tables. |
| **community**  list / elements=string | Community to identify multi topology routes. |
| **name**  string | Specify topology name. |
| **traffic_statistics**  dictionary | Collect statistics for BGP label-switched paths |
| **file**  dictionary | Statistics file options. |
| **filename**  string | Name of file in which to write trace information. |
| **files**  integer | Maximum number of trace files. |
| **no_world_readable**  boolean | Don’t allow any user to read the log file.  Choices:   - `false` - `true` |
| **size**  integer | Maximum trace file size. |
| **world_readable**  boolean | Don’t allow any user to read the log file.  Choices:   - `false` - `true` |
| **interval**  integer | Time to collect statistics (seconds). |
| **labeled_path**  boolean | Enable ingress labeled path statistics.  Choices:   - `false` - `true` |
| **set**  boolean | Set traffic-statistics.  Choices:   - `false` - `true` |
| **type**  string | Specify type of NLRI.  Choices:   - `"any"` - `"flow"` - `"labeled-unicast"` - `"multicast"` - `"segment-routing-te"` - `"unicast"` - `"signaling"` - `"auto-discovery-mspw"` - `"auto-discovery-only"` |
| **withdraw_priority_expedited**  boolean | Expedited queue; highest priority.  Choices:   - `false` - `true` |
| **withdraw_priority_priority**  integer | Output queue priority; higher is better. |
| **afi**  string | address family.  Choices:   - `"evpn"` - `"inet"` - `"inet-mdt"` - `"inet-mvpn"` - `"inet-vpn"` - `"inet6"` - `"inet6-mvpn"` - `"inet6-vpn"` - `"iso-vpn"` - `"l2vpn"` - `"route-target"` - `"traffic-engineering"` |
| **neighbor_address**  string | Specify neighbor address. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Junos device by executing the command **show protocols bgp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result |
| **state**  string | The state the configuration should be left in.  State *deleted* only removes BGP address family attributes that this modules manages and does not negate the BGP neighbor address family completely. Thereby, preserving address-family related configurations under BGP group neighbor context.  To delete the address family associated to neighbor use junipernetworks.junos.junos_bgp_neighbor_address_family modules for prior cleanup.  Refer to examples for more details.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](junos_bgp_address_family_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the device being managed.
> - This module works with connection `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - Tested against JunOS v18.4R1

## [Examples](junos_bgp_address_family_module.md#id5)

```yaml+jinja
# Using merged
#
# Before state
# ------------
#
# admin# show protocols bgp
#
# [edit]

- name: Merge Junos BGP address family configuration
  junipernetworks.junos.junos_bgp_address_family:
    config:
      address_family:
        - afi: 'evpn'
          af_type:
            - type: 'signaling'
              accepted_prefix_limit:
                maximum: 20
                limit_threshold: 98
                idle_timeout_value: 2001
              damping: true
              defer_initial_multipath_build:
                maximum_delay: 2
        - afi: 'inet'
          af_type:
            - type: 'flow'
              legacy_redirect_ip_action:
                send: true
                receive: true
              loops: 4
              no_install: true
              output_queue_priority_expedited: true
              secondary_independent_resolution: true

            - type: 'unicast'
              extended_nexthop: true
              extended_nexthop_color: true
              local_ipv4_address: '9.9.9.9'

            - type: 'labeled-unicast'
              entropy_label:
                no_next_hop_validation: true
              explicit_null:
                connected_only: true
              per_prefix_label: true
              per_group_label: true
              prefix_limit:
                maximum: 20
                limit_threshold: 99
                forever: true
              resolve_vpn: true
              rib: 'inet.3'
              route_refresh_priority_expedited: true
              route_refresh_priority_priority: 3

            - type: 'any'
              accepted_prefix_limit:
                maximum: 20
                limit_threshold: 99
                idle_timeout_value: 2000
              damping: true
              defer_initial_multipath_build:
                maximum_delay: 2
              delay_route_advertisements:
                max_delay_route_age: 20
                max_delay_routing_uptime: 32000
                min_delay_inbound_convergence: 32000
                min_delay_routing_uptime: 23000
              graceful_restart_forwarding_state_bit: 'from-fib'
    state: merged

# After state
# -----------
#
# admin# show protocols bgp
# family inet {
#     unicast {
#         local-ipv4-address 9.9.9.9;
#         extended-nexthop;
#         extended-nexthop-color;
#     }
#     flow {
#         loops 4;
#         no-install;
#         output-queue-priority expedited;
#         legacy-redirect-ip-action {
#             receive;
#             send;
#         }
#         secondary-independent-resolution;
#     }
#     any {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout 2000;
#         }
#         damping;
#         delay-route-advertisements {
#             minimum-delay {
#                 routing-uptime 23000;
#                 inbound-convergence 32000;
#             }
#             maximum-delay {
#                 route-age 20;
#                 routing-uptime 32000;
#             }
#         }
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#         graceful-restart {
#             forwarding-state-bit from-fib;
#         }
#     }
#     labeled-unicast {
#         prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout forever;
#         }
#         route-refresh-priority priority 3;
#         per-prefix-label;
#         per-group-label;
#         rib {
#             inet.3;
#         }
#         explicit-null connected-only;
#         resolve-vpn;
#         entropy-label {
#             no-next-hop-validation;
#         }
#     }
# }
# family evpn {
#     signaling {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 98 idle-timeout 2001;
#         }
#         damping;
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#     }
# }
# Using replaced
#
# Before state
# ------------
#
# admin# show protocols bgp
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
# family inet {
#     unicast {
#         local-ipv4-address 9.9.9.9;
#         extended-nexthop;
#         extended-nexthop-color;
#     }
#     flow {
#         loops 4;
#         no-install;
#         output-queue-priority expedited;
#         legacy-redirect-ip-action {
#             receive;
#             send;
#         }
#         secondary-independent-resolution;
#     }
#     any {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout 2000;
#         }
#         damping;
#         delay-route-advertisements {
#             minimum-delay {
#                 routing-uptime 23000;
#                 inbound-convergence 32000;
#             }
#             maximum-delay {
#                 route-age 20;
#                 routing-uptime 32000;
#             }
#         }
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#         graceful-restart {
#             forwarding-state-bit from-fib;
#         }
#     }
#     labeled-unicast {
#         prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout forever;
#         }
#         route-refresh-priority priority 3;
#         per-prefix-label;
#         per-group-label;
#         rib {
#             inet.3;
#         }
#         explicit-null connected-only;
#         resolve-vpn;
#         entropy-label {
#             no-next-hop-validation;
#         }
#     }
# }
# family evpn {
#     signaling {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 98 idle-timeout 2001;
#         }
#         damping;
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#     }
# }

- name: Replace existing Junos BGP address family config with provided config
  junipernetworks.junos.junos_bgp_address_family:
   config:
     address_family:
       - afi: 'evpn'
         af_type:
           - type: 'signaling'
             accepted_prefix_limit:
               maximum: 21
               limit_threshold: 99
               idle_timeout_value: 2002
             delay_route_advertisements:
               max_delay_route_age: 20
               max_delay_routing_uptime: 32000
               min_delay_inbound_convergence: 32000
               min_delay_routing_uptime: 23000
             damping: true
   state: replaced

# After state
# -----------
#
# admin# show protocols bgp
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
# family inet {
#     unicast {
#         local-ipv4-address 9.9.9.9;
#         extended-nexthop;
#         extended-nexthop-color;
#     }
#     flow {
#         loops 4;
#         no-install;
#         output-queue-priority expedited;
#         legacy-redirect-ip-action {
#             receive;
#             send;
#         }
#         secondary-independent-resolution;
#     }
#     any {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout 2000;
#         }
#         damping;
#         delay-route-advertisements {
#             minimum-delay {
#                 routing-uptime 23000;
#                 inbound-convergence 32000;
#             }
#             maximum-delay {
#                 route-age 20;
#                 routing-uptime 32000;
#             }
#         }
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#         graceful-restart {
#             forwarding-state-bit from-fib;
#         }
#     }
#     labeled-unicast {
#         prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout forever;
#         }
#         route-refresh-priority priority 3;
#         per-prefix-label;
#         per-group-label;
#         rib {
#             inet.3;
#         }
#         explicit-null connected-only;
#         resolve-vpn;
#         entropy-label {
#             no-next-hop-validation;
#         }
#     }
# }
# family evpn {
#     signaling {
#         accepted-prefix-limit {
#             maximum 21;
#             teardown 99 idle-timeout 2002;
#         }
#         damping;
#         delay-route-advertisements {
#             minimum-delay {
#                 routing-uptime 23000;
#                 inbound-convergence 32000;
#             }
#             maximum-delay {
#                 route-age 20;
#                 routing-uptime 32000;
#             }
#         }
#     }
# }
# Using overridden
#
# Before state
# ------------
#
# admin# show protocols bgp
# family inet {
#     unicast {
#         local-ipv4-address 9.9.9.9;
#         extended-nexthop;
#         extended-nexthop-color;
#     }
#     flow {
#         loops 4;
#         no-install;
#         output-queue-priority expedited;
#         legacy-redirect-ip-action {
#             receive;
#             send;
#         }
#         secondary-independent-resolution;
#     }
#     any {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout 2000;
#         }
#         damping;
#         delay-route-advertisements {
#             minimum-delay {
#                 routing-uptime 23000;
#                 inbound-convergence 32000;
#             }
#             maximum-delay {
#                 route-age 20;
#                 routing-uptime 32000;
#             }
#         }
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#         graceful-restart {
#             forwarding-state-bit from-fib;
#         }
#     }
#     labeled-unicast {
#         prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout forever;
#         }
#         route-refresh-priority priority 3;
#         per-prefix-label;
#         per-group-label;
#         rib {
#             inet.3;
#         }
#         explicit-null connected-only;
#         resolve-vpn;
#         entropy-label {
#             no-next-hop-validation;
#         }
#     }
# }
# family evpn {
#     signaling {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 98 idle-timeout 2001;
#         }
#         damping;
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#     }
# }

- name: Override Junos BGP address family config
  junipernetworks.junos.junos_bgp_address_family:
   config:
     address_family:
       - afi: 'evpn'
         af_type:
           - type: 'signaling'
             accepted_prefix_limit:
               maximum: 21
               limit_threshold: 99
               idle_timeout_value: 2002
             delay_route_advertisements:
               max_delay_route_age: 20
               max_delay_routing_uptime: 32000
               min_delay_inbound_convergence: 32000
               min_delay_routing_uptime: 23000
             damping: true
   state: overridden

# After state
# -----------
#
# admin# show protocols bgp
# family evpn {
#     signaling {
#         accepted-prefix-limit {
#             maximum 21;
#             teardown 99 idle-timeout 2002;
#         }
#         damping;
#         delay-route-advertisements {
#             minimum-delay {
#                 routing-uptime 23000;
#                 inbound-convergence 32000;
#             }
#             maximum-delay {
#                 route-age 20;
#                 routing-uptime 32000;
#             }
#         }
#     }
# }

# Using deleted
#
# Before state
# ------------
#
# admin# show protocols bgp
# preference 2;
# hold-time 5;
# advertise-inactive;
# out-delay 10;
# family inet {
#     unicast {
#         local-ipv4-address 9.9.9.9;
#         extended-nexthop;
#         extended-nexthop-color;
#     }
#     flow {
#         loops 4;
#         no-install;
#         output-queue-priority expedited;
#         legacy-redirect-ip-action {
#             receive;
#             send;
#         }
#         secondary-independent-resolution;
#     }
#     any {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout 2000;
#         }
#         damping;
#         delay-route-advertisements {
#             minimum-delay {
#                 routing-uptime 23000;
#                 inbound-convergence 32000;
#             }
#             maximum-delay {
#                 route-age 20;
#                 routing-uptime 32000;
#             }
#         }
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#         graceful-restart {
#             forwarding-state-bit from-fib;
#         }
#     }
#     labeled-unicast {
#         prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout forever;
#         }
#         route-refresh-priority priority 3;
#         per-prefix-label;
#         per-group-label;
#         rib {
#             inet.3;
#         }
#         explicit-null connected-only;
#         resolve-vpn;
#         entropy-label {
#             no-next-hop-validation;
#         }
#     }
# }
# family evpn {
#     signaling {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 98 idle-timeout 2001;
#         }
#         damping;
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#     }
# }

- name: Delete Junos BGP address family config based on the afi
  junipernetworks.junos.junos_bgp_address_family:
   config:
    address_family:
      - afi: 'inet'
   state: deleted

# After state
# -----------
#
# admin# show protocols bgp
# preference 2;
# hold-time 5;
# advertise-inactive;
# out-delay 10;
# family evpn {
#     signaling {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 98 idle-timeout 2001;
#         }
#         damping;
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#     }
# }

# Using deleted
#
# Before state
# ------------
#
# admin# show protocols bgp
# preference 2;
# hold-time 5;
# advertise-inactive;
# out-delay 10;
# family inet {
#     unicast {
#         local-ipv4-address 9.9.9.9;
#         extended-nexthop;
#         extended-nexthop-color;
#     }
#     flow {
#         loops 4;
#         no-install;
#         output-queue-priority expedited;
#         legacy-redirect-ip-action {
#             receive;
#             send;
#         }
#         secondary-independent-resolution;
#     }
#     any {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout 2000;
#         }
#         damping;
#         delay-route-advertisements {
#             minimum-delay {
#                 routing-uptime 23000;
#                 inbound-convergence 32000;
#             }
#             maximum-delay {
#                 route-age 20;
#                 routing-uptime 32000;
#             }
#         }
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#         graceful-restart {
#             forwarding-state-bit from-fib;
#         }
#     }
#     labeled-unicast {
#         prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout forever;
#         }
#         route-refresh-priority priority 3;
#         per-prefix-label;
#         per-group-label;
#         rib {
#             inet.3;
#         }
#         explicit-null connected-only;
#         resolve-vpn;
#         entropy-label {
#             no-next-hop-validation;
#         }
#     }
# }
# family evpn {
#     signaling {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 98 idle-timeout 2001;
#         }
#         damping;
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#     }
# }

- name: Delete complete Junos BGP address family config
  junipernetworks.junos.junos_bgp_address_family:
   config:
   state: deleted

# After state
# -----------
#
# admin# show protocols bgp
# preference 2;
# hold-time 5;
# advertise-inactive;
# out-delay 10;

# Using gathered
#
# Before state
# ------------
#
# admin# show protocols bgp
# preference 2;
# hold-time 5;
# advertise-inactive;
# out-delay 10;
# family inet {
#     unicast {
#         local-ipv4-address 9.9.9.9;
#         extended-nexthop;
#         extended-nexthop-color;
#     }
#     flow {
#         loops 4;
#         no-install;
#         output-queue-priority expedited;
#         legacy-redirect-ip-action {
#             receive;
#             send;
#         }
#         secondary-independent-resolution;
#     }
#     any {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout 2000;
#         }
#         damping;
#         delay-route-advertisements {
#             minimum-delay {
#                 routing-uptime 23000;
#                 inbound-convergence 32000;
#             }
#             maximum-delay {
#                 route-age 20;
#                 routing-uptime 32000;
#             }
#         }
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#         graceful-restart {
#             forwarding-state-bit from-fib;
#         }
#     }
#     labeled-unicast {
#         prefix-limit {
#             maximum 20;
#             teardown 99 idle-timeout forever;
#         }
#         route-refresh-priority priority 3;
#         per-prefix-label;
#         per-group-label;
#         rib {
#             inet.3;
#         }
#         explicit-null connected-only;
#         resolve-vpn;
#         entropy-label {
#             no-next-hop-validation;
#         }
#     }
# }
# family evpn {
#     signaling {
#         accepted-prefix-limit {
#             maximum 20;
#             teardown 98 idle-timeout 2001;
#         }
#         damping;
#         defer-initial-multipath-build {
#             maximum-delay 2;
#         }
#     }
# }

- name: Gather Junos BGP address family config
  junipernetworks.junos.junos_bgp_address_family:
    config:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": {
#         "address_family": [
#             {
#                 "af_type": [
#                     {
#                         "accepted_prefix_limit": {
#                             "idle_timeout_value": 2001,
#                             "limit_threshold": 98,
#                             "maximum": 20
#                         },
#                         "damping": true,
#                         "defer_initial_multipath_build": {
#                             "maximum_delay": 2
#                         },
#                         "type": "signaling"
#                     }
#                 ],
#                 "afi": "evpn"
#             },
#             {
#                 "af_type": [
#                     {
#                         "accepted_prefix_limit": {
#                             "idle_timeout_value": 2000,
#                             "limit_threshold": 99,
#                             "maximum": 20
#                         },
#                         "damping": true,
#                         "defer_initial_multipath_build": {
#                             "maximum_delay": 2
#                         },
#                         "delay_route_advertisements": {
#                             "max_delay_route_age": 20,
#                             "max_delay_routing_uptime": 32000,
#                             "min_delay_inbound_convergence": 32000,
#                             "min_delay_routing_uptime": 23000
#                         },
#                         "graceful_restart_forwarding_state_bit": "from-fib",
#                         "type": "any"
#                     },
#                     {
#                         "legacy_redirect_ip_action": {
#                             "receive": true,
#                             "send": true
#                         },
#                         "loops": 4,
#                         "no_install": true,
#                         "output_queue_priority_expedited": true,
#                         "secondary_independent_resolution": true,
#                         "type": "flow"
#                     },
#                     {
#                         "entropy_label": {
#                             "no_next_hop_validation": true
#                         },
#                         "explicit_null": {
#                             "connected_only": true
#                         },
#                         "per_group_label": true,
#                         "per_prefix_label": true,
#                         "prefix_limit": {
#                             "forever": true,
#                             "limit_threshold": 99,
#                             "maximum": 20
#                         },
#                         "resolve_vpn": true,
#                         "rib": "inet.3",
#                         "route_refresh_priority_priority": 3,
#                         "type": "labeled-unicast"
#                     },
#                     {
#                         "extended_nexthop": true,
#                         "extended_nexthop_color": true,
#                         "local_ipv4_address": "9.9.9.9",
#                         "type": "unicast"
#                     }
#                 ],
#                 "afi": "inet"
#             }
#         ]
#     }
#
# Using parsed
# parsed.cfg
# ------------
# <?xml version="1.0" encoding="UTF-8"?>
# <rpc-reply message-id="urn:uuid:0cadb4e8-5bba-47f4-986e-72906227007f">
#     <configuration changed-seconds="1590139550" changed-localtime="2020-05-22 09:25:50 UTC">
#         <version>18.4R1-S2.4</version>
#         <protocols>
#             <bgp>
#                 <preference>2</preference>
#                 <hold-time>5</hold-time>
#                 <advertise-inactive/>
#                 <out-delay>10</out-delay>
#                 <family>
#                     <inet>
#                         <unicast>
#                             <local-ipv4-address>9.9.9.9</local-ipv4-address>
#                             <extended-nexthop/>
#                             <extended-nexthop-color/>
#                         </unicast>
#                         <flow>
#                             <loops>
#                                 <loops>4</loops>
#                             </loops>
#                             <no-install/>
#                             <output-queue-priority>
#                                 <expedited/>
#                             </output-queue-priority>
#                             <legacy-redirect-ip-action>
#                                 <receive/>
#                                 <send/>
#                             </legacy-redirect-ip-action>
#                             <secondary-independent-resolution/>
#                         </flow>
#                         <any>
#                             <accepted-prefix-limit>
#                                 <maximum>20</maximum>
#                                 <teardown>
#                                     <limit-threshold>99</limit-threshold>
#                                     <idle-timeout>
#                                         <timeout>2000</timeout>
#                                     </idle-timeout>
#                                 </teardown>
#                             </accepted-prefix-limit>
#                             <damping/>
#                             <delay-route-advertisements>
#                                 <minimum-delay>
#                                     <routing-uptime>23000</routing-uptime>
#                                     <inbound-convergence>32000</inbound-convergence>
#                                 </minimum-delay>
#                                 <maximum-delay>
#                                     <route-age>20</route-age>
#                                     <routing-uptime>32000</routing-uptime>
#                                 </maximum-delay>
#                             </delay-route-advertisements>
#                             <defer-initial-multipath-build>
#                                 <maximum-delay>2</maximum-delay>
#                             </defer-initial-multipath-build>
#                             <graceful-restart>
#                                 <forwarding-state-bit>from-fib</forwarding-state-bit>
#                             </graceful-restart>
#                         </any>
#                         <labeled-unicast>
#                             <prefix-limit>
#                                 <maximum>20</maximum>
#                                 <teardown>
#                                     <limit-threshold>99</limit-threshold>
#                                     <idle-timeout>
#                                         <forever/>
#                                     </idle-timeout>
#                                 </teardown>
#                             </prefix-limit>
#                             <route-refresh-priority>
#                                 <priority>3</priority>
#                             </route-refresh-priority>
#                             <per-prefix-label/>
#                             <per-group-label/>
#                             <rib>
#                                 <inet.3/>
#                             </rib>
#                             <explicit-null>
#                                 <connected-only/>
#                             </explicit-null>
#                             <resolve-vpn/>
#                             <entropy-label>
#                                 <no-next-hop-validation/>
#                             </entropy-label>
#                         </labeled-unicast>
#                     </inet>
#                     <evpn>
#                         <signaling>
#                             <accepted-prefix-limit>
#                                 <maximum>20</maximum>
#                                 <teardown>
#                                     <limit-threshold>98</limit-threshold>
#                                     <idle-timeout>
#                                         <timeout>2001</timeout>
#                                     </idle-timeout>
#                                 </teardown>
#                             </accepted-prefix-limit>
#                             <damping/>
#                             <defer-initial-multipath-build>
#                                 <maximum-delay>2</maximum-delay>
#                             </defer-initial-multipath-build>
#                         </signaling>
#                     </evpn>
#                 </family>
#             </bgp>
#             <ospf3>
#                 <area>
#                     <name>0.0.0.100</name>
#                     <stub>
#                         <default-metric>200</default-metric>
#                     </stub>
#                     <interface>
#                         <name>so-0/0/0.0</name>
#                         <metric>5</metric>
#                         <priority>3</priority>
#                     </interface>
#                 </area>
#             </ospf3>
#         </protocols>
#         <routing-options>
#             <static>
#                 <route>
#                     <name>172.16.17.0/24</name>
#                     <discard />
#                 </route>
#             </static>
#             <router-id>10.200.16.75</router-id>
#             <autonomous-system>
#                 <as-number>65432</as-number>
#             </autonomous-system>
#         </routing-options>
#     </configuration>
# </rpc-reply>

- name: Parsed the bgp address family running config to get the facts
  junipernetworks.junos.junos_bgp_address_family:
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
#         "address_family": [
#             {
#                 "af_type": [
#                     {
#                         "accepted_prefix_limit": {
#                             "idle_timeout_value": 2001,
#                             "limit_threshold": 98,
#                             "maximum": 20
#                         },
#                         "damping": true,
#                         "defer_initial_multipath_build": {
#                             "maximum_delay": 2
#                         },
#                         "type": "signaling"
#                     }
#                 ],
#                 "afi": "evpn"
#             },
#             {
#                 "af_type": [
#                     {
#                         "accepted_prefix_limit": {
#                             "idle_timeout_value": 2000,
#                             "limit_threshold": 99,
#                             "maximum": 20
#                         },
#                         "damping": true,
#                         "defer_initial_multipath_build": {
#                             "maximum_delay": 2
#                         },
#                         "delay_route_advertisements": {
#                             "max_delay_route_age": 20,
#                             "max_delay_routing_uptime": 32000,
#                             "min_delay_inbound_convergence": 32000,
#                             "min_delay_routing_uptime": 23000
#                         },
#                         "graceful_restart_forwarding_state_bit": "from-fib",
#                         "type": "any"
#                     },
#                     {
#                         "legacy_redirect_ip_action": {
#                             "receive": true,
#                             "send": true
#                         },
#                         "loops": 4,
#                         "no_install": true,
#                         "output_queue_priority_expedited": true,
#                         "secondary_independent_resolution": true,
#                         "type": "flow"
#                     },
#                     {
#                         "entropy_label": {
#                             "no_next_hop_validation": true
#                         },
#                         "explicit_null": {
#                             "connected_only": true
#                         },
#                         "per_group_label": true,
#                         "per_prefix_label": true,
#                         "prefix_limit": {
#                             "forever": true,
#                             "limit_threshold": 99,
#                             "maximum": 20
#                         },
#                         "resolve_vpn": true,
#                         "rib": "inet.3",
#                         "route_refresh_priority_priority": 3,
#                         "type": "labeled-unicast"
#                     },
#                     {
#                         "extended_nexthop": true,
#                         "extended_nexthop_color": true,
#                         "local_ipv4_address": "9.9.9.9",
#                         "type": "unicast"
#                     }
#                 ],
#                 "afi": "inet"
#             }
#         ]
#     }
# Using rendered
#
#
- name: Render the commands for provided  configuration
  junipernetworks.junos.junos_bgp_address_family:
    config:
      address_family:
        - afi: 'evpn'
          af_type:
            - type: 'signaling'
              accepted_prefix_limit:
                maximum: 20
                limit_threshold: 98
                idle_timeout_value: 2001
              damping: true
              defer_initial_multipath_build:
                maximum_delay: 2
        - afi: 'inet'
          af_type:
            - type: 'flow'
              legacy_redirect_ip_action:
                send: true
                receive: true
              loops: 4
              no_install: true
              output_queue_priority_expedited: true
              secondary_independent_resolution: true

            - type: 'unicast'
              extended_nexthop: true
              extended_nexthop_color: true
              local_ipv4_address: '9.9.9.9'

            - type: 'labeled-unicast'
              entropy_label:
                no_next_hop_validation: true
              explicit_null:
                connected_only: true
              per_prefix_label: true
              per_group_label: true
              prefix_limit:
                maximum: 20
                limit_threshold: 99
                forever: true
              resolve_vpn: true
              rib: 'inet.3'
              route_refresh_priority_expedited: true
              route_refresh_priority_priority: 3

            - type: 'any'
              accepted_prefix_limit:
                maximum: 20
                limit_threshold: 99
                idle_timeout_value: 2000
              damping: true
              defer_initial_multipath_build:
                maximum_delay: 2
              delay_route_advertisements:
                max_delay_route_age: 20
                max_delay_routing_uptime: 32000
                min_delay_inbound_convergence: 32000
                min_delay_routing_uptime: 23000
              graceful_restart_forwarding_state_bit: 'from-fib'
    state: rendered

#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": "<nc:protocols xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0">
# <nc:bgp><nc:family><nc:evpn><nc:signaling><nc:accepted-prefix-limit><nc:maximum>20</nc:maximum>
# <nc:teardown><nc:limit-threshold>98</nc:limit-threshold><nc:idle-timeout><nc:timeout>2001</nc:timeout>
# </nc:idle-timeout></nc:teardown></nc:accepted-prefix-limit><nc:damping/><nc:defer-initial-multipath-build>
# <nc:maximum-delay>2</nc:maximum-delay></nc:defer-initial-multipath-build></nc:signaling>
# </nc:evpn><nc:inet><nc:flow><nc:legacy-redirect-ip-action><nc:send/><nc:receive/>
# </nc:legacy-redirect-ip-action><nc:loops>4</nc:loops><nc:no-install/>
# <nc:output-queue-priority><nc:expedited/></nc:output-queue-priority>
# <nc:secondary-independent-resolution/></nc:flow><nc:unicast><nc:extended-nexthop/>
# <nc:extended-nexthop-color/><nc:local-ipv4-address>9.9.9.9</nc:local-ipv4-address>
# </nc:unicast><nc:labeled-unicast><nc:entropy-label><nc:no-next-hop-validation/>
# </nc:entropy-label><nc:explicit-null><nc:connected-only/></nc:explicit-null>
# <nc:per-prefix-label/><nc:per-group-label/><nc:prefix-limit><nc:maximum>20</nc:maximum>
# <nc:teardown>99<nc:idle-timeout><nc:forever/></nc:idle-timeout></nc:teardown>
# </nc:prefix-limit><nc:resolve-vpn/><nc:rib><nc:inet.3/></nc:rib><nc:route-refresh-priority>
# <nc:expedited/><nc:priority>3</nc:priority></nc:route-refresh-priority></nc:labeled-unicast>
# <nc:any><nc:accepted-prefix-limit><nc:maximum>20</nc:maximum><nc:teardown>
# <nc:limit-threshold>99</nc:limit-threshold><nc:idle-timeout><nc:timeout>2000</nc:timeout>
# </nc:idle-timeout></nc:teardown></nc:accepted-prefix-limit><nc:damping/>
# <nc:defer-initial-multipath-build><nc:maximum-delay>2</nc:maximum-delay>
# </nc:defer-initial-multipath-build><nc:delay-route-advertisements>
# <nc:maximum-delay><nc:route-age>20</nc:route-age><nc:routing-uptime>32000</nc:routing-uptime>
# </nc:maximum-delay><nc:minimum-delay><nc:inbound-convergence>32000</nc:inbound-convergence>
# <nc:routing-uptime>23000</nc:routing-uptime></nc:minimum-delay></nc:delay-route-advertisements>
# <nc:graceful-restart><nc:forwarding-state-bit>from-fib</nc:forwarding-state-bit>
# </nc:graceful-restart></nc:any></nc:inet></nc:family></nc:bgp></nc:protocols>"
```

## [Return Values](junos_bgp_address_family_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  Returned: when changed  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  Returned: always  Sample: `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["<nc:protocols xmlns:nc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <nc:bgp><nc:family><nc:evpn><nc:signaling><nc:accepted-prefix-limit> <nc:maximum>21</nc:maximum><nc:teardown><nc:limit-threshold>99</nc:limit-threshold> <nc:idle-timeout><nc:timeout>2002</nc:timeout></nc:idle-timeout> </nc:teardown></nc:accepted-prefix-limit><nc:damping/> <nc:delay-route-advertisements><nc:maximum-delay> <nc:route-age>20</nc:route-age><nc:routing-uptime>32000</nc:routing-uptime> </nc:maximum-delay><nc:minimum-delay><nc:inbound-convergence>32000</nc:inbound-convergence> <nc:routing-uptime>23000</nc:routing-uptime></nc:minimum-delay></nc:delay-route-advertisements> </nc:signaling></nc:evpn></nc:family></nc:bgp></nc:protocols>", "xml 2", "xml 3"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
