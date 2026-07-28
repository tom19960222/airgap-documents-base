---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_linkagg module – (deprecated, removed after 2022-06-01) Manage link aggregation groups on VyOS network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_linkagg_module.html
fetched_at: 2026-07-28T00:23:21+00:00
---
# vyos.vyos.vyos_linkagg module – (deprecated, removed after 2022-06-01) Manage link aggregation groups on VyOS network devices

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/vyos/vyos) (version 3.0.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_linkagg`.

New in vyos.vyos 1.0.0

- [DEPRECATED](vyos_linkagg_module.md#deprecated)
- [Synopsis](vyos_linkagg_module.md#synopsis)
- [Parameters](vyos_linkagg_module.md#parameters)
- [Notes](vyos_linkagg_module.md#notes)
- [Examples](vyos_linkagg_module.md#examples)
- [Return Values](vyos_linkagg_module.md#return-values)
- [Status](vyos_linkagg_module.md#status)

## [DEPRECATED](vyos_linkagg_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality.

Alternative:
:   vyos_lag_interfaces

## [Synopsis](vyos_linkagg_module.md#id2)

- This module provides declarative management of link aggregation groups on VyOS network devices.

## [Parameters](vyos_linkagg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  list / elements=dictionary | List of link aggregation definitions. |
| **members**  list / elements=string | List of members of the link aggregation group. |
| **mode**  string | Mode of the link aggregation group.  Choices:   - `"802.3ad"` - `"active-backup"` - `"broadcast"` - `"round-robin"` - `"transmit-load-balance"` - `"adaptive-load-balance"` - `"xor-hash"` - `"on"` |
| **name**  string / required | Name of the link aggregation group. |
| **state**  string | State of the link aggregation group.  Choices:   - `"present"` - `"absent"` - `"up"` - `"down"` |
| **members**  list / elements=string | List of members of the link aggregation group. |
| **mode**  string | Mode of the link aggregation group.  Choices:   - `"802.3ad"` ← (default) - `"active-backup"` - `"broadcast"` - `"round-robin"` - `"transmit-load-balance"` - `"adaptive-load-balance"` - `"xor-hash"` - `"on"` |
| **name**  string | Name of the link aggregation group. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **state**  string | State of the link aggregation group.  Choices:   - `"present"` ← (default) - `"absent"` - `"up"` - `"down"` |

## [Notes](vyos_linkagg_module.md#id4)

> **Note:**
>
> - Tested against VYOS 1.1.7
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_linkagg_module.md#id5)

```yaml+jinja
- name: configure link aggregation group
  vyos.vyos.vyos_linkagg:
    name: bond0
    members:
    - eth0
    - eth1

- name: remove configuration
  vyos.vyos.vyos_linkagg:
    name: bond0
    state: absent

- name: Create aggregate of linkagg definitions
  vyos.vyos.vyos_linkagg:
    aggregate:
    - {name: bond0, members: [eth1]}
    - {name: bond1, members: [eth2]}

- name: Remove aggregate of linkagg definitions
  vyos.vyos.vyos_linkagg:
    aggregate:
    - name: bond0
    - name: bond1
    state: absent
```

## [Return Values](vyos_linkagg_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always, except for the platforms that use Netconf transport to manage the device.  Sample: `["set interfaces bonding bond0", "set interfaces ethernet eth0 bond-group 'bond0'", "set interfaces ethernet eth1 bond-group 'bond0'"]` |

## [Status](vyos_linkagg_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](vyos_linkagg_module.md#deprecated).

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
