---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_bgp_af module – (deprecated, removed after 2023-02-24) Manages BGP Address-family configuration."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_bgp_af_module.html
fetched_at: 2026-07-27T17:01:40+00:00
---
# cisco.nxos.nxos_bgp_af module – (deprecated, removed after 2023-02-24) Manages BGP Address-family configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_bgp_af`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_bgp_af_module.md#deprecated)
- [Synopsis](nxos_bgp_af_module.md#synopsis)
- [Parameters](nxos_bgp_af_module.md#parameters)
- [Notes](nxos_bgp_af_module.md#notes)
- [Examples](nxos_bgp_af_module.md#examples)
- [Return Values](nxos_bgp_af_module.md#return-values)
- [Status](nxos_bgp_af_module.md#status)

## [DEPRECATED](nxos_bgp_af_module.md#id1)

Removed in:
:   major release after 2023-02-24

Why:
:   Updated module released with more functionality.

Alternative:
:   nxos_bgp_address_family

## [Synopsis](nxos_bgp_af_module.md#id2)

- Manages BGP Address-family configurations on NX-OS switches.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_bgp_af_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **additional_paths_install**  boolean | Install a backup path into the forwarding table and provide prefix independent convergence (PIC) in case of a PE-CE link failure.  Choices:   - `false` - `true` |
| **additional_paths_receive**  boolean | Enables the receive capability of additional paths for all of the neighbors under this address family for which the capability has not been disabled.  Choices:   - `false` - `true` |
| **additional_paths_selection**  string | Configures the capability of selecting additional paths for a prefix. Valid values are a string defining the name of the route-map. |
| **additional_paths_send**  boolean | Enables the send capability of additional paths for all of the neighbors under this address family for which the capability has not been disabled.  Choices:   - `false` - `true` |
| **advertise_l2vpn_evpn**  boolean | Advertise evpn routes.  Choices:   - `false` - `true` |
| **afi**  string / required | Address Family Identifier.  Choices:   - `"ipv4"` - `"ipv6"` - `"vpnv4"` - `"vpnv6"` - `"l2vpn"` |
| **asn**  string / required | BGP autonomous system number. Valid values are String, Integer in ASPLAIN or ASDOT notation. |
| **client_to_client**  boolean | Configure client-to-client route reflection.  Choices:   - `false` - `true` |
| **dampen_igp_metric**  string | Specify dampen value for IGP metric-related changes, in seconds. Valid values are integer and keyword ‘default’. |
| **dampening_half_time**  string | Specify decay half-life in minutes for route-flap dampening. Valid values are integer and keyword ‘default’. |
| **dampening_max_suppress_time**  string | Specify max suppress time for route-flap dampening stable route. Valid values are integer and keyword ‘default’. |
| **dampening_reuse_time**  string | Specify route reuse time for route-flap dampening. Valid values are integer and keyword ‘default’. |
| **dampening_routemap**  string | Specify route-map for route-flap dampening. Valid values are a string defining the name of the route-map. |
| **dampening_state**  boolean | Enable/disable route-flap dampening.  Choices:   - `false` - `true` |
| **dampening_suppress_time**  string | Specify route suppress time for route-flap dampening. Valid values are integer and keyword ‘default’. |
| **default_information_originate**  boolean | Default information originate.  Choices:   - `false` - `true` |
| **default_metric**  string | Sets default metrics for routes redistributed into BGP. Valid values are Integer or keyword ‘default’ |
| **distance_ebgp**  string | Sets the administrative distance for eBGP routes. Valid values are Integer or keyword ‘default’. |
| **distance_ibgp**  string | Sets the administrative distance for iBGP routes. Valid values are Integer or keyword ‘default’. |
| **distance_local**  string | Sets the administrative distance for local BGP routes. Valid values are Integer or keyword ‘default’. |
| **inject_map**  list / elements=list | An array of route-map names which will specify prefixes to inject. Each array entry must first specify the inject-map name, secondly an exist-map name, and optionally the copy-attributes keyword which indicates that attributes should be copied from the aggregate. For example [[‘lax_inject_map’, ‘lax_exist_map’], [‘nyc_inject_map’, ‘nyc_exist_map’, ‘copy-attributes’], [‘fsd_inject_map’, ‘fsd_exist_map’]]. |
| **maximum_paths**  string | Configures the maximum number of equal-cost paths for load sharing. Valid value is an integer in the range 1-64. |
| **maximum_paths_ibgp**  string | Configures the maximum number of ibgp equal-cost paths for load sharing. Valid value is an integer in the range 1-64. |
| **networks**  list / elements=list | Networks to configure. Valid value is a list of network prefixes to advertise. The list must be in the form of an array. Each entry in the array must include a prefix address and an optional route-map. For example [[‘10.0.0.0/16’, ‘routemap_LA’], [‘192.168.1.1’, ‘Chicago’], [‘192.168.2.0/24’], [‘192.168.3.0/24’, ‘routemap_NYC’]]. |
| **next_hop_route_map**  string | Configure a route-map for valid nexthops. Valid values are a string defining the name of the route-map. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  Starting with Ansible 2.6 we recommend using `connection: httpapi` for NX-API.  This option will be removed in a release after 2022-06-01.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_nxos.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This is a common argument used for either *cli* or *nxapi* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. This value applies to either *cli* or *nxapi*. The port value will default to the appropriate transport common port if none is provided in the task. (cli=22, http=80, https=443). |
| **ssh_keyfile**  string | Specifies the SSH key to use to authenticate the connection to the remote device. This argument is only used for the *cli* transport. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. NX-API can be slow to return on long-running commands (sh mac, sh bgp, etc). |
| **transport**  string | Configures the transport connection to use when connecting to the remote device. The transport argument supports connectivity to the device over cli (ssh) or nxapi.  Choices:   - `"cli"` ← (default) - `"nxapi"` |
| **use_proxy**  boolean | If `no`, the environment variables `http_proxy` and `https_proxy` will be ignored.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | Configures the *transport* to use SSL if set to `yes` only when the `transport=nxapi`, otherwise this value is ignored.  Choices:   - `false` ← (default) - `true` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate either the CLI login or the nxapi authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates. If the transport argument is not nxapi, this value is ignored.  Choices:   - `false` ← (default) - `true` |
| **redistribute**  list / elements=list | A list of redistribute directives. Multiple redistribute entries are allowed. The list must be in the form of a nested array. the first entry of each array defines the source-protocol to redistribute from; the second entry defines a route-map name. A route-map is highly advised but may be optional on some platforms, in which case it may be omitted from the array list. For example [[‘direct’, ‘rm_direct’], [‘lisp’, ‘rm_lisp’]]. |
| **retain_route_target**  string  added in cisco.nxos 1.1.0 | Retains all of the routes or the routes which are part of configured route-map. Valid values are route-map names or keyword `all` or keyword `default`. `all` retains all the routes regardless of Target-VPN community. `default` will disable the retain route target option. If you are using route-map name please ensure that the name is not same as `all` and `default`. |
| **safi**  string / required | Sub Address Family Identifier.  Choices:   - `"unicast"` - `"multicast"` - `"evpn"` |
| **state**  string | Determines whether the config should be present or not on the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **suppress_inactive**  boolean | Advertises only active routes to peers.  Choices:   - `false` - `true` |
| **table_map**  string | Apply table-map to filter routes downloaded into URIB. Valid values are a string. |
| **table_map_filter**  boolean | Filters routes rejected by the route-map and does not download them to the RIB.  Choices:   - `false` - `true` |
| **vrf**  string | Name of the VRF. The name ‘default’ is a valid VRF representing the global bgp.  Default: `"default"` |

## [Notes](nxos_bgp_af_module.md#id4)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - `state=absent` removes the whole BGP ASN configuration
> - Default, where supported, restores params default value.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_bgp_af_module.md#id5)

```yaml+jinja
# configure a simple address-family
- cisco.nxos.nxos_bgp_af:
    asn: 65535
    vrf: TESTING
    afi: ipv4
    safi: unicast
    advertise_l2vpn_evpn: true
    state: present
    retain_route_target: all
```

## [Return Values](nxos_bgp_af_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  Returned: always  Sample: `["router bgp 65535", "vrf TESTING", "address-family ipv4 unicast", "advertise l2vpn evpn", "retain route-target all"]` |

## [Status](nxos_bgp_af_module.md#id7)

- This module will be removed in a major release after 2023-02-24.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_bgp_af_module.md#deprecated).

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
