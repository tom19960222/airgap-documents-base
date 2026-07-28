---
collection: ansible
version: "6"
title: "ansible.builtin.dpkg_selections module – Dpkg package selection selections"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/dpkg_selections_module.html
fetched_at: 2026-07-27T16:43:59+00:00
---
# ansible.builtin.dpkg_selections module – Dpkg package selection selections

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `dpkg_selections` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](dpkg_selections_module.md#synopsis)
- [Parameters](dpkg_selections_module.md#parameters)
- [Attributes](dpkg_selections_module.md#attributes)
- [Notes](dpkg_selections_module.md#notes)
- [Examples](dpkg_selections_module.md#examples)

## [Synopsis](dpkg_selections_module.md#id1)

- Change dpkg package selection state via –get-selections and –set-selections.

## [Parameters](dpkg_selections_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string / required | Name of the package. |
| **selection**  string / required | The selection state to set the package to.  Choices:   - `"install"` - `"hold"` - `"deinstall"` - `"purge"` |

## [Attributes](dpkg_selections_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platform: debian | Target OS/families that can be operated against |

## [Notes](dpkg_selections_module.md#id4)

> **Note:**
>
> - This module won’t cause any packages to be installed/removed/purged, use the `apt` module for that.

## [Examples](dpkg_selections_module.md#id5)

```yaml+jinja
- name: Prevent python from being upgraded
  ansible.builtin.dpkg_selections:
    name: python
    selection: hold

- name: Allow python to be upgraded
  ansible.builtin.dpkg_selections:
    name: python
    selection: install
```

### Authors

- Brian Brazil (@brian-brazil)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
