---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_evpn_vni module – Manages Cisco EVPN VXLAN Network Identifier (VNI)."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_evpn_vni_module.html
fetched_at: 2026-07-27T17:01:46+00:00
---
# cisco.nxos.nxos_evpn_vni module – Manages Cisco EVPN VXLAN Network Identifier (VNI).

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
> To use it in a playbook, specify: `cisco.nxos.nxos_evpn_vni`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_evpn_vni_module.md#synopsis)
- [Parameters](nxos_evpn_vni_module.md#parameters)
- [Notes](nxos_evpn_vni_module.md#notes)
- [Examples](nxos_evpn_vni_module.md#examples)
- [Return Values](nxos_evpn_vni_module.md#return-values)

## [Synopsis](nxos_evpn_vni_module.md#id1)

- Manages Cisco Ethernet Virtual Private Network (EVPN) VXLAN Network Identifier (VNI) configurations of a Nexus device.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_evpn_vni_module.md#id2)

| Parameter | Comments |
| --- | --- |
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
| **route_distinguisher**  string | The VPN Route Distinguisher (RD). The RD is combined with the IPv4 or IPv6 prefix learned by the PE router to create a globally unique address. |
| **route_target_both**  list / elements=string | Enables/Disables route-target settings for both import and export target communities using a single property. |
| **route_target_export**  list / elements=string | Sets the route-target ‘export’ extended communities. |
| **route_target_import**  list / elements=string | Sets the route-target ‘import’ extended communities. |
| **state**  string | Determines whether the config should be present or not on the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vni**  string / required | The EVPN VXLAN Network Identifier. |

## [Notes](nxos_evpn_vni_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - default, where supported, restores params default value.
> - RD override is not permitted. You should set it to the default values first and then reconfigure it.
> - `route_target_both`, `route_target_import` and `route_target_export valid` values are a list of extended communities, (i.e. [‘1.2.3.4:5’, ‘33:55’]) or the keywords ‘auto’ or ‘default’.
> - The `route_target_both` property is discouraged due to the inconsistent behavior of the property across Nexus platforms and image versions. For this reason it is recommended to use explicit `route_target_export` and `route_target_import` properties instead of `route_target_both`.
> - RD valid values are a string in one of the route-distinguisher formats, the keyword ‘auto’, or the keyword ‘default’.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_evpn_vni_module.md#id4)

```yaml+jinja
- name: vni configuration
  cisco.nxos.nxos_evpn_vni:
    vni: 6000
    route_distinguisher: 60:10
    route_target_import:
    - 5000:10
    - 4100:100
    route_target_export: auto
    route_target_both: default
```

## [Return Values](nxos_evpn_vni_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  Returned: always  Sample: `["evpn", "vni 6000 l2", "route-target import 5001:10"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
