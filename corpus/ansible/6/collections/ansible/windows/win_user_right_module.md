---
collection: ansible
version: "6"
title: "ansible.windows.win_user_right module – Manage Windows User Rights"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_user_right_module.html
fetched_at: 2026-07-27T16:45:05+00:00
---
# ansible.windows.win_user_right module – Manage Windows User Rights

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
> To use it in a playbook, specify: `ansible.windows.win_user_right`.

- [Synopsis](win_user_right_module.md#synopsis)
- [Parameters](win_user_right_module.md#parameters)
- [Notes](win_user_right_module.md#notes)
- [See Also](win_user_right_module.md#see-also)
- [Examples](win_user_right_module.md#examples)
- [Return Values](win_user_right_module.md#return-values)

## [Synopsis](win_user_right_module.md#id1)

- Add, remove or set User Rights for a group or users or groups.
- You can set user rights for both local and domain accounts.

## [Parameters](win_user_right_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | `add` will add the users/groups to the existing right.  `remove` will remove the users/groups from the existing right.  `set` will replace the users/groups of the existing right.  Choices:   - `"add"` - `"remove"` - `"set"` ← (default) |
| **name**  string / required | The name of the User Right as shown by the `Constant Name` value from <https://learn.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/user-rights-assignment>.  The module will return an error if the right is invalid. |
| **users**  list / elements=string / required | A list of users or groups to add/remove on the User Right.  These can be in the form DOMAIN\user-group, [user-group@DOMAIN.COM](mailto:user-group%40DOMAIN.COM) for domain users/groups.  For local users/groups it can be in the form user-group, .\user-group, SERVERNAME\user-group where SERVERNAME is the name of the remote server.  It is highly recommended to use the `.\` or `SERVERNAME\` prefix to avoid any ambiguity with domain account names or errors trying to lookup an account on a domain controller.  You can also add special local accounts like SYSTEM and others.  Can be set to an empty list with *action=set* to remove all accounts from the right. |

## [Notes](win_user_right_module.md#id3)

> **Note:**
>
> - If the server is domain joined this module can change a right but if a GPO governs this right then the changes won’t last.

## [See Also](win_user_right_module.md#id4)

> **See also:**
>
> [ansible.windows.win_group](win_group_module.md#ansible-collections-ansible-windows-win-group-module)
> :   Add and remove local groups.
>
> [ansible.windows.win_group_membership](win_group_membership_module.md#ansible-collections-ansible-windows-win-group-membership-module)
> :   Manage Windows local group membership.
>
> [ansible.windows.win_user](win_user_module.md#ansible-collections-ansible-windows-win-user-module)
> :   Manages local Windows user accounts.

## [Examples](win_user_right_module.md#id5)

```yaml+jinja
---
- name: Replace the entries of Deny log on locally
  ansible.windows.win_user_right:
    name: SeDenyInteractiveLogonRight
    users:
    - Guest
    - Users
    action: set

- name: Add account to Log on as a service
  ansible.windows.win_user_right:
    name: SeServiceLogonRight
    users:
    - .\Administrator
    - '{{ansible_hostname}}\local-user'
    action: add

- name: Remove accounts who can create Symbolic links
  ansible.windows.win_user_right:
    name: SeCreateSymbolicLinkPrivilege
    users:
    - SYSTEM
    - Administrators
    - DOMAIN\User
    - group@DOMAIN.COM
    action: remove

- name: Remove all accounts who cannot log on remote interactively
  ansible.windows.win_user_right:
    name: SeDenyRemoteInteractiveLogonRight
    users: []
```

## [Return Values](win_user_right_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **added**  list / elements=string | A list of accounts that were added to the right, this is empty if no accounts were added.  Returned: success  Sample: `["NT AUTHORITY\\SYSTEM", "DOMAIN\\User"]` |
| **removed**  list / elements=string | A list of accounts that were removed from the right, this is empty if no accounts were removed.  Returned: success  Sample: `["SERVERNAME\\Administrator", "BUILTIN\\Administrators"]` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
