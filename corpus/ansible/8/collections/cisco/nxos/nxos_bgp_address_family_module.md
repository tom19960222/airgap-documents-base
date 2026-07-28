---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_bgp_address_family module – BGP Address Family resource module."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_bgp_address_family_module.html
fetched_at: 2026-07-28T01:38:31+00:00
---
# cisco.nxos.nxos_bgp_address_family module – BGP Address Family resource module.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_bgp_address_family`.

New in cisco.nxos 2.0.0

- [Synopsis](nxos_bgp_address_family_module.md#synopsis)
- [Parameters](nxos_bgp_address_family_module.md#parameters)
- [Notes](nxos_bgp_address_family_module.md#notes)
- [Examples](nxos_bgp_address_family_module.md#examples)

## [Synopsis](nxos_bgp_address_family_module.md#id1)

- This module manages BGP Address Family configuration on devices running Cisco NX-OS.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: bgp_address_family

## [Parameters](nxos_bgp_address_family_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of BGP process configuration. |
| **address_family**  list / elements=dictionary | Address Family related configurations. |
| **additional_paths**  dictionary | Additional paths configuration. |
| **install_backup**  boolean | Install backup path.  **Choices:**   - `false` - `true` |
| **receive**  boolean | Additional paths Receive capability.  **Choices:**   - `false` - `true` |
| **selection**  dictionary | Additional paths selection |
| **route_map**  string | Route-map for additional paths selection |
| **send**  boolean | Additional paths Send capability  **Choices:**   - `false` - `true` |
| **advertise_l2vpn_evpn**  boolean | Enable advertising EVPN routes.  **Choices:**   - `false` - `true` |
| **advertise_pip**  boolean | Advertise physical ip for type-5 route.  **Choices:**   - `false` - `true` |
| **advertise_system_mac**  boolean | Advertise extra EVPN RT-2 with system MAC.  **Choices:**   - `false` - `true` |
| **afi**  string / required | Address Family indicator.  **Choices:**   - `"ipv4"` - `"ipv6"` - `"link-state"` - `"vpnv4"` - `"vpnv6"` - `"l2vpn"` |
| **aggregate_address**  list / elements=dictionary | Configure BGP aggregate prefixes |
| **advertise_map**  string | Select attribute information from specific routes. |
| **as_set**  boolean | Generate AS-SET information.  **Choices:**   - `false` - `true` |
| **attribute_map**  string | Set attribute information of aggregate. |
| **prefix**  string | Aggregate prefix. |
| **summary_only**  boolean | Do not advertise more specifics.  **Choices:**   - `false` - `true` |
| **suppress_map**  string | Conditionally filter more specific routes. |
| **allow_vni_in_ethertag**  boolean | Allow VNI in Ethernet Tag field in EVPN route.  **Choices:**   - `false` - `true` |
| **client_to_client**  dictionary | Configure client-to-client route reflection. |
| **no_reflection**  boolean | Reflection of routes permitted.  **Choices:**   - `false` - `true` |
| **dampen_igp_metric**  integer | Dampen IGP metric-related changes. |
| **dampening**  dictionary | Configure route flap dampening. |
| **decay_half_life**  integer | Decay half life. |
| **max_suppress_time**  integer | Maximum suppress time for stable route. |
| **route_map**  string | Apply route-map to specify dampening criteria. |
| **set**  boolean | Set route flap dampening.  **Choices:**   - `false` - `true` |
| **start_reuse_route**  integer | Value to start reusing a route. |
| **start_suppress_route**  integer | Value to start suppressing a route. |
| **default_information**  dictionary | Control distribution of default information. |
| **originate**  boolean | Distribute a default route.  **Choices:**   - `false` - `true` |
| **default_metric**  integer | Set metric of redistributed routes. |
| **distance**  dictionary | Configure administrative distance. |
| **ebgp_routes**  integer | Distance for EBGP routes. |
| **ibgp_routes**  integer | Distance for IBGP routes. |
| **local_routes**  integer | Distance for local routes. |
| **export_gateway_ip**  boolean | Export Gateway IP to Type-5 EVPN routes for VRF  **Choices:**   - `false` - `true` |
| **inject_map**  list / elements=dictionary | Routemap which specifies prefixes to inject. |
| **copy_attributes**  boolean | Copy attributes from aggregate.  **Choices:**   - `false` - `true` |
| **exist_map**  string | Routemap which specifies exist condition. |
| **route_map**  string | Route-map name. |
| **maximum_paths**  dictionary | Forward packets over multipath paths. |
| **eibgp**  dictionary | Configure multipath for both EBGP and IBGP paths. |
| **parallel_paths**  integer | Number of parallel paths. |
| **ibgp**  dictionary | Configure multipath for IBGP paths. |
| **parallel_paths**  integer | Number of parallel paths. |
| **local**  dictionary | Configure multipath for local paths. |
| **parallel_paths**  integer | Number of parallel paths. |
| **mixed**  dictionary | Configure multipath for local and remote paths. |
| **parallel_paths**  integer | Number of parallel paths. |
| **parallel_paths**  integer | Number of parallel paths. |
| **networks**  list / elements=dictionary | Configure an IP prefix to advertise. |
| **prefix**  string | IP prefix in CIDR format. |
| **route_map**  string | Route-map name. |
| **nexthop**  dictionary | Nexthop tracking. |
| **route_map**  string | Route-map name. |
| **trigger_delay**  dictionary | Set the delay to trigger nexthop tracking. |
| **critical_delay**  integer | Nexthop changes affecting reachability.  Delay value (miliseconds). |
| **non_critical_delay**  integer | Other nexthop changes.  Delay value (miliseconds). |
| **redistribute**  list / elements=dictionary | Configure redistribution. |
| **id**  string | The identifier for the protocol specified. |
| **protocol**  string / required | The name of the protocol.  **Choices:**   - `"am"` - `"direct"` - `"eigrp"` - `"isis"` - `"lisp"` - `"ospf"` - `"ospfv3"` - `"rip"` - `"static"` - `"hmm"` |
| **route_map**  string / required | The route map policy to constrain redistribution. |
| **retain**  dictionary | Retain the routes based on Target VPN Extended Communities. |
| **route_target**  dictionary | Specify Target VPN Extended Communities |
| **retain_all**  boolean | All the routes regardless of Target-VPN community  **Choices:**   - `false` - `true` |
| **route_map**  string | Apply route-map to filter routes. |
| **safi**  string | Sub Address Family indicator.  **Choices:**   - `"unicast"` - `"multicast"` - `"mvpn"` - `"evpn"` |
| **suppress_inactive**  boolean | Advertise only active routes to peers.  **Choices:**   - `false` - `true` |
| **table_map**  dictionary | Policy for filtering/modifying OSPF routes before sending them to RIB. |
| **filter**  boolean | Block the OSPF routes from being sent to RIB.  **Choices:**   - `false` - `true` |
| **name**  string / required | The Route Map name. |
| **timers**  dictionary | Configure bgp related timers. |
| **bestpath_defer**  dictionary | Configure bestpath defer timer value for batch prefix processing. |
| **defer_time**  integer | Bestpath defer time (mseconds). |
| **maximum_defer_time**  integer | Maximum bestpath defer time (mseconds). |
| **vrf**  string | Virtual Router Context. |
| **wait_igp_convergence**  boolean | Delay initial bestpath until redistributed IGPs have converged.  **Choices:**   - `false` - `true` |
| **as_number**  string | Autonomous System Number of the router. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ‘^router bgp’**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  State *deleted* only removes BGP attributes that this modules manages and does not negate the BGP process completely.  Refer to examples for more details.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](nxos_bgp_address_family_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 9.3.6.
> - Unsupported for Cisco MDS
> - For managing BGP neighbor address family configurations please use the [cisco.nxos.nxos_bgp_neighbor_address_family](nxos_bgp_neighbor_address_family_module.md#ansible-collections-cisco-nxos-nxos-bgp-neighbor-address-family-module) module.
> - This module works with connection `network_cli` and `httpapi`.

## [Examples](nxos_bgp_address_family_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# Nexus9000v#

- name: Merge the provided configuration with the existing running configuration
  cisco.nxos.nxos_bgp_address_family:
    config:
      as_number: 65536
      address_family:
        - afi: ipv4
          safi: multicast
          networks:
            - prefix: 192.0.2.32/27
            - prefix: 192.0.2.64/27
              route_map: rmap1
          nexthop:
            route_map: rmap2
            trigger_delay:
              critical_delay: 120
              non_critical_delay: 180
        - afi: ipv4
          safi: unicast
          vrf: site-1
          default_information:
            originate: True
          aggregate_address:
            - prefix: 203.0.113.0/24
              as_set: True
              summary_only: True
        - afi: ipv6
          safi: multicast
          vrf: site-1
          redistribute:
            - protocol: ospfv3
              id: 100
              route_map: rmap-ospf-1
            - protocol: eigrp
              id: 101
              route_map: rmap-eigrp-1

# Task output
# -------------
#  before: {}
#
#  commands:
#  - router bgp 65536
#  - address-family ipv4 multicast
#  - nexthop route-map rmap2
#  - nexthop trigger-delay critical 120 non-critical 180
#  - network 192.0.2.32/27
#  - network 192.0.2.64/27 route-map rmap1
#  - vrf site-1
#  - address-family ipv4 unicast
#  - default-information originate
#  - aggregate-address 203.0.113.0/24 as-set summary-only
#  - address-family ipv6 multicast
#  - redistribute ospfv3 100 route-map rmap-ospf-1
#  - redistribute eigrp 101 route-map rmap-eigrp-1
#
#  after:
#    as_number: "65536"
#    address_family:
#      - afi: ipv4
#        safi: multicast
#        networks:
#          - prefix: 192.0.2.32/27
#          - prefix: 192.0.2.64/27
#            route_map: rmap1
#        nexthop:
#          route_map: rmap2
#          trigger_delay:
#            critical_delay: 120
#            non_critical_delay: 180
#      - afi: ipv4
#        safi: unicast
#        vrf: site-1
#        default_information:
#          originate: True
#        aggregate_address:
#          - prefix: 203.0.113.0/24
#            as_set: True
#            summary_only: True
#      - afi: ipv6
#        safi: multicast
#        vrf: site-1
#        redistribute:
#          - id: "100"
#            protocol: ospfv3
#            route_map: rmap-ospf-1
#          - id: "101"
#            protocol: eigrp
#            route_map: rmap-eigrp-1

# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   address-family ipv4 multicast
#     nexthop route-map rmap2
#     nexthop trigger-delay critical 120 non-critical 180
#     network 192.0.2.32/27
#     network 192.0.2.64/27 route-map rmap1
#   vrf site-1
#     address-family ipv4 unicast
#       default-information originate
#       aggregate-address 203.0.113.0/24 as-set summary-only
#     address-family ipv6 multicast
#       redistribute ospfv3 100 route-map rmap-ospf-1
#       redistribute eigrp 101 route-map rmap-eigrp-1
#

# Using replaced

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   address-family ipv4 multicast
#     nexthop route-map rmap2
#     nexthop trigger-delay critical 120 non-critical 180
#     network 192.0.2.32/27
#     network 192.0.2.64/27 route-map rmap1
#   vrf site-1
#     address-family ipv4 unicast
#       default-information originate
#       aggregate-address 203.0.113.0/24 as-set summary-only
#     address-family ipv6 multicast
#       redistribute ospfv3 100 route-map rmap-ospf-1
#       redistribute eigrp 101 route-map rmap-eigrp-1

- name: Replace configuration of specified AFs
  cisco.nxos.nxos_bgp_address_family:
    config:
      as_number: 65536
      address_family:
        - afi: ipv4
          safi: multicast
          networks:
            - prefix: 192.0.2.64/27
              route_map: rmap1
          nexthop:
            route_map: rmap2
            trigger_delay:
              critical_delay: 120
              non_critical_delay: 180
          aggregate_address:
            - prefix: 203.0.113.0/24
              as_set: True
              summary_only: True
        - afi: ipv4
          safi: unicast
          vrf: site-1
    state: replaced

# Task output
# -------------
#  before:
#    as_number: "65536"
#    address_family:
#      - afi: ipv4
#        safi: multicast
#        networks:
#          - prefix: 192.0.2.32/27
#          - prefix: 192.0.2.64/27
#            route_map: rmap1
#        nexthop:
#          route_map: rmap2
#          trigger_delay:
#            critical_delay: 120
#            non_critical_delay: 180
#      - afi: ipv4
#        safi: unicast
#        vrf: site-1
#        default_information:
#          originate: True
#        aggregate_address:
#          - prefix: 203.0.113.0/24
#            as_set: True
#            summary_only: True
#      - afi: ipv6
#        safi: multicast
#        vrf: site-1
#        redistribute:
#          - id: "100"
#            protocol: ospfv3
#            route_map: rmap-ospf-1
#          - id: "101"
#            protocol: eigrp
#            route_map: rmap-eigrp-1
#
#  commands:
#  - router bgp 65536
#  - address-family ipv4 multicast
#  - no network 192.0.2.32/27
#  - aggregate-address 203.0.113.0/24 as-set summary-only
#  - vrf site-1
#  - address-family ipv4 unicast
#  - no default-information originate
#  - no aggregate-address 203.0.113.0/24 as-set summary-only
#
#  after:
#    as_number: "65536"
#    address_family:
#      - afi: ipv4
#        safi: multicast
#        networks:
#          - prefix: 192.0.2.64/27
#            route_map: rmap1
#        nexthop:
#          route_map: rmap2
#          trigger_delay:
#            critical_delay: 120
#            non_critical_delay: 180
#        aggregate_address:
#          - prefix: 203.0.113.0/24
#            as_set: True
#            summary_only: True
#
#      - afi: ipv4
#        safi: unicast
#        vrf: site-1
#
#      - afi: ipv6
#        safi: multicast
#        vrf: site-1
#        redistribute:
#          - protocol: ospfv3
#            id: "100"
#            route_map: rmap-ospf-1
#          - protocol: eigrp
#            id: "101"
#            route_map: rmap-eigrp-1

# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   address-family ipv4 multicast
#     nexthop route-map rmap2
#     nexthop trigger-delay critical 120 non-critical 180
#     network 192.0.2.64/27 route-map rmap1
#     aggregate-address 203.0.113.0/24 as-set summary-only
#   vrf site-1
#     address-family ipv4 unicast
#     address-family ipv6 multicast
#       redistribute ospfv3 100 route-map rmap-ospf-1
#       redistribute eigrp 101 route-map rmap-eigrp-1

# Using overridden

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   address-family ipv4 multicast
#     nexthop route-map rmap2
#     nexthop trigger-delay critical 120 non-critical 180
#     network 192.0.2.32/27
#     network 192.0.2.64/27 route-map rmap1
#   vrf site-1
#     address-family ipv4 unicast
#       default-information originate
#       aggregate-address 203.0.113.0/24 as-set summary-only
#     address-family ipv6 multicast
#       redistribute ospfv3 100 route-map rmap-ospf-1
#       redistribute eigrp 101 route-map rmap-eigrp-1

- name: Override all BGP AF configuration with provided configuration
  cisco.nxos.nxos_bgp_address_family: &overridden
    config:
      as_number: 65536
      address_family:
        - afi: ipv4
          safi: multicast
          networks:
            - prefix: 192.0.2.64/27
              route_map: rmap1
          aggregate_address:
            - prefix: 203.0.113.0/24
              as_set: True
              summary_only: True
        - afi: ipv4
          safi: unicast
          vrf: site-1
    state: overridden

# Task output
# -------------
#  before:
#    as_number: "65536"
#    address_family:
#      - afi: ipv4
#        safi: multicast
#        networks:
#          - prefix: 192.0.2.32/27
#          - prefix: 192.0.2.64/27
#            route_map: rmap1
#        nexthop:
#          route_map: rmap2
#          trigger_delay:
#            critical_delay: 120
#            non_critical_delay: 180
#      - afi: ipv4
#        safi: unicast
#        vrf: site-1
#        default_information:
#          originate: True
#        aggregate_address:
#          - prefix: 203.0.113.0/24
#            as_set: True
#            summary_only: True
#      - afi: ipv6
#        safi: multicast
#        vrf: site-1
#        redistribute:
#          - id: "100"
#            protocol: ospfv3
#            route_map: rmap-ospf-1
#          - id: "101"
#            protocol: eigrp
#            route_map: rmap-eigrp-1
#
#  commands:
#  - router bgp 65536
#  - vrf site-1
#  - no address-family ipv6 multicast
#  - exit
#  - address-family ipv4 multicast
#  - no nexthop route-map rmap2
#  - no nexthop trigger-delay critical 120 non-critical 180
#  - aggregate-address 203.0.113.0/24 as-set summary-only
#  - no network 192.0.2.32/27
#  - vrf site-1
#  - address-family ipv4 unicast
#  - no default-information originate
#  - no aggregate-address 203.0.113.0/24 as-set summary-only
#
#  after:
#    as_number: "65536"
#    address_family:
#      - afi: ipv4
#        safi: multicast
#        networks:
#          - prefix: 192.0.2.64/27
#            route_map: rmap1
#        aggregate_address:
#          - prefix: 203.0.113.0/24
#            as_set: True
#            summary_only: True
#      - afi: ipv4
#        safi: unicast
#        vrf: site-1

#
# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   address-family ipv4 multicast
#     network 192.0.2.64/27 route-map rmap1
#     aggregate-address 203.0.113.0/24 as-set summary-only
#   vrf site-1
#     address-family ipv4 unicast
#

# Using deleted to remove specified AFs

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   address-family ipv4 multicast
#     nexthop route-map rmap2
#     nexthop trigger-delay critical 120 non-critical 180
#     network 192.0.2.32/27
#     network 192.0.2.64/27 route-map rmap1
#   vrf site-1
#     address-family ipv4 unicast
#       default-information originate
#       aggregate-address 203.0.113.0/24 as-set summary-only
#     address-family ipv6 multicast
#       redistribute ospfv3 100 route-map rmap-ospf-1
#       redistribute eigrp 101 route-map rmap-eigrp-1

- name: Delete specified BGP AFs
  cisco.nxos.nxos_bgp_address_family:
    config:
      as_number: 65536
      address_family:
        - afi: ipv4
          safi: multicast
        - vrf: site-1
          afi: ipv6
          safi: multicast
    state: deleted

# Task output
# -------------
#  before:
#    as_number: "65536"
#    address_family:
#      - afi: ipv4
#        safi: multicast
#        networks:
#          - prefix: 192.0.2.32/27
#          - prefix: 192.0.2.64/27
#            route_map: rmap1
#        nexthop:
#          route_map: rmap2
#          trigger_delay:
#            critical_delay: 120
#            non_critical_delay: 180
#      - afi: ipv4
#        safi: unicast
#        vrf: site-1
#        default_information:
#          originate: True
#        aggregate_address:
#          - prefix: 203.0.113.0/24
#            as_set: True
#            summary_only: True
#      - afi: ipv6
#        safi: multicast
#        vrf: site-1
#        redistribute:
#          - id: "100"
#            protocol: ospfv3
#            route_map: rmap-ospf-1
#          - id: "101"
#            protocol: eigrp
#            route_map: rmap-eigrp-1
#
#  commands:
#  - router bgp 65563
#  - no address-family ipv4 multicast
#  - vrf site-1
#  - no address-family ipv6 multicast
#
#  after:
#    as_number: "65536"
#    address_family:
#      - afi: ipv4
#        safi: unicast
#        vrf: site-1
#        default_information:
#          originate: True
#        aggregate_address:
#          - prefix: 203.0.113.0/24
#            as_set: True
#            summary_only: True

# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   vrf site-1
#     address-family ipv4 unicast
#       default-information originate
#       aggregate-address 203.0.113.0/24 as-set summary-only

# Using deleted to remove all BGP AFs

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   address-family ipv4 multicast
#     nexthop route-map rmap2
#     nexthop trigger-delay critical 120 non-critical 180
#     network 192.0.2.32/27
#     network 192.0.2.64/27 route-map rmap1
#   vrf site-1
#     address-family ipv4 unicast
#       default-information originate
#       aggregate-address 203.0.113.0/24 as-set summary-only
#     address-family ipv6 multicast
#       redistribute ospfv3 100 route-map rmap-ospf-1
#       redistribute eigrp 101 route-map rmap-eigrp-1

- name: Delete all BGP AFs
  cisco.nxos.nxos_bgp_address_family:
    state: deleted

# Task output
# -------------
#  before:
#    as_number: "65536"
#    address_family:
#      - afi: ipv4
#        safi: multicast
#        networks:
#          - prefix: 192.0.2.32/27
#          - prefix: 192.0.2.64/27
#            route_map: rmap1
#        nexthop:
#          route_map: rmap2
#          trigger_delay:
#            critical_delay: 120
#            non_critical_delay: 180
#      - afi: ipv4
#        safi: unicast
#        vrf: site-1
#        default_information:
#          originate: True
#        aggregate_address:
#          - prefix: 203.0.113.0/24
#            as_set: True
#            summary_only: True
#      - afi: ipv6
#        safi: multicast
#        vrf: site-1
#        redistribute:
#          - id: "100"
#            protocol: ospfv3
#            route_map: rmap-ospf-1
#          - id: "101"
#            protocol: eigrp
#            route_map: rmap-eigrp-1
#
#  commands:
#  - router bgp 65563
#  - no address-family ipv4 multicast
#  - vrf site-1
#  - no address-family ipv4 unicast
#  - no address-family ipv6 multicast
#
#  after:
#    as_number: "65536"

# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
# Nexus9000v#

# Using rendered

- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.nxos.nxos_bgp_address_family:
    config:
      as_number: 65536
      address_family:
        - afi: ipv4
          safi: multicast
          networks:
            - prefix: 192.0.2.32/27
            - prefix: 192.0.2.64/27
              route_map: rmap1
          nexthop:
            route_map: rmap2
            trigger_delay:
              critical_delay: 120
              non_critical_delay: 180
        - afi: ipv4
          safi: unicast
          vrf: site-1
          default_information:
            originate: True
          aggregate_address:
            - prefix: 203.0.113.0/24
              as_set: True
              summary_only: True
        - afi: ipv6
          safi: multicast
          vrf: site-1
          redistribute:
            - protocol: ospfv3
              id: 100
              route_map: rmap-ospf-1
            - protocol: eigrp
              id: 101
              route_map: rmap-eigrp-1
    state: rendered

# Task Output (redacted)
# -----------------------
# rendered:
# - router bgp 65536
# - address-family ipv4 multicast
# - nexthop route-map rmap2
# - nexthop trigger-delay critical 120 non-critical 180
# - network 192.0.2.32/27
# - network 192.0.2.64/27 route-map rmap1
# - vrf site-1
# - address-family ipv4 unicast
# - default-information originate
# - aggregate-address 203.0.113.0/24 as-set summary-only
# - address-family ipv6 multicast
# - redistribute ospfv3 100 route-map rmap-ospf-1
# - redistribute eigrp 101 route-map rmap-eigrp-1

# Using parsed

# parsed.cfg
# ------------
# router bgp 65536
#   address-family ipv4 multicast
#     nexthop route-map rmap2
#     nexthop trigger-delay critical 120 non-critical 180
#     network 192.0.2.32/27
#    network 192.0.2.64/27 route-map rmap1
#  vrf site-1
#    address-family ipv4 unicast
#      default-information originate
#      aggregate-address 203.0.113.0/24 as-set summary-only
#    address-family ipv6 multicast
#      redistribute ospfv3 100 route-map rmap-ospf-1
#      redistribute eigrp 101 route-map rmap-eigrp-1

- name: Parse externally provided BGP AF config
  cisco.nxos.nxos_bgp_address_family:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
#  parsed:
#    as_number: "65536"
#    address_family:
#      - afi: ipv4
#        safi: multicast
#        networks:
#          - prefix: 192.0.2.32/27
#          - prefix: 192.0.2.64/27
#            route_map: rmap1
#        nexthop:
#          route_map: rmap2
#          trigger_delay:
#            critical_delay: 120
#            non_critical_delay: 180
#      - afi: ipv4
#        safi: unicast
#        vrf: site-1
#        default_information:
#          originate: True
#        aggregate_address:
#          - prefix: 203.0.113.0/24
#            as_set: True
#            summary_only: True
#      - afi: ipv6
#        safi: multicast
#        vrf: site-1
#        redistribute:
#          - id: "100"
#            protocol: ospfv3
#            route_map: rmap-ospf-1
#          - id: "101"
#            protocol: eigrp
#            route_map: rmap-eigrp-1
```

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
