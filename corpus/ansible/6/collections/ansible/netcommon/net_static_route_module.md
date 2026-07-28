---
collection: ansible
version: "6"
title: "ansible.netcommon.net_static_route module – (deprecated, removed after 2022-06-01) Manage static IP routes on network appliances (routers, switches et. al.)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_static_route_module.html
fetched_at: 2026-07-27T16:44:32+00:00
---
# ansible.netcommon.net_static_route module – (deprecated, removed after 2022-06-01) Manage static IP routes on network appliances (routers, switches et. al.)

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.net_static_route`.

New in ansible.netcommon 1.0.0

- [DEPRECATED](net_static_route_module.md#deprecated)
- [Synopsis](net_static_route_module.md#synopsis)
- [Parameters](net_static_route_module.md#parameters)
- [Notes](net_static_route_module.md#notes)
- [Examples](net_static_route_module.md#examples)
- [Return Values](net_static_route_module.md#return-values)
- [Status](net_static_route_module.md#status)

## [DEPRECATED](net_static_route_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use platform-specific “[netos]_static_route” module

## [Synopsis](net_static_route_module.md#id2)

- This module provides declarative management of static IP routes on network appliances (routers, switches et. al.).

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](net_static_route_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin_distance**  string | Admin distance of the static route. |
| **aggregate**  string | List of static route definitions |
| **mask**  string / required | Network prefix mask of the static route. |
| **next_hop**  string / required | Next hop IP of the static route. |
| **prefix**  string / required | Network prefix of the static route. |
| **purge**  string | Purge static routes not defined in the *aggregate* parameter.  Default: `false` |
| **state**  string | State of the static route configuration.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](net_static_route_module.md#id4)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_static_route_module.md#id5)

```yaml+jinja
- name: configure static route
  ansible.netcommon.net_static_route:
    prefix: 192.168.2.0
    mask: 255.255.255.0
    next_hop: 10.0.0.1

- name: remove configuration
  ansible.netcommon.net_static_route:
    prefix: 192.168.2.0
    mask: 255.255.255.0
    next_hop: 10.0.0.1
    state: absent

- name: configure aggregates of static routes
  ansible.netcommon.net_static_route:
    aggregate:
    - {prefix: 192.168.2.0, mask: 255.255.255.0, next_hop: 10.0.0.1}
    - {prefix: 192.168.3.0, mask: 255.255.255.0, next_hop: 10.0.2.1}

- name: Remove static route collections
  ansible.netcommon.net_static_route:
    aggregate:
    - {prefix: 172.24.1.0/24, next_hop: 192.168.42.64}
    - {prefix: 172.24.3.0/24, next_hop: 192.168.42.64}
    state: absent
```

## [Return Values](net_static_route_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["ip route 192.168.2.0/24 10.0.0.1"]` |

## [Status](net_static_route_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](net_static_route_module.md#deprecated).

### Authors

- Ricardo Carrillo Cruz (@rcarrillocruz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
