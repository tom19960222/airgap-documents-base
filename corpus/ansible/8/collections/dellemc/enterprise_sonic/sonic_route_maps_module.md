---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_route_maps module – route map configuration handling for SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_route_maps_module.html
fetched_at: 2026-07-28T02:03:48+00:00
---
# dellemc.enterprise_sonic.sonic_route_maps module – route map configuration handling for SONiC

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_route_maps`.

New in dellemc.enterprise_sonic 2.1.0

- [Synopsis](sonic_route_maps_module.md#synopsis)
- [Parameters](sonic_route_maps_module.md#parameters)
- [Examples](sonic_route_maps_module.md#examples)
- [Return Values](sonic_route_maps_module.md#return-values)

## [Synopsis](sonic_route_maps_module.md#id1)

- This module provides configuration management for route map parameters on devices running SONiC.

## [Parameters](sonic_route_maps_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies a list of route map configuration dictionaries |
| **action**  string | action type for the route map (permit or deny)  This value is required for creation and modification of a route  map or route map attributes as well as for deletion of route map  attributes. It can be omitted only when requesting deletion of a  route map statement or all route map statements for a given route  map map_name.  **Choices:**   - `"permit"` - `"deny"` |
| **call**  string | Name of a route map to jump to after executing ‘match’ and ‘set’  statements for the current route map. |
| **map_name**  string / required | Name of a route map |
| **match**  dictionary | Criteria for matching the route map to a route |
| **as_path**  string | Name of a configured BGP AS path list to be checked for  a match with the target route |
| **community**  string | Name of a configured BGP “community” to be checked for  a match with the target route |
| **evpn**  dictionary | BGP Ethernet Virtual Private Network to be checked for  a match with the target route |
| **default_route**  boolean | Default EVPN type-5 route  **Choices:**   - `false` - `true` |
| **route_type**  string | Non-default route type: One of the following:  mac-ip route, EVPN Type 3 Inclusive Multicast Ethernet  Tag (IMET) route, or prefix route  **Choices:**   - `"macip"` - `"multicast"` - `"prefix"` |
| **vni**  integer | VNI ID to be checked for a match; specified by a value in the  range 1-16777215 |
| **ext_comm**  string | Name of a configured BGP ‘extended community’ to be checked for  a match with the target route |
| **interface**  string | Next hop interface name (type and number) to be checked for a  match with the target route. The interface type can be any  of the following; ‘Ethernet/Eth’ interface or sub-interface,  ‘Loopback’ interface, ‘PortChannel’ interface or  sub-interface, ‘Vlan’ interface. |
| **ip**  dictionary | IP addresses or IP next hops to be checked for a match with the  target route |
| **address**  string | name of an IPv4 prefix list containing a list of address  prefixes to be checked for a match with the target route |
| **next_hop**  string | name of a prefix list containing a list of next-hop  prefixes to be checked for a match with the target route |
| **ipv6**  dictionary | IPv6 addresses to be checked for a match with the  target route |
| **address**  string / required | name of an IPv6 prefix list containing a list of address  prefixes to be checked for a match with the target route |
| **local_preference**  integer | local-preference value to be checked for a match with the  target route. This is a value in the range 0-4294967295. |
| **metric**  integer | metric value to be checked for a match with the target route.  This is a value in the range 0-4294967295. |
| **origin**  string | BGP origin to be checked for a match with the target route  **Choices:**   - `"egp"` - `"igp"` - `"incomplete"` |
| **peer**  dictionary | BGP routing peer/neighbor required for a matching route.  *ip*, *ipv6*, and *interface* are mutually exclusive. |
| **interface**  string | Name (type and number) of a BGP peer interface.  Allowed interface types are Ethernet or Eth (depending  on the configured interface-naming mode),  Vlan, and Portchannel |
| **ip**  string | IPv4 address of a BGP peer |
| **ipv6**  string | IPv6 address of a BGP peer |
| **source_protocol**  string | Source protocol required for a matching route  **Choices:**   - `"bgp"` - `"connected"` - `"ospf"` - `"static"` |
| **source_vrf**  string | Name of the source VRF required for a matching route |
| **tag**  integer | Tag value required for a matching route  The value must be in the range 1-4294967295 |
| **sequence_num**  integer | unique number in the range 1-66535 to specify priority of the map  This value is required for creation and modification of a route  map or route map attributes as well as for deletion of route map  attributes. It can be omitted only when requesting deletion of all  route map “statements” for a given route map “map_name”. |
| **set**  dictionary | Information to set into a matching route for re-distribution |
| **as_path_prepend**  string | String specifying a comma-separated list of AS-path numbers  to prepend to the BGP AS-path attribute in a matched route.  AS-path values in the list must be in the range  1-4294967295; for example, 2000,3000 |
| **comm_list_delete**  string | String specifying the name of a BGP community list containing  BGP Community values to be deleted from matching routes. |
| **community**  dictionary | BGP community attributes to add to or replace the BGP  community attributes in a matching route. Specifying the  ‘additive’ attribute is allowed only if one of  the other attributes (other than ‘none’) is specified.  It causes the specified ‘set community’ attributes  to be added to the already existing community  attributes in the matching route. If the ‘additive’ attribute  is not specified, the previously existing community attributes  in the matching route are replaced by the configured  ‘set community’ attributes. Specifying a ‘set community’ attribute  of ‘none’ is mutually exclusive with setting of other community  attributes and causes any community attributes in the matching  route to be removed. |
| **community_attributes**  list / elements=string | A list of one or more BGP community attributes. The allowed  values are the following:  local_as  Do not send outside local AS (well-known community)  no_advertise  Do not advertise to any peer (well-known community)  no_export  Do not export to next AS (well-known community)  no_peer  The route does not need to be advertised to peers.  (Advertisement of the route can be suppressed based  on other criteria.)  additive  Add the configured ‘set community’ attributes to  the matching route (if set to ‘true’); Previously existing  attributes in the matching route are, instead, replaced  by the configured attributes if this attribute is  not specified or if it is set to ‘false’.  none  Do not send any community attribute. This attribute  is mutually exclusive with all other ‘set community’  attributes. It causes all attributes to be removed  from the matching route.  *none* is mutually exclusive with all of the other attributes:  *local_as*, *no_advertise*, *no_export*, *no_peer*, *additive*,  and *additive*.  **Choices:**   - `"local_as"` - `"no_advertise"` - `"no_export"` - `"no_peer"` - `"additive"` - `"none"` |
| **community_number**  list / elements=string | A list of one or more BGP community numbers in the  form AA:NN where AA and NN are integers in the range  0-65535.  Note: Each community number in the list must be enclosed  in double quotes to avoid YAML parsing errors due to the  list values containing an embedded ‘:’ character. |
| **extcommunity**  dictionary | BGP extended community attributes to set into a matching route. |
| **rt**  list / elements=string | Route Target VPN extended communities in the format  ASN:NN or IP-ADDRESS:NN  Note: Each rt value in the list must be enclosed  in double quotes to avoid YAML parsing errors due to the  list values containing an embedded ‘:’ character. |
| **soo**  list / elements=string | Site-of-Origin VPN extended communities in the format  ASN:NN or IP-ADDRESS:NN  Note: Each rt value in the list must be enclosed  in double quotes to avoid YAML parsing errors due to the  list values containing an embedded ‘:’ character. |
| **ip_next_hop**  string | IPv4 next hop address to set into a matching route in the  dotted decimal format A.B.C.D |
| **ipv6_next_hop**  dictionary | IPv6 next hop address attributes to set into a matching route |
| **global_addr**  string | IPv6 global next hop address to set into a matching  route in the format A::B |
| **prefer_global**  boolean | Set the corresponding attribute into a matching route  if the value of this Ansible attribute is ‘true’.  The attribute indicates that the routing algorithm must  prefer the global next-hop address over the link-local  address if both exist.  **Choices:**   - `false` - `true` |
| **local_preference**  integer | BGP local preference path attribute; integer value in  the range 0-4294967295 |
| **metric**  dictionary | route metric value actions  *value* and *rtt_action* are mutually exclusive. |
| **rtt_action**  string | Action to take for modifying the metric for a matched  route using the Round Trip Time (rtt);  `set` causes the route metric to be set to the  rtt value.  `add` causes the rtt value to be added  to the route metric.  `subtract` causes the rtt value to be  subtracted from route metric.  **Choices:**   - `"set"` - `"add"` - `"subtract"` |
| **value**  integer | metric value to be set into a matching route;  value in the range 0-4294967295 |
| **origin**  string | BGP route origin; One of the following must be selected.  egp (External; remote EGP)  igp (Internal; local IGP)  incomplete (Unknown origin)  **Choices:**   - `"egp"` - `"igp"` - `"incomplete"` |
| **weight**  integer | BGP weight for the routing table. The weight must be an  integer in the range 0-4294967295 |
| **state**  string | Specifies the type of configuration update to be performed on the device.  For `merged`, merge specified attributes with existing configured attributes.  For `deleted`, delete the specified attributes from existing configuration.  For `replaced`, replace each modified list or dictionary with the  specified items.  For `overridden`, replace all current configuration for this resource  module with the specified configuration.  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"replaced"` - `"overridden"` |

