---
collection: ansible
version: "8"
title: "cisco.ios.ios_bgp_global module – Resource module to configure BGP."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_bgp_global_module.html
fetched_at: 2026-07-28T01:26:07+00:00
---
# cisco.ios.ios_bgp_global module – Resource module to configure BGP.

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
> To use it in a playbook, specify: `cisco.ios.ios_bgp_global`.

New in cisco.ios 1.3.0

- [Synopsis](ios_bgp_global_module.md#synopsis)
- [Parameters](ios_bgp_global_module.md#parameters)
- [Notes](ios_bgp_global_module.md#notes)
- [Examples](ios_bgp_global_module.md#examples)
- [Return Values](ios_bgp_global_module.md#return-values)

## [Synopsis](ios_bgp_global_module.md#id1)

- This module configures and manages the attributes of global bgp on Cisco IOS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: bgp_global

## [Parameters](ios_bgp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A dictionary of options for bgp configurations. |
| **aggregate_address**  dictionary | Configure BGP aggregate entry  This option is DEPRECATED and is replaced with aggregate_addresses which accepts list of dict as input, this attribute will be removed after 2024-06-01. |
| **address**  string | Specify aggregate address |
| **advertise_map**  string | Set condition to advertise attribute |
| **as_confed_set**  boolean | Generate AS confed set path information  **Choices:**   - `false` - `true` |
| **as_set**  boolean | Generate AS set path information  **Choices:**   - `false` - `true` |
| **attribute_map**  string | Set attributes of aggregate |
| **netmask**  string | Specify aggregate mask |
| **summary_only**  boolean | Filter more specific routes from updates  **Choices:**   - `false` - `true` |
| **suppress_map**  string | Conditionally filter more specific routes from updates |
| **aggregate_addresses**  list / elements=dictionary | Configure BGP aggregate entries |
| **address**  string | Specify aggregate address |
| **advertise_map**  string | Set condition to advertise attribute |
| **as_confed_set**  boolean | Generate AS confed set path information  **Choices:**   - `false` - `true` |
| **as_set**  boolean | Generate AS set path information  **Choices:**   - `false` - `true` |
| **attribute_map**  string | Set attributes of aggregate |
| **netmask**  string | Specify aggregate mask |
| **summary_only**  boolean | Filter more specific routes from updates  **Choices:**   - `false` - `true` |
| **suppress_map**  string | Conditionally filter more specific routes from updates |
| **as_number**  string | Autonomous system number |
| **auto_summary**  boolean | Enable automatic network number summarization  **Choices:**   - `false` - `true` |
| **bgp**  dictionary | Enable address family and enter its config mode |
| **additional_paths**  dictionary | Additional paths in the BGP table |
| **install**  boolean | Additional paths to install into RIB  **Choices:**   - `false` - `true` |
| **receive**  boolean | Receive additional paths from neighbors  **Choices:**   - `false` - `true` |
| **select**  dictionary | Selection criteria to pick the paths |
| **all**  boolean | Select all available paths  **Choices:**   - `false` - `true` |
| **best**  integer | Select best N paths (2-3). |
| **best_external**  boolean | Select best-external path  **Choices:**   - `false` - `true` |
| **group_best**  boolean | Select group-best path  **Choices:**   - `false` - `true` |
| **send**  boolean | Send additional paths to neighbors  **Choices:**   - `false` - `true` |
| **advertise_best_external**  boolean | Advertise best external path to internal peers  **Choices:**   - `false` - `true` |
| **aggregate_timer**  integer | Configure Aggregation Timer  Please refer vendor documentation for valid values |
| **always_compare_med**  boolean | Allow comparing MED from different neighbors  **Choices:**   - `false` - `true` |
| **asnotation**  boolean | Change the default as plain notation  asdot notation  **Choices:**   - `false` - `true` |
| **bestpath**  list / elements=dictionary | Change the default bestpath selection  This option is DEPRECATED and replaced with bestpath_options of type dict, this attribute will be removed after 2024-06-01. |
| **aigp**  boolean | if both paths doesn’t have aigp ignore on bestpath comparison  ignore  **Choices:**   - `false` - `true` |
| **compare_routerid**  boolean | Compare router-id for identical EBGP paths  **Choices:**   - `false` - `true` |
| **cost_community**  boolean | cost community  **Choices:**   - `false` - `true` |
| **igp_metric**  boolean | igp metric  Ignore igp metric in bestpath selection  **Choices:**   - `false` - `true` |
| **med**  dictionary | MED attribute |
| **confed**  boolean | Compare MED among confederation paths  **Choices:**   - `false` - `true` |
| **missing_as_worst**  boolean | Treat missing MED as the least preferred one  **Choices:**   - `false` - `true` |
| **bestpath_options**  dictionary | Change the default bestpath selection |
| **aigp**  boolean | if both paths doesn’t have aigp ignore on bestpath comparison  ignore  **Choices:**   - `false` - `true` |
| **compare_routerid**  boolean | Compare router-id for identical EBGP paths  **Choices:**   - `false` - `true` |
| **cost_community**  boolean | cost community  **Choices:**   - `false` - `true` |
| **igp_metric**  boolean | igp metric  Ignore igp metric in bestpath selection  **Choices:**   - `false` - `true` |
| **med**  dictionary | MED attribute |
| **confed**  boolean | Compare MED among confederation paths  **Choices:**   - `false` - `true` |
| **missing_as_worst**  boolean | Treat missing MED as the least preferred one  **Choices:**   - `false` - `true` |
| **client_to_client**  dictionary | Configure client to client route reflection |
| **all**  boolean | inter-cluster and intra-cluster (default)  **Choices:**   - `false` - `true` |
| **intra_cluster**  string | intra cluster reflection  intra-cluster reflection for cluster-id |
| **set**  boolean | set reflection of routes allowed  **Choices:**   - `false` - `true` |
| **cluster_id**  string | Configure Route-Reflector Cluster-id (peers may reset)  A.B.C.D/Please refer vendor documentation for valid Route-Reflector Cluster-id |
| **confederation**  dictionary | AS confederation parameters |
| **identifier**  string | Set routing domain confederation AS  AS number |
| **peers**  string | Peer ASs in BGP confederation  AS number |
| **consistency_checker**  dictionary | Consistency-checker |
| **auto_repair**  dictionary | Auto-Repair |
| **interval**  integer | Set the bgp consistency checker  Please refer vendor documentation for valid values |
| **set**  boolean | Enable Auto-Repair  **Choices:**   - `false` - `true` |
| **error_message**  dictionary | Log Error-Msg |
| **interval**  integer | Set the bgp consistency checker  Please refer vendor documentation for valid values |
| **set**  boolean | Enable Error-Msg  **Choices:**   - `false` - `true` |
| **dampening**  dictionary | Enable route-flap dampening |
| **max_suppress**  integer | Maximum duration to suppress a stable route  Please refer vendor documentation for valid values |
| **penalty_half_time**  integer | Half-life time for the penalty  Please refer vendor documentation for valid values |
| **reuse_route_val**  integer | Value to start reusing a route  Please refer vendor documentation for valid values |
| **route_map**  string | Route-map to specify criteria for dampening |
| **suppress_route_val**  integer | Value to start suppressing a route  Please refer vendor documentation for valid values |
| **deterministic_med**  boolean | Pick the best-MED path among paths advertised from the neighboring AS  **Choices:**   - `false` - `true` |
| **dmzlink_bw**  boolean | Use DMZ Link Bandwidth as weight for BGP multipaths  **Choices:**   - `false` - `true` |
| **enforce_first_as**  boolean | Enforce the first AS for EBGP routes(default)  **Choices:**   - `false` - `true` |
| **enhanced_error**  boolean | Enabled BGP Enhanced error handling  **Choices:**   - `false` - `true` |
| **fast_external_fallover**  boolean | Immediately reset session if a link to a directly connected external peer goes down  **Choices:**   - `false` - `true` |
| **graceful_restart**  dictionary | Graceful restart capability parameters |
| **extended**  boolean | Enable Graceful-Restart Extension  **Choices:**   - `false` - `true` |
| **restart_time**  integer | Set the max time needed to restart and come back up  Please refer vendor documentation for valid values |
| **set**  boolean | Set Graceful-Restart  **Choices:**   - `false` - `true` |
| **stalepath_time**  integer | Set the max time to hold onto restarting peer’s stale paths  Please refer vendor documentation for valid values |
| **graceful_shutdown**  dictionary | Graceful shutdown capability parameters |
| **community**  string | Set Community for Gshut routes  community number/community number in aa:nn format |
| **local_preference**  integer | Set Local Preference for Gshut routes  Please refer vendor documentation for valid values |
| **neighbors**  dictionary | Gracefully shut down all neighbors |
| **activate**  boolean | Activate graceful shutdown of all neighbors  **Choices:**   - `false` - `true` |
| **time**  integer | time in seconds  Please refer vendor documentation for valid values |
| **vrfs**  dictionary | Gracefully shut down all vrf neighbors |
| **activate**  boolean | Activate graceful shutdown of all neighbors  **Choices:**   - `false` - `true` |
| **time**  integer | time in seconds  Please refer vendor documentation for valid values |
| **inject_map**  dictionary | Routemap which specifies prefixes to inject  This option is DEPRECATED and is updated with inject_maps which is a list of dict, this attribute will be removed after 2024-06-01. |
| **copy_attributes**  boolean | Copy attributes from aggregate  **Choices:**   - `false` - `true` |
| **exist_map_name**  string | route-map name |
| **name**  string | route-map name |
| **inject_maps**  list / elements=dictionary | Routemap which specifies prefixes to inject |
| **copy_attributes**  boolean | Copy attributes from aggregate  **Choices:**   - `false` - `true` |
| **exist_map_name**  string | route-map name |
| **name**  string | route-map name |
| **listen**  dictionary | Neighbor subnet range listener |
| **limit**  integer | Set the max limit for the dynamic subnet range neighbors  Please refer vendor documentation for valid values |
| **range**  dictionary | Subnet network range |
| **host_with_subnet**  string | IPv4 subnet range(A.B.C.D/nn)  IPv6 subnet range(X:X:X:X::X/<0-128>) |
| **ipv4_with_subnet**  string | IPv4 subnet range(A.B.C.D/nn)  This option is DEPRECATED and is updated with host_with_subnet which is a common attribute for address, this attribute will be removed after 2024-06-01. |
| **ipv6_with_subnet**  string | IPv6 subnet range(X:X:X:X::X/<0-128>)  This option is DEPRECATED and is updated with host_with_subnet which is a common attribute for address attribute will be removed after 2024-06-01. |
| **peer_group**  string | Member of the peer-group |
| **log_neighbor_changes**  boolean | Log neighbor up/down and reset reason  **Choices:**   - `false` - `true` |
| **maxas_limit**  integer | Allow AS-PATH attribute from any neighbor imposing a limit on number of ASes  Please refer vendor documentation for valid values |
| **maxcommunity_limit**  integer | Allow COMMUNITY attribute from any neighbor imposing a limit on number of communities  Please refer vendor documentation for valid values |
| **maxextcommunity_limit**  integer | Allow EXTENDED COMMUNITY attribute from any neighbor imposing a limit on number of extended communities  Please refer vendor documentation for valid values |
| **nexthop**  dictionary | Nexthop tracking commands |
| **route_map**  string | Route map for valid nexthops |
| **trigger**  dictionary | nexthop trackings |
| **delay**  integer | Set the delay to trigger nexthop tracking  Please refer vendor documentation for valid values |
| **enable**  boolean | Enable nexthop tracking  **Choices:**   - `false` - `true` |
| **nopeerup_delay**  list / elements=dictionary | Set how long BGP will wait for the first peer to come up before beginning the update delay or graceful restart timers (in seconds)  This option is DEPRECATED and is replaced with nopeerup_delay_options which is of type dict, this attribute will be removed after 2024-06-01. |
| **cold_boot**  integer | How long to wait for the first peer to come up upon a cold boot  Please refer vendor documentation for valid values |
| **nsf_switchover**  integer | How long to wait for the first peer, post NSF switchover  Please refer vendor documentation for valid values |
| **post_boot**  integer | How long to wait for the first peer to come up once the system is already booted and all peers go down  Please refer vendor documentation for valid values |
| **user_initiated**  integer | How long to wait for the first peer, post a manual clear of BGP peers by the admin user  Please refer vendor documentation for valid values |
| **nopeerup_delay_options**  dictionary | Set how long BGP will wait for the first peer to come up before beginning the update delay or graceful restart timers (in seconds) |
| **cold_boot**  integer | How long to wait for the first peer to come up upon a cold boot  Please refer vendor documentation for valid values |
| **nsf_switchover**  integer | How long to wait for the first peer, post NSF switchover  Please refer vendor documentation for valid values |
| **post_boot**  integer | How long to wait for the first peer to come up once the system is already booted and all peers go down  Please refer vendor documentation for valid values |
| **user_initiated**  integer | How long to wait for the first peer, post a manual clear of BGP peers by the admin user  Please refer vendor documentation for valid values |
| **recursion**  boolean | recursion rule for the nexthops  recursion via host for the nexthops  **Choices:**   - `false` - `true` |
| **redistribute_internal**  boolean | Allow redistribution of iBGP into IGPs (dangerous)  **Choices:**   - `false` - `true` |
| **refresh**  dictionary | refresh |
| **max_eor_time**  integer | Configure refresh max-eor time  Please refer vendor documentation for valid values |
| **stalepath_time**  integer | Configure refresh stale-path time  Please refer vendor documentation for valid values |
| **regexp**  boolean | Select regular expression engine  Enable bounded-execution-time regular expression engine  **Choices:**   - `false` - `true` |
| **route_map**  boolean | route-map control commands  Have route-map set commands take priority over BGP commands such as next-hop unchanged  **Choices:**   - `false` - `true` |
| **router_id**  dictionary | Override configured router identifier (peers will reset) |
| **address**  string | Manually configured router identifier(A.B.C.D) |
| **interface**  string | Use IPv4 address on interface |
| **vrf**  boolean | vrf-specific router id configuration  Automatically assign per-vrf bgp router id  **Choices:**   - `false` - `true` |
| **scan_time**  integer | Configure background scanner interval  Please refer vendor documentation for valid values |
| **slow_peer**  dictionary | Configure slow-peer |
| **detection**  dictionary | Slow-peer detection |
| **set**  boolean | Slow-peer detection  **Choices:**   - `false` - `true` |
| **threshold**  integer | Set the slow-peer detection threshold  Please refer vendor documentation for valid values |
| **split_update_group**  dictionary | Configure slow-peer split-update-group |
| **dynamic**  boolean | Dynamically split the slow peer to slow-update group  **Choices:**   - `false` - `true` |
| **permanent**  boolean | Keep the slow-peer permanently in slow-update group  **Choices:**   - `false` - `true` |
| **snmp**  boolean | BGP SNMP options  BGP SNMP trap options  Use cbgp Peer2Type as part of index for traps  **Choices:**   - `false` - `true` |
| **soft_reconfig_backup**  boolean | Use soft-reconfiguration inbound only when route-refresh is not negotiated  **Choices:**   - `false` - `true` |
| **sso**  boolean | Stateful Switchover  Enable SSO only for Route-Refresh capable peers  **Choices:**   - `false` - `true` |
| **suppress_inactive**  boolean | Suppress routes that are not in the routing table  **Choices:**   - `false` - `true` |
| **transport**  boolean | Global enable/disable transport session parameters  Transport path MTU discovery  **Choices:**   - `false` - `true` |
| **update_delay**  integer | Set the max initial delay for sending update  Please refer vendor documentation for valid values |
| **update_group**  boolean | Manage peers in bgp update groups  Split update groups based on Policy  Keep peers with as-override in different update groups  **Choices:**   - `false` - `true` |
| **upgrade_cli**  dictionary | Upgrade to hierarchical AFI mode |
| **af_mode**  boolean | Upgrade to AFI mode  **Choices:**   - `false` - `true` |
| **set**  boolean | enable upgrade to hierarchical AFI mode  **Choices:**   - `false` - `true` |
| **bmp**  dictionary | BGP Monitoring Protocol |
| **buffer_size**  integer | BMP Buffer Size  Please refer vendor documentation for valid values |
| **initial_refresh**  dictionary | Initial Refresh options |
| **delay**  integer | Delay before Initial Refresh |
| **skip**  boolean | skip all refreshes  **Choices:**   - `false` - `true` |
| **server**  integer | Server Information  Please refer vendor documentation for valid values |
| **server_options**  dictionary | bmp server options |
| **activate**  boolean | activate server  **Choices:**   - `false` - `true` |
| **address**  dictionary | skip all refreshes |
| **host**  string | host address |
| **port**  integer | port number BMP server |
| **default_information**  boolean | Control distribution of default information  Distribute a default route  **Choices:**   - `false` - `true` |
| **default_metric**  integer | Set metric of redistributed routes  Please refer vendor documentation for valid values |
| **distance**  dictionary | Define an administrative distance |
| **admin**  dictionary | Administrative distance |
| **acl**  string | IP Standard access list number  IP Standard expanded access list number  Standard access-list name |
| **address**  string | IP Source address (A.B.C.D) |
| **distance**  integer | Administrative distance  Please refer vendor documentation for valid values |
| **wildcard_bit**  string | Wildcard bits (A.B.C.D) |
| **bgp**  dictionary | BGP distance |
| **routes_external**  integer | Distance for routes external to the AS  Please refer vendor documentation for valid values |
| **routes_internal**  integer | Distance for routes internal to the AS  Please refer vendor documentation for valid values |
| **routes_local**  integer | Distance for local routes  Please refer vendor documentation for valid values |
| **mbgp**  dictionary | MBGP distance |
| **routes_external**  integer | Distance for routes external to the AS  Please refer vendor documentation for valid values |
| **routes_internal**  integer | Distance for routes internal to the AS  Please refer vendor documentation for valid values |
| **routes_local**  integer | Distance for local routes  Please refer vendor documentation for valid values |
| **distribute_list**  dictionary | Filter networks in routing updates  This option is DEPRECATED and is replaced with distributes which is of type list of dict, this attribute will be removed after 2024-06-01. |
| **acl**  string | IP access list number/name |
| **in**  boolean | Filter incoming routing updates  **Choices:**   - `false` - `true` |
| **interface**  string | interface details |
| **out**  boolean | Filter outgoing routing updates  **Choices:**   - `false` - `true` |
| **distributes**  list / elements=dictionary | Filter networks in routing updates |
| **acl**  string | IP access list number/name |
| **gateway**  string | Filter prefixes in routing updates |
| **in**  boolean | Filter incoming routing updates  **Choices:**   - `false` - `true` |
| **interface**  string | interface details |
| **out**  boolean | Filter outgoing routing updates  **Choices:**   - `false` - `true` |
| **prefix**  string | Filtering incoming updates based on gateway |
| **maximum_paths**  dictionary | Forward packets over multiple paths |
| **eibgp**  integer | Both eBGP and iBGP paths as multipath |
| **ibgp**  integer | iBGP-multipath |
| **paths**  integer | Number of paths |
| **maximum_secondary_paths**  dictionary | Maximum secondary paths |
| **eibgp**  integer | Both eBGP and iBGP paths as secondary multipath |
| **ibgp**  integer | iBGP-secondary-multipath |
| **paths**  integer | Number of secondary paths |
| **neighbors**  aliases: neighbor  list / elements=dictionary | Specify a neighbor router |
| **activate**  boolean | Enable the Address Family for this Neighbor  **Choices:**   - `false` - `true` |
| **additional_paths**  dictionary | Negotiate additional paths capabilities with this neighbor |
| **disable**  boolean | Disable additional paths for this neighbor  **Choices:**   - `false` - `true` |
| **receive**  boolean | Receive additional paths from neighbors  **Choices:**   - `false` - `true` |
| **send**  boolean | Send additional paths to neighbors  **Choices:**   - `false` - `true` |
| **address**  string | Neighbor address (A.B.C.D)  This option is DEPRECATED and replaced with neighbor_address, this attribute will be removed after 2024-06-01. |
| **advertise**  dictionary | Advertise to this neighbor |
| **additional_paths**  dictionary | Advertise additional paths |
| **all**  boolean | Select all available paths  **Choices:**   - `false` - `true` |
| **best**  integer | Select best N paths (2-3). |
| **group_best**  boolean | Select group-best path  **Choices:**   - `false` - `true` |
| **best_external**  boolean | Advertise best-external (at RRs best-internal) path  **Choices:**   - `false` - `true` |
| **diverse_path**  dictionary | Advertise additional paths |
| **backup**  boolean | Diverse path can be backup path  **Choices:**   - `false` - `true` |
| **mpath**  boolean | Diverse path can be multipath  **Choices:**   - `false` - `true` |
| **advertise_map**  dictionary | specify route-map for conditional advertisement |
| **exist_map**  string | advertise prefix only if prefix is in the condition exists  condition route-map name |
| **name**  string | advertise route-map name |
| **non_exist_map**  string | advertise prefix only if prefix in the condition does not exist  condition route-map name |
| **advertisement_interval**  integer | Minimum interval between sending BGP routing updates |
| **aigp**  dictionary | AIGP on neighbor |
| **enable**  boolean | Enable AIGP  **Choices:**   - `false` - `true` |
| **send**  dictionary | Cost community or MED carrying AIGP VALUE |
| **cost_community**  dictionary | Cost extended community carrying AIGP Value |
| **id**  integer | Community ID  Please refer vendor documentation for valid values |
| **poi**  dictionary | Point of Insertion |
| **igp_cost**  boolean | Point of Insertion After IGP  **Choices:**   - `false` - `true` |
| **pre_bestpath**  boolean | Point of Insertion At Beginning  **Choices:**   - `false` - `true` |
| **transitive**  boolean | Cost community is Transitive  **Choices:**   - `false` - `true` |
| **med**  boolean | Med carrying AIGP Value  **Choices:**   - `false` - `true` |
| **allow_policy**  boolean | Enable the policy support for this IBGP Neighbor  **Choices:**   - `false` - `true` |
| **allowas_in**  integer | Accept as-path with my AS present in it |
| **as_override**  boolean | Override matching AS-number while sending update  Maintain Split Horizon while sending update  **Choices:**   - `false` - `true` |
| **bmp_activate**  dictionary | Activate the BMP monitoring for a BGP peer |
| **all**  boolean | Activate BMP monitoring for all servers  **Choices:**   - `false` - `true` |
| **server**  integer | Activate BMP for server  BMP Server Number  Please refer vendor documentation for valid values |
| **capability**  dictionary | Advertise capability to the peer  Advertise ORF capability to the peer  Advertise prefix-list ORF capability to this neighbor |
| **both**  boolean | Capability to SEND and RECEIVE the ORF to/from this neighbor  **Choices:**   - `false` - `true` |
| **receive**  boolean | Capability to RECEIVE the ORF from this neighbor  **Choices:**   - `false` - `true` |
| **send**  boolean | Capability to SEND the ORF to this neighbor  **Choices:**   - `false` - `true` |
| **cluster_id**  string | Configure Route-Reflector Cluster-id (peers may reset)  Route-Reflector Cluster-id as 32 bit quantity, or Route-Reflector Cluster-id in IP address format (A.B.C.D) |
| **default_originate**  dictionary | Originate default route to this neighbor |
| **route_map**  string | Route-map to specify criteria to originate default |
| **set**  boolean | Originate default route to this neighbor  **Choices:**   - `false` - `true` |
| **description**  string | Neighbor specific description |
| **disable_connected_check**  boolean | one-hop away EBGP peer using loopback address  **Choices:**   - `false` - `true` |
| **distribute_list**  dictionary | Filter updates to/from this neighbor |
| **acl**  string | IP access list number/name |
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
| **in**  boolean | Filter incoming updates  **Choices:**   - `false` - `true` |
| **out**  boolean | Filter outgoing updates  **Choices:**   - `false` - `true` |
| **path_acl**  string | AS path access list |
| **ha_mode**  dictionary | high availability mode |
| **disable**  boolean | disable graceful-restart  **Choices:**   - `false` - `true` |
| **set**  boolean | set ha-mode and graceful-restart for this peer  **Choices:**   - `false` - `true` |
| **inherit**  string | Inherit a template  Inherit a peer-session template and Template name |
| **ipv6_adddress**  string | Neighbor ipv6 address (X:X:X:X::X)  This option is DEPRECATED and replaced with neighbor_address, this attribute will be removed after 2024-06-01. |
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
| **maximum_prefix**  dictionary | Maximum number of prefixes accepted from this peer |
| **max_no**  integer | maximum no. of prefix limit |
| **restart**  integer | Restart bgp connection after limit is exceeded |
| **threshold_val**  integer | Threshold value (%) at which to generate a warning msg |
| **warning_only**  boolean | Only give warning message when limit is exceeded  **Choices:**   - `false` - `true` |
| **neighbor_address**  string | Neighbor address (A.B.C.D)  Neighbor tag  Neighbor ipv6 address (X:X:X:X::X) |
| **next_hop_self**  dictionary | Disable the next hop calculation for this neighbor |
| **all**  boolean | Enable next-hop-self for both eBGP and iBGP received paths  **Choices:**   - `false` - `true` |
| **set**  boolean | Enable next-hop-self  **Choices:**   - `false` - `true` |
| **next_hop_unchanged**  dictionary | Propagate next hop unchanged for iBGP paths to this neighbor  Propagate next hop unchanged for all paths (iBGP and eBGP) to this neighbor |
| **allpaths**  boolean | Propagate next hop unchanged for all paths (iBGP and eBGP) to this neighbor  **Choices:**   - `false` - `true` |
| **set**  boolean | Enable next-hop-unchanged  **Choices:**   - `false` - `true` |
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
| **peer_group**  string | Member of the peer-group |
| **remote_as**  string | Specify a BGP neighbor  AS of remote neighbor |
| **remove_private_as**  dictionary | Remove private AS number from outbound updates |
| **all**  boolean | Remove all private AS numbers  **Choices:**   - `false` - `true` |
| **replace_as**  boolean | Replace all private AS numbers with local AS  **Choices:**   - `false` - `true` |
| **set**  boolean | Remove private AS number  **Choices:**   - `false` - `true` |
| **route_map**  dictionary | Apply route map to neighbor  This option is DEPRECATED and is replaced with route_maps which accepts list of dict as input, this attribute will be removed after 2024-06-01. |
| **in**  boolean | Apply map to incoming routes  **Choices:**   - `false` - `true` |
| **name**  string | Replace all private AS numbers with local AS |
| **out**  boolean | Apply map to outbound routes  **Choices:**   - `false` - `true` |
| **route_maps**  list / elements=dictionary | Apply a list of route maps to neighbor |
| **in**  boolean | Apply map to incoming routes  **Choices:**   - `false` - `true` |
| **name**  string | Replace all private AS numbers with local AS |
| **out**  boolean | Apply map to outbound routes  **Choices:**   - `false` - `true` |
| **route_reflector_client**  boolean | Configure a neighbor as Route Reflector client  **Choices:**   - `false` - `true` |
| **route_server_client**  dictionary | Configure a neighbor as Route Server client |
| **context**  string | Specify Route Server context for neighbor  Route Server context name |
| **set**  boolean | Set Route Server client  **Choices:**   - `false` - `true` |
| **send_community**  dictionary | Send Community attribute to this neighbor |
| **both**  boolean | Send Standard and Extended Community attributes  **Choices:**   - `false` - `true` |
| **extended**  boolean | Send Extended Community attribute  **Choices:**   - `false` - `true` |
| **set**  boolean | Set send Community attribute to this neighbor  **Choices:**   - `false` - `true` |
| **standard**  boolean | Send Standard Community attribute  **Choices:**   - `false` - `true` |
| **send_label**  dictionary | Send NLRI + MPLS Label to this peer |
| **explicit_null**  boolean | Advertise Explicit Null label in place of Implicit Null  **Choices:**   - `false` - `true` |
| **set**  boolean | Set send NLRI + MPLS Label to this peer  **Choices:**   - `false` - `true` |
| **shutdown**  dictionary | Administratively shut down this neighbor |
| **community**  integer | Set Community for Gshut routes |
| **graceful**  integer | Gracefully shut down this neighbor  time in seconds  Please refer vendor documentation for valid values |
| **local_preference**  boolean | Set Local Preference for Gshut routes  **Choices:**   - `false` - `true` |
| **set**  boolean | shut down  **Choices:**   - `false` - `true` |
| **slow_peer**  dictionary | Configure slow-peer |
| **detection**  dictionary | Configure slow-peer |
| **disable**  boolean | Disable slow-peer detection  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable slow-peer detection  **Choices:**   - `false` - `true` |
| **threshold**  integer | Set the slow-peer detection threshold |
| **split_update_group**  dictionary | Configure slow-peer split-update-group |
| **dynamic**  dictionary | Dynamically split the slow peer to slow-update group |
| **disable**  boolean | Disable slow-peer detection  **Choices:**   - `false` - `true` |
| **enable**  boolean | Enable slow-peer detection  **Choices:**   - `false` - `true` |
| **permanent**  boolean | Keep the slow-peer permanently in slow-update group  **Choices:**   - `false` - `true` |
| **static**  boolean | Static slow-peer  **Choices:**   - `false` - `true` |
| **soft_reconfiguration**  boolean | Per neighbor soft reconfiguration  Allow inbound soft reconfiguration for this neighbor  **Choices:**   - `false` - `true` |
| **tag**  string | Neighbor tag  This option is DEPRECATED and replaced with neighbor_address, this attribute will be removed after 2024-06-01. |
| **timers**  dictionary | BGP per neighbor timers |
| **holdtime**  integer | Holdtime |
| **interval**  integer | Keepalive interval |
| **min_holdtime**  integer | Minimum hold time from neighbor |
| **translate_update**  dictionary | Translate Update to MBGP format |
| **nlri**  dictionary | Specify type of nlri to translate to |
| **multicast**  boolean | Translate Update to multicast nlri  **Choices:**   - `false` - `true` |
| **unicast**  boolean | Process Update as unicast nlri  **Choices:**   - `false` - `true` |
| **set**  boolean | Set Translate Update  **Choices:**   - `false` - `true` |
| **transport**  dictionary | Transport options |
| **connection_mode**  dictionary | Specify passive or active connection |
| **active**  boolean | Actively establish the TCP session  **Choices:**   - `false` - `true` |
| **passive**  boolean | Passively establish the TCP session  **Choices:**   - `false` - `true` |
| **multi_session**  boolean | Use Multi-session for transport  **Choices:**   - `false` - `true` |
| **path_mtu_discovery**  dictionary | Use transport path MTU discovery |
| **disable**  boolean | disable  **Choices:**   - `false` - `true` |
| **set**  boolean | Use path MTU discovery  **Choices:**   - `false` - `true` |
| **ttl_security**  integer | BGP ttl security check  maximum number of hops  Please refer vendor documentation for valid values |
| **unsuppress_map**  string | Route-map to selectively un-suppress suppressed routes  Name of route map |
| **update_source**  string | Source of routing updates |
| **version**  integer | Set the BGP version to match a neighbor  Neighbor’s BGP version  Please refer vendor documentation for valid values |
| **weight**  integer | Set default weight for routes from this neighbor |
| **networks**  list / elements=dictionary | Specify a network to announce via BGP |
| **address**  string | Specify network address |
| **backdoor**  boolean | Specify a BGP backdoor route  **Choices:**   - `false` - `true` |
| **netmask**  string | Specify network mask |
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
| **set**  boolean | Set the top level attribute  **Choices:**   - `false` - `true` |
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
| **match**  dictionary | On Demand stub Routes |
| **external**  boolean | Redistribute OSPF external routes  **Choices:**   - `false` - `true` |
| **internal**  boolean | Redistribute OSPF internal routes  **Choices:**   - `false` - `true` |
| **nssa_external**  boolean | Redistribute OSPF NSSA external routes  **Choices:**   - `false` - `true` |
| **type_1**  boolean | Redistribute NSSA external type 1 routes  **Choices:**   - `false` - `true` |
| **type_2**  boolean | Redistribute NSSA external type 2 routes  **Choices:**   - `false` - `true` |
| **metric**  integer | Metric for redistributed routes |
| **process_id**  integer | Process ID |
| **route_map**  string | Route map reference |
| **vrf**  string | VPN Routing/Forwarding Instance |
| **ospfv3**  dictionary | OSPFv3 |
| **match**  dictionary | On Demand stub Routes |
| **external**  boolean | Redistribute OSPF external routes  **Choices:**   - `false` - `true` |
| **internal**  boolean | Redistribute OSPF internal routes  **Choices:**   - `false` - `true` |
| **nssa_external**  boolean | Redistribute OSPF NSSA external routes  **Choices:**   - `false` - `true` |
| **type_1**  boolean | Redistribute NSSA external type 1 routes  **Choices:**   - `false` - `true` |
| **type_2**  boolean | Redistribute NSSA external type 2 routes  **Choices:**   - `false` - `true` |
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
| **route_server_context**  dictionary | Enter route server context command mode  This option is DEPRECATED as it is out of scope of the module, this attribute will be removed after 2024-06-01. |
| **address_family**  dictionary | Enter address family command mode |
| **afi**  string | Address family  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **import_map**  string | Import matching routes using a route map  Name of route map |
| **modifier**  string | Address Family modifier  **Choices:**   - `"multicast"` - `"unicast"` |
| **description**  string | Textual description of the router server context |
| **name**  string | Name of route server context |
| **scope**  dictionary | Enter scope command mode  This option is DEPRECATED as is not valid within the scope of module, this attribute will be removed after 2024-06-01. |
| **global**  boolean | Global scope  **Choices:**   - `false` - `true` |
| **vrf**  string | VRF scope  VPN Routing/Forwarding instance name |
| **synchronization**  boolean | Perform IGP synchronization  **Choices:**   - `false` - `true` |
| **table_map**  dictionary | Map external entry attributes into routing table |
| **filter**  boolean | Selective route download  **Choices:**   - `false` - `true` |
| **name**  string | route-map name |
| **template**  dictionary | Enter template command mode  This option is DEPRECATED as is not valid within the scope of module, this attribute will be removed after 2024-06-01. |
| **peer_policy**  string | Template configuration for policy parameters |
| **peer_session**  string | Template configuration for session parameters |
| **timers**  dictionary | Adjust routing timers  BGP timers |
| **holdtime**  integer | Holdtime |
| **keepalive**  integer | Keepalive interval |
| **min_holdtime**  integer | Minimum hold time from neighbor |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **sh running-config | section ^router bgp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"purged"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](ios_bgp_global_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - The module examples uses callback plugin (stdout_callback = yaml) to generate task output in yaml format.

## [Examples](ios_bgp_global_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# vios#sh running-config | section ^router bgp

- name: Merge provided configuration with device configuration
  cisco.ios.ios_bgp_global:
    config:
      as_number: 65000
      bgp:
        advertise_best_external: true
        bestpath:
          - compare_routerid: true
        dampening:
          penalty_half_time: 1
          reuse_route_val: 1
          suppress_route_val: 1
          max_suppress: 1
        graceful_shutdown:
          neighbors:
            time: 50
          community: 100
          local_preference: 100
        log_neighbor_changes: true
        nopeerup_delay:
          - post_boot: 10
      networks:
        - address: 192.0.2.3
        - address: 192.0.2.2
      neighbor:
        - address: 192.0.2.1
          description: merge neighbor
          remote_as: 100
          aigp:
            send:
              cost_community:
                id: 100
                poi:
                  igp_cost: true
                  transitive: true
          route_map:
            name: test-route
            out: true
      redistribute:
        - connected:
            metric: 10
      timers:
        keepalive: 100
        holdtime: 200
        min_holdtime: 150
    state: merged

# Task Output:
# ------------
#
# before: {}
# commands:
# - router bgp 65000
# - timers bgp 100 200 150
# - bgp advertise-best-external
# - bgp bestpath compare-routerid
# - bgp dampening 1 1 1 1
# - bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
# - bgp log-neighbor-changes
# - bgp nopeerup-delay post-boot 10
# - network 192.0.2.3
# - network 192.0.2.2
# - neighbor 192.0.2.1 remote-as 100
# - neighbor 192.0.2.1 description merge neighbor
# - neighbor 192.0.2.1 aigp send cost-community 100 poi igp-cost transitive
# - neighbor 192.0.2.1 route-map test-route out
# - redistribute connected metric 10
# after:
#   as_number: '65000'
#   bgp:
#     advertise_best_external: true
#     bestpath_options:
#       compare_routerid: true
#     dampening:
#       max_suppress: 1
#       penalty_half_time: 1
#       reuse_route_val: 1
#       suppress_route_val: 1
#     graceful_shutdown:
#       community: '100'
#       local_preference: 100
#       neighbors:
#         time: 50
#     log_neighbor_changes: true
#     nopeerup_delay_options:
#       post_boot: 10
#   neighbors:
#   - aigp:
#       send:
#         cost_community:
#           id: 100
#           poi:
#             igp_cost: true
#             transitive: true
#     description: merge neighbor
#     neighbor_address: 192.0.2.1
#     remote_as: '100'
#     route_maps:
#     - name: test-route
#       out: true
#   networks:
#   - address: 192.0.2.2
#   - address: 192.0.2.3
#   redistribute:
#   - connected:
#       metric: 10
#       set: true
#   timers:
#     holdtime: 200
#     keepalive: 100
#     min_holdtime: 150

# After state:
# ------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp nopeerup-delay post-boot 10
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  bgp bestpath compare-routerid
#  bgp dampening 1 1 1 1
#  bgp advertise-best-external
#  network 192.0.2.2
#  network 192.0.2.3
#  timers bgp 100 200 150
#  redistribute connected metric 10
#  neighbor 192.0.2.1 remote-as 100
#  neighbor 192.0.2.1 description merge neighbor
#  neighbor 192.0.2.1 aigp send cost-community 100 poi igp-cost transitive
#  neighbor 192.0.2.1 route-map test-route out

# Using replaced

# Before state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp nopeerup-delay post-boot 10
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  bgp bestpath compare-routerid
#  bgp dampening 1 1 1 1
#  network 192.0.2.2
#  network 192.0.2.3
#  bgp advertise-best-external
#  neighbor 198.0.2.1 remote-as 100
#  neighbor 198.0.2.1 description merge neighbor
#  neighbor 198.0.2.1 aigp send cost-community 100 poi igp-cost transitive
#  neighbor 198.0.2.1 route-map test-route out

- name: Replaces device configuration of listed global BGP with provided configuration
  cisco.ios.ios_bgp_global:
    config:
      as_number: 65000
      bgp:
        advertise_best_external: true
        bestpath:
          - med:
              confed: true
        log_neighbor_changes: true
        nopeerup_delay:
          - post_boot: 10
            cold_boot: 20
      networks:
        - address: 192.0.2.4
      neighbor:
        - address: 192.0.2.5
          description: replace neighbor
          remote_as: 100
          slow_peer:
            detection:
              disable: true
    state: replaced

# Task Output:
# ------------
#
# before:
#   as_number: '65000'
#   bgp:
#     advertise_best_external: true
#     bestpath_options:
#       compare_routerid: true
#     dampening:
#       max_suppress: 1
#       penalty_half_time: 1
#       reuse_route_val: 1
#       suppress_route_val: 1
#     graceful_shutdown:
#       community: '100'
#       local_preference: 100
#       neighbors:
#         time: 50
#     log_neighbor_changes: true
#     nopeerup_delay_options:
#       post_boot: 10
#   neighbors:
#   - aigp:
#       send:
#         cost_community:
#           id: 100
#           poi:
#             igp_cost: true
#             transitive: true
#     description: merge neighbor
#     neighbor_address: 198.0.2.1
#     remote_as: '100'
#     route_maps:
#     - name: test-route
#       out: true
#   networks:
#   - address: 192.0.2.2
#   - address: 192.0.2.3
# commands:
# - router bgp 65000
# - no bgp bestpath compare-routerid
# - bgp bestpath med confed
# - no bgp dampening 1 1 1 1
# - no bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
# - bgp nopeerup-delay cold-boot 20
# - network 192.0.2.4
# - no network 192.0.2.2
# - no network 192.0.2.3
# - neighbor 192.0.2.5 remote-as 100
# - neighbor 192.0.2.5 description replace neighbor
# - neighbor 192.0.2.5 slow-peer detection disable
# - no neighbor 198.0.2.1
# after:
#   as_number: '65000'
#   bgp:
#     advertise_best_external: true
#     bestpath_options:
#       med:
#         confed: true
#     log_neighbor_changes: true
#     nopeerup_delay_options:
#       cold_boot: 20
#       post_boot: 10
#   neighbors:
#   - description: replace neighbor
#     neighbor_address: 192.0.2.5
#     remote_as: '100'
#     slow_peer:
#       detection:
#         disable: true
#   networks:
#   - address: 192.0.2.4

# After state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp nopeerup-delay cold-boot 20
#  bgp nopeerup-delay post-boot 10
#  bgp bestpath med confed
#  bgp advertise-best-external
#  network 192.0.2.4
#  neighbor 192.0.2.5 remote-as 100
#  neighbor 192.0.2.5 description replace neighbor
#  neighbor 192.0.2.5 slow-peer detection disable

# Using Deleted

# Before state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp nopeerup-delay post-boot 10
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  bgp bestpath compare-routerid
#  bgp dampening 1 1 1 1
#  bgp advertise-best-external
#  neighbor 192.0.2.1 remote-as 100
#  neighbor 192.0.2.1 description merge neighbor
#  neighbor 192.0.2.1 aigp send cost-community 100 poi igp-cost transitive
#  neighbor 192.0.2.1 route-map test-route out

- name: "Delete global BGP (Note: This won't delete the configured global BGP)"
  cisco.ios.ios_bgp_global:
    config:
      as_number: 65000
    state: deleted

# Task Output:
# ------------
#
# before:
#   as_number: '65000'
#   bgp:
#     advertise_best_external: true
#     bestpath_options:
#       compare_routerid: true
#     dampening:
#       max_suppress: 1
#       penalty_half_time: 1
#       reuse_route_val: 1
#       suppress_route_val: 1
#     graceful_shutdown:
#       community: '100'
#       local_preference: 100
#       neighbors:
#         time: 50
#     log_neighbor_changes: true
#     nopeerup_delay_options:
#       post_boot: 10
#   neighbors:
#   - aigp:
#       send:
#         cost_community:
#           id: 100
#           poi:
#             igp_cost: true
#             transitive: true
#     description: merge neighbor
#     neighbor_address: 192.0.2.1
#     remote_as: '100'
#     route_maps:
#     - name: test-route
#       out: true
# commands:
# - router bgp 65000
# - no bgp advertise-best-external
# - no bgp bestpath compare-routerid
# - no bgp dampening 1 1 1 1
# - no bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
# - no bgp log-neighbor-changes
# - no bgp nopeerup-delay post-boot 10
# - no neighbor 192.0.2.1
# after:
#   as_number: '65000'

# After state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000

# Using Deleted without any config passed

# Before state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp nopeerup-delay post-boot 10
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  bgp bestpath compare-routerid
#  bgp dampening 1 1 1 1
#  bgp advertise-best-external
#  neighbor 192.0.2.1 remote-as 100
#  neighbor 192.0.2.1 description merge neighbor
#  neighbor 192.0.2.1 aigp send cost-community 100 poi igp-cost transitive
#  neighbor 192.0.2.1 route-map test-route out

- name: Delete global BGP without config
  cisco.ios.ios_bgp_global:
    state: deleted

# Task Output:
# ------------
#
# before:
#   as_number: '65000'
#   bgp:
#     advertise_best_external: true
#     bestpath_options:
#       compare_routerid: true
#     dampening:
#       max_suppress: 1
#       penalty_half_time: 1
#       reuse_route_val: 1
#       suppress_route_val: 1
#     graceful_shutdown:
#       community: '100'
#       local_preference: 100
#       neighbors:
#         time: 50
#     log_neighbor_changes: true
#     nopeerup_delay_options:
#       post_boot: 10
#   neighbors:
#   - aigp:
#       send:
#         cost_community:
#           id: 100
#           poi:
#             igp_cost: true
#             transitive: true
#     description: merge neighbor
#     neighbor_address: 192.0.2.1
#     remote_as: '100'
#     route_maps:
#     - name: test-route
#       out: true
# commands:
# - router bgp 65000
# - no bgp advertise-best-external
# - no bgp bestpath compare-routerid
# - no bgp dampening 1 1 1 1
# - no bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
# - no bgp nopeerup-delay post-boot 10
# - no neighbor 198.51.100.1
# after:
#   as_number: '65000'

# After state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000

# Using purged - would delete all configuration

# Before state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp nopeerup-delay post-boot 10
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  bgp bestpath compare-routerid
#  bgp dampening 1 1 1 1
#  bgp advertise-best-external
#  neighbor 192.0.2.1 remote-as 100
#  neighbor 192.0.2.1 description merge neighbor
#  neighbor 192.0.2.1 aigp send cost-community 100 poi igp-cost transitive
#  neighbor 192.0.2.1 route-map test-route out

- name:
    "Delete the configured global BGP (Note: This WILL delete the the configured
    global BGP)"
  cisco.ios.ios_bgp_global:
    state: purged

# Task Output:
# ------------
#
# before:
#   as_number: '65000'
#   bgp:
#     advertise_best_external: true
#     bestpath_options:
#       compare_routerid: true
#     dampening:
#       max_suppress: 1
#       penalty_half_time: 1
#       reuse_route_val: 1
#       suppress_route_val: 1
#     graceful_shutdown:
#       community: '100'
#       local_preference: 100
#       neighbors:
#         time: 50
#     log_neighbor_changes: true
#     nopeerup_delay_options:
#       post_boot: 10
#   neighbors:
#   - aigp:
#       send:
#         cost_community:
#           id: 100
#           poi:
#             igp_cost: true
#             transitive: true
#     description: merge neighbor
#     neighbor_address: 192.0.2.1
#     remote_as: '100'
#     route_maps:
#     - name: test-route
#       out: true
# commands:
#  - no router bgp 65000
# after: {}

# After state:
# -------------
#
# vios#sh running-config | section ^router bgp

# Using gathered

# Before state:
# -------------
#
# vios#sh running-config | section ^router bgp
# router bgp 65000
#  bgp log-neighbor-changes
#  bgp nopeerup-delay post-boot 10
#  bgp graceful-shutdown all neighbors 50 local-preference 100 community 100
#  bgp bestpath compare-routerid
#  bgp dampening 1 1 1 1
#  bgp advertise-best-external
#  network 192.0.2.3
#  timers bgp 100 200 150
#  redistribute connected metric 10
#  neighbor 192.0.2.1 remote-as 100
#  neighbor 192.0.2.1 description merge neighbor
#  neighbor 192.0.2.1 aigp send cost-community 100 poi igp-cost transitive
#  neighbor 192.0.2.1 route-map test-route out

- name: Gather facts for bgp_global
  cisco.ios.ios_bgp_global:
    config:
    state: gathered

# Task Output:
# ------------
#
# gathered:
#   as_number: '65000'
#   bgp:
#     advertise_best_external: true
#     bestpath_options:
#       compare_routerid: true
#     dampening:
#       max_suppress: 1
#       penalty_half_time: 1
#       reuse_route_val: 1
#       suppress_route_val: 1
#     graceful_shutdown:
#       community: '100'
#       local_preference: 100
#       neighbors:
#         time: 50
#     log_neighbor_changes: true
#     nopeerup_delay_options:
#       post_boot: 10
#   neighbors:
#   - aigp:
#       send:
#         cost_community:
#           id: 100
#           poi:
#             igp_cost: true
#             transitive: true
#     description: merge neighbor
#     neighbor_address: 192.0.2.1
#     remote_as: '100'
#     route_maps:
#     - name: test-route
#       out: true
#   networks:
#   - address: 192.0.2.3
#   redistribute:
#   - connected:
#       metric: 10
#       set: true
#   timers:
#     holdtime: 200
#     keepalive: 100
#     min_holdtime: 150

# Using Rendered

- name: Rendered the provided configuration with the existing running configuration
  cisco.ios.ios_bgp_global:
    config:
      aggregate_addresses:
        - address: 192.0.2.1
          attribute_map: testMap1
          netmask: 255.255.255.0
          summary_only: true
        - address: 192.0.2.2
          as_set: true
          netmask: 255.255.255.0
        - address: 192.0.2.3
          as_set: true
          netmask: 255.255.255.0
      as_number: "65000"
      auto_summary: true
      bgp:
        additional_paths:
          install: true
          receive: true
        aggregate_timer: 0
        always_compare_med: true
        asnotation: true
        bestpath_options:
          aigp: true
          compare_routerid: true
          med:
            confed: true
            missing_as_worst: true
        confederation:
          identifier: "22"
        consistency_checker:
          error_message:
            interval: 10
            set: true
        dampening:
          route_map: routeMap1Test
        deterministic_med: true
        graceful_restart:
          restart_time: 2
          stalepath_time: 22
        graceful_shutdown:
          community: "77"
          local_preference: 230
          vrfs:
            time: 31
        inject_maps:
          - copy_attributes: true
            exist_map_name: Testmap3
            name: map2
          - copy_attributes: true
            exist_map_name: Testmap2
            name: map1
        listen:
          limit: 200
          range:
            host_with_subnet: 192.0.2.1/24
            peer_group: PaulNetworkGroup
        log_neighbor_changes: true
        maxas_limit: 2
        maxcommunity_limit: 3
        maxextcommunity_limit: 3
        nexthop:
          route_map: RouteMap1
          trigger:
            delay: 2
        nopeerup_delay_options:
          cold_boot: 2
          nsf_switchover: 10
          post_boot: 22
          user_initiated: 22
        recursion: true
        redistribute_internal: true
        refresh:
          max_eor_time: 700
          stalepath_time: 800
        router_id:
          vrf: true
        scan_time: 22
        slow_peer:
          detection:
            threshold: 345
          split_update_group:
            dynamic: true
            permanent: true
        sso: true
        suppress_inactive: true
        update_delay: 2
        update_group: true
      bmp:
        buffer_size: 22
        server: 2
      distance:
        bgp:
          routes_external: 2
          routes_internal: 3
          routes_local: 4
        mbgp:
          routes_external: 2
          routes_internal: 3
          routes_local: 5
      distributes:
        - in: true
          prefix: prefixTest
        - gateway: gatewayTest
          out: true
        - acl: "300"
          interface: Loopback0
          out: true
      maximum_paths:
        ibgp: 2
        paths: 2
      maximum_secondary_paths:
        ibgp: 22
        paths: 22
      neighbors:
        - neighbor_address: 192.0.2.10
          remote_as: "64500"
          update_source: Loopback1
        - activate: true
          neighbor_address: 192.0.2.11
          remote_as: "45000"
          send_community:
            extended: true
        - activate: true
          neighbor_address: 192.0.2.12
          remote_as: "45000"
        - neighbor_address: 192.0.2.13
          remote_as: "6553601"
        - advertise:
            diverse_path:
              backup: true
          neighbor_address: 192.0.2.8
          route_reflector_client: true
        - neighbor_address: 192.0.2.9
          remote_as: "64500"
          route_maps:
            - in: true
              name: rmp1
            - in: true
              name: rmp2
          update_source: Loopback0
        - activate: true
          advertise:
            additional_paths:
              group_best: true
          neighbor_address: 2001:DB8::1037
        - neighbor_address: testNebTag
          peer_group: "5"
          soft_reconfiguration: true
          version: 4
      networks:
        - address: 192.0.2.15
          backdoor: true
          netmask: 55.255.255.0
          route_map: mp1
        - address: 192.0.2.16
          backdoor: true
          netmask: 255.255.255.0
          route_map: mp2
        - address: 192.0.2.17
          backdoor: true
          netmask: 255.255.255.0
          route_map: mp2
      redistribute:
        - static:
            metric: 33
            route_map: rmp1
            set: true
        - application:
            metric: 22
            name: app1
        - application:
            metric: 33
            name: app2
            route_map: mp1
        - connected:
            metric: 22
            set: true
        - mobile:
            metric: 211
            set: true
    state: rendered

# Task Output:
# ------------
#
# rendered:
# - router bgp 65000
# - auto-summary
# - bmp buffer-size 22
# - bmp server 2
# - distance bgp 2 3 4
# - distance mbgp 2 3 5
# - maximum-paths 2
# - maximum-paths ibgp 2
# - maximum-secondary-paths 22
# - maximum-secondary-paths ibgp 22
# - bgp additional-paths install receive
# - bgp aggregate-timer 0
# - bgp always-compare-med
# - bgp asnotation dot
# - bgp bestpath aigp ignore
# - bgp bestpath compare-routerid
# - bgp bestpath med confed missing-as-worst
# - bgp confederation identifier 22
# - bgp consistency-checker error-message interval 10
# - bgp dampening route-map routeMap1Test
# - bgp deterministic-med
# - bgp graceful-restart restart-time 2
# - bgp graceful-restart stalepath-time 22
# - bgp graceful-shutdown all vrfs 31 local-preference 230 community 77
# - bgp listen limit 200
# - bgp listen range 192.0.2.1/24 peer-group PaulNetworkGroup
# - bgp log-neighbor-changes
# - bgp maxas-limit 2
# - bgp maxcommunity-limit 3
# - bgp maxextcommunity-limit 3
# - bgp nexthop route-map RouteMap1
# - bgp nexthop trigger delay 2
# - bgp nopeerup-delay cold-boot 2
# - bgp nopeerup-delay post-boot 22
# - bgp nopeerup-delay nsf-switchover 10
# - bgp nopeerup-delay user-initiated 22
# - bgp recursion host
# - bgp redistribute-internal
# - bgp refresh max-eor-time 700
# - bgp refresh stalepath-time 800
# - bgp router-id vrf auto-assign
# - bgp scan-time 22
# - bgp slow-peer detection threshold 345
# - bgp slow-peer split-update-group dynamic permanent
# - bgp sso route-refresh-enable
# - bgp suppress-inactive
# - bgp update-delay 2
# - bgp update-group split as-override
# - bgp inject-map map2 exist-map Testmap3 copy-attributes
# - bgp inject-map map1 exist-map Testmap2 copy-attributes
# - distribute-list prefix prefixTest in
# - distribute-list gateway gatewayTest out
# - distribute-list 300 out Loopback0
# - aggregate-address 192.0.2.1 255.255.255.0 summary-only attribute-map testMap1
# - aggregate-address 192.0.2.2 255.255.255.0 as-set
# - aggregate-address 192.0.2.3 255.255.255.0 as-set
# - network 192.0.2.15 mask 55.255.255.0 route-map mp1 backdoor
# - network 192.0.2.16 mask 255.255.255.0 route-map mp2 backdoor
# - network 192.0.2.17 mask 255.255.255.0 route-map mp2 backdoor
# - neighbor 192.0.2.10 remote-as 64500
# - neighbor 192.0.2.10 update-source Loopback1
# - neighbor 192.0.2.11 remote-as 45000
# - neighbor 192.0.2.11 activate
# - neighbor 192.0.2.11 send-community extended
# - neighbor 192.0.2.12 remote-as 45000
# - neighbor 192.0.2.12 activate
# - neighbor 192.0.2.13 remote-as 6553601
# - neighbor 192.0.2.8 advertise diverse-path backup
# - neighbor 192.0.2.8 route-reflector-client
# - neighbor 192.0.2.9 remote-as 64500
# - neighbor 192.0.2.9 update-source Loopback0
# - neighbor 192.0.2.9 route-map rmp1 in
# - neighbor 192.0.2.9 route-map rmp2 in
# - neighbor 2001:DB8::1037 activate
# - neighbor 2001:DB8::1037 advertise additional-paths group-best
# - neighbor testNebTag peer-group 5
# - neighbor testNebTag soft-reconfiguration inbound
# - neighbor testNebTag version 4
# - redistribute static metric 33 route-map rmp1
# - redistribute application app1 metric 22
# - redistribute application app2 metric 33 route-map mp1
# - redistribute connected metric 22
# - redistribute mobile metric 211

# Using parsed

# File: parsed.cfg
# ----------------
#
# router bgp 65000
#  auto-summary
#  bmp buffer-size 22
#  bmp server 2
#  distance bgp 2 3 4
#  distance mbgp 2 3 5
#  maximum-paths 2
#  maximum-paths ibgp 2
#  maximum-secondary-paths 22
#  maximum-secondary-paths ibgp 22
#  description checking description as line
#  bgp additional-paths install receive
#  bgp aggregate-timer 0
#  bgp always-compare-med
#  bgp asnotation dot
#  bgp bestpath aigp ignore
#  bgp bestpath compare-routerid
#  bgp bestpath med confed missing-as-worst
#  bgp confederation identifier 22
#  bgp consistency-checker error-message interval 10
#  bgp dampening route-map routeMap1Test
#  bgp deterministic-med
#  bgp graceful-restart restart-time 2
#  bgp graceful-restart stalepath-time 22
#  bgp graceful-shutdown all vrfs 31 local-preference 230 community 77
#  bgp listen limit 200
#  bgp listen range 192.0.2.1/24 peer-group PaulNetworkGroup
#  bgp log-neighbor-changes
#  bgp maxas-limit 2
#  bgp maxcommunity-limit 3
#  bgp maxextcommunity-limit 3
#  bgp nexthop route-map RouteMap1
#  bgp nexthop trigger delay 2
#  bgp nopeerup-delay cold-boot 2
#  bgp nopeerup-delay post-boot 22
#  bgp nopeerup-delay nsf-switchover 10
#  bgp nopeerup-delay user-initiated 22
#  bgp recursion host
#  bgp redistribute-internal
#  bgp refresh max-eor-time 700
#  bgp refresh stalepath-time 800
#  bgp router-id vrf auto-assign
#  bgp scan-time 22
#  bgp slow-peer detection threshold 345
#  bgp slow-peer split-update-group dynamic permanent
#  bgp sso route-refresh-enable
#  bgp suppress-inactive
#  bgp update-delay 2
#  bgp update-group split as-override
#  bgp inject-map map2 exist-map Testmap3 copy-attributes
#  bgp inject-map map1 exist-map Testmap2 copy-attributes
#  distribute-list prefix prefixTest in
#  distribute-list gateway gatewayTest out
#  distribute-list 300 out Loopback0
#  aggregate-address 192.0.2.1 255.255.255.0 summary-only attribute-map testMap1
#  aggregate-address 192.0.2.2 255.255.255.0 as-set
#  aggregate-address 192.0.2.3 255.255.255.0 as-set
#  network 192.0.2.15 mask 55.255.255.0 route-map mp1 backdoor
#  network 192.0.2.16 mask 255.255.255.0 route-map mp2 backdoor
#  network 192.0.2.17 mask 255.255.255.0 route-map mp2 backdoor
#  neighbor 192.0.2.8 advertise diverse-path backup
#  neighbor 192.0.2.8 route-reflector-client
#  neighbor 192.0.2.9 remote-as 64500
#  neighbor 192.0.2.9 update-source Loopback0
#  neighbor 192.0.2.9 route-map rmp1 in
#  neighbor 192.0.2.9 route-map rmp2 in
#  neighbor 192.0.2.10 remote-as 64500
#  neighbor 192.0.2.10 update-source Loopback1
#  neighbor 192.0.2.11 remote-as 45000
#  neighbor 192.0.2.11 activate
#  neighbor 192.0.2.11 send-community extended
#  neighbor 192.0.2.12 remote-as 45000
#  neighbor 192.0.2.12 activate
#  neighbor 192.0.2.13 remote-as 6553601
#  neighbor 192.0.2.13 shutdown graceful 10 community 20
#  neighbor 2001:DB8::1037 activate
#  neighbor 2001:DB8::1037 advertise additional-paths group-best
#  neighbor testNebTag peer-group 5
#  neighbor testNebTag soft-reconfiguration inbound
#  neighbor testNebTag version 4
#  redistribute static metric 33 route-map rmp1
#  redistribute application app1 metric 22
#  redistribute application app2 metric 33 route-map mp1
#  redistribute connected metric 22
#  redistribute mobile metric 21

- name: Parse the commands for provided configuration
  cisco.ios.ios_bgp_global:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task Output:
# ------------
#
# parsed:
#     aggregate_addresses:
#     - address: 192.0.2.1
#       attribute_map: testMap1
#       netmask: 255.255.255.0
#       summary_only: true
#     - address: 192.0.2.2
#       as_set: true
#       netmask: 255.255.255.0
#     - address: 192.0.2.3
#       as_set: true
#       netmask: 255.255.255.0
#     as_number: '65000'
#     auto_summary: true
#     bgp:
#       additional_paths:
#         install: true
#         receive: true
#       aggregate_timer: 0
#       always_compare_med: true
#       asnotation: true
#       bestpath_options:
#         aigp: true
#         compare_routerid: true
#         med:
#           confed: true
#           missing_as_worst: true
#       confederation:
#         identifier: '22'
#       consistency_checker:
#         error_message:
#           interval: 10
#           set: true
#       dampening:
#         route_map: routeMap1Test
#       deterministic_med: true
#       graceful_restart:
#         restart_time: 2
#         stalepath_time: 22
#       graceful_shutdown:
#         community: '77'
#         local_preference: 230
#         vrfs:
#           time: 31
#       inject_maps:
#       - copy_attributes: true
#         exist_map_name: Testmap3
#         name: map2
#       - copy_attributes: true
#         exist_map_name: Testmap2
#         name: map1
#       listen:
#         limit: 200
#         range:
#           host_with_subnet: 192.0.2.1/24
#           peer_group: PaulNetworkGroup
#       log_neighbor_changes: true
#       maxas_limit: 2
#       maxcommunity_limit: 3
#       maxextcommunity_limit: 3
#       nexthop:
#         route_map: RouteMap1
#         trigger:
#           delay: 2
#       nopeerup_delay_options:
#         cold_boot: 2
#         nsf_switchover: 10
#         post_boot: 22
#         user_initiated: 22
#       recursion: true
#       redistribute_internal: true
#       refresh:
#         max_eor_time: 700
#         stalepath_time: 800
#       router_id:
#         vrf: true
#       scan_time: 22
#       slow_peer:
#         detection:
#           threshold: 345
#         split_update_group:
#           dynamic: true
#           permanent: true
#       sso: true
#       suppress_inactive: true
#       update_delay: 2
#       update_group: true
#     bmp:
#       buffer_size: 22
#       server: 2
#     distance:
#       bgp:
#         routes_external: 2
#         routes_internal: 3
#         routes_local: 4
#       mbgp:
#         routes_external: 2
#         routes_internal: 3
#         routes_local: 5
#     distributes:
#     - in: true
#       prefix: prefixTest
#     - gateway: gatewayTest
#       out: true
#     - acl: '300'
#       interface: Loopback0
#       out: true
#     maximum_paths:
#       ibgp: 2
#       paths: 2
#     maximum_secondary_paths:
#       ibgp: 22
#       paths: 22
#     neighbors:
#     - neighbor_address: 192.0.2.10
#       remote_as: '64500'
#       update_source: Loopback1
#     - activate: true
#       neighbor_address: 192.0.2.11
#       remote_as: '45000'
#       send_community:
#         extended: true
#     - activate: true
#       neighbor_address: 192.0.2.12
#       remote_as: '45000'
#     - neighbor_address: 192.0.2.13
#       remote_as: '6553601'
#     - advertise:
#         diverse_path:
#           backup: true
#       neighbor_address: 192.0.2.8
#       route_reflector_client: true
#     - neighbor_address: 192.0.2.9
#       remote_as: '64500'
#       route_maps:
#       - in: true
#         name: rmp1
#       - in: true
#         name: rmp2
#       update_source: Loopback0
#     - activate: true
#       advertise:
#         additional_paths:
#           group_best: true
#       neighbor_address: 2001:DB8::1037
#     - neighbor_address: testNebTag
#       peer_group: '5'
#       soft_reconfiguration: true
#       version: 4
#     networks:
#     - address: 192.0.2.15
#       backdoor: true
#       netmask: 55.255.255.0
#       route_map: mp1
#     - address: 192.0.2.16
#       backdoor: true
#       netmask: 255.255.255.0
#       route_map: mp2
#     - address: 192.0.2.17
#       backdoor: true
#       netmask: 255.255.255.0
#       route_map: mp2
#     redistribute:
#     - static:
#         metric: 33
#         route_map: rmp1
#         set: true
#     - application:
#         metric: 22
#         name: app1
#     - application:
#         metric: 33
#         name: app2
#         route_map: mp1
#     - connected:
#         metric: 22
#         set: true
#     - mobile:
#         metric: 21
#         set: true
```

## [Return Values](ios_bgp_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration after module execution.  **Returned:** when changed  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **before**  dictionary | The configuration prior to the module execution.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `"This output will always be in the same format as the module argspec.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** when *state* is `merged`, `replaced`, `overridden`, `deleted` or `purged`  **Sample:** `["router bgp 65000", "neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive", "bgp graceful-shutdown all neighbors 50 local-preference 100 community 100"]` |
| **gathered**  list / elements=string | Facts about the network resource gathered from the remote device as structured data.  **Returned:** when *state* is `gathered`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **parsed**  list / elements=string | The device native config provided in *running_config* option parsed into structured data as per module argspec.  **Returned:** when *state* is `parsed`  **Sample:** `["This output will always be in the same format as the module argspec.\n"]` |
| **rendered**  list / elements=string | The provided configuration in the task rendered in device-native format (offline).  **Returned:** when *state* is `rendered`  **Sample:** `["router bgp 65000", "neighbor 198.51.100.1 aigp send cost-community 100 poi igp-cost transitive", "bgp graceful-shutdown all neighbors 50 local-preference 100 community 100"]` |

### Authors

- Sumit Jaiswal (@justjais)
- Sagar Paul (@KB-perByte)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
