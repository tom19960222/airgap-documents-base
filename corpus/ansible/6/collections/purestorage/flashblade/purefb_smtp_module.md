---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_smtp module – Configure SMTP for Pure Storage FlashBlade"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_smtp_module.html
fetched_at: 2026-07-28T00:18:59+00:00
---
# purestorage.flashblade.purefb_smtp module – Configure SMTP for Pure Storage FlashBlade

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
> see [Requirements](purefb_smtp_module.md#ansible-collections-purestorage-flashblade-purefb-smtp-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_smtp`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_smtp_module.md#synopsis)
- [Requirements](purefb_smtp_module.md#requirements)
- [Parameters](purefb_smtp_module.md#parameters)
- [Notes](purefb_smtp_module.md#notes)
- [Examples](purefb_smtp_module.md#examples)

## [Synopsis](purefb_smtp_module.md#id1)

- Configure SMTP for a Pure Storage FlashBlade.
- Whilst there can be no relay host, a sender domain must be configured.

## [Requirements](purefb_smtp_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_smtp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **domain**  string / required | Domain name for alert messages |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **host**  string | Relay server name |

## [Notes](purefb_smtp_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_smtp_module.md#id5)

```yaml+jinja
- name: Configure SMTP settings
  purestorage.flashblade.purefb_smtp:
    host: hostname
    domain: xyz.com
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
