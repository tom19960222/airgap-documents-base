---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_fs_replica module – Manage filesystem replica links between Pure Storage FlashBlades"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_fs_replica_module.html
fetched_at: 2026-07-28T02:51:58+00:00
---
# purestorage.flashblade.purefb_fs_replica module – Manage filesystem replica links between Pure Storage FlashBlades

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
> see [Requirements](purefb_fs_replica_module.md#ansible-collections-purestorage-flashblade-purefb-fs-replica-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_fs_replica`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_fs_replica_module.md#synopsis)
- [Requirements](purefb_fs_replica_module.md#requirements)
- [Parameters](purefb_fs_replica_module.md#parameters)
- [Notes](purefb_fs_replica_module.md#notes)
- [Examples](purefb_fs_replica_module.md#examples)

## [Synopsis](purefb_fs_replica_module.md#id1)

- This module manages filesystem replica links between Pure Storage FlashBlades.

## [Requirements](purefb_fs_replica_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_fs_replica_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **in_progress**  boolean | Confirmation that you wish to delete a filesystem replica link  This may cancel any in-progress replication transfers)  **Choices:**   - `false` ← (default) - `true` |
| **name**  string / required | Local Filesystem Name. |
| **policy**  string | Name of filesystem snapshot policy to apply to the replica link. |
| **state**  string | Creates or modifies a filesystem replica link  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **target_array**  string | Remote array name to create replica on. |
| **target_fs**  string | Name of target filesystem name  If not supplied, will default to *name*. |

## [Notes](purefb_fs_replica_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_fs_replica_module.md#id5)

```yaml+jinja
- name: Create new filesystem replica from foo to bar on arrayB
  purestorage.flashblade.purefb_fs_replica:
    name: foo
    target_array: arrayB
    target_fs: bar
    policy: daily
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Add new snapshot policy to exisitng filesystem replica link
  purestorage.flashblade.purefb_fs_replica:
    name: foo
    policy: weekly
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete snapshot policy from filesystem replica foo
  purestorage.flashblade.purefb_fs_replica:
    name: foo
    policy: weekly
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
