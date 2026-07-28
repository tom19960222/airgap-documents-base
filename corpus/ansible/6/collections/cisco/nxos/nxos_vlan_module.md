---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_vlan module – (deprecated, removed after 2022-06-01) Manages VLAN resources and attributes."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_vlan_module.html
fetched_at: 2026-07-27T17:02:31+00:00
---
# cisco.nxos.nxos_vlan module – (deprecated, removed after 2022-06-01) Manages VLAN resources and attributes.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_vlan`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_vlan_module.md#deprecated)
- [Synopsis](nxos_vlan_module.md#synopsis)
- [Parameters](nxos_vlan_module.md#parameters)
- [Notes](nxos_vlan_module.md#notes)
- [Examples](nxos_vlan_module.md#examples)
- [Return Values](nxos_vlan_module.md#return-values)
- [Status](nxos_vlan_module.md#status)

## [DEPRECATED](nxos_vlan_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   nxos_vlans

## [Synopsis](nxos_vlan_module.md#id2)

- Manages VLAN configurations on NX-OS switches.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_vlan_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_state**  string | Manage the VLAN administrative state of the VLAN equivalent to shut/no shut in VLAN config mode.  Choices:   - `"up"` ← (default) - `"down"` |
| **aggregate**  list / elements=dictionary | List of VLANs definitions. |
| **admin_state**  string | Manage the VLAN administrative state of the VLAN equivalent to shut/no shut in VLAN config mode.  Choices:   - `"up"` - `"down"` |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vlan `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vlan interfaces on device it will result in failure. |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state arguments. |
| **interfaces**  list / elements=string | List of interfaces that should be associated to the VLAN or keyword ‘default’. |
| **mapped_vni**  string | The Virtual Network Identifier (VNI) ID that is mapped to the VLAN. Valid values are integer and keyword ‘default’. Range 4096-16773119. |
| **mode**  string | Set VLAN mode to classical ethernet or fabricpath. This is a valid option for Nexus 5000 and 7000 series.  Choices:   - `"ce"` - `"fabricpath"` |
| **name**  string | Name of VLAN or keyword ‘default’. |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` - `"absent"` |
| **vlan_id**  integer / required | Single VLAN ID. |
| **vlan_range**  string | Range of VLANs such as 2-10 or 2,5,10-15, etc. |
| **vlan_state**  string | Manage the vlan operational state of the VLAN  Choices:   - `"active"` - `"suspend"` |
| **associated_interfaces**  list / elements=string | This is a intent option and checks the operational state of the for given vlan `name` for associated interfaces. If the value in the `associated_interfaces` does not match with the operational state of vlan interfaces on device it will result in failure. |
| **delay**  integer | Time in seconds to wait before checking for the operational state on remote device. This wait is applicable for operational state arguments.  Default: `10` |
| **interfaces**  list / elements=string | List of interfaces that should be associated to the VLAN or keyword ‘default’. |
| **mapped_vni**  string | The Virtual Network Identifier (VNI) ID that is mapped to the VLAN. Valid values are integer and keyword ‘default’. Range 4096-16773119. |
| **mode**  string | Set VLAN mode to classical ethernet or fabricpath. This is a valid option for Nexus 5000 and 7000 series.  Choices:   - `"ce"` ← (default) - `"fabricpath"` |
| **name**  string | Name of VLAN or keyword ‘default’. |
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
| **purge**  boolean | Purge VLANs not defined in the *aggregate* parameter. This parameter can be used without aggregate as well.  Removal of Vlan 1 is not allowed and will be ignored by purge.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Manage the state of the resource.  Choices:   - `"present"` ← (default) - `"absent"` |
| **vlan_id**  integer | Single VLAN ID. |
| **vlan_range**  string | Range of VLANs such as 2-10 or 2,5,10-15, etc. |
| **vlan_state**  string | Manage the vlan operational state of the VLAN  Choices:   - `"active"` ← (default) - `"suspend"` |

## [Notes](nxos_vlan_module.md#id4)

> **Note:**
>
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_vlan_module.md#id5)

```yaml+jinja
- name: Ensure a range of VLANs are not present on the switch
  cisco.nxos.nxos_vlan:
    vlan_range: 2-10,20,50,55-60,100-150
    state: absent

- name: Ensure VLAN 50 exists with the name WEB and is in the shutdown state
  cisco.nxos.nxos_vlan:
    vlan_id: 50
    admin_state: down
    name: WEB

- name: Ensure VLAN is NOT on the device
  cisco.nxos.nxos_vlan:
    vlan_id: 50
    state: absent

- name: Add interfaces to VLAN and check intent (config + intent)
  cisco.nxos.nxos_vlan:
    vlan_id: 100
    interfaces:
    - Ethernet2/1
    - Ethernet2/5
    associated_interfaces:
    - Ethernet2/1
    - Ethernet2/5

- name: Check interfaces assigned to VLAN
  cisco.nxos.nxos_vlan:
    vlan_id: 100
    associated_interfaces:
    - Ethernet2/1
    - Ethernet2/5

- name: Create aggregate of vlans
  cisco.nxos.nxos_vlan:
    aggregate:
    - {vlan_id: 4000, mode: ce}
    - {vlan_id: 4001, name: vlan-4001}

- name: purge vlans - removes all other vlans except the ones mentioned in aggregate)
  cisco.nxos.nxos_vlan:
    aggregate:
    - vlan_id: 1
    - vlan_id: 4001
    purge: yes
```

## [Return Values](nxos_vlan_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | Set of command strings to send to the remote device  Returned: always  Sample: `["vlan 20", "vlan 55", "vn-segment 5000"]` |

## [Status](nxos_vlan_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_vlan_module.md#deprecated).

### Authors

- Jason Edelman (@jedelman8)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
