---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_snap module – Manage filesystem snapshots on Pure Storage FlashBlades"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_snap_module.html
fetched_at: 2026-07-28T00:18:59+00:00
---
# purestorage.flashblade.purefb_snap module – Manage filesystem snapshots on Pure Storage FlashBlades

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
> see [Requirements](purefb_snap_module.md#ansible-collections-purestorage-flashblade-purefb-snap-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_snap`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_snap_module.md#synopsis)
- [Requirements](purefb_snap_module.md#requirements)
- [Parameters](purefb_snap_module.md#parameters)
- [Notes](purefb_snap_module.md#notes)
- [Examples](purefb_snap_module.md#examples)

## [Synopsis](purefb_snap_module.md#id1)

- Create or delete volumes and filesystem snapshots on Pure Storage FlashBlades.
- Restoring a filesystem from a snapshot is only supported using the latest snapshot.

## [Requirements](purefb_snap_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_snap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **eradicate**  boolean | Define whether to eradicate the snapshot on delete or leave in trash.  Choices:   - `false` ← (default) - `true` |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **name**  string / required | The name of the source filesystem. |
| **now**  boolean  added in purestorage.flashblade 1.7.0 | Whether to initiate a snapshot replication immeadiately  Choices:   - `false` ← (default) - `true` |
| **state**  string | Define whether the filesystem snapshot should exist or not.  Choices:   - `"absent"` - `"present"` ← (default) - `"restore"` |
| **suffix**  string | Suffix of snapshot name. |
| **targets**  list / elements=string  added in purestorage.flashblade 1.7.0 | Name of target to replicate snapshot to.  This is only applicable when *now* is **True** |

## [Notes](purefb_snap_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_snap_module.md#id5)

```yaml+jinja
- name: Create snapshot foo.ansible
  purestorage.flashblade.purefb_snap:
    name: foo
    suffix: ansible
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Create immeadiate snapshot foo.ansible to connected FB bar
  purestorage.flashblade.purefb_snap:
    name: foo
    suffix: ansible
    now: True
    targets:
    - bar
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Delete snapshot named foo.snap
  purestorage.flashblade.purefb_snap:
    name: foo
    suffix: snap
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent

- name: Recover deleted snapshot foo.ansible
  purestorage.flashblade.purefb_snap:
    name: foo
    suffix: ansible
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: present

- name: Restore filesystem foo (uses latest snapshot)
  purestorage.flashblade.purefb_snap:
    name: foo
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: restore

- name: Eradicate snapshot named foo.snap
  purestorage.flashblade.purefb_snap:
    name: foo
    suffix: snap
    eradicate: true
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
    state: absent
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
