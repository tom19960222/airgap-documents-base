---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_s3acc module – Create or delete FlashBlade Object Store accounts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_s3acc_module.html
fetched_at: 2026-07-28T00:18:57+00:00
---
# purestorage.flashblade.purefb_s3acc module – Create or delete FlashBlade Object Store accounts

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
> see [Requirements](purefb_s3acc_module.md#ansible-collections-purestorage-flashblade-purefb-s3acc-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_s3acc`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_s3acc_module.md#synopsis)
- [Requirements](purefb_s3acc_module.md#requirements)
- [Parameters](purefb_s3acc_module.md#parameters)
- [Notes](purefb_s3acc_module.md#notes)
- [Examples](purefb_s3acc_module.md#examples)

## [Synopsis](purefb_s3acc_module.md#id1)

- Create or delete object store accounts on a Pure Stoage FlashBlade.

## [Requirements](purefb_s3acc_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_s3acc_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **name**  string / required | The name of object store account |
| **state**  string | Create or delete object store account  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](purefb_s3acc_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_s3acc_module.md#id5)

```yaml+jinja
- name: Crrate object store account foo
  purestorage.flashblade.purefb_s3acc:
    name: foo
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete object store account foo
  purestorage.flashblade.purefb_s3acc:
    name: foo
    state: absent
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
