---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_load_balancer module – Create and manage cloud Load Balancers on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_load_balancer_module.html
fetched_at: 2026-07-27T17:49:41+00:00
---
# hetzner.hcloud.hcloud_load_balancer module – Create and manage cloud Load Balancers on the Hetzner Cloud.

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
> see [Requirements](hcloud_load_balancer_module.md#ansible-collections-hetzner-hcloud-hcloud-load-balancer-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_load_balancer`.

New in hetzner.hcloud 0.1.0

- [Synopsis](hcloud_load_balancer_module.md#synopsis)
- [Requirements](hcloud_load_balancer_module.md#requirements)
- [Parameters](hcloud_load_balancer_module.md#parameters)
- [See Also](hcloud_load_balancer_module.md#see-also)
- [Examples](hcloud_load_balancer_module.md#examples)
- [Return Values](hcloud_load_balancer_module.md#return-values)

## [Synopsis](hcloud_load_balancer_module.md#id1)

- Create, update and manage cloud Load Balancers on the Hetzner Cloud.

## [Requirements](hcloud_load_balancer_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0
- hcloud-python >= 1.8.0

## [Parameters](hcloud_load_balancer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **delete_protection**  boolean | Protect the Load Balancer for deletion.  Choices:   - `false` - `true` |
| **disable_public_interface**  boolean | Disables the public interface.  Choices:   - `false` ← (default) - `true` |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the Hetzner Cloud Load Balancer to manage.  Only required if no Load Balancer *name* is given |
| **labels**  dictionary | User-defined labels (key-value pairs). |
| **load_balancer_type**  string | The Load Balancer Type of the Hetzner Cloud Load Balancer to manage.  Required if Load Balancer does not exist. |
| **location**  string | Location of Load Balancer.  Required if no *network_zone* is given and Load Balancer does not exist. |
| **name**  string | The Name of the Hetzner Cloud Load Balancer to manage.  Only required if no Load Balancer *id* is given or a Load Balancer does not exist. |
| **network_zone**  string | Network Zone of Load Balancer.  Required of no *location* is given and Load Balancer does not exist. |
| **state**  string | State of the Load Balancer.  Choices:   - `"absent"` - `"present"` ← (default) |

## [See Also](hcloud_load_balancer_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_load_balancer_module.md#id5)

```yaml+jinja
- name: Create a basic Load Balancer
  hcloud_load_balancer:
    name: my-Load Balancer
    load_balancer_type: lb11
    location: fsn1
    state: present

- name: Ensure the Load Balancer is absent (remove if needed)
  hcloud_load_balancer:
    name: my-Load Balancer
    state: absent
```

## [Return Values](hcloud_load_balancer_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_load_balancer**  complex | The Load Balancer instance  Returned: Always |
| **delete_protection**  boolean | True if Load Balancer is protected for deletion  Returned: always  Sample: `false` |
| **disable_public_interface**  boolean | True if Load Balancer public interface is disabled  Returned: always  Sample: `false` |
| **id**  integer | Numeric identifier of the Load Balancer  Returned: always  Sample: `1937415` |
| **ipv4_address**  string | Public IPv4 address of the Load Balancer  Returned: always  Sample: `"116.203.104.109"` |
| **ipv6_address**  string | Public IPv6 address of the Load Balancer  Returned: always  Sample: `"2a01:4f8:1c1c:c140::1"` |
| **labels**  dictionary | User-defined labels (key-value pairs)  Returned: always |
| **load_balancer_type**  string | Name of the Load Balancer type of the Load Balancer  Returned: always  Sample: `"cx11"` |
| **location**  string | Name of the location of the Load Balancer  Returned: always  Sample: `"fsn1"` |
| **name**  string | Name of the Load Balancer  Returned: always  Sample: `"my-Load-Balancer"` |
| **status**  string | Status of the Load Balancer  Returned: always  Sample: `"running"` |

### Authors

- Lukas Kaemmerling (@LKaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
