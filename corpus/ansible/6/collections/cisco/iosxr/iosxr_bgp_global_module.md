---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_bgp_global module – Resource module to configure BGP."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_bgp_global_module.html
fetched_at: 2026-07-27T16:55:38+00:00
---
# cisco.iosxr.iosxr_bgp_global module – Resource module to configure BGP.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/cisco/iosxr) (version 3.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_bgp_global`.

New in cisco.iosxr 2.0.0

- [Synopsis](iosxr_bgp_global_module.md#synopsis)
- [Parameters](iosxr_bgp_global_module.md#parameters)
- [Notes](iosxr_bgp_global_module.md#notes)
- [Examples](iosxr_bgp_global_module.md#examples)

## [Synopsis](iosxr_bgp_global_module.md#id1)

- This module configures and manages the attributes of BGP global on Cisco IOS-XR platforms.

## [Parameters](iosxr_bgp_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of configurations for BGP global. |
| **as_number**  string | Autonomous system number of the router. |
| **bfd**  dictionary | Configure BFD parameters. |
| **minimum_interval**  integer | Specifies the BFD session’s minimum-interval value for the neighbor. |
| **multiplier**  integer | Specifies the BFD session’s multiplier value for the neighbor. |
| **bgp**  dictionary | BGP parameters. |
| **as_path_loopcheck**  boolean | Enable AS-path loop checking for iBGP peers.  Choices:   - `false` - `true` |
| **auto_policy_soft_reset**  dictionary | Enable automatic soft peer reset on policy reconfiguration. |
| **disable**  boolean | Disable an automatic soft reset of Border Gateway Protocol (BGP) peers.  Choices:   - `false` - `true` |
| **bestpath**  dictionary | Select the bestpath selection algorithim for BGP routes. |
| **aigp**  dictionary | AIGP attribute |
| **ignore**  boolean | Ignore AIGP attribute.  Choices:   - `false` - `true` |
| **as_path**  dictionary | Select the bestpath selection based on as-path. |
| **ignore**  boolean | ignore  Choices:   - `false` - `true` |
| **multipath_relax**  boolean | multipath-relax  Choices:   - `false` - `true` |
| **compare_routerid**  boolean | Compare router-id for identical EBGP paths.  Choices:   - `false` - `true` |
| **cost_community**  dictionary | Cost community. |
| **ignore**  boolean | ignore cost_community  Choices:   - `false` - `true` |
| **med**  dictionary | MED attribute |
| **always**  boolean | Allow comparing MED from different neighbors.  Choices:   - `false` - `true` |
| **confed**  boolean | Compare MED among confederation paths.  Choices:   - `false` - `true` |
| **missing_as_worst**  boolean | Treat missing MED as the least preferred one.  Choices:   - `false` - `true` |
| **origin_as**  dictionary | BGP origin-AS knobs. |
| **allow**  dictionary | BGP origin-AS knobs. |
| **invalid**  boolean | BGP bestpath selection will allow ‘invalid’ origin-AS  Choices:   - `false` - `true` |
| **use**  dictionary | BGP origin-AS knobs. |
| **validity**  boolean | BGP bestpath selection will use origin-AS validity  Choices:   - `false` - `true` |
| **cluster_id**  string | Cluster ID of this router acting as a route reflector. |
| **confederation**  dictionary | confederation. |
| **identifier**  integer | Set routing domain confederation AS. |
| **peers**  list / elements=integer | Enter peer ASs in BGP confederation mode. |
| **default**  dictionary | Configure default value. |
| **local_preference**  integer | local preferance.  Please refer vendor documentation for valid values |
| **enforce_first_as**  dictionary | Enforce the first AS for EBGP routes |
| **disable**  boolean | disable enforce 1st as  Choices:   - `false` - `true` |
| **fast_external_fallover**  dictionary | Immediately reset session if a link to a directly connected external peer goes down. |
| **disable**  boolean | disable fast external fallover.  Choices:   - `false` - `true` |
| **graceful_restart**  dictionary | Enable graceful restart support. |
| **graceful_reset**  boolean | Reset gracefully if configuration change forces a peer reset.  Choices:   - `false` - `true` |
| **purge_time**  integer | Time before stale routes are purged in seconds <1-6000>. |
| **restart_time**  integer | Restart time advertised to neighbors in seconds <1-4095>. |
| **set**  boolean | Enable graceful-restart.  Choices:   - `false` - `true` |
| **stalepath_time**  integer | Maximum time to wait for restart of GR capable peers in seconds <1-4095>. |
| **install**  dictionary | Install diversion path to RIB/CEF. |
| **diversion**  boolean | Install diversion path to RIB/CEF.  Choices:   - `false` - `true` |
| **log**  dictionary | Log bgp info |
| **log_message**  dictionary | Log neighbor inbound/outbound message. |
| **disable**  boolean | disable inbound outbound messages.  Choices:   - `false` - `true` |
| **neighbor**  dictionary | Log neighbor state info. |
| **changes**  dictionary | Log neighbor up/down and reset reason. |
| **detail**  boolean | detail  Choices:   - `false` - `true` |
| **disable**  boolean | disable  Choices:   - `false` - `true` |
| **maximum**  dictionary | Maximum number of neighbors that can be configured |
| **neighbor**  integer | Maximum number of neighbors <1-15000>. |
| **multipath**  dictionary | Change multipath selection criteria |
| **as_path**  dictionary | AS path |
| **ignore**  dictionary | Ignore as-path related check for multipath selection. |
| **onwards**  boolean | Ignore everything onwards as-path for multipath selection.  Choices:   - `false` - `true` |
| **origin_as**  dictionary | BGP origin-AS knobs. |
| **validation**  dictionary | BGP origin-AS validation knobs. |
| **disable**  boolean | Disable RPKI origin-AS validation.  Choices:   - `false` - `true` |
| **signal**  dictionary | Signal origin-AS validity towards peers. |
| **ibgp**  boolean | Signal origin-AS validity towards iBGP peers  Choices:   - `false` - `true` |
| **time**  dictionary | Time to wait between an RPKI update and a BGP table walk. |
| **time_in_second**  integer | Prefix validation time (in seconds). |
| **time_off**  boolean | No automatic prefix validation after an RPKI update.  Choices:   - `false` - `true` |
| **redistribute_internal**  boolean | Redistribute internal BGP routes.  Choices:   - `false` - `true` |
| **router_id**  string | Configure Router-id. Example- A.B.C.D IPv4 address. |
| **scan_time**  integer | Configure background scanner interval for generic scanner Example- <5-3600>. |
| **unsafe_ebgp_policy**  boolean | Make eBGP neighbors with no policy pass all routes(cisco-support).  Choices:   - `false` - `true` |
| **update_delay**  integer | Set the max initial delay for sending updates Example-<0-3600> in secs. |
| **default_information**  dictionary | Control distribution of default information. |
| **originate**  boolean | Distribute a default route  Choices:   - `false` - `true` |
| **default_metric**  integer | Default metric. Example-<1-4294967295>. |
| **graceful_maintenance**  dictionary | This allows the router to be brought in or out of service gracefully. |
| **activate**  string | All neighbors with graceful-maintenance config  Choices:   - `"all-neighbors"` - `"retain-routes"` - `"all-neighbors retain-routes"` - `""` |
| **ibgp**  dictionary | Set options for iBGP peers. |
| **policy**  dictionary | Set options for route-policy. |
| **out**  dictionary | Set options for outbound policy. |
| **enforce_modifications**  boolean | Allow policy to modify all attributes.  Choices:   - `false` - `true` |
| **mpls**  dictionary | Enable mpls parameters. |
| **activate**  dictionary | Enter mpls interfaces in BGP mpls activate mode. |
| **interface**  string | Name of interface to enable mpls. |
| **mvpn**  boolean | Connect to PIM/PIM6.  Choices:   - `false` - `true` |
| **neighbors**  list / elements=dictionary | Specify a neighbor router. |
| **advertisement_interval**  integer | Minimum interval between sending BGP routing updates.Example-<0-600>. |
| **bfd**  dictionary | Configure BFD parameters. |
| **fast_detect**  dictionary | Enable Fast detection |
| **disable**  boolean | Prevent bfd settings from being inherited from the parent.  Choices:   - `false` - `true` |
| **strict_mode**  boolean | Hold down neighbor session until BFD session is up  Choices:   - `false` - `true` |
| **minimum_interval**  integer | Specifies the BFD session’s minimum-interval value for the neighbor. |
| **multiplier**  integer | Specifies the BFD session’s multiplier value for the neighbor. |
| **bmp_activate**  dictionary | Enable BMP logging for this neighbor. |
| **server**  integer | Enable BMP connection to particular server.Example-<1-8>. |
| **capability**  dictionary | Advertise capability to the peer. |
| **additional_paths**  dictionary | BGP additional-paths commands. |
| **receive**  dictionary | Additional paths receive capability |
| **disable**  boolean | set receive capability  Choices:   - `false` - `true` |
| **set**  boolean | set receive capability  Choices:   - `false` - `true` |
| **send**  dictionary | Additional paths Send capability |
| **disable**  boolean | set send capability  Choices:   - `false` - `true` |
| **set**  boolean | set send capability  Choices:   - `false` - `true` |
| **suppress**  dictionary | Suppress advertising capability to the peer. |
| **all**  dictionary | all capability |
| **inheritance_disable**  boolean | Do not inherit this configuration from parent group.  Choices:   - `false` - `true` |
| **set**  boolean | set all.  Choices:   - `false` - `true` |
| **four_byte_AS**  dictionary | 4-byte-as capability |
| **set**  boolean | set 4_byte_as.  Choices:   - `false` - `true` |
| **cluster_id**  string | Cluster ID of this router acting as a route reflector. |
| **description**  string | Neighbor specific description. |
| **dmz_link_bandwidth**  dictionary | Propagate the DMZ link bandwidth. |
| **inheritance_disable**  boolean | Do not inherit this configuration from parent group.  Choices:   - `false` - `true` |
| **set**  boolean | set dmz-link-bandwidth.  Choices:   - `false` - `true` |
| **dscp**  string | Set IP DSCP (DiffServ CodePoint).Please refer vendor document for valid entries. |
| **ebgp_multihop**  dictionary | Allow EBGP neighbors not on directly connected networks. |
| **mpls**  boolean | Disable BGP MPLS forwarding.  Choices:   - `false` - `true` |
| **value**  integer | maximum hop count.Example-<1-255>. |
| **ebgp_recv_extcommunity_dmz**  dictionary | Receive extcommunity dmz link bandwidth from ebgp neighbor. |
| **inheritance_disable**  boolean | Prevent ebgp-recv-community-dmz from being inherited from parent  Choices:   - `false` - `true` |
| **set**  boolean | set ebgp-recv-community-dmz.  Choices:   - `false` - `true` |
| **ebgp_send_extcommunity_dmz**  dictionary | Send extcommunity dmz link bandwidth from ebgp neighbor. |
| **cumulatie**  boolean | Send cumulative community dmz link bandwidth of all multipaths to ebgp neighbor.  Choices:   - `false` - `true` |
| **inheritance_disable**  boolean | Prevent ebgp-send-community-dmz from being inherited from parent  Choices:   - `false` - `true` |
| **set**  boolean | set ebgp-send-community-dmz.  Choices:   - `false` - `true` |
| **egress_engineering**  dictionary | Enable egress peer engineering for this neighbor. |
| **inheritance_disable**  boolean | Prevent egress-engineering from being inherited from parent  Choices:   - `false` - `true` |
| **set**  boolean | set egress-engineering.  Choices:   - `false` - `true` |
| **enforce_first_as**  dictionary | Enforce the first AS for EBGP routes |
| **disable**  boolean | disable enforce 1st as  Choices:   - `false` - `true` |
| **graceful_maintenance**  dictionary | Attributes for Graceful Maintenance. This will cause neighbors to de-prefer routes from this router and choose alternates. This allows the router to be brought in or out of service gracefully. |
| **activate**  dictionary | Routes will be announced with the graceful maintenance attributes while activated either here or under router bgp configuration. |
| **inheritance_disable**  boolean | Prevent activate from being inherited from the parent.  Choices:   - `false` - `true` |
| **set**  boolean | activate.  Choices:   - `false` - `true` |
| **as_prepends**  dictionary | Number of times to prepend the local AS number to the AS path of routes. Default=0 |
| **inheritance_disable**  boolean | Prevent as prepends from being inherited from the parent.  Choices:   - `false` - `true` |
| **value**  integer | Range of values for as prepends.Example-<0-6> . |
| **local_preference**  dictionary | local preference with which to advertise routes to ibgp neigbors. Default=No Touch |
| **inheritance_disable**  boolean | Prevent local preference from being inherited from the parent.  Choices:   - `false` - `true` |
| **value**  integer | Range of values for Local Preference.Example-<0-4294967295> . |
| **set**  boolean | set graceful maintenance.  Choices:   - `false` - `true` |
| **graceful_restart**  dictionary | Enable graceful restart support for this neighbor. |
| **restart_time**  integer | Restart time advertised to neighbors in seconds <1-4095>. |
| **stalepath_time**  integer | Maximum time to wait for restart of GR capable peers in seconds <1-4095>. |
| **ignore_connected_check**  dictionary | Bypass the directly connected nexthop check for single-hop eBGP peering |
| **inheritance_disable**  boolean | Prevent ignore-connected-check from being inherited from the parent  Choices:   - `false` - `true` |
| **set**  boolean | set ignore-connected-check.  Choices:   - `false` - `true` |
| **keychain**  dictionary | Set keychain based authentication. |
| **inheritance_disable**  boolean | Prevent keychain from being inherited from parent.  Choices:   - `false` - `true` |
| **name**  string | Name of the key chain - maximum 32 characters. |
| **local**  dictionary | Configure local parameter |
| **address**  dictionary | IPv4 address |
| **inheritance_disable**  boolean | Prevent local address from being inherited from parent.  Choices:   - `false` - `true` |
| **ipv4_address**  string | IPv4 address <A.B.C.D>. |
| **local_as**  dictionary | Specify local AS number. |
| **inheritance_disable**  boolean | Prevent local AS from being inherited from parent.  Choices:   - `false` - `true` |
| **value**  integer | 2 byte, 4 byte As number |
| **log**  dictionary | Logging update messages per neighbor. |
| **log_message**  dictionary | Logging update/notification messages per neighbor. |
| **in**  dictionary | Inbound log messages |
| **disable**  boolean | Disable inbound message logging.  Choices:   - `false` - `true` |
| **inheritance_disable**  boolean | Prevents the msg log from being inherited from the parent.  Choices:   - `false` - `true` |
| **value**  integer | Range for message log buffer size <1-100>. |
| **out**  dictionary | Outbound log messages |
| **disable**  boolean | Disable inbound message logging.  Choices:   - `false` - `true` |
| **inheritance_disable**  boolean | Prevents the msg log from being inherited from the parent.  Choices:   - `false` - `true` |
| **value**  integer | Range for message log buffer size <1-100>. |
| **neighbor_address**  aliases: neighbor  string / required | Neighbor router address. |
| **origin_as**  dictionary | BGP origin-AS knobs. |
| **validation**  dictionary | BGP origin-AS validation knobs. |
| **disable**  boolean | Disable RPKI origin-AS validation.  Choices:   - `false` - `true` |
| **receive_buffer_size**  integer | Set socket and BGP receive buffer size.Example <512-131072>. |
| **remote_as**  integer | Neighbor Autonomous System. |
| **send_buffer_size**  integer | Set socket and BGP send buffer size.Example <4096-131072>. |
| **session_open_mode**  string | Establish BGP session using this TCP open mode.  Choices:   - `"active-only"` - `"both"` - `"passive-only"` |
| **shutdown**  dictionary | Administratively shut down this neighbor. |
| **inheritance_disable**  boolean | Prevent shutdown from being inherited from parent  Choices:   - `false` - `true` |
| **set**  boolean | shutdown.  Choices:   - `false` - `true` |
| **tcp**  dictionary | TCP session configuration commands. |
| **mss**  dictionary | Maximum Segment Size. |
| **inheritance_disable**  boolean | Prevent mss from being inherited from parent  Choices:   - `false` - `true` |
| **value**  integer | TCP initial maximum segment size. |
| **timers**  dictionary | BGP per neighbor timers. |
| **holdtime**  integer | hold time <3-65535> or 0 Disable hold time. |
| **keepalive_time**  integer | keepalive interval <0-65535>. |
| **ttl_security**  dictionary | Enable EBGP TTL security. |
| **inheritance_disable**  boolean | Prevent ttl-security from being inherited from parent  Choices:   - `false` - `true` |
| **set**  boolean | set ttl-security  Choices:   - `false` - `true` |
| **update**  dictionary | BGP Update configuration. |
| **in**  dictionary | Inbound update message handling. |
| **filtering**  dictionary | Inbound update message filtering |
| **attribute_filter**  dictionary | Attribute-filter configuration. |
| **group**  string | Name of group. |
| **logging**  dictionary | Update filtering syslog message. |
| **disable**  boolean | Disable update filtering syslog message.  Choices:   - `false` - `true` |
| **update_message**  dictionary | Filtered update messages. |
| **buffers**  integer | Number of buffers to store filtered update messages. |
| **update_source**  string | Source of routing updates.Refer vendor document for valid values. |
| **nsr**  dictionary | Enable non-stop-routing support for all neighbors. |
| **disable**  boolean | disable nsr  Choices:   - `false` - `true` |
| **set**  boolean | set nsr  Choices:   - `false` - `true` |
| **rpki**  dictionary | Configure RPKI. |
| **route**  dictionary | Configure an RPKI route.A.B.C.D/length or X:X::X/length Network/Minimum prefix length |
| **max**  integer | Maximum prefix length. Example- <1-128> . |
| **origin**  integer | Origin Autonomous System number (in asplain format) Example-<1-4294967295>. |
| **value**  string | A.B.C.D/length or X:X::X/length Network/Minimum prefix length. |
| **servers**  list / elements=dictionary | Configure RPKI cache-servers. |
| **name**  string | address of rpki server. |
| **purge_time**  integer | Time to wait after a cache goes down to clean up stale routes |
| **refresh_time**  dictionary | Time between sending serial-queries for the RPKI cache-server |
| **time_off**  boolean | Do not send serial-queries periodically  Choices:   - `false` - `true` |
| **value**  integer | Purge time (in seconds) <30-360> |
| **response_time**  dictionary | Time to wait for a response from the RPKI cache-server |
| **time_off**  boolean | Wait indefinitely for a response  Choices:   - `false` - `true` |
| **value**  integer | Purge time (in seconds) <15-3600> |
| **shutdown**  boolean | Shutdown the RPKI cache-server  Choices:   - `false` - `true` |
| **transport**  dictionary | Specify a transport method for the RPKI cache-server |
| **ssh**  dictionary | Connect to the RPKI cache-server using SSH |
| **port**  integer | Specify a port number for the RPKI cache-server transport |
| **tcp**  dictionary | Connect to the RPKI cache-server using TCP (unencrypted) |
| **port**  integer | Specify a port number for the RPKI cache-server transport |
| **socket**  dictionary | set socket parameters. |
| **receive_buffer_size**  integer | socket receive buffer size.Example-<512-131072>. |
| **send_buffer_size**  integer | socket send buffer size.Example- <4096-131072>. |
| **timers**  dictionary | BGP per neighbor timers. |
| **holdtime**  integer | hold time <3-65535> or 0 Disable hold time. |
| **keepalive_time**  integer | keepalive interval <0-65535>. |
| **update**  dictionary | BGP Update configuration. |
| **in**  dictionary | Inbound update message handling |
| **error_handling**  dictionary | Inbound update message error handling. |
| **basic**  dictionary | Inbound update message basic error handling |
| **ebgp**  dictionary | Inbound update message basic error handling for EBGP neighbors |
| **disable**  boolean | disable  Choices:   - `false` - `true` |
| **ibgp**  dictionary | Inbound update message basic error handling for ibgp neighbors |
| **disable**  boolean | disable  Choices:   - `false` - `true` |
| **extended**  dictionary | Inbound update message extended error handling |
| **ebgp**  boolean | Inbound update message extended error handling for EBGP neighbors  Choices:   - `false` - `true` |
| **ibgp**  boolean | Inbound update message extended error handling for ibgp neighbors  Choices:   - `false` - `true` |
| **limit**  integer | Upper bound on transient memory usage for update generation.Example-<16-2048>. |
| **out**  dictionary | BGP Update generation configuration. |
| **logging**  boolean | Enable logging of update generation events.  Choices:   - `false` - `true` |
| **vrfs**  list / elements=dictionary | Specify a vrf name. |
| **bfd**  dictionary | Configure BFD parameters. |
| **minimum_interval**  integer | Specifies the BFD session’s minimum-interval value for the neighbor. |
| **multiplier**  integer | Specifies the BFD session’s multiplier value for the neighbor. |
| **bgp**  dictionary | BGP commands. |
| **auto_policy_soft_reset**  dictionary | Enable automatic soft peer reset on policy reconfiguration. |
| **disable**  boolean | Disable an automatic soft reset of Border Gateway Protocol (BGP) peers.  Choices:   - `false` - `true` |
| **bestpath**  dictionary | Select the bestpath selection algorithim for BGP routes. |
| **aigp**  dictionary | AIGP attribute |
| **ignore**  boolean | Ignore AIGP attribute.  Choices:   - `false` - `true` |
| **as_path**  dictionary | Select the bestpath selection based on as-path. |
| **ignore**  boolean | ignore  Choices:   - `false` - `true` |
| **multipath_relax**  boolean | multipath-relax  Choices:   - `false` - `true` |
| **compare_routerid**  boolean | Compare router-id for identical EBGP paths.  Choices:   - `false` - `true` |
| **cost_community**  dictionary | Cost community. |
| **ignore**  boolean | ignore cost_community  Choices:   - `false` - `true` |
| **med**  dictionary | MED attribute |
| **always**  boolean | Allow comparing MED from different neighbors.  Choices:   - `false` - `true` |
| **confed**  boolean | Compare MED among confederation paths.  Choices:   - `false` - `true` |
| **missing_as_worst**  boolean | Treat missing MED as the least preferred one.  Choices:   - `false` - `true` |
| **origin_as**  dictionary | BGP origin-AS knobs. |
| **allow**  dictionary | BGP origin-AS knobs. |
| **invalid**  boolean | BGP bestpath selection will allow ‘invalid’ origin-AS  Choices:   - `false` - `true` |
| **use**  dictionary | BGP origin-AS knobs. |
| **validity**  boolean | BGP bestpath selection will use origin-AS validity  Choices:   - `false` - `true` |
| **default**  dictionary | Configure default value. |
| **local_preference**  integer | local preferance.  Please refer vendor documentation for valid values |
| **enforce_first_as**  dictionary | Enforce the first AS for EBGP routes |
| **disable**  boolean | disable enforce 1st as  Choices:   - `false` - `true` |
| **fast_external_fallover**  dictionary | Immediately reset session if a link to a directly connected external peer goes down. |
| **disable**  boolean | disable fast external fallover.  Choices:   - `false` - `true` |
| **log**  dictionary | Log bgp info |
| **log_message**  dictionary | Log neighbor inbound/outbound message. |
| **disable**  boolean | disable inbound outbound messages.  Choices:   - `false` - `true` |
| **neighbor**  dictionary | Log neighbor state info. |
| **changes**  dictionary | Log neighbor up/down and reset reason. |
| **detail**  boolean | detail  Choices:   - `false` - `true` |
| **disable**  boolean | disable  Choices:   - `false` - `true` |
| **multipath**  dictionary | Change multipath selection criteria |
| **as_path**  dictionary | AS path |
| **ignore**  dictionary | Ignore as-path related check for multipath selection. |
| **onwards**  boolean | Ignore everything onwards as-path for multipath selection.  Choices:   - `false` - `true` |
| **redistribute_internal**  boolean | Redistribute internal BGP routes.  Choices:   - `false` - `true` |
| **router_id**  string | Configure Router-id. Example- A.B.C.D IPv4 address. |
| **unsafe_ebgp_policy**  boolean | Make eBGP neighbors with no policy pass all routes(cisco-support).  Choices:   - `false` - `true` |
| **default_information**  dictionary | Control distribution of default information. |
| **originate**  boolean | Distribute a default route  Choices:   - `false` - `true` |
| **default_metric**  integer | Default metric. Example-<1-4294967295>. |
| **mpls**  dictionary | Enable mpls parameters. |
| **activate**  dictionary | Enter mpls interfaces in BGP mpls activate mode. |
| **interface**  string | Name of interface to enable mpls. |
| **neighbors**  list / elements=dictionary | Specify a neighbor router. |
| **advertisement_interval**  integer | Minimum interval between sending BGP routing updates.Example-<0-600>. |
| **bfd**  dictionary | Configure BFD parameters. |
| **fast_detect**  dictionary | Enable Fast detection |
| **disable**  boolean | Prevent bfd settings from being inherited from the parent.  Choices:   - `false` - `true` |
| **strict_mode**  boolean | Hold down neighbor session until BFD session is up  Choices:   - `false` - `true` |
| **minimum_interval**  integer | Specifies the BFD session’s minimum-interval value for the neighbor. |
| **multiplier**  integer | Specifies the BFD session’s multiplier value for the neighbor. |
| **bmp_activate**  dictionary | Enable BMP logging for this neighbor. |
| **server**  integer | Enable BMP connection to particular server.Example-<1-8>. |
| **capability**  dictionary | Advertise capability to the peer. |
| **additional_paths**  dictionary | BGP additional-paths commands. |
| **receive**  dictionary | Additional paths receive capability |
| **disable**  boolean | set receive capability  Choices:   - `false` - `true` |
| **set**  boolean | set receive capability  Choices:   - `false` - `true` |
| **send**  dictionary | Additional paths Send capability |
| **disable**  boolean | set send capability  Choices:   - `false` - `true` |
| **set**  boolean | set send capability  Choices:   - `false` - `true` |
| **suppress**  dictionary | Suppress advertising capability to the peer. |
| **all**  dictionary | all capability |
| **inheritance_disable**  boolean | Do not inherit this configuration from parent group.  Choices:   - `false` - `true` |
| **set**  boolean | set all.  Choices:   - `false` - `true` |
| **four_byte_AS**  dictionary | 4-byte-as capability |
| **set**  boolean | set 4_byte_as.  Choices:   - `false` - `true` |
| **cluster_id**  string | Cluster ID of this router acting as a route reflector. |
| **description**  string | Neighbor specific description. |
| **dmz_link_bandwidth**  dictionary | Propagate the DMZ link bandwidth. |
| **inheritance_disable**  boolean | Do not inherit this configuration from parent group.  Choices:   - `false` - `true` |
| **set**  boolean | set dmz-link-bandwidth.  Choices:   - `false` - `true` |
| **dscp**  string | Set IP DSCP (DiffServ CodePoint).Please refer vendor document for valid entries. |
| **ebgp_multihop**  dictionary | Allow EBGP neighbors not on directly connected networks. |
| **mpls**  boolean | Disable BGP MPLS forwarding.  Choices:   - `false` - `true` |
| **value**  integer | maximum hop count.Example-<1-255>. |
| **ebgp_recv_extcommunity_dmz**  dictionary | Receive extcommunity dmz link bandwidth from ebgp neighbor. |
| **inheritance_disable**  boolean | Prevent ebgp-recv-community-dmz from being inherited from parent  Choices:   - `false` - `true` |
| **set**  boolean | set ebgp-recv-community-dmz.  Choices:   - `false` - `true` |
| **ebgp_send_extcommunity_dmz**  dictionary | Send extcommunity dmz link bandwidth from ebgp neighbor. |
| **cumulatie**  boolean | Send cumulative community dmz link bandwidth of all multipaths to ebgp neighbor.  Choices:   - `false` - `true` |
| **inheritance_disable**  boolean | Prevent ebgp-send-community-dmz from being inherited from parent  Choices:   - `false` - `true` |
| **set**  boolean | set ebgp-send-community-dmz.  Choices:   - `false` - `true` |
| **egress_engineering**  dictionary | Enable egress peer engineering for this neighbor. |
| **inheritance_disable**  boolean | Prevent egress-engineering from being inherited from parent  Choices:   - `false` - `true` |
| **set**  boolean | set egress-engineering.  Choices:   - `false` - `true` |
| **enforce_first_as**  dictionary | Enforce the first AS for EBGP routes |
| **disable**  boolean | disable enforce 1st as  Choices:   - `false` - `true` |
| **graceful_maintenance**  dictionary | Attributes for Graceful Maintenance. This will cause neighbors to de-prefer routes from this router and choose alternates. This allows the router to be brought in or out of service gracefully. |
| **activate**  dictionary | Routes will be announced with the graceful maintenance attributes while activated either here or under router bgp configuration. |
| **inheritance_disable**  boolean | Prevent activate from being inherited from the parent.  Choices:   - `false` - `true` |
| **set**  boolean | activate.  Choices:   - `false` - `true` |
| **as_prepends**  dictionary | Number of times to prepend the local AS number to the AS path of routes. Default=0 |
| **inheritance_disable**  boolean | Prevent as prepends from being inherited from the parent.  Choices:   - `false` - `true` |
| **value**  integer | Range of values for as prepends.Example-<0-6> . |
| **local_preference**  dictionary | local preference with which to advertise routes to ibgp neigbors. Default=No Touch |
| **inheritance_disable**  boolean | Prevent local preference from being inherited from the parent.  Choices:   - `false` - `true` |
| **value**  integer | Range of values for Local Preference.Example-<0-4294967295> . |
| **set**  boolean | set graceful maintenance.  Choices:   - `false` - `true` |
| **graceful_restart**  dictionary | Enable graceful restart support for this neighbor. |
| **restart_time**  integer | Restart time advertised to neighbors in seconds <1-4095>. |
| **stalepath_time**  integer | Maximum time to wait for restart of GR capable peers in seconds <1-4095>. |
| **ignore_connected_check**  dictionary | Bypass the directly connected nexthop check for single-hop eBGP peering |
| **inheritance_disable**  boolean | Prevent ignore-connected-check from being inherited from the parent  Choices:   - `false` - `true` |
| **set**  boolean | set ignore-connected-check.  Choices:   - `false` - `true` |
| **keychain**  dictionary | Set keychain based authentication. |
| **inheritance_disable**  boolean | Prevent keychain from being inherited from parent.  Choices:   - `false` - `true` |
| **name**  string | Name of the key chain - maximum 32 characters. |
| **local**  dictionary | Configure local parameter |
| **address**  dictionary | IPv4 address |
| **inheritance_disable**  boolean | Prevent local address from being inherited from parent.  Choices:   - `false` - `true` |
| **ipv4_address**  string | IPv4 address <A.B.C.D>. |
| **local_as**  dictionary | Specify local AS number. |
| **inheritance_disable**  boolean | Prevent local AS from being inherited from parent.  Choices:   - `false` - `true` |
| **value**  integer | 2 byte, 4 byte As number |
| **log**  dictionary | Logging update messages per neighbor. |
| **log_message**  dictionary | Logging update/notification messages per neighbor. |
| **in**  dictionary | Inbound log messages |
| **disable**  boolean | Disable inbound message logging.  Choices:   - `false` - `true` |
| **inheritance_disable**  boolean | Prevents the msg log from being inherited from the parent.  Choices:   - `false` - `true` |
| **value**  integer | Range for message log buffer size <1-100>. |
| **out**  dictionary | Outbound log messages |
| **disable**  boolean | Disable inbound message logging.  Choices:   - `false` - `true` |
| **inheritance_disable**  boolean | Prevents the msg log from being inherited from the parent.  Choices:   - `false` - `true` |
| **value**  integer | Range for message log buffer size <1-100>. |
| **neighbor_address**  aliases: neighbor  string / required | Neighbor router address. |
| **origin_as**  dictionary | BGP origin-AS knobs. |
| **validation**  dictionary | BGP origin-AS validation knobs. |
| **disable**  boolean | Disable RPKI origin-AS validation.  Choices:   - `false` - `true` |
| **receive_buffer_size**  integer | Set socket and BGP receive buffer size.Example <512-131072>. |
| **remote_as**  integer | Neighbor Autonomous System. |
| **send_buffer_size**  integer | Set socket and BGP send buffer size.Example <4096-131072>. |
| **session_open_mode**  string | Establish BGP session using this TCP open mode.  Choices:   - `"active-only"` - `"both"` - `"passive-only"` |
| **shutdown**  dictionary | Administratively shut down this neighbor. |
| **inheritance_disable**  boolean | Prevent shutdown from being inherited from parent  Choices:   - `false` - `true` |
| **set**  boolean | shutdown.  Choices:   - `false` - `true` |
| **tcp**  dictionary | TCP session configuration commands. |
| **mss**  dictionary | Maximum Segment Size. |
| **inheritance_disable**  boolean | Prevent mss from being inherited from parent  Choices:   - `false` - `true` |
| **value**  integer | TCP initial maximum segment size. |
| **timers**  dictionary | BGP per neighbor timers. |
| **holdtime**  integer | hold time <3-65535> or 0 Disable hold time. |
| **keepalive_time**  integer | keepalive interval <0-65535>. |
| **ttl_security**  dictionary | Enable EBGP TTL security. |
| **inheritance_disable**  boolean | Prevent ttl-security from being inherited from parent  Choices:   - `false` - `true` |
| **set**  boolean | set ttl-security  Choices:   - `false` - `true` |
| **update**  dictionary | BGP Update configuration. |
| **in**  dictionary | Inbound update message handling. |
| **filtering**  dictionary | Inbound update message filtering |
| **attribute_filter**  dictionary | Attribute-filter configuration. |
| **group**  string | Name of group. |
| **logging**  dictionary | Update filtering syslog message. |
| **disable**  boolean | Disable update filtering syslog message.  Choices:   - `false` - `true` |
| **update_message**  dictionary | Filtered update messages. |
| **buffers**  integer | Number of buffers to store filtered update messages. |
| **update_source**  string | Source of routing updates.Refer vendor document for valid values. |
| **rd**  dictionary | route distinguisher. |
| **auto**  boolean | Automatic route distinguisher.  Choices:   - `false` - `true` |
| **socket**  dictionary | set socket parameters. |
| **receive_buffer_size**  integer | socket receive buffer size.Example-<512-131072>. |
| **send_buffer_size**  integer | socket send buffer size.Example- <4096-131072>. |
| **timers**  dictionary | BGP per neighbor timers. |
| **holdtime**  integer | hold time <3-65535> or 0 Disable hold time. |
| **keepalive_time**  integer | keepalive interval <0-65535>. |
| **vrf**  string | VRF name. |
| **running_config**  string | The state the configuration should be left in. - State *purged* removes all the BGP configurations from the target device. Use caution with this state. - State *deleted* only removes BGP attributes that this modules manages and does not negate the BGP process completely. Thereby, preserving address-family related configurations under BGP context. - Running states *deleted* and *replaced* will result in an error if there are address-family configuration lines present under a neighbor, or a vrf context that is to be removed. Please use the [cisco.iosxr.iosxr_bgp_address_family](iosxr_bgp_address_family_module.md#ansible-collections-cisco-iosxr-iosxr-bgp-address-family-module) or [cisco.iosxr.iosxr_bgp_neighbor_address_family](iosxr_bgp_neighbor_address_family_module.md#ansible-collections-cisco-iosxr-iosxr-bgp-neighbor-address-family-module) modules for prior cleanup. - Refer to examples for more details. |
| **state**  string | The state the configuration should be left in.  Choices:   - `"deleted"` - `"merged"` ← (default) - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` - `"purged"` |

## [Notes](iosxr_bgp_global_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`.

## [Examples](iosxr_bgp_global_module.md#id4)

```yaml+jinja
##### Using Merged ##########################################
-----------------------------------------------------------------

# configuration on device  Before merge state:

#RP/0/0/CPU0:10#show running-config router bgp
#Thu Feb  4 09:38:36.245 UTC
#% No such configuration item(s)
#RP/0/0/CPU0:10#

# --------------Merge state---------------
#  - name: Merge the following configuration
#       cisco.iosxr.iosxr_bgp_global:
#         config:
#             as_number: 65536
#             default_metric: 5
#             socket:
#               receive_buffer_size: 514
#               send_buffer_size: 4098
#             bgp:
#               confederation:
#                 identifier: 4
#               bestpath:
#                 med:
#                   confed: True
#               cluster_id: 5
#               router_id: 192.0.2.10
#             neighbors:
#               - neighbor: 192.0.2.13
#                 remote_as: 65538
#                 bfd:
#                   fast_detect:
#                     strict_mode: True
#                   multiplier: 6
#                   minimum_interval: 20
#             vrfs:
#               - vrf: vrf1
#                 default_metric: 5
# ----------------------------------------
#

# commands:
# - "router bgp 65536",
# - "bgp cluster-id 5",
# - "bgp router-id 192.0.2.10",
# - "bgp bestpath med confed",
# - "bgp confederation identifier 4",
# - "default-metric 5",
# - "socket receive-buffer-size 514",
# - "socket send-buffer-size 4098",
# - "neighbor 192.0.2.13",
# - "bfd fast-detect strict-mode",
# - "bfd minimum-interval 20",
# - "bfd multiplier 6",
# - "remote-as 65538",
# - "vrf vrf1",
# - "default-metric 5"

# Configuration on device After Merge state:
# --------------------------------------------

# RP/0/0/CPU0:10#show running-config router bgp
# Thu Feb  4 09:44:32.480 UTC
# router bgp 65536
#  bgp confederation identifier 4
#  bgp router-id 192.0.2.10
#  bgp cluster-id 5
#  default-metric 5
#  socket send-buffer-size 4098
#  bgp bestpath med confed
#  socket receive-buffer-size 514
#  neighbor 192.0.2.13
#   remote-as 65538
#   bfd fast-detect strict-mode
#   bfd multiplier 6
#   bfd minimum-interval 20
#  !
#  vrf vrf1
#   default-metric 5
#  !
# !

##### Using replaced ###########################################

# configuration on device before replaced
# --------------------------------------------
#
# RP/0/0/CPU0:10#show running-config router bgp
# Thu Feb  4 09:44:32.480 UTC
# router bgp 65536
#  bgp confederation identifier 4
#  bgp router-id 192.0.2.10
#  bgp cluster-id 5
#  default-metric 5
#  socket send-buffer-size 4098
#  bgp bestpath med confed
#  socket receive-buffer-size 514
#  neighbor 192.0.2.13
#   remote-as 65538
#   bfd fast-detect strict-mode
#   bfd multiplier 6
#   bfd minimum-interval 20
#  !
#  vrf vrf1
#   default-metric 5
#  !
# !
# --------------Replace state---------------
# - name: Replace the following configuration
#       cisco.iosxr.iosxr_bgp_global:
#         state: replaced
#         config:
#             as_number: 65536
#             default_metric: 4
#             socket:
#               receive_buffer_size: 514
#               send_buffer_size: 4098
#             bgp:
#               confederation:
#                 identifier: 4
#               bestpath:
#                 med:
#                   confed: True
#               cluster_id: 5
#               router_id: 192.0.2.10
#             neighbors:
#               - neighbor: 192.0.2.14
#                 remote_as: 65538
#                 bfd:
#                   fast_detect:
#                     strict_mode: True
#                   multiplier: 6
#                   minimum_interval: 20
#             vrfs:
#               - vrf: vrf1
#                 default_metric: 5
# -------------------------------------------
# commands:
# - "router bgp 65536",
# - "default-metric 4",
# - "neighbor 192.0.2.14",
# - "bfd fast-detect strict-mode",
# - "bfd minimum-interval 20",
# - "bfd multiplier 6",
# - "remote-as 65538",
# - "no neighbor 192.0.2.13"

# configuration on device After Replaced  state:
# ----------------------------------------------

# RP/0/0/CPU0:10#show running-config router bgp
# Thu Feb  4 09:54:11.161 UTC
# router bgp 65536
#  bgp confederation identifier 4
#  bgp router-id 192.0.2.10
#  bgp cluster-id 5
#  default-metric 4
#  socket send-buffer-size 4098
#  bgp bestpath med confed
#  socket receive-buffer-size 514
#  neighbor 192.0.2.14
#   remote-as 65538
#   bfd fast-detect strict-mode
#   bfd multiplier 6
#   bfd minimum-interval 20
#  !
#  vrf vrf1
#   default-metric 5
#  !
# !

##### Using deleted ############################################

# configuration on device Before deleted state
# ---------------------------------------------
#
# RP/0/0/CPU0:10#show running-config router bgp
# Thu Feb  4 09:54:11.161 UTC
# router bgp 65536
#  bgp confederation identifier 4
#  bgp router-id 192.0.2.10
#  bgp cluster-id 5
#  default-metric 4
#  socket send-buffer-size 4098
#  bgp bestpath med confed
#  socket receive-buffer-size 514
#  neighbor 192.0.2.14
#   remote-as 65538
#   bfd fast-detect strict-mode
#   bfd multiplier 6
#   bfd minimum-interval 20
#  !
#  vrf vrf1
#   default-metric 5
#  !
# !
#
# --------------------------------------------------------
# - name: Delete BGP configurations handled by this module
#  cisco.iosxr.iosxr_bgp_global:
#         state: deleted
#         config:
#             as_number: 65536
#
# commands:
# "router bgp 65536",
# "no bgp cluster-id 5",
# "no bgp router-id 192.0.2.10",
# "no bgp bestpath med confed",
# "no bgp confederation identifier 4",
# "no default-metric 4",
# "no socket receive-buffer-size 514",
# "no socket send-buffer-size 4098",
# "no neighbor 192.0.2.14",
# "no vrf vrf1"
#
# configuration on device after delete
# -------------------------------------------
#
# RP/0/0/CPU0:10#show running-config router bgp
# Thu Feb  4 10:01:08.232 UTC
# router bgp 65536
# !
#

################# Using Purged ########################################

# configuration on device Before Purged state
# --------------------------------------------
#
# RP/0/0/CPU0:10#show running-config router bgp
# Thu Feb  4 09:54:11.161 UTC
# router bgp 65536
#  bgp confederation identifier 4
#  bgp router-id 192.0.2.10
#  bgp cluster-id 5
#  default-metric 4
#  socket send-buffer-size 4098
#  bgp bestpath med confed
#  socket receive-buffer-size 514
#  address-family ipv4 unicast
#  neighbor 192.0.2.14
#   remote-as 65538
#   bfd fast-detect strict-mode
#   bfd multiplier 6
#   bfd minimum-interval 20
#   address-family ipv4 unicast
#  !
#  vrf vrf1
#   default-metric 5
#  !
# !
#
# - name: Purge all BGP configurations from the device
#   cisco.iosxr.iosxr_bgp_global:
#     state: purged
#
#  commands:
# - no router bgp 65563
#
# configuration on device After purged state:
# ---------------------------------------------
#
# #RP/0/0/CPU0:10#show running-config router bgp
# #Thu Feb  4 09:38:36.245 UTC
# #% No such configuration item(s)
# #RP/0/0/CPU0:10#
#
#
# ################# Using Rendred #######################################################
#
# - name: Render platform specific configuration lines (without connecting to the device)
#   cisco.iosxr.iosxr_bgp_global:
#         state: rendered
#         config:
#             as_number: 1
#             default_metric: 4
#             vrfs:
#               - vrf: vrf3
#                 bfd:
#                   minimum_interval: 20
#                   multiplier: 10
#                 bgp:
#                   fast_external_fallover:
#                     disable: True
#                   router_id: 1.2.3.4
#                   auto_policy_soft_reset:
#                     disable: True
#                 #rd:
#                 #  auto: True
#                 #  #value: 1
#                 timers:
#                   keepalive_time: 20
#                   holdtime: 30
#               - vrf: vrf2
#                 bgp:
#                   enforce_first_as:
#                     disable: True
#                 default_metric: 4
#                 neighbors:
#                   - neighbor: 1.1.1.3
#                     remote_as: 2
#                     graceful_maintenance:
#                       set: True
#                       activate:
#                         #set: True
#                         inheritance_disable: True
#                       local_preference:
#                         value: 1
#                         #inheritance_disable: True
#                       as_prepends:
#                         value: 2
# rendered output
# ------------------------------------
#   "router bgp 1",
#   "default-metric 4",
#   "vrf vrf3",
#   "bfd multiplier 10",
#   "bfd minimum-interval 20",
#   "bgp auto-policy-soft-reset disable",
#   "bgp fast-external-fallover disable",
#   "bgp router-id 1.2.3.4",
#   "timers bgp 20 30",
#   "vrf vrf2",
#   "neighbor 1.1.1.3",
#   "remote-as 2",
#   "graceful-maintenance",
#   "graceful-maintenance activate inheritance-disable",
#   "graceful-maintenance local-preference 1",
#   "graceful-maintenance as-prepends 2",
#   "bgp enforce-first-as disable",
#   "default-metric 4"
#
# ############## Using parsed #####################
#  parsed.cfg
#  ------------
# router bgp 65536
#  bgp confederation identifier 4
#  bgp router-id 192.0.2.10
#  bgp cluster-id 5
#  default-metric 4
#  socket send-buffer-size 4098
#  bgp bestpath med confed
#  socket receive-buffer-size 514
#  neighbor 192.0.2.11
#   remote-as 65537
#   cluster-id 3
#  !
#  neighbor 192.0.2.14
#   remote-as 65538
#   bfd fast-detect strict-mode
#   bfd multiplier 6
#   bfd minimum-interval 20
#  !
# !
# ------------------------------------
#
# - name: Parse externally provided BGP config
#   cisco.iosxr.iosxr_bgp_global:
#     running_config: "{{ lookup('file', 'parsed.cfg') }}"
#     state: parsed
#
# #Task output using parsed
#     as_number: "65536"
#     default_metric: 4
#     socket:
#       receive_buffer_size: 514
#       send_buffer_size: 4098
#     bgp:
#       confederation:
#         identifier: 4
#       bestpath:
#         med:
#           confed: true
#       cluster_id: "5"
#       router_id: "192.0.2.10"
#     neighbors:
#       - neighbor: 192.0.2.11
#         remote_as: 65537
#         cluster_id: "3"
#       - neighbor: "192.0.2.14"
#         remote_as: 65538
#         bfd:
#           fast_detect:
#             strict_mode: true
#           multiplier: 6
#           minimum_interval: 20
```

### Authors

- Ashwini Mhatre (@amhatre)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
