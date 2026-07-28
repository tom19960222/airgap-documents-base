---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_eula module – Sign Pure Storage FlashBlade EULA"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_eula_module.html
fetched_at: 2026-07-28T00:18:46+00:00
---
# purestorage.flashblade.purefb_eula module – Sign Pure Storage FlashBlade EULA

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
> see [Requirements](purefb_eula_module.md#ansible-collections-purestorage-flashblade-purefb-eula-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_eula`.

New in purestorage.flashblade 1.6.0

- [Synopsis](purefb_eula_module.md#synopsis)
- [Requirements](purefb_eula_module.md#requirements)
- [Parameters](purefb_eula_module.md#parameters)
- [Notes](purefb_eula_module.md#notes)
- [Examples](purefb_eula_module.md#examples)

## [Synopsis](purefb_eula_module.md#id1)

- Sign the FlashBlade EULA for Day 0 config, or change signatory.

## [Requirements](purefb_eula_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_eula_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **company**  string / required | Full legal name of the entity.  The value must be between 1 and 64 characters in length. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **name**  string / required | Full legal name of the individual at the company who has the authority to accept the terms of the agreement.  The value must be between 1 and 64 characters in length. |
| **title**  string / required | Individual’s job title at the company.  The value must be between 1 and 64 characters in length. |

## [Notes](purefb_eula_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_eula_module.md#id5)

```yaml+jinja
- name: Sign EULA for FlashBlade
  purestorage.flashblade.purefb_eula:
    company: "ACME Storage, Inc."
    name: "Fred Bloggs"
    title: "Storage Manager"
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
