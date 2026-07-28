---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_network module – Create and manage cloud Networks on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_network_module.html
fetched_at: 2026-07-28T02:34:05+00:00
---
# hetzner.hcloud.hcloud_network module – Create and manage cloud Networks on the Hetzner Cloud.

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
> see [Requirements](hcloud_network_module.md#ansible-collections-hetzner-hcloud-hcloud-network-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_network`.

- [Synopsis](hcloud_network_module.md#synopsis)
- [Requirements](hcloud_network_module.md#requirements)
- [Parameters](hcloud_network_module.md#parameters)
- [See Also](hcloud_network_module.md#see-also)
- [Examples](hcloud_network_module.md#examples)
- [Return Values](hcloud_network_module.md#return-values)

## [Synopsis](hcloud_network_module.md#id1)

- Create, update and manage cloud Networks on the Hetzner Cloud.
- You need at least hcloud-python 1.3.0.

## [Requirements](hcloud_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.3.0
- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **delete_protection**  boolean | Protect the Network for deletion.  **Choices:**   - `false` - `true` |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **expose_routes_to_vswitch**  boolean | Indicates if the routes from this network should be exposed to the vSwitch connection.  The exposing only takes effect if a vSwitch connection is active.  **Choices:**   - `false` - `true` |
| **id**  integer | The ID of the Hetzner Cloud Networks to manage.  Only required if no Network *name* is given. |
| **ip_range**  string | IP range of the Network.  Required if Network does not exist. |
| **labels**  dictionary | User-defined labels (key-value pairs). |
| **name**  string | The Name of the Hetzner Cloud Network to manage.  Only required if no Network *id* is given or a Network does not exist. |
| **state**  string | State of the Network.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [See Also](hcloud_network_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_network_module.md#id5)

```yaml+jinja
- name: Create a basic network
  hcloud_network:
    name: my-network
    ip_range: 10.0.0.0/8
    state: present

- name: Ensure the Network is absent (remove if needed)
  hcloud_network:
    name: my-network
    state: absent
```

## [Return Values](hcloud_network_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_network**  complex | The Network  **Returned:** always |
| **delete_protection**  boolean  *added in hetzner.hcloud 0.1.0* | True if Network is protected for deletion  **Returned:** always  **Sample:** `false` |
| **expose_routes_to_vswitch**  boolean | Indicates if the routes from this network should be exposed to the vSwitch connection.  **Returned:** always  **Sample:** `false` |
| **id**  integer | ID of the Network  **Returned:** always  **Sample:** `12345` |
| **ip_range**  string | IP range of the Network  **Returned:** always  **Sample:** `"10.0.0.0/8"` |
| **labels**  dictionary | User-defined labels (key-value pairs)  **Returned:** always  **Sample:** `{"key": "value", "mylabel": 123}` |
| **name**  string | Name of the Network  **Returned:** always  **Sample:** `"my-volume"` |

### Authors

- Lukas Kaemmerling (@lkaemmerling)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
