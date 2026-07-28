---
collection: ansible
version: "8"
title: "community.network.icx_static_route module – Manage static IP routes on Ruckus ICX 7000 series switches"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/icx_static_route_module.html
fetched_at: 2026-07-28T01:56:52+00:00
---
# community.network.icx_static_route module – Manage static IP routes on Ruckus ICX 7000 series switches

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
> To use it in a playbook, specify: `community.network.icx_static_route`.

- [Synopsis](icx_static_route_module.md#synopsis)
- [Parameters](icx_static_route_module.md#parameters)
- [Notes](icx_static_route_module.md#notes)
- [Examples](icx_static_route_module.md#examples)
- [Return Values](icx_static_route_module.md#return-values)

## [Synopsis](icx_static_route_module.md#id1)

- This module provides declarative management of static IP routes on Ruckus ICX network devices.

Aliases: network.icx.icx_static_route

## [Parameters](icx_static_route_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **admin_distance**  integer | Admin distance of the static route. Range is 1 to 255. |
| **aggregate**  list / elements=dictionary | List of static route definitions. |
| **admin_distance**  integer | Admin distance of the static route. Range is 1 to 255. |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  **Choices:**   - `false` - `true` |
| **mask**  string | Network prefix mask of the static route. |
| **next_hop**  string | Next hop IP of the static route. |
| **prefix**  string | Network prefix of the static route. |
| **state**  string | State of the static route configuration.  **Choices:**   - `"present"` - `"absent"` |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  **Choices:**   - `false` - `true` ← (default) |
| **mask**  string | Network prefix mask of the static route. |
| **next_hop**  string | Next hop IP of the static route. |
| **prefix**  string | Network prefix of the static route. |
| **purge**  boolean | Purge routes not defined in the *aggregate* parameter.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | State of the static route configuration.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](icx_static_route_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1.
> - For information on using ICX platform, see [the ICX OS Platform Options guide](user_guide/platform_icx.md).

## [Examples](icx_static_route_module.md#id4)

```yaml+jinja
- name: Configure static route
  community.network.icx_static_route:
    prefix: 192.168.2.0/24
    next_hop: 10.0.0.1

- name: Remove configuration
  community.network.icx_static_route:
    prefix: 192.168.2.0
    mask: 255.255.255.0
    next_hop: 10.0.0.1
    state: absent

- name: Add static route aggregates
  community.network.icx_static_route:
    aggregate:
      - { prefix: 172.16.32.0, mask: 255.255.255.0, next_hop: 10.0.0.8 }
      - { prefix: 172.16.33.0, mask: 255.255.255.0, next_hop: 10.0.0.8 }

- name: Remove static route aggregates
  community.network.icx_static_route:
    aggregate:
      - { prefix: 172.16.32.0, mask: 255.255.255.0, next_hop: 10.0.0.8 }
      - { prefix: 172.16.33.0, mask: 255.255.255.0, next_hop: 10.0.0.8 }
    state: absent
```

## [Return Values](icx_static_route_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["ip route 192.168.2.0 255.255.255.0 10.0.0.1"]` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
