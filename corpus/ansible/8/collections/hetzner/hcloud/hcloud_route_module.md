---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_route module – Create and delete cloud routes on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_route_module.html
fetched_at: 2026-07-28T02:34:09+00:00
---
# hetzner.hcloud.hcloud_route module – Create and delete cloud routes on the Hetzner Cloud.

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/ui/repo/published/hetzner/hcloud/) (version 1.16.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_route_module.md#ansible-collections-hetzner-hcloud-hcloud-route-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_route`.

- [Synopsis](hcloud_route_module.md#synopsis)
- [Requirements](hcloud_route_module.md#requirements)
- [Parameters](hcloud_route_module.md#parameters)
- [See Also](hcloud_route_module.md#see-also)
- [Examples](hcloud_route_module.md#examples)
- [Return Values](hcloud_route_module.md#return-values)

## [Synopsis](hcloud_route_module.md#id1)

- Create, update and delete cloud routes on the Hetzner Cloud.

## [Requirements](hcloud_route_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.3.0
- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_route_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **destination**  string / required | Destination network or host of this route. |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **gateway**  string / required | Gateway for the route. |
| **network**  string / required | The name of the Hetzner Cloud Network. |
| **state**  string | State of the route.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [See Also](hcloud_route_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_route_module.md#id5)

```yaml+jinja
- name: Create a basic route
  hcloud_route:
    network: my-network
    destination: 10.100.1.0/24
    gateway: 10.0.1.1
    state: present

- name: Ensure the route is absent
  hcloud_route:
    network: my-network
    destination: 10.100.1.0/24
    gateway: 10.0.1.1
    state: absent
```

## [Return Values](hcloud_route_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_route**  complex | One Route of a Network  **Returned:** always |
| **destination**  string | Destination network or host of this route  **Returned:** always  **Sample:** `"10.0.0.0/8"` |
| **gateway**  string | Gateway of the route  **Returned:** always  **Sample:** `"10.0.0.1"` |
| **network**  string | Name of the Network  **Returned:** always  **Sample:** `"my-network"` |

### Authors

- Lukas Kaemmerling (@lkaemmerling)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
