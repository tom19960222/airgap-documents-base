---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_ospfv2 module – OSPFv2 resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_ospfv2_module.html
fetched_at: 2026-07-28T01:38:58+00:00
---
# cisco.nxos.nxos_ospfv2 module – OSPFv2 resource module

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
> To use it in a playbook, specify: `cisco.nxos.nxos_ospfv2`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_ospfv2_module.md#synopsis)
- [Parameters](nxos_ospfv2_module.md#parameters)
- [Notes](nxos_ospfv2_module.md#notes)
- [Examples](nxos_ospfv2_module.md#examples)
- [Return Values](nxos_ospfv2_module.md#return-values)

## [Synopsis](nxos_ospfv2_module.md#id1)

- This module manages OSPFv2 configuration on devices running Cisco NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: ospfv2

## [Parameters](nxos_ospfv2_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of OSPF process configuration. |
| **processes**  list / elements=dictionary | A list of OSPF instances’ configurations. |
| **areas**  list / elements=dictionary | Configure properties of OSPF Areas. |
| **area_id**  string / required | The Area ID in IP Address format. |
| **authentication**  dictionary | Authentication settings for the Area. |
| **message_digest**  boolean | Use message-digest authentication.  **Choices:**   - `false` - `true` |
| **set**  boolean | Set authentication for the area.  **Choices:**   - `false` - `true` |
| **default_cost**  integer | Specify the default cost for default summary LSA. |
| **filter_list**  list / elements=dictionary | Filter prefixes between OSPF areas. |
| **direction**  string / required | The direction to apply the route map.  **Choices:**   - `"in"` - `"out"` |
| **route_map**  string / required | The Route-map name. |
| **nssa**  dictionary | NSSA settings for the area. |
| **default_information_originate**  boolean | Originate Type-7 default LSA into NSSA area.  **Choices:**   - `false` - `true` |
| **no_redistribution**  boolean | Do not send redistributed LSAs into NSSA area.  **Choices:**   - `false` - `true` |
| **no_summary**  boolean | Do not send summary LSAs into NSSA area.  **Choices:**   - `false` - `true` |
| **set**  boolean | Configure area as NSSA.  **Choices:**   - `false` - `true` |
| **translate**  dictionary | Translate LSA. |
| **type7**  dictionary | Translate from Type 7 to Type 5. |
| **always**  boolean | Always translate LSAs  **Choices:**   - `false` - `true` |
| **never**  boolean | Never translate LSAs  **Choices:**   - `false` - `true` |
| **supress_fa**  boolean | Suppress forwarding address in translated LSAs.  **Choices:**   - `false` - `true` |
| **ranges**  list / elements=dictionary | Configure an address range for the area. |
| **cost**  integer | Cost to use for the range. |
| **not_advertise**  boolean | Suppress advertising the specified range.  **Choices:**   - `false` - `true` |
| **prefix**  string / required | IP in Prefix format (x.x.x.x/len) |
| **stub**  dictionary | Settings for configuring the area as a stub. |
| **no_summary**  boolean | Prevent ABR from sending summary LSAs into stub area.  **Choices:**   - `false` - `true` |
| **set**  boolean | Configure the area as a stub.  **Choices:**   - `false` - `true` |
| **auto_cost**  dictionary | Calculate OSPF cost according to bandwidth. |
| **reference_bandwidth**  integer / required | Reference bandwidth used to assign OSPF cost. |
| **unit**  string / required | Specify in which unit the reference bandwidth is specified.  **Choices:**   - `"Gbps"` - `"Mbps"` |
| **bfd**  boolean | Enable BFD on all OSPF interfaces.  **Choices:**   - `false` - `true` |
| **default_information**  dictionary | Control distribution of default routes. |
| **originate**  dictionary | Distribute a default route. |
| **always**  boolean | Always advertise a default route.  **Choices:**   - `false` - `true` |
| **route_map**  string | Policy to control distribution of default routes |
| **set**  boolean | Enable distribution of default route.  **Choices:**   - `false` - `true` |
| **default_metric**  integer | Specify default metric for redistributed routes. |
| **distance**  integer | Configure the OSPF administrative distance. |
| **flush_routes**  boolean | Flush routes on a non-graceful controlled restart.  **Choices:**   - `false` - `true` |
| **graceful_restart**  dictionary | Configure graceful restart. |
| **grace_period**  integer | Configure maximum interval to restart gracefully. |
| **helper_disable**  boolean | Enable/Disable helper mode.  **Choices:**   - `false` - `true` |
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
| **include_stub**  boolean | Advertise Max metric for Stub links as well.  **Choices:**   - `false` - `true` |
| **on_startup**  dictionary | Effective only at startup. |
| **set**  boolean | Set on-startup attribute.  **Choices:**   - `false` - `true` |
| **wait_for_bgp_asn**  integer | ASN of BGP to wait for. |
| **wait_period**  integer | Wait period in seconds after startup. |
| **set**  boolean | Set router-lsa attribute.  **Choices:**   - `false` - `true` |
| **summary_lsa**  dictionary | Summary LSAs configuration. |
| **max_metric_value**  integer | Max metric value for summary LSAs. |
| **set**  boolean | Set summary-lsa attribute.  **Choices:**   - `false` - `true` |
| **maximum_paths**  integer | Maximum paths per destination. |
| **mpls**  dictionary | OSPF MPLS configuration settings. |
| **traffic_eng**  dictionary | OSPF MPLS Traffic Engineering commands. |
| **areas**  list / elements=dictionary | List of Area IDs. |
| **area_id**  string | Area Id in ip address format. |
| **multicast_intact**  boolean | MPLS TE multicast support.  **Choices:**   - `false` - `true` |
| **router_id**  string | Router ID associated with TE. |
| **name_lookup**  boolean | Display OSPF router ids as DNS names.  **Choices:**   - `false` - `true` |
| **passive_interface**  dictionary | Suppress routing updates on the interface. |
| **default**  boolean | Interfaces passive by default.  **Choices:**   - `false` - `true` |
| **process_id**  string / required | The OSPF process tag. |
| **redistribute**  list / elements=dictionary | Redistribute information from another routing protocol. |
| **id**  string | The identifier for the protocol specified. |
| **protocol**  string / required | The name of the protocol.  **Choices:**   - `"bgp"` - `"direct"` - `"eigrp"` - `"isis"` - `"lisp"` - `"ospf"` - `"rip"` - `"static"` |
| **route_map**  string / required | The route map policy to constrain redistribution. |
| **rfc1583compatibility**  boolean | Configure 1583 compatibility for external path preferences.  **Choices:**   - `false` - `true` |
| **router_id**  string | Set OSPF process router-id. |
| **shutdown**  boolean | Shutdown the OSPF protocol instance.  **Choices:**   - `false` - `true` |
| **summary_address**  list / elements=dictionary | Configure route summarization for redistribution. |
| **not_advertise**  boolean | Suppress advertising the specified summary.  **Choices:**   - `false` - `true` |
| **prefix**  string / required | IP prefix in format x.x.x.x/ml. |
| **tag**  integer | A 32-bit tag value. |
| **table_map**  dictionary | Policy for filtering/modifying OSPF routes before sending them to RIB. |
| **filter**  boolean | Block the OSPF routes from being sent to RIB.  **Choices:**   - `false` - `true` |
| **name**  string / required | The Route Map name. |
| **timers**  dictionary | Configure timer related constants. |
| **lsa_arrival**  integer | Mimimum interval between arrival of a LSA. |
| **lsa_group_pacing**  integer | LSA group refresh/maxage interval. |
| **throttle**  dictionary | Configure throttle related constants. |
| **lsa**  dictionary | Set rate-limiting for LSA generation. |
| **hold_interval**  integer | The hold interval. |
| **max_interval**  integer | The max interval. |
| **start_interval**  integer | The start interval. |
| **spf**  dictionary | Set OSPF SPF timers. |
| **initial_spf_delay**  integer | Initial SPF schedule delay in milliseconds. |
| **max_wait_time**  integer | Maximum wait time between SPF calculations. |
| **min_hold_time**  integer | Minimum hold time between SPF calculations. |
| **vrfs**  list / elements=dictionary | Configure VRF specific OSPF settings. |
| **areas**  list / elements=dictionary | Configure properties of OSPF Areas. |
| **area_id**  string / required | The Area ID in IP Address format. |
| **authentication**  dictionary | Authentication settings for the Area. |
| **message_digest**  boolean | Use message-digest authentication.  **Choices:**   - `false` - `true` |
| **set**  boolean | Set authentication for the area.  **Choices:**   - `false` - `true` |
| **default_cost**  integer | Specify the default cost for default summary LSA. |
| **filter_list**  list / elements=dictionary | Filter prefixes between OSPF areas. |
| **direction**  string / required | The direction to apply the route map.  **Choices:**   - `"in"` - `"out"` |
| **route_map**  string / required | The Route-map name. |
| **nssa**  dictionary | NSSA settings for the area. |
| **default_information_originate**  boolean | Originate Type-7 default LSA into NSSA area.  **Choices:**   - `false` - `true` |
| **no_redistribution**  boolean | Do not send redistributed LSAs into NSSA area.  **Choices:**   - `false` - `true` |
| **no_summary**  boolean | Do not send summary LSAs into NSSA area.  **Choices:**   - `false` - `true` |
| **set**  boolean | Configure area as NSSA.  **Choices:**   - `false` - `true` |
| **translate**  dictionary | Translate LSA. |
| **type7**  dictionary | Translate from Type 7 to Type 5. |
| **always**  boolean | Always translate LSAs  **Choices:**   - `false` - `true` |
| **never**  boolean | Never translate LSAs  **Choices:**   - `false` - `true` |
| **supress_fa**  boolean | Suppress forwarding address in translated LSAs.  **Choices:**   - `false` - `true` |
| **ranges**  list / elements=dictionary | Configure an address range for the area. |
| **cost**  integer | Cost to use for the range. |
| **not_advertise**  boolean | Suppress advertising the specified range.  **Choices:**   - `false` - `true` |
| **prefix**  string / required | IP in Prefix format (x.x.x.x/len) |
| **stub**  dictionary | Settings for configuring the area as a stub. |
| **no_summary**  boolean | Prevent ABR from sending summary LSAs into stub area.  **Choices:**   - `false` - `true` |
| **set**  boolean | Configure the area as a stub.  **Choices:**   - `false` - `true` |
| **auto_cost**  dictionary | Calculate OSPF cost according to bandwidth. |
| **reference_bandwidth**  integer / required | Reference bandwidth used to assign OSPF cost. |
| **unit**  string / required | Specify in which unit the reference bandwidth is specified.  **Choices:**   - `"Gbps"` - `"Mbps"` |
| **bfd**  boolean | Enable BFD on all OSPF interfaces.  **Choices:**   - `false` - `true` |
| **capability**  dictionary | OSPF capability settings. |
| **vrf_lite**  dictionary | Enable VRF-lite capability settings. |
| **evpn**  boolean | Ethernet VPN.  **Choices:**   - `false` - `true` |
| **set**  boolean | Enable VRF-lite support.  **Choices:**   - `false` - `true` |
| **default_information**  dictionary | Control distribution of default routes. |
| **originate**  dictionary | Distribute a default route. |
| **always**  boolean | Always advertise a default route.  **Choices:**   - `false` - `true` |
| **route_map**  string | Policy to control distribution of default routes |
| **set**  boolean | Enable distribution of default route.  **Choices:**   - `false` - `true` |
| **default_metric**  integer | Specify default metric for redistributed routes. |
| **distance**  integer | Configure the OSPF administrative distance. |
| **down_bit_ignore**  boolean | Configure a PE router to ignore the DN bit for network summary, external and NSSA external LSA.  **Choices:**   - `false` - `true` |
| **graceful_restart**  dictionary | Configure graceful restart. |
| **grace_period**  integer | Configure maximum interval to restart gracefully. |
| **helper_disable**  boolean | Enable/Disable helper mode.  **Choices:**   - `false` - `true` |
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
| **include_stub**  boolean | Advertise Max metric for Stub links as well.  **Choices:**   - `false` - `true` |
| **on_startup**  dictionary | Effective only at startup. |
| **set**  boolean | Set on-startup attribute.  **Choices:**   - `false` - `true` |
| **wait_for_bgp_asn**  integer | ASN of BGP to wait for. |
| **wait_period**  integer | Wait period in seconds after startup. |
| **set**  boolean | Set router-lsa attribute.  **Choices:**   - `false` - `true` |
| **summary_lsa**  dictionary | Summary LSAs configuration. |
| **max_metric_value**  integer | Max metric value for summary LSAs. |
| **set**  boolean | Set summary-lsa attribute.  **Choices:**   - `false` - `true` |
| **maximum_paths**  integer | Maximum paths per destination. |
| **name_lookup**  boolean | Display OSPF router ids as DNS names.  **Choices:**   - `false` - `true` |
| **passive_interface**  dictionary | Suppress routing updates on the interface. |
| **default**  boolean | Interfaces passive by default.  **Choices:**   - `false` - `true` |
| **redistribute**  list / elements=dictionary | Redistribute information from another routing protocol. |
| **id**  string | The identifier for the protocol specified. |
| **protocol**  string / required | The name of the protocol.  **Choices:**   - `"bgp"` - `"direct"` - `"eigrp"` - `"isis"` - `"lisp"` - `"ospf"` - `"rip"` - `"static"` |
| **route_map**  string / required | The route map policy to constrain redistribution. |
| **rfc1583compatibility**  boolean | Configure 1583 compatibility for external path preferences.  **Choices:**   - `false` - `true` |
| **router_id**  string | Set OSPF process router-id. |
| **shutdown**  boolean | Shutdown the OSPF protocol instance.  **Choices:**   - `false` - `true` |
| **summary_address**  list / elements=dictionary | Configure route summarization for redistribution. |
| **not_advertise**  boolean | Suppress advertising the specified summary.  **Choices:**   - `false` - `true` |
| **prefix**  string / required | IP prefix in format x.x.x.x/ml. |
| **tag**  integer | A 32-bit tag value. |
| **table_map**  dictionary | Policy for filtering/modifying OSPF routes before sending them to RIB. |
| **filter**  boolean | Block the OSPF routes from being sent to RIB.  **Choices:**   - `false` - `true` |
| **name**  string / required | The Route Map name. |
| **timers**  dictionary | Configure timer related constants. |
| **lsa_arrival**  integer | Mimimum interval between arrival of a LSA. |
| **lsa_group_pacing**  integer | LSA group refresh/maxage interval. |
| **throttle**  dictionary | Configure throttle related constants. |
| **lsa**  dictionary | Set rate-limiting for LSA generation. |
| **hold_interval**  integer | The hold interval. |
| **max_interval**  integer | The max interval. |
| **start_interval**  integer | The start interval. |
| **spf**  dictionary | Set OSPF SPF timers. |
| **initial_spf_delay**  integer | Initial SPF schedule delay in milliseconds. |
| **max_wait_time**  integer | Maximum wait time between SPF calculations. |
| **min_hold_time**  integer | Minimum hold time between SPF calculations. |
| **vrf**  string / required | Name/Identifier of the VRF. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section “^router ospf .\*”**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"parsed"` - `"rendered"` |

## [Notes](nxos_ospfv2_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 7.0(3)I5(1).
> - Unsupported for Cisco MDS
> - This module works with connection `network_cli` and `httpapi`.

## [Examples](nxos_ospfv2_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# nxos-9k-rdo# sh running-config | section "^router ospf .*"
# nxos-9k-rdo#

- name: Merge the provided configuration with the existing running configuration
  cisco.nxos.nxos_ospfv2:
    config:
      processes:
      - process_id: 100
        router_id: 203.0.113.20
      - process_id: 102
        router_id: 198.51.100.1
        areas:
        - area_id: 0.0.0.100
          filter_list:
          - route_map: rmap_1
            direction: in
          - route_map: rmap_2
            direction: out
          ranges:
          - prefix: 198.51.100.64/27
            not_advertise: true
          - prefix: 198.51.100.96/27
            cost: 120
        - area_id: 0.0.0.101
          authentication:
            message_digest: true
        redistribute:
        - protocol: eigrp
          id: 120
          route_map: rmap_1
        - protocol: direct
          route_map: ospf102-direct-connect
        vrfs:
        - vrf: zone1
          router_id: 198.51.100.129
          redistribute:
          - protocol: static
            route_map: zone1-static-connect
          summary_address:
          - prefix: 198.51.100.128/27
            tag: 121
          - prefix: 198.51.100.160/27
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
#  - redistribute eigrp 120 route-map rmap_1
#  - redistribute direct route-map ospf102-direct-connect
#  - area 0.0.0.100 filter-list route-map rmap_1 in
#  - area 0.0.0.100 filter-list route-map rmap_2 out
#  - area 0.0.0.100 range 198.51.100.64/27 not-advertise
#  - area 0.0.0.100 range 198.51.100.96/27 cost 120
#  - area 0.0.0.101 authentication message-digest
#  - vrf zone1
#  - router-id 198.51.100.129
#  - summary-address 198.51.100.128/27 tag 121
#  - summary-address 198.51.100.160/27
#  - redistribute static route-map zone1-static-connect
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
#    - areas:
#      - area_id: 0.0.0.100
#        filter_list:
#        - direction: out
#          route_map: rmap_2
#        - direction: in
#          route_map: rmap_1
#        ranges:
#        - not_advertise: true
#          prefix: 198.51.100.64/27
#        - cost: 120
#          prefix: 198.51.100.96/27
#      - area_id: 0.0.0.101
#        authentication:
#          message_digest: true
#      process_id: "102"
#      redistribute:
#      - protocol: direct
#        route_map: ospf102-direct-connect
#      - id: "120"
#        protocol: eigrp
#        route_map: rmap_1
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
#        redistribute:
#        - protocol: static
#          route_map: zone1-static-connect
#        router_id: 198.51.100.129
#        vrf: zone1
#      - auto_cost:
#          reference_bandwidth: 45
#          unit: Gbps
#        vrf: zone2
#

# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospf .*"
# router ospf 100
#   router-id 203.0.113.20
# router ospf 102
#   router-id 198.51.100.1
#   redistribute direct route-map ospf102-direct-connect
#   redistribute eigrp 120 route-map rmap_1
#   area 0.0.0.100 filter-list route-map rmap_2 out
#   area 0.0.0.100 filter-list route-map rmap_1 in
#   area 0.0.0.100 range 198.51.100.64/27 not-advertise
#   area 0.0.0.100 range 198.51.100.96/27 cost 120
#   area 0.0.0.101 authentication message-digest
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.0.102 nssa no-summary default-information-originate
#     area 0.0.0.103 nssa no-summary
#     area 0.0.0.103 nssa translate type7 always
#     redistribute static route-map zone1-static-connect
#     summary-address 198.51.100.128/27 tag 121
#     summary-address 198.51.100.160/27
#   vrf zone2
#     auto-cost reference-bandwidth 45 Gbps

# Using replaced

# Before state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospf .*"
# router ospf 100
#   router-id 203.0.113.20
# router ospf 102
#   router-id 198.51.100.1
#   redistribute direct route-map ospf102-direct-connect
#   redistribute eigrp 120 route-map rmap_1
#   area 0.0.0.100 filter-list route-map rmap_2 out
#   area 0.0.0.100 filter-list route-map rmap_1 in
#   area 0.0.0.100 range 198.51.100.64/27 not-advertise
#   area 0.0.0.100 range 198.51.100.96/27 cost 120
#   area 0.0.0.101 authentication message-digest
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.0.102 nssa no-summary default-information-originate
#     area 0.0.0.103 nssa no-summary
#     area 0.0.0.103 nssa translate type7 always
#     redistribute static route-map zone1-static-connect
#     summary-address 198.51.100.128/27 tag 121
#     summary-address 198.51.100.160/27
#   vrf zone2
#     auto-cost reference-bandwidth 45 Gbps

- name: Replace device configurations of listed OSPF processes with provided configurations
  cisco.nxos.nxos_ospfv2:
    config:
      processes:
      - process_id: 102
        router_id: 198.51.100.1
        areas:
        - area_id: 0.0.0.100
          filter_list:
          - route_map: rmap_8
            direction: in
          ranges:
          - prefix: 198.51.100.64/27
            not_advertise: true
        - area_id: 0.0.0.101
          stub:
            no_summary: true
        redistribute:
        - protocol: eigrp
          id: 130
          route_map: rmap_1
        - protocol: direct
          route_map: ospf102-direct-connect
        vrfs:
        - vrf: zone1
          router_id: 198.51.100.129
          redistribute:
          - protocol: bgp
            id: 65563
            route_map: zone1-bgp-connect
          areas:
          - area_id: 0.0.0.102
            nssa:
              default_information_originate: true
              no_summary: true
    state: replaced

# Task output
# -------------
# before:
#    processes:
#    - process_id: "100"
#      router_id: 203.0.113.20
#    - areas:
#      - area_id: 0.0.0.100
#        filter_list:
#        - direction: out
#          route_map: rmap_2
#        - direction: in
#          route_map: rmap_1
#        ranges:
#        - not_advertise: true
#          prefix: 198.51.100.64/27
#        - cost: 120
#          prefix: 198.51.100.96/27
#      - area_id: 0.0.0.101
#        authentication:
#          message_digest: true
#      process_id: "102"
#      redistribute:
#      - protocol: direct
#        route_map: ospf102-direct-connect
#      - id: "120"
#        protocol: eigrp
#        route_map: rmap_1
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
#        redistribute:
#        - protocol: static
#          route_map: zone1-static-connect
#        router_id: 198.51.100.129
#        vrf: zone1
#      - auto_cost:
#          reference_bandwidth: 45
#          unit: Gbps
#        vrf: zone2
#
#  commands:
#  - router ospf 102
#  - redistribute eigrp 130 route-map rmap_1
#  - no redistribute eigrp 120 route-map rmap_1
#  - area 0.0.0.100 filter-list route-map rmap_8 in
#  - no area 0.0.0.100 filter-list route-map rmap_2 out
#  - no area 0.0.0.100 range 198.51.100.96/27
#  - no area 0.0.0.101 authentication
#  - area 0.0.0.101 stub no-summary
#  - vrf zone1
#  - no summary-address 198.51.100.128/27 tag 121
#  - no summary-address 198.51.100.160/27
#  - redistribute bgp 65563 route-map zone1-bgp-connect
#  - no redistribute static route-map zone1-static-connect
#  - no area 0.0.0.103 nssa
#  - no area 0.0.0.103 nssa translate type7 always
#  - no vrf zone2
#
# after:
#    processes:
#    - process_id: "100"
#      router_id: 203.0.113.20
#    - areas:
#      - area_id: 0.0.0.101
#        stub:
#          no_summary: true
#      - area_id: 0.0.0.100
#        filter_list:
#        - direction: in
#          route_map: rmap_8
#        ranges:
#        - not_advertise: true
#          prefix: 198.51.100.64/27
#      process_id: "102"
#      redistribute:
#      - protocol: direct
#        route_map: ospf102-direct-connect
#      - id: "130"
#        protocol: eigrp
#        route_map: rmap_1
#      router_id: 198.51.100.1
#      vrfs:
#      - areas:
#        - area_id: 0.0.0.102
#          nssa:
#            default_information_originate: true
#            no_summary: true
#        redistribute:
#        - id: "65563"
#          protocol: bgp
#          route_map: zone1-bgp-connect
#        router_id: 198.51.100.129
#        vrf: zone1

# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospf .*"
# router ospf 100
#   router-id 203.0.113.20
# router ospf 102
#   router-id 198.51.100.1
#   area 0.0.0.101 stub no-summary
#   redistribute direct route-map ospf102-direct-connect
#   redistribute eigrp 130 route-map rmap_1
#   area 0.0.0.100 filter-list route-map rmap_8 in
#   area 0.0.0.100 range 198.51.100.64/27 not-advertise
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.0.102 nssa no-summary default-information-originate
#     redistribute bgp 65563 route-map zone1-bgp-connect

# Using overridden

# Before state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospf .*"
# router ospf 100
#   router-id 203.0.113.20
# router ospf 102
#   router-id 198.51.100.1
#   redistribute direct route-map ospf102-direct-connect
#   redistribute eigrp 120 route-map rmap_1
#   area 0.0.0.100 filter-list route-map rmap_2 out
#   area 0.0.0.100 filter-list route-map rmap_1 in
#   area 0.0.0.100 range 198.51.100.64/27 not-advertise
#   area 0.0.0.100 range 198.51.100.96/27 cost 120
#   area 0.0.0.101 authentication message-digest
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.0.102 nssa no-summary default-information-originate
#     area 0.0.0.103 nssa no-summary
#     area 0.0.0.103 nssa translate type7 always
#     redistribute static route-map zone1-static-connect
#     summary-address 198.51.100.128/27 tag 121
#     summary-address 198.51.100.160/27
#   vrf zone2
#     auto-cost reference-bandwidth 45 Gbps

- name: Override all OSPF configuration with provided configuration
  cisco.nxos.nxos_ospfv2:
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
#    - areas:
#      - area_id: 0.0.0.100
#        filter_list:
#        - direction: out
#          route_map: rmap_2
#        - direction: in
#          route_map: rmap_1
#        ranges:
#        - not_advertise: true
#          prefix: 198.51.100.64/27
#        - cost: 120
#          prefix: 198.51.100.96/27
#      - area_id: 0.0.0.101
#        authentication:
#          message_digest: true
#      process_id: "102"
#      redistribute:
#      - protocol: direct
#        route_map: ospf102-direct-connect
#      - id: "120"
#        protocol: eigrp
#        route_map: rmap_1
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
#        redistribute:
#        - protocol: static
#          route_map: zone1-static-connect
#        router_id: 198.51.100.129
#        vrf: zone1
#      - auto_cost:
#          reference_bandwidth: 45
#          unit: Gbps
#        vrf: zone2
#
# commands:
#  - no router ospf 100
#  - router ospf 104
#  - router-id 203.0.113.20
#  - router ospf 102
#  - shutdown
#  - no redistribute direct route-map ospf102-direct-connect
#  - no redistribute eigrp 120 route-map rmap_1
#  - no area 0.0.0.100 filter-list route-map rmap_2 out
#  - no area 0.0.0.100 filter-list route-map rmap_1 in
#  - no area 0.0.0.100 range 198.51.100.64/27
#  - no area 0.0.0.100 range 198.51.100.96/27
#  - no area 0.0.0.101 authentication
#  - no vrf zone1
#  - no vrf zone2
#
# after:
#    processes:
#    - process_id: "102"
#      router_id: 198.51.100.1
#      shutdown: true
#    - process_id: "104"
#      router_id: 203.0.113.20

# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospf .*"
# router ospf 102
#   router-id 198.51.100.1
#   shutdown
# router ospf 104
#   router-id 203.0.113.20

# Using deleted to delete a single OSPF process

# Before state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospf .*"
# router ospf 100
#   router-id 203.0.113.20
# router ospf 102
#   router-id 198.51.100.1
#   redistribute direct route-map ospf102-direct-connect
#   redistribute eigrp 120 route-map rmap_1
#   area 0.0.0.100 filter-list route-map rmap_2 out
#   area 0.0.0.100 filter-list route-map rmap_1 in
#   area 0.0.0.100 range 198.51.100.64/27 not-advertise
#   area 0.0.0.100 range 198.51.100.96/27 cost 120
#   area 0.0.0.101 authentication message-digest
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.0.102 nssa no-summary default-information-originate
#     area 0.0.0.103 nssa no-summary
#     area 0.0.0.103 nssa translate type7 always
#     redistribute static route-map zone1-static-connect
#     summary-address 198.51.100.128/27 tag 121
#     summary-address 198.51.100.160/27
#   vrf zone2
#     auto-cost reference-bandwidth 45 Gbps

- name: Delete a single OSPF process
  cisco.nxos.nxos_ospfv2:
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
#    - areas:
#      - area_id: 0.0.0.100
#        filter_list:
#        - direction: out
#          route_map: rmap_2
#        - direction: in
#          route_map: rmap_1
#        ranges:
#        - not_advertise: true
#          prefix: 198.51.100.64/27
#        - cost: 120
#          prefix: 198.51.100.96/27
#      - area_id: 0.0.0.101
#        authentication:
#          message_digest: true
#      process_id: "102"
#      redistribute:
#      - protocol: direct
#        route_map: ospf102-direct-connect
#      - id: "120"
#        protocol: eigrp
#        route_map: rmap_1
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
#        redistribute:
#        - protocol: static
#          route_map: zone1-static-connect
#        router_id: 198.51.100.129
#        vrf: zone1
#      - auto_cost:
#          reference_bandwidth: 45
#          unit: Gbps
#        vrf: zone2
#
# commands:
#  - no router ospf 102
#
# after:
#   processes:
#   - process_id: "100"
#     router_id: 203.0.113.20

# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospf .*"
# router ospf 100
#   router-id 203.0.113.20

# Using deleted all OSPF processes from the device

# Before state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospf .*"
# router ospf 100
#   router-id 203.0.113.20
# router ospf 102
#   router-id 198.51.100.1
#   redistribute direct route-map ospf102-direct-connect
#   redistribute eigrp 120 route-map rmap_1
#   area 0.0.0.100 filter-list route-map rmap_2 out
#   area 0.0.0.100 filter-list route-map rmap_1 in
#   area 0.0.0.100 range 198.51.100.64/27 not-advertise
#   area 0.0.0.100 range 198.51.100.96/27 cost 120
#   area 0.0.0.101 authentication message-digest
#   vrf zone1
#     router-id 198.51.100.129
#     area 0.0.0.102 nssa no-summary default-information-originate
#     area 0.0.0.103 nssa no-summary
#     area 0.0.0.103 nssa translate type7 always
#     redistribute static route-map zone1-static-connect
#     summary-address 198.51.100.128/27 tag 121
#     summary-address 198.51.100.160/27
#   vrf zone2
#     auto-cost reference-bandwidth 45 Gbps

- name: Delete all OSPF processes from the device
  cisco.nxos.nxos_ospfv2:
    state: deleted

# Task output
# -------------
# before:
#    processes:
#    - process_id: "100"
#      router_id: 203.0.113.20
#    - areas:
#      - area_id: 0.0.0.100
#        filter_list:
#        - direction: out
#          route_map: rmap_2
#        - direction: in
#          route_map: rmap_1
#        ranges:
#        - not_advertise: true
#          prefix: 198.51.100.64/27
#        - cost: 120
#          prefix: 198.51.100.96/27
#      - area_id: 0.0.0.101
#        authentication:
#          message_digest: true
#      process_id: "102"
#      redistribute:
#      - protocol: direct
#        route_map: ospf102-direct-connect
#      - id: "120"
#        protocol: eigrp
#        route_map: rmap_1
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
#        redistribute:
#        - protocol: static
#          route_map: zone1-static-connect
#        router_id: 198.51.100.129
#        vrf: zone1
#      - auto_cost:
#          reference_bandwidth: 45
#          unit: Gbps
#        vrf: zone2
#
# commands:
#  - no router ospf 100
#  - no router ospf 102
#
#  after: {}

# After state:
# ------------
# nxos-9k-rdo# sh running-config | section "^router ospf .*"
# nxos-9k-rdo#

# Using rendered

- name: Render platform specific configuration lines (without connecting to the device)
  cisco.nxos.nxos_ospfv2:
    config:
      processes:
      - process_id: 100
        router_id: 203.0.113.20
      - process_id: 102
        router_id: 198.51.100.1
        areas:
        - area_id: 0.0.0.100
          filter_list:
          - route_map: rmap_1
            direction: in
          - route_map: rmap_2
            direction: out
          ranges:
          - prefix: 198.51.100.64/27
            not_advertise: true
          - prefix: 198.51.100.96/27
            cost: 120
        - area_id: 0.0.0.101
          authentication:
            message_digest: true
        redistribute:
        - protocol: eigrp
          id: 120
          route_map: rmap_1
        - protocol: direct
          route_map: ospf102-direct-connect
        vrfs:
        - vrf: zone1
          router_id: 198.51.100.129
          redistribute:
          - protocol: static
            route_map: zone1-static-connect
          summary_address:
          - prefix: 198.51.100.128/27
            tag: 121
          - prefix: 198.51.100.160/27
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
#  - router ospf 100
#  - router-id 203.0.113.20
#  - router ospf 102
#  - router-id 198.51.100.1
#  - redistribute eigrp 120 route-map rmap_1
#  - redistribute direct route-map ospf102-direct-connect
#  - area 0.0.0.100 filter-list route-map rmap_1 in
#  - area 0.0.0.100 filter-list route-map rmap_2 out
#  - area 0.0.0.100 range 198.51.100.64/27 not-advertise
#  - area 0.0.0.100 range 198.51.100.96/27 cost 120
#  - area 0.0.0.101 authentication message-digest
#  - vrf zone1
#  - router-id 198.51.100.129
#  - summary-address 198.51.100.128/27 tag 121
#  - summary-address 198.51.100.160/27
#  - redistribute static route-map zone1-static-connect
#  - area 0.0.0.102 nssa no-summary default-information-originate
#  - area 0.0.0.103 nssa no-summary
#  - area 0.0.0.103 nssa translate type7 always
#  - vrf zone2
#  - auto-cost reference-bandwidth 45 Gbps

# Using parsed

# parsed.cfg
# ------------
# router ospf 100
#   router-id 192.0.100.1
#   area 0.0.0.101 nssa no-summary no-redistribution
#   area 0.0.0.102 stub no-summary
#   redistribute direct route-map ospf-direct-connect
#   redistribute eigrp 120 route-map rmap_1
#   area 0.0.0.100 filter-list route-map rmap_2 out
#   area 0.0.0.100 filter-list route-map rmap_1 in
#   area 0.0.0.100 range 192.0.2.0/24 not-advertise
#   area 0.0.0.100 range 192.0.3.0/24 cost 120
#   area 0.0.0.100 authentication message-digest
#   vrf zone1
#     router-id 192.0.100.2
#     area 0.0.100.1 nssa no-summary no-redistribution
#     redistribute static route-map zone1-direct-connect
#     summary-address 10.0.0.0/24 tag 120
#     summary-address 11.0.0.0/24 not-advertise
#   vrf zone2
#     auto-cost reference-bandwidth 45 Gbps
#     down-bit-ignore
#     capability vrf-lite evpn
#     shutdown
# router ospf 102
#   router-id 198.54.100.1
#   shutdown
#   vrf zone2
#     summary-address 192.0.8.0/24 tag 120
#   vrf zone4
#     shutdown

- name: Parse externally provided OSPFv2 config
  cisco.nxos.nxos_ospfv2:
    running_config: "{{ lookup('file', 'ospfv2.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
# parsed:
#   processes:
#   - process_id: "100"
#     areas:
#       - area_id: 0.0.0.101
#         nssa:
#           no_redistribution: true
#           no_summary: true
#       - area_id: 0.0.0.102
#         stub:
#           no_summary: true
#       - area_id: 0.0.0.100
#         authentication:
#           message_digest: true
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
#     redistribute:
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
#         redistribute:
#           - protocol: static
#             route_map: zone1-direct-connect
#         router_id: 192.0.100.2
#         summary_address:
#           - prefix: 10.0.0.0/24
#             tag: 120
#           - not_advertise: true
#             prefix: 11.0.0.0/24
#       - vrf: zone2
#         auto_cost:
#           reference_bandwidth: 45
#           unit: Gbps
#         capability:
#           vrf_lite:
#             evpn: true
#         down_bit_ignore: true
#         shutdown: true
#   - process_id: "102"
#     router_id: 198.54.100.1
#     shutdown: true
#     vrfs:
#       - vrf: zone2
#         summary_address:
#           - prefix: 192.0.8.0/24
#             tag: 120
#       - vrf: zone4
#         shutdown: true

# Using gathered

- name: Gather OSPFv2 facts using gathered
  cisco.nxos.nxos_ospfv2:
    state: gathered

# Task output (redacted)
# -----------------------
#  gathered:
#    processes:
#      - process_id: "102"
#        areas:
#          - area_id: 0.0.0.101
#            stub:
#              no_summary: true
#          - area_id: 0.0.0.100
#            filter_list:
#              - direction: in
#                route_map: rmap_8
#            ranges:
#              - not_advertise: true
#                prefix: 198.51.100.64/27
#        redistribute:
#          - protocol: direct
#            route_map: ospf102-direct-connect
#          - id: "130"
#            protocol: eigrp
#            route_map: rmap_1
#        router_id: 198.51.100.1
#        vrfs:
#          - vrf: zone1
#            areas:
#              - area_id: 0.0.0.102
#                nssa:
#                  default_information_originate: true
#                  no_summary: true
#            redistribute:
#             - id: "65563"
#               protocol: bgp
#               route_map: zone1-bgp-connect
#            router_id: 198.51.100.129
#
```

## [Return Values](nxos_ospfv2_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  dictionary | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **before**  dictionary | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `"The configuration returned will always be in the same format\n of the parameters above.\n"` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["router ospf 102", "router-id 198.54.100.1", "router ospf 100", "router-id 192.0.100.1", "redistribute eigrp 120 route-map rmap_1", "redistribute direct route-map ospf-direct-connect", "area 0.0.0.100 filter-list route-map rmap_1 in", "area 0.0.0.100 filter-list route-map rmap_2 out", "area 0.0.0.100 range 192.0.2.0/24 not-advertise", "area 0.0.0.100 range 192.0.3.0/24 cost 120", "vrf zone1", "router-id 192.0.100.2", "summary-address 10.0.0.0/24 tag 121", "summary-address 11.0.0.0/24", "redistribute static route-map zone1-direct-connect", "vrf zone2", "auto-cost reference-bandwidth 45 Gbps", "capability vrf-lite evpn"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
