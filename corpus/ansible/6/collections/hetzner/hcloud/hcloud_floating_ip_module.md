---
collection: ansible
version: "6"
title: "hetzner.hcloud.hcloud_floating_ip module – Create and manage cloud Floating IPs on the Hetzner Cloud."
source_url: https://docs.ansible.com/projects/ansible/6/collections/hetzner/hcloud/hcloud_floating_ip_module.html
fetched_at: 2026-07-27T17:49:39+00:00
---
# hetzner.hcloud.hcloud_floating_ip module – Create and manage cloud Floating IPs on the Hetzner Cloud.

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
> see [Requirements](hcloud_floating_ip_module.md#ansible-collections-hetzner-hcloud-hcloud-floating-ip-module-requirements) for details.
>
> To use it in a playbook, specify: `hetzner.hcloud.hcloud_floating_ip`.

New in hetzner.hcloud 0.1.0

- [Synopsis](hcloud_floating_ip_module.md#synopsis)
- [Requirements](hcloud_floating_ip_module.md#requirements)
- [Parameters](hcloud_floating_ip_module.md#parameters)
- [See Also](hcloud_floating_ip_module.md#see-also)
- [Examples](hcloud_floating_ip_module.md#examples)
- [Return Values](hcloud_floating_ip_module.md#return-values)

## [Synopsis](hcloud_floating_ip_module.md#id1)

- Create, update and manage cloud Floating IPs on the Hetzner Cloud.

## [Requirements](hcloud_floating_ip_module.md#id2)

The below requirements are needed on the host that executes this module.

- hcloud-python >= 1.0.0
- hcloud-python >= 1.6.0

## [Parameters](hcloud_floating_ip_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string / required | This is the API Token for the Hetzner Cloud.  You can also set this option by using the environment variable HCLOUD_TOKEN |
| **delete_protection**  boolean | Protect the Floating IP for deletion.  Choices:   - `false` - `true` |
| **description**  string | The Description of the Hetzner Cloud Floating IPs. |
| **endpoint**  string | This is the API Endpoint for the Hetzner Cloud.  Default: `"https://api.hetzner.cloud/v1"` |
| **force**  boolean | Force the assignment or deletion of the Floating IP.  Choices:   - `false` - `true` |
| **home_location**  string | Home Location of the Hetzner Cloud Floating IP.  Required if no *server* is given and Floating IP does not exist. |
| **id**  integer | The ID of the Hetzner Cloud Floating IPs to manage.  Only required if no Floating IP *name* is given. |
| **labels**  dictionary | User-defined labels (key-value pairs). |
| **name**  string | The Name of the Hetzner Cloud Floating IPs to manage.  Only required if no Floating IP *id* is given or a Floating IP does not exist. |
| **server**  string | Server Name the Floating IP should be assigned to.  Required if no *home_location* is given and Floating IP does not exist. |
| **state**  string | State of the Floating IP.  Choices:   - `"absent"` - `"present"` ← (default) |
| **type**  string | Type of the Floating IP.  Required if Floating IP does not exist  Choices:   - `"ipv4"` - `"ipv6"` |

## [See Also](hcloud_floating_ip_module.md#id4)

> **See also:**
>
> [Documentation for Hetzner Cloud API](https://docs.hetzner.cloud/)
> :   Complete reference for the Hetzner Cloud API.

## [Examples](hcloud_floating_ip_module.md#id5)

```yaml+jinja
- name: Create a basic IPv4 Floating IP
  hcloud_floating_ip:
    name: my-floating-ip
    home_location: fsn1
    type: ipv4
    state: present
- name: Create a basic IPv6 Floating IP
  hcloud_floating_ip:
    name: my-floating-ip
    home_location: fsn1
    type: ipv6
    state: present
- name: Assign a Floating IP to a server
  hcloud_floating_ip:
    name: my-floating-ip
    server: 1234
    state: present
- name: Assign a Floating IP to another server
  hcloud_floating_ip:
    name: my-floating-ip
    server: 1234
    force: yes
    state: present
- name: Floating IP should be absent
  hcloud_floating_ip:
    name: my-floating-ip
    state: absent
```

## [Return Values](hcloud_floating_ip_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **hcloud_floating_ip**  complex | The Floating IP instance  Returned: Always |
| **delete_protection**  boolean  added in hetzner.hcloud 0.1.0 | True if Floating IP is protected for deletion  Returned: always  Sample: `false` |
| **description**  string | Description of the Floating IP  Returned: Always  Sample: `"my-floating-ip"` |
| **home_location**  string | Name of the home location of the Floating IP  Returned: Always  Sample: `"fsn1"` |
| **id**  integer | ID of the Floating IP  Returned: Always  Sample: `12345` |
| **ip**  string | IP Address of the Floating IP  Returned: Always  Sample: `"116.203.104.109"` |
| **labels**  dictionary | User-defined labels (key-value pairs)  Returned: Always  Sample: `{"key": "value", "mylabel": 123}` |
| **name**  string | Name of the Floating IP  Returned: Always  Sample: `"my-floating-ip"` |
| **server**  string | Name of the server the Floating IP is assigned to.  Returned: Always  Sample: `"my-server"` |
| **type**  string | Type of the Floating IP  Returned: Always  Sample: `"ipv4"` |

### Authors

- Lukas Kaemmerling (@lkaemmerling)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/hetzner.hcloud/issues)
[Repository (Sources)](https://github.com/ansible-collections/hetzner.hcloud)
