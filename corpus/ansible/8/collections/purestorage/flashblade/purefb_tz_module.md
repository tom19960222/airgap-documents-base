---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_tz module – Configure Pure Storage FlashBlade timezone"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_tz_module.html
fetched_at: 2026-07-28T02:52:25+00:00
---
# purestorage.flashblade.purefb_tz module – Configure Pure Storage FlashBlade timezone

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
> see [Requirements](purefb_tz_module.md#ansible-collections-purestorage-flashblade-purefb-tz-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_tz`.

New in purestorage.flashblade 1.10.0

- [Synopsis](purefb_tz_module.md#synopsis)
- [Requirements](purefb_tz_module.md#requirements)
- [Parameters](purefb_tz_module.md#parameters)
- [Notes](purefb_tz_module.md#notes)
- [Examples](purefb_tz_module.md#examples)

## [Synopsis](purefb_tz_module.md#id1)

- Configure the timezone for a Pure Storage FlashBlade.

## [Requirements](purefb_tz_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_tz_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **timezone**  string | If not provided, the module will attempt to get the current local timezone from the server |

## [Notes](purefb_tz_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_tz_module.md#id5)

```yaml+jinja
- name: Set FlashBlade Timezone to Americas/Los_Angeles
  purestorage.flashblade.purefb_tz:
    timezone: "America/Los_Angeles"
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
