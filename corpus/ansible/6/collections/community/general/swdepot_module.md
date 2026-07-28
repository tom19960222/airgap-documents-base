---
collection: ansible
version: "6"
title: "community.general.swdepot module – Manage packages with swdepot package manager (HP-UX)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/swdepot_module.html
fetched_at: 2026-07-27T17:13:29+00:00
---
# community.general.swdepot module – Manage packages with swdepot package manager (HP-UX)

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
> To use it in a playbook, specify: `community.general.swdepot`.

- [Synopsis](swdepot_module.md#synopsis)
- [Parameters](swdepot_module.md#parameters)
- [Examples](swdepot_module.md#examples)

## [Synopsis](swdepot_module.md#id1)

- Will install, upgrade and remove packages with swdepot package manager (HP-UX)

## [Parameters](swdepot_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **depot**  string | The source repository from which install or upgrade a package. |
| **name**  aliases: pkg  string / required | package name. |
| **state**  string / required | whether to install (`present`, `latest`), or remove (`absent`) a package.  Choices:   - `"present"` - `"latest"` - `"absent"` |

## [Examples](swdepot_module.md#id3)

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

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
