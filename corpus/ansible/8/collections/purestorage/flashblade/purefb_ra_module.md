---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_ra module – Enable or Disable Pure Storage FlashBlade Remote Assist"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_ra_module.html
fetched_at: 2026-07-28T02:52:13+00:00
---
# purestorage.flashblade.purefb_ra module – Enable or Disable Pure Storage FlashBlade Remote Assist

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
> see [Requirements](purefb_ra_module.md#ansible-collections-purestorage-flashblade-purefb-ra-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_ra`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_ra_module.md#synopsis)
- [Requirements](purefb_ra_module.md#requirements)
- [Parameters](purefb_ra_module.md#parameters)
- [Notes](purefb_ra_module.md#notes)
- [Examples](purefb_ra_module.md#examples)

## [Synopsis](purefb_ra_module.md#id1)

- Enablke or Disable Remote Assist for a Pure Storage FlashBlade.

## [Requirements](purefb_ra_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_ra_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **state**  string | Define state of remote assist  When set to *enable* the RA port can be exposed using the *debug* module.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Notes](purefb_ra_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_ra_module.md#id5)

```yaml+jinja
- name: Enable Remote Assist port
  purestorage.flashblade.purefb_ra:
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Disable Remote Assist port
  purestorage.flashblade.purefb_ra:
    state: absent
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
