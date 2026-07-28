---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_bgp_neighbor_address_family module – BGP Neighbor Address Family resource module."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_bgp_neighbor_address_family_module.html
fetched_at: 2026-07-27T17:01:42+00:00
---
# cisco.nxos.nxos_bgp_neighbor_address_family module – BGP Neighbor Address Family resource module.

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/cisco/nxos) (version 3.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_bgp_neighbor_address_family`.

New in cisco.nxos 2.0.0

- [Synopsis](nxos_bgp_neighbor_address_family_module.md#synopsis)
- [Parameters](nxos_bgp_neighbor_address_family_module.md#parameters)
- [Notes](nxos_bgp_neighbor_address_family_module.md#notes)
- [Examples](nxos_bgp_neighbor_address_family_module.md#examples)

## [Synopsis](nxos_bgp_neighbor_address_family_module.md#id1)

- This module manages BGP Neighbor Address Family configuration on devices running Cisco NX-OS.

## [Parameters](nxos_bgp_neighbor_address_family_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  dictionary | BGP Neighbor AF configuration. |
| **as_number**  string | Autonomous System Number of the router. |
| **neighbors**  list / elements=dictionary | A list of BGP Neighbor AF configuration. |
| **address_family**  list / elements=dictionary | BGP Neighbor Address Family related configurations. |
| **advertise_map**  dictionary | Specify route-map for conditional advertisement. |
| **exist_map**  string | Condition route-map to advertise only when prefix in condition exists. |
| **non_exist_map**  string | Condition route-map to advertise only when prefix in condition does not exist. |
| **route_map**  string / required | Route-map name. |
| **advertisement_interval**  integer | Minimum interval between sending BGP routing updates. |
| **afi**  string / required | Address Family indicator.  Choices:   - `"ipv4"` - `"ipv6"` - `"link-state"` - `"vpnv4"` - `"vpnv6"` - `"l2vpn"` |
| **allowas_in**  dictionary | Accept as-path with my AS present in it. |
| **max_occurences**  integer | Number of occurrences of AS number, default is 3. |
| **set**  boolean | Activate allowas-in property.  Choices:   - `false` - `true` |
| **as_override**  boolean | Override matching AS-number while sending update.  Choices:   - `false` - `true` |
| **capability**  dictionary | Advertise capability to the peer. |
| **additional_paths**  dictionary | Additional paths capability. |
| **receive**  string | Additional paths Receive capability.  Choices:   - `"enable"` - `"disable"` |
| **send**  string | Additional paths Send capability.  Choices:   - `"enable"` - `"disable"` |
| **default_originate**  dictionary | Originate a default toward this peer. |
| **route_map**  string | Route-map to specify criteria for originating default. |
| **set**  boolean | Set default-originate attribute.  Choices:   - `false` - `true` |
| **disable_peer_as_check**  boolean | Disable checking of peer AS-number while advertising.  Choices:   - `false` - `true` |
| **filter_list**  dictionary | Name of filter-list. |
| **inbound**  string | Apply policy to incoming routes. |
| **outbound**  string | Apply policy to outgoing routes. |
| **inherit**  dictionary | Inherit a template. |
| **sequence**  integer | Sequence number. |
| **template**  string | Template name. |
| **maximum_prefix**  dictionary | Maximum number of prefixes from this neighbor. |
| **generate_warning_threshold**  integer | Threshold percentage at which to generate a warning. |
| **max_prefix_limit**  integer | Maximum prefix limit. |
| **restart_interval**  integer | Restart bgp connection after limit is exceeded. |
| **warning_only**  boolean | Only give a warning message when limit is exceeded.  Choices:   - `false` - `true` |
| **next_hop_self**  dictionary | Set our address as nexthop (non-reflected). |
| **all_routes**  boolean | Set our address as nexthop for all routes.  Choices:   - `false` - `true` |
| **set**  boolean | Set next-hop-self attribute.  Choices:   - `false` - `true` |
| **next_hop_third_party**  boolean | Compute a third-party nexthop if possible.  Choices:   - `false` - `true` |
| **prefix_list**  dictionary | Apply prefix-list. |
| **inbound**  string | Apply policy to incoming routes. |
| **outbound**  string | Apply policy to outgoing routes. |
| **rewrite_evpn_rt_asn**  boolean | Auto generate RTs for EBGP neighbor.  Choices:   - `false` - `true` |
| **route_map**  dictionary | Apply route-map to neighbor. |
| **inbound**  string | Apply policy to incoming routes. |
| **outbound**  string | Apply policy to outgoing routes. |
| **route_reflector_client**  boolean | Configure a neighbor as Route reflector client.  Choices:   - `false` - `true` |
| **safi**  string | Sub Address Family indicator.  Choices:   - `"unicast"` - `"multicast"` - `"mvpn"` - `"evpn"` |
| **send_community**  dictionary | Send Community attribute to this neighbor. |
| **both**  boolean | Send Standard and Extended Community attributes.  Choices:   - `false` - `true` |
| **extended**  boolean | Send Extended Community attribute.  Choices:   - `false` - `true` |
| **set**  boolean | Set send-community attribute.  Choices:   - `false` - `true` |
| **standard**  boolean | Send Standard Community attribute.  Choices:   - `false` - `true` |
| **soft_reconfiguration_inbound**  dictionary | Soft reconfiguration. |
| **always**  boolean | Always perform inbound soft reconfiguration.  Choices:   - `false` - `true` |
| **set**  boolean | Set soft-reconfiguration inbound attribute.  Choices:   - `false` - `true` |
| **soo**  string | Specify Site-of-origin extcommunity. |
| **suppress_inactive**  boolean | Advertise only active routes to peer.  Choices:   - `false` - `true` |
| **unsuppress_map**  string | Route-map to selectively unsuppress suppressed routes. |
| **weight**  integer | Set default weight for routes from this neighbor. |
| **neighbor_address**  string / required | IP/IPv6 address of the neighbor. |
| **vrfs**  list / elements=dictionary | Virtual Router Context. |
| **neighbors**  list / elements=dictionary | A list of BGP Neighbor AF configuration. |
| **address_family**  list / elements=dictionary | BGP Neighbor Address Family related configurations. |
| **advertise_map**  dictionary | Specify route-map for conditional advertisement. |
| **exist_map**  string | Condition route-map to advertise only when prefix in condition exists. |
| **non_exist_map**  string | Condition route-map to advertise only when prefix in condition does not exist. |
| **route_map**  string / required | Route-map name. |
| **advertisement_interval**  integer | Minimum interval between sending BGP routing updates. |
| **afi**  string / required | Address Family indicator.  Choices:   - `"ipv4"` - `"ipv6"` - `"link-state"` - `"vpnv4"` - `"vpnv6"` - `"l2vpn"` |
| **allowas_in**  dictionary | Accept as-path with my AS present in it. |
| **max_occurences**  integer | Number of occurrences of AS number, default is 3. |
| **set**  boolean | Activate allowas-in property.  Choices:   - `false` - `true` |
| **as_override**  boolean | Override matching AS-number while sending update.  Choices:   - `false` - `true` |
| **capability**  dictionary | Advertise capability to the peer. |
| **additional_paths**  dictionary | Additional paths capability. |
| **receive**  string | Additional paths Receive capability.  Choices:   - `"enable"` - `"disable"` |
| **send**  string | Additional paths Send capability.  Choices:   - `"enable"` - `"disable"` |
| **default_originate**  dictionary | Originate a default toward this peer. |
| **route_map**  string | Route-map to specify criteria for originating default. |
| **set**  boolean | Set default-originate attribute.  Choices:   - `false` - `true` |
| **disable_peer_as_check**  boolean | Disable checking of peer AS-number while advertising.  Choices:   - `false` - `true` |
| **filter_list**  dictionary | Name of filter-list. |
| **inbound**  string | Apply policy to incoming routes. |
| **outbound**  string | Apply policy to outgoing routes. |
| **inherit**  dictionary | Inherit a template. |
| **sequence**  integer | Sequence number. |
| **template**  string | Template name. |
| **maximum_prefix**  dictionary | Maximum number of prefixes from this neighbor. |
| **generate_warning_threshold**  integer | Threshold percentage at which to generate a warning. |
| **max_prefix_limit**  integer | Maximum prefix limit. |
| **restart_interval**  integer | Restart bgp connection after limit is exceeded. |
| **warning_only**  boolean | Only give a warning message when limit is exceeded.  Choices:   - `false` - `true` |
| **next_hop_self**  dictionary | Set our address as nexthop (non-reflected). |
| **all_routes**  boolean | Set our address as nexthop for all routes.  Choices:   - `false` - `true` |
| **set**  boolean | Set next-hop-self attribute.  Choices:   - `false` - `true` |
| **next_hop_third_party**  boolean | Compute a third-party nexthop if possible.  Choices:   - `false` - `true` |
| **prefix_list**  dictionary | Apply prefix-list. |
| **inbound**  string | Apply policy to incoming routes. |
| **outbound**  string | Apply policy to outgoing routes. |
| **rewrite_evpn_rt_asn**  boolean | Auto generate RTs for EBGP neighbor.  Choices:   - `false` - `true` |
| **route_map**  dictionary | Apply route-map to neighbor. |
| **inbound**  string | Apply policy to incoming routes. |
| **outbound**  string | Apply policy to outgoing routes. |
| **route_reflector_client**  boolean | Configure a neighbor as Route reflector client.  Choices:   - `false` - `true` |
| **safi**  string | Sub Address Family indicator.  Choices:   - `"unicast"` - `"multicast"` - `"mvpn"` - `"evpn"` |
| **send_community**  dictionary | Send Community attribute to this neighbor. |
| **both**  boolean | Send Standard and Extended Community attributes.  Choices:   - `false` - `true` |
| **extended**  boolean | Send Extended Community attribute.  Choices:   - `false` - `true` |
| **set**  boolean | Set send-community attribute.  Choices:   - `false` - `true` |
| **standard**  boolean | Send Standard Community attribute.  Choices:   - `false` - `true` |
| **soft_reconfiguration_inbound**  dictionary | Soft reconfiguration. |
| **always**  boolean | Always perform inbound soft reconfiguration.  Choices:   - `false` - `true` |
| **set**  boolean | Set soft-reconfiguration inbound attribute.  Choices:   - `false` - `true` |
| **soo**  string | Specify Site-of-origin extcommunity. |
| **suppress_inactive**  boolean | Advertise only active routes to peer.  Choices:   - `false` - `true` |
| **unsuppress_map**  string | Route-map to selectively unsuppress suppressed routes. |
| **weight**  integer | Set default weight for routes from this neighbor. |
| **neighbor_address**  string / required | IP/IPv6 address of the neighbor. |
| **vrf**  string | VRF name. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the command **show running-config | section ‘^router bgp’**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  State *deleted* only removes BGP attributes that this modules manages and does not negate the BGP process completely.  Refer to examples for more details.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"parsed"` - `"gathered"` - `"rendered"` |

## [Notes](nxos_bgp_neighbor_address_family_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 9.3.6.
> - Unsupported for Cisco MDS
> - For managing BGP address family configurations please use the [cisco.nxos.nxos_bgp_address_family](nxos_bgp_address_family_module.md#ansible-collections-cisco-nxos-nxos-bgp-address-family-module) module.
> - This module works with connection `network_cli` and `httpapi`.

## [Examples](nxos_bgp_neighbor_address_family_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# Nexus9000v#

- name: Merge the provided configuration with the existing running configuration
  cisco.nxos.nxos_bgp_neighbor_address_family: &id001
    config:
      as_number: 65536
      neighbors:
        - neighbor_address: 192.0.2.32
          address_family:
            - afi: ipv4
              safi: unicast
              maximum_prefix:
                max_prefix_limit: 20
                generate_warning_threshold: 75
              weight: 100
              prefix_list:
                inbound: rmap1
                outbound: rmap2
            - afi: ipv6
              safi: unicast
        - neighbor_address: 192.0.2.33
          address_family:
            - afi: ipv4
              safi: multicast
              inherit:
                template: BasePolicy
                sequence: 200
      vrfs:
        - vrf: site-1
          neighbors:
            - neighbor_address: 203.0.113.1
              address_family:
                - afi: ipv4
                  safi: unicast
                  suppress_inactive: True
                  next_hop_self:
                    set: True
            - neighbor_address: 203.0.113.2
              address_family:
                - afi: ipv6
                  safi: unicast
                - afi: ipv4
                  safi: multicast
                  send_community:
                    set: True

# Task output
# -------------
#  before: {}
#
#  commands:
#  - router bgp 65536
#  - neighbor 192.0.2.32
#  - address-family ipv4 unicast
#  - maximum-prefix 20 75
#  - weight 100
#  - prefix-list rmap1 in
#  - prefix-list rmap2 out
#  - address-family ipv6 unicast
#  - neighbor 192.0.2.33
#  - address-family ipv4 multicast
#  - inherit peer-policy BasePolicy 200
#  - vrf site-1
#  - neighbor 203.0.113.1
#  - address-family ipv4 unicast
#  - suppress-inactive
#  - next-hop-self
#  - neighbor 203.0.113.2
#  - address-family ipv6 unicast
#  - address-family ipv4 multicast
#  - send-community
#
#  after:
#    as_number: "65536"
#    neighbors:
#      - neighbor_address: 192.0.2.32
#        address_family:
#          - afi: ipv4
#            safi: unicast
#            maximum_prefix:
#              max_prefix_limit: 20
#              generate_warning_threshold: 75
#            weight: 100
#            prefix_list:
#              inbound: rmap1
#              outbound: rmap2
#          - afi: ipv6
#            safi: unicast
#      - neighbor_address: 192.0.2.33
#        address_family:
#          - afi: ipv4
#            safi: multicast
#            inherit:
#              template: BasePolicy
#              sequence: 200
#    vrfs:
#      - vrf: site-1
#        neighbors:
#          - neighbor_address: 203.0.113.1
#            address_family:
#              - afi: ipv4
#                safi: unicast
#                suppress_inactive: true
#                next_hop_self:
#                  set: true
#          - neighbor_address: 203.0.113.2
#            address_family:
#              - afi: ipv4
#                safi: multicast
#                send_community:
#                  set: True
#              - afi: ipv6
#                safi: unicast

# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   neighbor 192.0.2.32
#     address-family ipv4 unicast
#       maximum-prefix 20 75
#       weight 100
#       prefix-list rmap1 in
#       prefix-list rmap2 out
#     address-family ipv6 unicast
#   neighbor 192.0.2.33
#     address-family ipv4 multicast
#       inherit peer-policy BasePolicy 200
#   vrf site-1
#     neighbor 203.0.113.1
#       address-family ipv4 unicast
#         suppress-inactive
#         next-hop-self
#     neighbor 203.0.113.2
#       address-family ipv4 multicast
#         send-community
#       address-family ipv6 unicast
#

# Using replaced

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   neighbor 192.0.2.32
#     address-family ipv4 unicast
#       maximum-prefix 20 75
#       weight 100
#       prefix-list rmap1 in
#       prefix-list rmap2 out
#     address-family ipv6 unicast
#   neighbor 192.0.2.33
#     address-family ipv4 multicast
#       inherit peer-policy BasePolicy 200
#   vrf site-1
#     neighbor 203.0.113.1
#       address-family ipv4 unicast
#         suppress-inactive
#         next-hop-self
#     neighbor 203.0.113.2
#       address-family ipv4 multicast
#         send-community
#       address-family ipv6 unicast
#

- name: Replace specified neighbor AFs with given configuration
  cisco.nxos.nxos_bgp_neighbor_address_family: &replaced
    config:
      as_number: 65536
      neighbors:
        - neighbor_address: 192.0.2.32
          address_family:
            - afi: ipv4
              safi: unicast
              weight: 110
            - afi: ipv6
              safi: unicast
        - neighbor_address: 192.0.2.33
          address_family:
            - afi: ipv4
              safi: multicast
              inherit:
                template: BasePolicy
                sequence: 200
      vrfs:
        - vrf: site-1
          neighbors:
            - neighbor_address: 203.0.113.1
              address_family:
                - afi: ipv4
                  safi: unicast
            - neighbor_address: 203.0.113.2
              address_family:
                - afi: ipv6
                  safi: unicast
                - afi: ipv4
                  safi: multicast
                  send_community:
                    set: True
    state: replaced

# Task output
# -------------
#  before:
#    as_number: "65536"
#    neighbors:
#      - neighbor_address: 192.0.2.32
#        address_family:
#          - afi: ipv4
#            safi: unicast
#            maximum_prefix:
#              max_prefix_limit: 20
#              generate_warning_threshold: 75
#            weight: 100
#            prefix_list:
#              inbound: rmap1
#              outbound: rmap2
#          - afi: ipv6
#            safi: unicast
#      - neighbor_address: 192.0.2.33
#        address_family:
#          - afi: ipv4
#            safi: multicast
#            inherit:
#              template: BasePolicy
#              sequence: 200
#    vrfs:
#      - vrf: site-1
#        neighbors:
#          - neighbor_address: 203.0.113.1
#            address_family:
#              - afi: ipv4
#                safi: unicast
#                suppress_inactive: true
#                next_hop_self:
#                  set: true
#          - neighbor_address: 203.0.113.2
#            address_family:
#              - afi: ipv4
#                safi: multicast
#                send_community:
#                  set: True
#              - afi: ipv6
#                safi: unicast
#
#  commands:
#    - router bgp 65536
#    - neighbor 192.0.2.32
#    - address-family ipv4 unicast
#    - no maximum-prefix 20 75
#    - weight 110
#    - no prefix-list rmap1 in
#    - no prefix-list rmap2 out
#    - vrf site-1
#    - neighbor 203.0.113.1
#    - address-family ipv4 unicast
#    - no suppress-inactive
#    - no next-hop-self
#
#  after:
#    as_number: "65536"
#    neighbors:
#      - neighbor_address: 192.0.2.32
#        address_family:
#          - afi: ipv4
#            safi: unicast
#            weight: 110
#          - afi: ipv6
#            safi: unicast
#      - neighbor_address: 192.0.2.33
#        address_family:
#          - afi: ipv4
#            safi: multicast
#            inherit:
#              template: BasePolicy
#              sequence: 200
#    vrfs:
#      - vrf: site-1
#        neighbors:
#          - neighbor_address: 203.0.113.1
#            address_family:
#              - afi: ipv4
#                safi: unicast
#          - neighbor_address: 203.0.113.2
#            address_family:
#              - afi: ipv4
#                safi: multicast
#                send_community:
#                  set: True
#              - afi: ipv6
#                safi: unicast

# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   neighbor 192.0.2.32
#     address-family ipv4 unicast
#       weight 110
#     address-family ipv6 unicast
#   neighbor 192.0.2.33
#     address-family ipv4 multicast
#       inherit peer-policy BasePolicy 200
#   vrf site-1
#     neighbor 203.0.113.1
#       address-family ipv4 unicast
#     neighbor 203.0.113.2
#       address-family ipv4 multicast
#         send-community
#       address-family ipv6 unicast
#

# Using overridden

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   neighbor 192.0.2.32
#     address-family ipv4 unicast
#       maximum-prefix 20 75
#       weight 100
#       prefix-list rmap1 in
#       prefix-list rmap2 out
#     address-family ipv6 unicast
#   neighbor 192.0.2.33
#     address-family ipv4 multicast
#       inherit peer-policy BasePolicy 200
#   vrf site-1
#     neighbor 203.0.113.1
#       address-family ipv4 unicast
#         suppress-inactive
#         next-hop-self
#     neighbor 203.0.113.2
#       address-family ipv4 multicast
#         send-community
#       address-family ipv6 unicast
#

- name: Override all BGP AF configuration with provided configuration
  cisco.nxos.nxos_bgp_neighbor_address_family:
    config:
      as_number: 65536
      neighbors:
        - neighbor_address: 192.0.2.32
          address_family:
            - afi: ipv4
              safi: unicast
      vrfs:
        - vrf: site-1
          neighbors:
            - neighbor_address: 203.0.113.1
              address_family:
                - afi: ipv4
                  safi: unicast
                  suppress_inactive: True
                  next_hop_self:
                    set: True
    state: overridden

# Task output
# -------------
#  before:
#    as_number: "65536"
#    neighbors:
#      - neighbor_address: 192.0.2.32
#        address_family:
#          - afi: ipv4
#            safi: unicast
#            maximum_prefix:
#              max_prefix_limit: 20
#              generate_warning_threshold: 75
#            weight: 100
#            prefix_list:
#              inbound: rmap1
#              outbound: rmap2
#          - afi: ipv6
#            safi: unicast
#      - neighbor_address: 192.0.2.33
#        address_family:
#          - afi: ipv4
#            safi: multicast
#            inherit:
#              template: BasePolicy
#              sequence: 200
#    vrfs:
#      - vrf: site-1
#        neighbors:
#          - neighbor_address: 203.0.113.1
#            address_family:
#              - afi: ipv4
#                safi: unicast
#                suppress_inactive: true
#                next_hop_self:
#                  set: true
#          - neighbor_address: 203.0.113.2
#            address_family:
#              - afi: ipv4
#                safi: multicast
#                send_community:
#                  set: True
#              - afi: ipv6
#                safi: unicast
#
#  commands:
#    - router bgp 65536
#    - neighbor 192.0.2.32
#    - address-family ipv4 unicast
#    - no maximum-prefix 20 75
#    - no weight 100
#    - no prefix-list rmap1 in
#    - no prefix-list rmap2 out
#    - no address-family ipv6 unicast
#    - neighbor 192.0.2.33
#    - no address-family ipv4 multicast
#    - vrf site-1
#    - neighbor 203.0.113.2
#    - no address-family ipv4 multicast
#    - no address-family ipv6 unicast
#
#  after:
#    as_number: "65536"
#    neighbors:
#      - neighbor_address: 192.0.2.32
#        address_family:
#          - afi: ipv4
#            safi: unicast
#    vrfs:
#      - vrf: site-1
#        neighbors:
#          - neighbor_address: 203.0.113.1
#            address_family:
#              - afi: ipv4
#                safi: unicast
#                suppress_inactive: True
#                next_hop_self:
#                  set: True

# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   neighbor 192.0.2.32
#     address-family ipv4 unicast
#   vrf site-1
#     neighbor 203.0.113.1
#       address-family ipv4 unicast
#         suppress-inactive
#         next-hop-self

# Using deleted to remove specified neighbor AFs

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   neighbor 192.0.2.32
#     address-family ipv4 unicast
#       maximum-prefix 20 75
#       weight 100
#       prefix-list rmap1 in
#       prefix-list rmap2 out
#     address-family ipv6 unicast
#   neighbor 192.0.2.33
#     address-family ipv4 multicast
#       inherit peer-policy BasePolicy 200
#   vrf site-1
#     neighbor 203.0.113.1
#       address-family ipv4 unicast
#         suppress-inactive
#         next-hop-self
#     neighbor 203.0.113.2
#       address-family ipv4 multicast
#         send-community
#       address-family ipv6 unicast
#

- name: Delete BGP configs handled by this module
  cisco.nxos.nxos_bgp_neighbor_address_family:
    config:
      as_number: 65536
      neighbors:
        - neighbor_address: 192.0.2.32
          address_family:
            - afi: ipv4
              safi: unicast
      vrfs:
        - vrf: site-1
          neighbors:
            - neighbor_address: 203.0.113.2
              address_family:
                - afi: ipv6
                  safi: unicast
    state: deleted

# Task output
# -------------
#  before:
#    as_number: "65536"
#    neighbors:
#      - neighbor_address: 192.0.2.32
#        address_family:
#          - afi: ipv4
#            safi: unicast
#            maximum_prefix:
#              max_prefix_limit: 20
#              generate_warning_threshold: 75
#            weight: 100
#            prefix_list:
#              inbound: rmap1
#              outbound: rmap2
#          - afi: ipv6
#            safi: unicast
#      - neighbor_address: 192.0.2.33
#        address_family:
#          - afi: ipv4
#            safi: multicast
#            inherit:
#              template: BasePolicy
#              sequence: 200
#    vrfs:
#      - vrf: site-1
#        neighbors:
#          - neighbor_address: 203.0.113.1
#            address_family:
#              - afi: ipv4
#                safi: unicast
#                suppress_inactive: true
#                next_hop_self:
#                  set: true
#          - neighbor_address: 203.0.113.2
#            address_family:
#              - afi: ipv4
#                safi: multicast
#                send_community:
#                  set: True
#              - afi: ipv6
#                safi: unicast
#
#  commands:
#    - router bgp 65536
#    - neighbor 192.0.2.32
#    - no address-family ipv4 unicast
#    - vrf site-1
#    - neighbor 203.0.113.2
#    - no address-family ipv6 unicast
#
#  after:
#    as_number: "65536"
#    neighbors:
#      - neighbor_address: 192.0.2.32
#        address_family:
#          - afi: ipv6
#            safi: unicast
#      - neighbor_address: 192.0.2.33
#        address_family:
#          - afi: ipv4
#            safi: multicast
#            inherit:
#              template: BasePolicy
#              sequence: 200
#    vrfs:
#      - vrf: site-1
#        neighbors:
#          - neighbor_address: 203.0.113.1
#            address_family:
#              - afi: ipv4
#                safi: unicast
#                suppress_inactive: true
#                next_hop_self:
#                  set: true
#          - neighbor_address: 203.0.113.2
#            address_family:
#              - afi: ipv4
#                safi: multicast
#                send_community:
#                  set: True
#
# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   neighbor 192.0.2.32
#     address-family ipv6 unicast
#   neighbor 192.0.2.33
#     address-family ipv4 multicast
#       inherit peer-policy BasePolicy 200
#   vrf site-1
#     neighbor 203.0.113.1
#       address-family ipv4 unicast
#         suppress-inactive
#         next-hop-self
#     neighbor 203.0.113.2
#       address-family ipv4 multicast
#         send-community
#

# Using deleted to remove all neighbor AFs

# Before state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   neighbor 192.0.2.32
#     address-family ipv4 unicast
#       maximum-prefix 20 75
#       weight 100
#       prefix-list rmap1 in
#       prefix-list rmap2 out
#     address-family ipv6 unicast
#   neighbor 192.0.2.33
#     address-family ipv4 multicast
#       inherit peer-policy BasePolicy 200
#   vrf site-1
#     neighbor 203.0.113.1
#       address-family ipv4 unicast
#         suppress-inactive
#         next-hop-self
#     neighbor 203.0.113.2
#       address-family ipv4 multicast
#         send-community
#       address-family ipv6 unicast
#

- name: Delete all BGP neighbor AF configs handled by this module
  cisco.nxos.nxos_bgp_neighbor_address_family:
    state: deleted

# Task output
# -------------
#  before:
#    as_number: "65536"
#    neighbors:
#      - neighbor_address: 192.0.2.32
#        address_family:
#          - afi: ipv4
#            safi: unicast
#            maximum_prefix:
#              max_prefix_limit: 20
#              generate_warning_threshold: 75
#            weight: 100
#            prefix_list:
#              inbound: rmap1
#              outbound: rmap2
#          - afi: ipv6
#            safi: unicast
#      - neighbor_address: 192.0.2.33
#        address_family:
#          - afi: ipv4
#            safi: multicast
#            inherit:
#              template: BasePolicy
#              sequence: 200
#    vrfs:
#      - vrf: site-1
#        neighbors:
#          - neighbor_address: 203.0.113.1
#            address_family:
#              - afi: ipv4
#                safi: unicast
#                suppress_inactive: true
#                next_hop_self:
#                  set: true
#          - neighbor_address: 203.0.113.2
#            address_family:
#              - afi: ipv4
#                safi: multicast
#                send_community:
#                  set: True
#              - afi: ipv6
#                safi: unicast
#
#  commands:
#    - router bgp 65536
#    - neighbor 192.0.2.32
#    - no address-family ipv4 unicast
#    - no address-family ipv6 unicast
#    - neighbor 192.0.2.33
#    - no address-family ipv4 multicast
#    - vrf site-1
#    - neighbor 203.0.113.1
#    - no address-family ipv4 unicast
#    - neighbor 203.0.113.2
#    - no address-family ipv6 unicast
#    - no address-family ipv4 multicast
#
#  after:
#    as_number: "65536"
#
# After state:
# -------------
# Nexus9000v# show running-config | section "^router bgp"
# router bgp 65536
#   neighbor 192.0.2.32
#   neighbor 192.0.2.33
#   vrf site-1
#     neighbor 203.0.113.1
#     neighbor 203.0.113.2
#

# Using rendered

- name: Render platform specific configuration lines with state rendered (without connecting to the device)
  cisco.nxos.nxos_bgp_neighbor_address_family:
    config:
      as_number: 65536
      neighbors:
        - neighbor_address: 192.0.2.32
          address_family:
            - afi: ipv4
              safi: unicast
              maximum_prefix:
                max_prefix_limit: 20
                generate_warning_threshold: 75
              weight: 100
              prefix_list:
                inbound: rmap1
                outbound: rmap2
            - afi: ipv6
              safi: unicast
        - neighbor_address: 192.0.2.33
          address_family:
            - afi: ipv4
              safi: multicast
              inherit:
                template: BasePolicy
                sequence: 200
      vrfs:
        - vrf: site-1
          neighbors:
            - neighbor_address: 203.0.113.1
              address_family:
                - afi: ipv4
                  safi: unicast
                  suppress_inactive: True
                  next_hop_self:
                    set: True
            - neighbor_address: 203.0.113.2
              address_family:
                - afi: ipv6
                  safi: unicast
                - afi: ipv4
                  safi: multicast
                  send_community:
                    set: True
    state: rendered

# Task Output (redacted)
# -----------------------
#  rendered:
#    - router bgp 65536
#    - neighbor 192.0.2.32
#    - address-family ipv4 unicast
#    - maximum-prefix 20 75
#    - weight 100
#    - prefix-list rmap1 in
#    - prefix-list rmap2 out
#    - address-family ipv6 unicast
#    - neighbor 192.0.2.33
#    - address-family ipv4 multicast
#    - inherit peer-policy BasePolicy 200
#    - vrf site-1
#    - neighbor 203.0.113.1
#    - address-family ipv4 unicast
#    - suppress-inactive
#    - next-hop-self
#    - neighbor 203.0.113.2
#    - address-family ipv6 unicast
#    - address-family ipv4 multicast
#    - send-community

# Using parsed

# parsed.cfg
# ------------
# router bgp 65536
#   neighbor 192.0.2.32
#     address-family ipv4 unicast
#       maximum-prefix 20 75
#       weight 100
#       prefix-list rmap1 in
#       prefix-list rmap2 out
#     address-family ipv6 unicast
#   neighbor 192.0.2.33
#     address-family ipv4 multicast
#       inherit peer-policy BasePolicy 200
#   vrf site-1
#     neighbor 203.0.113.1
#       address-family ipv4 unicast
#         suppress-inactive
#         next-hop-self
#     neighbor 203.0.113.2
#       address-family ipv4 multicast
#         send-community
#       address-family ipv6 unicast

- name: Parse externally provided BGP neighbor AF config
  register: result
  cisco.nxos.nxos_bgp_neighbor_address_family:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
#  parsed:
#    as_number: "65536"
#    neighbors:
#      - neighbor_address: 192.0.2.32
#        address_family:
#          - afi: ipv4
#           safi: unicast
#           maximum_prefix:
#              max_prefix_limit: 20
#              generate_warning_threshold: 75
#           weight: 100
#            prefix_list:
#              inbound: rmap1
#              outbound: rmap2
#          - afi: ipv6
#            safi: unicast
#      - neighbor_address: 192.0.2.33
#        address_family:
#          - afi: ipv4
#            safi: multicast
#            inherit:
#              template: BasePolicy
#              sequence: 200
#    vrfs:
#      - vrf: site-1
#        neighbors:
#          - neighbor_address: 203.0.113.1
#            address_family:
#              - afi: ipv4
#                safi: unicast
#                suppress_inactive: true
#                next_hop_self:
#                  set: true
#          - neighbor_address: 203.0.113.2
#            address_family:
#              - afi: ipv4
#                safi: multicast
#                send_community:
#                  set: True
#              - afi: ipv6
#                safi: unicast
```

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
