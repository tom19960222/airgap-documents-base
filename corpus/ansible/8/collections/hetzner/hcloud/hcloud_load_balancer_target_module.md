---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_load_balancer_target module – Manage Hetzner Cloud Load Balancer targets"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_load_balancer_target_module.html
fetched_at: 2026-07-28T02:34:03+00:00
---
# hetzner.hcloud.hcloud_load_balancer_target module – Manage Hetzner Cloud Load Balancer targets

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
> see [Requirements](hcloud_load_balancer_target_module.md#ansible-collections-hetzner-hcloud-hcloud-load-balancer-target-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_load_balancer_target`.

New in hetzner.hcloud 0.1.0

- [Synopsis](hcloud_load_balancer_target_module.md#synopsis)
- [Requirements](hcloud_load_balancer_target_module.md#requirements)
- [Parameters](hcloud_load_balancer_target_module.md#parameters)
- [See Also](hcloud_load_balancer_target_module.md#see-also)
- [Examples](hcloud_load_balancer_target_module.md#examples)
- [Return Values](hcloud_load_balancer_target_module.md#return-values)

## [Synopsis](hcloud_load_balancer_target_module.md#id1)

- Create and delete Hetzner Cloud Load Balancer targets

## [Requirements](hcloud_load_balancer_target_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.8.1
- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_load_balancer_target_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **ip**  string | An IP from a Hetzner Dedicated Server, needs to belongs to the same user as the project.  Required if *type* is ip |
| **label_selector**  string | A Label Selector that will be used to determine the targets dynamically  Required if *type* is label_selector |
| **load_balancer**  string / required | The name of the Hetzner Cloud Load Balancer. |
| **server**  string | The name of the Hetzner Cloud Server.  Required if *type* is server |
| **state**  string | State of the load_balancer_network.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **type**  string / required | The type of the target.  **Choices:**   - `"server"` - `"label_selector"` - `"ip"` |
| **use_private_ip**  boolean | Route the traffic over the private IP of the Load Balancer through a Hetzner Cloud Network.  Load Balancer needs to be attached to a network. See hetzner.hcloud.hcloud.hcloud_load_balancer_network  **Choices:**   - `false` ← (default) - `true` |

## [See Also](hcloud_load_balancer_target_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_load_balancer_target_module.md#id5)

```yaml+jinja
- name: Create a server Load Balancer target
  hetzner.hcloud.hcloud_load_balancer_target:
    type: server
    load_balancer: my-LoadBalancer
    server: my-server
    state: present

- name: Create a label_selector Load Balancer target
  hetzner.hcloud.hcloud_load_balancer_target:
    type: label_selector
    load_balancer: my-LoadBalancer
    label_selector: application=backend
    state: present

- name: Create an IP Load Balancer target
  hetzner.hcloud.hcloud_load_balancer_target:
    type: ip
    load_balancer: my-LoadBalancer
    ip: 127.0.0.1
    state: present

- name: Ensure the Load Balancer target is absent (remove if needed)
  hetzner.hcloud.hcloud_load_balancer_target:
    type: server
    load_balancer: my-LoadBalancer
    server: my-server
    state: absent
```

## [Return Values](hcloud_load_balancer_target_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_load_balancer_target**  complex | The relationship between a Load Balancer and a network  **Returned:** always |
| **ip**  string | IP of the dedicated server  **Returned:** if *type* is ip  **Sample:** `"127.0.0.1"` |
| **label_selector**  string | Label Selector  **Returned:** if *type* is label_selector  **Sample:** `"application=backend"` |
| **load_balancer**  string | Name of the Load Balancer  **Returned:** always  **Sample:** `"my-LoadBalancer"` |
| **server**  string | Name of the Server  **Returned:** if *type* is server  **Sample:** `"my-server"` |
| **type**  string | Type of the Load Balancer Target  **Returned:** always  **Sample:** `"server"` |
| **use_private_ip**  boolean | Route the traffic over the private IP of the Load Balancer through a Hetzner Cloud Network.  Load Balancer needs to be attached to a network. See hetzner.hcloud.hcloud.hcloud_load_balancer_network  **Returned:** always  **Sample:** `true` |

### Authors

- Lukas Kaemmerling (@lkaemmerling)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
