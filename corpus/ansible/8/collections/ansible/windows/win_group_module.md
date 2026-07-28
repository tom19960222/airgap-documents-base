---
collection: ansible
version: "8"
title: "ansible.windows.win_group module – Add and remove local groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/win_group_module.html
fetched_at: 2026-07-28T01:10:38+00:00
---
# ansible.windows.win_group module – Add and remove local groups

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.win_group`.

- [Synopsis](win_group_module.md#synopsis)
- [Parameters](win_group_module.md#parameters)
- [See Also](win_group_module.md#see-also)
- [Examples](win_group_module.md#examples)

## [Synopsis](win_group_module.md#id1)

- Add and remove local groups.
- For non-Windows targets, please use the [ansible.builtin.group](../builtin/group_module.md#ansible-collections-ansible-builtin-group-module) module instead.

## [Parameters](win_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | Description of the group. |
| **name**  string / required | Name of the group. |
| **state**  string | Create or remove the group.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [See Also](win_group_module.md#id3)

> **See also:**
>
> [ansible.builtin.group](../builtin/group_module.md#ansible-collections-ansible-builtin-group-module)
> :   Add or remove groups.
>
> [community.windows.win_domain_group](../../community/windows/win_domain_group_module.md#ansible-collections-community-windows-win-domain-group-module)
> :   Creates, modifies or removes domain groups.
>
> [ansible.windows.win_group_membership](win_group_membership_module.md#ansible-collections-ansible-windows-win-group-membership-module)
> :   Manage Windows local group membership.

## [Examples](win_group_module.md#id4)

```yaml+jinja
- name: Create a new group
  ansible.windows.win_group:
    name: deploy
    description: Deploy Group
    state: present

- name: Remove a group
  ansible.windows.win_group:
    name: deploy
    state: absent
```

### Authors

- Chris Hoffman (@chrishoffman)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
