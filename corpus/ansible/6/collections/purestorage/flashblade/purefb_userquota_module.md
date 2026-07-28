---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_userquota module – Manage filesystem user quotas"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_userquota_module.html
fetched_at: 2026-07-28T00:19:06+00:00
---
# purestorage.flashblade.purefb_userquota module – Manage filesystem user quotas

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
> see [Requirements](purefb_userquota_module.md#ansible-collections-purestorage-flashblade-purefb-userquota-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_userquota`.

New in purestorage.flashblade 1.7.0

- [Synopsis](purefb_userquota_module.md#synopsis)
- [Requirements](purefb_userquota_module.md#requirements)
- [Parameters](purefb_userquota_module.md#parameters)
- [Notes](purefb_userquota_module.md#notes)
- [Examples](purefb_userquota_module.md#examples)

## [Synopsis](purefb_userquota_module.md#id1)

- This module manages user quotas for filesystems on Pure Storage FlashBlade.

## [Requirements](purefb_userquota_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_userquota_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **name**  string / required | Filesystem Name. |
| **quota**  string | User quota in M, G, T or P units. This cannot be 0.  This value will override the file system’s default user quota. |
| **state**  string | Create, delete or modifies a quota.  Choices:   - `"present"` ← (default) - `"absent"` |
| **uid**  integer | The user id on which the quota is enforced.  Cannot be combined with *uname* |
| **uname**  string | The user name on which the quota is enforced.  Cannot be combined with *uid* |

## [Notes](purefb_userquota_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_userquota_module.md#id5)

```yaml+jinja
- name: Create new user (using UID) quota for filesystem named foo
  purestorage.flashblade.purefb_userquota:
    name: foo
    quota: 1T
    uid: 1234
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Create new user (using username) quota for filesystem named foo
  purestorage.flashblade.purefb_userquota:
    name: foo
    quota: 1T
    uname: bar
    state: present
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete user quota on filesystem foo for user by UID
  purestorage.flashblade.purefb_userquota:
    name: foo
    uid: 1234
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Delete user quota on filesystem foo for user by username
  purestorage.flashblade.purefb_userquota:
    name: foo
    uname: bar
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Update user quota on filesystem foo for user by username
  purestorage.flashblade.purefb_userquota:
    name: foo
    quota: 20G
    uname: bar
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641

- name: Update user quota on filesystem foo for user by UID
  purestorage.flashblade.purefb_userquota:
    name: foo
    quota: 20G
    uid: bar
    state: absent
    fb_url: 10.10.10.2
    api_token: T-55a68eb5-c785-4720-a2ca-8b03903bf641
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