## [Examples](sonic_route_maps_module.md#id3)

```yaml+jinja
# Using "merged" state to create initial configuration
#
# Before state:
# -------------
#
# sonic# show running-configuration route-map
# sonic#
# (No configuration present)
#
# -------------
#
- name: Merge initial route_maps configuration
  dellemc.enterprise_sonic.sonic_route_maps:
     config:
       - map_name: rm1
         action: permit
         sequence_num: 80
         match:
           as_path: bgp_as1
           community: bgp_comm_list1
           evpn:
             default_route: true
             vni: 735
           ext_comm: bgp_ext_comm1
           interface: Ethernet4
           ip:
             address: ip_pfx_list1
           ipv6:
             address: ipv6_pfx_list1
           local_preference: 8000
           metric: 400
           origin: egp
           peer:
             ip: 10.20.30.40
           source_protocol: bgp
           source_vrf: Vrf1
           tag: 7284
         set:
           as_path_prepend: 200,315,7135
           comm_list_delete: bgp_comm_list2
           community:
             community_number:
               - "35:58"
               - "79:150"
               - "308:650"
             community_attributes:
               - local_as
               - no_advertise
               - no_export
               - no_peer
               - additive
           extcommunity:
             rt:
               - "30:40"
             soo:
               - "10.73.14.9:78"
           ip_next_hop: 10.48.16.18
           ipv6_next_hop:
             global_addr: 30::30
             prefer_global: true
           local_preference: 635
           metric:
             metric_value: 870
           origin: egp
           weight: 93471
       - map_name: rm1
         action: deny
         sequence_num: 3047
         match:
           evpn:
             route_type: multicast
           origin: incomplete
           peer:
             interface: Ethernet6
           source_protocol: ospf
         set:
           metric:
             rtt_action: add
           origin: incomplete
       - map_name: rm3
         action: deny
         sequence_num: 285
         match:
           evpn:
             route_type: macip
           origin: igp
           peer:
             ipv6: 87:95:15::53
           source_protocol: connected
         set:
           community:
             community_attributes:
               - none
           metric:
             rtt_action: set
           origin: igp
         call: rm1
       - map_name: rm4
         action: permit
         sequence_num: 480
         match:
           evpn:
             route_type: prefix
           source_protocol: static
         set:
           metric:
             rtt_action: subtract
     state: merged

# After state:
# ------------
#
# sonic# show running-configuration route-map
# !
# route-map rm1 permit 80
#  match as-path bgp_as1
#  match evpn default-route
#  match evpn vni 735
#  match ip address prefix-list ip_pfx_list1
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Ethernet4
#  match community bgp_comm_list1
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match peer 10.20.30.40
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set as-path prepend 200,315,7135
#  set community 35:58 79:150 308:650 local-AS no-advertise no-export no-peer additive
#  set extcommunity rt 30:40
#  set extcommunity soo 10.73.14.9:78
#  set comm-list bgp_comm_list2 delete
#  set metric 870
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set ipv6 next-hop prefer-global
#  set local-preference 635
#  set origin egp
#  set weight 93471
# !
# route-map rm1 deny 3047
#  match evpn route-type multicast
#  match peer Ethernet6
#  match source-protocol ospf
#  match origin incomplete
#  set metric +rtt
#  set origin incomplete
# !
# route-map rm3 deny 285
#  match evpn route-type macip
#  call rm1
#  match peer 87:95:15::53
#  match source-protocol connected
#  match origin igp
#  set community none
#  set metric rtt
#  set origin igp
# !
# route-map rm4 permit 480
#  match evpn route-type prefix
#  match source-protocol static
#  set metric -rtt
# ------------

# Using "merged" state to update and add configuration
#
# Before state:
# ------------
#
# sonic# show running-configuration route-map
# !
# route-map rm1 permit 80
#  match as-path bgp_as1
#  match evpn default-route
#  match evpn vni 735
#  match ip address prefix-list ip_pfx_list1
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Ethernet4
#  match community bgp_comm_list1
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match peer 10.20.30.40
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set as-path prepend 200,315,7135
#  set community 35:58 79:150 308:650 local-AS no-advertise no-export no-peer additive
#  set extcommunity rt 30:40
#  set extcommunity soo 10.73.14.9:78
#  set comm-list bgp_comm_list2 delete
#  set metric 870
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set ipv6 next-hop prefer-global
#  set local-preference 635
#  set origin egp
#  set weight 93471
# !
# route-map rm1 deny 3047
#  match evpn route-type multicast
#  match peer Ethernet6
#  match source-protocol ospf
#  match origin incomplete
#  set metric +rtt
#  set origin incomplete
# !
# route-map rm3 deny 285
#  match evpn route-type macip
#  call rm1
#  match peer 87:95:15::53
#  match source-protocol connected
#  match origin igp
#  set community none
#  set metric rtt
#  set origin igp
# !
# route-map rm4 permit 480
#  match evpn route-type prefix
#  match source-protocol static
#  set metric -rtt
# ------------
#
- name: Merge additional and modified route map configuration
  dellemc.enterprise_sonic.sonic_route_maps:
     config:
       - map_name: rm1
         action: permit
         sequence_num: 80
         match:
           as_path: bgp_as2
           community: bgp_comm_list3
           evpn:
             route_type: prefix
             vni: 850
           interface: Vlan7
           ip:
             address: ip_pfx_list2
             next_hop: ip_pfx_list3
           peer:
             interface: Portchannel14
         set:
           as_path_prepend: 188,257
           community:
             community_number:
               - "45:736"
           ipv6_next_hop:
             prefer_global: false
           metric:
             rtt_action: add
       - map_name: rm1
         action: deny
         sequence_num: 3047
         match:
           as_path: bgp_as3
           ext_comm: bgp_ext_comm2
           origin: igp
         set:
           metric:
             rtt_action: subtract
       - map_name: rm2
         action: permit
         sequence_num: 100
         match:
           interface: Ethernet16
         set:
           as_path_prepend: 200,300,400
           ipv6_next_hop:
             global_addr: 37::58
             prefer_global: true
           metric: 8000
       - map_name: rm3
         action: deny
         sequence_num: 285
         match:
           local_preference: 14783
           source_protocol: bgp
         set:
           community:
             community_attributes:
               - no_advertise
     state: merged

# After state:
# ------------
#
# sonic# show running-configuration route-map
# !
# route-map rm1 permit 80
#  match as-path bgp_as2
#  match evpn default-route
#  match evpn route-type prefix
#  match evpn vni 850
#  match ip address prefix-list ip_pfx_list2
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Vlan7
#  match community bgp_comm_list3
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match ip next-hop prefix-list ip_pfx_list3
#  match peer PortChannel 14
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set as-path prepend 188,257
#  set community 35:58 79:150 308:650 45:736 local-AS no-advertise no-export no-peer additive
#  set extcommunity rt 30:40
#  set extcommunity soo 10.73.14.9:78
#  set comm-list bgp_comm_list2 delete
#  set metric +rtt
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set local-preference 635
#  set origin egp
#  set weight 93471
# !
# route-map rm1 deny 3047
#  match as-path bgp_as3
#  match evpn route-type multicast
#  match ext-community bgp_ext_comm2
#  match peer Ethernet6
#  match source-protocol ospf
#  match origin igp
#  set metric -rtt
#  set origin incomplete
# !
# route-map rm2 permit 100
#  match interface Ethernet16
#  set as-path prepend 200,300,400
#  set ipv6 next-hop global 37::58
#  set ipv6 next-hop prefer-global
#  set metric 8000
# !
# route-map rm3 deny 285
#  match evpn route-type macip
#  match local-preference 14783
#  call rm1
#  match peer 87:95:15::53
#  match source-protocol bgp
#  match origin igp
#  set community no-advertise
#  set metric rtt
#  set origin igp
# !
# route-map rm4 permit 480
#  match evpn route-type prefix
#  match source-protocol static
#  set metric -rtt

# Using "replaced" state to replace the contents of a list
#
# Before state:
# ------------
#
# sonic(config-route-map)# do show running-configuration route-map rm1 80
# !
# route-map rm1 permit 80
#  match as-path bgp_as2
#  match evpn default-route
#  match evpn route-type prefix
#  match evpn vni 850
#  match ip address prefix-list ip_pfx_list2
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Vlan7
#  match community bgp_comm_list3
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match ip next-hop prefix-list ip_pfx_list3
#  match peer PortChannel 14
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set as-path prepend 188,257
#  set community 35:58 79:150 308:650 45:736 local-AS no-export no-peer additive
#  set extcommunity rt 30:40
#  set extcommunity soo 10.73.14.9:78
#  set comm-list bgp_comm_list2 delete
#  set metric +rtt
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set local-preference 635
#  set origin egp
#  set weight 93471
# ------------
- name: Replace a list
  dellemc.enterprise_sonic.sonic_route_maps:
     config:
       - map_name: rm1
         action: permit
         sequence_num: 80
         set:
           community:
             community_number:
               - "15:30"
               - "26:54"
     state: replaced

# After state:
# ------------
#
# sonic#show running-configuration route-map rm1 80
# !
# route-map rm1 permit 80
#  match as-path bgp_as2
#  match evpn default-route
#  match evpn route-type prefix
#  match evpn vni 850
#  match ip address prefix-list ip_pfx_list2
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Vlan7
#  match community bgp_comm_list3
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match ip next-hop prefix-list ip_pfx_list3
#  match peer PortChannel 14
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set as-path prepend 188,257
#  set community 15:30 26:54 local-AS no-export no-peer additive
#  set extcommunity rt 30:40
#  set extcommunity soo 10.73.14.9:78
#  set comm-list bgp_comm_list2 delete
#  set metric +rtt
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set local-preference 635
#  set origin egp
#  set weight 93471

# Using "replaced" state to replace the contents of dictionaries
#
# Before state:
# ------------
# sonic# show running-configuration route-map
# !
# route-map rm1 permit 80
#  match as-path bgp_as2
#  match evpn default-route
#  match evpn route-type prefix
#  match evpn vni 850
#  match ip address prefix-list ip_pfx_list2
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Vlan7
#  match community bgp_comm_list3
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match ip next-hop prefix-list ip_pfx_list3
#  match peer PortChannel 14
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set as-path prepend 188,257
#  set community 15:30 26:54 local-AS no-export no-peer additive
#  set extcommunity rt 30:40
#  set extcommunity soo 10.73.14.9:78
#  set comm-list bgp_comm_list2 delete
#  set metric +rtt
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set local-preference 635
#  set origin egp
#  set weight 93471
# !
# route-map rm1 deny 3047
#  match as-path bgp_as3
#  match evpn route-type multicast
#  match ext-community bgp_ext_comm2
#  match peer Ethernet6
#  match source-protocol ospf
#  match origin igp
#  set metric -rtt
#  set origin incomplete
# !
# route-map rm2 permit 100
#  match interface Ethernet16
#  set as-path prepend 200,300,400
#  set ipv6 next-hop global 37::58
#  set ipv6 next-hop prefer-global
#  set metric 8000
# !
# route-map rm3 deny 285
#  match evpn route-type macip
#  match local-preference 14783
#  call rm1
#  match peer 87:95:15::53
#  match source-protocol bgp
#  match origin igp
#  set community no-advertise
#  set metric rtt
#  set origin igp
# !
# route-map rm4 permit 480
#  match evpn route-type prefix
#  match source-protocol static
#  set metric -rtt
# ------------
- name: Replace dictionaries
  dellemc.enterprise_sonic.sonic_route_maps:
     config:
       - map_name: rm1
         action: permit
         sequence_num: 80
         match:
           evpn:
             route_type: multicast
           ip:
             address: ip_pfx_list1
         set:
           community:
             community_attributes:
               - no_advertise
           extcommunity:
             rt:
               - "20:20"

       - map_name: rm2
         action: permit
         sequence_num: 100
         set:
           ipv6_next_hop:
             global_addr: 45::90
     state: replaced

# After state:
# ------------
#
# sonic# show running-configuration route-map
# !
# route-map rm1 permit 80
#  match as-path bgp_as2
#  match evpn route-type multicast
#  match ip address prefix-list ip_pfx_list1
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Vlan7
#  match community bgp_comm_list3
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match peer PortChannel 14
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set as-path prepend 188,257
#  set community no-advertise
#  set extcommunity rt 20:20
#  set comm-list bgp_comm_list2 delete
#  set metric +rtt
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set local-preference 635
#  set origin egp
#  set weight 93471
# !
# route-map rm1 deny 3047
#  match as-path bgp_as3
#  match evpn route-type multicast
#  match ext-community bgp_ext_comm2
#  match peer Ethernet6
#  match source-protocol ospf
#  match origin igp
#  set metric -rtt
#  set origin incomplete
# !
# route-map rm2 permit 100
#  match interface Ethernet16
#  set as-path prepend 200,300,400
#  set metric 8000
#  set ipv6 next-hop global 45::90
# !
# route-map rm3 deny 285
#  match evpn route-type macip
#  match local-preference 14783
#  call rm1
#  match peer 87:95:15::53
#  match source-protocol bgp
#  match origin igp
#  set community no-advertise
#  set metric rtt
#  set origin igp
# !
# route-map rm4 permit 480
#  match evpn route-type prefix
#  match source-protocol static
#  set metric -rtt

# Using "overridden" state to override all existing configuration with new
# configuration
#
# Before state:
# ------------
#
# sonic# show running-configuration route-map
# !
# route-map rm1 permit 80
#  match as-path bgp_as2
#  match evpn route-type multicast
#  match ip address prefix-list ip_pfx_list1
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Vlan7
#  match community bgp_comm_list3
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match peer PortChannel 14
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set as-path prepend 188,257
#  set community no-advertise
#  set extcommunity rt 30:40
#  set extcommunity rt 20:20
#  set comm-list bgp_comm_list2 delete
#  set metric +rtt
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set local-preference 635
#  set origin egp
#  set weight 93471
# !
# route-map rm1 deny 3047
#  match as-path bgp_as3
#  match evpn route-type multicast
#  match ext-community bgp_ext_comm2
#  match peer Ethernet6
#  match source-protocol ospf
#  match origin igp
#  set metric -rtt
#  set origin incomplete
# !
# route-map rm2 permit 100
#  match interface Ethernet16
#  set as-path prepend 200,300,400
#  set metric 8000
#  set ipv6 next-hop global 45::90
# !
# route-map rm3 deny 285
#  match evpn route-type macip
#  match local-preference 14783
#  call rm1
#  match peer 87:95:15::53
#  match source-protocol bgp
#  match origin igp
#  set community no-advertise
#  set metric rtt
#  set origin igp
# !
# route-map rm4 permit 480
#  match evpn route-type prefix
#  match source-protocol static
#  set metric -rtt
# ------------
- name: Override all route map configuration with new configuration
  dellemc.enterprise_sonic.sonic_route_maps:
     config:
       - map_name: rm5
         action: permit
         sequence_num: 250
         match:
           interface: Ethernet28
         set:
           as_path_prepend: 150,275
           metric: 7249
     state: overridden

# After state:
# ------------
#
# sonic# show running-configuration route-map
# !
# route-map rm5 permit 250
#  match interface Ethernet28
#  set as-path prepend 150,275
#  set metric 7249

# Using "overridden" state to override all existing configuration with new
# configuration. (Restore previous configuration.)
#
# Before state:
# ------------
#
# sonic# show running-configuration route-map
# !
# route-map rm5 permit 250
#  match interface Ethernet28
#  set as-path prepend 150,275
#  set metric 7249
# ------------
- name: Override (restore) all route map configuration with older configuration
  dellemc.enterprise_sonic.sonic_route_maps:
     config:
       - map_name: rm1
         action: permit
         sequence_num: 80
         match:
           as_path: bgp_as2
           community: bgp_comm_list3
           evpn:
             default_route: true
             route_type: prefix
             vni: 850
           ext_comm: bgp_ext_comm1
           interface: Vlan7
           ip:
             address: ip_pfx_list2
             next_hop: ip_pfx_list3
           ipv6:
             address: ipv6_pfx_list1
           local_preference: 8000
           metric: 400
           origin: egp
           peer:
             interface: Portchannel14
           source_protocol: bgp
           source_vrf: Vrf1
           tag: 7284
         set:
           as_path_prepend: 188,257
           comm_list_delete: bgp_comm_list2
           community:
             community_number:
               - "35:58"
               - "79:150"
               - "308:650"
               - "45:736"
             community_attributes:
               - local_as
               - no_export
               - no_peer
               - additive
           extcommunity:
             rt:
               - "30:40"
             soo:
               - "10.73.14.9:78"
           ip_next_hop: 10.48.16.18
           ipv6_next_hop:
             global_addr: 30::30
           local_preference: 635
           metric:
             rtt_action: add
           origin: egp
           weight: 93471
       - map_name: rm1
         action: deny
         sequence_num: 3047
         match:
           as_path: bgp_as3
           evpn:
             route_type: multicast
           ext_comm: bgp_ext_comm2
           origin: igp
           peer:
             interface: Ethernet6
           source_protocol: ospf
         set:
           metric:
             rtt_action: subtract
           origin: incomplete
       - map_name: rm2
         action: permit
         sequence_num: 100
         match:
           interface: Ethernet16
         set:
           as_path_prepend: 200,300,400
           ipv6_next_hop:
             global_addr: 37::58
             prefer_global: true
           metric: 8000
       - map_name: rm3
         action: deny
         sequence_num: 285
         match:
           evpn:
             route_type: macip
           origin: igp
           peer:
             ipv6: 87:95:15::53
           local_preference: 14783
           source_protocol: bgp
         set:
           community:
             community_attributes:
               - no_advertise
           metric:
             rtt_action: set
           origin: igp
         call: rm1
       - map_name: rm4
         action: permit
         sequence_num: 480
         match:
           evpn:
             route_type: prefix
           source_protocol: static
         set:
           metric:
             rtt_action: subtract
     state: overridden

# After state:
# ------------
#
# sonic# show running-configuration route-map
# !
# route-map rm1 permit 80
#  match as-path bgp_as2
#  match evpn default-route
#  match evpn route-type prefix
#  match evpn vni 850
#  match ip address prefix-list ip_pfx_list2
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Vlan7
#  match community bgp_comm_list3
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match ip next-hop prefix-list ip_pfx_list3
#  match peer PortChannel 14
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set as-path prepend 188,257
#  set community 35:58 79:150 308:650 45:736 local-AS no-export no-peer additive
#  set extcommunity rt 30:40
#  set extcommunity soo 10.73.14.9:78
#  set comm-list bgp_comm_list2 delete
#  set metric +rtt
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set local-preference 635
#  set origin egp
#  set weight 93471
# !
# route-map rm1 deny 3047
#  match as-path bgp_as3
#  match evpn route-type multicast
#  match ext-community bgp_ext_comm2
#  match peer Ethernet6
#  match source-protocol ospf
#  match origin igp
#  set metric -rtt
#  set origin incomplete
# !
# route-map rm2 permit 100
#  match interface Ethernet16
#  set as-path prepend 200,300,400
#  set ipv6 next-hop global 37::58
#  set ipv6 next-hop prefer-global
#  set metric 8000
# !
# route-map rm3 deny 285
#  match evpn route-type macip
#  match local-preference 14783
#  call rm1
#  match peer 87:95:15::53
#  match source-protocol bgp
#  match origin igp
#  set community no-advertise
#  set metric rtt
#  set origin igp
# !
# route-map rm4 permit 480
#  match evpn route-type prefix
#  match source-protocol static
#  set metric -rtt

# Using "deleted" state to remove configuration
#
# Before state:
# ------------
#
# sonic# show running-configuration route-map rm1 80
# !
# route-map rm1 permit 80
#  match as-path bgp_as2
#  match evpn default-route
#  match evpn route-type prefix
#  match evpn vni 850
#  match ip address prefix-list ip_pfx_list2
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Vlan7
#  match community bgp_comm_list3
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match ip next-hop prefix-list ip_pfx_list3
#  match peer PortChannel 14
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set as-path prepend 188,257
#  set community 35:58 79:150 308:650 45:736 local-AS no-export no-peer additive
#  set extcommunity rt 30:40
#  set extcommunity soo 10.73.14.9:78
#  set comm-list bgp_comm_list2 delete
#  set metric +rtt
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set local-preference 635
#  set origin egp
#  set weight 93471
# ------------
- name: Delete selected route map configuration
  dellemc.enterprise_sonic.sonic_route_maps:
     config:
       - map_name: rm1
         action: permit
         sequence_num: 80
         match:
           as_path:  bgp_as2
           community:  bgp_comm_list3
           evpn:
             vni: 850
           ip:
             address: ip_pfx_list2
         set:
           as_path_prepend: 188,257
           community:
             community_number:
               - "35:58"
             community_attributes:
               - local_as
           extcommunity:
             rt:
               - "30:40"
     state: deleted

# After state:
# ------------
#
# sonic# show running-configuration route-map rm1 80
# !
# route-map rm1 permit 80
#  match evpn default-route
#  match evpn route-type prefix
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Vlan7
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match ip next-hop prefix-list ip_pfx_list3
#  match peer PortChannel 14
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set community 79:150 308:650 45:736 no-export no-peer additive
#  set extcommunity soo 10.73.14.9:78
#  set comm-list bgp_comm_list2 delete
#  set metric +rtt
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set local-preference 635
#  set origin egp
#  set weight 93471

# Using "deleted" state to remove a route map or route map subset
#
# Before state:
# ------------
#
# sonic# show running-configuration route-map
# !
# route-map rm1 permit 80
#  match evpn default-route
#  match evpn route-type prefix
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Vlan7
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match ip next-hop prefix-list ip_pfx_list3
#  match peer PortChannel 14
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set community 79:150 308:650 45:736 no-export no-peer additive
#  set extcommunity soo 10.73.14.9:78
#  set comm-list bgp_comm_list2 delete
#  set metric +rtt
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set local-preference 635
#  set origin egp
#  set weight 93471
# !
# route-map rm1 deny 3047
#  match as-path bgp_as3
#  match evpn route-type multicast
#  match ext-community bgp_ext_comm2
#  match peer Ethernet6
#  match source-protocol ospf
#  match origin igp
#  set metric -rtt
#  set origin incomplete
# !
# route-map rm2 permit 100
#  match interface Ethernet16
#  set as-path prepend 200,300,400
#  set metric 8000
#  set ipv6 next-hop prefer-global
#  set ipv6 next-hop global 37::58
# !
# route-map rm3 deny 285
#  match evpn route-type macip
#  match local-preference 14783
#  call rm1
#  match peer 87:95:15::53
#  match source-protocol bgp
#  match origin igp
#  set community no-advertise
#  set metric rtt
#  set origin igp
# !
# route-map rm4 permit 480
#  match evpn route-type prefix
#  match source-protocol static
#  set metric -rtt
# ------------
- name: Delete a route map or route map subset
  dellemc.enterprise_sonic.sonic_route_maps:
     config:
       - map_name: rm1
         sequence_num: 3047
       - map_name: rm2
         sequence_num: 100
     state: deleted

# After state:
# ------------
#
# sonic# show running-configuration route-map
# !
# route-map rm1 permit 80
#  match evpn default-route
#  match evpn route-type prefix
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Vlan7
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match ip next-hop prefix-list ip_pfx_list3
#  match peer PortChannel 14
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set community 79:150 308:650 45:736 no-export no-peer additive
#  set extcommunity soo 10.73.14.9:78
#  set comm-list bgp_comm_list2 delete
#  set metric +rtt
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set local-preference 635
#  set origin egp
#  set weight 93471
# !
# route-map rm3 deny 285
#  match evpn route-type macip
#  match local-preference 14783
#  call rm1
#  match peer 87:95:15::53
#  match source-protocol bgp
#  match origin igp
#  set community no-advertise
#  set metric rtt
#  set origin igp
# !
# route-map rm4 permit 480
#  match evpn route-type prefix
#  match source-protocol static
#  set metric -rtt

# Using "deleted" state to remove all route map configuration
#
# Before state:
# ------------
#
# sonic# show running-configuration route-map
# !
# route-map rm1 permit 80
#  match evpn default-route
#  match evpn route-type prefix
#  match ipv6 address prefix-list ipv6_pfx_list1
#  match interface Vlan7
#  match ext-community bgp_ext_comm1
#  match tag 7284
#  match local-preference 8000
#  match source-vrf Vrf1
#  match ip next-hop prefix-list ip_pfx_list3
#  match peer PortChannel 14
#  match source-protocol bgp
#  match metric 400
#  match origin egp
#  set community 79:150 308:650 45:736 no-export no-peer additive
#  set extcommunity soo 10.73.14.9:78
#  set comm-list bgp_comm_list2 delete
#  set metric +rtt
#  set ip next-hop 10.48.16.18
#  set ipv6 next-hop global 30::30
#  set local-preference 635
#  set origin egp
#  set weight 93471
# !
# route-map rm3 deny 285
#  match evpn route-type macip
#  match local-preference 14783
#  call rm1
#  match peer 87:95:15::53
#  match source-protocol bgp
#  match origin igp
#  set community no-advertise
#  set metric rtt
#  set origin igp
# !
# route-map rm4 permit 480
#  match evpn route-type prefix
#  match source-protocol static
#  set metric -rtt
# ------------
- name: Delete all route map configuration
  dellemc.enterprise_sonic.sonic_route_maps:
     config: []
     state: deleted

# After state:
# ------------
#
# sonic# show running-configuration route-map
# sonic#
# (no route map configuration present)
```

## [Return Values](sonic_route_maps_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n as the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n as the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Kerry Meyer (@kerry-meyer)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
