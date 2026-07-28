---
collection: ansible
version: "6"
title: "cisco.ios.ios_static_routes module – Resource module to configure static routes."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_static_routes_module.html
fetched_at: 2026-07-27T16:55:30+00:00
---
# cisco.ios.ios_static_routes module – Resource module to configure static routes.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/cisco/ios) (version 3.3.2).
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

## [Parameters](ios_static_routes_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | A dictionary of static route options |
| **address_families**  list / elements=dictionary | Address family to use for the static routes |
| **afi**  string / required | Top level address family indicator.  Choices:   - `"ipv4"` - `"ipv6"` |
| **routes**  list / elements=dictionary | Configuring static route |
| **dest**  string / required | Destination prefix with its subnet mask |
| **next_hops**  list / elements=dictionary | next hop address or interface |
| **dhcp**  boolean | Default gateway obtained from DHCP  Choices:   - `false` - `true` |
| **distance_metric**  integer | Distance metric for this route |
| **forward_router_address**  string | Forwarding router’s address |
| **global**  boolean | Next hop address is global  Choices:   - `false` - `true` |
| **interface**  string | Interface for directly connected static routes |
| **multicast**  boolean | multicast route  Choices:   - `false` - `true` |
| **name**  string | Specify name of the next hop |
| **permanent**  boolean | permanent route  Choices:   - `false` - `true` |
| **tag**  integer | Set tag for this route  Refer to vendor documentation for valid values. |
| **track**  integer | Install route depending on tracked item with tracked object number.  Tracking does not support multicast  Refer to vendor documentation for valid values. |
| **topology**  string | Configure static route for a Topology Routing/Forwarding instance  NOTE, VRF and Topology can be used together only with Multicast and Topology should pre-exist before it can be used |
| **vrf**  string | IP VPN Routing/Forwarding instance name.  NOTE, In case of IPV4/IPV6 VRF routing table should pre-exist before configuring.  NOTE, if the vrf information is not provided then the routes shall be configured under global vrf. |
| **running_config**  string | This option is used only with state *parsed*.  The value of this option should be the output received from the IOS device by executing the command **show running-config | include ip route|ipv6 route**.  The state *parsed* reads the configuration from `running_config` option and transforms it into Ansible structured data as per the resource module’s argspec and the value is then returned in the *parsed* key within the result. |
| **state**  string | The state the configuration should be left in  The states *rendered*, *gathered* and *parsed* does not perform any change on the device.  The state *rendered* will transform the configuration in `config` option to platform specific CLI commands which will be returned in the *rendered* key within the result. For state *rendered* active connection to remote host is not required.  The state *gathered* will fetch the running configuration from device and transform it into structured data in the format as per the resource module argspec and the value is returned in the *gathered* key within the result.  The state *parsed* reads the configuration from `running_config` option and transforms it into JSON format as per the resource module parameters and the value is returned in the *parsed* key within the result. The value of `running_config` option should be the same format as the output of command *show running-config | include ip route|ipv6 route* executed on device. For state *parsed* active connection to remote host is not required.  Choices:   - `"merged"` ← (default) - `"replaced"` - `"overridden"` - `"deleted"` - `"gathered"` - `"rendered"` - `"parsed"` |

## [Notes](ios_static_routes_module.md#id3)

> **Note:**
>
> - Tested against Cisco IOSv Version 15.2 on VIRL.
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>

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

# Commands fired:
# ---------------
# ip route vrf blue 192.0.2.0 255.255.255.0 10.0.0.8 name merged_blue track 150 tag 50
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name merged_route_1 tag 40
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name merged_route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name merged_route_3
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 name merged_v6 tag 105

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
# ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 name test_vrf track 150 tag 50
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name route_1 tag 40
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 name test_v6 tag 105

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

# Commands fired:
# ---------------
# no ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name route_1 tag 40
# no ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# no ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 175 name replaced_route track 150 tag 70

# After state:
# ------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 name test_vrf track 150 tag 50
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 175 name replaced_route track 150 tag 70
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

# Using overridden

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 name test_vrf track 150 tag 50
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name route_1 tag 40
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 name test_v6 tag 105

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

# Commands fired:
# ---------------
# no ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name route_1 tag 40
# no ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# no ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# no ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 198.51.101.8 name test_vrf track 150 tag 50
# no ipv6 route FD5D:12C9:2201:1::/64 FD5D:12C9:2202::2 name test_v6 tag 105
# ip route vrf blue 192.0.2.0 255.255.255.0 198.51.101.4 name override_vrf track 150 tag 50

# After state:
# ------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf blue 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name override_vrf track 150

# Using Deleted

# Example 1:
# ----------
# To delete the exact static routes, with all the static routes explicitly mentioned in want

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 name test_vrf track 150 tag 50
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name route_1 tag 40
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 name test_v6 tag 105

- name: Delete provided configuration from the device configuration
  cisco.ios.ios_static_routes:
    config:
    - vrf: ansible_temp_vrf
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

# Commands fired:
# ---------------
# no ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 198.51.101.8 name test_vrf track 150 tag 50
# no ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name route_1 tag 40
# no ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# no ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# no ipv6 route FD5D:12C9:2201:1::/64 FD5D:12C9:2202::2 name test_v6 tag 105

# After state:
# ------------
#
# vios#show running-config | include ip route|ipv6 route

