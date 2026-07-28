---
collection: ansible
version: "8"
title: "community.general.swdepot module – Manage packages with swdepot package manager (HP-UX)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/swdepot_module.html
fetched_at: 2026-07-28T01:50:52+00:00
---
# community.general.swdepot module – Manage packages with swdepot package manager (HP-UX)

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
> To use it in a playbook, specify: `community.general.swdepot`.

- [Synopsis](swdepot_module.md#synopsis)
- [Parameters](swdepot_module.md#parameters)
- [Attributes](swdepot_module.md#attributes)
- [Examples](swdepot_module.md#examples)

## [Synopsis](swdepot_module.md#id1)

- Will install, upgrade and remove packages with swdepot package manager (HP-UX)

Aliases: packaging.os.swdepot

## [Parameters](swdepot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **depot**  string | The source repository from which install or upgrade a package. |
| **name**  aliases: pkg  string / required | package name. |
| **state**  string / required | whether to install (`present`, `latest`), or remove (`absent`) a package.  **Choices:**   - `"present"` - `"latest"` - `"absent"` |

## [Attributes](swdepot_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](swdepot_module.md#id4)

```yaml+jinja
- name: Install a package
  community.general.swdepot:
    name: unzip-6.0
    state: present
    depot: 'repository:/path'

- name: Install the latest version of a package
  community.general.swdepot:
    name: unzip
    state: latest
    depot: 'repository:/path'

- name: Remove a package
  community.general.swdepot:
    name: unzip
    state: absent
```

### Authors

- Raul Melo (@melodous)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
