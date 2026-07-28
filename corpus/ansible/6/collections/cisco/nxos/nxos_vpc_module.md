---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_vpc module – Manages global VPC configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_vpc_module.html
fetched_at: 2026-07-27T17:02:32+00:00
---
# cisco.nxos.nxos_vpc module – Manages global VPC configuration

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
> To use it in a playbook, specify: `cisco.nxos.nxos_vpc`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_vpc_module.md#synopsis)
- [Parameters](nxos_vpc_module.md#parameters)
- [Notes](nxos_vpc_module.md#notes)
- [Examples](nxos_vpc_module.md#examples)
- [Return Values](nxos_vpc_module.md#return-values)

## [Synopsis](nxos_vpc_module.md#id1)

- Manages global VPC configuration

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_vpc_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auto_recovery**  boolean | Enables/Disables auto recovery on platforms that support disable  timers are not modifiable with this attribute  mutually exclusive with auto_recovery_reload_delay  Choices:   - `false` - `true` |
| **auto_recovery_reload_delay**  string | Manages auto-recovery reload-delay timer in seconds  mutually exclusive with auto_recovery |
| **delay_restore**  string | manages delay restore command and config value in seconds |
| **delay_restore_interface_vlan**  string | manages delay restore interface-vlan command and config value in seconds  not supported on all platforms |
| **delay_restore_orphan_port**  string | manages delay restore orphan-port command and config value in seconds  not supported on all platforms |
| **domain**  string / required | VPC domain |
| **peer_gw**  boolean | Enables/Disables peer gateway  Choices:   - `false` - `true` |
| **pkl_dest**  string | Destination (remote) IP address used for peer keepalive link  pkl_dest is required whenever pkl options are used. |
| **pkl_src**  string | Source IP address used for peer keepalive link |
| **pkl_vrf**  string | VRF used for peer keepalive link  The VRF must exist on the device before using pkl_vrf.  (Note) ‘default’ is an overloaded term: Default vrf context for pkl_vrf is ‘management’; ‘pkl_vrf: default’ refers to the literal ‘default’ rib. |
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
| **role_priority**  string | Role priority for device. Remember lower is better. |
| **state**  string | Manages desired state of the resource  Choices:   - `"present"` ← (default) - `"absent"` |
| **system_priority**  string | System priority device. Remember they must match between peers. |

## [Notes](nxos_vpc_module.md#id3)

> **Note:**
>
> - Tested against NXOSv 7.3.(0)D1(1) on VIRL
> - Unsupported for Cisco MDS
> - The feature vpc must be enabled before this module can be used
> - If not using management vrf, vrf must be globally on the device before using in the pkl config
> - Although source IP isn’t required on the command line it is required when using this module. The PKL VRF must also be configured prior to using this module.
> - Both pkl_src and pkl_dest are needed when changing PKL VRF.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_vpc_module.md#id4)

```yaml+jinja
- name: configure a simple asn
  cisco.nxos.nxos_vpc:
    domain: 100
    role_priority: 1000
    system_priority: 2000
    pkl_dest: 192.168.100.4
    pkl_src: 10.1.100.20
    peer_gw: true
    auto_recovery: true

- name: configure
  cisco.nxos.nxos_vpc:
    domain: 100
    role_priority: 32667
    system_priority: 2000
    peer_gw: true
    pkl_src: 10.1.100.2
    pkl_dest: 192.168.100.4
    auto_recovery: true

- name: Configure VPC with delay restore and existing keepalive VRF
  cisco.nxos.nxos_vpc:
    domain: 10
    role_priority: 28672
    system_priority: 2000
    delay_restore: 180
    peer_gw: true
    pkl_src: 1.1.1.2
    pkl_dest: 1.1.1.1
    pkl_vrf: vpckeepalive
    auto_recovery: true
```

## [Return Values](nxos_vpc_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | commands sent to the device  Returned: always  Sample: `["vpc domain 100", "peer-keepalive destination 192.168.100.4 source 10.1.100.20 vrf management", "auto-recovery", "peer-gateway"]` |

### Authors

- Jason Edelman (@jedelman8)
- Gabriele Gerbino (@GGabriele)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
