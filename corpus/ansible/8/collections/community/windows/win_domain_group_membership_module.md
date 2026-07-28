---
collection: ansible
version: "8"
title: "community.windows.win_domain_group_membership module – Manage Windows domain group membership"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_domain_group_membership_module.html
fetched_at: 2026-07-28T02:01:48+00:00
---
# community.windows.win_domain_group_membership module – Manage Windows domain group membership

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_domain_group_membership`.

- [Synopsis](win_domain_group_membership_module.md#synopsis)
- [Parameters](win_domain_group_membership_module.md#parameters)
- [Notes](win_domain_group_membership_module.md#notes)
- [See Also](win_domain_group_membership_module.md#see-also)
- [Examples](win_domain_group_membership_module.md#examples)
- [Return Values](win_domain_group_membership_module.md#return-values)

## [Synopsis](win_domain_group_membership_module.md#id1)

- Allows the addition and removal of domain users and domain groups from/to a domain group.

## [Parameters](win_domain_group_membership_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain_password**  string | The password for *username*. |
| **domain_server**  string | Specifies the Active Directory Domain Services instance to connect to.  Can be in the form of an FQDN or NetBIOS name.  If not specified then the value is based on the domain of the computer running PowerShell. |
| **domain_username**  string | The username to use when interacting with AD.  If this is not set then the user Ansible used to log in with will be used instead when using CredSSP or Kerberos with credential delegation. |
| **members**  list / elements=string / required | A list of members to ensure are present/absent from the group.  The given names must be a SamAccountName of a user, group, service account, or computer.  For computers, you must add “$” after the name; for example, to add “Mycomputer” to a group, use “Mycomputer$” as the member.  If the member object is part of another domain in a multi-domain forest, you must add the domain and “\” in front of the name. |
| **name**  string / required | Name of the domain group to manage membership on. |
| **state**  string | Desired state of the members in the group.  When `state` is `pure`, only the members specified will exist, and all other existing members not specified are removed.  **Choices:**   - `"absent"` - `"present"` ← (default) - `"pure"` |

## [Notes](win_domain_group_membership_module.md#id3)

> **Note:**
>
> - This must be run on a host that has the ActiveDirectory powershell module installed.

## [See Also](win_domain_group_membership_module.md#id4)

> **See also:**
>
> [community.windows.win_domain_user](win_domain_user_module.md#ansible-collections-community-windows-win-domain-user-module)
> :   Manages Windows Active Directory user accounts.
>
> [community.windows.win_domain_group](win_domain_group_module.md#ansible-collections-community-windows-win-domain-group-module)
> :   Creates, modifies or removes domain groups.

## [Examples](win_domain_group_membership_module.md#id5)

```yaml+jinja
- name: Add a domain user/group to a domain group
  community.windows.win_domain_group_membership:
    name: Foo
    members:
      - Bar
    state: present

- name: Remove a domain user/group from a domain group
  community.windows.win_domain_group_membership:
    name: Foo
    members:
      - Bar
    state: absent

- name: Ensure only a domain user/group exists in a domain group
  community.windows.win_domain_group_membership:
    name: Foo
    members:
      - Bar
    state: pure

- name: Add a computer to a domain group
  community.windows.win_domain_group_membership:
    name: Foo
    members:
      - DESKTOP$
    state: present

- name: Add a domain user/group from another Domain in the multi-domain forest to a domain group
  community.windows.win_domain_group_membership:
    domain_server: DomainAAA.cloud
    name: GroupinDomainAAA
    members:
      - DomainBBB.cloud\UserInDomainBBB
    state: Present
```

## [Return Values](win_domain_group_membership_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **added**  list / elements=string | A list of members added when `state` is `present` or `pure`; this is empty if no members are added.  **Returned:** success and `state` is `present` or `pure`  **Sample:** `["UserName", "GroupName"]` |
| **members**  list / elements=string | A list of all domain group members at completion; this is empty if the group contains no members.  **Returned:** success  **Sample:** `["UserName", "GroupName"]` |
| **name**  string | The name of the target domain group.  **Returned:** always  **Sample:** `"Domain-Admins"` |
| **removed**  list / elements=string | A list of members removed when `state` is `absent` or `pure`; this is empty if no members are removed.  **Returned:** success and `state` is `absent` or `pure`  **Sample:** `["UserName", "GroupName"]` |

### Authors

- Marius Rieder (@jiuka)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
