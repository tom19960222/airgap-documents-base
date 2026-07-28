---
collection: ansible
version: "6"
title: "community.general.pkgin module – Package manager for SmartOS, NetBSD, et al"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pkgin_module.html
fetched_at: 2026-07-27T17:11:56+00:00
---
# community.general.pkgin module – Package manager for SmartOS, NetBSD, et al

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.pkgin`.

- [Synopsis](pkgin_module.md#synopsis)
- [Parameters](pkgin_module.md#parameters)
- [Notes](pkgin_module.md#notes)
- [Examples](pkgin_module.md#examples)

## [Synopsis](pkgin_module.md#id1)

- The standard package manager for SmartOS, but also usable on NetBSD or any OS that uses `pkgsrc`. (Home: <http://pkgin.net/>)

## [Parameters](pkgin_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **clean**  boolean | Clean packages cache  Choices:   - `false` ← (default) - `true` |
| **force**  boolean | Force package reinstall  Choices:   - `false` ← (default) - `true` |
| **full_upgrade**  boolean | Upgrade all packages to their newer versions  Choices:   - `false` ← (default) - `true` |
| **name**  aliases: pkg  list / elements=string | Name of package to install/remove;  multiple names may be given, separated by commas |
| **state**  string | Intended state of the package  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_cache**  boolean | Update repository database. Can be run with other steps or on it’s own.  Choices:   - `false` ← (default) - `true` |
| **upgrade**  boolean | Upgrade main packages to their newer versions  Choices:   - `false` ← (default) - `true` |

## [Notes](pkgin_module.md#id3)

> **Note:**
>
> - Known bug with pkgin < 0.8.0: if a package is removed and another package depends on it, the other package will be silently removed as well. New to Ansible 1.9: check-mode support.

## [Examples](pkgin_module.md#id4)

```yaml+jinja
- name: Install package foo
  community.general.pkgin:
    name: foo
    state: present

- name: Install specific version of foo package
  community.general.pkgin:
    name: foo-2.0.1
    state: present

- name: Update cache and install foo package
  community.general.pkgin:
    name: foo
    update_cache: true

- name: Remove package foo
  community.general.pkgin:
    name: foo
    state: absent

- name: Remove packages foo and bar
  community.general.pkgin:
    name: foo,bar
    state: absent

- name: Update repositories as a separate step
  community.general.pkgin:
    update_cache: true

- name: Upgrade main packages (equivalent to pkgin upgrade)
  community.general.pkgin:
    upgrade: true

- name: Upgrade all packages (equivalent to pkgin full-upgrade)
  community.general.pkgin:
    full_upgrade: true

- name: Force-upgrade all packages (equivalent to pkgin -F full-upgrade)
  community.general.pkgin:
    full_upgrade: true
    force: true

- name: Clean packages cache (equivalent to pkgin clean)
  community.general.pkgin:
    clean: true
```

### Authors

- Larry Gilbert (@L2G)
- Shaun Zinck (@szinck)
- Jasper Lievisse Adriaanse (@jasperla)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
