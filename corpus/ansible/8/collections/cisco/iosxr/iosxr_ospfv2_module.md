---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_ospfv2 module – Resource module to configure OSPFv2."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_ospfv2_module.html
fetched_at: 2026-07-28T01:26:54+00:00
---
# cisco.iosxr.iosxr_ospfv2 module – Resource module to configure OSPFv2.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/ui/repo/published/cisco/iosxr/) (version 5.0.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_ospfv2`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_ospfv2_module.md#synopsis)
- [Parameters](iosxr_ospfv2_module.md#parameters)
- [Notes](iosxr_ospfv2_module.md#notes)
- [Examples](iosxr_ospfv2_module.md#examples)
- [Return Values](iosxr_ospfv2_module.md#return-values)

## [Synopsis](iosxr_ospfv2_module.md#id1)

- This module manages global OSPFv2 configuration on devices running Cisco IOS-XR

Aliases: ospfv2

## [Parameters](iosxr_ospfv2_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of OSPFv2 process configuration |
| **processes**  list / elements=dictionary | A list of OSPFv2 instances configuration |
| **address_family_unicast**  boolean | Enable unicast topology for ipv4 address family  **Choices:**   - `false` - `true` |
| **adjacency_stagger**  dictionary | Stagger OSPFv2 adjacency bring up |
| **disable**  boolean | Disable stagger OSPFv2 adjacency  **Choices:**   - `false` - `true` |
| **max_adjacency**  integer | Maximum simultaneous neighbors to bring up |
| **min_adjacency**  integer | Initial number of neighbors to bring up per area (default 2) |
| **apply_weight**  dictionary | Enable weights configured under interfaces for load sharing |
| **bandwidth**  integer | Reference bandwidth to use for calculation (Mbits/sec) |
| **default_weight**  integer | Specify default weight value to use when it is not configured under interface |
| **areas**  list / elements=dictionary | Configure OSPFv2 areas’ properties |
| **area_id**  string / required | Area ID as IP address or integer |
| **authentication**  dictionary | Enable authentication |
| **keychain**  string | Specify keychain name |
| **message_digest**  dictionary | Use message-digest authentication |
| **keychain**  string | Specify keychain name |
| **no_auth**  boolean | Use no authentication  **Choices:**   - `false` - `true` |
| **authentication_key**  dictionary | Used to mention authentication password (key) |
| **clear**  string | Specifies an UNENCRYPTED password (key) will follow |
| **encrypted**  string | Specifies an ENCRYPTED password (key) will follow |
| **password**  string | The OSPFv2 password (key) |
| **bfd**  dictionary | Configure BFD parameters |
| **fast_detect**  dictionary | Configure fast detection |
| **set**  boolean | Enable fast detection only  **Choices:**   - `false` - `true` |
| **strict_mode**  boolean | Hold down neighbor session until BFD session is up  **Choices:**   - `false` - `true` |
| **minimum_interval**  integer | Hello interval in milli-seconds |
| **multiplier**  integer | Detect multiplier |
| **cost**  integer | Interface cost |
| **dead_interval**  integer | Interval after which a neighbor is declared dead |
| **default_cost**  integer | Set the summary default-cost of a NSSA/stub area. Stub’s advertised external route metric |
| **hello_interval**  integer | Time between HELLO packets |
| **mpls**  dictionary | Configure MPLS routing protocol parameters |
| **ldp**  dictionary | Configure LDP parameters |
| **auto_config**  boolean | Enable LDP IGP interface auto-configuration  **Choices:**   - `false` - `true` |
| **sync**  boolean | Enable LDP IGP synchronization  **Choices:**   - `false` - `true` |
| **sync_igp_shortcuts**  boolean | LDP sync for igp-shortcut tunnels  **Choices:**   - `false` - `true` |
| **traffic_eng**  boolean | Configure an ospf area to run MPLS Traffic Engineering  **Choices:**   - `false` - `true` |
| **mtu_ignore**  string | Enable/Disable ignoring of MTU in DBD packets  **Choices:**   - `"enable"` - `"disable"` |
| **nssa**  dictionary | NSSA settings for the area |
| **default_information_originate**  dictionary | Originate default Type 7 LSA |
| **metric**  integer | OSPFv2 default metric |
| **metric_type**  integer | Metric type for default routes |
| **no_redistribution**  boolean | Do not send redistributed LSAs into NSSA area  **Choices:**   - `false` - `true` |
| **no_summary**  boolean | Do not send summary LSAs into NSSA area  **Choices:**   - `false` - `true` |
| **set**  boolean | Configure area as NSSA  **Choices:**   - `false` - `true` |
| **translate**  dictionary | Translate LSA |
| **type7**  dictionary | Translate from Type 7 to Type 5 |
| **always**  boolean | Always translate LSAs  **Choices:**   - `false` - `true` |
| **ranges**  list / elements=dictionary | Summarize routes matching address/mask (border routers only) |
| **address**  string / required | IP in Prefix format (x.x.x.x/len) |
| **advertise**  boolean | Advertise this range (default)  **Choices:**   - `false` - `true` |
| **not_advertise**  boolean | DoNotAdvertise this range  **Choices:**   - `false` - `true` |
| **route_policy**  list / elements=dictionary | Specify the route-policy to filter type 3 LSAs (list can have one inbound and/or one outbound policy only) |
| **direction**  string | Specify inbound or outbound  **Choices:**   - `"in"` - `"out"` |
| **parameters**  list / elements=string | Specify parameter values for the policy |
| **stub**  dictionary | Settings for configuring the area as a stub |
| **no_summary**  boolean | Do not send summary LSA into stub area  **Choices:**   - `false` - `true` |
| **set**  boolean | Configure the area as a stub  **Choices:**   - `false` - `true` |
| **transmit_delay**  integer | Estimated time needed to send link-state update packet |
| **virtual_link**  list / elements=dictionary | Define a virtual link |
| **authentication**  dictionary | Enable authentication |
| **keychain**  string | Specify keychain name |
| **message_digest**  dictionary | Use message-digest authentication |
| **keychain**  string | Specify keychain name |
| **no_auth**  boolean | Use no authentication  **Choices:**   - `false` - `true` |
| **authentication_key**  dictionary | Used to mention authentication password (key) |
| **clear**  string | Specifies an UNENCRYPTED password (key) will follow |
| **encrypted**  string | Specifies an ENCRYPTED password (key) will follow |
| **password**  string | The OSPFv2 password (key) |
| **dead_interval**  integer | Interval after which a neighbor is declared dead |
| **hello_interval**  integer | Time between HELLO packets |
| **id**  string / required | Router-ID of virtual link neighbor (A.B.C.D) |
| **message_digest_key**  dictionary | Message digest authentication password (key) |
| **id**  integer / required | Key ID (1-255) |
| **md5**  dictionary | Use MD5 Algorithm |
| **clear**  boolean | Specifies an UNENCRYPTED password (key) will follow  **Choices:**   - `false` - `true` |
| **encrypted**  boolean | Specifies an ENCRYPTED password (key) will follow  **Choices:**   - `false` - `true` |
| **password**  string | The OSPFv2 password (key) |
| **retransmit_interval**  integer | Delay between LSA retransmissions |
| **transmit_delay**  integer | Link state transmit delay |
| **authentication**  dictionary | Enable authentication |
| **keychain**  string | Specify keychain name |
| **message_digest**  dictionary | Use message-digest authentication |
| **keychain**  string | Specify keychain name |
| **set**  boolean | Specify message-digest selection  **Choices:**   - `false` - `true` |
| **no_auth**  boolean | Use no authentication  **Choices:**   - `false` - `true` |
| **authentication_key**  dictionary | Used to mention authentication password (key) |
| **clear**  boolean | Specifies an UNENCRYPTED password (key) will follow  **Choices:**   - `false` - `true` |
| **encrypted**  boolean | Specifies an ENCRYPTED password (key) will follow  **Choices:**   - `false` - `true` |
| **password**  string | The OSPFv2 password (key) |
| **auto_cost**  dictionary | Calculate OSPFv2 interface cost according to bandwidth |
| **disable**  boolean | Assign OSPFv2 cost based on interface type  **Choices:**   - `false` - `true` |
| **reference_bandwidth**  integer | Specify reference bandwidth in megabits per sec |
| **bfd**  dictionary | Configure BFD parameters |
| **fast_detect**  dictionary | Configure fast detection |
| **set**  boolean | Enable fast detection only  **Choices:**   - `false` - `true` |
| **strict_mode**  boolean | Hold down neighbor session until BFD session is up  **Choices:**   - `false` - `true` |
| **minimum_interval**  integer | Hello interval in milli-seconds |
| **multiplier**  integer | Detect multiplier |
| **capability**  dictionary | Enable specific OSPFv2 feature |
| **opaque**  dictionary | Configure opaque LSA |
| **disable**  boolean | Disable Opaque LSA capability  **Choices:**   - `false` - `true` |
| **set**  boolean | Enable opaque LSA  **Choices:**   - `false` - `true` |
| **type7**  string | NSSA capability |
| **cost**  integer | Interface cost (1-65535) |
| **database_filter**  string | Filter OSPFv2 LSA during synchronization and flooding (all outgoing LSA). Enable/Disable filtering  **Choices:**   - `"enable"` - `"disable"` |
| **dead_interval**  integer | Interval after which a neighbor is declared dead |
| **default_information_originate**  dictionary | Distribute default route |
| **always**  boolean | Always advertise default route  **Choices:**   - `false` - `true` |
| **metric**  integer | OSPFv2 default metric |
| **metric_type**  integer | OSPFv2 metric type for default routes |
| **route_policy**  string | Apply route-policy to default-information origination |
| **set**  boolean | Enable distribution of default route  **Choices:**   - `false` - `true` |
| **default_metric**  integer | Set metric of redistributed routes |
| **demand_circuit**  string | Enable/Disable OSPFv2 demand circuit  **Choices:**   - `"enable"` - `"disable"` |
| **distance**  dictionary | Define an administrative distance |
| **admin_distance**  list / elements=dictionary | Administrative distance |
| **access_list**  string | Access list name |
| **source**  string | Source IP address |
| **value**  integer | Distance value |
| **wildcard**  string | IP wild card bits (A.B.C.D) |
| **ospf_distance**  dictionary | OSPFv2 administrative distance |
| **external**  integer | Distance for external routes |
| **inter_area**  integer | Distance for inter-area routes |
| **intra_area**  integer | Distance for intra-area routes |
| **distribute_bgp_ls**  dictionary | Enable Distribution of LSAs to external services |
| **instance_id**  integer | Set distribution process instance identifier |
| **throttle**  integer | Throttle time between successive LSA updates |
| **distribute_link_state**  dictionary | Enable Distribution of LSAs to external services |
| **instance_id**  integer | Set distribution process instance identifier |
| **throttle**  integer | Throttle time between successive LSA updates |
| **distribute_list**  list / elements=dictionary | Filter networks in routing updates (list can have one inbound and/or one outbound policy only) |
| **access_list**  string | Inbound/outbound access-list |
| **direction**  string | Filter incoming/outgoing routing updates  **Choices:**   - `"in"` - `"out"` |
| **outgoing_params**  dictionary | Specify additional parameters for outgoing updates only |
| **id**  string | For BGP, specify AS number. 2-byte AS number (or) 4-byte AS number in asdot (X.Y) format (or) 4-byte AS number in asplain format  For OSPF, specify OSPFv2 instance name |
| **route_type**  string | Type of routes  **Choices:**   - `"bgp"` - `"connected"` - `"dagr"` - `"ospf"` - `"static"` |
| **route_policy**  string | Route Policy to filter OSPFv2 prefixes (for incoming updates only) |
| **external_out**  string | Enable/Disable advertisement of intra-area prefixes as external  **Choices:**   - `"enable"` - `"disable"` |
| **flood_reduction**  string | Enable/Disable OSPFv2 Flood Reduction  **Choices:**   - `"enable"` - `"disable"` |
| **hello_interval**  integer | Time between HELLO packets (<1-65535> seconds) |
| **ignore_lsa_mospf**  boolean | Do not complain upon receiving MOSPFv2 Type 6 LSA  **Choices:**   - `false` - `true` |
| **link_down_fast_detect**  boolean | Enable fast or early detection of link-down events  **Choices:**   - `false` - `true` |
| **log_adjacency_changes**  dictionary | Log adjacency state changes |
| **detail**  boolean | Log all state changes  **Choices:**   - `false` - `true` |
| **disable**  boolean | Disable log adjacency changes  **Choices:**   - `false` - `true` |
| **set**  boolean | Set log adjacency  **Choices:**   - `false` - `true` |
| **loopback_stub_network**  string | Advertise loopback as a stub network  **Choices:**   - `"enable"` - `"disable"` |
| **max_lsa**  dictionary | Feature to limit the number of non-self-originated LSAs |
| **ignore_count**  integer | Set count on how many times adjacencies can be suppressed |
| **ignore_time**  integer | Set number of minutes during which all adjacencies are suppressed |
| **reset_time**  integer | Set number of minutes after which ignore-count is reset to zero |
| **threshold**  integer | Threshold value (%) at which to generate a warning message |
| **warning_only**  boolean | Log a warning message when limit is exceeded  **Choices:**   - `false` - `true` |
| **max_metric**  dictionary | Set maximum metric |
| **router_lsa**  dictionary | Maximum metric in self-originated router-LSAs |
| **external_lsa**  dictionary | External LSA configuration |
| **max_metric_value**  integer | Set max metric value for external LSAs |
| **set**  boolean | Set external-lsa attribute  **Choices:**   - `false` - `true` |
| **include_stub**  boolean | Advertise Max metric for Stub links as well  **Choices:**   - `false` - `true` |
| **on_startup**  dictionary | Effective only at startup |
| **set**  boolean | Set on-startup attribute  **Choices:**   - `false` - `true` |
| **wait_for_bgp_asn**  integer | ASN of BGP to wait for |
| **wait_period**  integer | Wait period in seconds after startup |
| **set**  boolean | Set router-lsa attribute  **Choices:**   - `false` - `true` |
| **summary_lsa**  dictionary | Summary LSAs configuration |
| **max_metric_value**  integer | Max metric value for summary LSAs |
| **set**  boolean | Set summary-lsa attribute  **Choices:**   - `false` - `true` |
| **message_digest_key**  dictionary | Message digest authentication password (key) |
| **id**  integer / required | Key ID |
| **md5**  dictionary / required | Use MD5 Algorithm |
| **clear**  boolean | Specifies an UNENCRYPTED password (key) will follow  **Choices:**   - `false` - `true` |
| **encrypted**  boolean | Specifies an ENCRYPTED password (key) will follow  **Choices:**   - `false` - `true` |
| **password**  string | The OSPFv2 password (key) |
| **microloop_avoidance**  dictionary | Avoid microloops |
| **protected**  boolean | Avoid microloops for protected prefixes only)  **Choices:**   - `false` - `true` |
| **rib_update_delay**  integer | Delay to introduce between SPF and RIB updates |
| **segment_routing**  boolean | Enable segment routing microloop avoidance  **Choices:**   - `false` - `true` |
| **monitor_convergence**  dictionary | Enables OSPFv2 route convergence monitoring |
| **prefix_list**  string | Enables Individual Prefix Monitoring |
| **track_external_routes**  boolean | Enables Tracking External(Type-5/7) Prefix monitoring  **Choices:**   - `false` - `true` |
| **track_ip_frr**  boolean | Enables Tracking IP-Frr Convergence  **Choices:**   - `false` - `true` |
| **track_summary_routes**  boolean | Enables Tracking Summary(Inter-Area) Prefix monitoring  **Choices:**   - `false` - `true` |
| **mpls**  dictionary | Configure MPLS routing protocol parameters |
| **ldp**  dictionary | Configure LDP parameters |
| **auto_config**  boolean | Enable LDP IGP interface auto-configuration  **Choices:**   - `false` - `true` |
| **sync**  boolean | Enable LDP IGP synchronization  **Choices:**   - `false` - `true` |
| **sync_igp_shortcuts**  boolean | LDP sync for igp-shortcut tunnels  **Choices:**   - `false` - `true` |
| **traffic_eng**  dictionary | Routing protocol commands for MPLS Traffic Engineering |
| **autoroute_exclude**  dictionary | Exclude IP address destinations from using TE tunnels |
| **parameters**  list / elements=string | Specify parameter values for the policy |
| **route_policy**  string | Policy name |
| **igp_intact**  boolean | Retain one or more IPv4 nexthops with tunnel nexthops  **Choices:**   - `false` - `true` |
| **ldp_sync_update**  boolean | Enable LDP sync induced metric propagation  **Choices:**   - `false` - `true` |
| **multicast_intact**  boolean | Publish multicast-intact paths to RIB  **Choices:**   - `false` - `true` |
| **router_id**  string | Traffic Engineering stable IP address for system |
| **mtu_ignore**  string | Enable/Disable ignoring of MTU in DBD packets  **Choices:**   - `"enable"` - `"disable"` |
| **network**  dictionary | Network type |
| **broadcast**  boolean | Specify OSPFv2 broadcast multi-access network  **Choices:**   - `false` - `true` |
| **non_broadcast**  boolean | Specify OSPFv2 NBMA network  **Choices:**   - `false` - `true` |
| **point_to_multipoint**  boolean | Specify OSPFv2 point-to-multipoint network  **Choices:**   - `false` - `true` |
| **point_to_point**  boolean | Specify OSPFv2 point-to-point network  **Choices:**   - `false` - `true` |
| **nsf**  dictionary | Non-stop forwarding |
| **cisco**  dictionary | Cisco Non-stop forwarding |
| **enforce_global**  boolean | Cancel NSF restart when non-NSF-aware neighbors detected for the whole OSPFv2 process  **Choices:**   - `false` - `true` |
| **set**  boolean | Enable Cisco NSF  **Choices:**   - `false` - `true` |
| **flush_delay_time**  integer | Maximum time allowed for external route learning |
| **ietf**  dictionary | IETF graceful restart |
| **helper_disable**  boolean | Disable router’s helper support level  **Choices:**   - `false` - `true` |
| **set**  boolean | Only enable ietf option  **Choices:**   - `false` - `true` |
| **interval**  integer | Minimum interval between NSF restarts (<90-3600> seconds) |
| **lifetime**  integer | Maximum route lifetime following restart (<90-1800> seconds) |
| **nsr**  boolean | Enable NSR for all VRFs in this process. ‘False’ option to disable NSR for all VRFs in this process  **Choices:**   - `false` - `true` |
| **packet_size**  integer | Size of OSPFv2 packets to use. min=576 max=MTU bytes |
| **passive**  string | Enable/Disable passive  **Choices:**   - `"enable"` - `"disable"` |
| **prefix_suppression**  dictionary | Suppress advertisement of the prefixes |
| **secondary_address**  boolean | Enable/Disable secondary address suppression  **Choices:**   - `false` - `true` |
| **set**  boolean | Set the suppression option  **Choices:**   - `false` - `true` |
| **priority**  integer | Router priority |
| **process_id**  string / required | The OSPFv2 Process ID |
| **protocol_shutdown**  dictionary | Protocol specific configuration |
| **host_mode**  boolean | Only traffic destined for this box allowed(cisco-support)  **Choices:**   - `false` - `true` |
| **limit**  dictionary | High watermark for incoming priority events |
| **high**  integer | Hello events are dropped when incoming event queue exceeds this value |
| **low**  integer | DBD/LS Update/Req packets are dropped when incoming event queue exceeds this value |
| **medium**  integer | LSA ACKs are dropped when incoming event queue exceeds this value |
| **on_reload**  boolean | Shutdown post reload only  **Choices:**   - `false` - `true` |
| **set**  boolean | Shutdown the OSPFv2 Protocol  **Choices:**   - `false` - `true` |
| **redistribute**  dictionary | Redistribute information from another routing Protocol |
| **id**  string | OnePK application name for application routes (or) AS number for bgp and eigrp (or) instance name for isis and ospf |
| **level**  integer | ISIS levels  **Choices:**   - `1` - `2` - `12` |
| **lsa_type_summary**  boolean | LSA type 3 for redistributed routes  **Choices:**   - `false` - `true` |
| **match**  string | Redistribution of routes. For OSPFv2 - external/internal/nssa-external 1/2. For EIGRP - external/internal |
| **metric**  integer | Metric for redistributed routes |
| **metric_type**  integer | OSPFv2 exterior metric type for redistributed routes  **Choices:**   - `1` - `2` |
| **nssa_only**  boolean | Redistribute to NSSA areas only  **Choices:**   - `false` - `true` |
| **preserve_med**  boolean | Preserve med of BGP routes  **Choices:**   - `false` - `true` |
| **route_policy**  dictionary | Apply route-policy to redistribution |
| **name**  string | Name of the policy |
| **parameters**  list / elements=string | Specify parameter values for the policy |
| **route_type**  string | Route type to redistribute  **Choices:**   - `"application"` - `"bgp"` - `"connected"` - `"dagr"` - `"eigrp"` - `"isis"` - `"mobile"` - `"ospf"` - `"rip"` - `"static"` - `"subscriber"` |
| **tag**  integer | Set tag for routes redistributed into OSPFv2 |
| **retransmit_interval**  integer | Delay between LSA retransmissions |
| **router_id**  string | OSPFv2 router-id in IPv4 address format (A.B.C.D) |
| **security_ttl**  dictionary | Enable security |
| **hops**  integer | Maximum number of IP hops allowed <1-254> |
| **set**  boolean | Enable ttl security  **Choices:**   - `false` - `true` |
| **summary_in**  string | Enable/Disable advertisement of external prefixes as inter-area  **Choices:**   - `"enable"` - `"disable"` |
| **summary_prefix**  list / elements=dictionary | Configure IP address summaries |
| **not_advertise**  boolean | Suppress routes that match the specified prefix/mask pair  **Choices:**   - `false` - `true` |
| **prefix**  string / required | IP summary address/mask (A.B.C.D/prefix) |
| **tag**  integer | Set tag |
| **timers**  dictionary | Configure timer related constants |
| **graceful_shutdown**  dictionary | Timers for graceful shutdown(cisco-support) |
| **initial_delay**  integer | Delay before starting graceful shutdown |
| **retain_routes**  integer | Time to keep routes active after graceful shutdown |
| **lsa**  dictionary | OSPFv2 global LSA timers |
| **group_pacing**  integer | OSPFv2 LSA group pacing timer. Interval between group of LSA being refreshed or maxaged |
| **min_arrival**  integer | OSPFv2 MinLSArrival timer. The minimum interval in millisec between accepting the same LSA |
| **refresh**  integer | OSPFv2 LSA refresh interval. How often self-originated LSAs should be refreshed, in seconds |
| **pacing_flood**  integer | OSPFv2 flood pacing timer. Interval in msec to pace flooding on all interfaces |
| **throttle**  dictionary | OSPFv2 throttle timers |
| **fast_reroute**  integer | Fast-reroute throttle timer. Delay between end of SPF and start of the fast-reroute computation in milliseconds |
| **lsa_all**  dictionary | LSA throttle timers for all types of OSPFv2 LSAs |
| **initial_delay**  integer | Delay to generate first occurance of LSA in milliseconds |
| **max_delay**  integer | Maximum delay between originating the same LSA in milliseconds |
| **min_delay**  integer | Minimum delay between originating the same LSA in milliseconds |
| **spf**  dictionary | OSPFv2 SPF throttle timers |
| **change_delay**  integer | Delay between receiving a change to SPF calculation in milliseconds |
| **max_wait**  integer | Maximum wait time in milliseconds for SPF calculations |
| **second_delay**  integer | Delay between first and second SPF calculation in milliseconds |
| **transmit_delay**  integer | Estimated time needed to send link-state update packet |
| **weight**  integer | Interface weight |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config router ospf**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` - `"overridden"` |

## [Notes](iosxr_ospfv2_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md)

## [Examples](iosxr_ospfv2_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# RP/0/RP0/CPU0:anton#show running-config router ospf
# Thu Jun 11 15:54:44.569 UTC
# % No such configuration item(s)
#

- name: Merge provided OSPFv2 configuration with the existing configuration
  cisco.iosxr.iosxr_ospfv2:
    config:
      processes:
      - process_id: '27'
        areas:
        - area_id: '10'
          hello_interval: 2
          authentication:
            keychain: ansi11393
      - process_id: '26'
        adjacency_stagger:
          max_adjacency: 20
          min_adjacency: 10
      - process_id: '10'
        authentication:
          keychain: ansible_test1102
        areas:
        - area_id: '11'
          default_cost: 5
          cost: 11
        - area_id: 22
          default_cost: 6
      - process_id: '30'
        areas:
        - area_id: 11
          default_cost: 5
        - area_id: 22
          default_cost: 6

        cost: 2
        default_metric: 10
        transmit_delay: 2
        hello_interval: 1
        dead_interval: 2
        retransmit_interval: 2
        weight: 2
        packet_size: 577
        priority: 1
        router_id: 2.2.2.2
        demand_circuit: enable
        passive: disable
        summary_in: enable
        flood_reduction: disable
        mtu_ignore: enable
        external_out: disable
    state: merged

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": {}
#
#  "commands": [
#        "router ospf 30",
#        "cost 2",
#        "weight 2",
#        "passive disable",
#        "priority 1",
#        "flood-reduction disable",
#        "default-metric 10",
#        "router-id 2.2.2.2",
#        "demand-circuit enable",
#        "packet-size 577",
#        "transmit-delay 2",
#        "summary-in enable",
#        "external-out disable",
#        "dead-interval 2",
#        "hello-interval 1",
#        "retransmit-interval 2",
#        "mtu-ignore enable",
#        "area 11 default-cost 5",
#        "area 22 default-cost 6",
#        "router ospf 26",
#        "adjacency stagger 10 20",
#        "authentication message-digest keychain ansible1101pass",
#        "router ospf 27",
#        "area 10 authentication keychain ansi11393",
#        "area 10 hello-interval 2",
#        "router ospf 10",
#        "authentication keychain ansible_test1102",
#        "area 11 default-cost 5",
#        "area 11 cost 11",
#        "area 22 default-cost 6"
#    ]
#
#  "after": {
#        "processes": [
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "cost": 11,
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "authentication": {
#                    "keychain": "ansible_test1102"
#                },
#                "process_id": "10"
#            },
#            {
#                "adjacency_stagger": {
#                    "max_adjacency": 20,
#                    "min_adjacency": 10
#                },
#                "authentication": {
#                    "message_digest": {
#                        "keychain": "ansible1101pass"
#                    }
#                },
#                "process_id": "26"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "10",
#                        "authentication": {
#                            "keychain": "ansi11393"
#                        },
#                        "hello_interval": 2
#                    }
#                ],
#                "process_id": "27"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "cost": 2,
#                "dead_interval": 2,
#                "default_metric": 10,
#                "demand_circuit": "enable",
#                "external_out": "disable",
#                "flood_reduction": "disable",
#                "hello_interval": 1,
#                "mtu_ignore": "enable",
#                "packet_size": 577,
#                "passive": "disable",
#                "priority": 1,
#                "process_id": "30",
#                "retransmit_interval": 2,
#                "router_id": "2.2.2.2",
#                "summary_in": "enable",
#                "transmit_delay": 2,
#                "weight": 2
#            }
#        ]
#    }
#
#
# ------------
# After state
# ------------
#
# RP/0/RP0/CPU0:anton#show running-config router ospf
# Thu Jun 11 16:06:44.406 UTC
# router ospf 10
#  authentication keychain ansible_test1102
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospf 26
#  authentication message-digest keychain ansible1101pass
#  adjacency stagger 10 20
# !
# router ospf 27
#  area 10
#  authentication keychain ansi11393
#   hello-interval 2
# !
# !
# router ospf 30
#  router-id 2.2.2.2
#  summary-in enable
#  external-out disable
#  cost 2
#  packet-size 577
#  weight 2
#  passive disable
#  priority 1
#  mtu-ignore enable
#  flood-reduction disable
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit enable
#  hello-interval 1
#  transmit-delay 2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
#

# Using replaced
#
# ------------
# Before state
# ------------
#
#
# RP/0/RP0/CPU0:anton#show running-config router ospf
# Thu Jun 11 16:06:44.406 UTC
# router ospf 10
#  authentication keychain ansible_test1102
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospf 26
#  authentication message-digest keychain ansible1101pass
#  adjacency stagger 10 20
# !
# router ospf 27
#  area 10
#  authentication keychain ansi11393
#   hello-interval 2
# !
# !
# router ospf 30
#  router-id 2.2.2.2
#  summary-in enable
#  external-out disable
#  cost 2
#  packet-size 577
#  weight 2
#  passive disable
#  priority 1
#  mtu-ignore enable
#  flood-reduction disable
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit enable
#  hello-interval 1
#  transmit-delay 2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
#

- name: Replace OSPFv2 routes configurations from the device
  cisco.iosxr.iosxr_ospfv2:
    config:
      processes:
      - process_id: 27
        areas:
        - area_id: 10
          hello_interval: 2
        - area_id: 20
          cost: 2
          default_cost: 2
          authentication:
            keychain: ansi11393
      - process_id: 26
        adjacency_stagger:
          min_adjacency: 10
          max_adjacency: 20
    state: replaced

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": {
#        "processes": [
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "cost": 11,
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "authentication": {
#                    "keychain": "ansible_test1102"
#                },
#                "process_id": "10"
#            },
#            {
#                "adjacency_stagger": {
#                    "max_adjacency": 20,
#                    "min_adjacency": 10
#                },
#                "authentication": {
#                    "message_digest": {
#                        "keychain": "ansible1101pass"
#                    }
#                },
#                "process_id": "26"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "10",
#                        "authentication": {
#                            "keychain": "ansi11393"
#                        },
#                        "hello_interval": 2
#                    }
#                ],
#                "process_id": "27"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "cost": 2,
#                "dead_interval": 2,
#                "default_metric": 10,
#                "demand_circuit": "enable",
#                "external_out": "disable",
#                "flood_reduction": "disable",
#                "hello_interval": 1,
#                "mtu_ignore": "enable",
#                "packet_size": 577,
#                "passive": "disable",
#                "priority": 1,
#                "process_id": "30",
#                "retransmit_interval": 2,
#                "router_id": "2.2.2.2",
#                "summary_in": "enable",
#                "transmit_delay": 2,
#                "weight": 2
#            }
#        ]
#    }
#
#  "commands": [
#        "router ospf 27",
#        "no area 10 authentication keychain ansi11393",
#        "area 20 authentication keychain ansi11393",
#        "area 20 default-cost 2",
#        "area 20 cost 2"
#    ]
#
#  "after": {
#        "processes": [
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "cost": 11,
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "authentication": {
#                    "keychain": "ansible_test1102"
#                },
#                "process_id": "10"
#            },
#            {
#                "adjacency_stagger": {
#                    "max_adjacency": 20,
#                    "min_adjacency": 10
#                },
#                "authentication": {
#                    "message_digest": {
#                        "keychain": "ansible1101pass"
#                    }
#                },
#                "process_id": "26"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "10",
#                        "hello_interval": 2
#                    },
#                    {
#                        "area_id": "20",
#                        "authentication": {
#                            "keychain": "ansi11393"
#                        },
#                        "cost": 2,
#                        "default_cost": 2
#                    }
#                ],
#                "process_id": "27"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "cost": 2,
#                "dead_interval": 2,
#                "default_metric": 10,
#                "demand_circuit": "enable",
#                "external_out": "disable",
#                "flood_reduction": "disable",
#                "hello_interval": 1,
#                "mtu_ignore": "enable",
#                "packet_size": 577,
#                "passive": "disable",
#                "priority": 1,
#                "process_id": "30",
#                "retransmit_interval": 2,
#                "router_id": "2.2.2.2",
#                "summary_in": "enable",
#                "transmit_delay": 2,
#                "weight": 2
#            }
#        ]
#    }
#
#
# -----------
# After state
# -----------
#
# RP/0/RP0/CPU0:anton(config)#do show running-config router ospf
# Thu Jun 11 16:40:31.038 UTC
# router ospf 10
#  authentication keychain ansible_test1102
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospf 26
#  authentication message-digest keychain ansible1101pass
#  adjacency stagger 10 20
# !
# router ospf 27
#  area 10
#   hello-interval 2
#  !
#  area 20
#   cost 2
#   authentication keychain ansi11393
#   default-cost 2
#  !
# !
# router ospf 30
#  router-id 2.2.2.2
#  summary-in enable
#  external-out disable
#  cost 2
#  packet-size 577
#  weight 2
#  passive disable
#  priority 1
#  mtu-ignore enable
#  flood-reduction disable
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit enable
#  hello-interval 1
#  transmit-delay 2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
#

# Using overridden
#
# ------------
# Before state
# ------------
#
#
# RP/0/RP0/CPU0:anton#show running-config router ospf
# Thu Jun 11 16:06:44.406 UTC
# router ospf 10
#  authentication keychain ansible_test1102
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospf 26
#  authentication message-digest keychain ansible1101pass
#  adjacency stagger 10 20
# !
# router ospf 27
#  area 10
#  authentication keychain ansi11393
#   hello-interval 2
# !
# !
# router ospf 30
#  router-id 2.2.2.2
#  summary-in enable
#  external-out disable
#  cost 2
#  packet-size 577
#  weight 2
#  passive disable
#  priority 1
#  mtu-ignore enable
#  flood-reduction disable
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit enable
#  hello-interval 1
#  transmit-delay 2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
#

- name: Override existing OSPFv2 configurations from the device
  cisco.iosxr.iosxr_ospfv2:
    config:
      processes:
      - process_id: 27
        areas:
        - area_id: 10
          hello_interval: 2
          authentication:
            keychain: ansi11393
        - area_id: 20
          cost: 2
          default_cost: 2
          authentication:
            keychain: ansi11393
      - process_id: 26
        adjacency_stagger:
          min_adjacency: 10
          max_adjacency: 20
    state: overridden

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": {
#        "processes": [
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "cost": 11,
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "authentication": {
#                    "keychain": "ansible_test1102"
#                },
#                "process_id": "10"
#            },
#            {
#                "adjacency_stagger": {
#                    "max_adjacency": 20,
#                    "min_adjacency": 10
#                },
#                "authentication": {
#                    "message_digest": {
#                        "keychain": "ansible1101pass"
#                    }
#                },
#                "process_id": "26"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "10",
#                        "authentication": {
#                            "keychain": "ansi11393"
#                        },
#                        "hello_interval": 2
#                    }
#                ],
#                "process_id": "27"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "cost": 2,
#                "dead_interval": 2,
#                "default_metric": 10,
#                "demand_circuit": "enable",
#                "external_out": "disable",
#                "flood_reduction": "disable",
#                "hello_interval": 1,
#                "mtu_ignore": "enable",
#                "packet_size": 577,
#                "passive": "disable",
#                "priority": 1,
#                "process_id": "30",
#                "retransmit_interval": 2,
#                "router_id": "2.2.2.2",
#                "summary_in": "enable",
#                "transmit_delay": 2,
#                "weight": 2
#            }
#        ]
#    }
#
#  "commands": [
#        "router ospf 10",
#        "no authentication keychain ansible_test1102",
#        "no area 11 default-cost 5",
#        "no area 11 cost 11",
#        "no area 22 default-cost 6",
#        "router ospf 30",
#        "no cost 2",
#        "no weight 2",
#        "no passive disable",
#        "no priority 1",
#        "no flood-reduction disable",
#        "no default-metric 10",
#        "no router-id 2.2.2.2",
#        "no demand-circuit enable",
#        "no packet-size 577",
#        "no transmit-delay 2",
#        "no summary-in enable",
#        "no external-out disable",
#        "no dead-interval 2",
#        "no hello-interval 1",
#        "no retransmit-interval 2",
#        "no mtu-ignore enable",
#        "no area 11 default-cost 5",
#        "no area 22 default-cost 6",
#        "router ospf 27",
#        "area 20 authentication keychain ansi11393",
#        "area 20 default-cost 2",
#        "area 20 cost 2"
#    ]
#
#  "after": {
#        "processes": [
#            {
#                "process_id": "10"
#            },
#            {
#                "adjacency_stagger": {
#                    "max_adjacency": 20,
#                    "min_adjacency": 10
#                },
#                "authentication": {
#                    "message_digest": {
#                        "keychain": "ansible1101pass"
#                    }
#                },
#                "process_id": "26"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "10",
#                        "authentication": {
#                            "keychain": "ansi11393"
#                        },
#                        "hello_interval": 2
#                    },
#                    {
#                        "area_id": "20",
#                        "authentication": {
#                            "keychain": "ansi11393"
#                        },
#                        "cost": 2,
#                        "default_cost": 2
#                    }
#                ],
#                "process_id": "27"
#            },
#            {
#                "process_id": "30"
#            }
#        ]
#    }
#
#
# -----------
# After state
# -----------
#
# RP/0/RP0/CPU0:anton#show running-config router ospf
# Thu Jun 11 16:50:36.332 UTC
# router ospf 10
# !
# router ospf 26
#  authentication message-digest keychain ansible1101pass
#  adjacency stagger 10 20
# !
# router ospf 27
#  area 10
#   authentication keychain ansi11393
#   hello-interval 2
#  !
#  area 20
#   cost 2
#   authentication keychain ansi11393
#   default-cost 2
#  !
# !
# router ospf 30
# !
#

# Using deleted
#
# ------------
# Before state
# ------------
#
#
# RP/0/RP0/CPU0:anton#show running-config router ospf
# Thu Jun 11 16:06:44.406 UTC
# router ospf 10
#  authentication keychain ansible_test1102
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospf 26
#  authentication message-digest keychain ansible1101pass
#  adjacency stagger 10 20
# !
# router ospf 27
#  area 10
#  authentication keychain ansi11393
#   hello-interval 2
# !
# !
# router ospf 30
#  router-id 2.2.2.2
#  summary-in enable
#  external-out disable
#  cost 2
#  packet-size 577
#  weight 2
#  passive disable
#  priority 1
#  mtu-ignore enable
#  flood-reduction disable
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit enable
#  hello-interval 1
#  transmit-delay 2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
#

- name: Deleted existing OSPFv2 configurations from the device
  cisco.iosxr.iosxr_ospfv2:
    config:
      processes:
      - process_id: '10'
      - process_id: '26'
      - process_id: '27'
      - process_id: '30'
    state: deleted

#
#
# ------------------------
# Module Execution Result
# ------------------------
#
#  "before": {
#        "processes": [
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "cost": 11,
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "authentication": {
#                    "keychain": "ansible_test1102"
#                },
#                "process_id": "10"
#            },
#            {
#                "adjacency_stagger": {
#                    "max_adjacency": 20,
#                    "min_adjacency": 10
#                },
#                "authentication": {
#                    "message_digest": {
#                        "keychain": "ansible1101pass"
#                    }
#                },
#                "process_id": "26"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "10",
#                        "authentication": {
#                            "keychain": "ansi11393"
#                        },
#                        "hello_interval": 2
#                    }
#                ],
#                "process_id": "27"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "cost": 2,
#                "dead_interval": 2,
#                "default_metric": 10,
#                "demand_circuit": "enable",
#                "external_out": "disable",
#                "flood_reduction": "disable",
#                "hello_interval": 1,
#                "mtu_ignore": "enable",
#                "packet_size": 577,
#                "passive": "disable",
#                "priority": 1,
#                "process_id": "30",
#                "retransmit_interval": 2,
#                "router_id": "2.2.2.2",
#                "summary_in": "enable",
#                "transmit_delay": 2,
#                "weight": 2
#            }
#        ]
#    },
#
#  "commands": [
#        "router ospf 10",
#        "no authentication keychain ansible_test1102",
#        "no area 11 default-cost 5",
#        "no area 11 cost 11",
#        "no area 22 default-cost 6",
#        "router ospf 26",
#        "no adjacency stagger 10 20",
#        "no authentication message-digest keychain ansible1101pass",
#        "router ospf 27",
#        "no area 10 authentication keychain ansi11393",
#        "no area 10 hello-interval 2",
#        "router ospf 30",
#        "no cost 2",
#        "no weight 2",
#        "no passive disable",
#        "no priority 1",
#        "no flood-reduction disable",
#        "no default-metric 10",
#        "no router-id 2.2.2.2",
#        "no demand-circuit enable",
#        "no packet-size 577",
#        "no transmit-delay 2",
#        "no summary-in enable",
#        "no external-out disable",
#        "no dead-interval 2",
#        "no hello-interval 1",
#        "no retransmit-interval 2",
#        "no mtu-ignore enable",
#        "no area 11 default-cost 5",
#        "no area 22 default-cost 6"
#    ]
#
#  "after": {
#        "processes": [
#            {
#                "process_id": "10"
#            },
#            {
#                "process_id": "26"
#            },
#            {
#                "process_id": "27"
#            },
#            {
#                "process_id": "30"
#            }
#        ]
#    }
#
#
# -----------
# After state
# -----------
#
# RP/0/RP0/CPU0:anton(config)#show running-config router ospf
# Thu Jun 11 17:07:34.218 UTC
# router ospf 10
# !
# router ospf 26
# !
# router ospf 27
# !
# router ospf 30
# !

# Using parsed
# parsed.cfg
# ------------
# Thu Jun 11 17:28:51.918 UTC
# router ospf 10
#  authentication keychain ansible_test1102
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospf 26
#  authentication message-digest keychain ansible1101pass
#  adjacency stagger 10 20
# !
# router ospf 27
#  area 10
#   authentication keychain ansi11393
#   hello-interval 2
#  !
# !
# router ospf 30
#  router-id 2.2.2.2
#  summary-in enable
#  external-out disable
#  cost 2
#  packet-size 577
#  weight 2
#  passive disable
#  priority 1
#  mtu-ignore enable
#  flood-reduction disable
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit enable
#  hello-interval 1
#  transmit-delay 2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
- name: Parsed the device configuration to get output commands
  cisco.iosxr.iosxr_ospfv2:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "parsed": {
#        "processes": [
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "cost": 11,
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "authentication": {
#                    "keychain": "ansible_test1102"
#                },
#                "process_id": "10"
#            },
#            {
#                "adjacency_stagger": {
#                    "max_adjacency": 20,
#                    "min_adjacency": 10
#                },
#                "authentication": {
#                    "message_digest": {
#                        "keychain": "ansible1101pass"
#                    }
#                },
#                "process_id": "26"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "10",
#                        "authentication": {
#                            "keychain": "ansi11393"
#                        },
#                        "hello_interval": 2
#                    }
#                ],
#                "process_id": "27"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "cost": 2,
#                "dead_interval": 2,
#                "default_metric": 10,
#                "demand_circuit": "enable",
#                "external_out": "disable",
#                "flood_reduction": "disable",
#                "hello_interval": 1,
#                "mtu_ignore": "enable",
#                "packet_size": 577,
#                "passive": "disable",
#                "priority": 1,
#                "process_id": "30",
#                "retransmit_interval": 2,
#                "router_id": "2.2.2.2",
#                "summary_in": "enable",
#                "transmit_delay": 2,
#                "weight": 2
#            }
#        ]
#    }

# Using rendered
#
#
- name: Render the commands for provided  configuration
  cisco.iosxr.iosxr_ospfv2:
    config:
      processes:
      - process_id: 27
        areas:
        - area_id: 10
          hello_interval: 2
          authentication:
            keychain: ansi11393
      - process_id: 26
        adjacency_stagger:
          min_adjacency: 10
          max_adjacency: 20
      - process_id: 10
        authentication:
          keychain: ansible_test1102
        areas:
        - area_id: 11
          default_cost: 5
          cost: 11
        - area_id: 22
          default_cost: 6
      - process_id: 30
        areas:
        - area_id: 11
          default_cost: 5
        - area_id: 22
          default_cost: 6

        cost: 2
        default_metric: 10
        transmit_delay: 2
        hello_interval: 1
        dead_interval: 2
        retransmit_interval: 2
        weight: 2
        packet_size: 577
        priority: 1
        router_id: 2.2.2.2
        demand_circuit: enable
        passive: disable
        summary_in: enable
        flood_reduction: disable
        mtu_ignore: enable
        external_out: disable
    state: rendered

#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#
# "rendered": [
#        "router ospf 27",
#        "area 10 authentication keychain ansi11393",
#        "area 10 hello-interval 2",
#        "router ospf 26",
#        "adjacency stagger 10 20",
#        "authentication message-digest keychain ansible1101pass",
#        "router ospf 10",
#        "authentication keychain ansible_test1102",
#        "area 11 default-cost 5",
#        "area 11 cost 11",
#        "area 22 default-cost 6",
#        "router ospf 30",
#        "cost 2",
#        "weight 2",
#        "passive disable",
#        "priority 1",
#        "flood-reduction disable",
#        "default-metric 10",
#        "router-id 2.2.2.2",
#        "demand-circuit enable",
#        "packet-size 577",
#        "transmit-delay 2",
#        "summary-in enable",
#        "external-out disable",
#        "dead-interval 2",
#        "hello-interval 1",
#        "retransmit-interval 2",
#        "mtu-ignore enable",
#        "area 11 default-cost 5",
#        "area 22 default-cost 6"
#    ]

# Using gathered
#
# Before state:
# -------------
#
# RP/0/RP0/CPU0:anton#show running-config router ospf
# Thu Jun 11 16:06:44.406 UTC
# router ospf 10
#  authentication keychain ansible_test1102
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospf 26
#  authentication message-digest keychain ansible1101pass
#  adjacency stagger 10 20
# !
# router ospf 27
#  area 10
#  authentication keychain ansi11393
#   hello-interval 2
# !
# !
# router ospf 30
#  router-id 2.2.2.2
#  summary-in enable
#  external-out disable
#  cost 2
#  packet-size 577
#  weight 2
#  passive disable
#  priority 1
#  mtu-ignore enable
#  flood-reduction disable
#  dead-interval 2
#  retransmit-interval 2
#  demand-circuit enable
#  hello-interval 1
#  transmit-delay 2
#  default-metric 10
#  area 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
#
- name: Gather ospfv2 routes configuration
  cisco.iosxr.iosxr_ospfv2:
    state: gathered
#
#
# -------------------------
# Module Execution Result
# -------------------------
#
#    "gathered": {
#        "processes": [
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "cost": 11,
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "authentication": {
#                    "keychain": "ansible_test1102"
#                },
#                "process_id": "10"
#            },
#            {
#                "adjacency_stagger": {
#                    "max_adjacency": 20,
#                    "min_adjacency": 10
#                },
#                "authentication": {
#                    "message_digest": {
#                        "keychain": "ansible1101pass"
#                    }
#                },
#                "process_id": "26"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "10",
#                        "authentication": {
#                            "keychain": "ansi11393"
#                        },
#                        "hello_interval": 2
#                    }
#                ],
#                "process_id": "27"
#            },
#            {
#                "areas": [
#                    {
#                        "area_id": "11",
#                        "default_cost": 5
#                    },
#                    {
#                        "area_id": "22",
#                        "default_cost": 6
#                    }
#                ],
#                "cost": 2,
#                "dead_interval": 2,
#                "default_metric": 10,
#                "demand_circuit": "enable",
#                "external_out": "disable",
#                "flood_reduction": "disable",
#                "hello_interval": 1,
#                "mtu_ignore": "enable",
#                "packet_size": 577,
#                "passive": "disable",
#                "priority": 1,
#                "process_id": "30",
#                "retransmit_interval": 2,
#                "router_id": "2.2.2.2",
#                "summary_in": "enable",
#                "transmit_delay": 2,
#                "weight": 2
#            }
#        ]
#    }
#
# After state:
# -------------
#
# RP/0/RP0/CPU0:anton#show running-config router ospf
# Thu Jun 11 16:06:44.406 UTC
# router ospf 10
#  authentication keychain ansible_test1102
#  area 11
#   cost 11
#   default-cost 5
#  !
#  area 22
#   default-cost 6
#  !
# !
# router ospf 26
#  authentication message-digest keychain ansible1101pass
#  adjacency stagger 10 20
# !
# router ospf 27
#  area 10
#  authentication keychain ansi11393
#   hello-interval 2
# !
# !
# router ospf 30
# router-id 2.2.2.2
# summary-in enable
# external-out disable
# cost 2
# packet-size 577
# weight 2
# passive disable
# priority 1
# mtu-ignore enable
# flood-reduction disable
# dead-interval 2
# retransmit-interval 2
# demand-circuit enable
# hello-interval 1
# transmit-delay 2
# default-metric 10
# area 11
#  default-cost 5
# !
# area 22
#  default-cost 6
# !
# !
#
#
```

## [Return Values](iosxr_ospfv2_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["router ospf 30", "authentication message-digest keychain 'ansible1101pass'"]` |

### Authors

- Rohit Thakur (@rohitthakur2590)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
