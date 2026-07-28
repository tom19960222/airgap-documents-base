---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_subnetwork module – Manage cloud subnetworks on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_subnetwork_module.html
fetched_at: 2026-07-28T02:34:14+00:00
---
# hetzner.hcloud.hcloud_subnetwork module – Manage cloud subnetworks on the Hetzner Cloud.

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
> see [Requirements](hcloud_subnetwork_module.md#ansible-collections-hetzner-hcloud-hcloud-subnetwork-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_subnetwork`.

- [Synopsis](hcloud_subnetwork_module.md#synopsis)
- [Requirements](hcloud_subnetwork_module.md#requirements)
- [Parameters](hcloud_subnetwork_module.md#parameters)
- [See Also](hcloud_subnetwork_module.md#see-also)
- [Examples](hcloud_subnetwork_module.md#examples)
- [Return Values](hcloud_subnetwork_module.md#return-values)

## [Synopsis](hcloud_subnetwork_module.md#id1)

- Create, update and delete cloud subnetworks on the Hetzner Cloud.

## [Requirements](hcloud_subnetwork_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.10.0
- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_subnetwork_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **ip_range**  string / required | IP range of the subnetwork. |
| **network**  string / required | The ID or Name of the Hetzner Cloud Networks. |
| **network_zone**  string / required | Name of network zone. |
| **state**  string | State of the subnetwork.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **type**  string / required | Type of subnetwork.  **Choices:**   - `"server"` - `"cloud"` - `"vswitch"` |
| **vswitch_id**  integer | ID of the vSwitch you want to couple with your Network.  Required if type == vswitch |

## [See Also](hcloud_subnetwork_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_subnetwork_module.md#id5)

```yaml+jinja
- name: Create a basic subnetwork
  hcloud_subnetwork:
    network: my-network
    ip_range: 10.0.0.0/16
    network_zone: eu-central
    type: cloud
    state: present

- name: Create a basic subnetwork
  hcloud_subnetwork:
    network: my-vswitch-network
    ip_range: 10.0.0.0/24
    network_zone: eu-central
    type: vswitch
    vswitch_id: 123
    state: present

- name: Ensure the subnetwork is absent (remove if needed)
  hcloud_subnetwork:
    network: my-network
    ip_range: 10.0.0.0/8
    network_zone: eu-central
    type: cloud
    state: absent
```

## [Return Values](hcloud_subnetwork_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_subnetwork**  complex | One Subnet of a Network  **Returned:** always |
| **gateway**  string | Gateway of the subnetwork  **Returned:** always  **Sample:** `"10.0.0.1"` |
| **ip_range**  string | IP range of the Network  **Returned:** always  **Sample:** `"10.0.0.0/8"` |
| **network**  string | Name of the Network  **Returned:** always  **Sample:** `"my-network"` |
| **network_zone**  string | Name of network zone  **Returned:** always  **Sample:** `"eu-central"` |
| **type**  string | Type of subnetwork  **Returned:** always  **Sample:** `"server"` |
| **vswitch_id**  integer | ID of the vswitch, null if not type vswitch  **Returned:** always  **Sample:** `123` |

### Authors

- Lukas Kaemmerling (@lkaemmerling)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
