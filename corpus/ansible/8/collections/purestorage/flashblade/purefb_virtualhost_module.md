---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_virtualhost module – Manage FlashBlade Object Store Virtual Hosts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_virtualhost_module.html
fetched_at: 2026-07-28T02:52:28+00:00
---
# purestorage.flashblade.purefb_virtualhost module – Manage FlashBlade Object Store Virtual Hosts

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
> see [Requirements](purefb_virtualhost_module.md#ansible-collections-purestorage-flashblade-purefb-virtualhost-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_virtualhost`.

New in purestorage.flashblade 1.6.0

- [Synopsis](purefb_virtualhost_module.md#synopsis)
- [Requirements](purefb_virtualhost_module.md#requirements)
- [Parameters](purefb_virtualhost_module.md#parameters)
- [Notes](purefb_virtualhost_module.md#notes)
- [Examples](purefb_virtualhost_module.md#examples)

## [Synopsis](purefb_virtualhost_module.md#id1)

- Add or delete FlashBlade Object Store Virtual Hosts

## [Requirements](purefb_virtualhost_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_virtualhost_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **name**  string / required | Name of the Object Store Virtual Host  A hostname or domain by which the array can be addressed for virtual hosted-style S3 requests. |
| **state**  string | Define whether the Object Store Virtual Host should be added or deleted  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefb_virtualhost_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_virtualhost_module.md#id5)

```yaml+jinja
- name: Add Object Store Virtual Host
  purestorage.flashblade.purefb_virtualhost:
    name: "s3.acme.com"
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3

- name: Delete Object Store Virtual Host
  purestorage.flashblade.purefb_virtualhost:
    name: "nohost.acme.com"
    state: absent
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
