---
collection: ansible
version: "8"
title: "cisco.ios.ios_static_routes module – Resource module to configure static routes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ios/ios_static_routes_module.html
fetched_at: 2026-07-28T01:26:28+00:00
---
# cisco.ios.ios_static_routes module – Resource module to configure static routes.

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
> To use it in a playbook, specify: `cisco.ios.ios_static_routes`.

New in cisco.ios 1.0.0

- [Synopsis](ios_static_routes_module.md#synopsis)
- [Parameters](ios_static_routes_module.md#parameters)
- [Notes](ios_static_routes_module.md#notes)
- [Examples](ios_static_routes_module.md#examples)
- [Return Values](ios_static_routes_module.md#return-values)

## [Synopsis](ios_static_routes_module.md#id1)

- This module configures and manages the static routes on IOS platforms.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: static_routes

## [Parameters](ios_static_routes_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of static route options |
| **address_families**  list / elements=dictionary | Address family to use for the static routes |
| **afi**  string / required | Top level address family indicator.  **Choices:**   - `"ipv4"` - `"ipv6"` |
| **routes**  list / elements=dictionary | Configuring static route |
| **dest**  string / required | Destination prefix with its subnet mask |
| **next_hops**  list / elements=dictionary | next hop address or interface |
| **dhcp**  boolean | Default gateway obtained from DHCP  **Choices:**   - `false` - `true` |
| **distance_metric**  integer | Distance metric for this route |
| **forward_router_address**  string | Forwarding router’s address |
| **global**  boolean | Next hop address is global  **Choices:**   - `false` - `true` |
| **interface**  string | Interface for directly connected static routes |
| **multicast**  boolean | multicast route  **Choices:**   - `false` - `true` |
| **name**  string | Specify name of the next hop |
| **permanent**  boolean | permanent route  **Choices:**   - `false` - `true` |
| **tag**  integer | Set tag for this route  Refer to vendor documentation for valid values. |
| **track**  integer | Install route depending on tracked item with tracked object number.  Tracking does not support multicast  Refer to vendor documentation for valid values. |
| **unicast**  boolean | unicast route (ipv6 specific)  **Choices:**   - `false` - `true` |
| **topology**  string | Configure static route for a Topology Routing/Forwarding instance  NOTE, VRF and Topology can be used together only with Multicast and Topology should pre-exist before it can be used |
| **vrf**  string | IP VPN Routing/Forwarding instance name.  NOTE, In case of IPV4/IPV6 VRF routing table should pre-exist before configuring.  NOTE, if the vrf information is not provided then the routes shall be configured under global vrf. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | include ip route|ipv6 route**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  **Choices:**   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](ios_static_routes_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSXE Version 17.3 on CML.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - The module examples uses callback plugin (stdout_callback = yaml) to generate task output in yaml format.

## [Examples](ios_static_routes_module.md#id4)

```yaml+jinja
# Using merged

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route

- name: Merge provided configuration with device configuration
  cisco.ios.ios_static_routes:
    config:
      - vrf: blue
        address_families:
          - afi: ipv4
            routes:
              - dest: 192.0.2.0/24
                next_hops:
                  - forward_router_address: 192.0.2.1
                    name: merged_blue
                    tag: 50
                    track: 150
      - address_families:
          - afi: ipv4
            routes:
              - dest: 198.51.100.0/24
                next_hops:
                  - forward_router_address: 198.51.101.1
                    name: merged_route_1
                    distance_metric: 110
                    tag: 40
                    multicast: true
                  - forward_router_address: 198.51.101.2
                    name: merged_route_2
                    distance_metric: 30
                  - forward_router_address: 198.51.101.3
                    name: merged_route_3
          - afi: ipv6
            routes:
              - dest: 2001:DB8:0:3::/64
                next_hops:
                  - forward_router_address: 2001:DB8:0:3::2
                    name: merged_v6
                    tag: 105
    state: merged

# Task Output
# -----------
#
# before:
# - {}
# commands:
# - ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name merged_v6
# - ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name merged_route_1 multicast
# - ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name merged_route_2
# - ip route 198.51.100.0 255.255.255.0 198.51.101.3 name merged_route_3
# - ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name merged_blue track 150
# after:
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 198.51.100.0/24
#       next_hops:
#       - forward_router_address: 198.51.101.3
#         name: merged_route_3
#       - distance_metric: 30
#         forward_router_address: 198.51.101.2
#         name: merged_route_2
#       - distance_metric: 110
#         forward_router_address: 198.51.101.1
#         multicast: true
#         name: merged_route_1
#         tag: 40
#   - afi: ipv6
#     routes:
#     - dest: 2001:DB8:0:3::/64
#       next_hops:
#       - forward_router_address: 2001:DB8:0:3::2
#         name: merged_v6
#         tag: 105
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 192.0.2.0/24
#       next_hops:
#       - forward_router_address: 192.0.2.1
#         name: merged_blue
#         tag: 50
#         track: 150
#   vrf: blue

# After state:
# ------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name merged_blue track 150
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name merged_route_3
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name merged_route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name merged_route_1 multicast
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name merged_v6

# Using replaced

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name merged_blue track 150
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name merged_route_3
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name merged_route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name merged_route_1 multicast
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name merged_v6

- name: Replace provided configuration with device configuration
  cisco.ios.ios_static_routes:
    config:
      - address_families:
          - afi: ipv4
            routes:
              - dest: 198.51.100.0/24
                next_hops:
                  - forward_router_address: 198.51.101.1
                    name: replaced_route
                    distance_metric: 175
                    tag: 70
                    multicast: true
    state: replaced

# Task Output
# -----------
#
# before:
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 198.51.100.0/24
#       next_hops:
#       - forward_router_address: 198.51.101.3
#         name: merged_route_3
#       - distance_metric: 30
#         forward_router_address: 198.51.101.2
#         name: merged_route_2
#       - distance_metric: 110
#         forward_router_address: 198.51.101.1
#         multicast: true
#         name: merged_route_1
#         tag: 40
#   - afi: ipv6
#     routes:
#     - dest: 2001:DB8:0:3::/64
#       next_hops:
#       - forward_router_address: 2001:DB8:0:3::2
#         name: merged_v6
#         tag: 105
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 192.0.2.0/24
#       next_hops:
#       - forward_router_address: 192.0.2.1
#         name: merged_blue
#         tag: 50
#         track: 150
#   vrf: blue
# commands:
# - ip route 198.51.100.0 255.255.255.0 198.51.101.1 175 tag 70 name replaced_route multicast
# - no ip route 198.51.100.0 255.255.255.0 198.51.101.3 name merged_route_3
# - no ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name merged_route_2
# after:
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 198.51.100.0/24
#       next_hops:
#       - distance_metric: 175
#         forward_router_address: 198.51.101.1
#         multicast: true
#         name: replaced_route
#         tag: 70
#   - afi: ipv6
#     routes:
#     - dest: 2001:DB8:0:3::/64
#       next_hops:
#       - forward_router_address: 2001:DB8:0:3::2
#         name: merged_v6
#         tag: 105
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 192.0.2.0/24
#       next_hops:
#       - forward_router_address: 192.0.2.1
#         name: merged_blue
#         tag: 50
#         track: 150
#   vrf: blue

# After state:
# ------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name merged_blue track 150
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 175 tag 70 name replaced_route multicast
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name merged_v6

# Using overridden

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name merged_blue track 150
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 175 tag 70 name replaced_route multicast
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name merged_v6

- name: Override provided configuration with device configuration
  cisco.ios.ios_static_routes:
    config:
      - vrf: blue
        address_families:
          - afi: ipv4
            routes:
              - dest: 192.0.2.0/24
                next_hops:
                  - forward_router_address: 192.0.2.1
                    name: override_vrf
                    tag: 50
                    track: 150
    state: overridden

# Task Output
# -----------
#
# before:
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 198.51.100.0/24
#       next_hops:
#       - distance_metric: 175
#         forward_router_address: 198.51.101.1
#         multicast: true
#         name: replaced_route
#         tag: 70
#   - afi: ipv6
#     routes:
#     - dest: 2001:DB8:0:3::/64
#       next_hops:
#       - forward_router_address: 2001:DB8:0:3::2
#         name: merged_v6
#         tag: 105
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 192.0.2.0/24
#       next_hops:
#       - forward_router_address: 192.0.2.1
#         name: merged_blue
#         tag: 50
#         track: 150
#   vrf: blue
# commands:
# - ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name override_vrf track 150
# - no ip route 198.51.100.0 255.255.255.0 198.51.101.1 175 tag 70 name replaced_route multicast
# - no ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name merged_v6
# after:
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 192.0.2.0/24
#       next_hops:
#       - forward_router_address: 192.0.2.1
#         name: override_vrf
#         tag: 50
#         track: 150
#   vrf: blue

# After state:
# ------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name override_vrf track 150

# Using deleted

# Before state:
# -------------
# vios#show running-config | include ip route|ipv6 route
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

- name: Delete the exact static routes, with all the static routes explicitly mentioned in want
  cisco.ios.ios_static_routes:
    config:
      - vrf: blue
        address_families:
          - afi: ipv4
            routes:
              - dest: 192.0.2.0/24
                next_hops:
                  - forward_router_address: 192.0.2.1
                    name: test_vrf
                    tag: 50
                    track: 150
      - address_families:
          - afi: ipv4
            routes:
              - dest: 198.51.100.0/24
                next_hops:
                  - forward_router_address: 198.51.101.1
                    name: route_1
                    distance_metric: 110
                    tag: 40
                    multicast: true
                  - forward_router_address: 198.51.101.2
                    name: route_2
                    distance_metric: 30
                  - forward_router_address: 198.51.101.3
                    name: route_3
          - afi: ipv6
            routes:
              - dest: 2001:DB8:0:3::/64
                next_hops:
                  - forward_router_address: 2001:DB8:0:3::2
                    name: test_v6
                    tag: 105
    state: deleted

# Task Output
# -----------
#
# before:
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 198.51.100.0/24
#       next_hops:
#       - forward_router_address: 198.51.101.3
#         name: route_3
#       - distance_metric: 30
#         forward_router_address: 198.51.101.2
#         name: route_2
#       - distance_metric: 110
#         forward_router_address: 198.51.101.1
#         multicast: true
#         name: route_1
#         tag: 40
#   - afi: ipv6
#     routes:
#     - dest: 2001:DB8:0:3::/64
#       next_hops:
#       - forward_router_address: 2001:DB8:0:3::2
#         name: test_v6
#         tag: 105
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 192.0.2.0/24
#       next_hops:
#       - forward_router_address: 192.0.2.1
#         name: test_vrf
#         tag: 50
#         track: 150
#   vrf: blue
# commands:
# - no ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# - no ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# - no ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# - no ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# - no ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6
# after: {}

# After state:
# ------------
#
# vios#show running-config | include ip route|ipv6 route

# Using deleted - delete based on specific routes

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

- name: Delete destination specific static routes
  cisco.ios.ios_static_routes:
    config:
      - address_families:
          - afi: ipv4
            routes:
              - dest: 198.51.100.0/24
    state: deleted

# Task Output
# -----------
#
# before:
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 198.51.100.0/24
#       next_hops:
#       - forward_router_address: 198.51.101.3
#         name: route_3
#       - distance_metric: 30
#         forward_router_address: 198.51.101.2
#         name: route_2
#       - distance_metric: 110
#         forward_router_address: 198.51.101.1
#         multicast: true
#         name: route_1
#         tag: 40
#   - afi: ipv6
#     routes:
#     - dest: 2001:DB8:0:3::/64
#       next_hops:
#       - forward_router_address: 2001:DB8:0:3::2
#         name: test_v6
#         tag: 105
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 192.0.2.0/24
#       next_hops:
#       - forward_router_address: 192.0.2.1
#         name: test_vrf
#         tag: 50
#         track: 150
#   vrf: blue
# commands:
# - no ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# - no ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# - no ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# after:
# - address_families:
#   - afi: ipv6
#     routes:
#     - dest: 2001:DB8:0:3::/64
#       next_hops:
#       - forward_router_address: 2001:DB8:0:3::2
#         name: test_v6
#         tag: 105
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 192.0.2.0/24
#       next_hops:
#       - forward_router_address: 192.0.2.1
#         name: test_vrf
#         tag: 50
#         track: 150
#   vrf: blue

# After state:
# ------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

# Using deleted - delete based on vrfs

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

- name: Delete vrf specific static routes
  cisco.ios.ios_static_routes:
    config:
      - vrf: blue
    state: deleted

# Task Output
# -----------
#
# before:
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 198.51.100.0/24
#       next_hops:
#       - forward_router_address: 198.51.101.3
#         name: route_3
#       - distance_metric: 30
#         forward_router_address: 198.51.101.2
#         name: route_2
#       - distance_metric: 110
#         forward_router_address: 198.51.101.1
#         multicast: true
#         name: route_1
#         tag: 40
#   - afi: ipv6
#     routes:
#     - dest: 2001:DB8:0:3::/64
#       next_hops:
#       - forward_router_address: 2001:DB8:0:3::2
#         name: test_v6
#         tag: 105
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 192.0.2.0/24
#       next_hops:
#       - forward_router_address: 192.0.2.1
#         name: test_vrf
#         tag: 50
#         track: 150
#   vrf: blue
# commands:
# - no ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# after:
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 198.51.100.0/24
#       next_hops:
#       - forward_router_address: 198.51.101.3
#         name: route_3
#       - distance_metric: 30
#         forward_router_address: 198.51.101.2
#         name: route_2
#       - distance_metric: 110
#         forward_router_address: 198.51.101.1
#         multicast: true
#         name: route_1
#         tag: 40
#   - afi: ipv6
#     routes:
#     - dest: 2001:DB8:0:3::/64
#       next_hops:
#       - forward_router_address: 2001:DB8:0:3::2
#         name: test_v6
#         tag: 105

# After state:
# ------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

# Using deleted - delete all

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

- name: Delete ALL configured static routes
  cisco.ios.ios_static_routes:
    state: deleted

# Task Output
# -----------
#
# before:
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 198.51.100.0/24
#       next_hops:
#       - forward_router_address: 198.51.101.3
#         name: route_3
#       - distance_metric: 30
#         forward_router_address: 198.51.101.2
#         name: route_2
#       - distance_metric: 110
#         forward_router_address: 198.51.101.1
#         multicast: true
#         name: route_1
#         tag: 40
#   - afi: ipv6
#     routes:
#     - dest: 2001:DB8:0:3::/64
#       next_hops:
#       - forward_router_address: 2001:DB8:0:3::2
#         name: test_v6
#         tag: 105
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 192.0.2.0/24
#       next_hops:
#       - forward_router_address: 192.0.2.1
#         name: test_vrf
#         tag: 50
#         track: 150
#   vrf: blue
# commands:
# - no ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# - no ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# - no ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# - no ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6
# - no ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# after: {}

# After state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route

# Using gathered

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

- name: Gather facts of static routes
  cisco.ios.ios_static_routes:
    config:
    state: gathered

# Task Output
# -----------
#
# gathered:
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 198.51.100.0/24
#       next_hops:
#       - forward_router_address: 198.51.101.3
#         name: route_3
#       - distance_metric: 30
#         forward_router_address: 198.51.101.2
#         name: route_2
#       - distance_metric: 110
#         forward_router_address: 198.51.101.1
#         multicast: true
#         name: route_1
#         tag: 40
#   - afi: ipv6
#     routes:
#     - dest: 2001:DB8:0:3::/64
#       next_hops:
#       - forward_router_address: 2001:DB8:0:3::2
#         name: test_v6
#         tag: 105
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 192.0.2.0/24
#       next_hops:
#       - forward_router_address: 192.0.2.1
#         name: test_vrf
#         tag: 50
#         track: 150
#   vrf: blue

# Using rendered

- name: Render the commands for provided configuration
  cisco.ios.ios_static_routes:
    config:
      - vrf: blue
        address_families:
          - afi: ipv4
            routes:
              - dest: 192.0.2.0/24
                next_hops:
                  - forward_router_address: 192.0.2.1
                    name: test_vrf
                    tag: 50
                    track: 150
      - address_families:
          - afi: ipv4
            routes:
              - dest: 198.51.100.0/24
                next_hops:
                  - forward_router_address: 198.51.101.1
                    name: route_1
                    distance_metric: 110
                    tag: 40
                    multicast: true
                  - forward_router_address: 198.51.101.2
                    name: route_2
                    distance_metric: 30
                  - forward_router_address: 198.51.101.3
                    name: route_3
          - afi: ipv6
            routes:
              - dest: 2001:DB8:0:3::/64
                next_hops:
                  - forward_router_address: 2001:DB8:0:3::2
                    name: test_v6
                    tag: 105
    state: rendered

# Task Output
# -----------
#
# rendered:
# - ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# - ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# - ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# - ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# - ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

# Using parsed

# File: parsed.cfg
# ----------------
#
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

- name: Parse the provided configuration
  cisco.ios.ios_static_routes:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task Output
# -----------
#
# parsed:
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 198.51.100.0/24
#       next_hops:
#       - forward_router_address: 198.51.101.3
#         name: route_3
#       - distance_metric: 30
#         forward_router_address: 198.51.101.2
#         name: route_2
#       - distance_metric: 110
#         forward_router_address: 198.51.101.1
#         multicast: true
#         name: route_1
#         tag: 40
#   - afi: ipv6
#     routes:
#     - dest: 2001:DB8:0:3::/64
#       next_hops:
#       - forward_router_address: 2001:DB8:0:3::2
#         name: test_v6
#         tag: 105
# - address_families:
#   - afi: ipv4
#     routes:
#     - dest: 192.0.2.0/24
#       next_hops:
#       - forward_router_address: 192.0.2.1
#         name: test_vrf
#         tag: 50
#         track: 150
#   vrf: blue
```

## [Return Values](ios_static_routes_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format of the parameters above."]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format of the parameters above."]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device  **Returned:** always  **Sample:** `["ip route vrf test 172.31.10.0 255.255.255.0 10.10.10.2 name new_test multicast"]` |
| **gathered**  list / elements=string | The configuration as structured data transformed for the running configuration fetched from remote host  **Returned:** When `state` is *gathered*  **Sample:** `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **parsed**  list / elements=string | The configuration as structured data transformed for the value of `running_config` option  **Returned:** When `state` is *parsed*  **Sample:** `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **rendered**  list / elements=string | The set of CLI commands generated from the value in `config` option  **Returned:** When `state` is *rendered*  **Sample:** `["ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3", "ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6"]` |

### Authors

- Sagar Paul (@KB-perByte)
- Sumit Jaiswal (@justjais)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
