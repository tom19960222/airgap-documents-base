---
collection: ansible
version: "8"
title: "community.general.xfs_quota module – Manage quotas on XFS filesystems"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/xfs_quota_module.html
fetched_at: 2026-07-28T01:51:34+00:00
---
# community.general.xfs_quota module – Manage quotas on XFS filesystems

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
> see [Requirements](xfs_quota_module.md#ansible-collections-community-general-xfs-quota-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.xfs_quota`.

- [Synopsis](xfs_quota_module.md#synopsis)
- [Requirements](xfs_quota_module.md#requirements)
- [Parameters](xfs_quota_module.md#parameters)
- [Attributes](xfs_quota_module.md#attributes)
- [Examples](xfs_quota_module.md#examples)
- [Return Values](xfs_quota_module.md#return-values)

## [Synopsis](xfs_quota_module.md#id1)

- Configure quotas on XFS filesystems.
- Before using this module /etc/projects and /etc/projid need to be configured.

Aliases: system.xfs_quota

## [Requirements](xfs_quota_module.md#id2)

The below requirements are needed on the host that executes this module.

- xfsprogs

## [Parameters](xfs_quota_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bhard**  string | Hard blocks quota limit.  This argument supports human readable sizes. |
| **bsoft**  string | Soft blocks quota limit.  This argument supports human readable sizes. |
| **ihard**  integer | Hard inodes quota limit. |
| **isoft**  integer | Soft inodes quota limit. |
| **mountpoint**  string / required | The mount point on which to apply the quotas. |
| **name**  string | The name of the user, group or project to apply the quota to, if other than default. |
| **rtbhard**  string | Hard realtime blocks quota limit.  This argument supports human readable sizes. |
| **rtbsoft**  string | Soft realtime blocks quota limit.  This argument supports human readable sizes. |
| **state**  string | Whether to apply the limits or remove them.  When removing limit, they are set to 0, and not quite removed.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **type**  string / required | The XFS quota type.  **Choices:**   - `"user"` - `"group"` - `"project"` |

## [Attributes](xfs_quota_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](xfs_quota_module.md#id5)

```yaml+jinja
- name: Set default project soft and hard limit on /opt of 1g
  community.general.xfs_quota:
    type: project
    mountpoint: /opt
    bsoft: 1g
    bhard: 1g
    state: present

- name: Remove the default limits on /opt
  community.general.xfs_quota:
    type: project
    mountpoint: /opt
    state: absent

- name: Set default soft user inode limits on /home of 1024 inodes and hard of 2048
  community.general.xfs_quota:
    type: user
    mountpoint: /home
    isoft: 1024
    ihard: 2048
```

## [Return Values](xfs_quota_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **bhard**  integer | the current bhard setting in bytes  **Returned:** always  **Sample:** `1024` |
| **bsoft**  integer | the current bsoft setting in bytes  **Returned:** always  **Sample:** `1024` |
| **ihard**  integer | the current ihard setting in bytes  **Returned:** always  **Sample:** `100` |
| **isoft**  integer | the current isoft setting in bytes  **Returned:** always  **Sample:** `100` |
| **rtbhard**  integer | the current rtbhard setting in bytes  **Returned:** always  **Sample:** `1024` |
| **rtbsoft**  integer | the current rtbsoft setting in bytes  **Returned:** always  **Sample:** `1024` |

### Authors

- William Leemans (@bushvin)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
