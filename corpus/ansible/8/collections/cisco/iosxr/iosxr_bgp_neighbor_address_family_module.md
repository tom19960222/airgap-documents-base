---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_bgp_neighbor_address_family module – Resource module to configure BGP Neighbor Address family."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_bgp_neighbor_address_family_module.html
fetched_at: 2026-07-28T01:26:38+00:00
---
# cisco.iosxr.iosxr_bgp_neighbor_address_family module – Resource module to configure BGP Neighbor Address family.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_bgp_neighbor_address_family`.

New in cisco.iosxr 2.0.0

- [Synopsis](iosxr_bgp_neighbor_address_family_module.md#synopsis)
- [Parameters](iosxr_bgp_neighbor_address_family_module.md#parameters)
- [Notes](iosxr_bgp_neighbor_address_family_module.md#notes)
- [Examples](iosxr_bgp_neighbor_address_family_module.md#examples)

## [Synopsis](iosxr_bgp_neighbor_address_family_module.md#id1)

- This module configures and manages the attributes of BGP global on Cisco IOS-XR platforms.

Aliases: bgp_neighbor_address_family

## [Parameters](iosxr_bgp_neighbor_address_family_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | BGP neighbor address family configurations. |
| **as_number**  string | Autonomous system number. |
| **neighbors**  list / elements=dictionary | A list of BGP neighbor address family configurations. |
| **address_family**  list / elements=dictionary | Enable address family and enter its config mode |
| **afi**  string | address family.  **Choices:**   - `"ipv4"` - `"ipv6"` - `"l2vpn"` - `"link-state"` - `"vpnv4"` - `"vpnv6"` |
| **aigp**  dictionary | AIGP attribute |
| **disable**  boolean | Ignore AIGP attribute.  **Choices:**   - `false` - `true` |
| **send_cost_community_disable**  boolean | send AIGP attribute.  **Choices:**   - `false` - `true` |
| **send_med**  dictionary | send med options. |
| **disable**  boolean | disable Send AIGP value in MED.  **Choices:**   - `false` - `true` |
| **set**  boolean | set Send AIGP value in MED.  **Choices:**   - `false` - `true` |
| **set**  boolean | Set AIGP attribute.  **Choices:**   - `false` - `true` |
| **allowas_in**  dictionary | Allow as-path with my AS present in it. |
| **set**  boolean | set allowas_in  **Choices:**   - `false` - `true` |
| **value**  integer | Number of occurences of AS number 1-10. |
| **as_override**  dictionary | Override matching AS-number while sending update |
| **inheritance_disable**  boolean | Prevent as-override from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set as_override  **Choices:**   - `false` - `true` |
| **bestpath_origin_as_allow_invalid**  boolean | Change default route selection criteria.Allow BGP origin-AS knobs.  **Choices:**   - `false` - `true` |
| **capability_orf_prefix**  string | Advertise address prefix ORF capability to this neighbor.  **Choices:**   - `"both"` - `"send"` - `"none"` - `"receive"` |
| **default_originate**  dictionary | Originate default route to this neighbor. |
| **inheritance_disable**  boolean | Prevent default-originate from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **route_policy**  string | Route policy to specify criteria to originate default |
| **set**  boolean | set default route.  **Choices:**   - `false` - `true` |
| **long_lived_graceful_restart**  dictionary | Enable long lived graceful restart support. |
| **capable**  boolean | Treat neighbor as LLGR capable.  **Choices:**   - `false` - `true` |
| **stale_time**  dictionary | Maximum time to wait before purging long-lived stale routes. |
| **accept**  integer | max accept time |
| **send**  integer | max send time |
| **maximum_prefix**  dictionary | Maximum number of prefixes to accept from this peer. |
| **discard_extra_paths**  boolean | Discard extra paths when limit is exceeded.  **Choices:**   - `false` - `true` |
| **max_limit**  integer | maximum no. of prefix limit.<1-4294967295. |
| **restart**  integer | Restart time interval. |
| **threshold_value**  integer | hreshold value (%) at which to generate a warning msg <1-100>. |
| **warning_only**  boolean | Only give warning message when limit is exceeded.  **Choices:**   - `false` - `true` |
| **multipath**  boolean | Paths from this neighbor is eligible for multipath.  **Choices:**   - `false` - `true` |
| **next_hop_self**  dictionary | Disable the next hop calculation for this neighbor. |
| **inheritance_disable**  boolean | Prevent next_hop_self from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set next hop self.  **Choices:**   - `false` - `true` |
| **next_hop_unchanged**  dictionary | Disable the next hop calculation for this neighbor. |
| **inheritance_disable**  boolean | Prevent next_hop_unchanged from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **multipath**  boolean | Do not overwrite nexthop before advertising multipaths.  **Choices:**   - `false` - `true` |
| **set**  boolean | set next hop unchanged.  **Choices:**   - `false` - `true` |
| **optimal_route_reflection_group_name**  string | Configure optimal-route-reflection group. |
| **orf_route_policy**  string | Specify ORF and inbound filtering criteria.’ |
| **origin_as**  dictionary | BGP origin-AS knobs. |
| **validation**  dictionary | BGP origin-AS validation knobs. |
| **disable**  boolean | Disable RPKI origin-AS validation.  **Choices:**   - `false` - `true` |
| **remove_private_AS**  dictionary | Remove private AS number from outbound updates. |
| **entire_aspath**  boolean | remove only if all ASes in the path are private.  **Choices:**   - `false` - `true` |
| **inbound**  boolean | Remove private AS number from inbound updates.  **Choices:**   - `false` - `true` |
| **inheritance_disable**  boolean | Prevent remove-private-AS from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set remove private As.  **Choices:**   - `false` - `true` |
| **route_policy**  dictionary | Apply route policy to neighbor. |
| **inbound**  string | Apply route policy to inbound routes. |
| **outbound**  string | Apply route policy to outbound routes. |
| **route_reflector_client**  dictionary | Configure a neighbor as Route Reflector client. |
| **inheritance_disable**  boolean | Prevent route-reflector-client from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set route-reflector-client.  **Choices:**   - `false` - `true` |
| **safi**  string | Address Family modifier  **Choices:**   - `"flowspec"` - `"mdt"` - `"multicast"` - `"mvpn"` - `"rt-filter"` - `"tunnel"` - `"unicast"` - `"labeled-unicast"` |
| **send_community_ebgp**  dictionary | Send community attribute to this external neighbor. |
| **inheritance_disable**  boolean | Prevent send_community_ebgp from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set send_community_ebgp.  **Choices:**   - `false` - `true` |
| **send_community_gshut_ebgp**  dictionary | Allow the g-shut community to be sent to this external neighbor. |
| **inheritance_disable**  boolean | Prevent send_community_gshut_ebgp from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set send_community_gshut_ebgp.  **Choices:**   - `false` - `true` |
| **send_extended_community_ebgp**  dictionary | Send extended community attribute to this external neighbor. |
| **inheritance_disable**  boolean | Prevent send_extended_community_ebgp from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set send_extended_community_ebgp.  **Choices:**   - `false` - `true` |
| **send_multicast_attributes**  dictionary | Send multicast attributes to this neighbor . |
| **disable**  boolean | Disable send multicast attributes.  **Choices:**   - `false` - `true` |
| **set**  boolean | set send_multicast_attributes.  **Choices:**   - `false` - `true` |
| **soft_reconfiguration**  dictionary | Per neighbor soft reconfiguration. |
| **inbound**  dictionary | inbound soft reconfiguration |
| **always**  boolean | Allow inbound soft reconfiguration for this neighbor. Always use soft reconfig, even if route refresh is supported.  **Choices:**   - `false` - `true` |
| **inheritance_disable**  boolean | Prevent soft_reconfiguration from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set inbound  **Choices:**   - `false` - `true` |
| **validation**  dictionary | Flowspec Validation for this neighbor. |
| **disable**  boolean | disable validation.  **Choices:**   - `false` - `true` |
| **redirect**  boolean | Flowspec Redirect nexthop Validation.  **Choices:**   - `false` - `true` |
| **set**  boolean | set validation.  **Choices:**   - `false` - `true` |
| **weight**  integer | Set default weight for routes from this neighbor. |
| **neighbor_address**  string / required | Neighbor router address. |
| **vrfs**  list / elements=dictionary | Configure BGP neighbor afin a VRF. |
| **neighbors**  list / elements=dictionary | A list of BGP neighbor address family configurations. |
| **address_family**  list / elements=dictionary | Enable address family and enter its config mode |
| **afi**  string | address family.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **aigp**  dictionary | AIGP attribute |
| **disable**  boolean | Ignore AIGP attribute.  **Choices:**   - `false` - `true` |
| **send_cost_community_disable**  boolean | send AIGP attribute.  **Choices:**   - `false` - `true` |
| **send_med**  dictionary | send med options. |
| **disable**  boolean | disable Send AIGP value in MED.  **Choices:**   - `false` - `true` |
| **set**  boolean | set Send AIGP value in MED.  **Choices:**   - `false` - `true` |
| **set**  boolean | Set AIGP attribute.  **Choices:**   - `false` - `true` |
| **allowas_in**  dictionary | Allow as-path with my AS present in it. |
| **set**  boolean | set allowas_in  **Choices:**   - `false` - `true` |
| **value**  integer | Number of occurences of AS number 1-10. |
| **as_override**  aliases: as_overrride  dictionary | Override matching AS-number while sending update |
| **inheritance_disable**  boolean | Prevent as-override from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set as_override  **Choices:**   - `false` - `true` |
| **capability_orf_prefix**  string | Advertise address prefix ORF capability to this neighbor.  **Choices:**   - `"both"` - `"send"` - `"none"` - `"receive"` |
| **default_originate**  dictionary | Originate default route to this neighbor. |
| **inheritance_disable**  boolean | Prevent default-originate from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **route_policy**  string | Route policy to specify criteria to originate default |
| **set**  boolean | set default route.  **Choices:**   - `false` - `true` |
| **long_lived_graceful_restart**  dictionary | Enable long lived graceful restart support. |
| **capable**  boolean | Treat neighbor as LLGR capable.  **Choices:**   - `false` - `true` |
| **stale_time**  dictionary | Maximum time to wait before purging long-lived stale routes. |
| **accept**  integer | max accept time |
| **send**  integer | max send time |
| **maximum_prefix**  dictionary | Maximum number of prefixes to accept from this peer. |
| **discard_extra_paths**  boolean | Discard extra paths when limit is exceeded.  **Choices:**   - `false` - `true` |
| **max_limit**  integer | maximum no. of prefix limit.<1-4294967295. |
| **restart**  integer | Restart time interval. |
| **threshold_value**  integer | hreshold value (%) at which to generate a warning msg <1-100>. |
| **warning_only**  boolean | Only give warning message when limit is exceeded.  **Choices:**   - `false` - `true` |
| **multipath**  boolean | Paths from this neighbor is eligible for multipath.  **Choices:**   - `false` - `true` |
| **next_hop_self**  dictionary | Disable the next hop calculation for this neighbor. |
| **inheritance_disable**  boolean | Prevent next_hop_self from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set next hop self.  **Choices:**   - `false` - `true` |
| **next_hop_unchanged**  dictionary | Disable the next hop calculation for this neighbor. |
| **inheritance_disable**  boolean | Prevent next_hop_unchanged from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **multipath**  boolean | Do not overwrite nexthop before advertising multipaths.  **Choices:**   - `false` - `true` |
| **set**  boolean | set next hop unchanged.  **Choices:**   - `false` - `true` |
| **optimal_route_reflection_group_name**  string | Configure optimal-route-reflection group. |
| **orf_route_policy**  string | Specify ORF and inbound filtering criteria.’ |
| **remove_private_AS**  dictionary | Remove private AS number from outbound updates. |
| **entire_aspath**  boolean | remove only if all ASes in the path are private.  **Choices:**   - `false` - `true` |
| **inbound**  boolean | Remove private AS number from inbound updates.  **Choices:**   - `false` - `true` |
| **inheritance_disable**  boolean | Prevent remove-private-AS from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set remove private As.  **Choices:**   - `false` - `true` |
| **route_policy**  dictionary | Apply route policy to neighbor. |
| **inbound**  string | Apply route policy to inbound routes. |
| **outbound**  string | Apply route policy to outbound routes. |
| **route_reflector_client**  dictionary | Configure a neighbor as Route Reflector client. |
| **inheritance_disable**  boolean | Prevent route-reflector-client from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set route-reflector-client.  **Choices:**   - `false` - `true` |
| **safi**  string | Address Family modifier  **Choices:**   - `"flowspec"` - `"multicast"` - `"mvpn"` - `"unicast"` - `"labeled-unicast"` |
| **send_community_ebgp**  dictionary | Send community attribute to this external neighbor. |
| **inheritance_disable**  boolean | Prevent send_community_ebgp from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set send_community_ebgp.  **Choices:**   - `false` - `true` |
| **send_community_gshut_ebgp**  dictionary | Allow the g-shut community to be sent to this external neighbor. |
| **inheritance_disable**  boolean | Prevent send_community_gshut_ebgp from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set send_community_gshut_ebgp.  **Choices:**   - `false` - `true` |
| **send_extended_community_ebgp**  dictionary | Send extended community attribute to this external neighbor. |
| **inheritance_disable**  boolean | Prevent send_extended_community_ebgp from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set send_extended_community_ebgp.  **Choices:**   - `false` - `true` |
| **site_of_origin**  string | Site-of-Origin extended community associated with the neighbor. |
| **soft_reconfiguration**  dictionary | Per neighbor soft reconfiguration. |
| **inbound**  dictionary | inbound soft reconfiguration |
| **always**  boolean | Allow inbound soft reconfiguration for this neighbor. Always use soft reconfig, even if route refresh is supported.  **Choices:**   - `false` - `true` |
| **inheritance_disable**  boolean | Prevent soft_reconfiguration from being inherited from the parent.  **Choices:**   - `false` - `true` |
| **set**  boolean | set inbound  **Choices:**   - `false` - `true` |
| **validation**  dictionary | Flowspec Validation for this neighbor. |
| **disable**  boolean | disable validation.  **Choices:**   - `false` - `true` |
| **redirect**  boolean | Flowspec Redirect nexthop Validation.  **Choices:**   - `false` - `true` |
| **set**  boolean | set validation.  **Choices:**   - `false` - `true` |
| **weight**  integer | Set default weight for routes from this neighbor. |
| **neighbor_address**  string / required | Neighbor router address. |
| **vrf**  string | VRF name. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the Iosxr device by executing the command **show running-config router bgp**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](iosxr_bgp_neighbor_address_family_module.md#id3)

> **Note:**
>
> - This module works with connection `network_cli`.

## [Examples](iosxr_bgp_neighbor_address_family_module.md#id4)

```yaml+jinja
# Using merged
# Before state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.2.1
#  address-family ipv4 unicast
#  address-family vpnv4 unicast
#  neighbor 192.0.2.2
#   remote-as 65537
#  neighbor 192.0.2.3
#   remote-as 65538
#  vrf vrf1
#   rd auto
#   neighbor 192.0.2.4
#    remote-as 65539
#  vrf vrf2
#   rd auto
#   neighbor 192.0.2.5
#    remote-as 65540

- name: Merge the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_bgp_neighbor_address_family:
    state: merged
    config:
      as_number: 65536
      neighbors:
        - neighbor_address: 192.0.2.2
          address_family:
            - afi: "ipv4"
              safi: "unicast"
              multipath: true
              default_originate:
                set: true
              weight: 5
        - neighbor_address: 192.0.2.3
          address_family:
            - afi: "ipv4"
              safi: "unicast"
              multipath: true
              default_originate:
                set: true
              weight: 4
      vrfs:
        - vrf: vrf1
          neighbors:
            - neighbor_address: 192.0.2.4
              address_family:
                - afi: "ipv4"
                  safi: "unicast"
                  multipath: true
                  default_originate:
                    set: true
                  capability_orf_prefix: both
        - vrf: vrf2
          neighbors:
            - neighbor_address: 192.0.2.5
              address_family:
                - afi: "ipv4"
                  safi: "unicast"
                  multipath: true
                  default_originate:
                    set: true
                  capability_orf_prefix: both
# Task output
# -------------
# commands:
# - router bgp 65536
# - neighbor 192.0.2.2
# - address-family ipv4 unicast
# - default-originate
# - multipath
# - weight 5
# - neighbor 192.0.2.3
# - address-family ipv4 unicast
# - default-originate
# - multipath
# - weight 4
# - vrf vrf1
# - neighbor 192.0.2.4
# - address-family ipv4 unicast
# - capability orf prefix both
# - default-originate
# - multipath
# - vrf vrf2
# - neighbor 192.0.2.5
# - address-family ipv4 unicast
# - capability orf prefix both
# - default-originate
# - multipath
#
#
# after:
#   as_number: 65536
#   neighbors:
#     - neighbor_address: 192.0.2.2
#       address_family:
#         - afi: "ipv4"
#           safi: "unicast"
#           multipath: true
#           default_originate:
#             set: true
#           weight: 5
#     - neighbor_address: 192.0.2.3
#       address_family:
#         - afi: "ipv4"
#           safi: "unicast"
#           multipath: true
#           default_originate:
#             set: true
#           weight: 4
#   vrfs:
#     - vrf: vrf1
#       neighbors:
#         - neighbor_address: 192.0.2.4
#           address_family:
#             - afi: "ipv4"
#               safi: "unicast"
#               multipath: true
#               default_originate:
#                 set: true
#               capability_orf_prefix: both
#     - vrf: vrf2
#       neighbors:
#         - neighbor_address: 192.0.2.5
#           address_family:
#             - afi: "ipv4"
#               safi: "unicast"
#               multipath: true
#               default_originate:
#                 set: true
#               capability_orf_prefix: both
#
#
# After state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#  address-family vpnv4 unicast
#  neighbor 192.0.2.2
#   remote-as 65537
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  neighbor 1.1.1.2
#   remote-as 65538
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  vrf vrf1
#   rd auto
#   neighbor 192.0.2.4
#    remote-as 65539
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate
#  vrf vrf2
#   rd auto
#   neighbor 192.0.2.5
#    remote-as 65540
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate
#
#
# Using delete
# Before state:
# -------------
#
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#  address-family vpnv4 unicast
#  neighbor 192.0.2.2
#   remote-as 65537
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  neighbor 192.0.2.3
#   remote-as 65538
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  vrf vrf1
#   rd auto
#   neighbor 192.0.2.4
#    remote-as 65539
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate
#  vrf vrf2
#   rd auto
#   neighbor 192.0.2.5
#    remote-as 65540
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate

- name:  Delete the provided configuration
  cisco.iosxr.iosxr_bgp_neighbor_address_family:
    state: deleted
    config:
      as_number: 65536
      neighbors:
        - neighbor_address: 192.0.2.2
          address_family:
            - afi: "ipv4"
              safi: "unicast"
              multipath: true
              default_originate:
                set: true
              weight: 5

# Task output
# -------------
#
# commands:
# - router bgp 65536
# - neighbor 192.0.2.2
# - no address-family ipv4 unicast
#
#
# after:
#   as_number: 65536
#   neighbors:
#     - neighbor_address: 192.0.2.3
#       address_family:
#         - afi: "ipv4"
#           safi: "unicast"
#           multipath: true
#           default_originate:
#             set: true
#           weight: 4
#   vrfs:
#     - vrf: vrf1
#       neighbors:
#         - neighbor_address: 192.0.2.4
#           address_family:
#             - afi: "ipv4"
#               safi: "unicast"
#               multipath: true
#               default_originate:
#                 set: true
#               capability_orf_prefix: both
#         - neighbor_address: 192.0.2.5
#           address_family:
#             - afi: "ipv4"
#               safi: "unicast"
#               multipath: true
#               default_originate:
#                 set: true
#               capability_orf_prefix: both
#
#
# Using Replaced
# Before state:
# -------------
#
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#  address-family vpnv4 unicast
#  neighbor 192.0.2.2
#   remote-as 65537
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  neighbor 192.0.2.3
#   remote-as 65538
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  vrf vrf1
#   rd auto
#   neighbor 192.0.2.4
#    remote-as 65539
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate
#  vrf vrf2
#   rd auto
#   neighbor 192.0.2.5
#    remote-as 65540
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate

- name: Replace the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_bgp_neighbor_address_family:
    state: replaced
    config:
      as_number: 65536
      neighbors:
        - neighbor_address: 192.0.2.2
          address_family:
            - afi: "ipv4"
              safi: "unicast"
              default_originate:
                set: true
              weight: 4
# Task output
# -------------
# commands:
# - router bgp 65536
# - neighbor 192.0.2.2
# - address-family ipv4 unicast
# - no multipath
# - weight 4
#
# after:
#   as_number: 65536
#   neighbors:
#     - neighbor_address: 192.0.2.2
#       address_family:
#         - afi: "ipv4"
#           safi: "unicast"
#           multipath: true
#           default_originate:
#             set: true
#           weight: 4
#     - neighbor_address: 192.0.2.3
#       address_family:
#         - afi: "ipv4"
#           safi: "unicast"
#           multipath: true
#           default_originate:
#             set: true
#           weight: 5
#   vrfs:
#     - vrf: vrf1
#       neighbors:
#         - neighbor_address: 192.0.2.4
#           address_family:
#             - afi: "ipv4"
#               safi: "unicast"
#               multipath: true
#               default_originate:
#                 set: true
#               capability_orf_prefix: both
#         - neighbor_address: 192.0.2.5
#           address_family:
#             - afi: "ipv4"
#               safi: "unicast"
#               multipath: true
#               default_originate:
#                 set: true
#               capability_orf_prefix: both
#
# After state:
# -------------
# Nexus9000v# show running-config router bgp
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#  address-family vpnv4 unicast
#  neighbor 192.0.2.2
#   remote-as 65537
#   address-family ipv4 unicast
#     multipath
#     weight 4
#     default-originate
#  neighbor 192.0.2.3
#   remote-as 65538
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  vrf vrf1
#   rd auto
#   neighbor 192.0.2.4
#    remote-as 65539
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate
#  vrf vrf2
#   rd auto
#   neighbor 192.0.2.5
#    remote-as 65540
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate
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
#  address-family vpnv4 unicast
#  neighbor 192.0.2.2
#   remote-as 65537
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  neighbor 192.0.2.3
#   remote-as 65538
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  vrf vrf1
#   rd auto
#   neighbor 192.0.2.4
#    remote-as 65539
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate
#  vrf vrf2
#   rd auto
#   neighbor 192.0.2.5
#    remote-as 65540
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate

- name:  override the provided configuration
  cisco.iosxr.iosxr_bgp_neighbor_address_family:
    state: overridden
    config:
      as_number: 65536
      neighbors:
        - neighbor_address: 192.0.2.2
          address_family:
            - afi: "ipv4"
              safi: "unicast"
              multipath: true
              default_originate:
                set: true
              weight: 5
# Task output
# -------------
#
# commands:
# - router bgp 65536
# - neighbor 192.0.2.3
# - no address-family ipv4 unicast
# - vrf vrf1
# - neighbor 192.0.2.4
# - no address-family ipv4 unicast
# - vrf vrf1
# - neighbor 192.0.2.5
# - no address-family ipv4 unicast
#
#
#
# after:
#   as_number: 65536
#   neighbors:
#     - neighbor_address: 192.0.2.2
#       address_family:
#         - afi: "ipv4"
#           safi: "unicast"
#           multipath: true
#           default_originate:
#             set: true
#           weight: 5
#
# After state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#  address-family vpnv4 unicast
#  neighbor 192.0.2.2
#   remote-as 65537
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#
#
#
# Using rendered
# Before state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.2.1
#  address-family ipv4 unicast
#  address-family vpnv4 unicast
#  neighbor 192.0.2.2
#   remote-as 65537
#  neighbor 192.0.2.3
#   remote-as 65538
#  vrf vrf1
#   rd auto
#   neighbor 192.0.2.4
#    remote-as 65539
#  vrf vrf2
#   rd auto
#   neighbor 192.0.2.5
#    remote-as 65540

- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.iosxr.iosxr_bgp_neighbor_address_family:
    state: rendered
    config:
      as_number: 65536
      neighbors:
        - neighbor_address: 192.0.2.2
          address_family:
            - afi: "ipv4"
              safi: "unicast"
              multipath: true
              default_originate:
                set: true
              weight: 5
        - neighbor_address: 192.0.2.3
          address_family:
            - afi: "ipv4"
              safi: "unicast"
              multipath: true
              default_originate:
                set: true
              weight: 4
      vrfs:
        - vrf: vrf1
          neighbors:
            - neighbor_address: 192.0.2.4
              address_family:
                - afi: "ipv4"
                  safi: "unicast"
                  multipath: true
                  default_originate:
                    set: true
                  capability_orf_prefix: both
        - vrf: vrf2
          neighbors:
            - neighbor_address: 192.0.2.5
              address_family:
                - afi: "ipv4"
                  safi: "unicast"
                  multipath: true
                  default_originate:
                    set: true
                  capability_orf_prefix: both
# Task output
# -------------
# commands:
# - router bgp 65536
# - neighbor 192.0.2.2
# - address-family ipv4 unicast
# - default-originate
# - multipath
# - weight 5
# - neighbor 192.0.2.3
# - address-family ipv4 unicast
# - default-originate
# - multipath
# - weight 4
# - vrf vrf1
# - neighbor 192.0.2.4
# - address-family ipv4 unicast
# - capability orf prefix both
# - default-originate
# - multipath
# - vrf vrf2
# - neighbor 192.0.2.5
# - address-family ipv4 unicast
# - capability orf prefix both
# - default-originate
# - multipath
#
# Using parsed
#
#parsed.cfg
#------------
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#  address-family vpnv4 unicast
#  neighbor 192.0.2.2
#   remote-as 65537
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  neighbor 1.1.1.2
#   remote-as 65538
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  vrf vrf1
#   rd auto
#   neighbor 192.0.2.4
#    remote-as 65539
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate
#  vrf vrf2
#   rd auto
#   neighbor 192.0.2.5
#    remote-as 65540
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate

- name: Parse externally provided BGP neighbor AF config
  cisco.iosxr.iosxr_bgp_neighbor_address_family:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed
# Task output (redacted)
# -----------------------
# parsed:
#   as_number: 65536
#   neighbors:
#     - neighbor_address: 192.0.2.2
#       address_family:
#         - afi: "ipv4"
#           safi: "unicast"
#           multipath: true
#           default_originate:
#             set: true
#           weight: 5
#     - neighbor_address: 192.0.2.3
#       address_family:
#         - afi: "ipv4"
#           safi: "unicast"
#           multipath: true
#           default_originate:
#             set: true
#           weight: 4
#   vrfs:
#     - vrf: vrf1
#       neighbors:
#         - neighbor_address: 192.0.2.4
#           address_family:
#             - afi: "ipv4"
#               safi: "unicast"
#               multipath: true
#               default_originate:
#                 set: true
#               capability_orf_prefix: both
#     - vrf: vrf2
#       neighbors:
#         - neighbor_address: 192.0.2.5
#           address_family:
#             - afi: "ipv4"
#               safi: "unicast"
#               multipath: true
#               default_originate:
#                 set: true
#               capability_orf_prefix: both
#
#
#Using Gathered
#-----------------
# Before state state:
# -------------
# RP/0/0/CPU0:iosxr-02#show running-config router bgp
# Sat Feb 20 03:49:43.618 UTC
# router bgp 65536
#  bgp router-id 192.0.1.1
#  address-family ipv4 unicast
#  address-family vpnv4 unicast
#  neighbor 192.0.2.2
#   remote-as 65537
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  neighbor 1.1.1.2
#   remote-as 65538
#   address-family ipv4 unicast
#     multipath
#     weight 5
#     default-originate
#  vrf vrf1
#   rd auto
#   neighbor 192.0.2.4
#    remote-as 65539
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate
#  vrf vrf2
#   rd auto
#   neighbor 192.0.2.5
#    remote-as 65540
#    address-family ipv4 unicast
#     multipath
#     capability orf prefix both
#     default-originate
#
#
#
- name: Gathered the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_bgp_neighbor_address_family:
        config:
        state: gathered

# Task output
# -----------------------
# gathered:
#   as_number: 65536
#   neighbors:
#     - neighbor_address: 192.0.2.2
#       address_family:
#         - afi: "ipv4"
#           safi: "unicast"
#           multipath: true
#           default_originate:
#             set: true
#           weight: 5
#     - neighbor_address: 192.0.2.3
#       address_family:
#         - afi: "ipv4"
#           safi: "unicast"
#           multipath: true
#           default_originate:
#             set: true
#           weight: 4
#   vrfs:
#     - vrf: vrf1
#       neighbors:
#         - neighbor_address: 192.0.2.4
#           address_family:
#             - afi: "ipv4"
#               safi: "unicast"
#               multipath: true
#               default_originate:
#                 set: true
#               capability_orf_prefix: both
#     - vrf: vrf2
#       neighbors:
#         - neighbor_address: 192.0.2.5
#           address_family:
#             - afi: "ipv4"
#               safi: "unicast"
#               multipath: true
#               default_originate:
#                 set: true
#               capability_orf_prefix: both
#
```

### Authors

- Ashwini Mhatre (@amhatre)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
