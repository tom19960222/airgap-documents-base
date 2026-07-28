---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_vxlan_vtep_vni module – Creates a Virtual Network Identifier member (VNI)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_vxlan_vtep_vni_module.html
fetched_at: 2026-07-27T17:02:40+00:00
---
# cisco.nxos.nxos_vxlan_vtep_vni module – Creates a Virtual Network Identifier member (VNI)

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
> To use it in a playbook, specify: `cisco.nxos.nxos_vxlan_vtep_vni`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_vxlan_vtep_vni_module.md#synopsis)
- [Parameters](nxos_vxlan_vtep_vni_module.md#parameters)
- [Notes](nxos_vxlan_vtep_vni_module.md#notes)
- [Examples](nxos_vxlan_vtep_vni_module.md#examples)
- [Return Values](nxos_vxlan_vtep_vni_module.md#return-values)

## [Synopsis](nxos_vxlan_vtep_vni_module.md#id1)

- Creates a Virtual Network Identifier member (VNI) for an NVE overlay interface.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_vxlan_vtep_vni_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **assoc_vrf**  boolean | This attribute is used to identify and separate processing VNIs that are associated with a VRF and used for routing. The VRF and VNI specified with this command must match the configuration of the VNI under the VRF.  Choices:   - `false` - `true` |
| **ingress_replication**  string | Specifies mechanism for host reachability advertisement.  Choices:   - `"bgp"` - `"static"` - `"default"` |
| **interface**  string / required | Interface name for the VXLAN Network Virtualization Endpoint. |
| **multicast_group**  string | The multicast group (range) of the VNI. Valid values are string and keyword ‘default’. |
| **multisite_ingress_replication**  string  added in cisco.nxos 1.1.0 | Enables multisite ingress replication.  Choices:   - `"disable"` - `"enable"` - `"optimized"` |
| **peer_list**  list / elements=string | Set the ingress-replication static peer list. Valid values are an array, a space-separated string of ip addresses, or the keyword ‘default’. |
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
| **state**  string | Determines whether the config should be present or not on the device.  Choices:   - `"present"` ← (default) - `"absent"` |
| **suppress_arp**  boolean | Suppress arp under layer 2 VNI.  Choices:   - `false` - `true` |
| **suppress_arp_disable**  boolean | Overrides the global ARP suppression config. This is available on NX-OS 9K series running 9.2.x or higher.  Choices:   - `false` - `true` |
| **vni**  string / required | ID of the Virtual Network Identifier. |

## [Notes](nxos_vxlan_vtep_vni_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - default, where supported, restores params default value.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_vxlan_vtep_vni_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_vxlan_vtep_vni:
    interface: nve1
    vni: 6000
    ingress_replication: default
    multisite_ingress_replication: enable
```

## [Return Values](nxos_vxlan_vtep_vni_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  Returned: always  Sample: `["interface nve1", "member vni 6000", "multisite ingress-replication"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
