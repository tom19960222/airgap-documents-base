---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_bgp module – (deprecated, removed after 2023-01-27) Manages BGP configuration."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_bgp_module.html
fetched_at: 2026-07-27T17:01:38+00:00
---
# cisco.nxos.nxos_bgp module – (deprecated, removed after 2023-01-27) Manages BGP configuration.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_bgp`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_bgp_module.md#deprecated)
- [Synopsis](nxos_bgp_module.md#synopsis)
- [Parameters](nxos_bgp_module.md#parameters)
- [Notes](nxos_bgp_module.md#notes)
- [Examples](nxos_bgp_module.md#examples)
- [Return Values](nxos_bgp_module.md#return-values)
- [Status](nxos_bgp_module.md#status)

## [DEPRECATED](nxos_bgp_module.md#id1)

Removed in:
:   major release after 2023-01-27

Why:
:   Updated module released with more functionality.

Alternative:
:   nxos_bgp_global

## [Synopsis](nxos_bgp_module.md#id2)

- Manages BGP configurations on NX-OS switches.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_bgp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **asn**  string / required | BGP autonomous system number. Valid values are String, Integer in ASPLAIN or ASDOT notation. |
| **bestpath_always_compare_med**  boolean | Enable/Disable MED comparison on paths from different autonomous systems.  Choices:   - `false` - `true` |
| **bestpath_aspath_multipath_relax**  boolean | Enable/Disable load sharing across the providers with different (but equal-length) AS paths.  Choices:   - `false` - `true` |
| **bestpath_compare_neighborid**  boolean | Enable/Disable neighborid. Use this when more paths available than max path config.  Choices:   - `false` - `true` |
| **bestpath_compare_routerid**  boolean | Enable/Disable comparison of router IDs for identical eBGP paths.  Choices:   - `false` - `true` |
| **bestpath_cost_community_ignore**  boolean | Enable/Disable Ignores the cost community for BGP best-path calculations.  Choices:   - `false` - `true` |
| **bestpath_med_confed**  boolean | Enable/Disable enforcement of bestpath to do a MED comparison only between paths originated within a confederation.  Choices:   - `false` - `true` |
| **bestpath_med_missing_as_worst**  boolean | Enable/Disable assigns the value of infinity to received routes that do not carry the MED attribute, making these routes the least desirable.  Choices:   - `false` - `true` |
| **bestpath_med_non_deterministic**  boolean | Enable/Disable deterministic selection of the best MED pat from among the paths from the same autonomous system.  Choices:   - `false` - `true` |
| **cluster_id**  string | Route Reflector Cluster-ID. |
| **confederation_id**  string | Routing domain confederation AS. |
| **confederation_peers**  list / elements=string | AS confederation parameters. |
| **disable_policy_batching**  boolean | Enable/Disable the batching evaluation of prefix advertisement to all peers.  Choices:   - `false` - `true` |
| **disable_policy_batching_ipv4_prefix_list**  string | Enable/Disable the batching evaluation of prefix advertisements to all peers with prefix list. |
| **disable_policy_batching_ipv6_prefix_list**  string | Enable/Disable the batching evaluation of prefix advertisements to all peers with prefix list. |
| **enforce_first_as**  boolean | Enable/Disable enforces the neighbor autonomous system to be the first AS number listed in the AS path attribute for eBGP. On NX-OS, this property is only supported in the global BGP context.  Choices:   - `false` - `true` |
| **event_history_cli**  string | Enable/Disable cli event history buffer.  Choices:   - `"size_small"` - `"size_medium"` - `"size_large"` - `"size_disable"` - `"default"` - `"true"` - `"false"` |
| **event_history_detail**  string | Enable/Disable detail event history buffer.  Choices:   - `"size_small"` - `"size_medium"` - `"size_large"` - `"size_disable"` - `"default"` - `"true"` - `"false"` |
| **event_history_events**  string | Enable/Disable event history buffer.  Choices:   - `"size_small"` - `"size_medium"` - `"size_large"` - `"size_disable"` - `"default"` - `"true"` - `"false"` |
| **event_history_periodic**  string | Enable/Disable periodic event history buffer.  Choices:   - `"size_small"` - `"size_medium"` - `"size_large"` - `"size_disable"` - `"default"` - `"true"` - `"false"` |
| **fast_external_fallover**  boolean | Enable/Disable immediately reset the session if the link to a directly connected BGP peer goes down. Only supported in the global BGP context.  Choices:   - `false` - `true` |
| **flush_routes**  boolean | Enable/Disable flush routes in RIB upon controlled restart. On NX-OS, this property is only supported in the global BGP context.  Choices:   - `false` - `true` |
| **graceful_restart**  boolean | Enable/Disable graceful restart.  Choices:   - `false` - `true` |
| **graceful_restart_helper**  boolean | Enable/Disable graceful restart helper mode.  Choices:   - `false` - `true` |
| **graceful_restart_timers_restart**  string | Set maximum time for a restart sent to the BGP peer. |
| **graceful_restart_timers_stalepath_time**  string | Set maximum time that BGP keeps the stale routes from the restarting BGP peer. |
| **isolate**  boolean | Enable/Disable isolate this router from BGP perspective.  Choices:   - `false` - `true` |
| **local_as**  string | Local AS number to be used within a VRF instance. |
| **log_neighbor_changes**  boolean | Enable/Disable message logging for neighbor up/down event.  Choices:   - `false` - `true` |
| **maxas_limit**  string | Specify Maximum number of AS numbers allowed in the AS-path attribute. Valid values are between 1 and 512. |
| **neighbor_down_fib_accelerate**  boolean | Enable/Disable handle BGP neighbor down event, due to various reasons.  Choices:   - `false` - `true` |
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
| **reconnect_interval**  string | The BGP reconnection interval for dropped sessions. Valid values are between 1 and 60. |
| **router_id**  string | Router Identifier (ID) of the BGP router VRF instance. |
| **shutdown**  boolean | Administratively shutdown the BGP protocol.  Choices:   - `false` - `true` |
| **state**  string | Determines whether the config should be present or not on the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **suppress_fib_pending**  boolean | Enable/Disable advertise only routes programmed in hardware to peers.  Choices:   - `false` - `true` |
| **timer_bestpath_limit**  string | Specify timeout for the first best path after a restart, in seconds. |
| **timer_bgp_hold**  string | Set BGP hold timer. |
| **timer_bgp_keepalive**  string | Set BGP keepalive timer. |
| **vrf**  string | Name of the VRF. The name ‘default’ is a valid VRF representing the global BGP.  Default: `"default"` |

## [Notes](nxos_bgp_module.md#id4)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - `state=absent` removes the whole BGP ASN configuration when `vrf=default` or the whole VRF instance within the BGP process when using a different VRF.
> - Default when supported restores params default value.
> - Configuring global params is only permitted if `vrf=default`.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_bgp_module.md#id5)

```yaml+jinja
- name: Configure a simple ASN
  cisco.nxos.nxos_bgp:
    asn: 65535
    vrf: test
    router_id: 192.0.2.1
    state: present
```

## [Return Values](nxos_bgp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  Returned: always  Sample: `["router bgp 65535", "vrf test", "router-id 192.0.2.1"]` |

## [Status](nxos_bgp_module.md#id7)

- This module will be removed in a major release after 2023-01-27.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_bgp_module.md#deprecated).

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
