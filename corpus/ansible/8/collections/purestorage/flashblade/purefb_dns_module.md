---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_dns module – Configure Pure Storage FlashBlade DNS settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_dns_module.html
fetched_at: 2026-07-28T02:51:54+00:00
---
# purestorage.flashblade.purefb_dns module – Configure Pure Storage FlashBlade DNS settings

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
> see [Requirements](purefb_dns_module.md#ansible-collections-purestorage-flashblade-purefb-dns-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_dns`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_dns_module.md#synopsis)
- [Requirements](purefb_dns_module.md#requirements)
- [Parameters](purefb_dns_module.md#parameters)
- [Notes](purefb_dns_module.md#notes)
- [Examples](purefb_dns_module.md#examples)

## [Synopsis](purefb_dns_module.md#id1)

- Set or erase DNS configuration for Pure Storage FlashBlades.

## [Requirements](purefb_dns_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_dns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **domain**  string | Domain suffix to be appended when perofrming DNS lookups. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **nameservers**  list / elements=string | List of up to 3 unique DNS server IP addresses. These can be IPv4 or IPv6 - No validation is done of the addresses is performed. |
| **search**  list / elements=string | Ordered list of domain names to search  Deprecated option. Will be removed in Collection v1.6.0, There is no replacement for this. |
| **state**  string | Create or delete DNS servers configuration  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefb_dns_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_dns_module.md#id5)

```yaml+jinja
- name: Delete exisitng DNS settings
  purestorage.flashblade.purefb_dns:
    state: absent
    fa_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6

- name: Set DNS settings
  purestorage.flashblade.purefb_dns:
    domain: purestorage.com
    nameservers:
      - 8.8.8.8
      - 8.8.4.4
    search:
      - purestorage.com
      - acme.com
    fa_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
