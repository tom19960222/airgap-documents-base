---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_rdns module – Create and manage reverse DNS entries on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_rdns_module.html
fetched_at: 2026-07-27T17:49:48+00:00
---
# hetzner.hcloud.hcloud_rdns module – Create and manage reverse DNS entries on the Hetzner Cloud.

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
> see [Requirements](hcloud_rdns_module.md#ansible-collections-hetzner-hcloud-hcloud-rdns-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_rdns`.

- [Synopsis](hcloud_rdns_module.md#synopsis)
- [Requirements](hcloud_rdns_module.md#requirements)
- [Parameters](hcloud_rdns_module.md#parameters)
- [See Also](hcloud_rdns_module.md#see-also)
- [Examples](hcloud_rdns_module.md#examples)
- [Return Values](hcloud_rdns_module.md#return-values)

## [Synopsis](hcloud_rdns_module.md#id1)

- Create, update and delete reverse DNS entries on the Hetzner Cloud.

## [Requirements](hcloud_rdns_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0
- hcloud-python >= 1.3.0

## [Parameters](hcloud_rdns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **dns_ptr**  string | The DNS address the *ip_address* should resolve to.  Omit the param to reset the reverse DNS entry to the default value. |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **floating_ip**  string | The name of the Hetzner Cloud Floating IP you want to add the reverse DNS entry to. |
| **ip_address**  string / required | The IP address that should point to *dns_ptr*. |
| **load_balancer**  string | The name of the Hetzner Cloud Load Balancer you want to add the reverse DNS entry to. |
| **primary_ip**  string | The name of the Hetzner Cloud Primary IP you want to add the reverse DNS entry to. |
| **server**  string | The name of the Hetzner Cloud server you want to add the reverse DNS entry to. |
| **state**  string | State of the reverse DNS entry.  Choices:   - `"absent"` - `"present"` ← (default) |

## [See Also](hcloud_rdns_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_rdns_module.md#id5)

```yaml+jinja
- name: Create a reverse DNS entry for a server
  hcloud_rdns:
    server: my-server
    ip_address: 123.123.123.123
    dns_ptr: example.com
    state: present

- name: Create a reverse DNS entry for a Floating IP
  hcloud_rdns:
    floating_ip: my-floating-ip
    ip_address: 123.123.123.123
    dns_ptr: example.com
    state: present

- name: Create a reverse DNS entry for a Primary IP
  hcloud_rdns:
    primary_ip: my-primary-ip
    ip_address: 123.123.123.123
    dns_ptr: example.com
    state: present

- name: Create a reverse DNS entry for a Load Balancer
  hcloud_rdns:
    load_balancer: my-load-balancer
    ip_address: 123.123.123.123
    dns_ptr: example.com
    state: present

- name: Ensure the reverse DNS entry is absent (remove if needed)
  hcloud_rdns:
    server: my-server
    ip_address: 123.123.123.123
    dns_ptr: example.com
    state: absent
```

## [Return Values](hcloud_rdns_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_rdns**  complex | The reverse DNS entry  Returned: always |
| **dns_ptr**  string | The DNS that resolves to the IP  Returned: always  Sample: `"example.com"` |
| **floating_ip**  string | Name of the Floating IP  Returned: always  Sample: `"my-floating-ip"` |
| **ip_address**  string | The IP address that point to the DNS ptr  Returned: always  Sample: `"123.123.123.123"` |
| **load_balancer**  string | Name of the Load Balancer  Returned: always  Sample: `"my-load-balancer"` |
| **primary_ip**  string | Name of the Primary IP  Returned: always  Sample: `"my-primary-ip"` |
| **server**  string | Name of the server  Returned: always  Sample: `"my-server"` |

### Authors

- Lukas Kaemmerling (@lkaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
