---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_banner module – Configure Pure Storage FlashBlade GUI and SSH MOTD message"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_banner_module.html
fetched_at: 2026-07-28T02:51:45+00:00
---
# purestorage.flashblade.purefb_banner module – Configure Pure Storage FlashBlade GUI and SSH MOTD message

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
> see [Requirements](purefb_banner_module.md#ansible-collections-purestorage-flashblade-purefb-banner-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_banner`.

New in purestorage.flashblade 1.4.0

- [Synopsis](purefb_banner_module.md#synopsis)
- [Requirements](purefb_banner_module.md#requirements)
- [Parameters](purefb_banner_module.md#parameters)
- [Notes](purefb_banner_module.md#notes)
- [Examples](purefb_banner_module.md#examples)

## [Synopsis](purefb_banner_module.md#id1)

- Configure MOTD for Pure Storage FlashBlades.
- This will be shown during an SSH or GUI login to the system.
- Multiple line messages can be achieved using \\n.

## [Requirements](purefb_banner_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_banner_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **banner**  string | Banner text, or MOTD, to use  **Default:** `"Welcome to the machine..."` |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **state**  string | Set ot delete the MOTD  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](purefb_banner_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_banner_module.md#id5)

```yaml+jinja
- name: Set new banner text
  purestorage.flashblade.purefb_banner:
    banner: "Banner over\ntwo lines"
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete banner text
  purestorage.flashblade.purefb_banner:
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
