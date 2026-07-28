---
collection: ansible
version: "8"
title: "cisco.ios.ios_route_maps module – Resource module to configure route maps."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_route_maps_module.html
fetched_at: 2026-07-28T01:26:25+00:00
---
# cisco.ios.ios_route_maps module – Resource module to configure route maps.

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
> To use it in a playbook, specify: `cisco.ios.ios_route_maps`.

New in cisco.ios 2.1.0

- [Synopsis](ios_route_maps_module.md#synopsis)
- [Parameters](ios_route_maps_module.md#parameters)
- [Notes](ios_route_maps_module.md#notes)
- [Examples](ios_route_maps_module.md#examples)
- [Return Values](ios_route_maps_module.md#return-values)

## [Synopsis](ios_route_maps_module.md#id1)

- This module configures and manages the attributes of Route maps on Cisco IOS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: route_maps

## [Parameters](ios_route_maps_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of configurations for Route maps. |
| **entries**  list / elements=dictionary | A list of configurations entries for Route maps. |
| **action**  string | Route map set operations  **Choices:**   - `"deny"` - `"permit"` |
| **continue_entry**  dictionary | Continue on a different entry within the route-map |
| **entry_sequence**  integer | Route-map entry sequence number  Please refer vendor documentation for valid values |
| **set**  boolean | Set continue  **Choices:**   - `false` - `true` |
| **description**  string | Route-map comment |
| **match**  dictionary | Match values from routing table |
| **additional_paths**  dictionary | BGP Add-Path match policie  BGP Add-Path advertise-set policy |
| **all**  boolean | BGP Add-Path advertise all paths  **Choices:**   - `false` - `true` |
| **best**  integer | BGP Add-Path advertise best n paths (1-3) |
| **best_range**  dictionary | BGP Add-Path advertise best paths (range m to n) |
| **lower_limit**  integer | BGP Add-Path best paths to advertise (lower limit) (1-3) |
| **upper_limit**  integer | BGP Add-Path best paths to advertise (upper limit) (1-3) |
| **group_best**  boolean | BGP Add-Path advertise group-best path  **Choices:**   - `false` - `true` |
| **as_path**  dictionary | Match BGP AS path list |
| **acls**  list / elements=integer | AS path access-list  Please refer vendor documentation for valid values |
| **set**  boolean | Set AS path list  **Choices:**   - `false` - `true` |
| **clns**  dictionary | CLNS information |
| **address**  string | Match address of route or match packet |
| **next_hop**  string | Match next-hop address of route |
| **route_source**  string | Match advertising source address of route |
| **community**  dictionary | Match BGP community list |
| **exact_match**  boolean | Do exact matching of communities  **Choices:**   - `false` - `true` |
| **name**  list / elements=string | Community-list number/Community-list name  Please refer vendor documentation for valid values |
| **extcommunity**  list / elements=string | Match BGP/VPN extended community list  Extended community-list number  Please refer vendor documentation for valid values |
| **interfaces**  list / elements=string | Match first hop interface of route |
| **ip**  dictionary | IP specific information |
| **address**  dictionary | Match address of route or match packet |
| **acls**  list / elements=string | Match entries of acl  IP acl name/number  Please refer vendor documentation for valid values |
| **prefix_lists**  list / elements=string | Match entries of prefix-lists  IP prefix-list name |
| **flowspec**  dictionary | Match src/dest prefix component of flowspec prefix |
| **acls**  list / elements=string | Match entries of acl  IP acl name/number  Please refer vendor documentation for valid values |
| **dest_pfx**  boolean | Match dest prefix component of flowspec prefix  **Choices:**   - `false` - `true` |
| **prefix_lists**  list / elements=string | Match entries of prefix-lists  IP prefix-list name |
| **src_pfx**  boolean | Match source prefix component of flowspec prefix  **Choices:**   - `false` - `true` |
| **next_hop**  dictionary | Match next-hop address of route |
| **acls**  list / elements=string | Match entries of acl  IP acl name/number  Please refer vendor documentation for valid values |
| **prefix_lists**  list / elements=string | Match entries of prefix-lists  IP prefix-list name |
| **set**  boolean | Set next-hop address  **Choices:**   - `false` - `true` |
| **redistribution_source**  dictionary | route redistribution source (EIGRP only) |
| **acls**  list / elements=string | Match entries of acl  IP acl name/number  Please refer vendor documentation for valid values |
| **prefix_lists**  list / elements=string | Match entries of prefix-lists  IP prefix-list name |
| **set**  boolean | Set redistribution-source  **Choices:**   - `false` - `true` |
| **route_source**  dictionary | Match advertising source address of route |
| **acls**  list / elements=string | Match entries of acl  IP acl name/number  Please refer vendor documentation for valid values |
| **prefix_lists**  list / elements=string | Match entries of prefix-lists  IP prefix-list name |
| **redistribution_source**  boolean | route redistribution source (EIGRP only)  **Choices:**   - `false` - `true` |
| **set**  boolean | Set redistribution-source  **Choices:**   - `false` - `true` |
| **ipv6**  dictionary | IPv6 specific information |
| **address**  dictionary | Match address of route or match packet |
| **acl**  string | IPv6 access-list name |
| **prefix_list**  string | IPv6 prefix-list name |
| **flowspec**  dictionary | Match next-hop address of route |
| **acl**  string | IPv6 access-list name |
| **dest_pfx**  boolean | Match dest prefix component of flowspec prefix  **Choices:**   - `false` - `true` |
| **prefix_list**  string | IPv6 prefix-list name |
| **src_pfx**  boolean | Match source prefix component of flowspec prefix  **Choices:**   - `false` - `true` |
| **next_hop**  dictionary | Match next-hop address of route |
| **acl**  string | IPv6 access-list name |
| **prefix_list**  string | IPv6 prefix-list name |
| **route_source**  dictionary | Match advertising source address of route |
| **acl**  string | IPv6 access-list name |
| **prefix_list**  string | IPv6 prefix-list name |
| **length**  dictionary | Packet length |
| **maximum**  integer | Maximum packet length  Please refer vendor documentation for valid values |
| **minimum**  integer | Minimum packet length  Please refer vendor documentation for valid values |
| **local_preference**  dictionary | Local preference for route |
| **set**  boolean | Set the Local preference for route  **Choices:**   - `false` - `true` |
| **value**  list / elements=string | Local preference value  Please refer vendor documentation for valid values |
| **mdt_group**  dictionary | Match routes corresponding to MDT group |
| **acls**  list / elements=string | IP access-list number/IP standard access-list name  Please refer vendor documentation for valid values |
| **set**  boolean | Set and Match routes corresponding to MDT group  **Choices:**   - `false` - `true` |
| **metric**  dictionary | Match metric of route |
| **deviation**  boolean | Deviation option to match metric in a range  **Choices:**   - `false` - `true` |
| **deviation_value**  integer | deviation value, 500 +- 10 creates the range 490 - 510  Please refer vendor documentation for valid values |
| **external**  boolean | Match route using external protocol metric  **Choices:**   - `false` - `true` |
| **value**  integer | Metric value  Please refer vendor documentation for valid values |
| **mpls_label**  boolean | Match routes which have MPLS labels  **Choices:**   - `false` - `true` |
| **policy_lists**  list / elements=string | Match IP policy list |
| **route_type**  dictionary | Match route-type of route |
| **external**  dictionary | external route (BGP, EIGRP and OSPF type 1/2) |
| **set**  boolean | Set external route  **Choices:**   - `false` - `true` |
| **type_1**  boolean | OSPF external type 1 route  **Choices:**   - `false` - `true` |
| **type_2**  boolean | OSPF external type 2 route  **Choices:**   - `false` - `true` |
| **internal**  boolean | internal route (including OSPF intra/inter area)  **Choices:**   - `false` - `true` |
| **level_1**  boolean | IS-IS level-1 route  **Choices:**   - `false` - `true` |
| **level_2**  boolean | IS-IS level-2 route  **Choices:**   - `false` - `true` |
| **local**  boolean | locally generated route  **Choices:**   - `false` - `true` |
| **nssa_external**  dictionary | nssa-external route (OSPF type 1/2) |
| **set**  boolean | Set nssa-external route  **Choices:**   - `false` - `true` |
| **type_1**  boolean | OSPF external type 1 route  **Choices:**   - `false` - `true` |
| **type_2**  boolean | OSPF external type 2 route  **Choices:**   - `false` - `true` |
| **rpki**  dictionary | Match RPKI state of route |
| **invalid**  boolean | RPKI Invalid State  **Choices:**   - `false` - `true` |
| **not_found**  boolean | RPKI Not Found State  **Choices:**   - `false` - `true` |
| **valid**  boolean | RPKI Valid State  **Choices:**   - `false` - `true` |
| **security_group**  dictionary | Security Group |
| **destination**  list / elements=integer | Destination Security Group, destination Security tag  Please refer vendor documentation for valid values |
| **source**  list / elements=integer | Source Security Group, source Security tag  Please refer vendor documentation for valid values |
| **source_protocol**  dictionary | Match source-protocol of route |
| **bgp**  string | Border Gateway Protocol (BGP)  Autonomous system number  Please refer vendor documentation for valid values |
| **connected**  boolean | Connected  **Choices:**   - `false` - `true` |
| **eigrp**  integer | Enhanced Interior Gateway Routing Protocol (EIGRP)  Autonomous system number  Please refer vendor documentation for valid values |
| **isis**  boolean | ISO IS-IS  **Choices:**   - `false` - `true` |
| **lisp**  boolean | Locator ID Separation Protocol (LISP)  **Choices:**   - `false` - `true` |
| **mobile**  boolean | Mobile routes  **Choices:**   - `false` - `true` |
| **ospf**  integer | Open Shortest Path First (OSPF) Process ID  Please refer vendor documentation for valid values |
| **ospfv3**  integer | OSPFv3 Process ID  Please refer vendor documentation for valid values |
| **rip**  boolean | Routing Information Protocol (RIP)  **Choices:**   - `false` - `true` |
| **static**  boolean | Static routes  **Choices:**   - `false` - `true` |
| **tag**  dictionary | Match tag of route |
| **tag_list**  list / elements=string | Route Tag List/Tag list name |
| **value**  list / elements=string | Tag value/Tag in Dotted Decimal eg, 10.10.10.10 |
| **track**  integer | tracking object |
| **sequence**  integer | Sequence to insert to/delete from existing route-map entry  Please refer vendor documentation for valid values |
| **set**  dictionary | Match source-protocol of route |
| **aigp_metric**  dictionary | accumulated metric value |
| **igp_metric**  boolean | metric value from rib  **Choices:**   - `false` - `true` |
| **value**  integer | manual value |
| **as_path**  dictionary | Prepend string for a BGP AS-path attribute |
| **prepend**  dictionary | Prepend to the as-path |
| **as_number**  list / elements=string | AS number  Please refer vendor documentation for valid values |
| **last_as**  integer | Prepend last AS to the as-path  Number of last-AS prepends  Please refer vendor documentation for valid values |
| **tag**  boolean | Set the tag as an AS-path attribute  **Choices:**   - `false` - `true` |
| **automatic_tag**  boolean | Automatically compute TAG value  **Choices:**   - `false` - `true` |
| **clns**  string | OSI summary address  Next hop address  CLNS summary prefix |
| **comm_list**  string | set BGP community list (for deletion)  Community-list name/number  Delete matching communities |
| **community**  dictionary | BGP community attribute |
| **additive**  boolean | Add to the existing community  **Choices:**   - `false` - `true` |
| **gshut**  boolean | Graceful Shutdown (well-known community)  **Choices:**   - `false` - `true` |
| **internet**  boolean | Internet (well-known community)  **Choices:**   - `false` - `true` |
| **local_as**  boolean | Do not send outside local AS (well-known community)  **Choices:**   - `false` - `true` |
| **no_advertise**  boolean | Do not advertise to any peer (well-known community)  **Choices:**   - `false` - `true` |
| **no_export**  boolean | Do not export to next AS (well-known community)  **Choices:**   - `false` - `true` |
| **none**  boolean | No community attribute  **Choices:**   - `false` - `true` |
| **number**  string | community number  community number in aa:nn format  Please refer vendor documentation for valid values |
| **dampening**  dictionary | Set BGP route flap dampening parameters |
| **max_suppress**  integer | Maximum duration to suppress a stable route  Please refer vendor documentation for valid values |
| **penalty_half_time**  integer | half-life time for the penalty  Please refer vendor documentation for valid values |
| **reuse_route_val**  integer | Penalty to start reusing a route  Please refer vendor documentation for valid values |
| **suppress_route_val**  integer | Penalty to start suppressing a route  Please refer vendor documentation for valid values |
| **default**  string | Set default information  Default output interface |
| **extcomm_list**  string | Set BGP/VPN extended community list (for deletion)  Extended community-list number/name  Delete matching extended communities |
| **extcommunity**  dictionary | BGP extended community attribute |
| **cost**  dictionary | Cost extended community |
| **cost_value**  integer | Cost Value (No-preference Cost = 2147483647)  Please refer vendor documentation for valid values |
| **id**  string | Community ID  Please refer vendor documentation for valid values |
| **igp**  boolean | Compare following IGP cost comparison  **Choices:**   - `false` - `true` |
| **pre_bestpath**  boolean | Compare before all other steps in bestpath calculation  **Choices:**   - `false` - `true` |
| **rt**  dictionary | Route Target extended community |
| **additive**  boolean | Add to the existing extcommunity  **Choices:**   - `false` - `true` |
| **address**  string | VPN extended community |
| **range**  dictionary | Specify a range of extended community |
| **lower_limit**  string | VPN extended community |
| **upper_limit**  string | VPN extended community |
| **soo**  string | Site-of-Origin extended community |
| **vpn_distinguisher**  dictionary | VPN Distinguisher |
| **additive**  boolean | Add to the existing extcommunity  **Choices:**   - `false` - `true` |
| **address**  string | VPN extended community |
| **range**  dictionary | Specify a range of extended community |
| **lower_limit**  string | VPN extended community |
| **upper_limit**  string | VPN extended community |
| **global_route**  boolean | Set to global routing table  **Choices:**   - `false` - `true` |
| **interfaces**  list / elements=string | Output interface |
| **ip**  dictionary | IP specific information |
| **address**  string | Specify IP address  Prefix-list name to set ip address |
| **df**  integer | Set DF bit  **Choices:**   - `0` - `1` |
| **global_route**  dictionary | global routing table |
| **address**  string | IP address of next hop |
| **verify_availability**  dictionary | Verify if nexthop is reachable |
| **address**  string | IP address of next hop |
| **sequence**  integer | Sequence to insert into next-hop list  Please refer vendor documentation for valid values |
| **track**  integer | Set the next hop depending on the state of a tracked object  tracked object number  Please refer vendor documentation for valid values |
| **next_hop**  dictionary | Next hop address |
| **address**  string | IP address of next hop |
| **dynamic**  boolean | application dynamically sets next hop  DHCP learned next hop  **Choices:**   - `false` - `true` |
| **encapsulate**  string | Encapsulation profile for VPN nexthop  L3VPN  Encapsulation profile name |
| **peer_address**  boolean | Use peer address (for BGP only)  **Choices:**   - `false` - `true` |
| **recursive**  dictionary | Recursive next-hop |
| **address**  string | IP address of recursive next hop |
| **global_route**  boolean | global routing table  **Choices:**   - `false` - `true` |
| **vrf**  string | VRF |
| **self**  boolean | Use self address (for BGP only)  **Choices:**   - `false` - `true` |
| **verify_availability**  dictionary | Verify if nexthop is reachable |
| **address**  string | IP address of next hop |
| **sequence**  integer | Sequence to insert into next-hop list  Please refer vendor documentation for valid values |
| **set**  boolean | Set and Verify if nexthop is reachable  **Choices:**   - `false` - `true` |
| **track**  integer | Set the next hop depending on the state of a tracked object  tracked object number  Please refer vendor documentation for valid values |
| **precedence**  dictionary | Set precedence field |
| **critical**  boolean | Set critical precedence (5)  **Choices:**   - `false` - `true` |
| **flash**  boolean | Set flash precedence (3)  **Choices:**   - `false` - `true` |
| **flash_override**  boolean | Set flash override precedence (4)  **Choices:**   - `false` - `true` |
| **immediate**  boolean | Set immediate precedence (2)  **Choices:**   - `false` - `true` |
| **internet**  boolean | Set internetwork control precedence (6)  **Choices:**   - `false` - `true` |
| **network**  boolean | Set network control precedence (7)  **Choices:**   - `false` - `true` |
| **priority**  boolean | Set priority precedence (1)  **Choices:**   - `false` - `true` |
| **routine**  boolean | Set routine precedence (0)  **Choices:**   - `false` - `true` |
| **set**  boolean | Just set precedence field  **Choices:**   - `false` - `true` |
| **qos_group**  integer | Set QOS Group ID  Please refer vendor documentation for valid values |
| **tos**  dictionary | Set type of service field |
| **max_reliability**  boolean | Set max reliable TOS (2)  **Choices:**   - `false` - `true` |
| **max_throughput**  boolean | Set max throughput TOS (4)  **Choices:**   - `false` - `true` |
| **min_delay**  boolean | Set min delay TOS (8)  **Choices:**   - `false` - `true` |
| **min_monetary_cost**  boolean | Set min monetary cost TOS (1)  **Choices:**   - `false` - `true` |
| **normal**  boolean | Set normal TOS (0)  **Choices:**   - `false` - `true` |
| **set**  boolean | Just set type of service field  **Choices:**   - `false` - `true` |
| **vrf**  dictionary | VRF |
| **address**  string | IP address of next hop |
| **name**  string | VRF name |
| **verify_availability**  dictionary | Verify if nexthop is reachable |
| **address**  string | IP address of next hop |
| **sequence**  integer | Sequence to insert into next-hop list  Please refer vendor documentation for valid values |
| **set**  boolean | Set and Verify if nexthop is reachable  **Choices:**   - `false` - `true` |
| **track**  integer | Set the next hop depending on the state of a tracked object  tracked object number  Please refer vendor documentation for valid values |
| **ipv6**  dictionary | IPv6 specific information |
| **address**  string | IPv6 address  IPv6 prefix-list |
| **default**  boolean | Set default information  **Choices:**   - `false` - `true` |
| **global_route**  dictionary | global routing table |
| **address**  string | Next hop address (X:X:X:X::X) |
| **verify_availability**  dictionary | Verify if nexthop is reachable |
| **address**  string | Next hop address (X:X:X:X::X) |
| **sequence**  integer | Sequence to insert into next-hop list  Please refer vendor documentation for valid values |
| **track**  integer | Set the next hop depending on the state of a tracked object  tracked object number  Please refer vendor documentation for valid values |
| **next_hop**  dictionary | IPv6 Next hop |
| **address**  string | Next hop address (X:X:X:X::X) |
| **encapsulate**  string | Encapsulation profile for VPN nexthop  L3VPN  Encapsulation profile name |
| **peer_address**  boolean | Use peer address (for BGP only)  **Choices:**   - `false` - `true` |
| **recursive**  string | Recursive next-hop  IPv6 address of recursive next-hop |
| **precedence**  integer | Set precedence field  Precedence value  Please refer vendor documentation for valid values |
| **vrf**  dictionary | VRF name |
| **name**  string | VRF name |
| **verify_availability**  dictionary | Verify if nexthop is reachable |
| **address**  string | IPv6 address of next hop |
| **sequence**  integer | Sequence to insert into next-hop list  Please refer vendor documentation for valid values |
| **track**  integer | Set the next hop depending on the state of a tracked object  tracked object number  Please refer vendor documentation for valid values |
| **level**  dictionary | Where to import route |
| **level_1**  boolean | Import into a level-1 area  **Choices:**   - `false` - `true` |
| **level_1_2**  boolean | Import into level-1 and level-2  **Choices:**   - `false` - `true` |
| **level_2**  boolean | Import into level-2 sub-domain  **Choices:**   - `false` - `true` |
| **nssa_only**  boolean | Import only into OSPF NSSA areas and don’t propagate  **Choices:**   - `false` - `true` |
| **lisp**  string | Locator ID Separation Protocol specific information  Specify a locator-set to use in LISP route-import  The name of the locator set |
| **local_preference**  integer | BGP local preference path attribute  Please refer vendor documentation for valid values |
| **metric**  dictionary | Metric value for destination routing protocol |
| **deviation**  string | Add or subtract metric  **Choices:**   - `"plus"` - `"minus"` |
| **eigrp_delay**  integer | EIGRP delay metric, in 10 microsecond units  Please refer vendor documentation for valid values |
| **metric_bandwidth**  integer | EIGRP Effective bandwidth metric (Loading) where 255 is 100 loaded  Please refer vendor documentation for valid values |
| **metric_reliability**  integer | EIGRP reliability metric where 255 is 100 reliable  Please refer vendor documentation for valid values |
| **metric_value**  integer | Metric value or Bandwidth in Kbits per second  Please refer vendor documentation for valid values |
| **mtu**  integer | EIGRP MTU of the path  Please refer vendor documentation for valid values |
| **metric_type**  dictionary | Type of metric for destination routing protocol |
| **external**  boolean | IS-IS external metric  **Choices:**   - `false` - `true` |
| **internal**  boolean | IS-IS internal metric or Use IGP metric as the MED for BGP  **Choices:**   - `false` - `true` |
| **type_1**  boolean | OSPF external type 1 metric  **Choices:**   - `false` - `true` |
| **type_2**  boolean | OSPF external type 2 metric  **Choices:**   - `false` - `true` |
| **mpls_label**  boolean | Set MPLS label for prefix  **Choices:**   - `false` - `true` |
| **origin**  dictionary | BGP origin code |
| **igp**  boolean | local IGP  **Choices:**   - `false` - `true` |
| **incomplete**  boolean | unknown heritage  **Choices:**   - `false` - `true` |
| **tag**  string | Tag value for destination routing protocol  Tag value A.B.C.D(dotted decimal format)/Tag value |
| **traffic_index**  integer | BGP traffic classification number for accounting  Please refer vendor documentation for valid values |
| **vrf**  string | Define VRF name  VPN Routing/Forwarding instance name |
| **weight**  integer | BGP weight for routing table  Please refer vendor documentation for valid values |
| **route_map**  string | Route map tag/name |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **sh running-config | section ^route-map**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *sh running-config | section ^route-map* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](ios_route_maps_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

## [Examples](ios_route_maps_module.md#id4)

```yaml+jinja
# Using deleted

# Before state:
# -------------
#
# router-ios#sh running-config | section ^route-map
# route-map test_1 deny 10
#  description this is test route
#  match ip next-hop prefix-list test_2_new test_1_new
#  match ip route-source 10
#  match security-group source tag 10 20
#  match local-preference 100 50
#  match mpls-label
# route-map test_1 deny 20
#  match track  105
#  match tag list test_match_tag
#  match route-type level-1
#  match additional-paths advertise-set all group-best
#  match as-path 200 100
#  match ipv6 address test_acl_20
#  continue 100
# route-map test_2 deny 10
#  match security-group source tag 10 20
#  match local-preference 55 105
#  match mpls-label
#  match ipv6 address test_ip_acl
#  match ipv6 next-hop prefix-list test_new
#  match ipv6 route-source route_src_acl
#  set automatic-tag
#  set ip precedence critical
#  set ip address prefix-list 192.0.2.1
#  set aigp-metric 100
#  set extcommunity cost pre-bestpath 10 100
#  set ip df 1
#  set ip next-hop verify-availability 198.51.111.1 100 track 10
#  set ip next-hop recursive global 198.51.110.1

- name: Delete provided Route maps config
  cisco.ios.ios_route_maps:
    config:
      - route_map: test_1
    state: deleted

#  Commands Fired:
#  ---------------
#
#  "commands": [
#         "no route-map test_1"
#     ]

# After state:
# -------------
# router-ios#sh running-config | section ^route-map
# route-map test_2 deny 10
#  match security-group source tag 10 20
#  match local-preference 55 105
#  match mpls-label
#  match ipv6 address test_ip_acl
#  match ipv6 next-hop prefix-list test_new
#  match ipv6 route-source route_src_acl
#  set automatic-tag
#  set ip precedence critical
#  set ip address prefix-list 192.0.2.1
#  set aigp-metric 100
#  set extcommunity cost pre-bestpath 10 100
#  set ip df 1
#  set ip next-hop verify-availability 198.51.111.1 100 track 10
#  set ip next-hop recursive global 198.51.110.1

# Using deleted without any config passed (NOTE: This will delete all Route maps configuration from device)

# Before state:
# -------------
#
# router-ios#sh running-config | section ^route-map
# route-map test_1 deny 10
#  description this is test route
#  match ip next-hop prefix-list test_2_new test_1_new
#  match ip route-source 10
#  match security-group source tag 10 20
#  match local-preference 100 50
#  match mpls-label
# route-map test_1 deny 20
#  match track  105
#  match tag list test_match_tag
#  match route-type level-1
#  match additional-paths advertise-set all group-best
#  match as-path 200 100
#  match ipv6 address test_acl_20
#  continue 100
# route-map test_2 deny 10
#  match security-group source tag 10 20
#  match local-preference 55 105
#  match mpls-label
#  match ipv6 address test_ip_acl
#  match ipv6 next-hop prefix-list test_new
#  match ipv6 route-source route_src_acl
#  set automatic-tag
#  set ip precedence critical
#  set ip address prefix-list 192.0.2.1
#  set aigp-metric 100
#  set extcommunity cost pre-bestpath 10 100
#  set ip df 1
#  set ip next-hop verify-availability 198.51.111.1 100 track 10
#  set ip next-hop recursive global 198.51.110.1

- name: Delete all Route maps config
  cisco.ios.ios_route_maps:
    state: deleted

# Commands Fired:
# ---------------
#
#  "commands": [
#         "no route-map test_1",
#         "no route-map test_2"
#     ]

# After state:
# -------------
# router-ios#sh running-config | section ^route-map
# router-ios#

# Using merged

# Before state:
# -------------
#
# router-ios#sh running-config | section ^route-map
# router-ios#

- name: Merge provided Route maps configuration
  cisco.ios.ios_route_maps:
    config:
      - route_map: test_1
        entries:
          - sequence: 10
            action: deny
            description: this is test route
            match:
              ip:
                next_hop:
                  prefix_lists:
                    - test_1_new
                    - test_2_new
                route_source:
                  acls:
                    - 10
              security_group:
                source:
                  - 10
                  - 20
              local_preference:
                value:
                  - 50
                  - 100
              mpls_label: true
          - sequence: 20
            action: deny
            continue_entry:
              entry_sequence: 100
            match:
              additional_paths:
                all: true
                group_best: true
              as_path:
                acls:
                  - 100
                  - 200
              ipv6:
                address:
                  acl: test_acl_20
              route_type:
                level_1: true
              tag:
                tag_list:
                  - test_match_tag
              track: 105
      - route_map: test_2
        entries:
          - sequence: 10
            action: deny
            match:
              ipv6:
                address:
                  acl: test_ip_acl
                next_hop:
                  prefix_list: test_new
                route_source:
                  acl: route_src_acl
              security_group:
                source:
                  - 10
                  - 20
              local_preference:
                value:
                  - 55
                  - 105
              mpls_label: true
            set:
              aigp_metric:
                value: 100
              automatic_tag: true
              extcommunity:
                cost:
                  id: 10
                  cost_value: 100
                  pre_bestpath: true
              ip:
                address: 192.0.2.1
                df: 1
                next_hop:
                  recursive:
                    global_route: true
                    address: 198.51.110.1
                  verify_availability:
                    address: 198.51.111.1
                    sequence: 100
                    track: 10
                precedence:
                  critical: true
    state: merged

#  Commands Fired:
#  ---------------
#
#   "commands": [
#      "route-map test_2 deny 10",
#      "match security-group source tag 10 20",
#      "match local-preference 55 105",
#      "match mpls-label",
#      "match ipv6 next-hop prefix-list test_new",
#      "match ipv6 route-source route_src_acl",
#      "match ipv6 address test_ip_acl",
#      "set extcommunity cost pre-bestpath 10 100",
#      "set ip df 1",
#      "set ip next-hop recursive global 198.51.110.1",
#      "set ip next-hop verify-availability 198.51.111.1 100 track 10",
#      "set ip precedence critical",
#      "set ip address prefix-list 192.0.2.1",
#      "set automatic-tag",
#      "set aigp-metric 100",
#      "route-map test_1 deny 20",
#      "continue 100",
#      "match track 105",
#      "match tag list test_match_tag",
#      "match ipv6 address test_acl_20",
#      "match route-type level-1",
#      "match as-path 200 100",
#      "match additional-paths advertise-set all group-best",
#      "route-map test_1 deny 10",
#      "description this is test route",
#      "match security-group source tag 10 20",
#      "match ip next-hop prefix-list test_2_new test_1_new",
#      "match ip route-source 10",
#      "match local-preference 100 50",
#      "match mpls-label"
#     ]

# After state:
# -------------
#
# router-ios#sh running-config | section ^route-map
# route-map test_1 deny 10
#  description this is test route
#  match ip next-hop prefix-list test_2_new test_1_new
#  match ip route-source 10
#  match security-group source tag 10 20
#  match local-preference 100 50
#  match mpls-label
# route-map test_1 deny 20
#  match track  105
#  match tag list test_match_tag
#  match route-type level-1
#  match additional-paths advertise-set all group-best
#  match as-path 200 100
#  match ipv6 address test_acl_20
#  continue 100
# route-map test_2 deny 10
#  match security-group source tag 10 20
#  match local-preference 55 105
#  match mpls-label
#  match ipv6 address test_ip_acl
#  match ipv6 next-hop prefix-list test_new
#  match ipv6 route-source route_src_acl
#  set automatic-tag
#  set ip precedence critical
#  set ip address prefix-list 192.0.2.1
#  set aigp-metric 100
#  set extcommunity cost pre-bestpath 10 100
#  set ip df 1
#  set ip next-hop verify-availability 198.51.111.1 100 track 10
#  set ip next-hop recursive global 198.51.110.1

# Using overridden

# Before state:
# -------------
#
# router-ios#sh running-config | section ^route-map
# route-map test_1 deny 10
#  description this is test route
#  match ip next-hop prefix-list test_2_new test_1_new
#  match ip route-source 10
#  match security-group source tag 10 20
#  match local-preference 100 50
#  match mpls-label
# route-map test_1 deny 20
#  match track  105
#  match tag list test_match_tag
#  match route-type level-1
#  match additional-paths advertise-set all group-best
#  match as-path 200 100
#  match ipv6 address test_acl_20
#  continue 100
# route-map test_2 deny 10
#  match security-group source tag 10 20
#  match local-preference 55 105
#  match mpls-label
#  match ipv6 address test_ip_acl
#  match ipv6 next-hop prefix-list test_new
#  match ipv6 route-source route_src_acl
#  set automatic-tag
#  set ip precedence critical
#  set ip address prefix-list 192.0.2.1
#  set aigp-metric 100
#  set extcommunity cost pre-bestpath 10 100
#  set ip df 1
#  set ip next-hop verify-availability 198.51.111.1 100 track 10
#  set ip next-hop recursive global 198.51.110.1

- name: Override provided Route maps configuration
  cisco.ios.ios_route_maps:
    config:
      - route_map: test_1
        entries:
          - sequence: 10
            action: deny
            description: this is override route
            match:
              ip:
                next_hop:
                  acls:
                    - 10
                    - test1_acl
                flowspec:
                  dest_pfx: true
                  acls:
                    - test_acl_1
                    - test_acl_2
              length:
                minimum: 10
                maximum: 100
              metric:
                value: 10
                external: true
              security_group:
                source:
                  - 10
                  - 20
              mpls_label: true
            set:
              extcommunity:
                vpn_distinguisher:
                  address: 192.0.2.1:12
                  additive: true
              metric:
                metric_value: 100
                deviation: plus
                eigrp_delay: 100
                metric_reliability: 10
                metric_bandwidth: 20
                mtu: 30
      - route_map: test_override
        entries:
          - sequence: 10
            action: deny
            match:
              ipv6:
                address:
                  acl: test_acl
                next_hop:
                  prefix_list: test_new
                route_source:
                  acl: route_src_acl
              security_group:
                source:
                  - 15
                  - 20
              local_preference:
                value:
                  - 105
                  - 110
              mpls_label: true
            set:
              aigp_metric:
                value: 100
              automatic_tag: true
              extcommunity:
                cost:
                  id: 10
                  cost_value: 100
                  pre_bestpath: true
              ip:
                address: 192.0.2.1
                df: 1
                next_hop:
                  recursive:
                    global_route: true
                    address: 198.110.51.1
                  verify_availability:
                    address: 198.110.51.2
                    sequence: 100
                    track: 10
                precedence:
                  critical: true
    state: overridden

# Commands Fired:
# ---------------
#
#  "commands": [
#         "no route-map test_2",
#         "route-map test_override deny 10",
#         "match security-group source tag 15 20",
#         "match local-preference 110 105",
#         "match mpls-label",
#         "match ipv6 next-hop prefix-list test_new",
#         "match ipv6 route-source route_src_acl",
#         "match ipv6 address test_acl",
#         "set extcommunity cost pre-bestpath 10 100",
#         "set ip df 1",
#         "set ip next-hop recursive global 198.110.51.1",
#         "set ip next-hop verify-availability 198.110.51.2 100 track 10",
#         "set ip precedence critical",
#         "set ip address prefix-list 192.0.2.1",
#         "set automatic-tag",
#         "set aigp-metric 100",
#         "route-map test_1 deny 10",
#         "no description this is test route",
#         "description this is override route",
#         "match ip flowspec dest-pfx test_acl_1 test_acl_2",
#         "no match ip next-hop prefix-list test_2_new test_1_new",
#         "match ip next-hop test1_acl 10",
#         "no match ip route-source 10",
#         "match metric external 10",
#         "match length 10 100",
#         "no match local-preference 100 50",
#         "set extcommunity vpn-distinguisher 192.0.2.1:12 additive",
#         "set metric 100 +100 10 20 30",
#         "no route-map test_1 deny 20"
#     ]

# After state:
# -------------
#
# router-ios#sh running-config | section ^route-map
# route-map test_override deny 10
#  match security-group source tag 15 20
#  match local-preference 110 105
#  match mpls-label
#  match ipv6 address test_acl
#  match ipv6 next-hop prefix-list test_new
#  match ipv6 route-source route_src_acl
#  set automatic-tag
#  set ip precedence critical
#  set ip address prefix-list 192.0.2.1
#  set aigp-metric 100
#  set extcommunity cost pre-bestpath 10 100
#  set ip df 1
#  set ip next-hop verify-availability 198.110.51.2 100 track 10
#  set ip next-hop recursive global 198.110.51.1
# route-map test_1 deny 10
#  description this is override route
#  match ip flowspec dest-pfx test_acl_1 test_acl_2
#  match ip next-hop test1_acl 10
#  match security-group source tag 10 20
#  match metric external 10
#  match mpls-label
#  match length 10 100
#  set metric 100 +100 10 20 30
#  set extcommunity vpn-distinguisher 192.0.2.1:12 additive

# Using replaced

# Before state:
# -------------
#
# router-ios#sh running-config | section ^route-map
# route-map test_1 deny 10
#  description this is test route
#  match ip next-hop prefix-list test_2_new test_1_new
#  match ip route-source 10
#  match security-group source tag 10 20
#  match local-preference 100 50
#  match mpls-label
# route-map test_1 deny 20
#  match track  105
#  match tag list test_match_tag
#  match route-type level-1
#  match additional-paths advertise-set all group-best
#  match as-path 200 100
#  match ipv6 address test_acl_20
#  continue 100
# route-map test_2 deny 10
#  match security-group source tag 10 20
#  match local-preference 55 105
#  match mpls-label
#  match ipv6 address test_ip_acl
#  match ipv6 next-hop prefix-list test_new
#  match ipv6 route-source route_src_acl
#  set automatic-tag
#  set ip precedence critical
#  set ip address prefix-list 192.0.2.1
#  set aigp-metric 100
#  set extcommunity cost pre-bestpath 10 100
#  set ip df 1
#  set ip next-hop verify-availability 198.51.111.1 100 track 10
#  set ip next-hop recursive global 198.51.110.1

- name: Replaced provided Route maps configuration
  cisco.ios.ios_route_maps:
    config:
      - route_map: test_1
        entries:
          - sequence: 10
            action: deny
            description: this is replaced route
            match:
              ip:
                next_hop:
                  acls:
                    - 10
                    - test1_acl
                flowspec:
                  dest_pfx: true
                  acls:
                    - test_acl_1
                    - test_acl_2
              length:
                minimum: 10
                maximum: 100
              metric:
                value: 10
                external: true
              security_group:
                source:
                  - 10
                  - 20
              mpls_label: true
            set:
              extcommunity:
                vpn_distinguisher:
                  address: 192.0.2.1:12
                  additive: true
              metric:
                metric_value: 100
                deviation: plus
                eigrp_delay: 100
                metric_reliability: 10
                metric_bandwidth: 20
                mtu: 30
      - route_map: test_replaced
        entries:
          - sequence: 10
            action: deny
            match:
              ipv6:
                address:
                  acl: test_acl
                next_hop:
                  prefix_list: test_new
                route_source:
                  acl: route_src_acl
              security_group:
                source:
                  - 15
                  - 20
              local_preference:
                value:
                  - 105
                  - 110
              mpls_label: true
            set:
              aigp_metric:
                value: 100
              automatic_tag: true
              extcommunity:
                cost:
                  id: 10
                  cost_value: 100
                  pre_bestpath: true
              ip:
                address: 192.0.2.1
                df: 1
                next_hop:
                  recursive:
                    global_route: true
                    address: 198.110.51.1
                  verify_availability:
                    address: 198.110.51.2
                    sequence: 100
                    track: 10
                precedence:
                  critical: true
    state: replaced

# Commands Fired:
# ---------------
#  "commands": [
#         "route-map test_replaced deny 10",
#         "match security-group source tag 15 20",
#         "match local-preference 110 105",
#         "match mpls-label",
#         "match ipv6 next-hop prefix-list test_new",
#         "match ipv6 route-source route_src_acl",
#         "match ipv6 address test_acl",
#         "set extcommunity cost pre-bestpath 10 100",
#         "set ip df 1",
#         "set ip next-hop recursive global 198.110.51.1",
#         "set ip next-hop verify-availability 198.110.51.2 100 track 10",
#         "set ip precedence critical",
#         "set ip address prefix-list 192.0.2.1",
#         "set automatic-tag",
#         "set aigp-metric 100",
#         "route-map test_1 deny 10",
#         "no description this is test route",
#         "description this is replaced route",
#         "match ip flowspec dest-pfx test_acl_1 test_acl_2",
#         "no match ip next-hop prefix-list test_2_new test_1_new",
#         "match ip next-hop test1_acl 10",
#         "no match ip route-source 10",
#         "match metric external 10",
#         "match length 10 100",
#         "no match local-preference 100 50",
#         "set extcommunity vpn-distinguisher 192.0.2.1:12 additive",
#         "set metric 100 +100 10 20 30",
#         "no route-map test_1 deny 20"
#     ]

# After state:
# -------------
#
# router-ios#sh running-config | section ^route-map
# route-map test_replaced deny 10
#  match security-group source tag 15 20
#  match local-preference 110 105
#  match mpls-label
#  match ipv6 address test_acl
#  match ipv6 next-hop prefix-list test_new
#  match ipv6 route-source route_src_acl
#  set automatic-tag
#  set ip precedence critical
#  set ip address prefix-list 192.0.2.1
#  set aigp-metric 100
#  set extcommunity cost pre-bestpath 10 100
#  set ip df 1
#  set ip next-hop verify-availability 198.110.51.2 100 track 10
#  set ip next-hop recursive global 198.110.51.1
# route-map test_1 deny 10
#  description this is replaced route
#  match ip flowspec dest-pfx test_acl_1 test_acl_2
#  match ip next-hop test1_acl 10
#  match security-group source tag 10 20
#  match metric external 10
#  match mpls-label
#  match length 10 100
#  set metric 100 +100 10 20 30
#  set extcommunity vpn-distinguisher 192.0.2.1:12 additive
# route-map test_2 deny 10
#  match security-group source tag 10 20
#  match local-preference 55 105
#  match mpls-label
#  match ipv6 address test_ip_acl
#  match ipv6 next-hop prefix-list test_new
#  match ipv6 route-source route_src_acl
#  set automatic-tag
#  set ip precedence critical
#  set ip address prefix-list 192.0.2.1
#  set aigp-metric 100
#  set extcommunity cost pre-bestpath 10 100
#  set ip df 1
#  set ip next-hop verify-availability 198.51.111.1 100 track 10
#  set ip next-hop recursive global 198.51.110.1

# Using Gathered

# Before state:
# -------------
#
# router-ios#sh running-config | section ^route-map
# route-map test_1 deny 10
#  description this is test route
#  match ip next-hop prefix-list test_2_new test_1_new
#  match ip route-source 10
#  match security-group source tag 10 20
#  match local-preference 100 50
#  match mpls-label
# route-map test_1 deny 20
#  match track  105
#  match tag list test_match_tag
#  match route-type level-1
#  match additional-paths advertise-set all group-best
#  match as-path 200 100
#  match ipv6 address test_acl_20
#  continue 100
# route-map test_2 deny 10
#  match security-group source tag 10 20
#  match local-preference 55 105
#  match mpls-label
#  match ipv6 address test_ip_acl
#  match ipv6 next-hop prefix-list test_new
#  match ipv6 route-source route_src_acl
#  set automatic-tag
#  set ip precedence critical
#  set ip address prefix-list 192.0.2.1
#  set aigp-metric 100
#  set extcommunity cost pre-bestpath 10 100
#  set ip df 1
#  set ip next-hop verify-availability 198.51.111.1 100 track 10
#  set ip next-hop recursive global 198.51.110.1

- name: Gather Route maps provided configurations
  cisco.ios.ios_route_maps:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": [
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "description": "this is test route",
#                     "match": {
#                         "ip": {
#                             "next_hop": {
#                                 "prefix_lists": [
#                                     "test_2_new",
#                                     "test_1_new"
#                                 ]
#                             },
#                             "route_source": {
#                                 "acls": [
#                                     "10"
#                                 ]
#                             }
#                         },
#                         "local_preference": {
#                             "value": [
#                                 "100",
#                                 "50"
#                             ]
#                         },
#                         "mpls_label": true,
#                         "security_group": {
#                             "source": [
#                                 10,
#                                 20
#                             ]
#                         }
#                     },
#                     "sequence": 10
#                 },
#                 {
#                     "action": "deny",
#                     "continue_entry": {
#                         "entry_sequence": 100
#                     },
#                     "match": {
#                         "additional_paths": {
#                             "all": true,
#                             "group_best": true
#                         },
#                         "as_path": {
#                             "acls": [
#                                 200,
#                                 100
#                             ]
#                         },
#                         "ipv6": {
#                             "address": {
#                                 "acl": "test_acl_20"
#                             }
#                         },
#                         "route_type": {
#                             "external": {
#                                 "set": true
#                             },
#                             "level_1": true,
#                             "nssa_external": {
#                                 "set": true
#                             }
#                         },
#                         "tag": {
#                             "tag_list": [
#                                 "test_match_tag"
#                             ]
#                         },
#                         "track": 105
#                     },
#                     "sequence": 20
#                 }
#             ],
#             "route_map": "test_1"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "match": {
#                         "ipv6": {
#                             "address": {
#                                 "acl": "test_ip_acl"
#                             },
#                             "next_hop": {
#                                 "prefix_list": "test_new"
#                             },
#                             "route_source": {
#                                 "acl": "route_src_acl"
#                             }
#                         },
#                         "local_preference": {
#                             "value": [
#                                 "55",
#                                 "105"
#                             ]
#                         },
#                         "mpls_label": true,
#                         "security_group": {
#                             "source": [
#                                 10,
#                                 20
#                             ]
#                         }
#                     },
#                     "sequence": 10,
#                     "set": {
#                         "aigp_metric": {
#                             "value": 100
#                         },
#                         "automatic_tag": true,
#                         "extcommunity": {
#                             "cost": {
#                                 "cost_value": 100,
#                                 "id": "10",
#                                 "pre_bestpath": true
#                             }
#                         },
#                         "ip": {
#                             "address": "192.0.2.1",
#                             "df": 1,
#                             "next_hop": {
#                                 "recursive": {
#                                     "address": "198.51.110.1",
#                                     "global_route": true
#                                 },
#                                 "verify_availability": {
#                                     "address": "198.51.111.1",
#                                     "sequence": 100,
#                                     "track": 10
#                                 }
#                             },
#                             "precedence": {
#                                 "critical": true
#                             }
#                         }
#                     }
#                 }
#             ],
#             "route_map": "test_2"
#         }
#     ]

# After state:
# ------------
#
# router-ios#sh running-config | section ^route-map
# route-map test_1 deny 10
#  description this is test route
#  match ip next-hop prefix-list test_2_new test_1_new
#  match ip route-source 10
#  match security-group source tag 10 20
#  match local-preference 100 50
#  match mpls-label
# route-map test_1 deny 20
#  match track  105
#  match tag list test_match_tag
#  match route-type level-1
#  match additional-paths advertise-set all group-best
#  match as-path 200 100
#  match ipv6 address test_acl_20
#  continue 100
# route-map test_2 deny 10
#  match security-group source tag 10 20
#  match local-preference 55 105
#  match mpls-label
#  match ipv6 address test_ip_acl
#  match ipv6 next-hop prefix-list test_new
#  match ipv6 route-source route_src_acl
#  set automatic-tag
#  set ip precedence critical
#  set ip address prefix-list 192.0.2.1
#  set aigp-metric 100
#  set extcommunity cost pre-bestpath 10 100
#  set ip df 1
#  set ip next-hop verify-availability 198.51.111.1 100 track 10
#  set ip next-hop recursive global 198.51.110.1

# Using Rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_route_maps:
    config:
      - route_map: test_1
        entries:
          - sequence: 10
            action: deny
            description: this is test route
            match:
              ip:
                next_hop:
                  prefix_lists:
                    - test_1_new
                    - test_2_new
                route_source:
                  acls:
                    - 10
              security_group:
                source:
                  - 10
                  - 20
              local_preference:
                value:
                  - 50
                  - 100
              mpls_label: true
          - sequence: 20
            action: deny
            continue_entry:
              entry_sequence: 100
            match:
              additional_paths:
                all: true
                group_best: true
              as_path:
                acls:
                  - 100
                  - 200
              ipv6:
                address:
                  acl: test_acl_20
              route_type:
                level_1: true
              tag:
                tag_list:
                  - test_match_tag
              track: 105
      - route_map: test_2
        entries:
          - sequence: 10
            action: deny
            match:
              ipv6:
                address:
                  acl: test_ip_acl
                next_hop:
                  prefix_list: test_new
                route_source:
                  acl: route_src_acl
              security_group:
                source:
                  - 10
                  - 20
              local_preference:
                value:
                  - 55
                  - 105
              mpls_label: true
            set:
              aigp_metric:
                value: 100
              automatic_tag: true
              extcommunity:
                cost:
                  id: 10
                  cost_value: 100
                  pre_bestpath: true
              ip:
                address: 192.0.2.1
                df: 1
                next_hop:
                  recursive:
                    global_route: true
                    address: 198.51.110.1
                  verify_availability:
                    address: 198.51.111.1
                    sequence: 100
                    track: 10
                precedence:
                  critical: true
    state: rendered

# Module Execution Result:
# ------------------------
#
#  "rendered": [
#      "route-map test_2 deny 10",
#      "match security-group source tag 10 20",
#      "match local-preference 55 105",
#      "match mpls-label",
#      "match ipv6 next-hop prefix-list test_new",
#      "match ipv6 route-source route_src_acl",
#      "match ipv6 address test_ip_acl",
#      "set extcommunity cost pre-bestpath 10 100",
#      "set ip df 1",
#      "set ip next-hop recursive global 198.51.110.1",
#      "set ip next-hop verify-availability 198.51.111.1 100 track 10",
#      "set ip precedence critical",
#      "set ip address prefix-list 192.0.2.1",
#      "set automatic-tag",
#      "set aigp-metric 100",
#      "route-map test_1 deny 20",
#      "continue 100",
#      "match track 105",
#      "match tag list test_match_tag",
#      "match ipv6 address test_acl_20",
#      "match route-type level-1",
#      "match as-path 200 100",
#      "match additional-paths advertise-set all group-best",
#      "route-map test_1 deny 10",
#      "description this is test route",
#      "match security-group source tag 10 20",
#      "match ip next-hop prefix-list test_2_new test_1_new",
#      "match ip route-source 10",
#      "match local-preference 100 50",
#      "match mpls-label"
#     ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# route-map test_1 deny 10
#  description this is test route
#  match ip next-hop prefix-list test_2_new test_1_new
#  match ip route-source 10
#  match security-group source tag 10 20
#  match local-preference 100 50
#  match mpls-label
# route-map test_1 deny 20
#  match track  105
#  match tag list test_match_tag
#  match route-type level-1
#  match additional-paths advertise-set all group-best
#  match as-path 200 100
#  match ipv6 address test_acl_20
#  continue 100
# route-map test_2 deny 10
#  match security-group source tag 10 20
#  match local-preference 55 105
#  match mpls-label
#  match ipv6 address test_ip_acl
#  match ipv6 next-hop prefix-list test_new
#  match ipv6 route-source route_src_acl
#  set automatic-tag
#  set ip precedence critical
#  set ip address prefix-list 192.0.2.1
#  set aigp-metric 100
#  set extcommunity cost pre-bestpath 10 100
#  set ip df 1
#  set ip next-hop verify-availability 198.51.111.1 100 track 10
#  set ip next-hop recursive global 198.51.110.1

- name: Parse the provided configuration with the existing running configuration
  cisco.ios.ios_route_maps:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "description": "this is test route",
#                     "match": {
#                         "ip": {
#                             "next_hop": {
#                                 "prefix_lists": [
#                                     "test_2_new",
#                                     "test_1_new"
#                                 ]
#                             },
#                             "route_source": {
#                                 "acls": [
#                                     "10"
#                                 ]
#                             }
#                         },
#                         "local_preference": {
#                             "value": [
#                                 "100",
#                                 "50"
#                             ]
#                         },
#                         "mpls_label": true,
#                         "security_group": {
#                             "source": [
#                                 10,
#                                 20
#                             ]
#                         }
#                     },
#                     "sequence": 10
#                 },
#                 {
#                     "action": "deny",
#                     "continue_entry": {
#                         "entry_sequence": 100
#                     },
#                     "match": {
#                         "additional_paths": {
#                             "all": true,
#                             "group_best": true
#                         },
#                         "as_path": {
#                             "acls": [
#                                 200,
#                                 100
#                             ]
#                         },
#                         "ipv6": {
#                             "address": {
#                                 "acl": "test_acl_20"
#                             }
#                         },
#                         "route_type": {
#                             "external": {
#                                 "set": true
#                             },
#                             "level_1": true,
#                             "nssa_external": {
#                                 "set": true
#                             }
#                         },
#                         "tag": {
#                             "tag_list": [
#                                 "test_match_tag"
#                             ]
#                         },
#                         "track": 105
#                     },
#                     "sequence": 20
#                 }
#             ],
#             "route_map": "test_1"
#         },
#         {
#             "entries": [
#                 {
#                     "action": "deny",
#                     "match": {
#                         "ipv6": {
#                             "address": {
#                                 "acl": "test_ip_acl"
#                             },
#                             "next_hop": {
#                                 "prefix_list": "test_new"
#                             },
#                             "route_source": {
#                                 "acl": "route_src_acl"
#                             }
#                         },
#                         "local_preference": {
#                             "value": [
#                                 "55",
#                                 "105"
#                             ]
#                         },
#                         "mpls_label": true,
#                         "security_group": {
#                             "source": [
#                                 10,
#                                 20
#                             ]
#                         }
#                     },
#                     "sequence": 10,
#                     "set": {
#                         "aigp_metric": {
#                             "value": 100
#                         },
#                         "automatic_tag": true,
#                         "extcommunity": {
#                             "cost": {
#                                 "cost_value": 100,
#                                 "id": "10",
#                                 "pre_bestpath": true
#                             }
#                         },
#                         "ip": {
#                             "address": "192.0.2.1",
#                             "df": 1,
#                             "next_hop": {
#                                 "recursive": {
#                                     "address": "198.51.110.1",
#                                     "global_route": true
#                                 },
#                                 "verify_availability": {
#                                     "address": "198.51.111.1",
#                                     "sequence": 100,
#                                     "track": 10
#                                 }
#                             },
#                             "precedence": {
#                                 "critical": true
#                             }
#                         }
#                     }
#                 }
#             ],
#             "route_map": "test_2"
#         }
#     ]
```

## [Return Values](ios_route_maps_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["route-map test_1 deny 10", "description this is test route", "match ip route-source 10", "match track  105"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
