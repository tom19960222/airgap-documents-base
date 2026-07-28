---
collection: ansible
version: "8"
title: "community.general.portinstall module – Installing packages from FreeBSD’s ports system"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/portinstall_module.html
fetched_at: 2026-07-28T01:49:09+00:00
---
# community.general.portinstall module – Installing packages from FreeBSD’s ports system

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
> To use it in a playbook, specify: `community.general.portinstall`.

- [Synopsis](portinstall_module.md#synopsis)
- [Parameters](portinstall_module.md#parameters)
- [Attributes](portinstall_module.md#attributes)
- [Examples](portinstall_module.md#examples)

## [Synopsis](portinstall_module.md#id1)

- Manage packages for FreeBSD using ‘portinstall’.

Aliases: packaging.os.portinstall

## [Parameters](portinstall_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  aliases: pkg  string / required | name of package to install/remove |
| **state**  string | state of the package  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_packages**  boolean | use packages instead of ports whenever available  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](portinstall_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](portinstall_module.md#id4)

```yaml+jinja
- name: Install package foo
  community.general.portinstall:
    name: foo
    state: present

- name: Install package security/cyrus-sasl2-saslauthd
  community.general.portinstall:
    name: security/cyrus-sasl2-saslauthd
    state: present

- name: Remove packages foo and bar
  community.general.portinstall:
    name: foo,bar
    state: absent
```

### Authors

- berenddeboer (@berenddeboer)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
