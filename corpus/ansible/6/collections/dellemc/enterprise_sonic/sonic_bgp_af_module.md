---
collection: ansible
version: "6"
title: "dellemc.enterprise_sonic.sonic_bgp_af module – Manage global BGP address-family and its parameters"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/enterprise_sonic/sonic_bgp_af_module.html
fetched_at: 2026-07-27T17:24:48+00:00
---
# dellemc.enterprise_sonic.sonic_bgp_af module – Manage global BGP address-family and its parameters

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/dellemc/enterprise_sonic) (version 1.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_bgp_af`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_bgp_af_module.md#synopsis)
- [Parameters](sonic_bgp_af_module.md#parameters)
- [Notes](sonic_bgp_af_module.md#notes)
- [Examples](sonic_bgp_af_module.md#examples)
- [Return Values](sonic_bgp_af_module.md#return-values)

## [Synopsis](sonic_bgp_af_module.md#id1)

- This module provides configuration management of global BGP_AF parameters on devices running Enterprise SONiC.
- bgp_as and vrf_name must be created in advance on the device.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_bgp_af_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies the BGP_AF related configuration. |
| **address_family**  dictionary | Specifies BGP address family related configurations. |
| **afis**  list / elements=dictionary | List of address families, such as ipv4, ipv6, and l2vpn.  afi and safi are required together. |
| **advertise_all_vni**  boolean | Specifies the advertise all vni flag.  Choices:   - `false` - `true` |
| **advertise_default_gw**  boolean | Specifies the advertise default gateway flag.  Choices:   - `false` - `true` |
| **advertise_prefix**  list / elements=dictionary | Specifies the prefix of the advertise.  afi and safi are required together. |
| **afi**  string | Specifies afi of the advertise.  Choices:   - `"ipv4"` - `"ipv6"` - `"l2vpn"` |
| **safi**  string | Specifies safi of the advertise.  Choices:   - `"unicast"` ← (default) - `"evpn"` |
| **afi**  string / required | Type of address family to configure.  Choices:   - `"ipv4"` - `"ipv6"` - `"l2vpn"` |
| **dampening**  boolean | Enable route flap dampening if set to true  Choices:   - `false` - `true` |
| **max_path**  dictionary | Specifies the maximum paths of ibgp and ebgp count. |
| **ebgp**  integer | Specifies the count of the ebgp multipaths count. |
| **ibgp**  integer | Specifies the count of the ibgp multipaths count. |
| **network**  list / elements=string | Enable routing on an IP network for each prefix provided in the network |
| **redistribute**  list / elements=dictionary | Specifies the redistribute information from another routing protocol. |
| **metric**  string | Specifies the metric for redistributed routes. |
| **protocol**  string / required | Specifies the protocol for configuring redistribute information.  Choices:   - `"ospf"` - `"static"` - `"connected"` |
| **route_map**  string | Specifies the route map reference. |
| **safi**  string | Specifies the type of communication for the address family.  Choices:   - `"unicast"` ← (default) - `"evpn"` |
| **bgp_as**  string / required | Specifies the BGP autonomous system (AS) number which is already configured on the device. |
| **vrf_name**  string | Specifies the VRF name which is already configured on the device.  Default: `"default"` |
| **state**  string | Specifies the operation to be performed on the BGP_AF process configured on the device.  In case of merged, the input configuration is merged with the existing BGP_AF configuration on the device.  In case of deleted, the existing BGP_AF configuration is removed from the device.  Choices:   - `"merged"` ← (default) - `"deleted"` |

## [Notes](sonic_bgp_af_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_bgp_af_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
#do show running-configuration bgp
#!
#router bgp 51
# router-id 111.2.2.41
# timers 60 180
# !
# address-family ipv4 unicast
#  maximum-paths 1
#  maximum-paths ibgp 1
#  dampening
# !
# address-family ipv6 unicast
#  redistribute connected route-map bb metric 21
#  redistribute ospf route-map aa metric 27
#  redistribute static route-map bb metric 26
#  maximum-paths 4
#  maximum-paths ibgp 5
# !
# address-family l2vpn evpn
#!
#
- name: Delete BGP Address family configuration from the device
  dellemc.enterprise_sonic.sonic_bgp_af:
     config:
       - bgp_as: 51
         address_family:
           afis:
             - afi: l2vpn
               safi: evpn
               advertise_all_vni: False
               advertise_default_gw: False
               advertise_prefix:
             - afi: ipv4
               safi: unicast
             - afi: ipv6
               safi: unicast
               max_path:
                 ebgp: 2
                 ibgp: 5
               redistribute:
                 - metric: "21"
                   protocol: connected
                   route_map: bb
                 - metric: "27"
                   protocol: ospf
                   route_map: aa
                 - metric: "26"
                   protocol: static
                   route_map: bb
     state: deleted

# After state:
# ------------
#
#do show running-configuration bgp
#!
#router bgp 51
# router-id 111.2.2.41
# timers 60 180
# !
# address-family ipv6 unicast
# !
# address-family l2vpn evpn
#
# Using deleted
#
# Before state:
# -------------
#
#do show running-configuration bgp
#!
#router bgp 51
# router-id 111.2.2.41
# timers 60 180
# !
# address-family ipv6 unicast
# !
# address-family l2vpn evpn
#
- name: Delete All BGP address family configurations
  dellemc.enterprise_sonic.sonic_bgp_af:
     config:
     state: deleted

# After state:
# ------------
#
#do show running-configuration bgp
#!
#router bgp 51
# router-id 111.2.2.41
# timers 60 180
#
# Using merged
#
# Before state:
# -------------
#
#do show running-configuration bgp
#!
#router bgp 51
# router-id 111.2.2.41
# timers 60 180
# !
# address-family l2vpn evpn
#
- name: Merge provided BGP address family configuration on the device.
  dellemc.enterprise_sonic.sonic_bgp_af:
     config:
       - bgp_as: 51
         address_family:
           afis:
             - afi: l2vpn
               safi: evpn
               advertise_all_vni: False
               advertise_default_gw: False
               advertise_prefix:
             - afi: ipv4
               safi: unicast
               network:
                 - 2.2.2.2/16
                 - 192.168.10.1/32
               dampening: True
             - afi: ipv6
               safi: unicast
               max_path:
                 ebgp: 4
                 ibgp: 5
               redistribute:
                 - metric: "21"
                   protocol: connected
                   route_map: bb
                 - metric: "27"
                   protocol: ospf
                   route_map: aa
                 - metric: "26"
                   protocol: static
                   route_map: bb
     state: merged
# After state:
# ------------
#
#do show running-configuration bgp
#!
#router bgp 51
# router-id 111.2.2.41
# timers 60 180
# !
# address-family ipv4 unicast
#  network 2.2.2.2/16
#  network 192.168.10.1/32
#  dampening
# !
# address-family ipv6 unicast
#  redistribute connected route-map bb metric 21
#  redistribute ospf route-map aa metric 27
#  redistribute static route-map bb metric 26
#  maximum-paths 4
#  maximum-paths ibgp 5
# !
# address-family l2vpn evpn
#
```

## [Return Values](sonic_bgp_af_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  Returned: when changed  Sample: `["The configuration returned always in the same format of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  Returned: always  Sample: `["The configuration returned is always in the same format of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  Returned: always  Sample: `["command 1", "command 2", "command 3"]` |

### Authors

- Niraimadaiselvam M (@niraimadaiselvamm)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
[Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
