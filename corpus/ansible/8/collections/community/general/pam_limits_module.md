---
collection: ansible
version: "8"
title: "community.general.pam_limits module – Modify Linux PAM limits"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/pam_limits_module.html
fetched_at: 2026-07-28T01:48:57+00:00
---
# community.general.pam_limits module – Modify Linux PAM limits

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.pam_limits`.

- [Synopsis](pam_limits_module.md#synopsis)
- [Parameters](pam_limits_module.md#parameters)
- [Attributes](pam_limits_module.md#attributes)
- [Notes](pam_limits_module.md#notes)
- [Examples](pam_limits_module.md#examples)

## [Synopsis](pam_limits_module.md#id1)

- The [community.general.pam_limits](pam_limits_module.md#ansible-collections-community-general-pam-limits-module) module modifies PAM limits.
- The default file is `/etc/security/limits.conf`.
- For the full documentation, see `man 5 limits.conf`.

Aliases: system.pam_limits

## [Parameters](pam_limits_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **backup**  boolean | Create a backup file including the timestamp information so you can get the original file back if you somehow clobbered it incorrectly.  **Choices:**   - `false` ← (default) - `true` |
| **comment**  string | Comment associated with the limit.  **Default:** `""` |
| **dest**  string | Modify the limits.conf path.  **Default:** `"/etc/security/limits.conf"` |
| **domain**  string / required | A username, @groupname, wildcard, UID/GID range. |
| **limit_item**  string / required | The limit to be set.  **Choices:**   - `"core"` - `"data"` - `"fsize"` - `"memlock"` - `"nofile"` - `"rss"` - `"stack"` - `"cpu"` - `"nproc"` - `"as"` - `"maxlogins"` - `"maxsyslogins"` - `"priority"` - `"locks"` - `"sigpending"` - `"msgqueue"` - `"nice"` - `"rtprio"` - `"chroot"` |
| **limit_type**  string / required | Limit type, see `man 5 limits.conf` for an explanation.  **Choices:**   - `"hard"` - `"soft"` - `"-"` |
| **use_max**  boolean | If set to `true`, the maximal value will be used or conserved.  If the specified value is superior to the value in the file, file content is replaced with the new value, else content is not modified.  **Choices:**   - `false` ← (default) - `true` |
| **use_min**  boolean | If set to `true`, the minimal value will be used or conserved.  If the specified value is inferior to the value in the file, file content is replaced with the new value, else content is not modified.  **Choices:**   - `false` ← (default) - `true` |
| **value**  string / required | The value of the limit.  Value must either be `unlimited`, `infinity` or `-1`, all of which indicate no limit, or a limit of 0 or larger.  Value must be a number in the range -20 to 19 inclusive, if `limit_item` is set to `nice` or `priority`.  Refer to the `man 5 limits.conf` manual pages for more details. |

## [Attributes](pam_limits_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  *added in community.general 2.0.0* | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full**  *added in community.general 2.0.0* | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](pam_limits_module.md#id4)

> **Note:**
>
> - If `dest` file does not exist, it is created.

## [Examples](pam_limits_module.md#id5)

```yaml+jinja
- name: Add or modify nofile soft limit for the user joe
  community.general.pam_limits:
    domain: joe
    limit_type: soft
    limit_item: nofile
    value: 64000

- name: Add or modify fsize hard limit for the user smith. Keep or set the maximal value
  community.general.pam_limits:
    domain: smith
    limit_type: hard
    limit_item: fsize
    value: 1000000
    use_max: true

- name: Add or modify memlock, both soft and hard, limit for the user james with a comment
  community.general.pam_limits:
    domain: james
    limit_type: '-'
    limit_item: memlock
    value: unlimited
    comment: unlimited memory lock for james

- name: Add or modify hard nofile limits for wildcard domain
  community.general.pam_limits:
    domain: '*'
    limit_type: hard
    limit_item: nofile
    value: 39693561
```

### Authors

- Sebastien Rohaut (@usawa)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
