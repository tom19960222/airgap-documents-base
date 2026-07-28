---
collection: ansible
version: "8"
title: "community.general.slackpkg module – Package manager for Slackware >= 12.2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/slackpkg_module.html
fetched_at: 2026-07-28T01:50:38+00:00
---
# community.general.slackpkg module – Package manager for Slackware >= 12.2

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
> see [Requirements](slackpkg_module.md#ansible-collections-community-general-slackpkg-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.slackpkg`.

- [Synopsis](slackpkg_module.md#synopsis)
- [Requirements](slackpkg_module.md#requirements)
- [Parameters](slackpkg_module.md#parameters)
- [Attributes](slackpkg_module.md#attributes)
- [Examples](slackpkg_module.md#examples)

## [Synopsis](slackpkg_module.md#id1)

- Manage binary packages for Slackware using ‘slackpkg’ which is available in versions after 12.2.

Aliases: packaging.os.slackpkg

## [Requirements](slackpkg_module.md#id2)

The below requirements are needed on the host that executes this module.

- Slackware >= 12.2

## [Parameters](slackpkg_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: pkg  list / elements=string / required | name of package to install/remove |
| **state**  string | State of the package, you can use `installed` as an alias for `present` and `removed` as one for `absent`.  **Choices:**   - `"present"` ← (default) - `"absent"` - `"latest"` - `"installed"` - `"removed"` |
| **update_cache**  boolean | update the package database first  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](slackpkg_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](slackpkg_module.md#id5)

```yaml+jinja
- name: Install package foo
  community.general.slackpkg:
    name: foo
    state: present

- name: Remove packages foo and bar
  community.general.slackpkg:
    name: foo,bar
    state: absent

- name: Make sure that it is the most updated package
  community.general.slackpkg:
    name: foo
    state: latest
```

### Authors

- Kim Nørgaard (@KimNorgaard)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
