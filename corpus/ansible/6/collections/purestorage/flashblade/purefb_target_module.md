---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_target module – Manage remote S3-capable targets for a FlashBlade"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_target_module.html
fetched_at: 2026-07-28T00:19:03+00:00
---
# purestorage.flashblade.purefb_target module – Manage remote S3-capable targets for a FlashBlade

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
> see [Requirements](purefb_target_module.md#ansible-collections-purestorage-flashblade-purefb-target-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_target`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_target_module.md#synopsis)
- [Requirements](purefb_target_module.md#requirements)
- [Parameters](purefb_target_module.md#parameters)
- [Notes](purefb_target_module.md#notes)
- [Examples](purefb_target_module.md#examples)

## [Synopsis](purefb_target_module.md#id1)

- Manage remote S3-capable targets for a FlashBlade system
- Use this for non-FlashBlade targets.
- Use *purestorage.flashblade.purefb_connect* for FlashBlade targets.

## [Requirements](purefb_target_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_target_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | Address of S3-capable target (IP or FQDN) |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **name**  string / required | Name of S3-capable target (IP or FQDN) |
| **state**  string | Create or delete remote target  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](purefb_target_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_target_module.md#id5)

```yaml+jinja
- name: Create a connection to remote S3-capable target
  purestorage.flashblade.purefb_target:
    name: target_1
    address: 10.10.10.20
    fb_url: 10.10.10.2
    api_token: T-89faa581-c668-483d-b77d-23c5d88ba35c
- name: Delete connection to remote S3-capable system
  purestorage.flashblade.purefb_target:
    state: absent
    name: target_1
    target_api: 9c0b56bc-f941-f7a6-9f85-dcc3e9a8f7d6
    fb_url: 10.10.10.2
    api_token: T-89faa581-c668-483d-b77d-23c5d88ba35c
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
