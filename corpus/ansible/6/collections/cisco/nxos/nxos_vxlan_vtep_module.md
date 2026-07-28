---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_vxlan_vtep module – Manages VXLAN Network Virtualization Endpoint (NVE)."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_vxlan_vtep_module.html
fetched_at: 2026-07-27T17:02:39+00:00
---
# cisco.nxos.nxos_vxlan_vtep module – Manages VXLAN Network Virtualization Endpoint (NVE).

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
> To use it in a playbook, specify: `cisco.nxos.nxos_vxlan_vtep`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_vxlan_vtep_module.md#synopsis)
- [Parameters](nxos_vxlan_vtep_module.md#parameters)
- [Notes](nxos_vxlan_vtep_module.md#notes)
- [Examples](nxos_vxlan_vtep_module.md#examples)
- [Return Values](nxos_vxlan_vtep_module.md#return-values)

## [Synopsis](nxos_vxlan_vtep_module.md#id1)

- Manages VXLAN Network Virtualization Endpoint (NVE) overlay interface that terminates VXLAN tunnels.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_vxlan_vtep_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the NVE interface. |
| **global_ingress_replication_bgp**  boolean | Configures ingress replication protocol as bgp for all VNIs. This is available on Nexus 9000 series switches running NX-OS software release 9.2(x) or higher.  Choices:   - `false` - `true` |
| **global_mcast_group_L2**  string | Global multicast IP prefix for L2 VNIs or the keyword ‘default’. This is available on Nexus 9000 series switches running NX-OS software release 9.2(x) or higher. |
| **global_mcast_group_L3**  string | Global multicast IP prefix for L3 VNIs or the keyword ‘default’. This is available on Nexus 9000 series switches running NX-OS software release 9.2(x) or higher. |
| **global_suppress_arp**  boolean | Enables ARP suppression for all VNIs. This is available on NX-OS 9K series running 9.2.x or higher.  Choices:   - `false` - `true` |
| **host_reachability**  boolean | Specify mechanism for host reachability advertisement. A Boolean value of ‘true’ indicates that BGP will be used for host reachability advertisement. A Boolean value of ‘false’ indicates that no protocol is used for host reachability advertisement. Other host reachability advertisement protocols (e.g. OpenFlow, controller, etc.) are not supported.  Choices:   - `false` - `true` |
| **interface**  string / required | Interface name for the VXLAN Network Virtualization Endpoint. |
| **multisite_border_gateway_interface**  string  added in cisco.nxos 1.1.0 | Specify the loopback interface whose IP address should be used for the NVE Multisite Border-gateway Interface. This is available on specific Nexus 9000 series switches running NX-OS 7.0(3)I7(x) or higher. Specify “default” to remove an existing gateway config. |
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
| **shutdown**  boolean | Administratively shutdown the NVE interface.  Choices:   - `false` - `true` |
| **source_interface**  string | Specify the loopback interface whose IP address should be used for the NVE interface. |
| **source_interface_hold_down_time**  string | Suppresses advertisement of the NVE loopback address until the overlay has converged. |
| **state**  string | Determines whether the config should be present or not on the device.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](nxos_vxlan_vtep_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - The module is used to manage NVE properties, not to create NVE interfaces. Use [cisco.nxos.nxos_interface](nxos_interface_module.md#ansible-collections-cisco-nxos-nxos-interface-module) if you wish to do so.
> - `state=absent` removes the interface.
> - Default, where supported, restores params default value.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_vxlan_vtep_module.md#id4)

```yaml+jinja
- cisco.nxos.nxos_vxlan_vtep:
    interface: nve1
    description: default
    host_reachability: true
    source_interface: Loopback0
    source_interface_hold_down_time: 30
    shutdown: default
    multisite_border_gateway_interface: Loopback0
```

## [Return Values](nxos_vxlan_vtep_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  Returned: always  Sample: `["interface nve1", "source-interface loopback0", "source-interface hold-down-time 30", "description simple description", "shutdown", "host-reachability protocol bgp", "multisite border-gateway interface loopback0"]` |

### Authors

- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
