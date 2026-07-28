---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_network module – Manage network interfaces in a Pure Storage FlashBlade"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_network_module.html
fetched_at: 2026-07-28T00:18:53+00:00
---
# purestorage.flashblade.purefb_network module – Manage network interfaces in a Pure Storage FlashBlade

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/purestorage/flashblade) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_network_module.md#ansible-collections-purestorage-flashblade-purefb-network-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_network`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_network_module.md#synopsis)
- [Requirements](purefb_network_module.md#requirements)
- [Parameters](purefb_network_module.md#parameters)
- [Notes](purefb_network_module.md#notes)
- [Examples](purefb_network_module.md#examples)

## [Synopsis](purefb_network_module.md#id1)

- This module manages network interfaces on Pure Storage FlashBlade.
- When creating a network interface a subnet must already exist with a network prefix that covers the IP address of the interface being created.

## [Requirements](purefb_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | IP address of interface. |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **itype**  string | Type of interface.  Choices:   - `"vip"` ← (default) |
| **name**  string / required | Interface Name. |
| **services**  string | Define which services are configured for the interfaces.  Choices:   - `"data"` ← (default) - `"replication"` |
| **state**  string | Create, delete or modifies a network interface.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](purefb_network_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_network_module.md#id5)

```yaml+jinja
- name: Create new network interface named foo
  purestorage.flashblade.purefb_network:
    name: foo
    address: 10.21.200.23
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Change IP address of network interface named foo
  purestorage.flashblade.purefb_network:
    name: foo
    state: present
    address: 10.21.200.123
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete network interface named foo
  purestorage.flashblade.purefb_network:
    name: foo
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
