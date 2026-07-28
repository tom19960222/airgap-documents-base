---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_subnet module – Manage network subnets in a Pure Storage FlashBlade"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_subnet_module.html
fetched_at: 2026-07-28T02:52:21+00:00
---
# purestorage.flashblade.purefb_subnet module – Manage network subnets in a Pure Storage FlashBlade

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flashblade/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_subnet_module.md#ansible-collections-purestorage-flashblade-purefb-subnet-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_subnet`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_subnet_module.md#synopsis)
- [Requirements](purefb_subnet_module.md#requirements)
- [Parameters](purefb_subnet_module.md#parameters)
- [Notes](purefb_subnet_module.md#notes)
- [Examples](purefb_subnet_module.md#examples)

## [Synopsis](purefb_subnet_module.md#id1)

- This module manages network subnets on Pure Storage FlashBlade.

## [Requirements](purefb_subnet_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_subnet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **gateway**  string | IPv4 or IPv6 address of subnet gateway. |
| **lag**  string  *added in purestorage.flashblade 1.7.0* | Name of the Link Aggreation Group to use for the subnet.  **Default:** `"uplink"` |
| **mtu**  integer | MTU size of the subnet. Range is 1280 to 9216.  **Default:** `1500` |
| **name**  string / required | Subnet Name. |
| **prefix**  string | IPv4 or IPv6 address associated with the subnet.  Supply the prefix length (CIDR) as well as the IP address.  Required for subnet creation. |
| **state**  string | Create, delete or modifies a subnet.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vlan**  integer | VLAN ID of the subnet.  **Default:** `0` |

## [Notes](purefb_subnet_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_subnet_module.md#id5)

```yaml+jinja
- name: Create new network subnet named foo
  purestorage.flashblade.purefb_subnet:
    name: foo
    prefix: "10.21.200.3/24"
    gateway: 10.21.200.1
    mtu: 9000
    vlan: 2200
    lag: bar
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Change configuration of existing subnet foo
  purestorage.flashblade.purefb_subnet:
    name: foo
    state: present
    prefix: "10.21.100.3/24"
    gateway: 10.21.100.1
    mtu: 1500
    address: 10.21.200.123
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete network subnet named foo
  purestorage.flashblade.purefb_subnet:
    name: foo
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
