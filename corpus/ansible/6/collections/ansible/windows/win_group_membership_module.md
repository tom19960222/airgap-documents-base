---
collection: ansible
version: "6"
title: "ansible.windows.win_group_membership module – Manage Windows local group membership"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_group_membership_module.html
fetched_at: 2026-07-27T16:44:57+00:00
---
# ansible.windows.win_group_membership module – Manage Windows local group membership

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
> To use it in a playbook, specify: `ansible.windows.win_group_membership`.

- [Synopsis](win_group_membership_module.md#synopsis)
- [Parameters](win_group_membership_module.md#parameters)
- [See Also](win_group_membership_module.md#see-also)
- [Examples](win_group_membership_module.md#examples)
- [Return Values](win_group_membership_module.md#return-values)

## [Synopsis](win_group_membership_module.md#id1)

- Allows the addition and removal of local, service and domain users, and domain groups from a local group.

## [Parameters](win_group_membership_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **members**  list / elements=string / required | A list of members to ensure are present/absent from the group.  Accepts local users as .\username, and SERVERNAME\username.  Accepts domain users and groups as DOMAIN\username and [username@DOMAIN](mailto:username%40DOMAIN).  Accepts service users as NT AUTHORITY\username.  Accepts all local, domain and service user types as username, favoring domain lookups when in a domain. |
| **name**  string / required | Name of the local group to manage membership on. |
| **state**  string | Desired state of the members in the group.  When `state` is `pure`, only the members specified will exist, and all other existing members not specified are removed.  Choices:   - `"absent"` - `"present"` ← (default) - `"pure"` |

## [See Also](win_group_membership_module.md#id3)

> **See also:**
>
> [community.windows.win_domain_group](../../community/windows/win_domain_group_module.md#ansible-collections-community-windows-win-domain-group-module)
> :   Creates, modifies or removes domain groups.
>
> [ansible.windows.win_domain_membership](win_domain_membership_module.md#ansible-collections-ansible-windows-win-domain-membership-module)
> :   Manage domain/workgroup membership for a Windows host.
>
> [ansible.windows.win_group](win_group_module.md#ansible-collections-ansible-windows-win-group-module)
> :   Add and remove local groups.

## [Examples](win_group_membership_module.md#id4)

```yaml+jinja
- name: Add a local and domain user to a local group
  ansible.windows.win_group_membership:
    name: Remote Desktop Users
    members:
      - NewLocalAdmin
      - DOMAIN\TestUser
    state: present

- name: Remove a domain group and service user from a local group
  ansible.windows.win_group_membership:
    name: Backup Operators
    members:
      - DOMAIN\TestGroup
      - NT AUTHORITY\SYSTEM
    state: absent

- name: Ensure only a domain user exists in a local group
  ansible.windows.win_group_membership:
    name: Remote Desktop Users
    members:
      - DOMAIN\TestUser
    state: pure
```

## [Return Values](win_group_membership_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **added**  list / elements=string | A list of members added when `state` is `present` or `pure`; this is empty if no members are added.  Returned: success and `state` is `present`  Sample: `["SERVERNAME\\NewLocalAdmin", "DOMAIN\\TestUser"]` |
| **members**  list / elements=string | A list of all local group members at completion; this is empty if the group contains no members.  Returned: success  Sample: `["DOMAIN\\TestUser", "SERVERNAME\\NewLocalAdmin"]` |
| **name**  string | The name of the target local group.  Returned: always  Sample: `"Administrators"` |
| **removed**  list / elements=string | A list of members removed when `state` is `absent` or `pure`; this is empty if no members are removed.  Returned: success and `state` is `absent`  Sample: `["DOMAIN\\TestGroup", "NT AUTHORITY\\SYSTEM"]` |

### Authors

- Andrew Saraceni (@andrewsaraceni)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
