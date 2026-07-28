---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_bgp_neighbor module – (deprecated, removed after 2023-01-27) Manages BGP neighbors configurations."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_bgp_neighbor_module.html
fetched_at: 2026-07-27T17:01:41+00:00
---
# cisco.nxos.nxos_bgp_neighbor module – (deprecated, removed after 2023-01-27) Manages BGP neighbors configurations.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_bgp_neighbor`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_bgp_neighbor_module.md#deprecated)
- [Synopsis](nxos_bgp_neighbor_module.md#synopsis)
- [Parameters](nxos_bgp_neighbor_module.md#parameters)
- [Notes](nxos_bgp_neighbor_module.md#notes)
- [Examples](nxos_bgp_neighbor_module.md#examples)
- [Return Values](nxos_bgp_neighbor_module.md#return-values)
- [Status](nxos_bgp_neighbor_module.md#status)

## [DEPRECATED](nxos_bgp_neighbor_module.md#id1)

Removed in:
:   major release after 2023-01-27

Why:
:   Updated module released with more functionality.

Alternative:
:   nxos_bgp_global

## [Synopsis](nxos_bgp_neighbor_module.md#id2)

- Manages BGP neighbors configurations on NX-OS switches.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_bgp_neighbor_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **asn**  string / required | BGP autonomous system number. Valid values are string, Integer in ASPLAIN or ASDOT notation. |
| **bfd**  string | Enables/Disables BFD for a given neighbor.  Dependency: ‘’feature bfd’’  Choices:   - `"enable"` - `"disable"` |
| **capability_negotiation**  boolean | Configure whether or not to negotiate capability with this neighbor.  Choices:   - `false` - `true` |
| **connected_check**  boolean | Configure whether or not to check for directly connected peer.  Choices:   - `false` - `true` |
| **description**  string | Description of the neighbor. |
| **dynamic_capability**  boolean | Configure whether or not to enable dynamic capability.  Choices:   - `false` - `true` |
| **ebgp_multihop**  string | Specify multihop TTL for a remote peer. Valid values are integers between 2 and 255, or keyword ‘default’ to disable this property. |
| **local_as**  string | Specify the local-as number for the eBGP neighbor. Valid values are String or Integer in ASPLAIN or ASDOT notation, or ‘default’, which means not to configure it. |
| **log_neighbor_changes**  string | Specify whether or not to enable log messages for neighbor up/down event.  Choices:   - `"enable"` - `"disable"` - `"inherit"` |
| **low_memory_exempt**  boolean | Specify whether or not to shut down this neighbor under memory pressure.  Choices:   - `false` - `true` |
| **maximum_peers**  string | Specify Maximum number of peers for this neighbor prefix Valid values are between 1 and 1000, or ‘default’, which does not impose the limit. Note that this parameter is accepted only on neighbors with address/prefix. |
| **neighbor**  string / required | Neighbor Identifier. Valid values are string. Neighbors may use IPv4 or IPv6 notation, with or without prefix length. |
| **peer_type**  string  added in cisco.nxos 1.1.0 | Specify the peer type for BGP session.  Choices:   - `"fabric_border_leaf"` - `"fabric_external"` - `"disable"` |
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
| **pwd**  string | Specify the password for neighbor. Valid value is string. |
| **pwd_type**  string | Specify the encryption type the password will use. Valid values are ‘3des’ or ‘cisco_type_7’ encryption or keyword ‘default’.  Choices:   - `"3des"` - `"cisco_type_7"` - `"default"` |
| **remote_as**  string | Specify Autonomous System Number of the neighbor. Valid values are String or Integer in ASPLAIN or ASDOT notation, or ‘default’, which means not to configure it. |
| **remove_private_as**  string | Specify the config to remove private AS number from outbound updates. Valid values are ‘enable’ to enable this config, ‘disable’ to disable this config, ‘all’ to remove all private AS number, or ‘replace-as’, to replace the private AS number.  Choices:   - `"enable"` - `"disable"` - `"all"` - `"replace-as"` |
| **shutdown**  boolean | Configure to administratively shutdown this neighbor.  Choices:   - `false` - `true` |
| **state**  string | Determines whether the config should be present or not on the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **suppress_4_byte_as**  boolean | Configure to suppress 4-byte AS Capability.  Choices:   - `false` - `true` |
| **timers_holdtime**  string | Specify holdtime timer value. Valid values are integers between 0 and 3600 in terms of seconds, or ‘default’, which is 180. |
| **timers_keepalive**  string | Specify keepalive timer value. Valid values are integers between 0 and 3600 in terms of seconds, or ‘default’, which is 60. |
| **transport_passive_only**  boolean | Specify whether or not to only allow passive connection setup. Valid values are ‘true’, ‘false’, and ‘default’, which defaults to ‘false’. This property can only be configured when the neighbor is in ‘ip’ address format without prefix length.  Choices:   - `false` - `true` |
| **update_source**  string | Specify source interface of BGP session and updates. |
| **vrf**  string | Name of the VRF. The name ‘default’ is a valid VRF representing the global bgp.  Default: `"default"` |

## [Notes](nxos_bgp_neighbor_module.md#id4)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - `state=absent` removes the whole BGP neighbor configuration.
> - Default, where supported, restores params default value.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_bgp_neighbor_module.md#id5)

```yaml+jinja
# create a new neighbor
- cisco.nxos.nxos_bgp_neighbor:
    asn: 65535
    neighbor: 192.0.2.3
    local_as: 20
    remote_as: 30
    bfd: enable
    description: just a description
    update_source: Ethernet1/3
    state: present
    peer_type: fabric_external
```

## [Return Values](nxos_bgp_neighbor_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  Returned: always  Sample: `["router bgp 65535", "neighbor 192.0.2.3", "remote-as 30", "update-source Ethernet1/3", "description just a description", "local-as 20", "peer-type fabric-external"]` |

## [Status](nxos_bgp_neighbor_module.md#id7)

- This module will be removed in a major release after 2023-01-27.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_bgp_neighbor_module.md#deprecated).

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
