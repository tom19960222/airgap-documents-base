---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_static_routes module – Static routes resource module"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_static_routes_module.html
fetched_at: 2026-07-28T01:39:13+00:00
---
# cisco.nxos.nxos_static_routes module – Static routes resource module

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
> To use it in a playbook, specify: `cisco.nxos.nxos_static_routes`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_static_routes_module.md#synopsis)
- [Parameters](nxos_static_routes_module.md#parameters)
- [Notes](nxos_static_routes_module.md#notes)
- [Examples](nxos_static_routes_module.md#examples)
- [Return Values](nxos_static_routes_module.md#return-values)

## [Synopsis](nxos_static_routes_module.md#id1)

- This module configures and manages the attributes of static routes on Cisco NX-OS platforms.

Aliases: static_routes

## [Parameters](nxos_static_routes_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A list of configurations for static routes |
| **address_families**  list / elements=dictionary | A dictionary specifying the address family to which the static route(s) belong. |
| **afi**  string / required | Specifies the top level address family indicator.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **routes**  list / elements=dictionary | A dictionary that specifies the static route configurations |
| **dest**  string / required | Destination prefix of static route  The address format is <ipv4/v6 address>/<mask>  The mask is number in range 0-32 for IPv4 and in range 0-128 for IPv6 |
| **next_hops**  list / elements=dictionary | Details of route to be taken |
| **admin_distance**  integer | Preference or administrative distance of route (range 1-255) |
| **dest_vrf**  string | VRF of the destination |
| **forward_router_address**  string | IP address of the next hop router |
| **interface**  string | Outgoing interface to take. For anything except ‘Null0’, then next hop IP address should also be configured. |
| **route_name**  string | Name of the static route |
| **tag**  integer | Route tag value (numeric) |
| **track**  integer | Track value (range 1 - 512). Track must already be configured on the device before adding the route. |
| **vrf**  string | The VRF to which the static route(s) belong |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the NX-OS device by executing the following commands in order **show running-config | include ‘^ip(v6**\* route’) and **show running-config | section ‘^vrf context’**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  **Choices:**   - `"deleted"` - `"merged"` ← (default) - `"overridden"` - `"replaced"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](nxos_static_routes_module.md#id3)

> **Note:**
>
> - Tested against NX-OS 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - When a route is configured for a non-existent VRF, the VRF is created and the route is added to it.
> - When deleting routes for a VRF, all routes inside the VRF are deleted, but the VRF is not deleted.

## [Examples](nxos_static_routes_module.md#id4)

```yaml+jinja
# Using deleted:

# Before state:
# -------------
#
# ip route 192.0.2.32/28 192.0.2.12 name new_route
# ip route 192.0.2.26/24 192.0.2.13 tag 12

- name: Delete all routes
  cisco.nxos.nxos_static_routes:
    state: deleted

# Task Output
# -----------
# before:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.0/24
#             next_hops:
#               - forward_router_address: 192.0.2.13
#                 tag: 12
#           - dest: 192.0.2.32/28
#             next_hops:
#               - forward_router_address: 192.0.2.12
#                 route_name: new_route
# commands:
# - configure terminal
# - no ip route 192.0.2.0/24 192.0.2.13 tag 12
# - no ip route 192.0.2.32/28 192.0.2.12 name new_route
# after: []
# After state:
# ------------
#

# Before state:
# ------------
#
# ip route 192.0.2.16/28 192.0.2.24 name new_route
# ip route 192.0.2.80/28 192.0.2.26 tag 12
# vrf context trial_vrf
# ip route 192.0.2.64/28 192.0.2.22 tag 4
# ip route 192.0.2.64/28 192.0.2.23 name merged_route 1
# ipv6 route 2200:10::/36 2048:ae12::1 vrf dest 5

- name: Delete routes based on VRF
  cisco.nxos.nxos_static_routes:
    config:
    - vrf: trial_vrf
    state: deleted

# Task Output
# -----------
# before:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.64/28
#             next_hops:
#               - forward_router_address: 192.0.2.22
#                 tag: 4
#               - admin_distance: 1
#                 forward_router_address: 192.0.2.23
#                 route_name: merged_route
#       - afi: ipv6
#         routes:
#           - dest: '2200:10::/36'
#             next_hops:
#               - admin_distance: 5
#                 dest_vrf: dest
#                 forward_router_address: '2048:ae12::1'
#     vrf: trial_vrf
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.16/28
#             next_hops:
#               - forward_router_address: 192.0.2.24
#                 route_name: new_route
#           - dest: 192.0.2.80/28
#             next_hops:
#               - forward_router_address: 192.0.2.26
#                 tag: 12
# commands:
# - vrf context trial_vrf
# - no ip route 192.0.2.64/28 192.0.2.22 tag 4
# - no ip route 192.0.2.64/28 192.0.2.23 name merged_route 1
# - no ipv6 route 2200:10::/36 2048:ae12::1 vrf dest 5
# after:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.16/28
#             next_hops:
#               - forward_router_address: 192.0.2.24
#                 route_name: new_route
#           - dest: 192.0.2.80/28
#             next_hops:
#               - forward_router_address: 192.0.2.26
#                 tag: 12

# After state:
# -----------
# ip route 192.0.2.16/28 192.0.2.24 name new_route
# ip route 192.0.2.80/28 192.0.2.26 tag 12
# vrf context trial_vrf

# Before state:
# ------------
#
# ip route 192.0.2.16/28 192.0.2.24 name new_route
# ip route 192.0.2.80/28 192.0.2.26 tag 12
# vrf context trial_vrf
# ip route 192.0.2.64/28 192.0.2.22 tag 4
# ip route 192.0.2.64/28 192.0.2.23 name merged_route 1
# ipv6 route 2200:10::/36 2048:ae12::1 vrf dest 5

- name: Delete routes based on AFI in a VRF
  cisco.nxos.nxos_static_routes:
    config:
    - vrf: trial_vrf
      address_families:
      - afi: ipv4
    state: deleted

# Task Output
# -----------
# before:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.64/28
#             next_hops:
#               - forward_router_address: 192.0.2.22
#                 tag: 4
#               - admin_distance: 1
#                 forward_router_address: 192.0.2.23
#                 route_name: merged_route
#       - afi: ipv6
#         routes:
#           - dest: '2200:10::/36'
#             next_hops:
#               - admin_distance: 5
#                 dest_vrf: dest
#                 forward_router_address: '2048:ae12::1'
#     vrf: trial_vrf
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.16/28
#             next_hops:
#               - forward_router_address: 192.0.2.24
#                 route_name: new_route
#           - dest: 192.0.2.80/28
#             next_hops:
#               - forward_router_address: 192.0.2.26
#                 tag: 12
# commands:
# - vrf context trial_vrf
# - no ip route 192.0.2.64/28 192.0.2.22 tag 4
# - no ip route 192.0.2.64/28 192.0.2.23 name merged_route 1
# after:
#   - address_families:
#       - afi: ipv6
#         routes:
#           - dest: '2200:10::/36'
#             next_hops:
#               - admin_distance: 5
#                 dest_vrf: dest
#                 forward_router_address: '2048:ae12::1'
#     vrf: trial_vrf
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.16/28
#             next_hops:
#               - forward_router_address: 192.0.2.24
#                 route_name: new_route
#           - dest: 192.0.2.80/28
#             next_hops:
#               - forward_router_address: 192.0.2.26
#                 tag: 12

# After state:
# -----------
# ip route 192.0.2.16/28 192.0.2.24 name new_route
# ip route 192.0.2.80/28 192.0.2.26 tag 12
# vrf context trial_vrf
# ipv6 route 2200:10::/36 2048:ae12::1 vrf dest 5

# Using merged

# Before state:
# -------------
#

- name: Merge new static route configuration
  cisco.nxos.nxos_static_routes:
    config:
    - vrf: trial_vrf
      address_families:
      - afi: ipv4
        routes:
        - dest: 192.0.2.64/24
          next_hops:
          - forward_router_address: 192.0.2.22
            tag: 4
            admin_distance: 2

    - address_families:
      - afi: ipv4
        routes:
        - dest: 192.0.2.16/24
          next_hops:
          - forward_router_address: 192.0.2.24
            route_name: new_route
      - afi: ipv6
        routes:
        - dest: 2001:db8::/64
          next_hops:
          - interface: eth1/3
            forward_router_address: 2001:db8::12
    state: merged

# Task Output
# -----------
# before:[]
# commands:
# - vrf context trial_vrf
# - ip route 192.0.2.64/24 192.0.2.22 tag 4 2
# - configure terminal
# - ip route 192.0.2.16/24 192.0.2.24 name new_route
# - ipv6 route 2001:db8::/64 Ethernet1/3 2001:db8::12
# after:
#     - vrf: trial_vrf
#       address_families:
#       - afi: ipv4
#         routes:
#         - dest: 192.0.2.64/24
#           next_hops:
#           - forward_router_address: 192.0.2.22
#             tag: 4
#             admin_distance: 2
#
#     - address_families:
#       - afi: ipv4
#         routes:
#         - dest: 192.0.2.16/24
#           next_hops:
#           - forward_router_address: 192.0.2.24
#             route_name: new_route
#       - afi: ipv6
#         routes:
#         - dest: 2001:db8::/64
#           next_hops:
#           - interface: eth1/3
#             forward_router_address: 2

# After state:
# ------------
#
# ip route 192.0.2.16/24 192.0.2.24 name new_route
# ipv6 route 2001:db8::/64 Ethernet1/3 2001:db8::12
# vrf context trial_vrf
#   ip route 192.0.2.0/24 192.0.2.22 tag 4 2

# Using overridden:

# Before state:
# -------------
#
# ip route 192.0.2.16/28 192.0.2.24 name new_route
# ip route 192.0.2.80/28 192.0.2.26 tag 12
# vrf context trial_vrf
# ip route 192.0.2.64/28 192.0.2.22 tag 4
# ip route 192.0.2.64/28 192.0.2.23 name merged_route 1

- name: Overriden existing static route configuration with new configuration
  cisco.nxos.nxos_static_routes:
    config:
    - vrf: trial_vrf
      address_families:
      - afi: ipv4
        routes:
        - dest: 192.0.2.16/28
          next_hops:
          - forward_router_address: 192.0.2.23
            route_name: overridden_route1
            admin_distance: 3

          - forward_router_address: 192.0.2.45
            route_name: overridden_route2
            dest_vrf: destinationVRF
            interface: Ethernet1/2
    state: overridden

# Task Output
# -----------
# before:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.64/28
#             next_hops:
#               - forward_router_address: 192.0.2.22
#                 tag: 4
#               - admin_distance: 1
#                 forward_router_address: 192.0.2.23
#                 route_name: merged_route
#     vrf: trial_vrf
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.16/28
#             next_hops:
#               - forward_router_address: 192.0.2.24
#                 route_name: new_route
#           - dest: 192.0.2.80/28
#             next_hops:
#               - forward_router_address: 192.0.2.26
#                 tag: 12
# commands:
# - configure terminal
# - no ip route 192.0.2.16/28 192.0.2.24 name new_route
# - no ip route 192.0.2.80/28 192.0.2.26 tag 12
# - vrf context trial_vrf
# - no ip route 192.0.2.64/28 192.0.2.22 tag 4
# - no ip route 192.0.2.64/28 192.0.2.23 name merged_route 1
# - ip route 192.0.2.16/28 192.0.2.23 name overridden_route1 3
# - ip route 192.0.2.16/28 Ethernet1/2 192.0.2.45 vrf destinationVRF name overridden_route2
# after:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.16/28
#             next_hops:
#               - admin_distance: 3
#                 forward_router_address: 192.0.2.23
#                 route_name: overridden_route1
#               - dest_vrf: destinationVRF
#                 forward_router_address: 192.0.2.45
#                 interface: Ethernet1/2
#                 route_name: overridden_route2
#    vrf: trial_vrf

# After state:
# ------------
#
# vrf context trial_vrf
#   ip route 192.0.2.16/28 192.0.2.23 name overridden_route1 3
#   ip route 192.0.2.16/28 Ethernet1/2 192.0.2.45 vrf destinationVRF name overridden_route2

# Using replaced:

# Before state:
# ------------
# ip route 192.0.2.16/28 192.0.2.24 name new_route
# ip route 192.0.2.80/28 192.0.2.26 tag 12
# vrf context trial_vrf
# ip route 192.0.2.64/28 192.0.2.22 tag 4
# ip route 192.0.2.64/28 192.0.2.23 name merged_route 1

- name: Replaced the existing static configuration of a prefix with new configuration
  cisco.nxos.nxos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 192.0.2.16/28
          next_hops:
          - forward_router_address: 192.0.2.23
            route_name: replaced_route1
            admin_distance: 3

          - forward_router_address: 192.0.2.45
            route_name: replaced_route2
            dest_vrf: destinationVRF
            interface: Ethernet1/2
    state: replaced

# Task Output
# -----------
# before:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.64/28
#             next_hops:
#               - forward_router_address: 192.0.2.22
#                 tag: 4
#               - admin_distance: 1
#                 forward_router_address: 192.0.2.23
#                 route_name: merged_route
#     vrf: trial_vrf
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.16/28
#             next_hops:
#               - forward_router_address: 192.0.2.24
#                 route_name: new_route
#           - dest: 192.0.2.80/28
#             next_hops:
#               - forward_router_address: 192.0.2.26
#                 tag: 12
# commands:
# - configure terminal
# - no ip route 192.0.2.16/28 192.0.2.24 name new_route
# - ip route 192.0.2.16/28 192.0.2.23 name replaced_route1 3
# - ip route 192.0.2.16/28 Ethernet1/2 192.0.2.45 vrf destinationVRF name replaced_route2
# after:
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.64/28
#             next_hops:
#               - forward_router_address: 192.0.2.22
#                 tag: 4
#               - admin_distance: 1
#                 forward_router_address: 192.0.2.23
#                 route_name: merged_route
#     vrf: trial_vrf
#   - address_families:
#       - afi: ipv4
#         routes:
#           - dest: 192.0.2.16/28
#             next_hops:
#               - admin_distance: 3
#                 forward_router_address: 192.0.2.23
#                 route_name: replaced_route1
#               - dest_vrf: destinationVRF
#                 forward_router_address: 192.0.2.45
#                 interface: Ethernet1/2
#                 route_name: replaced_route2
#           - dest: 192.0.2.80/28
#             next_hops:
#               - forward_router_address: 192.0.2.26
#                 tag: 12

# After state:
# -----------
# ip route 192.0.2.16/28 192.0.2.23 name replaced_route1 3
# ip route 192.0.2.16/28 Ethernet1/2 192.0.2.45 vrf destinationVRF name replaced_route2
# ip route 192.0.2.80/28 192.0.2.26 tag 12
# vrf context trial_vrf
# ip route 192.0.2.64/28 192.0.2.22 tag 4
# ip route 192.0.2.64/28 192.0.2.23 name merged_route 1

# Using gathered:

# Before state:
# -------------
# ipv6 route 2001:db8:12::/32  2001:db8::12
# vrf context Test
#    ip route 192.0.2.48/28 192.0.2.13
#    ip route 192.0.2.48/28 192.0.2.14 5

- name: Gather the exisitng condiguration
  cisco.nxos.nxos_static_routes:
    state: gathered

# returns:
# gathered:
#     - vrf: Test
#       address_families:
#         - afi: ipv4
#           routes:
#             - dest: 192.0.2.48/28
#               next_hops:
#                 - forward_router_address: 192.0.2.13
#
#                 - forward_router_address: 192.0.2.14
#                   admin_distance: 5
#
#     - address_families:
#         - afi: ipv6
#           routes:
#             - dest: 2001:db8:12::/32
#               next_hops:
#                 - forward_router_address: 2001:db8::12

# Using rendered:

- name: Render required configuration to be pushed to the device
  cisco.nxos.nxos_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 192.0.2.48/28
          next_hops:
          - forward_router_address: 192.0.2.13

      - afi: ipv6
        routes:
        - dest: 2001:db8::/64
          next_hops:
          - interface: eth1/3
            forward_router_address: 2001:db8::12
    state: rendered

# returns
# rendered:
#   vrf context default
#   ip route 192.0.2.48/28 192.0.2.13
#   ipv6 route 2001:db8::/64 Ethernet1/3 2001:db8::12

# Using parsed

- name: Parse the config to structured data
  cisco.nxos.nxos_static_routes:
    running_config: |
      ipv6 route 2002:db8:12::/32 2002:db8:12::1
      vrf context Test
        ip route 192.0.2.48/28 192.0.2.13
        ip route 192.0.2.48/28 192.0.2.14 5

# returns:
# parsed:
#     - vrf: Test
#       address_families:
#         - afi: ipv4
#           routes:
#             - dest: 192.0.2.48/28
#               next_hops:
#                 - forward_router_address: 192.0.2.13
#
#                 - forward_router_address: 192.0.2.14
#                   admin_distance: 5
#
#     - address_families:
#         - afi: ipv6
#           routes:
#             - dest: 2002:db8:12::/32
#               next_hops:
#                 - forward_router_address: 2002:db8:12::1
```

## [Return Values](nxos_static_routes_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["ip route 192.0.2.48/28 192.0.2.12 Ethernet1/2 name sample_route", "ipv6 route 2001:db8:3000::/36 2001:db8:200:2::2", "vrf context test", "ip route 192.0.2.48/28 192.0.2.121"]` |

### Authors

- Adharsh Srivats Rangarajan (@adharshsrivatsr)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
