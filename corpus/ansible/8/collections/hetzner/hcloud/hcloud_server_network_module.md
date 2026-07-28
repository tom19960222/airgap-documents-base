---
collection: ansible
version: "8"
title: "hetzner.hcloud.hcloud_server_network module – Manage the relationship between Hetzner Cloud Networks and servers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/hetzner/hcloud/hcloud_server_network_module.html
fetched_at: 2026-07-28T02:34:11+00:00
---
# hetzner.hcloud.hcloud_server_network module – Manage the relationship between Hetzner Cloud Networks and servers

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
> see [Requirements](hcloud_server_network_module.md#ansible-collections-hetzner-hcloud-hcloud-server-network-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_server_network`.

- [Synopsis](hcloud_server_network_module.md#synopsis)
- [Requirements](hcloud_server_network_module.md#requirements)
- [Parameters](hcloud_server_network_module.md#parameters)
- [See Also](hcloud_server_network_module.md#see-also)
- [Examples](hcloud_server_network_module.md#examples)
- [Return Values](hcloud_server_network_module.md#return-values)

## [Synopsis](hcloud_server_network_module.md#id1)

- Create and delete the relationship Hetzner Cloud Networks and servers

## [Requirements](hcloud_server_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.3.0
- python-dateutil >= 2.7.5
- requests >=2.20

## [Parameters](hcloud_server_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alias_ips**  list / elements=string | Alias IPs the server has. |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  **Default:** `"https://api.hetzner.cloud/v1"` |
| **ip**  string | The IP the server should have. |
| **network**  string / required | The name of the Hetzner Cloud Networks. |
| **server**  string / required | The name of the Hetzner Cloud server. |
| **state**  string | State of the server_network.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [See Also](hcloud_server_network_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_server_network_module.md#id5)

```yaml+jinja
- name: Create a basic server network
  hcloud_server_network:
    network: my-network
    server: my-server
    state: present

- name: Create a server network and specify the ip address
  hcloud_server_network:
    network: my-network
    server: my-server
    ip: 10.0.0.1
    state: present

- name: Create a server network and add alias ips
  hcloud_server_network:
    network: my-network
    server: my-server
    ip: 10.0.0.1
    alias_ips:
       - 10.1.0.1
       - 10.2.0.1
    state: present

- name: Ensure the server network is absent (remove if needed)
  hcloud_server_network:
    network: my-network
    server: my-server
    state: absent
```

## [Return Values](hcloud_server_network_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_server_network**  complex | The relationship between a server and a network  **Returned:** always |
| **alias_ips**  list / elements=string | Alias IPs of the server within the Network ip range  **Returned:** always  **Sample:** `["10.1.0.1", "..."]` |
| **ip**  string | IP of the server within the Network ip range  **Returned:** always  **Sample:** `"10.0.0.8"` |
| **network**  string | Name of the Network  **Returned:** always  **Sample:** `"my-network"` |
| **server**  string | Name of the server  **Returned:** always  **Sample:** `"my-server"` |

### Authors

- Lukas Kaemmerling (@lkaemmerling)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
- [Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
