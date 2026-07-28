---
collection: ansible
version: "6"
title: "ansible.windows.win_acl_inheritance module – Change ACL inheritance"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_acl_inheritance_module.html
fetched_at: 2026-07-27T16:44:52+00:00
---
# ansible.windows.win_acl_inheritance module – Change ACL inheritance

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) (version 1.12.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_acl_inheritance`.

- [Synopsis](win_acl_inheritance_module.md#synopsis)
- [Parameters](win_acl_inheritance_module.md#parameters)
- [See Also](win_acl_inheritance_module.md#see-also)
- [Examples](win_acl_inheritance_module.md#examples)

## [Synopsis](win_acl_inheritance_module.md#id1)

- Change ACL (Access Control List) inheritance and optionally copy inherited ACE’s (Access Control Entry) to dedicated ACE’s or vice versa.

## [Parameters](win_acl_inheritance_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **path**  string / required | Path to be used for changing inheritance  Support for registry keys have been added in `ansible.windows>=1.11.0` |
| **reorganize**  boolean | For **ERROR while parsing**: While parsing P() at index 5: Parameter “state” is not of the form FQCN#type = *absent*, indicates if the inherited ACE’s should be copied from the parent. This is necessary (in combination with removal) for a simple ACL instead of using multiple ACE deny entries.  For **ERROR while parsing**: While parsing P() at index 5: Parameter “state” is not of the form FQCN#type = *present*, indicates if the inherited ACE’s should be deduplicated compared to the parent. This removes complexity of the ACL structure.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Specify whether to enable *present* or disable *absent* ACL inheritance.  Choices:   - `"absent"` ← (default) - `"present"` |

## [See Also](win_acl_inheritance_module.md#id3)

> **See also:**
>
> [ansible.windows.win_acl](win_acl_module.md#ansible-collections-ansible-windows-win-acl-module)
> :   Set file/directory/registry permissions for a system user or group.
>
> [ansible.windows.win_file](win_file_module.md#ansible-collections-ansible-windows-win-file-module)
> :   Creates, touches or removes files or directories.
>
> [ansible.windows.win_stat](win_stat_module.md#ansible-collections-ansible-windows-win-stat-module)
> :   Get information about Windows files.

## [Examples](win_acl_inheritance_module.md#id4)

```yaml+jinja
- name: Disable inherited ACE's
  ansible.windows.win_acl_inheritance:
    path: C:\apache
    state: absent

- name: Disable and copy inherited ACE's
  ansible.windows.win_acl_inheritance:
    path: C:\apache
    state: absent
    reorganize: true

- name: Enable and remove dedicated ACE's
  ansible.windows.win_acl_inheritance:
    path: C:\apache
    state: present
    reorganize: true

- name: Disable registry key inherited ACE's
  ansible.windows.win_acl_inheritance:
    path: HKLM:\SOFTWARE\Secrets
    state: absent

- name: Disable and copy registry key inherited ACE's
  ansible.windows.win_acl_inheritance:
    path: HKLM:\SOFTWARE\Secrets
    state: absent
    reorganize: true

- name: Enable and remove registry key dedicated ACE's
  ansible.windows.win_acl_inheritance:
    path: HKLM:\SOFTWARE\Secrets
    state: present
    reorganize: true
```

### Authors

- Oleg Galushko (@inorangestylee)
- Hans-Joachim Kliemeck (@h0nIg)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
