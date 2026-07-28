---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_lifecycle module – Manage FlashBlade object lifecycles"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_lifecycle_module.html
fetched_at: 2026-07-28T02:52:05+00:00
---
# purestorage.flashblade.purefb_lifecycle module – Manage FlashBlade object lifecycles

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
> see [Requirements](purefb_lifecycle_module.md#ansible-collections-purestorage-flashblade-purefb-lifecycle-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_lifecycle`.

New in purestorage.flashblade 1.4.0

- [Synopsis](purefb_lifecycle_module.md#synopsis)
- [Requirements](purefb_lifecycle_module.md#requirements)
- [Parameters](purefb_lifecycle_module.md#parameters)
- [Notes](purefb_lifecycle_module.md#notes)
- [Examples](purefb_lifecycle_module.md#examples)

## [Synopsis](purefb_lifecycle_module.md#id1)

- Manage lifecycles for object buckets

## [Requirements](purefb_lifecycle_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_lifecycle_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **abort_uploads_after**  string  *added in purestorage.flashblade 1.8.0* | Duration of time after which incomplete multipart uploads will be aborted.  Enter as days (d) or weeks (w). Range is 1 - 2147483647 days. |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **bucket**  string / required | Bucket the lifecycle rule applies to |
| **enabled**  boolean | State of lifecycle rule  **Choices:**   - `false` - `true` ← (default) |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **keep_current_for**  string  *added in purestorage.flashblade 1.8.0* | Time after which current versions will be marked expired.  Enter as days (d) or weeks (w). Range is 1 - 2147483647 days. |
| **keep_current_until**  string  *added in purestorage.flashblade 1.8.0* | Date after which current versions will be marked expired.  Enter as date in form YYYY-MM-DD.  **Note:** setting a date in the past will delete ALL objects with the value of *prefix* as they are created. |
| **keep_previous_for**  aliases: keep_for  string | Time after which previous versions will be marked expired.  Enter as days (d) or weeks (w). Range is 1 - 2147483647 days. |
| **name**  string / required | Name of the lifecycle rule |
| **prefix**  string | Object key prefix identifying one or more objects in the bucket |
| **state**  string | Create or delete lifecycle rule  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefb_lifecycle_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_lifecycle_module.md#id5)

```yaml+jinja
- name: Create a lifecycle rule called bar for bucket foo (pre-Purity//FB 3.2.3)
  purestorage.flashblade.purefb_lifecycle:
    name: bar
    bucket: foo
    keep_previous_for: 2d
    prefix: test
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Create a lifecycle rule called bar for bucket foo (post-Purity//FB 3.2.3)
  purestorage.flashblade.purefb_lifecycle:
    name: bar
    bucket: foo
    keep_previous_for: 2d
    keep_current_for: 1w
    abort_uploads_after: 1d
    keep_current_until: 2020-11-23
    prefix: test
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Modify a lifecycle rule (post-Purity//FB 3.2.3)
  purestorage.flashblade.purefb_lifecycle:
    name: bar
    bucket: foo
    keep_previous_for: 10d
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
- name: Delete lifecycle rule foo from bucket foo
  purestorage.flashblade.purefb_lifecycle:
    name: foo
    bucket: bar
    state: absent
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
