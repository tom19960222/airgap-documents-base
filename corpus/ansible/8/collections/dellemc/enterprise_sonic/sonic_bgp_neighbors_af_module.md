---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_bgp_neighbors_af module – Manage the BGP neighbor address-family and its parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_bgp_neighbors_af_module.html
fetched_at: 2026-07-28T02:03:32+00:00
---
# dellemc.enterprise_sonic.sonic_bgp_neighbors_af module – Manage the BGP neighbor address-family and its parameters

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_bgp_neighbors_af`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_bgp_neighbors_af_module.md#synopsis)
- [Parameters](sonic_bgp_neighbors_af_module.md#parameters)
- [Notes](sonic_bgp_neighbors_af_module.md#notes)
- [Examples](sonic_bgp_neighbors_af_module.md#examples)
- [Return Values](sonic_bgp_neighbors_af_module.md#return-values)

## [Synopsis](sonic_bgp_neighbors_af_module.md#id1)

- This module provides configuration management of BGP neighbors address-family parameters on devices running Enterprise SONiC.
- bgp_as, vrf_name and neighbors need be created in advance on the device.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_bgp_neighbors_af_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies the BGP neighbors address-family related configuration. |
| **bgp_as**  string / required | Specifies the BGP autonomous system (AS) number which is already configured on the device. |
| **neighbors**  list / elements=dictionary | Specifies BGP neighbor related configurations in address-family configuration mode. |
| **address_family**  list / elements=dictionary | Specifies BGP address-family related configurations.  afi and safi are required together. |
| **activate**  boolean | Enables the address-family for this neighbor.  **Choices:**   - `false` - `true` |
| **afi**  string / required | Type of address-family to configure.  **Choices:**   - `"ipv4"` - `"ipv6"` - `"l2vpn"` |
| **allowas_in**  dictionary | Specifies the allowas in values. |
| **origin**  boolean | Specifies the origin value.  **Choices:**   - `false` - `true` |
| **value**  integer | Specifies the value of the allowas in. |
| **ip_afi**  dictionary | Common configuration attributes for IPv4 and IPv6 unicast address families. |
| **default_policy_name**  string | Specifies routing policy definition. |
| **send_default_route**  boolean | Enable or disable sending of default-route to the neighbor.  **Choices:**   - `false` ← (default) - `true` |
| **prefix_limit**  dictionary | Specifies prefix limit attributes. |
| **max_prefixes**  integer | Maximum number of prefixes that will be accepted from the neighbor. |
| **prevent_teardown**  boolean | Enable or disable teardown of BGP session when maximum prefix limit is exceeded.  **Choices:**   - `false` ← (default) - `true` |
| **restart_timer**  integer | Time interval in seconds after which the BGP session is re-established after being torn down. |
| **warning_threshold**  integer | Threshold on number of prefixes that can be received from a neighbor before generation of warning messages.  Expressed as a percentage of max-prefixes. |
| **prefix_list_in**  string | Inbound route filtering policy for a neighbor. |
| **prefix_list_out**  string | Outbound route filtering policy for a neighbor. |
| **route_map**  list / elements=dictionary | Specifies the route-map. |
| **direction**  string | Specifies the direction of the route-map. |
| **name**  string | Specifies the name of the route-map. |
| **route_reflector_client**  boolean | Specifies a neighbor as a route-reflector client.  **Choices:**   - `false` - `true` |
| **route_server_client**  boolean | Specifies a neighbor as a route-server client.  **Choices:**   - `false` - `true` |
| **safi**  string | Specifies the type of cast for the address-family.  **Choices:**   - `"unicast"` ← (default) - `"evpn"` |
| **neighbor**  string / required | Neighbor router address which is already configured on the device. |
| **vrf_name**  string | Specifies the VRF name which is already configured on the device.  **Default:** `"default"` |
| **state**  string | Specifies the operation to be performed on the BGP process that is configured on the device.  In case of merged, the input configuration is merged with the existing BGP configuration on the device.  In case of deleted, the existing BGP configuration is removed from the device.  **Choices:**   - `"merged"` ← (default) - `"deleted"` |

## [Notes](sonic_bgp_neighbors_af_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_bgp_neighbors_af_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
#!
#router bgp 4
# !
# neighbor interface Eth1/3
#  !
#  address-family ipv4 unicast
#   activate
#   allowas-in 4
#   route-map aa in
#   route-map aa out
#   route-reflector-client
#   route-server-client
#   send-community both
#!
#
- name: Deletes neighbors address-family with specific values
  dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
     config:
       - bgp_as: 4
         neighbors:
           - neighbor: Eth1/3
             address_family:
               - afi: ipv4
                 safi: unicast
                 allowas_in:
                   value: 4
                 route_map:
                   - name: aa
                     direction: in
                   - name: aa
                     direction: out
                 route_reflector_client: true
                 route_server_client: true
     state: deleted

# After state:
# ------------
#!
#router bgp 4
# !
# neighbor interface Eth1/3
#  !
#  address-family ipv4 unicast
#   send-community both
#!

# Using deleted
#
# Before state:
# -------------
#
#!
#router bgp 4
# !
# neighbor interface Eth1/3
#  !
#  address-family ipv4 unicast
#   activate
#   allowas-in 4
#   route-map aa in
#   route-map aa out
#   route-reflector-client
#   route-server-client
#   send-community both
#!
# neighbor interface Eth1/5
#  !
#  address-family ipv4 unicast
#   activate
#   allowas-in origin
#   send-community both
#!
#
- name: Deletes neighbors address-family with specific values
  dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
     config:
     state: deleted

# After state:
# ------------
#!
#router bgp 4
#!

# Using deleted
#
# Before state:
# -------------
#
#!
#router bgp 4
# !
# neighbor interface Eth1/3
#!
#
- name: Merges neighbors address-family with specific values
  dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
     config:
       - bgp_as: 4
         neighbors:
           - neighbor: Eth1/3
             address_family:
               - afi: ipv4
                 safi: unicast
                 allowas_in:
                   value: 4
                 route_map:
                   - name: aa
                     direction: in
                   - name: aa
                     direction: out
                 route_reflector_client: true
                 route_server_client: true
     state: merged

# After state:
# ------------
#!
#router bgp 4
# !
# neighbor interface Eth1/3
#  !
#  address-family ipv4 unicast
#   activate
#   allowas-in 4
#   route-map aa in
#   route-map aa out
#   route-reflector-client
#   route-server-client
#   send-community both
#!

# Using merged
#
# Before state:
# -------------
#
# sonic# show running-configuration bgp neighbor vrf default 1.1.1.1
# (No bgp neighbor configuration present)
- name: "Configure BGP neighbor prefix-list attributes"
  dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
    config:
     - bgp_as: 51
       neighbors:
         - neighbor: 1.1.1.1
           address_family:
             - afi: ipv4
               safi: unicast
               ip_afi:
                 default_policy_name: rmap_reg1
                 send_default_route: true
               prefix_limit:
                 max_prefixes: 1
                 prevent_teardown: true
                 warning_threshold: 80
               prefix_list_in: p1
               prefix_list_out: p2
    state: merged
# After state:
# ------------
#
# sonic# show running-configuration bgp neighbor vrf default 1.1.1.1
# !
# neighbor 1.1.1.1
#  !
#  address-family ipv4 unicast
#   default-originate route-map rmap_reg1
#   prefix-list p1 in
#   prefix-list p2 out
#   send-community both
#   maximum-prefix 1 80 warning-only

# Using deleted
#
# Before state:
# -------------
#
# sonic# show running-configuration bgp neighbor vrf default 1.1.1.1
# !
# neighbor 1.1.1.1
#  !
#  address-family ipv6 unicast
#   default-originate route-map rmap_reg2
#   prefix-list p1 in
#   prefix-list p2 out
#   send-community both
#   maximum-prefix 5 90 restart 2
- name: "Delete BGP neighbor prefix-list attributes"
  dellemc.enterprise_sonic.sonic_bgp_neighbors_af:
    config:
     - bgp_as: 51
       neighbors:
         - neighbor: 1.1.1.1
           address_family:
             - afi: ipv6
               safi: unicast
               ip_afi:
                 default_policy_name: rmap_reg2
                 send_default_route: true
               prefix_limit:
                 max_prefixes: 5
                 warning_threshold: 90
                 restart-timer: 2
               prefix_list_in: p1
               prefix_list_out: p2
    state: deleted
# sonic# show running-configuration bgp neighbor vrf default 1.1.1.1
# (No bgp neighbor configuration present)
```

## [Return Values](sonic_bgp_neighbors_af_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Niraimadaiselvam M (@niraimadaiselvamm)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
