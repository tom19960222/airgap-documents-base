---
collection: ansible
version: "6"
title: "community.general.apt_repo module – Manage APT repositories via apt-repo"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/apt_repo_module.html
fetched_at: 2026-07-27T17:08:08+00:00
---
# community.general.apt_repo module – Manage APT repositories via apt-repo

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
> To use it in a playbook, specify: `community.general.apt_repo`.

- [Synopsis](apt_repo_module.md#synopsis)
- [Parameters](apt_repo_module.md#parameters)
- [Notes](apt_repo_module.md#notes)
- [Examples](apt_repo_module.md#examples)

## [Synopsis](apt_repo_module.md#id1)

- Manages APT repositories using apt-repo tool.
- See <https://www.altlinux.org/Apt-repo> for details about apt-repo

## [Parameters](apt_repo_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **remove_others**  boolean | Remove other then added repositories  Used if *state=present*  Choices:   - `false` ← (default) - `true` |
| **repo**  string / required | Name of the repository to add or remove. |
| **state**  string | Indicates the desired repository state.  Choices:   - `"absent"` - `"present"` ← (default) |
| **update**  boolean | Update the package database after changing repositories.  Choices:   - `false` ← (default) - `true` |

## [Notes](apt_repo_module.md#id3)

> **Note:**
>
> - This module works on ALT based distros.
> - Does NOT support checkmode, due to a limitation in apt-repo tool.

## [Examples](apt_repo_module.md#id4)

```yaml+jinja
- name: Remove all repositories
  community.general.apt_repo:
    repo: all
    state: absent

- name: Add repository `Sisysphus` and remove other repositories
  community.general.apt_repo:
    repo: Sisysphus
    state: present
    remove_others: true

- name: Add local repository `/space/ALT/Sisyphus` and update package cache
  community.general.apt_repo:
    repo: copy:///space/ALT/Sisyphus
    state: present
    update: true
```

### Authors

- Mikhail Gordeev (@obirvalger)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
