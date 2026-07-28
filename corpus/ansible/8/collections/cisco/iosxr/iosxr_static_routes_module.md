---
collection: ansible
version: "8"
title: "cisco.iosxr.iosxr_static_routes module – Resource module to configure static routes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/iosxr/iosxr_static_routes_module.html
fetched_at: 2026-07-28T01:26:59+00:00
---
# cisco.iosxr.iosxr_static_routes module – Resource module to configure static routes.

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
> To use it in a playbook, specify: `cisco.iosxr.iosxr_static_routes`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_static_routes_module.md#synopsis)
- [Parameters](iosxr_static_routes_module.md#parameters)
- [Examples](iosxr_static_routes_module.md#examples)
- [Return Values](iosxr_static_routes_module.md#return-values)

## [Synopsis](iosxr_static_routes_module.md#id1)

- This module manages static routes on devices running Cisco IOS-XR.

Aliases: static_routes

## [Parameters](iosxr_static_routes_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of static route options. |
| **address_families**  list / elements=dictionary | A dictionary specifying the address family to which the static route(s) belong. |
| **afi**  string / required | Specifies the top level address family indicator.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **routes**  list / elements=dictionary | A dictionary that specifies the static route configurations. |
| **dest**  string / required | An IPv4 or IPv6 address in CIDR notation that specifies the destination network for the static route. |
| **next_hops**  list / elements=dictionary | Next hops to the specified destination. |
| **admin_distance**  integer | The administrative distance for this static route.  Refer to vendor documentation for valid values. |
| **description**  string | Specifies the description for this static route. |
| **dest_vrf**  string | The destination VRF. |
| **forward_router_address**  string | The IP address of the next hop that can be used to reach the destination network. |
| **interface**  string | The interface to use to reach the destination. |
| **metric**  integer | Specifes the metric for this static route.  Refer to vendor documentation for valid values. |
| **tag**  integer | Specifies a numeric tag for this static route.  Refer to vendor documentation for valid values. |
| **track**  string | Specifies the object to be tracked.  This enables object tracking for static routes. |
| **tunnel_id**  integer | Specifies a tunnel id for the route.  Refer to vendor documentation for valid values. |
| **vrflabel**  integer | Specifies the VRF label for this static route.  Refer to vendor documentation for valid values. |
| **safi**  string / required | Specifies the subsequent address family indicator.  **Choices:**   - `"unicast"` - `"multicast"` |
| **vrf**  string | The VRF to which the static route(s) belong. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS-XR device by executing the command **show running-config router static**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Examples](iosxr_static_routes_module.md#id3)

```yaml+jinja
# Using merged

# Before state
# -------------
# RP/0/RP0/CPU0:ios#show running-config router static
# Sat Feb 22 07:46:30.089 UTC
# % No such configuration item(s)
#
- name: Merge the provided configuration with the existing running configuration
  cisco.iosxr.iosxr_static_routes:
    config:
    - address_families:
      - afi: ipv4
        safi: unicast
        routes:
        - dest: 192.0.2.16/28
          next_hops:
          - forward_router_address: 192.0.2.10
            interface: FastEthernet0/0/0/1
            description: LAB
            metric: 120
            tag: 10

          - interface: FastEthernet0/0/0/5
            track: ip_sla_1

        - dest: 192.0.2.32/28
          next_hops:
          - forward_router_address: 192.0.2.11
            admin_distance: 100

      - afi: ipv6
        safi: unicast
        routes:
        - dest: 2001:db8:1000::/36
          next_hops:
          - interface: FastEthernet0/0/0/7
            description: DC

          - interface: FastEthernet0/0/0/8
            forward_router_address: 2001:db8:2000:2::1

    - vrf: DEV_SITE
      address_families:
      - afi: ipv4
        safi: unicast
        routes:
        - dest: 192.0.2.48/28
          next_hops:
          - forward_router_address: 192.0.2.12
            description: DEV
            dest_vrf: test_1

        - dest: 192.0.2.80/28
          next_hops:
          - interface: FastEthernet0/0/0/2
            forward_router_address: 192.0.2.14
            dest_vrf: test_1
            track: ip_sla_2
            vrflabel: 124
    state: merged

# Task Output
# -----------
# before: []
# commands:
# - router static
# - address-family ipv4 unicast
# - 192.0.2.16/28 192.0.2.10 FastEthernet0/0/0/1 description LAB metric 120 tag 10
# - 192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
# - 192.0.2.32/28 192.0.2.11 100
# - address-family ipv6 unicast
# - 2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
# - 2001:db8:1000::/36 2001:db8:2000:2::1 FastEthernet0/0/0/8
# - vrf DEV_SITE
# - address-family ipv4 unicast
# - 192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
# - 192.0.2.80/28 vrf test_1 192.0.2.14 FastEthernet0/0/0/2 track ip_sla_2 vrflabel 124
# after:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.16/28
#             next_hops:
#               - description: LAB
#                 forward_router_address: 192.0.2.10
#                 interface: FastEthernet0/0/0/1
#                 metric: 120
#                 tag: 10
#               - interface: FastEthernet0/0/0/5
#                 track: ip_sla_1
#           - dest: 192.0.2.32/28
#             next_hops:
#               - admin_distance: 100
#                 forward_router_address: 192.0.2.11
#         safi: unicast
#       - afi: ipv6
#         routes:
#           - dest: 2001:db8:1000::/36
#             next_hops:
#               - description: DC
#                 interface: FastEthernet0/0/0/7
#               - forward_router_address: 2001:db8:2000:2::1
#                 interface: FastEthernet0/0/0/8
#         safi: unicast
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.48/28
#             next_hops:
#               - description: DEV
#                 dest_vrf: test_1
#                 forward_router_address: 192.0.2.12
#           - dest: 192.0.2.80/28
#             next_hops:
#               - dest_vrf: test_1
#                 forward_router_address: 192.0.2.14
#                 interface: FastEthernet0/0/0/2
#                 track: ip_sla_2
#                 vrflabel: 124
#         safi: unicast
#     vrf: DEV_SITE

#
# After state
# -------------
# RP/0/RP0/CPU0:ios#show running-config router static
# Sat Feb 22 07:49:11.754 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

# Using merged to update existing static routes

# Before state
# -------------
# RP/0/RP0/CPU0:ios#show running-config router static
# Sat Feb 22 07:49:11.754 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

- name: Update existing static routes configuration using merged
  cisco.iosxr.iosxr_static_routes:
    config:
    - vrf: DEV_SITE
      address_families:
      - afi: ipv4
        safi: unicast
        routes:
        - dest: 192.0.2.48/28
          next_hops:
          - forward_router_address: 192.0.2.12
            vrflabel: 2301
            dest_vrf: test_1

        - dest: 192.0.2.80/28
          next_hops:
          - interface: FastEthernet0/0/0/2
            forward_router_address: 192.0.2.14
            dest_vrf: test_1
            description: rt_test_1
    state: merged

# Task Output
# -----------
# before:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.16/28
#             next_hops:
#               - description: LAB
#                 forward_router_address: 192.0.2.10
#                 interface: FastEthernet0/0/0/1
#                 metric: 120
#                 tag: 10
#               - interface: FastEthernet0/0/0/5
#                 track: ip_sla_1
#           - dest: 192.0.2.32/28
#             next_hops:
#               - admin_distance: 100
#                 forward_router_address: 192.0.2.11
#         safi: unicast
#       - afi: ipv6
#         routes:
#           - dest: 2001:db8:1000::/36
#             next_hops:
#               - description: DC
#                 interface: FastEthernet0/0/0/7
#               - forward_router_address: 2001:db8:2000:2::1
#                 interface: FastEthernet0/0/0/8
#         safi: unicast
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.48/28
#             next_hops:
#               - description: DEV
#                 dest_vrf: test_1
#                 forward_router_address: 192.0.2.12
#           - dest: 192.0.2.80/28
#             next_hops:
#               - dest_vrf: test_1
#                 forward_router_address: 192.0.2.14
#                 interface: FastEthernet0/0/0/2
#                 track: ip_sla_2
#                 vrflabel: 124
#         safi: unicast
#     vrf: DEV_SITE
# commands:
# - router static
# - vrf DEV_SITE
# - address-family ipv4 unicast
# - 192.0.2.48/28 vrf test_1 192.0.2.12 description DEV vrflabel 2301
# - 192.0.2.80/28 vrf test_1 192.0.2.14 FastEthernet0/0/0/2 description rt_test_1 track ip_sla_2 vrflabel 124
# after:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.16/28
#             next_hops:
#               - description: LAB
#                 forward_router_address: 192.0.2.10
#                 interface: FastEthernet0/0/0/1
#                 metric: 120
#                 tag: 10
#               - interface: FastEthernet0/0/0/5
#                 track: ip_sla_1
#           - dest: 192.0.2.32/28
#             next_hops:
#               - admin_distance: 100
#                 forward_router_address: 192.0.2.11
#         safi: unicast
#       - afi: ipv6
#         routes:
#           - dest: 2001:db8:1000::/36
#             next_hops:
#               - description: DC
#                 interface: FastEthernet0/0/0/7
#               - forward_router_address: 2001:db8:2000:2::1
#                 interface: FastEthernet0/0/0/8
#         safi: unicast
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.48/28
#             next_hops:
#               - description: DEV
#                 dest_vrf: test_1
#                 forward_router_address: 192.0.2.12
#                 vrflabel: 2301
#           - dest: 192.0.2.80/28
#             next_hops:
#               - description: rt_test_1
#                 dest_vrf: test_1
#                 forward_router_address: 192.0.2.14
#                 interface: FastEthernet0/0/0/2
#                 track: ip_sla_2
#                 vrflabel: 124
#         safi: unicast
#     vrf: DEV_SITE

# After state
# -------------
# RP/0/RP0/CPU0:ios#show running-config router static
# Sat Feb 22 07:49:11.754 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV vrflabel 2301
#    192.0.2.80/28 vrf test_1 192.0.2.14 FastEthernet0/0/0/2 description rt_test_1 track ip_sla_2 vrflabel 124
#   !
#  !
# !

# Using replaced to replace all next hop entries for a single destination network

# Before state
# --------------

# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 07:59:08.669 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.48/28 GigabitEthernet0/0/0/1 192.0.3.24 vrflabel 2302
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

- name: Replace device configurations of static routes with provided configurations
  cisco.iosxr.iosxr_static_routes:
    config:
    - vrf: DEV_SITE
      address_families:
      - afi: ipv4
        safi: unicast
        routes:
        - dest: 192.0.2.48/28
          next_hops:
          - forward_router_address: 192.0.2.15
            interface: FastEthernet0/0/0/3
            description: DEV_NEW
            dest_vrf: dev_test_2
    state: replaced

# Task Output
# -----------
# before:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 0.0.0.0/0
#             next_hops:
#               - forward_router_address: 10.0.151.254
#                 interface: MgmtEth0
#           - dest: 192.0.2.16/28
#             next_hops:
#               - description: LAB
#                 forward_router_address: 192.0.2.10
#                 interface: FastEthernet0/0/0/1
#                 metric: 120
#                 tag: 10
#               - interface: FastEthernet0/0/0/5
#                 track: ip_sla_1
#           - dest: 192.0.2.32/28
#             next_hops:
#               - admin_distance: 100
#                 forward_router_address: 192.0.2.11
#         safi: unicast
#       - afi: ipv6
#         routes:
#           - dest: 2001:db8:1000::/36
#             next_hops:
#               - description: DC
#                 interface: FastEthernet0/0/0/7
#               - forward_router_address: 2001:db8:2000:2::1
#                 interface: FastEthernet0/0/0/8
#         safi: unicast
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.48/28
#             next_hops:
#               - description: DEV
#                 dest_vrf: test_1
#                 forward_router_address: 192.0.2.12
#               - forward_router_address: 192.0.3.24
#                 interface: GigabitEthernet0/0/0/1
#                 vrflabel: 2302
#           - dest: 192.0.2.80/28
#             next_hops:
#               - dest_vrf: test_1
#                 forward_router_address: 192.0.2.14
#                 interface: FastEthernet0/0/0/2
#                 track: ip_sla_2
#                 vrflabel: 124
#         safi: unicast
#     vrf: DEV_SITE
#commands:
# - router static
# - vrf DEV_SITE
# - address-family ipv4 unicast
# - no 192.0.2.48/28 vrf test_1 192.0.2.12
# - no 192.0.2.48/28 192.0.3.24 GigabitEthernet0/0/0/1
# - 192.0.2.48/28 vrf dev_test_2 192.0.2.15 FastEthernet0/0/0/3 description DEV_NEW
# after:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.16/28
#             next_hops:
#               - description: LAB
#                 forward_router_address: 192.0.2.10
#                 interface: FastEthernet0/0/0/1
#                 metric: 120
#                 tag: 10
#               - interface: FastEthernet0/0/0/5
#                 track: ip_sla_1
#           - dest: 192.0.2.32/28
#             next_hops:
#               - admin_distance: 100
#                 forward_router_address: 192.0.2.11
#         safi: unicast
#       - afi: ipv6
#         routes:
#           - dest: 2001:db8:1000::/36
#             next_hops:
#               - description: DC
#                 interface: FastEthernet0/0/0/7
#               - forward_router_address: 2001:db8:2000:2::1
#                 interface: FastEthernet0/0/0/8
#         safi: unicast
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.48/28
#             next_hops:
#               - description: DEV_NEW
#                 dest_vrf: dev_test_2
#                 forward_router_address: 192.0.2.15
#                 interface: FastEthernet0/0/0/3
#           - dest: 192.0.2.80/28
#             next_hops:
#               - dest_vrf: test_1
#                 forward_router_address: 192.0.2.14
#                 interface: FastEthernet0/0/0/2
#                 track: ip_sla_2
#                 vrflabel: 124
#         safi: unicast
#     vrf: DEV_SITE

# After state
# ------------
# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 08:04:07.085 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf dev_test_2 FastEthernet0/0/0/3 192.0.2.15 description DEV_NEW
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

# Using overridden to override all static route entries on the device

# Before state
# -------------
# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 07:59:08.669 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.48/28 GigabitEthernet0/0/0/1 192.0.3.24 vrflabel 2302
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

- name: Overridde all static routes configuration with provided configuration
  cisco.iosxr.iosxr_static_routes:
    config:
    - vrf: DEV_NEW
      address_families:
      - afi: ipv4
        safi: unicast
        routes:
        - dest: 192.0.2.48/28
          next_hops:
          - forward_router_address: 192.0.2.15
            interface: FastEthernet0/0/0/3
            description: DEV1
      - afi: ipv6
        safi: unicast
        routes:
        - dest: 2001:db8:3000::/36
          next_hops:
          - interface: FastEthernet0/0/0/4
            forward_router_address: 2001:db8:2000:2::2
            description: PROD1
            track: ip_sla_1
    state: overridden

# Task Output
# -----------
# before:
#     - address_families:
#         - afi: ipv4
#           routes:
#             - dest: 192.0.2.16/28
#               next_hops:
#                 - description: LAB
#                   forward_router_address: 192.0.2.10
#                   interface: FastEthernet0/0/0/1
#                   metric: 120
#                   tag: 10
#                 - interface: FastEthernet0/0/0/5
#                   track: ip_sla_1
#             - dest: 192.0.2.32/28
#               next_hops:
#                 - admin_distance: 100
#                   forward_router_address: 192.0.2.11
#           safi: unicast
#         - afi: ipv6
#           routes:
#             - dest: 2001:db8:1000::/36
#               next_hops:
#                 - description: DC
#                   interface: FastEthernet0/0/0/7
#                 - forward_router_address: 2001:db8:2000:2::1
#                   interface: FastEthernet0/0/0/8
#           safi: unicast
#     - address_families:
#         - afi: ipv4
#           routes:
#             - dest: 192.0.2.48/28
#               next_hops:
#                 - description: DEV
#                   dest_vrf: test_1
#                   forward_router_address: 192.0.2.12
#                 - forward_router_address: 192.0.3.24
#                   interface: GigabitEthernet0/0/0/1
#                   vrflabel: 2302
#             - dest: 192.0.2.80/28
#               next_hops:
#                 - dest_vrf: test_1
#                   forward_router_address: 192.0.2.14
#                   interface: FastEthernet0/0/0/2
#                   track: ip_sla_2
#                   vrflabel: 124
#           safi: unicast
#       vrf: DEV_SITE
# commands:
#     - router static
#     - no vrf DEV_SITE
#     - no address-family ipv4 unicast
#     - no address-family ipv6 unicast
#     - vrf DEV_NEW
#     - address-family ipv4 unicast
#     - 192.0.2.48/28 192.0.2.15 FastEthernet0/0/0/3 description DEV1
#     - address-family ipv6 unicast
#     - 2001:db8:3000::/36 2001:db8:2000:2::2 FastEthernet0/0/0/4 description PROD1
#       track ip_sla_1
# after:
#     - vrf: DEV_NEW
#       address_families:
#         - afi: ipv4
#           safi: unicast
#           routes:
#             - dest: 192.0.2.48/28
#               next_hops:
#                 - forward_router_address: 192.0.2.15
#                   interface: FastEthernet0/0/0/3
#                   description: DEV1
#         - afi: ipv6
#           safi: unicast
#           routes:
#             - dest: 2001:db8:3000::/36
#               next_hops:
#                 - interface: FastEthernet0/0/0/4
#                   forward_router_address: 2001:db8:2000:2::2
#                   description: PROD1
#                   track: ip_sla_1

# After state
# -------------
# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 08:07:41.516 UTC
# router static
#  vrf DEV_NEW
#   address-family ipv4 unicast
#    192.0.2.48/28 FastEthernet0/0/0/3 192.0.2.15 description DEV1
#   !
#   address-family ipv6 unicast
#    2001:db8:3000::/36 FastEthernet0/0/0/4 2001:db8:2000:2::2 description PROD1 track ip_sla_1
#   !
#  !
# !

# Using deleted to delete all destination network entries under a single AFI

# Before state
# -------------
# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 07:59:08.669 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.48/28 GigabitEthernet0/0/0/1 192.0.3.24 vrflabel 2302
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

- name: Delete all destination network entries under a single AFI
  cisco.iosxr.iosxr_static_routes:
    config:
    - vrf: DEV_SITE
      address_families:
      - afi: ipv4
        safi: unicast
    state: deleted

# Task output
# -----------------------
# before:
#     - address_families:
#         - afi: ipv4
#           routes:
#             - dest: 192.0.2.16/28
#               next_hops:
#                 - description: LAB
#                   forward_router_address: 192.0.2.10
#                   interface: FastEthernet0/0/0/1
#                   metric: 120
#                   tag: 10
#                 - interface: FastEthernet0/0/0/5
#                   track: ip_sla_1
#             - dest: 192.0.2.32/28
#               next_hops:
#                 - admin_distance: 100
#                   forward_router_address: 192.0.2.11
#           safi: unicast
#         - afi: ipv6
#           routes:
#             - dest: 2001:db8:1000::/36
#               next_hops:
#                 - description: DC
#                   interface: FastEthernet0/0/0/7
#                 - forward_router_address: 2001:db8:2000:2::1
#                   interface: FastEthernet0/0/0/8
#           safi: unicast
#     - address_families:
#         - afi: ipv4
#           routes:
#             - dest: 192.0.2.48/28
#               next_hops:
#                 - description: DEV
#                   dest_vrf: test_1
#                   forward_router_address: 192.0.2.12
#                 - forward_router_address: 192.0.3.24
#                   interface: GigabitEthernet0/0/0/1
#                   vrflabel: 2302
#             - dest: 192.0.2.80/28
#               next_hops:
#                 - dest_vrf: test_1
#                   forward_router_address: 192.0.2.14
#                   interface: FastEthernet0/0/0/2
#                   track: ip_sla_2
#                   vrflabel: 124
#           safi: unicast
#       vrf: DEV_SITE
# commands:
#  - router static
#  - vrf DEV_SITE
#  - no address-family ipv4 unicast
# after:
#     - address_families:
#         - afi: ipv4
#           routes:
#             - dest: 192.0.2.16/28
#               next_hops:
#                 - description: LAB
#                   forward_router_address: 192.0.2.10
#                   interface: FastEthernet0/0/0/1
#                   metric: 120
#                   tag: 10
#                 - interface: FastEthernet0/0/0/5
#                   track: ip_sla_1
#             - dest: 192.0.2.32/28
#               next_hops:
#                 - admin_distance: 100
#                   forward_router_address: 192.0.2.11
#           safi: unicast
#         - afi: ipv6
#           routes:
#             - dest: 2001:db8:1000::/36
#               next_hops:
#                 - description: DC
#                   interface: FastEthernet0/0/0/7
#                 - forward_router_address: 2001:db8:2000:2::1
#                   interface: FastEthernet0/0/0/8
#           safi: unicast
#     - address_families:
#         - afi: ipv4
#           routes:
#             - dest: 192.0.2.48/28
#               next_hops:
#                 - description: DEV
#                   dest_vrf: test_1
#                   forward_router_address: 192.0.2.12
#                 - forward_router_address: 192.0.3.24
#                   interface: GigabitEthernet0/0/0/1
#                   vrflabel: 2302
#             - dest: 192.0.2.80/28
#               next_hops:
#                 - dest_vrf: test_1
#                   forward_router_address: 192.0.2.14
#                   interface: FastEthernet0/0/0/2
#                   track: ip_sla_2
#                   vrflabel: 124
#           safi: unicast
#     - vrf: DEV_SITE

# After state
# ------------

# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 08:16:41.464 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#  !
# !

# Using deleted to remove all static route entries from the device

# Before state
# -------------
# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 07:59:08.669 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.48/28 GigabitEthernet0/0/0/1 192.0.3.24 vrflabel 2302
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

- name: Delete static routes configuration
  cisco.iosxr.iosxr_static_routes:
    state: deleted

# Task output
# -----------------------
# before:
#     - address_families:
#         - afi: ipv4
#           routes:
#             - dest: 192.0.2.16/28
#               next_hops:
#                 - description: LAB
#                   forward_router_address: 192.0.2.10
#                   interface: FastEthernet0/0/0/1
#                   metric: 120
#                   tag: 10
#                 - interface: FastEthernet0/0/0/5
#                   track: ip_sla_1
#             - dest: 192.0.2.32/28
#               next_hops:
#                 - admin_distance: 100
#                   forward_router_address: 192.0.2.11
#           safi: unicast
#         - afi: ipv6
#           routes:
#             - dest: 2001:db8:1000::/36
#               next_hops:
#                 - description: DC
#                   interface: FastEthernet0/0/0/7
#                 - forward_router_address: 2001:db8:2000:2::1
#                   interface: FastEthernet0/0/0/8
#           safi: unicast
#     - address_families:
#         - afi: ipv4
#           routes:
#             - dest: 192.0.2.48/28
#               next_hops:
#                 - description: DEV
#                   dest_vrf: test_1
#                   forward_router_address: 192.0.2.12
#                 - forward_router_address: 192.0.3.24
#                   interface: GigabitEthernet0/0/0/1
#                   vrflabel: 2302
#             - dest: 192.0.2.80/28
#               next_hops:
#                 - dest_vrf: test_1
#                   forward_router_address: 192.0.2.14
#                   interface: FastEthernet0/0/0/2
#                   track: ip_sla_2
#                   vrflabel: 124
#           safi: unicast
#       vrf: DEV_SITE
# commands:
#     - no router static
# after: []
# After state
# ------------
# RP/0/RP0/CPU0:ios#sh running-config router static
# Sat Feb 22 08:50:43.038 UTC
# % No such configuration item(s)

# Using gathered to gather static route facts from the device

- name: Gather static routes facts from the device using iosxr_static_routes module
  cisco.iosxr.iosxr_static_routes:
    state: gathered

# Task output (redacted)
# -----------------------
# "gathered": [
#    {
#        "address_families": [
#            {
#                "afi": "ipv4",
#                "routes": [
#                    {
#                        "dest": "192.0.2.16/28",
#                        "next_hops": [
#                            {
#                                "description": "LAB",
#                                "forward_router_address": "192.0.2.10",
#                                "interface": "FastEthernet0/0/0/1",
#                                "metric": 120,
#                                "tag": 10
#                            },
#                            {
#                                "interface": "FastEthernet0/0/0/5",
#                                "track": "ip_sla_1"
#                            }
#                        ]
#                    },
#                    {
#                        "dest": "192.0.2.32/28",
#                        "next_hops": [
#                            {
#                                "admin_distance": 100,
#                                "forward_router_address": "192.0.2.11"
#                            }
#                        ]
#                    }
#                ],
#                "safi": "unicast"
#            },
#            {
#                "afi": "ipv6",
#                "routes": [
#                    {
#                        "dest": "2001:db8:1000::/36",
#                        "next_hops": [
#                            {
#                                "description": "DC",
#                                "interface": "FastEthernet0/0/0/7"
#                            },
#                            {
#                                "forward_router_address": "2001:db8:2000:2::1",
#                                "interface": "FastEthernet0/0/0/8"
#                            }
#                        ]
#                    }
#                ],
#                "safi": "unicast"
#            }
#        ]
#    },
#    {
#        "address_families": [
#            {
#                "afi": "ipv4",
#                "routes": [
#                    {
#                        "dest": "192.0.2.48/28",
#                        "next_hops": [
#                            {
#                                "description": "DEV",
#                                "dest_vrf": "test_1",
#                                "forward_router_address": "192.0.2.12"
#                            },
#                            {
#                                "forward_router_address": "192.0.3.24",
#                                "interface": "GigabitEthernet0/0/0/1",
#                                "vrflabel": 2302
#                            }
#                        ]
#                    },
#                    {
#                        "dest": "192.0.2.80/28",
#                        "next_hops": [
#                            {
#                                "dest_vrf": "test_1",
#                                "forward_router_address": "192.0.2.14",
#                                "interface": "FastEthernet0/0/0/2",
#                                "track": "ip_sla_2",
#                                "vrflabel": 124
#                            }
#                        ]
#                    }
#                ],
#                "safi": "unicast"
#            }
#        ],
#        "vrf": "DEV_SITE"
#    }
#  ]

# Using rendered

- name: Render platform specific commands (without connecting to the device)
  cisco.iosxr.iosxr_static_routes:
  config:
  - vrf: DEV_SITE
    address_families:
    - afi: ipv4
      safi: unicast
      routes:
      - dest: 192.0.2.48/28
        next_hops:
        - forward_router_address: 192.0.2.12
          description: DEV
          dest_vrf: test_1

      - dest: 192.0.2.80/28
        next_hops:
        - interface: FastEthernet0/0/0/2
          forward_router_address: 192.0.2.14
          dest_vrf: test_1
          track: ip_sla_2
          vrflabel: 124

# Task Output (redacted)
# -----------------------
# "rendered": [
#    "router static"s,
#    "vrf DEV_SITE",
#    "address-family ipv4 unicast",
#    "192.0.2.48/28 vrf test_1 192.0.2.12 description DEV",
#    "192.0.2.80/28 vrf test_1 192.0.2.14 FastEthernet0/0/0/2 track ip_sla_2 vrflabel 124"

# Using parsed

# parsed.cfg
# ------------
# Fri Nov 29 21:10:41.896 UTC
# router static
#  address-family ipv4 unicast
#   192.0.2.16/28 FastEthernet0/0/0/1 192.0.2.10 tag 10 description LAB metric 120
#   192.0.2.16/28 FastEthernet0/0/0/5 track ip_sla_1
#   192.0.2.32/28 192.0.2.11 100
#  !
#  address-family ipv6 unicast
#   2001:db8:1000::/36 FastEthernet0/0/0/7 description DC
#   2001:db8:1000::/36 FastEthernet0/0/0/8 2001:db8:2000:2::1
#  !
#  vrf DEV_SITE
#   address-family ipv4 unicast
#    192.0.2.48/28 vrf test_1 192.0.2.12 description DEV
#    192.0.2.80/28 vrf test_1 FastEthernet0/0/0/2 192.0.2.14 vrflabel 124 track ip_sla_2
#   !
#  !
# !

- name: Use parsed state to convert externally supplied device specific static routes
    commands to structured format
  cisco.iosxr.iosxr_static_routes:
    running_config: "{{ lookup('file', '../../fixtures/parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------
# "parsed": [
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "192.0.2.16/28",
#                            "next_hops": [
#                                {
#                                    "description": "LAB",
#                                    "forward_router_address": "192.0.2.10",
#                                    "interface": "FastEthernet0/0/0/1",
#                                    "metric": 120,
#                                    "tag": 10
#                                },
#                                {
#                                    "interface": "FastEthernet0/0/0/5",
#                                    "track": "ip_sla_1"
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "192.0.2.32/28",
#                            "next_hops": [
#                                {
#                                    "admin_distance": 100,
#                                    "forward_router_address": "192.0.2.11"
#                                }
#                            ]
#                        }
#                    ],
#                    "safi": "unicast"
#                },
#                {
#                    "afi": "ipv6",
#                    "routes": [
#                        {
#                            "dest": "2001:db8:1000::/36",
#                            "next_hops": [
#                                {
#                                    "description": "DC",
#                                    "interface": "FastEthernet0/0/0/7"
#                                },
#                                {
#                                    "forward_router_address": "2001:db8:2000:2::1",
#                                    "interface": "FastEthernet0/0/0/8"
#                                }
#                            ]
#                        }
#                    ],
#                    "safi": "unicast"
#                }
#            ]
#        },
#        {
#            "address_families": [
#                {
#                    "afi": "ipv4",
#                    "routes": [
#                        {
#                            "dest": "192.0.2.48/28",
#                            "next_hops": [
#                                {
#                                    "description": "DEV",
#                                    "dest_vrf": "test_1",
#                                    "forward_router_address": "192.0.2.12"
#                                }
#                            ]
#                        },
#                        {
#                            "dest": "192.0.2.80/28",
#                            "next_hops": [
#                                {
#                                    "dest_vrf": "test_1",
#                                    "forward_router_address": "192.0.2.14",
#                                    "interface": "FastEthernet0/0/0/2",
#                                    "track": "ip_sla_2",
#                                    "vrflabel": 124
#                                }
#                            ]
#                        }
#                    ],
#                    "safi": "unicast"
#                }
#            ],
#            "vrf": "DEV_SITE"
#        }
#    ]
# }
```

## [Return Values](iosxr_static_routes_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["router static", "vrf dev_site", "address-family ipv4 unicast", "192.0.2.48/28 192.0.2.12 FastEthernet0/0/0/1 track ip_sla_10 description dev1", "address-family ipv6 unicast", "no 2001:db8:1000::/36", "2001:db8:3000::/36 2001:db8:2000:2::2 FastEthernet0/0/0/4 track ip_sla_11 description prod1"]` |

### Authors

- Nilashish Chakraborty (@NilashishC)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
