---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_primary_ip module – Create and manage cloud Primary IPs on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_primary_ip_module.html
fetched_at: 2026-07-27T17:49:48+00:00
---
# hetzner.hcloud.hcloud_primary_ip module – Create and manage cloud Primary IPs on the Hetzner Cloud.

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
> see [Requirements](hcloud_primary_ip_module.md#ansible-collections-hetzner-hcloud-hcloud-primary-ip-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_primary_ip`.

New in hetzner.hcloud 1.8.0

- [Synopsis](hcloud_primary_ip_module.md#synopsis)
- [Requirements](hcloud_primary_ip_module.md#requirements)
- [Parameters](hcloud_primary_ip_module.md#parameters)
- [See Also](hcloud_primary_ip_module.md#see-also)
- [Examples](hcloud_primary_ip_module.md#examples)
- [Return Values](hcloud_primary_ip_module.md#return-values)

## [Synopsis](hcloud_primary_ip_module.md#id1)

- Create, update and manage cloud Primary IPs on the Hetzner Cloud.

## [Requirements](hcloud_primary_ip_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0
- hcloud-python >= 1.9.0

## [Parameters](hcloud_primary_ip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **auto_delete**  boolean | Delete this Primary IP when the resource it is assigned to is deleted  Choices:   - `false` ← (default) - `true` |
| **datacenter**  string | Home Location of the Hetzner Cloud Primary IP.  Required if no *server* is given and Primary IP does not exist. |
| **delete_protection**  boolean | Protect the Primary IP for deletion.  Choices:   - `false` - `true` |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **id**  integer | The ID of the Hetzner Cloud Primary IPs to manage.  Only required if no Primary IP *name* is given. |
| **labels**  dictionary | User-defined labels (key-value pairs). |
| **name**  string | The Name of the Hetzner Cloud Primary IPs to manage.  Only required if no Primary IP *id* is given or a Primary IP does not exist. |
| **state**  string | State of the Primary IP.  Choices:   - `"absent"` - `"present"` ← (default) |
| **type**  string | Type of the Primary IP.  Required if Primary IP does not exist  Choices:   - `"ipv4"` - `"ipv6"` |

## [See Also](hcloud_primary_ip_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_primary_ip_module.md#id5)

```yaml+jinja
- name: Create a basic IPv4 Primary IP
  hcloud_primary_ip:
    name: my-primary-ip
    datacenter: fsn1-dc14
    type: ipv4
    state: present
- name: Create a basic IPv6 Primary IP
  hcloud_primary_ip:
    name: my-primary-ip
    datacenter: fsn1-dc14
    type: ipv6
    state: present
- name: Primary IP should be absent
  hcloud_primary_ip:
    name: my-primary-ip
    state: absent
```

## [Return Values](hcloud_primary_ip_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_primary_ip**  complex | The Primary IP instance  Returned: Always |
| **datacenter**  string | Name of the datacenter of the Primary IP  Returned: Always  Sample: `"fsn1-dc14"` |
| **delete_protection**  boolean | True if Primary IP is protected for deletion  Returned: always  Sample: `false` |
| **id**  integer | ID of the Primary IP  Returned: Always  Sample: `12345` |
| **ip**  string | IP Address of the Primary IP  Returned: Always  Sample: `"116.203.104.109"` |
| **labels**  dictionary | User-defined labels (key-value pairs)  Returned: Always  Sample: `{"key": "value", "mylabel": 123}` |
| **name**  string | Name of the Primary IP  Returned: Always  Sample: `"my-primary-ip"` |
| **type**  string | Type of the Primary IP  Returned: Always  Sample: `"ipv4"` |

### Authors

- Lukas Kaemmerling (@lkaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
