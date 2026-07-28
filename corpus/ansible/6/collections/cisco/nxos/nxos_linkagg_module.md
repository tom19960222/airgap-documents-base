---
collection: ansible
version: "6"
title: "cisco.nxos.nxos_linkagg module – (deprecated, removed after 2022-06-01) Manage link aggregation groups on Cisco NXOS devices."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/nxos/nxos_linkagg_module.html
fetched_at: 2026-07-27T17:02:02+00:00
---
# cisco.nxos.nxos_linkagg module – (deprecated, removed after 2022-06-01) Manage link aggregation groups on Cisco NXOS devices.

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
> To use it in a playbook, specify: `cisco.nxos.nxos_linkagg`.

New in cisco.nxos 1.0.0

- [DEPRECATED](nxos_linkagg_module.md#deprecated)
- [Synopsis](nxos_linkagg_module.md#synopsis)
- [Parameters](nxos_linkagg_module.md#parameters)
- [Notes](nxos_linkagg_module.md#notes)
- [Examples](nxos_linkagg_module.md#examples)
- [Return Values](nxos_linkagg_module.md#return-values)
- [Status](nxos_linkagg_module.md#status)

## [DEPRECATED](nxos_linkagg_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality.

Alternative:
:   nxos_lag_interfaces

## [Synopsis](nxos_linkagg_module.md#id2)

- This module provides declarative management of link aggregation groups on Cisco NXOS devices.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](nxos_linkagg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of link aggregation definitions. |
| **force**  boolean | When true it forces link aggregation group members to match what is declared in the members param. This can be used to remove members.  Choices:   - `false` - `true` |
| **group**  string / required | Channel-group number for the port-channel Link aggregation group. |
| **members**  list / elements=string | List of interfaces that will be managed in the link aggregation group. |
| **min_links**  integer | Minimum number of ports required up before bringing up the link aggregation group. |
| **mode**  string | Mode for the link aggregation group.  Choices:   - `"active"` - `"on"` - `"passive"` |
| **state**  string | State of the link aggregation group.  Choices:   - `"present"` - `"absent"` |
| **force**  boolean | When true it forces link aggregation group members to match what is declared in the members param. This can be used to remove members.  Choices:   - `false` ← (default) - `true` |
| **group**  string | Channel-group number for the port-channel Link aggregation group. |
| **members**  list / elements=string | List of interfaces that will be managed in the link aggregation group. |
| **min_links**  integer | Minimum number of ports required up before bringing up the link aggregation group. |
| **mode**  string | Mode for the link aggregation group.  Choices:   - `"active"` - `"on"` ← (default) - `"passive"` |
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
| **purge**  boolean | Purge links not defined in the *aggregate* parameter.  Choices:   - `false` ← (default) - `true` |
| **state**  string | State of the link aggregation group.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](nxos_linkagg_module.md#id4)

> **Note:**
>
> - Tested against NXOSv 7.0(3)I5(1).
> - Unsupported for Cisco MDS
> - `state=absent` removes the portchannel config and interface if it already exists. If members to be removed are not explicitly passed, all existing members (if any), are removed.
> - Members must be a list.
> - LACP needs to be enabled first if active/passive modes are used.
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_linkagg_module.md#id5)

```yaml+jinja
- name: create link aggregation group
  cisco.nxos.nxos_linkagg:
    group: 99
    state: present

- name: delete link aggregation group
  cisco.nxos.nxos_linkagg:
    group: 99
    state: absent

- name: set link aggregation group to members
  cisco.nxos.nxos_linkagg:
    group: 10
    min_links: 3
    mode: active
    members:
    - Ethernet1/2
    - Ethernet1/4

- name: remove link aggregation group from Ethernet1/2
  cisco.nxos.nxos_linkagg:
    group: 10
    min_links: 3
    mode: active
    members:
    - Ethernet1/4

- name: Create aggregate of linkagg definitions
  cisco.nxos.nxos_linkagg:
    aggregate:
    - {group: 3}
    - {group: 100, min_links: 3}

- name: Remove aggregate of linkagg definitions
  cisco.nxos.nxos_linkagg:
    aggregate:
    - {group: 3}
    - {group: 100, min_links: 3}
    state: absent
```

## [Return Values](nxos_linkagg_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["interface port-channel 30", "lacp min-links 5", "interface Ethernet2/1", "channel-group 30 mode active", "no interface port-channel 30"]` |

## [Status](nxos_linkagg_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](nxos_linkagg_module.md#deprecated).

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