# Example 2:
# ----------
# To delete the destination specific static routes

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 name test_vrf track 150 tag 50
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name route_1 tag 40
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 name test_v6 tag 105

- name: Delete provided configuration from the device configuration
  cisco.ios.ios_static_routes:
    config:
    - address_families:
      - afi: ipv4
        routes:
        - dest: 198.51.100.0/24
    state: deleted

# Commands fired:
# ---------------
# no ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# no ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# no ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast

# After state:
# ------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

# Example 3:
# ----------
# To delete the vrf specific static routes

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 name test_vrf track 150 tag 50
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name route_1 tag 40
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 name test_v6 tag 105

- name: Delete provided configuration from the device configuration
  cisco.ios.ios_static_routes:
    config:
    - vrf: ansible_temp_vrf
    state: deleted

# Commands fired:
# ---------------
# no ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 name test_vrf track 150 tag 50

# After state:
# ------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

# Using Deleted without any config passed
#"(NOTE: This will delete all of configured resource module attributes from each configured interface)"

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 name test_vrf track 150 tag 50
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name route_1 tag 40
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 name test_v6 tag 105

- name: Delete ALL configured IOS static routes
  cisco.ios.ios_static_routes:
    state: deleted

# Commands fired:
# ---------------
# no ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 tag 50 name test_vrf track 150
# no ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# no ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# no ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 tag 40 name route_1 multicast
# no ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 tag 105 name test_v6

# After state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
#

# Using gathered

# Before state:
# -------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 name test_vrf track 150 tag 50
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name route_1 tag 40
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 name test_v6 tag 105

- name: Gather listed static routes with provided configurations
  cisco.ios.ios_static_routes:
    config:
    state: gathered

# Module Execution Result:
# ------------------------
#
# "gathered": [
#         {
#             "address_families": [
#                 {
#                     "afi": "ipv4",
#                     "routes": [
#                         {
#                             "dest": "192.0.2.0/24",
#                             "next_hops": [
#                                 {
#                                     "forward_router_address": "192.0.2.1",
#                                     "name": "test_vrf",
#                                     "tag": 50,
#                                     "track": 150
#                                 }
#                             ]
#                         }
#                     ]
#                 }
#             ],
#             "vrf": "ansible_temp_vrf"
#         },
#         {
#             "address_families": [
#                 {
#                     "afi": "ipv6",
#                     "routes": [
#                         {
#                             "dest": "2001:DB8:0:3::/64",
#                             "next_hops": [
#                                 {
#                                     "forward_router_address": "2001:DB8:0:3::2",
#                                     "name": "test_v6",
#                                     "tag": 105
#                                 }
#                             ]
#                         }
#                     ]
#                 },
#                 {
#                     "afi": "ipv4",
#                     "routes": [
#                         {
#                             "dest": "198.51.100.0/24",
#                             "next_hops": [
#                                 {
#                                     "distance_metric": 110,
#                                     "forward_router_address": "198.51.101.1",
#                                     "multicast": true,
#                                     "name": "route_1",
#                                     "tag": 40
#                                 },
#                                 {
#                                     "distance_metric": 30,
#                                     "forward_router_address": "198.51.101.2",
#                                     "name": "route_2"
#                                 },
#                                 {
#                                     "forward_router_address": "198.51.101.3",
#                                     "name": "route_3"
#                                 }
#                             ]
#                         }
#                     ]
#                 }
#             ]
#         }
#     ]

# After state:
# ------------
#
# vios#show running-config | include ip route|ipv6 route
# ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 name test_vrf track 150 tag 50
# ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name route_1 tag 40
# ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2
# ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3
# ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 name test_v6 tag 105

# Using rendered

- name: Render the commands for provided  configuration
  cisco.ios.ios_static_routes:
    config:
    - vrf: ansible_temp_vrf
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

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "ip route vrf ansible_temp_vrf 192.0.2.0 255.255.255.0 192.0.2.1 name test_vrf track 150 tag 50",
#         "ip route 198.51.100.0 255.255.255.0 198.51.101.1 110 multicast name route_1 tag 40",
#         "ip route 198.51.100.0 255.255.255.0 198.51.101.2 30 name route_2",
#         "ip route 198.51.100.0 255.255.255.0 198.51.101.3 name route_3",
#         "ipv6 route 2001:DB8:0:3::/64 2001:DB8:0:3::2 name test_v6 tag 105"
#     ]
```

## [Return Values](ios_static_routes_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The configuration as structured data after module completion.  Returned: when changed  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **before**  list / elements=string | The configuration as structured data prior to module invocation.  Returned: always  Sample: `["The configuration returned will always be in the same format of the parameters above."]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device  Returned: always  Sample: `["ip route vrf test 172.31.10.0 255.255.255.0 10.10.10.2 name new_test multicast"]` |
| **gathered**  list / elements=string | The configuration as structured data transformed for the running configuration fetched from remote host  Returned: When `state` is *gathered*  Sample: `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **parsed**  list / elements=string | The configuration as structured data transformed for the value of `running_config` option  Returned: When `state` is *parsed*  Sample: `["The configuration returned will always be in the same format of the parameters above.\n"]` |
| **rendered**  list / elements=string | The set of CLI commands generated from the value in `config` option  Returned: When `state` is *rendered*  Sample: `["interface Ethernet1/1", "mtu 1800"]` |

### Authors

- Sumit Jaiswal (@justjais)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
