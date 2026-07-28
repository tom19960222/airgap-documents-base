---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_bucket module – Manage Object Store Buckets on a  Pure Storage FlashBlade."
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_bucket_module.html
fetched_at: 2026-07-28T02:51:48+00:00
---
# purestorage.flashblade.purefb_bucket module – Manage Object Store Buckets on a Pure Storage FlashBlade.

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
> see [Requirements](purefb_bucket_module.md#ansible-collections-purestorage-flashblade-purefb-bucket-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_bucket`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_bucket_module.md#synopsis)
- [Requirements](purefb_bucket_module.md#requirements)
- [Parameters](purefb_bucket_module.md#parameters)
- [Notes](purefb_bucket_module.md#notes)
- [Examples](purefb_bucket_module.md#examples)

## [Synopsis](purefb_bucket_module.md#id1)

- This module managess object store (s3) buckets on Pure Storage FlashBlade.

## [Requirements](purefb_bucket_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_bucket_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string / required | Object Store Account for Bucket. |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **default_retention**  string  *added in purestorage.flashblade 1.12.0* | The retention period, in days, used to apply locks on new objects if none is specified by the S3 client  Valid values between 1 and 365000  Use “” to clear |
| **eradicate**  boolean | Define whether to eradicate the bucket on delete or leave in trash.  **Choices:**   - `false` ← (default) - `true` |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **freeze_locked_objects**  boolean  *added in purestorage.flashblade 1.12.0* | If set to true, a locked object will be read-only and no new versions of the object may be created due to modifications  After enabling, can be disabled only by contacting Pure Technical Services  **Choices:**   - `false` ← (default) - `true` |
| **hard_limit**  boolean  *added in purestorage.flashblade 1.12.0* | Whether the *quota* value is enforced or not  **Choices:**   - `false` - `true` |
| **mode**  string  *added in purestorage.flashblade 1.10.0* | The type of bucket to be created. Also referred to a VSO Mode.  Requires Purity//FB 3.3.3 or higher  *multi-site-writable* type can only be used after feature is enabled by Pure Technical Support  **Choices:**   - `"classic"` ← (default) - `"multi-site-writable"` |
| **name**  string / required | Bucket Name. |
| **object_lock_enabled**  boolean  *added in purestorage.flashblade 1.12.0* | If set to true, then S3 APIs relating to object lock may be used  **Choices:**   - `false` ← (default) - `true` |
| **quota**  string  *added in purestorage.flashblade 1.12.0* | User quota in M, G, T or P units. This cannot be 0.  This value will override the object store account’s default bucket quota. |
| **retention_lock**  string  *added in purestorage.flashblade 1.12.0* | Set retention lock level for the bucket  Once set to *ratcheted* can only be lowered by Pure Technical Services  **Choices:**   - `"ratcheted"` - `"unlocked"` ← (default) |
| **retention_mode**  string  *added in purestorage.flashblade 1.12.0* | The retention mode used to apply locks on new objects if none is specified by the S3 client  Use “” to clear  Once set to *compliance* this can only be changed by contacting Pure Technical Services  **Choices:**   - `"compliance"` - `"governance"` - `""` |
| **state**  string | Create, delete or modifies a bucket.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **versioning**  string | State of S3 bucket versioning  **Choices:**   - `"enabled"` - `"suspended"` - `"absent"` ← (default) |

## [Notes](purefb_bucket_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_bucket_module.md#id5)

```yaml+jinja
- name: Create new bucket named foo in account bar
  purestorage.flashblade.purefb_bucket:
    name: foo
    account: bar
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete bucket named foo in account bar
  purestorage.flashblade.purefb_bucket:
    name: foo
    account: bar
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Change bucket versioning state
  purestorage.flashblade.purefb_bucket:
    name: foo
    account: bar
    versioning: enabled
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Recover deleted bucket named foo in account bar
  purestorage.flashblade.purefb_bucket:
    name: foo
    account: bar
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Eradicate bucket named foo in account bar
  purestorage.flashblade.purefb_bucket:
    name: foo
    account: bar
    state: absent
    eradicate: true
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
