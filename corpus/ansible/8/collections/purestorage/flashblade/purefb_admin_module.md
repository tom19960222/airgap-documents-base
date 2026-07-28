---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_admin module – Configure Pure Storage FlashBlade Global Admin settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_admin_module.html
fetched_at: 2026-07-28T02:51:42+00:00
---
# purestorage.flashblade.purefb_admin module – Configure Pure Storage FlashBlade Global Admin settings

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
> see [Requirements](purefb_admin_module.md#ansible-collections-purestorage-flashblade-purefb-admin-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_admin`.

New in purestorage.flashblade 1.8.0

- [Synopsis](purefb_admin_module.md#synopsis)
- [Requirements](purefb_admin_module.md#requirements)
- [Parameters](purefb_admin_module.md#parameters)
- [Notes](purefb_admin_module.md#notes)
- [Examples](purefb_admin_module.md#examples)

## [Synopsis](purefb_admin_module.md#id1)

- Set global admin settings for the FlashBlade

## [Requirements](purefb_admin_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_admin_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **lockout**  integer | Account lockout duration, in seconds, after max_login exceeded  Range between 1 second and 90 days (7776000 seconds) |
| **max_login**  integer | Maximum number of failed logins before account is locked |
| **min_password**  integer | Minimum user password length  Range between 1 and 100  **Default:** `1` |

## [Notes](purefb_admin_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_admin_module.md#id5)

```yaml+jinja
- name: Set global login parameters
  purestorage.flashblade.purefb_admin:
    max_login: 5
    min_password: 10
    lockout: 300
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
