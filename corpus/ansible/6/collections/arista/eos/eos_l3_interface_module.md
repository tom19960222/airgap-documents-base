---
collection: ansible
version: "6"
title: "arista.eos.eos_l3_interface module – (deprecated, removed after 2022-06-01) Manage L3 interfaces on Arista EOS network devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_l3_interface_module.html
fetched_at: 2026-07-27T16:45:11+00:00
---
# arista.eos.eos_l3_interface module – (deprecated, removed after 2022-06-01) Manage L3 interfaces on Arista EOS network devices.

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/arista/eos) (version 5.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_l3_interface`.

New in arista.eos 1.0.0

- [DEPRECATED](eos_l3_interface_module.md#deprecated)
- [Synopsis](eos_l3_interface_module.md#synopsis)
- [Parameters](eos_l3_interface_module.md#parameters)
- [Notes](eos_l3_interface_module.md#notes)
- [Examples](eos_l3_interface_module.md#examples)
- [Return Values](eos_l3_interface_module.md#return-values)
- [Status](eos_l3_interface_module.md#status)

## [DEPRECATED](eos_l3_interface_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   eos_l3_interfaces

## [Synopsis](eos_l3_interface_module.md#id2)

- This module provides declarative management of L3 interfaces on Arista EOS network devices.

## [Parameters](eos_l3_interface_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of L3 interfaces definitions. Each of the entry in aggregate list should define name of interface `name` and a optional `ipv4` or `ipv6` address. |
| **ipv4**  string | IPv4 address to be set for the L3 interface mentioned in *name* option. The address format is <ipv4 address>/<mask>, the mask is number in range 0-32 eg. 192.168.0.1/24 |
| **ipv6**  string | IPv6 address to be set for the L3 interface mentioned in *name* option. The address format is <ipv6 address>/<mask>, the mask is number in range 0-128 eg. fd5d:12c9:2201:1::1/64 |
| **name**  string / required | Name of the L3 interface to be configured eg. ethernet1 |
| **state**  string | State of the L3 interface configuration. It indicates if the configuration should be present or absent on remote device.  Choices:   - `"present"` - `"absent"` |
| **ipv4**  string | IPv4 address to be set for the L3 interface mentioned in *name* option. The address format is <ipv4 address>/<mask>, the mask is number in range 0-32 eg. 192.168.0.1/24 |
| **ipv6**  string | IPv6 address to be set for the L3 interface mentioned in *name* option. The address format is <ipv6 address>/<mask>, the mask is number in range 0-128 eg. fd5d:12c9:2201:1::1/64 |
| **name**  string | Name of the L3 interface to be configured eg. ethernet1 |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  Starting with Ansible 2.6 we recommend using `connection: httpapi` for eAPI.  This option will be removed in a release after 2022-06-01.  For more information please see the [EOS Platform Options guide](../network/user_guide/platform_eos.md).   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This is a common argument used for either *cli* or *eapi* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. This value applies to either *cli* or *eapi*.  The port value will default to the appropriate transport common port if none is provided in the task (cli=22, http=80, https=443).  Default: `0` |
| **ssh_keyfile**  path | Specifies the SSH keyfile to use to authenticate the connection to the remote device. This argument is only used for *cli* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` ← (default) - `"eapi"` |
| **use_proxy**  boolean | If `no`, the environment variables `http_proxy` and `https_proxy` will be ignored.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | Configures the *transport* to use SSL if set to `yes` only when the `transport=eapi`. If the transport argument is not eapi, this value is ignored.  Choices:   - `false` - `true` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate either the CLI login or the eAPI authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates. If the transport argument is not eapi, this value is ignored.  Choices:   - `false` - `true` ← (default) |
| **state**  string | State of the L3 interface configuration. It indicates if the configuration should be present or absent on remote device.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](eos_l3_interface_module.md#id4)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - For information on using CLI, eAPI and privileged mode see the :ref:`EOS Platform Options guide <eos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Arista EOS devices see the `Arista integration page <<https://www.ansible.com/ansible-arista-networks>>`_.

## [Examples](eos_l3_interface_module.md#id5)

```yaml+jinja
- name: Remove ethernet1 IPv4 and IPv6 address
  arista.eos.eos_l3_interface:
    name: ethernet1
    state: absent

- name: Set ethernet1 IPv4 address
  arista.eos.eos_l3_interface:
    name: ethernet1
    ipv4: 192.168.0.1/24

- name: Set ethernet1 IPv6 address
  arista.eos.eos_l3_interface:
    name: ethernet1
    ipv6: fd5d:12c9:2201:1::1/64

- name: Set interface Vlan1 (SVI) IPv4 address
  arista.eos.eos_l3_interface:
    name: Vlan1
    ipv4: 192.168.0.5/24

- name: Set IP addresses on aggregate
  arista.eos.eos_l3_interface:
    aggregate:
    - name: ethernet1
      ipv4: 192.168.2.10/24
    - name: ethernet1
      ipv4: 192.168.3.10/24
      ipv6: fd5d:12c9:2201:1::1/64

- name: Remove IP addresses on aggregate
  arista.eos.eos_l3_interface:
    aggregate:
    - name: ethernet1
      ipv4: 192.168.2.10/24
    - name: ethernet1
      ipv4: 192.168.3.10/24
      ipv6: fd5d:12c9:2201:1::1/64
    state: absent
```

## [Return Values](eos_l3_interface_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["interface ethernet1", "ip address 192.168.0.1/24", "ipv6 address fd5d:12c9:2201:1::1/64"]` |

## [Status](eos_l3_interface_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](eos_l3_interface_module.md#deprecated).

### Authors

- Ganesh Nalawade (@ganeshrn)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
