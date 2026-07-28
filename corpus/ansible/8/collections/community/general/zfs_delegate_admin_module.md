---
collection: ansible
version: "8"
title: "community.general.zfs_delegate_admin module – Manage ZFS delegated administration (user admin privileges)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/zfs_delegate_admin_module.html
fetched_at: 2026-07-28T01:51:38+00:00
---
# community.general.zfs_delegate_admin module – Manage ZFS delegated administration (user admin privileges)

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](zfs_delegate_admin_module.md#ansible-collections-community-general-zfs-delegate-admin-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.zfs_delegate_admin`.

- [Synopsis](zfs_delegate_admin_module.md#synopsis)
- [Requirements](zfs_delegate_admin_module.md#requirements)
- [Parameters](zfs_delegate_admin_module.md#parameters)
- [Attributes](zfs_delegate_admin_module.md#attributes)
- [Examples](zfs_delegate_admin_module.md#examples)

## [Synopsis](zfs_delegate_admin_module.md#id1)

- Manages ZFS file system delegated administration permissions, which allow unprivileged users to perform ZFS operations normally restricted to the superuser.
- See the `zfs allow` section of `zfs(1M)` for detailed explanations of options.
- This module attempts to adhere to the behavior of the command line tool as much as possible.

Aliases: storage.zfs.zfs_delegate_admin

## [Requirements](zfs_delegate_admin_module.md#id2)

The below requirements are needed on the host that executes this module.

- A ZFS/OpenZFS implementation that supports delegation with `zfs allow`, including: Solaris >= 10, illumos (all versions), FreeBSD >= 8.0R, ZFS on Linux >= 0.7.0.

## [Parameters](zfs_delegate_admin_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **descendents**  boolean | Apply permissions to `name`‘s descendents (`zfs allow -d`).  **Choices:**   - `false` - `true` |
| **everyone**  boolean | Apply permissions to everyone.  **Choices:**   - `false` ← (default) - `true` |
| **groups**  list / elements=string | List of groups to whom permission(s) should be granted. |
| **local**  boolean | Apply permissions to `name` locally (`zfs allow -l`).  **Choices:**   - `false` - `true` |
| **name**  string / required | File system or volume name, for example `rpool/myfs`. |
| **permissions**  list / elements=string | The list of permission(s) to delegate (required if `state=present`).  Supported permissions depend on the ZFS version in use. See for example <https://openzfs.github.io/openzfs-docs/man/8/zfs-allow.8.html> for OpenZFS. |
| **recursive**  boolean | Unallow permissions recursively (ignored when `state=present`).  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Whether to allow (`present`), or unallow (`absent`) a permission.  When set to `present`, at least one “entity” param of `users`, `groups`, or `everyone` are required.  When set to `absent`, removes permissions from the specified entities, or removes all permissions if no entity params are specified.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **users**  list / elements=string | List of users to whom permission(s) should be granted. |

## [Attributes](zfs_delegate_admin_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](zfs_delegate_admin_module.md#id5)

```yaml+jinja
- name: Grant `zfs allow` and `unallow` permission to the `adm` user with the default local+descendents scope
  community.general.zfs_delegate_admin:
    name: rpool/myfs
    users: adm
    permissions: allow,unallow

- name: Grant `zfs send` to everyone, plus the group `backup`
  community.general.zfs_delegate_admin:
    name: rpool/myvol
    groups: backup
    everyone: true
    permissions: send

- name: Grant `zfs send,receive` to users `foo` and `bar` with local scope only
  community.general.zfs_delegate_admin:
    name: rpool/myfs
    users: foo,bar
    permissions: send,receive
    local: true

- name: Revoke all permissions from everyone (permissions specifically assigned to users and groups remain)
  community.general.zfs_delegate_admin:
    name: rpool/myfs
    everyone: true
    state: absent
```

### Authors

- Nate Coraor (@natefoo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
