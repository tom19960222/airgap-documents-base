---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_bgp_neighbor_af module – (deprecated, removed after 2023-02-24) Manages BGP address-family’s neighbors configuration."
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_bgp_neighbor_af_module.html
fetched_at: 2026-07-28T01:38:35+00:00
---
# cisco.nxos.nxos_bgp_neighbor_af module – (deprecated, removed after 2023-02-24) Manages BGP address-family’s neighbors configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_bgp_neighbor_af`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_bgp_neighbor_af_module.md#deprecated)
- [Synopsis](nxos_bgp_neighbor_af_module.md#synopsis)
- [Parameters](nxos_bgp_neighbor_af_module.md#parameters)
- [Notes](nxos_bgp_neighbor_af_module.md#notes)
- [Examples](nxos_bgp_neighbor_af_module.md#examples)
- [Return Values](nxos_bgp_neighbor_af_module.md#return-values)
- [Status](nxos_bgp_neighbor_af_module.md#status)

## [DEPRECATED](nxos_bgp_neighbor_af_module.md#id1)

Removed in:
:   major release after 2023-02-24

Why:
:   Updated module released with more functionality.

Alternative:
:   nxos_bgp_neighbor_address_family

## [Synopsis](nxos_bgp_neighbor_af_module.md#id2)

- Manages BGP address-family’s neighbors configurations on NX-OS switches.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: bgp_neighbor_af

## [Parameters](nxos_bgp_neighbor_af_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **additional_paths_receive**  string | Valid values are enable for basic command enablement; disable for disabling the command at the neighbor af level (it adds the disable keyword to the basic command); and inherit to remove the command at this level (the command value is inherited from a higher BGP layer).  **Choices:**   - `"enable"` - `"disable"` - `"inherit"` |
| **additional_paths_send**  string | Valid values are enable for basic command enablement; disable for disabling the command at the neighbor af level (it adds the disable keyword to the basic command); and inherit to remove the command at this level (the command value is inherited from a higher BGP layer).  **Choices:**   - `"enable"` - `"disable"` - `"inherit"` |
| **advertise_map_exist**  list / elements=string | Conditional route advertisement. This property requires two route maps, an advertise-map and an exist-map. Valid values are an array specifying both the advertise-map name and the exist-map name, or simply ‘default’ e.g. [‘my_advertise_map’, ‘my_exist_map’]. This command is mutually exclusive with the advertise_map_non_exist property. |
| **advertise_map_non_exist**  list / elements=string | Conditional route advertisement. This property requires two route maps, an advertise-map and an exist-map. Valid values are an array specifying both the advertise-map name and the non-exist-map name, or simply ‘default’ e.g. [‘my_advertise_map’, ‘my_non_exist_map’]. This command is mutually exclusive with the advertise_map_exist property. |
| **afi**  string / required | Address Family Identifier.  **Choices:**   - `"ipv4"` - `"ipv6"` - `"vpnv4"` - `"vpnv6"` - `"l2vpn"` |
| **allowas_in**  boolean | Activate allowas-in property  **Choices:**   - `false` - `true` |
| **allowas_in_max**  string | Max-occurrences value for allowas_in. Valid values are an integer value or ‘default’. This is mutually exclusive with allowas_in. |
| **as_override**  boolean | Activate the as-override feature.  **Choices:**   - `false` - `true` |
| **asn**  string / required | BGP autonomous system number. Valid values are String, Integer in ASPLAIN or ASDOT notation. |
| **default_originate**  boolean | Activate the default-originate feature.  **Choices:**   - `false` - `true` |
| **default_originate_route_map**  string | Route-map for the default_originate property. Valid values are a string defining a route-map name, or ‘default’. This is mutually exclusive with default_originate. |
| **disable_peer_as_check**  boolean | Disable checking of peer AS-number while advertising  **Choices:**   - `false` - `true` |
| **filter_list_in**  string | Valid values are a string defining a filter-list name, or ‘default’. |
| **filter_list_out**  string | Valid values are a string defining a filter-list name, or ‘default’. |
| **max_prefix_interval**  string | Optional restart interval. Valid values are an integer. Requires max_prefix_limit. May not be combined with max_prefix_warning. |
| **max_prefix_limit**  string | maximum-prefix limit value. Valid values are an integer value or ‘default’. |
| **max_prefix_threshold**  string | Optional threshold percentage at which to generate a warning. Valid values are an integer value. Requires max_prefix_limit. |
| **max_prefix_warning**  boolean | Optional warning-only keyword. Requires max_prefix_limit. May not be combined with max_prefix_interval.  **Choices:**   - `false` - `true` |
| **neighbor**  string / required | Neighbor Identifier. Valid values are string. Neighbors may use IPv4 or IPv6 notation, with or without prefix length. |
| **next_hop_self**  boolean | Activate the next-hop-self feature.  **Choices:**   - `false` - `true` |
| **next_hop_third_party**  boolean | Activate the next-hop-third-party feature.  **Choices:**   - `false` - `true` |
| **prefix_list_in**  string | Valid values are a string defining a prefix-list name, or ‘default’. |
| **prefix_list_out**  string | Valid values are a string defining a prefix-list name, or ‘default’. |
| **rewrite_evpn_rt_asn**  boolean  *added in cisco.nxos 1.1.0* | Auto generate route targets for EBGP neighbor.  **Choices:**   - `false` - `true` |
| **route_map_in**  string | Valid values are a string defining a route-map name, or ‘default’. |
| **route_map_out**  string | Valid values are a string defining a route-map name, or ‘default’. |
| **route_reflector_client**  boolean | Router reflector client.  **Choices:**   - `false` - `true` |
| **safi**  string / required | Sub Address Family Identifier.  **Choices:**   - `"unicast"` - `"multicast"` - `"evpn"` |
| **send_community**  string | send-community attribute.  **Choices:**   - `"none"` - `"both"` - `"extended"` - `"standard"` - `"default"` |
| **soft_reconfiguration_in**  string | Valid values are ‘enable’ for basic command enablement; ‘always’ to add the always keyword to the basic command; and ‘inherit’ to remove the command at this level (the command value is inherited from a higher BGP layer).  **Choices:**   - `"enable"` - `"always"` - `"inherit"` |
| **soo**  string | Site-of-origin. Valid values are a string defining a VPN extcommunity or ‘default’. |
| **state**  string | Determines whether the config should be present or not on the device.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **suppress_inactive**  boolean | suppress-inactive feature.  **Choices:**   - `false` - `true` |
| **unsuppress_map**  string | unsuppress-map. Valid values are a string defining a route-map name or ‘default’. |
| **vrf**  string | Name of the VRF. The name ‘default’ is a valid VRF representing the global bgp.  **Default:** `"default"` |
| **weight**  string | Weight value. Valid values are an integer value or ‘default’. |

## [Notes](nxos_bgp_neighbor_af_module.md#id4)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - `state=absent` removes the whole BGP address-family’s neighbor configuration.
> - Default, when supported, removes properties
> - In order to default maximum-prefix configuration, only `max_prefix_limit=default` is needed.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_bgp_neighbor_af_module.md#id5)

```yaml+jinja
- name: configure RR client
  cisco.nxos.nxos_bgp_neighbor_af:
    asn: 65535
    neighbor: 192.0.2.3
    afi: ipv4
    safi: unicast
    route_reflector_client: true
    state: present
    rewrite_evpn_rt_asn: true
```

## [Return Values](nxos_bgp_neighbor_af_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  **Returned:** always  **Sample:** `["router bgp 65535", "neighbor 192.0.2.3", "address-family ipv4 unicast", "route-reflector-client", "rewrite-evpn-rt-asn"]` |

## [Status](nxos_bgp_neighbor_af_module.md#id7)

- This module will be removed in a major release after 2023-02-24.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_bgp_neighbor_af_module.md#deprecated).

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
