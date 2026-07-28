---
collection: ansible
version: "8"
title: "community.network.cnos_static_route module – Manage static IP routes on Lenovo CNOS network devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/cnos_static_route_module.html
fetched_at: 2026-07-28T01:56:19+00:00
---
# community.network.cnos_static_route module – Manage static IP routes on Lenovo CNOS network devices

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.cnos_static_route`.

- [Synopsis](cnos_static_route_module.md#synopsis)
- [Parameters](cnos_static_route_module.md#parameters)
- [Notes](cnos_static_route_module.md#notes)
- [Examples](cnos_static_route_module.md#examples)
- [Return Values](cnos_static_route_module.md#return-values)

## [Synopsis](cnos_static_route_module.md#id1)

- This module provides declarative management of static IP routes on Lenovo CNOS network devices.

Aliases: network.cnos.cnos_static_route

## [Parameters](cnos_static_route_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin_distance**  string | Admin distance of the static route.  **Default:** `1` |
| **aggregate**  string | List of static route definitions. |
| **description**  aliases: description  string | Name of the static route |
| **interface**  string | Interface of the static route. |
| **mask**  string | Network prefix mask of the static route. |
| **next_hop**  string | Next hop IP of the static route. |
| **prefix**  string | Network prefix of the static route. |
| **state**  string | State of the static route configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **tag**  string | Set tag of the static route. |

## [Notes](cnos_static_route_module.md#id3)

> **Note:**
>
> - Tested against CNOS 10.10.1

## [Examples](cnos_static_route_module.md#id4)

```yaml+jinja
- name: Configure static route
  community.network.cnos_static_route:
    prefix: 10.241.107.0
    mask: 255.255.255.0
    next_hop: 10.241.106.1

- name: Configure ultimate route with name and tag
  community.network.cnos_static_route:
    prefix: 10.241.107.0
    mask: 255.255.255.0
    interface: Ethernet1/13
    description: hello world
    tag: 100

- name: Remove configuration
  community.network.cnos_static_route:
    prefix: 10.241.107.0
    mask: 255.255.255.0
    next_hop: 10.241.106.0
    state: absent

- name: Add static route aggregates
  community.network.cnos_static_route:
    aggregate:
      - { prefix: 10.241.107.0, mask: 255.255.255.0, next_hop: 10.241.105.0 }
      - { prefix: 10.241.106.0, mask: 255.255.255.0, next_hop: 10.241.104.0 }

- name: Remove static route aggregates
  community.network.cnos_static_route:
    aggregate:
      - { prefix: 10.241.107.0, mask: 255.255.255.0, next_hop: 10.241.105.0 }
      - { prefix: 10.241.106.0, mask: 255.255.255.0, next_hop: 10.241.104.0 }
    state: absent
```

## [Return Values](cnos_static_route_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["ip route 10.241.107.0 255.255.255.0 10.241.106.0"]` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
