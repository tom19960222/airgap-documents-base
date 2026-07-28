---
collection: ansible
version: "6"
title: "ansible.builtin.group module – Add or remove groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/group_module.html
fetched_at: 2026-07-27T16:44:02+00:00
---
# ansible.builtin.group module – Add or remove groups

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `group` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](group_module.md#synopsis)
- [Requirements](group_module.md#requirements)
- [Parameters](group_module.md#parameters)
- [Attributes](group_module.md#attributes)
- [See Also](group_module.md#see-also)
- [Examples](group_module.md#examples)
- [Return Values](group_module.md#return-values)

## [Synopsis](group_module.md#id1)

- Manage presence of groups on a host.
- For Windows targets, use the [ansible.windows.win_group](../windows/win_group_module.md#ansible-collections-ansible-windows-win-group-module) module instead.

## [Requirements](group_module.md#id2)

The below requirements are needed on the host that executes this module.

- groupadd
- groupdel
- groupmod

## [Parameters](group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **gid**  integer | Optional *GID* to set for the group. |
| **local**  boolean | Forces the use of “local” command alternatives on platforms that implement it.  This is useful in environments that use centralized authentication when you want to manipulate the local groups. (for example, it uses `lgroupadd` instead of `groupadd`).  This requires that these commands exist on the targeted host, otherwise it will be a fatal error.  Choices:   - `false` ← (default) - `true` |
| **name**  string / required | Name of the group to manage. |
| **non_unique**  boolean  added in Ansible 2.8 | This option allows to change the group ID to a non-unique value. Requires `gid`.  Not supported on macOS or BusyBox distributions.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Whether the group should be present or not on the remote host.  Choices:   - `"absent"` - `"present"` ← (default) |
| **system**  boolean | If *yes*, indicates that the group created is a system group.  Choices:   - `false` ← (default) - `true` |

## [Attributes](group_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platform: posix | Target OS/families that can be operated against |

## [See Also](group_module.md#id5)

> **See also:**
>
> [ansible.builtin.user](user_module.md#ansible-collections-ansible-builtin-user-module)
> :   Manage user accounts.
>
> [ansible.windows.win_group](../windows/win_group_module.md#ansible-collections-ansible-windows-win-group-module)
> :   Add and remove local groups.

## [Examples](group_module.md#id6)

```yaml+jinja
- name: Ensure group "somegroup" exists
  ansible.builtin.group:
    name: somegroup
    state: present

- name: Ensure group "docker" exists with correct gid
  ansible.builtin.group:
    name: docker
    state: present
    gid: 1750
```

## [Return Values](group_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **gid**  integer | Group ID of the group.  Returned: When `state` is ‘present’  Sample: `1001` |
| **name**  string | Group name.  Returned: always  Sample: `"users"` |
| **state**  string | Whether the group is present or not.  Returned: always  Sample: `"absent"` |
| **system**  boolean | Whether the group is a system group or not.  Returned: When `state` is ‘present’  Sample: `false` |

### Authors

- Stephen Fromm (@sfromm)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
