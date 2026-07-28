---
collection: ansible
version: "6"
title: "community.windows.win_route module – Add or remove a static route"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_route_module.html
fetched_at: 2026-07-27T17:23:53+00:00
---
# community.windows.win_route module – Add or remove a static route

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_route`.

- [Synopsis](win_route_module.md#synopsis)
- [Parameters](win_route_module.md#parameters)
- [Notes](win_route_module.md#notes)
- [Examples](win_route_module.md#examples)
- [Return Values](win_route_module.md#return-values)

## [Synopsis](win_route_module.md#id1)

- Add or remove a static route.

## [Parameters](win_route_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **destination**  string / required | Destination IP address in CIDR format (ip address/prefix length). |
| **gateway**  string | The gateway used by the static route.  If `gateway` is not provided it will be set to `0.0.0.0`. |
| **metric**  integer | Metric used by the static route.  Default: `1` |
| **state**  string | If `absent`, it removes a network static route.  If `present`, it adds a network static route.  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](win_route_module.md#id3)

> **Note:**
>
> - Works only with Windows 2012 R2 and newer.

## [Examples](win_route_module.md#id4)

```yaml+jinja
---
- name: Add a network static route
  community.windows.win_route:
    destination: 192.168.2.10/32
    gateway: 192.168.1.1
    metric: 1
    state: present

- name: Remove a network static route
  community.windows.win_route:
    destination: 192.168.2.10/32
    state: absent
```

## [Return Values](win_route_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **output**  string | A message describing the task result.  Returned: always  Sample: `"Route added"` |

### Authors

- Daniele Lazzari (@dlazz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
