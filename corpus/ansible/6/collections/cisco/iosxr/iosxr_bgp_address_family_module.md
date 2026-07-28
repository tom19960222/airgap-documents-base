---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_bgp_address_family module – Resource module to configure BGP Address family."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_bgp_address_family_module.html
fetched_at: 2026-07-27T16:55:37+00:00
---
# cisco.iosxr.iosxr_bgp_address_family module – Resource module to configure BGP Address family.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_bgp_address_family`.

New in cisco.iosxr 2.0.0

- [Synopsis](iosxr_bgp_address_family_module.md#synopsis)
- [Parameters](iosxr_bgp_address_family_module.md#parameters)
- [Notes](iosxr_bgp_address_family_module.md#notes)
- [Examples](iosxr_bgp_address_family_module.md#examples)

## [Synopsis](iosxr_bgp_address_family_module.md#id1)

- This module configures and manages the attributes of BGP address family on Cisco IOS-XR platforms.

## [Parameters](iosxr_bgp_address_family_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | A list of configurations for BGP address family. |
| **address_family**  list / elements=dictionary | Enable address family and enter its config mode |
| **additional_paths**  string | BGP additional-paths commands  Choices:   - `"send"` - `"receive"` |
| **advertise_best_external**  boolean | Advertise best-external path.  Choices:   - `false` - `true` |
| **afi**  string | address family.  Choices:   - `"ipv4"` - `"ipv6"` - `"l2vpn"` - `"link-state"` - `"vpnv4"` - `"vpnv6"` |
| **aggregate_address**  list / elements=dictionary | Configure BGP aggregate entries. |
| **as_confed_set**  boolean | Generate AS confed set path information.  Choices:   - `false` - `true` |
| **as_set**  boolean | Generate AS set path information.  Choices:   - `false` - `true` |
| **route_policy**  string | Policy to condition advertisement, suppression, and attributes. |
| **summary_only**  boolean | Filter more specific routes from updates.  Choices:   - `false` - `true` |
| **value**  string | IPv4 Aggregate address and mask or masklength. |
| **allocate_label**  dictionary | Allocate labels. |
| **all**  boolean | Allocate labels for all prefixes.  Choices:   - `false` - `true` |
| **route_policy**  string | Use a route policy to select prefixes for label allocation. |
| **allow_vpn_default_originate**  boolean | Allow sending default originate route to VPN neighbor.  Choices:   - `false` - `true` |
| **as_path_loopcheck_out_disable**  boolean | Configure AS Path loop checking for outbound updates.  Choices:   - `false` - `true` |
| **bgp**  dictionary | BGP Commands. |
| **attribute_download**  boolean | Configure attribute download for this address-family.  Choices:   - `false` - `true` |
| **bestpath**  dictionary | Change default route selection criteria. |
| **origin_as**  dictionary | BGP origin-AS knobs. |
| **allow**  dictionary | BGP origin-AS knobs. |
| **invalid**  boolean | BGP bestpath selection will allow ‘invalid’ origin-AS  Choices:   - `false` - `true` |
| **use**  dictionary | BGP origin-AS knobs. |
| **validity**  boolean | BGP bestpath selection will use origin-AS validity  Choices:   - `false` - `true` |
| **client_to_client**  dictionary | Configure client to client route reflection. |
| **reflection**  dictionary | disable client to client reflection of cluster id. |
| **cluster_id_disable**  dictionary | ID of Cluster for which reflection is to be disabled. |
| **cluster_id**  string | ID of Cluster for which reflection is to be disabled. |
| **disable**  boolean | disable cluster id.  Choices:   - `false` - `true` |
| **disable**  boolean | disable reflection.  Choices:   - `false` - `true` |
| **dampening**  dictionary | Enable route-flap dampening |
| **route_policy**  string | Route policy to specify criteria for dampening. |
| **set**  boolean | Enable dampening.  Choices:   - `false` - `true` |
| **value**  integer | Half-life time for the penalty |
| **import_delay**  dictionary | Specify delay for batching import processing. |
| **delay_ms_parts**  integer | milliseconds part <0-999>. |
| **delay_second_parts**  integer | Delay, seconds part <0-10>. |
| **label_delay**  dictionary | Specify delay for batching label processing |
| **delay_ms_parts**  integer | milliseconds part <0-999>. |
| **delay_second_parts**  integer | Delay, seconds part <0-10>. |
| **origin_as**  dictionary | BGP origin-AS knobs. |
| **validation**  dictionary | BGP origin-AS validation knobs. |
| **disable**  boolean | Disable RPKI origin-AS validation.  Choices:   - `false` - `true` |
| **signal**  dictionary | Signal origin-AS validity towards peers. |
| **ibgp**  boolean | Signal origin-AS validity towards iBGP peers  Choices:   - `false` - `true` |
| **scan_time**  integer | Configure background scanner interval for this address-family Example- <5-3600>. |
| **default_martian_check_disable**  boolean | Martian check default  Choices:   - `false` - `true` |
| **distance**  dictionary | Define an administrative distance. |
| **local_routes**  integer | Distance for local routes <1-255>. |
| **routes_external_to_as**  integer | Distance for routes external to the AS <1-255>. |
| **routes_internal_to_as**  integer | Distance for routes internal to the AS <1-255>. |
| **dynamic_med**  integer | Dynamic MED Interval. |
| **global_table_multicast**  boolean | Enable global table multicast.  Choices:   - `false` - `true` |
| **inter_as_install**  boolean | Install remote mvpn routes in default vrf.This is applicable for mvpn afi.  Choices:   - `false` - `true` |
| **label_mode**  dictionary | label configuration. |
| **per_ce**  boolean | Set per CE label mode  Choices:   - `false` - `true` |
| **per_prefix**  boolean | Set per perfix label mode.  Choices:   - `false` - `true` |
| **per_vrf**  boolean | Set per VRF label mode.  Choices:   - `false` - `true` |
| **route_policy**  string | Use a route policy to select prefixes for label allocation mode. |
| **maximum_paths**  dictionary | Forward packets over multiple paths. |
| **ebgp**  dictionary | ebgp-multipath. |
| **max_path_value**  integer | <2-64> Number of paths (limit includes backup path). |
| **order_igp_metric**  boolean | Order candidate multipaths for selection as per configured number(cisco-support).  Choices:   - `false` - `true` |
| **selective_order_igp_metric**  boolean | Allow multipaths only from marked neighbors  Choices:   - `false` - `true` |
| **eibgp**  dictionary | eiBGP-multipath. |
| **max_path_value**  integer | <2-64> Number of paths (limit includes backup path). |
| **order_igp_metric**  boolean | Order candidate multipaths for selection as per configured number(cisco-support).  Choices:   - `false` - `true` |
| **selective_order_igp_metric**  boolean | Allow multipaths only from marked neighbors  Choices:   - `false` - `true` |
| **ibgp**  dictionary | iBGP-multipath. |
| **max_path_value**  integer | <2-64> Number of paths (limit includes backup path). |
| **order_igp_metric**  boolean | Order candidate multipaths for selection as per configured number(cisco-support).  Choices:   - `false` - `true` |
| **selective_order_igp_metric**  boolean | Allow multipaths only from marked neighbors  Choices:   - `false` - `true` |
| **unequal_cost**  dictionary | Allow multipaths to have different BGP nexthop IGP metrics. |
| **order_igp_metric**  boolean | Order candidate multipaths for selection as per configured number(cisco-support).  Choices:   - `false` - `true` |
| **selective_order_igp_metric**  boolean | Allow multipaths only from marked neighbors  Choices:   - `false` - `true` |
| **set**  boolean | set unequal_cost.  Choices:   - `false` - `true` |
| **mvpn_single_forwarder_selection_all**  boolean | Enable single forwarder selection for all  Choices:   - `false` - `true` |
| **mvpn_single_forwarder_selection_highest_ip_address**  boolean | Enable single forwarder selection for PE with highest ip address.  Choices:   - `false` - `true` |
| **networks**  list / elements=dictionary | Specify a network to announce via BGP. |
| **backdoor_route_policy**  string | Specify a BGP backdoor route. |
| **network**  string | Specify a network to announce via BGP. |
| **route_policy**  string | Route-policy to modify the attributes. |
| **nexthop**  dictionary | Nexthop |
| **resolution_prefix_length_minimum**  integer | Set minimum prefix-length for nexthop resolution.  Choices:   - `0` - `32` |
| **route_policy**  string | Policy to filter out nexthop notification. |
| **trigger_delay_critical**  integer | For critical notification |
| **trigger_delay_non_critical**  integer | For non critical notification. |
| **optimal_route_reflection**  dictionary | Configure optimal-route-reflection group. |
| **group_name**  string | ORR group name - maximum 32 characters. |
| **primary_address**  string | IPv4 primary address. |
| **secondary_address**  string | IPv4 secondary address |
| **permanent_network_route_policy**  string | Name of the policy. |
| **redistribute**  list / elements=dictionary | Redistribute information from another routing protocol. |
| **external**  boolean | Redistribute EIGRP external routes.applicable for eigrp.  Choices:   - `false` - `true` |
| **external_ospf**  integer | Redistribute OSPF external routes.applicable for ospf.  Choices:   - `1` - `2` |
| **id**  string | Identifier for the routing protocol for configuring redistribute information. Example-application name, eigrp/is-is instance name, ospf tag  Valid for protocols ‘ospf’, ‘eigrp’, ‘isis’ and ‘application’. |
| **internal**  boolean | Redistribute EIGRP internal routes.applicable for eigrp.  Choices:   - `false` - `true` |
| **level**  string | Redistribute routes from the specified ISIS levels.  Redistribute ISIS level 1 routes  Redistribute ISIS level 1 inter-area routes  Redistribute ISIS level 2 ISIS routes  Choices:   - `"1"` - `"2"` - `"1-inter-area"` |
| **metric**  integer | Specifies the metric for redistributed routes. |
| **nssa_external**  boolean | Redistribute OSPF NSSA external routes.applicable for ospf.  Choices:   - `false` - `true` |
| **protocol**  string / required | Specifies the protocol for configuring redistribute information.  Choices:   - `"ospf"` - `"application"` - `"eigrp"` - `"isis"` - `"static"` - `"connected"` - `"lisp"` - `"mobile"` - `"rip"` - `"subscriber"` |
| **route_policy**  string | Specifies the route policy reference. |
| **retain_local_label**  integer | Label retention time in minutes <3-60>. |
| **route_target_download**  boolean | Route target RIB installation.  Choices:   - `false` - `true` |
| **safi**  string | Address Family modifier  Choices:   - `"flowspec"` - `"mdt"` - `"multicast"` - `"mvpn"` - `"rt-filter"` - `"tunnel"` - `"unicast"` - `"evpn"` - `"mspw"` - `"vpls-vpws"` - `"link-state"` |
| **segmented_multicast**  boolean | Enable segmented multicast.This is applicable for mvpn afi.  Choices:   - `false` - `true` |
| **table_policy**  string | Configure policy for installation of routes to RIB. |
| **update**  dictionary | BGP Update generation configuration. |
| **limit**  dictionary | Update limit. |
| **address_family**  integer | Update limit for sub-groups. |
| **sub_group**  dictionary | Update limit for address-family. |
| **ebgp**  integer | Update limit for eBGP sub-groups<1-512. |
| **ibgp**  integer | Update limit for iBGP sub-groups<1-512. |
| **wait_install**  boolean | Wait for route install.  Choices:   - `false` - `true` |
| **vrf**  string | VRF name. |
| **vrf_all_conf**  dictionary | configuration is for all vrfs and its applicable for afi vpn6 and modifier unicast. |
| **label_mode**  dictionary | Label-related configuration. |
| **per_ce**  boolean | Set per CE label mode  Choices:   - `false` - `true` |
| **per_vrf**  boolean | Set per VRF label mode.  Choices:   - `false` - `true` |
| **route_policy**  string | Use a route policy to select prefixes for label allocation mode. |
| **source_rt_import_policy**  boolean | Source import route-targets from import-policy.  Choices:   - `false` - `true` |
| **table_policy**  string | Configure policy for installation of routes to RIB. |
| **weight**  dictionary | Define or modify weight. |
| **reset_on_import**  boolean | set reset_on_import.  Choices:   - `false` - `true` |
| **reset_on_import_disable**  boolean | disable reset_on_import.  Choices:   - `false` - `true` |
| **as_number**  string | Autonomous system number. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Iosxr device by executing the command **show running-config router bgp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  Choices:   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](iosxr_bgp_address_family_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`.

## [Examples](iosxr_bgp_address_family_module.md#id4)

```yaml+jinja
# Using merged
# Before state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.2.1
#  address-family vpnv4 unicast
#  vrf vrf1
#   rd auto
- name: Merge the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_bgp_address_family:
    state: merged
    config:
      as_number: "65536"
      address_family:
        - afi: "ipv4"
          safi: "unicast"
          vrf: vrf1
          dynamic_med: 9
          redistribute:
            - protocol: connected
              metric: 10
        - afi: "ipv4"
          safi: "unicast"
          dynamic_med: 10
          redistribute:
            - protocol: application
              id: test1
              metric: 10
          bgp:
            scan_time: 20
            attribute_download: true
          advertise_best_external: true
          allocate_label:
            all: true
# Task output
# -------------
# commands:
# - router bgp 65536
# - address-family ipv4 unicast
# - advertise best-external
# - allocate-label all
# - bgp attribute-download
# - bgp scan-time 20
# - dynamic-med interval 10
# - redistribute application test1 metric 10
# - vrf vrf1
# - address-family ipv4 unicast
# - dynamic-med interval 9
# - redistribute connected metric 10
#
#
# after:
#   as_number: "65536"
#   address_family:
#     - afi: "ipv4"
#       safi: "unicast"
#       vrf: vrf1
#       dynamic_med: 9
#       redistribute:
#         - protocol: connected
#           metric: 10
#     - afi: "ipv4"
#       safi: "unicast"
#       dynamic_med: 10
#       redistribute:
#         - protocol: application
#           id: "test1"
#           metric: 10
#       bgp:
#         scan_time: 20
#         attribute_download: true
#       advertise_best_external: true
#       allocate_label:
#         all: true
#
# After state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#    advertise best-external
#    allocate-label all
#    bgp attribute-download
#    bgp scan-time 20
#  address-family vpnv4 unicast
#  vrf vrf1
#   rd auto
#   address-family ipv4 unicast
#     dynamic-med interval 9
#     redistribute connected metric 10
#
# Using replaced
# Before state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#    advertise best-external
#    allocate-label all
#    bgp attribute-download
#    bgp scan-time 20
#  address-family vpnv4 unicast
#  vrf vrf1
#   rd auto
#   address-family ipv4 unicast
#     dynamic-med interval 9
#     redistribute connected metric 10
#
#
- name: Replace the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_bgp_address_family:
    state: replaced
    config:
      as_number: "65536"
      address_family:
        - afi: "ipv4"
          safi: "unicast"
          vrf: vrf1
          dynamic_med: 10
# Task output
# -------------
# commands:
# - router bgp 65536
# - vrf vrf1
# - address-family ipv4 unicast
# - dynamic-med interval 10
# - no redistribute connected metric 10
#
# after:
#   as_number: "65536"
#   address_family:
#     - afi: "ipv4"
#       safi: "unicast"
#       vrf: vrf1
#       dynamic_med: 10
#     - afi: "ipv4"
#       safi: "unicast"
#       dynamic_med: 10
#       redistribute:
#         - protocol: application
#           id: "test1"
#           metric: 10
#       bgp:
#         scan_time: 20
#         attribute_download: true
#       advertise_best_external: true
#       allocate_label:
#         all: true
# After state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#    advertise best-external
#    allocate-label all
#    bgp attribute-download
#    bgp scan-time 20
#  address-family vpnv4 unicast
#  vrf vrf1
#   rd auto
#   address-family ipv4 unicast
#     dynamic-med interval 10
#
#
# Using overridden
# Before state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#    advertise best-external
#    allocate-label all
#    bgp attribute-download
#    bgp scan-time 20
#  address-family vpnv4 unicast
#  vrf vrf1
#   rd auto
#   address-family ipv4 unicast
#     dynamic-med interval 9
#     redistribute connected metric 10
#
#
- name: Override the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_bgp_address_family:
    state: overridden
    config:
      as_number: "65536"
      address_family:
        - afi: "ipv4"
          safi: "unicast"
          vrf: vrf1
          dynamic_med: 10

# Task output
# -------------
# commands:
# - router bgp 65536
# - no address-family ipv4 unicast
# - vrf vrf1
# - address-family ipv4 unicast
# - dynamic-med interval 10
# - no redistribute connected metric 10
#
#
# after:
#   as_number: "65536"
#   address_family:
#     - afi: "ipv4"
#       safi: "unicast"
#       vrf: vrf1
#       dynamic_med: 10
#
# After state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family vpnv4 unicast
#  vrf vrf1
#   rd auto
#   address-family ipv4 unicast
#     dynamic-med interval 10
#
#
# Using deleted
# Before state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#    advertise best-external
#    allocate-label all
#    bgp attribute-download
#    bgp scan-time 20
#  address-family vpnv4 unicast
#  vrf vrf1
#   rd auto
#   address-family ipv4 unicast
#     dynamic-med interval 9
#     redistribute connected metric 10
#
#
- name: Delete the provided configuration
  cisco.iosxr.iosxr_bgp_address_family:
    state: deleted
    config:

# Task output
# -------------
# commands:
# - router bgp 65536
# - no address-family ipv4 unicast
# - vrf vrf1
# - no address-family ipv4 unicast
#
#
# after:
#   as_number: "65536"
#
#
# After state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family vpnv4 unicast
#  vrf vrf1
#   rd auto
#
# Using rendered
# -------------
#
- name: rendered state example
  cisco.iosxr.iosxr_bgp_address_family:
    state: rendered
    config:
      as_number: "65536"
      address_family:
        - afi: "ipv4"
          safi: "unicast"
          vrf: vrf1
          dynamic_med: 9
          redistribute:
            - protocol: connected
              metric: 10
        - afi: "ipv4"
          safi: "unicast"
          dynamic_med: 10
          redistribute:
            - protocol: application
              id: test1
              metric: 10
          bgp:
            scan_time: 20
            attribute_download: true
          advertise_best_external: true
          allocate_label:
            all: true
# Task output
# -------------
# commands:
# - router bgp 65536
# - address-family ipv4 unicast
# - advertise best-external
# - allocate-label all
# - bgp attribute-download
# - bgp scan-time 20
# - dynamic-med interval 10
# - redistribute application test1 metric 10
# - vrf vrf1
# - address-family ipv4 unicast
# - dynamic-med interval 9
# - redistribute connected metric 10
#
# Using gathered
# -------------
- name: Merge the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_bgp_address_family:
    state: gathered
    config:
      as_number: "65536"
      address_family:
        - afi: "ipv4"
          safi: "unicast"
          vrf: vrf1
          dynamic_med: 9
          redistribute:
            - protocol: connected
              metric: 10
        - afi: "ipv4"
          safi: "unicast"
          dynamic_med: 10
          redistribute:
            - protocol: application
              id: test1
              metric: 10
          bgp:
            scan_time: 20
            attribute_download: true
          advertise_best_external: true
          allocate_label:
            all: true
# gathered:
#   as_number: "65536"
#   address_family:
#     - afi: "ipv4"
#       safi: "unicast"
#       vrf: vrf1
#       dynamic_med: 9
#       redistribute:
#         - protocol: connected
#           metric: 10
#     - afi: "ipv4"
#       safi: "unicast"
#       dynamic_med: 10
#       redistribute:
#         - protocol: application
#           id: "test1"
#           metric: 10
#       bgp:
#         scan_time: 20
#         attribute_download: true
#       advertise_best_external: true
#       allocate_label:
#         all: true
#
# Using parsed
#
#parsed.cfg
#------------
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#    advertise best-external
#    allocate-label all
#    bgp attribute-download
#    bgp scan-time 20
#  address-family vpnv4 unicast
#  vrf vrf1
#   rd auto
#   address-family ipv4 unicast
#     dynamic-med interval 9
#     redistribute connected metric 10
#
- name: Parse externally provided BGP neighbor AF config
  cisco.iosxr.iosxr_bgp_address_family:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
# parsed:
#   as_number: "65536"
#   address_family:
#     - afi: "ipv4"
#       safi: "unicast"
#       vrf: vrf1
#       dynamic_med: 9
#       redistribute:
#         - protocol: connected
#           metric: 10
#     - afi: "ipv4"
#       safi: "unicast"
#       dynamic_med: 10
#       redistribute:
#         - protocol: application
#           id: "test1"
#           metric: 10
#       bgp:
#         scan_time: 20
#         attribute_download: true
#       advertise_best_external: true
#       allocate_label:
#         all: true
```

### Authors

- Ashwini Mhatre (@amhatre)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
