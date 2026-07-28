---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_subnet module – Manage network subnets in a Pure Storage FlashArray"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_subnet_module.html
fetched_at: 2026-07-28T02:51:29+00:00
---
# purestorage.flasharray.purefa_subnet module – Manage network subnets in a Pure Storage FlashArray

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_subnet_module.md#ansible-collections-purestorage-flasharray-purefa-subnet-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_subnet`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_subnet_module.md#synopsis)
- [Requirements](purefa_subnet_module.md#requirements)
- [Parameters](purefa_subnet_module.md#parameters)
- [Notes](purefa_subnet_module.md#notes)
- [Examples](purefa_subnet_module.md#examples)

## [Synopsis](purefa_subnet_module.md#id1)

- This module manages the network subnets on a Pure Storage FlashArray.

## [Requirements](purefa_subnet_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_subnet_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **enabled**  boolean | whether the subnet should be enabled or not  **Choices:**   - `false` - `true` ← (default) |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **gateway**  string | IPv4 or IPv6 address of subnet gateway. |
| **mtu**  integer | MTU size of the subnet. Range is 568 to 9000.  **Default:** `1500` |
| **name**  string / required | Subnet name. |
| **prefix**  string | Set the IPv4 or IPv6 address to be associated with the subnet. |
| **state**  string | Create or delete subnet.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **vlan**  integer | VLAN ID. Range is 0 to 4094. |

## [Notes](purefa_subnet_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_subnet_module.md#id5)

```yaml+jinja
- name: Create subnet subnet100
  purestorage.flasharray.purefa_subnet:
    name: subnet100
    vlan: 100
    gateway: 10.21.200.1
    prefix: "10.21.200.0/24"
    mtu: 9000
    state: present
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40

- name: Disable subnet subnet100
  purestorage.flasharray.purefa_subnet:
    name: subnet100
    enabled: false
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40

- name: Delete subnet subnet100
  purestorage.flasharray.purefa_subnet:
    name: subnet100
    state: absent
    fa_url: 10.10.10.2
    api_token: c6033033-fe69-2515-a9e8-966bb7fe4b40
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
