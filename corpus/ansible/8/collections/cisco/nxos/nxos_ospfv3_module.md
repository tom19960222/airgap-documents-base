---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_ospfv3 module – OSPFv3 resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_ospfv3_module.html
fetched_at: 2026-07-28T01:38:59+00:00
---
# cisco.nxos.nxos_ospfv3 module – OSPFv3 resource module

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_ospfv3`.

New in cisco.nxos 1.2.0

- [Synopsis](nxos_ospfv3_module.md#synopsis)
- [Parameters](nxos_ospfv3_module.md#parameters)
- [Notes](nxos_ospfv3_module.md#notes)
- [Examples](nxos_ospfv3_module.md#examples)
- [Return Values](nxos_ospfv3_module.md#return-values)

## [Synopsis](nxos_ospfv3_module.md#id1)

- This module manages OSPFv3 configuration on devices running Cisco NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: ospfv3

## [Parameters](nxos_ospfv3_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of OSPFv3 process configuration. |
| **processes**  list / elements=dictionary | A list of OSPFv3 instances’ configurations. |
| **address_family**  dictionary | IPv6 unicast address-family OSPFv3 settings. |
| **afi**  string | Configure OSPFv3 settings under IPv6 address-family.  **Choices:**   - `"ipv6"` |
| **areas**  list / elements=dictionary | Configure properties of OSPF Areas under address-family. |
| **area_id**  string / required | The Area ID in IP Address format. |
| **default_cost**  integer | Specify the default cost. |
| **filter_list**  list / elements=dictionary | Filter prefixes between OSPF areas. |
| **direction**  string / required | The direction to apply the route map.  **Choices:**   - `"in"` - `"out"` |
| **route_map**  string / required | The Route-map name. |
| **ranges**  list / elements=dictionary | Configure an address range for the area. |
| **cost**  integer | Cost to use for the range. |
| **not_advertise**  boolean | Suppress advertising the specified range.  **Choices:**   - `false` - `true` |
| **prefix**  string / required | IP in Prefix format (x.x.x.x/len) |
| **default_information**  dictionary | Control distribution of default routes. |
| **originate**  dictionary | Distribute a default route. |
| **always**  boolean | Always advertise a default route.  **Choices:**   - `false` - `true` |
| **route_map**  string | Policy to control distribution of default routes |
| **set**  boolean | Enable distribution of default route.  **Choices:**   - `false` - `true` |
| **distance**  integer | Configure the OSPF administrative distance. |
| **maximum_paths**  integer | Maximum paths per destination. |
| **redistribute**  list / elements=dictionary | Redistribute information from another routing protocol. |
| **id**  string | The identifier for the protocol specified. |
| **protocol**  string / required | The name of the protocol.  **Choices:**   - `"bgp"` - `"direct"` - `"eigrp"` - `"isis"` - `"lisp"` - `"ospfv3"` - `"rip"` - `"static"` |
| **route_map**  string / required | The route map policy to constrain redistribution. |
| **safi**  string | Configure OSPFv3 settings under IPv6 unicast address-family.  **Choices:**   - `"unicast"` |
| **summary_address**  list / elements=dictionary | Configure route summarization for redistribution. |
| **not_advertise**  boolean | Suppress advertising the specified summary.  **Choices:**   - `false` - `true` |
| **prefix**  string / required | IPv6 prefix format ‘xxxx:xxxx/ml’, ‘xxxx:xxxx::/ml’ or ‘xxxx::xx/128’ |
| **tag**  integer | A 32-bit tag value. |
| **table_map**  dictionary | Policy for filtering/modifying OSPF routes before sending them to RIB. |
| **filter**  boolean | Block the OSPF routes from being sent to RIB.  **Choices:**   - `false` - `true` |
| **name**  string / required | The Route Map name. |
| **timers**  dictionary | Configure timer related constants. |
| **throttle**  dictionary | Configure throttle related constants. |
| **spf**  dictionary | Set OSPF SPF timers. |
| **initial_spf_delay**  integer | Initial SPF schedule delay in milliseconds. |
| **max_wait_time**  integer | Maximum wait time between SPF calculations. |
| **min_hold_time**  integer | Minimum hold time between SPF calculations. |
| **areas**  list / elements=dictionary | Configure properties of OSPF Areas. |
| **area_id**  string / required | The Area ID in IP Address format. |
| **nssa**  dictionary | NSSA settings for the area. |
| **default_information_originate**  boolean | Originate Type-7 default LSA into NSSA area.  **Choices:**   - `false` - `true` |
| **no_redistribution**  boolean | Do not send redistributed LSAs into NSSA area.  **Choices:**   - `false` - `true` |
| **no_summary**  boolean | Do not send summary LSAs into NSSA area.  **Choices:**   - `false` - `true` |
| **route_map**  string | Policy to control distribution of default route. |
| **set**  boolean | Configure area as NSSA.  **Choices:**   - `false` - `true` |
| **translate**  dictionary | Translate LSA. |
| **type7**  dictionary | Translate from Type 7 to Type 5. |
| **always**  boolean | Always translate LSAs  **Choices:**   - `false` - `true` |
| **never**  boolean | Never translate LSAs  **Choices:**   - `false` - `true` |
| **supress_fa**  boolean | Suppress forwarding address in translated LSAs.  **Choices:**   - `false` - `true` |
| **stub**  dictionary | Settings for configuring the area as a stub. |
| **no_summary**  boolean | Prevent ABR from sending summary LSAs into stub area.  **Choices:**   - `false` - `true` |
| **set**  boolean | Configure the area as a stub.  **Choices:**   - `false` - `true` |
| **auto_cost**  dictionary | Calculate OSPF cost according to bandwidth. |
| **reference_bandwidth**  integer / required | Reference bandwidth used to assign OSPF cost. |
| **unit**  string / required | Specify in which unit the reference bandwidth is specified.  **Choices:**   - `"Gbps"` - `"Mbps"` |
| **flush_routes**  boolean | Flush routes on a non-graceful controlled restart.  **Choices:**   - `false` - `true` |
| **graceful_restart**  dictionary | Configure graceful restart. |
| **grace_period**  integer | Configure maximum interval to restart gracefully. |
| **helper_disable**  boolean | Enable/Disable helper mode.  **Choices:**   - `false` - `true` |
| **planned_only**  boolean | Enable graceful restart only for a planned restart  **Choices:**   - `false` - `true` |
| **set**  boolean | Enable graceful-restart.  **Choices:**   - `false` - `true` |
| **isolate**  boolean | Isolate this router from OSPF perspective.  **Choices:**   - `false` - `true` |
| **log_adjacency_changes**  dictionary | Log changes in adjacency state. |
| **detail**  boolean | Notify all state changes.  **Choices:**   - `false` - `true` |
| **log**  boolean | Enable/disable logging changes in adjacency state.  **Choices:**   - `false` - `true` |
| **max_lsa**  dictionary | Feature to limit the number of non-self-originated LSAs. |
| **ignore_count**  integer | Set count on how many times adjacencies can be suppressed. |
| **ignore_time**  integer | Set time during which all adjacencies are suppressed. |
| **max_non_self_generated_lsa**  integer / required | Set the maximum number of non self-generated LSAs. |
| **reset_time**  integer | Set number of minutes after which ignore-count is reset to zero. |
| **threshold**  integer | Threshold value (%) at which to generate a warning message. |
| **warning_only**  boolean | Log a warning message when limit is exceeded.  **Choices:**   - `false` - `true` |
| **max_metric**  dictionary | Maximize the cost metric. |
| **router_lsa**  dictionary | Router LSA configuration. |
| **external_lsa**  dictionary | External LSA configuration. |
| **max_metric_value**  integer | Set max metric value for external LSAs. |
| **set**  boolean | Set external-lsa attribute.  **Choices:**   - `false` - `true` |
| **inter_area_prefix_lsa**  dictionary | Inter-area-prefix LSAs configuration. |
| **max_metric_value**  integer | Max metric value for summary LSAs. |
| **set**  boolean | Set summary-lsa attribute.  **Choices:**   - `false` - `true` |
| **on_startup**  dictionary | Effective only at startup. |
| **set**  boolean | Set on-startup attribute.  **Choices:**   - `false` - `true` |
| **wait_for_bgp_asn**  integer | ASN of BGP to wait for. |
| **wait_period**  integer | Wait period in seconds after startup. |
| **set**  boolean | Set router-lsa attribute.  **Choices:**   - `false` - `true` |
| **stub_prefix_lsa**  boolean | Advertise Max metric for Stub links as well.  **Choices:**   - `false` - `true` |
| **name_lookup**  boolean | Display OSPF router ids as DNS names.  **Choices:**   - `false` - `true` |
| **passive_interface**  dictionary | Suppress routing updates on the interface. |
| **default**  boolean | Interfaces passive by default.  **Choices:**   - `false` - `true` |
| **process_id**  string / required | The OSPF process tag. |
| **router_id**  string | Set OSPF process router-id. |
| **shutdown**  boolean | Shutdown the OSPF protocol instance.  **Choices:**   - `false` - `true` |
| **timers**  dictionary | Configure timer related constants. |
| **lsa_arrival**  integer | Mimimum interval between arrival of a LSA. |
| **lsa_group_pacing**  integer | LSA group refresh/maxage interval. |
| **throttle**  dictionary | Configure throttle related constants. |
| **lsa**  dictionary | Set rate-limiting for LSA generation. |
| **hold_interval**  integer | The hold interval. |
| **max_interval**  integer | The max interval. |
| **start_interval**  integer | The start interval. |
| **vrfs**  list / elements=dictionary | Configure VRF specific OSPF settings. |
| **areas**  list / elements=dictionary | Configure properties of OSPF Areas. |
| **area_id**  string / required | The Area ID in IP Address format. |
| **nssa**  dictionary | NSSA settings for the area. |
| **default_information_originate**  boolean | Originate Type-7 default LSA into NSSA area.  **Choices:**   - `false` - `true` |
| **no_redistribution**  boolean | Do not send redistributed LSAs into NSSA area.  **Choices:**   - `false` - `true` |
| **no_summary**  boolean | Do not send summary LSAs into NSSA area.  **Choices:**   - `false` - `true` |
| **route_map**  string | Policy to control distribution of default route. |
| **set**  boolean | Configure area as NSSA.  **Choices:**   - `false` - `true` |
| **translate**  dictionary | Translate LSA. |
| **type7**  dictionary | Translate from Type 7 to Type 5. |
| **always**  boolean | Always translate LSAs  **Choices:**   - `false` - `true` |
| **never**  boolean | Never translate LSAs  **Choices:**   - `false` - `true` |
| **supress_fa**  boolean | Suppress forwarding address in translated LSAs.  **Choices:**   - `false` - `true` |
| **stub**  dictionary | Settings for configuring the area as a stub. |
| **no_summary**  boolean | Prevent ABR from sending summary LSAs into stub area.  **Choices:**   - `false` - `true` |
| **set**  boolean | Configure the area as a stub.  **Choices:**   - `false` - `true` |
| **auto_cost**  dictionary | Calculate OSPF cost according to bandwidth. |
| **reference_bandwidth**  integer / required | Reference bandwidth used to assign OSPF cost. |
| **unit**  string / required | Specify in which unit the reference bandwidth is specified.  **Choices:**   - `"Gbps"` - `"Mbps"` |
| **graceful_restart**  dictionary | Configure graceful restart. |
| **grace_period**  integer | Configure maximum interval to restart gracefully. |
| **helper_disable**  boolean | Enable/Disable helper mode.  **Choices:**   - `false` - `true` |
| **planned_only**  boolean | Enable graceful restart only for a planned restart  **Choices:**   - `false` - `true` |
| **set**  boolean | Enable graceful-restart.  **Choices:**   - `false` - `true` |
| **log_adjacency_changes**  dictionary | Log changes in adjacency state. |
| **detail**  boolean | Notify all state changes.  **Choices:**   - `false` - `true` |
| **log**  boolean | Enable/disable logging changes in adjacency state.  **Choices:**   - `false` - `true` |
| **max_lsa**  dictionary | Feature to limit the number of non-self-originated LSAs. |
| **ignore_count**  integer | Set count on how many times adjacencies can be suppressed. |
| **ignore_time**  integer | Set time during which all adjacencies are suppressed. |
| **max_non_self_generated_lsa**  integer / required | Set the maximum number of non self-generated LSAs. |
| **reset_time**  integer | Set number of minutes after which ignore-count is reset to zero. |
| **threshold**  integer | Threshold value (%) at which to generate a warning message. |
| **warning_only**  boolean | Log a warning message when limit is exceeded.  **Choices:**   - `false` - `true` |
| **max_metric**  dictionary | Maximize the cost metric. |
| **router_lsa**  dictionary | Router LSA configuration. |
| **external_lsa**  dictionary | External LSA configuration. |
| **max_metric_value**  integer | Set max metric value for external LSAs. |
| **set**  boolean | Set external-lsa attribute.  **Choices:**   - `false` - `true` |
| **inter_area_prefix_lsa**  dictionary | Inter-area-prefix LSAs configuration. |
| **max_metric_value**  integer | Max metric value for summary LSAs. |
| **set**  boolean | Set summary-lsa attribute.  **Choices:**   - `false` - `true` |
| **on_startup**  dictionary | Effective only at startup. |
| **set**  boolean | Set on-startup attribute.  **Choices:**   - `false` - `true` |
| **wait_for_bgp_asn**  integer | ASN of BGP to wait for. |
| **wait_period**  integer | Wait period in seconds after startup. |
| **set**  boolean | Set router-lsa attribute.  **Choices:**   - `false` - `true` |
| **stub_prefix_lsa**  boolean | Advertise Max metric for Stub links as well.  **Choices:**   - `false` - `true` |
| **name_lookup**  boolean | Display OSPF router ids as DNS names.  **Choices:**   - `false` - `true` |
| **passive_interface**  dictionary | Suppress routing updates on the interface. |
| **default**  boolean | Interfaces passive by default.  **Choices:**   - `false` - `true` |
| **router_id**  string | Set OSPF process router-id. |
| **shutdown**  boolean | Shutdown the OSPF protocol instance.  **Choices:**   - `false` - `true` |
| **timers**  dictionary | Configure timer related constants. |
| **lsa_arrival**  integer | Mimimum interval between arrival of a LSA. |
| **lsa_group_pacing**  integer | LSA group refresh/maxage interval. |
| **throttle**  dictionary | Configure throttle related constants. |
| **lsa**  dictionary | Set rate-limiting for LSA generation. |
| **hold_interval**  integer | The hold interval. |
| **max_interval**  integer | The max interval. |
| **start_interval**  integer | The start interval. |
| **vrf**  string / required | Name/Identifier of the VRF. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section “^router ospfv3”**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](nxos_ospfv3_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 7.0(3)I5(1).
> - Unsupported for Cisco MDS
> - This module works with connection `network_cli` and `httpapi`.

## [Examples](nxos_ospfv3_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# nxos-9k-rdo# sh running-config | section "^router ospfv3"
# nxos-9k-rdo#

- name: Merge the provided configuration with the existing running configuration
  cisco.nxos.nxos_ospfv3:
    config:
      processes:
      - process_id: 100
        router_id: 203.0.113.20
      - process_id: 102
        router_id: 198.51.100.1
        address_family:
          afi: ipv6
          safi: unicast
          areas:
          - area_id: 0.0.0.100
            filter_list:
            - route_map: rmap_1
              direction: in
            - route_map: rmap_2
              direction: out
            ranges:
            - prefix: 2001:db2::/32
              not_advertise: true
            - prefix: 2001:db3::/32
              cost: 120
          redistribute:
          - protocol: eigrp
            id: 120
            route_map: rmap_1
          - protocol: direct
            route_map: ospf102-direct-connect
        vrfs:
        - vrf: zone1
          router_id: 198.51.100.129
          areas:
          - area_id: 0.0.0.102
            nssa:
              default_information_originate: true
              no_summary: true
          - area_id: 0.0.0.103
            nssa:
              no_summary: true
              translate:
                type7:
                  always: true
        - vrf: zone2
          auto_cost:
            reference_bandwidth: 45
            unit: Gbps
    state: merged

# Task output
# -------------
# before: {}
#
# commands:
#  - router ospf 102
#  - router-id 198.51.100.1
#  - address-family ipv6 unicast
#  - redistribute eigrp 120 route-map rmap_1
#  - redistribute direct route-map ospf102-direct-connect
#  - area 0.0.0.100 filter-list route-map rmap_1 in
#  - area 0.0.0.100 filter-list route-map rmap_2 out
#  - area 0.0.0.100 range 2001:db2::/32 not-advertise
#  - area 0.0.0.100 range 2001:db3::/32 cost 120
#  - vrf zone1
#  - router-id 198.51.100.129
#  - area 0.0.0.102 nssa no-summary default-information-originate
#  - area 0.0.0.103 nssa no-summary
#  - area 0.0.0.103 nssa translate type7 always
#  - vrf zone2
#  - auto-cost reference-bandwidth 45 Gbps
#  - router ospf 100
#  - router-id 203.0.113.20
#
# after:
#    processes:
#    - process_id: "100"
#      router_id: 203.0.113.20
#    - address_family:
#        afi: ipv4
#        safi: unicast
#        areas:
#        - area_id: 0.0.0.100
#          filter_list:
#          - direction: out
#            route_map: rmap_2
#          - direction: in
#            route_map: rmap_1
#          ranges:
#          - not_advertise: true
#            prefix: 2001:db2::/32
#          - cost: 120
#            prefix: 2001:db3::/32
#        redistribute:
#        - protocol: direct
#          route_map: ospf102-direct-connect
#        - id: "120"
#          protocol: eigrp
#          route_map: rmap_1
#      process_id: "102"
#      router_id: 198.51.100.1
#      vrfs:
#      - areas:
#        - area_id: 0.0.0.102
#          nssa:
#            default_information_originate: true
#            no_summary: true
#        - area_id: 0.0.0.103
#          nssa:
#            no_summary: true
#            translate:
#              type7:
#                always: true
#        router_id: 198.51.100.129
#        vrf: zone1
#      - auto_cost:
#          reference_bandwidth: 45
#          unit: Gbps
#        vrf: zone2
#

# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospfv3"
# router ospfv3 100
#   router-id 203.0.113.20
# router ospfv3 102
#   router-id 198.51.100.1
#   address-family ipv6 unicast
#     redistribute direct route-map ospf102-direct-connect
#     redistribute eigrp 120 route-map rmap_1
#     area 0.0.0.100 filter-list route-map rmap_2 out
#     area 0.0.0.100 filter-list route-map rmap_1 in
#     area 0.0.0.100 range 2001:db2::/32 not-advertise
#     area 0.0.0.100 range 2001:db3::/32 cost 120
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.0.102 nssa no-summary default-information-originate
#     area 0.0.0.103 nssa no-summary
#     area 0.0.0.103 nssa translate type7 always
#   vrf zone2
#     auto-cost reference-bandwidth 45 Gbps

# Using replaced

# Before state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospfv3"
# router ospfv3 100
#   router-id 203.0.113.20
# router ospfv3 102
#   router-id 198.51.100.1
#   address-family upv6 unicast
#     redistribute direct route-map ospf102-direct-connect
#     redistribute eigrp 120 route-map rmap_1
#     area 0.0.0.100 filter-list route-map rmap_2 out
#     area 0.0.0.100 filter-list route-map rmap_1 in
#     area 0.0.0.100 range 2001:db2::/32 not-advertise
#     area 0.0.0.100 range 2001:db3::/32 cost 120
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.0.102 nssa no-summary default-information-originate
#     area 0.0.0.103 nssa no-summary
#     area 0.0.0.103 nssa translate type7 always
#   vrf zone2
#     auto-cost reference-bandwidth 45 Gbps

- name: Replace device configurations of listed OSPFv3 processes with provided configurations
  cisco.nxos.nxos_ospfv3:
    config:
      processes:
      - process_id: 102
        router_id: 198.51.100.1
        address_family:
          afi: ipv6
          safi: unicast
          areas:
          - area_id: 0.0.0.100
            filter_list:
            - route_map: rmap_8
              direction: in
            ranges:
            - not_advertise: true
              prefix: 2001:db2::/32
          redistribute:
          - protocol: eigrp
            id: 130
            route_map: rmap_1
          - protocol: direct
            route_map: ospf102-direct-connect
        vrfs:
        - vrf: zone1
          router_id: 198.51.100.129
          areas:
          - area_id: 0.0.0.102
            nssa:
              default_information_originate: True
              no_summary: True
    state: replaced

# Task output
# -------------
# before:
#    processes:
#    - process_id: "100"
#      router_id: 203.0.113.20
#    - address_family:
#        afi: ipv4
#        safi: unicast
#        areas:
#        - area_id: 0.0.0.100
#          filter_list:
#          - direction: out
#            route_map: rmap_2
#          - direction: in
#            route_map: rmap_1
#          ranges:
#          - not_advertise: true
#            prefix: 2001:db2::/32
#          - cost: 120
#            prefix: 2001:db3::/32
#        redistribute:
#        - protocol: direct
#          route_map: ospf102-direct-connect
#        - id: "120"
#          protocol: eigrp
#          route_map: rmap_1
#      process_id: "102"
#      router_id: 198.51.100.1
#      vrfs:
#      - areas:
#        - area_id: 0.0.0.102
#          nssa:
#            default_information_originate: true
#            no_summary: true
#        - area_id: 0.0.0.103
#          nssa:
#            no_summary: true
#            translate:
#              type7:
#                always: true
#        router_id: 198.51.100.129
#        vrf: zone1
#      - auto_cost:
#          reference_bandwidth: 45
#          unit: Gbps
#        vrf: zone2
#
#  commands:
#  - router ospf 102
#  - address-family ipv6 unicast
#  - redistribute eigrp 130 route-map rmap_1
#  - no redistribute eigrp 120 route-map rmap_1
#  - area 0.0.0.100 filter-list route-map rmap_8 in
#  - no area 0.0.0.100 filter-list route-map rmap_2 out
#  - no area 0.0.0.100 range 2001:db3::/32
#  - vrf zone1
#  - no area 0.0.0.103 nssa
#  - no area 0.0.0.103 nssa translate type7 always
#  - no vrf zone2
#
# after:
#    processes:
#    - process_id: "100"
#      router_id: 203.0.113.20
#    - address_family:
#        afi: ipv6
#        safi: unicast
#        areas:
#        - area_id: 0.0.0.100
#          filter_list:
#          - direction: in
#            route_map: rmap_8
#          ranges:
#          - not_advertise: true
#            prefix: 2001:db2::/32
#        redistribute:
#        - protocol: direct
#          route_map: ospf102-direct-connect
#        - id: "130"
#          protocol: eigrp
#          route_map: rmap_1
#      process_id: "102"
#      router_id: 198.51.100.1
#      vrfs:
#      - areas:
#        - area_id: 0.0.0.102
#          nssa:
#            default_information_originate: true
#            no_summary: true
#        router_id: 198.51.100.129
#        vrf: zone1

# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospfv3"
# router ospfv3 100
#   router-id 203.0.113.20
# router ospfv3 102
#   router-id 198.51.100.1
#   address-family ipv6 unicast
#     redistribute direct route-map ospf102-direct-connect
#     redistribute eigrp 130 route-map rmap_1
#     area 0.0.0.100 filter-list route-map rmap_8 in
#     area 0.0.0.100 range 198.51.100.64/27 not-advertise
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.0.102 nssa no-summary default-information-originate

# Using overridden

# Before state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospfv3"
# router ospfv3 100
#   router-id 203.0.113.20
# router ospfv3 102
#   router-id 198.51.100.1
#   address-family ipv6 unicast
#     redistribute direct route-map ospf102-direct-connect
#     redistribute eigrp 120 route-map rmap_1
#     area 0.0.0.100 filter-list route-map rmap_2 out
#     area 0.0.0.100 filter-list route-map rmap_1 in
#     area 0.0.0.100 range 2001:db2::/32 not-advertise
#     area 0.0.0.100 range 2001:db3::/32 cost 120
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.0.102 nssa no-summary default-information-originate
#     area 0.0.0.103 nssa no-summary
#     area 0.0.0.103 nssa translate type7 always
#   vrf zone2
#     auto-cost reference-bandwidth 45 Gbps

- name: Override all OSPFv3 configuration with provided configuration
  cisco.nxos.nxos_ospfv3:
    config:
      processes:
      - process_id: 104
        router_id: 203.0.113.20
      - process_id: 102
        router_id: 198.51.100.1
        shutdown: true
    state: overridden

# Task output
# -------------
# before:
#    processes:
#    - process_id: "100"
#      router_id: 203.0.113.20
#    - address_family:
#        afi: ipv4
#        safi: unicast
#        areas:
#        - area_id: 0.0.0.100
#          filter_list:
#          - direction: out
#            route_map: rmap_2
#          - direction: in
#            route_map: rmap_1
#          ranges:
#          - not_advertise: true
#            prefix: 2001:db2::/32
#          - cost: 120
#            prefix: 2001:db3::/32
#        redistribute:
#        - protocol: direct
#          route_map: ospf102-direct-connect
#        - id: "120"
#          protocol: eigrp
#          route_map: rmap_1
#      process_id: "102"
#      router_id: 198.51.100.1
#      vrfs:
#      - areas:
#        - area_id: 0.0.0.102
#          nssa:
#            default_information_originate: true
#            no_summary: true
#        - area_id: 0.0.0.103
#          nssa:
#            no_summary: true
#            translate:
#              type7:
#                always: true
#        router_id: 198.51.100.129
#        vrf: zone1
#      - auto_cost:
#          reference_bandwidth: 45
#          unit: Gbps
#        vrf: zone2
#
# commands:
#  - no router ospfv3 100
#  - router ospfv3 104
#  - router-id 203.0.113.20
#  - router ospfv3 102
#  - shutdown
#  - address-family ipv6 unicast
#  - no redistribute direct route-map ospf102-direct-connect
#  - no redistribute eigrp 120 route-map rmap_1
#  - no area 0.0.0.100 filter-list route-map rmap_2 out
#  - no area 0.0.0.100 filter-list route-map rmap_1 in
#  - no area 0.0.0.100 range 2001:db2::/32
#  - no area 0.0.0.100 range 2001:db3::/32
#  - no vrf zone1
#  - no vrf zone2
#
# after:
#    processes:
#    - process_id: "102"
#      router_id: 198.51.100.1
#      shutdown: true
#      address_family:
#        afi: ipv6
#        safi: unicast
#    - process_id: "104"
#      router_id: 203.0.113.20

# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospfv3"
# router ospfv3 102
#   router-id 198.51.100.1
#   address-family ipv6 unicast
#   shutdown
# router ospfv3 104
#   router-id 203.0.113.20

# Using deleted to delete a single OSPF process

# Before state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospf .*"
# router ospfv3 100
#   router-id 203.0.113.20
# router ospfv3 102
#   router-id 198.51.100.1
#   address-family ipv6 unicast
#     redistribute direct route-map ospf102-direct-connect
#     redistribute eigrp 120 route-map rmap_1
#     area 0.0.0.100 filter-list route-map rmap_2 out
#     area 0.0.0.100 filter-list route-map rmap_1 in
#     area 0.0.0.100 range 2001:db2::/32 not-advertise
#     area 0.0.0.100 range 2001:db3::/32 cost 120
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.0.102 nssa no-summary default-information-originate
#     area 0.0.0.103 nssa no-summary
#     area 0.0.0.103 nssa translate type7 always
#   vrf zone2
#     auto-cost reference-bandwidth 45 Gbps

- name: Delete a single OSPFv3 process
  cisco.nxos.nxos_ospfv3:
    config:
      processes:
      - process_id: 102
    state: deleted

# Task output
# -------------
# before:
#    processes:
#    - process_id: "100"
#      router_id: 203.0.113.20
#    - address_family:
#        afi: ipv4
#        safi: unicast
#        areas:
#        - area_id: 0.0.0.100
#          filter_list:
#          - direction: out
#            route_map: rmap_2
#          - direction: in
#            route_map: rmap_1
#          ranges:
#          - not_advertise: true
#            prefix: 2001:db2::/32
#          - cost: 120
#            prefix: 2001:db3::/32
#        redistribute:
#        - protocol: direct
#          route_map: ospf102-direct-connect
#        - id: "120"
#          protocol: eigrp
#          route_map: rmap_1
#      process_id: "102"
#      router_id: 198.51.100.1
#      vrfs:
#      - areas:
#        - area_id: 0.0.0.102
#          nssa:
#            default_information_originate: true
#            no_summary: true
#        - area_id: 0.0.0.103
#          nssa:
#            no_summary: true
#            translate:
#              type7:
#                always: true
#        router_id: 198.51.100.129
#        vrf: zone1
#      - auto_cost:
#          reference_bandwidth: 45
#          unit: Gbps
#        vrf: zone2
#
# commands:
#  - no router ospfv3 102
#
# after:
#   processes:
#   - process_id: "100"
#     router_id: 203.0.113.20

# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospfv3"
# router ospfv3 100
#   router-id 203.0.113.20

# Using deleted all OSPFv3 processes from the device

# Before state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospfv3"
# router ospfv3 100
#   router-id 203.0.113.20
# router ospfv3 102
#   router-id 198.51.100.1
#   address-family ipv6 unicast
#     redistribute direct route-map ospf102-direct-connect
#     redistribute eigrp 120 route-map rmap_1
#     area 0.0.0.100 filter-list route-map rmap_2 out
#     area 0.0.0.100 filter-list route-map rmap_1 in
#     area 0.0.0.100 range 2001:db2::/32 not-advertise
#     area 0.0.0.100 range 2001:db3::/32 cost 120
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.0.102 nssa no-summary default-information-originate
#     area 0.0.0.103 nssa no-summary
#     area 0.0.0.103 nssa translate type7 always
#   vrf zone2
#     auto-cost reference-bandwidth 45 Gbps

- name: Delete all OSPFv3 processes from the device
  cisco.nxos.nxos_ospfv3:
    state: deleted

# Task output
# -------------
# before:
#    processes:
#    - process_id: "100"
#      router_id: 203.0.113.20
#    - address_family:
#        afi: ipv4
#        safi: unicast
#        areas:
#        - area_id: 0.0.0.100
#          filter_list:
#          - direction: out
#            route_map: rmap_2
#          - direction: in
#            route_map: rmap_1
#          ranges:
#          - not_advertise: true
#            prefix: 2001:db2::/32
#          - cost: 120
#            prefix: 2001:db3::/32
#        redistribute:
#        - protocol: direct
#          route_map: ospf102-direct-connect
#        - id: "120"
#          protocol: eigrp
#          route_map: rmap_1
#      process_id: "102"
#      router_id: 198.51.100.1
#      vrfs:
#      - areas:
#        - area_id: 0.0.0.102
#          nssa:
#            default_information_originate: true
#            no_summary: true
#        - area_id: 0.0.0.103
#          nssa:
#            no_summary: true
#            translate:
#              type7:
#                always: true
#        router_id: 198.51.100.129
#        vrf: zone1
#      - auto_cost:
#          reference_bandwidth: 45
#          unit: Gbps
#        vrf: zone2
#
# commands:
#  - no router ospfv3 100
#  - no router ospfv3 102
#
#  after: {}

# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospfv3"
# nxos-9k-rdo#

# Using rendered

- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.nxos.nxos_ospfv3:
    config:
      processes:
      - process_id: 100
        router_id: 203.0.113.20
      - process_id: 102
        router_id: 198.51.100.1
        address_family:
          afi: ipv6
          safi: unicast
          areas:
          - area_id: 0.0.0.100
            filter_list:
            - route_map: rmap_1
              direction: in
            - route_map: rmap_2
              direction: out
            ranges:
            - prefix: 2001:db2::/32
              not_advertise: true
            - prefix: 2001:db3::/32
              cost: 120
          redistribute:
          - protocol: eigrp
            id: 120
            route_map: rmap_1
          - protocol: direct
            route_map: ospf102-direct-connect
        vrfs:
        - vrf: zone1
          router_id: 198.51.100.129
          areas:
          - area_id: 0.0.0.102
            nssa:
              default_information_originate: true
              no_summary: true
          - area_id: 0.0.0.103
            nssa:
              no_summary: true
              translate:
                type7:
                  always: true
        - vrf: zone2
          auto_cost:
            reference_bandwidth: 45
            unit: Gbps
    state: rendered

# Task Output (redacted)
# -----------------------
# rendered:
#  - router ospfv3 100
#  - router-id 203.0.113.20
#  - router ospfv3 102
#  - router-id 198.51.100.1
#  - address-family ipv6 unicast
#  - redistribute eigrp 120 route-map rmap_1
#  - redistribute direct route-map ospf102-direct-connect
#  - area 0.0.0.100 filter-list route-map rmap_1 in
#  - area 0.0.0.100 filter-list route-map rmap_2 out
#  - area 0.0.0.100 range 2001:db2::/32 not-advertise
#  - area 0.0.0.100 range 2001:db3::/32 cost 120
#  - vrf zone1
#  - router-id 198.51.100.129
#  - area 0.0.0.102 nssa no-summary default-information-originate
#  - area 0.0.0.103 nssa no-summary
#  - area 0.0.0.103 nssa translate type7 always
#  - vrf zone2
#  - auto-cost reference-bandwidth 45 Gbps

# Using parsed

# parsed.cfg
# ------------
# router ospfv3 100
#   router-id 192.0.100.1
#   address-family ipv6 unicast
#     redistribute direct route-map ospf-direct-connect
#     redistribute eigrp 120 route-map rmap_1
#     area 0.0.0.100 filter-list route-map rmap_2 out
#     area 0.0.0.100 filter-list route-map rmap_1 in
#     area 0.0.0.100 range 2001:db2::/32 not-advertise
#     area 0.0.0.100 range 2001:db3::/32 cost 120
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.100.1 nssa no-summary no-redistribution
# router ospfv3 102
#   router-id 198.54.100.1
#   shutdown

- name: Parse externally provided OSPFv3 config
  cisco.nxos.nxos_ospfv3:
    running_config: "{{ lookup('file', 'ospfv2.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
# parsed:
#   processes:
#   - process_id: "100"
#     address_family:
#       afi: ipv6
#       safi: unicast
#       areas:
#       - area_id: 0.0.0.101
#         nssa:
#           no_redistribution: true
#           no_summary: true
#       - area_id: 0.0.0.102
#         stub:
#           no_summary: true
#         filter_list:
#           - direction: out
#             route_map: rmap_2
#           - direction: in
#             route_map: rmap_1
#         ranges:
#           - not_advertise: true
#             prefix: 192.0.2.0/24
#           - cost: 120
#             prefix: 192.0.3.0/24
#       redistribute:
#       - protocol: direct
#         route_map: ospf-direct-connect
#       - id: "120"
#         protocol: eigrp
#         route_map: rmap_1
#     router_id: 192.0.100.1
#     vrfs:
#       - vrf: zone1
#         areas:
#           - area_id: 0.0.100.1
#             nssa:
#               no_redistribution: true
#               no_summary: true
#         router_id: 192.0.100.2
#   - process_id: "102"
#     router_id: 198.54.100.1
#     shutdown: True

# Using gathered

- name: Gather OSPFv3 facts using gathered
  cisco.nxos.nxos_ospfv3:
    state: gathered

# Task output (redacted)
# -----------------------
#  gathered:
#    processes:
#    - process_id: "100"
#      router_id: 203.0.113.20
#    - address_family:
#        afi: ipv4
#        safi: unicast
#        areas:
#        - area_id: 0.0.0.100
#          filter_list:
#          - direction: out
#            route_map: rmap_2
#          - direction: in
#            route_map: rmap_1
#          ranges:
#          - not_advertise: true
#            prefix: 2001:db2::/32
#          - cost: 120
#            prefix: 2001:db3::/32
#        redistribute:
#        - protocol: direct
#          route_map: ospf102-direct-connect
#        - id: "120"
#          protocol: eigrp
#          route_map: rmap_1
#      process_id: "102"
#      router_id: 198.51.100.1
#      vrfs:
#      - areas:
#        - area_id: 0.0.0.102
#          nssa:
#            default_information_originate: true
#            no_summary: true
#        - area_id: 0.0.0.103
#          nssa:
#            no_summary: true
#            translate:
#              type7:
#                always: true
#        router_id: 198.51.100.129
#        vrf: zone1
#      - auto_cost:
#          reference_bandwidth: 45
#          unit: Gbps
#        vrf: zone2
#
```

## [Return Values](nxos_ospfv3_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["router ospfv3 102", "router-id 198.54.100.1", "router ospfv3 100", "router-id 192.0.100.1", "address-family ipv6 unicast", "redistribute eigrp 120 route-map rmap_1", "redistribute direct route-map ospf-direct-connect", "area 0.0.0.100 filter-list route-map rmap_1 in", "area 0.0.0.100 filter-list route-map rmap_2 out", "area 0.0.0.100 range 2001:db2::/32 not-advertise", "area 0.0.0.100 range 2001:db3::/32 cost 120", "vrf zone1", "router-id 192.0.100.2", "vrf zone2", "auto-cost reference-bandwidth 45 Gbps"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
