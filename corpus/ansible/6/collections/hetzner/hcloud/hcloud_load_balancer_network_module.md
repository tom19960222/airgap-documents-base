---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_load_balancer_network module – Manage the relationship between Hetzner Cloud Networks and Load Balancers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_load_balancer_network_module.html
fetched_at: 2026-07-27T17:49:42+00:00
---
# hetzner.hcloud.hcloud_load_balancer_network module – Manage the relationship between Hetzner Cloud Networks and Load Balancers

> **Note:**
>
> This module is part of the [hetzner.hcloud collection](https://galaxy.ansible.com/hetzner/hcloud) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install hetzner.hcloud`.
> You need further requirements to be able to use this module,
> see [Requirements](hcloud_load_balancer_network_module.md#ansible-collections-hetzner-hcloud-hcloud-load-balancer-network-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_load_balancer_network`.

New in hetzner.hcloud 0.1.0

- [Synopsis](hcloud_load_balancer_network_module.md#synopsis)
- [Requirements](hcloud_load_balancer_network_module.md#requirements)
- [Parameters](hcloud_load_balancer_network_module.md#parameters)
- [See Also](hcloud_load_balancer_network_module.md#see-also)
- [Examples](hcloud_load_balancer_network_module.md#examples)
- [Return Values](hcloud_load_balancer_network_module.md#return-values)

## [Synopsis](hcloud_load_balancer_network_module.md#id1)

- Create and delete the relationship Hetzner Cloud Networks and Load Balancers

## [Requirements](hcloud_load_balancer_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0
- hcloud-python >= 1.8.1

## [Parameters](hcloud_load_balancer_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **ip**  string | The IP the Load Balancer should have. |
| **load_balancer**  string / required | The name of the Hetzner Cloud Load Balancer. |
| **network**  string / required | The name of the Hetzner Cloud Networks. |
| **state**  string | State of the load_balancer_network.  Choices:   - `"absent"` - `"present"` ← (default) |

## [See Also](hcloud_load_balancer_network_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_load_balancer_network_module.md#id5)

```yaml+jinja
- name: Create a basic Load Balancer network
  hcloud_load_balancer_network:
    network: my-network
    load_balancer: my-LoadBalancer
    state: present

- name: Create a Load Balancer network and specify the ip address
  hcloud_load_balancer_network:
    network: my-network
    load_balancer: my-LoadBalancer
    ip: 10.0.0.1
    state: present

- name: Ensure the Load Balancer network is absent (remove if needed)
  hcloud_load_balancer_network:
    network: my-network
    load_balancer: my-LoadBalancer
    state: absent
```

## [Return Values](hcloud_load_balancer_network_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_load_balancer_network**  complex | The relationship between a Load Balancer and a network  Returned: always |
| **ip**  string | IP of the Load Balancer within the Network ip range  Returned: always  Sample: `"10.0.0.8"` |
| **load_balancer**  string | Name of the Load Balancer  Returned: always  Sample: `"my-LoadBalancer"` |
| **network**  string | Name of the Network  Returned: always  Sample: `"my-network"` |

### Authors

- Lukas Kaemmerling (@lkaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
