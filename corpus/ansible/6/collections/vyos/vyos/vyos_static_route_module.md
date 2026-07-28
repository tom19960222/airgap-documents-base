---
collection: ansible
version: "6"
title: "vyos.vyos.vyos_static_route module – (deprecated, removed after 2022-06-01) Manage static IP routes on Vyatta VyOS network devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/vyos/vyos/vyos_static_route_module.html
fetched_at: 2026-07-28T00:23:32+00:00
---
# vyos.vyos.vyos_static_route module – (deprecated, removed after 2022-06-01) Manage static IP routes on Vyatta VyOS network devices

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
> To use it in a playbook, specify: `vyos.vyos.vyos_static_route`.

New in vyos.vyos 1.0.0

- [DEPRECATED](vyos_static_route_module.md#deprecated)
- [Synopsis](vyos_static_route_module.md#synopsis)
- [Parameters](vyos_static_route_module.md#parameters)
- [Notes](vyos_static_route_module.md#notes)
- [Examples](vyos_static_route_module.md#examples)
- [Return Values](vyos_static_route_module.md#return-values)
- [Status](vyos_static_route_module.md#status)

## [DEPRECATED](vyos_static_route_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality.

Alternative:
:   vyos_static_routes

## [Synopsis](vyos_static_route_module.md#id2)

- This module provides declarative management of static IP routes on Vyatta VyOS network devices.

## [Parameters](vyos_static_route_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_distance**  integer | Admin distance of the static route. |
| **aggregate**  list / elements=dictionary | List of static route definitions |
| **admin_distance**  integer | Admin distance of the static route. |
| **mask**  string | Network prefix mask of the static route. |
| **next_hop**  string | Next hop IP of the static route. |
| **prefix**  string / required | Network prefix of the static route. `mask` param should be ignored if `prefix` is provided with `mask` value `prefix/mask`. |
| **state**  string | State of the static route configuration.  Choices:   - `"present"` - `"absent"` |
| **mask**  string | Network prefix mask of the static route. |
| **next_hop**  string | Next hop IP of the static route. |
| **prefix**  string | Network prefix of the static route. `mask` param should be ignored if `prefix` is provided with `mask` value `prefix/mask`. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **state**  string | State of the static route configuration.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](vyos_static_route_module.md#id4)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_static_route_module.md#id5)

```yaml+jinja
- name: configure static route
  vyos.vyos.vyos_static_route:
    prefix: 192.168.2.0
    mask: 24
    next_hop: 10.0.0.1

- name: configure static route prefix/mask
  vyos.vyos.vyos_static_route:
    prefix: 192.168.2.0/16
    next_hop: 10.0.0.1

- name: remove configuration
  vyos.vyos.vyos_static_route:
    prefix: 192.168.2.0
    mask: 16
    next_hop: 10.0.0.1
    state: absent

- name: configure aggregates of static routes
  vyos.vyos.vyos_static_route:
    aggregate:
    - {prefix: 192.168.2.0, mask: 24, next_hop: 10.0.0.1}
    - {prefix: 192.168.3.0, mask: 16, next_hop: 10.0.2.1}
    - {prefix: 192.168.3.0/16, next_hop: 10.0.2.1}

- name: Remove static route collections
  vyos.vyos.vyos_static_route:
    aggregate:
    - {prefix: 172.24.1.0/24, next_hop: 192.168.42.64}
    - {prefix: 172.24.3.0/24, next_hop: 192.168.42.64}
    state: absent
```

## [Return Values](vyos_static_route_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["set protocols static route 192.168.2.0/16 next-hop 10.0.0.1"]` |

## [Status](vyos_static_route_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](vyos_static_route_module.md#deprecated).

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
[Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
