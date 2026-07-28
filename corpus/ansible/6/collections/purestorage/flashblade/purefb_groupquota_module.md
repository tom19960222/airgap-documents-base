---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_groupquota module – Manage filesystem group quotas"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_groupquota_module.html
fetched_at: 2026-07-28T00:18:48+00:00
---
# purestorage.flashblade.purefb_groupquota module – Manage filesystem group quotas

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
> see [Requirements](purefb_groupquota_module.md#ansible-collections-purestorage-flashblade-purefb-groupquota-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_groupquota`.

New in purestorage.flashblade 1.7.0

- [Synopsis](purefb_groupquota_module.md#synopsis)
- [Requirements](purefb_groupquota_module.md#requirements)
- [Parameters](purefb_groupquota_module.md#parameters)
- [Notes](purefb_groupquota_module.md#notes)
- [Examples](purefb_groupquota_module.md#examples)

## [Synopsis](purefb_groupquota_module.md#id1)

- This module manages group quotas for filesystems on Pure Storage FlashBlade.

## [Requirements](purefb_groupquota_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_groupquota_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **gid**  integer | The group id on which the quota is enforced.  Cannot be combined with *gname* |
| **gname**  string | The group name on which the quota is enforced.  Cannot be combined with *gid* |
| **name**  string / required | Filesystem Name. |
| **quota**  string | Group quota in M, G, T or P units. This cannot be 0.  This value will override the file system’s default group quota. |
| **state**  string | Create, delete or modifies a quota.  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](purefb_groupquota_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_groupquota_module.md#id5)

```yaml+jinja
- name: Create new group (using GID) quota for filesystem named foo
  purestorage.flashblade.purefb_groupquota:
    name: foo
    quota: 1T
    gid: 1234
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Create new group (using groupname) quota for filesystem named foo
  purestorage.flashblade.purefb_groupquota:
    name: foo
    quota: 1T
    gname: bar
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete group quota on filesystem foo for group by GID
  purestorage.flashblade.purefb_groupquota:
    name: foo
    gid: 1234
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete group quota on filesystem foo for group by groupname
  purestorage.flashblade.purefb_groupquota:
    name: foo
    gname: bar
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Update group quota on filesystem foo for group by groupname
  purestorage.flashblade.purefb_groupquota:
    name: foo
    quota: 20G
    gname: bar
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Update group quota on filesystem foo for group by GID
  purestorage.flashblade.purefb_groupquota:
    name: foo
    quota: 20G
    gid: bar
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
