---
collection: ansible
version: "6"
title: "arista.eos.eos_vlan module – (deprecated, removed after 2022-06-01) Manage VLANs on Arista EOS network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_vlan_module.html
fetched_at: 2026-07-27T16:45:20+00:00
---
# arista.eos.eos_vlan module – (deprecated, removed after 2022-06-01) Manage VLANs on Arista EOS network devices

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
> To use it in a playbook, specify: `arista.eos.eos_vlan`.

New in arista.eos 1.0.0

- [DEPRECATED](eos_vlan_module.md#deprecated)
- [Synopsis](eos_vlan_module.md#synopsis)
- [Parameters](eos_vlan_module.md#parameters)
- [Notes](eos_vlan_module.md#notes)
- [Examples](eos_vlan_module.md#examples)
- [Return Values](eos_vlan_module.md#return-values)
- [Status](eos_vlan_module.md#status)

## [DEPRECATED](eos_vlan_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   eos_vlans

## [Synopsis](eos_vlan_module.md#id2)

- This module provides declarative management of VLANs on Arista EOS network devices.

## [Parameters](eos_vlan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of VLANs definitions. |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vlan `name` for associated interfaces. The name of interface is case sensitive and should be in expanded format and not abbreviated. If the value in the `associated_interfaces` does not match with the operational state of vlan interfaces on device it will result in failure. |
| **delay**  integer | Delay the play should wait to check for declarative intent params values.  Default: `10` |
| **interfaces**  list / elements=string | List of interfaces that should be associated to the VLAN. The name of interface is case sensitive and should be in expanded format and not abbreviated. |
| **name**  string | Name of the VLAN. |
| **state**  string | State of the VLAN configuration.  Choices:   - `"present"` ← (default) - `"absent"` - `"active"` - `"suspend"` |
| **vlan_id**  integer / required | ID of the VLAN. |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vlan `name` for associated interfaces. The name of interface is case sensitive and should be in expanded format and not abbreviated. If the value in the `associated_interfaces` does not match with the operational state of vlan interfaces on device it will result in failure. |
| **delay**  integer | Delay the play should wait to check for declarative intent params values.  Default: `10` |
| **interfaces**  list / elements=string | List of interfaces that should be associated to the VLAN. The name of interface is case sensitive and should be in expanded format and not abbreviated. |
| **name**  string | Name of the VLAN. |
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
| **purge**  boolean | Purge VLANs not defined in the *aggregate* parameter.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of the VLAN configuration.  Choices:   - `"present"` ← (default) - `"absent"` - `"active"` - `"suspend"` |
| **vlan_id**  integer | ID of the VLAN. |

## [Notes](eos_vlan_module.md#id4)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - For information on using CLI, eAPI and privileged mode see the :ref:`EOS Platform Options guide <eos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Arista EOS devices see the `Arista integration page <<https://www.ansible.com/ansible-arista-networks>>`_.

## [Examples](eos_vlan_module.md#id5)

```yaml+jinja
- name: Create vlan
  arista.eos.eos_vlan:
    vlan_id: 4000
    name: vlan-4000
    state: present

- name: Add interfaces to vlan
  arista.eos.eos_vlan:
    vlan_id: 4000
    state: present
    interfaces:
    - Ethernet1
    - Ethernet2

- name: Check if interfaces is assigned to vlan
  arista.eos.eos_vlan:
    vlan_id: 4000
    associated_interfaces:
    - Ethernet1
    - Ethernet2

- name: Suspend vlan
  arista.eos.eos_vlan:
    vlan_id: 4000
    state: suspend

- name: Unsuspend vlan
  arista.eos.eos_vlan:
    vlan_id: 4000
    state: active

- name: Create aggregate of vlans
  arista.eos.eos_vlan:
    aggregate:
    - vlan_id: 4000
    - {vlan_id: 4001, name: vlan-4001}
```

## [Return Values](eos_vlan_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["vlan 20", "name test-vlan"]` |

## [Status](eos_vlan_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](eos_vlan_module.md#deprecated).

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
