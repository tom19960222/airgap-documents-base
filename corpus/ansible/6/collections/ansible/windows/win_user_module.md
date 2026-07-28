---
collection: ansible
version: "6"
title: "ansible.windows.win_user module – Manages local Windows user accounts"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/windows/win_user_module.html
fetched_at: 2026-07-27T16:45:05+00:00
---
# ansible.windows.win_user module – Manages local Windows user accounts

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
> To use it in a playbook, specify: `ansible.windows.win_user`.

- [Synopsis](win_user_module.md#synopsis)
- [Parameters](win_user_module.md#parameters)
- [Notes](win_user_module.md#notes)
- [See Also](win_user_module.md#see-also)
- [Examples](win_user_module.md#examples)
- [Return Values](win_user_module.md#return-values)

## [Synopsis](win_user_module.md#id1)

- Manages local Windows user accounts.
- For non-Windows targets, use the [ansible.builtin.user](../builtin/user_module.md#ansible-collections-ansible-builtin-user-module) module instead.

## [Parameters](win_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **account_disabled**  boolean | `yes` will disable the user account.  `no` will clear the disabled flag.  Choices:   - `false` - `true` |
| **account_locked**  boolean | Only `no` can be set and it will unlock the user account if locked.  Choices:   - `false` - `true` |
| **description**  string | Description of the user. |
| **fullname**  string | Full name of the user. |
| **groups**  list / elements=string | Adds or removes the user from this comma-separated list of groups, depending on the value of *groups_action*.  When *groups_action* is `replace` and *groups* is set to the empty string (‘groups=’), the user is removed from all groups.  Since `ansible.windows v1.5.0` it is possible to specify a group using it’s security identifier. |
| **groups_action**  string | If `add`, the user is added to each group in *groups* where not already a member.  If `replace`, the user is added as a member of each group in *groups* and removed from any other groups.  If `remove`, the user is removed from each group in *groups*.  Choices:   - `"add"` - `"replace"` ← (default) - `"remove"` |
| **home_directory**  string  added in ansible.windows 1.0.0 | The designated home directory of the user. |
| **login_script**  string  added in ansible.windows 1.0.0 | The login script of the user. |
| **name**  string / required | Name of the user to create, remove or modify. |
| **password**  string | Optionally set the user’s password to this (plain text) value. |
| **password_expired**  boolean | `yes` will require the user to change their password at next login.  `no` will clear the expired password flag.  Choices:   - `false` - `true` |
| **password_never_expires**  boolean | `yes` will set the password to never expire.  `no` will allow the password to expire.  Choices:   - `false` - `true` |
| **profile**  string  added in ansible.windows 1.0.0 | The profile path of the user. |
| **state**  string | When `absent`, removes the user account if it exists.  When `present`, creates or updates the user account.  When `query`, retrieves the user account details without making any changes.  Choices:   - `"absent"` - `"present"` ← (default) - `"query"` |
| **update_password**  string | `always` will update passwords if they differ.  `on_create` will only set the password for newly created users.  Choices:   - `"always"` ← (default) - `"on_create"` |
| **user_cannot_change_password**  boolean | `yes` will prevent the user from changing their password.  `no` will allow the user to change their password.  Choices:   - `false` - `true` |

## [Notes](win_user_module.md#id3)

> **Note:**
>
> - The return values are based on the user object after the module options have been set. When running in check mode the values will still reflect the existing user settings and not what they would have been changed to.

## [See Also](win_user_module.md#id4)

> **See also:**
>
> [ansible.builtin.user](../builtin/user_module.md#ansible-collections-ansible-builtin-user-module)
> :   Manage user accounts.
>
> [ansible.windows.win_domain_membership](win_domain_membership_module.md#ansible-collections-ansible-windows-win-domain-membership-module)
> :   Manage domain/workgroup membership for a Windows host.
>
> [community.windows.win_domain_user](../../community/windows/win_domain_user_module.md#ansible-collections-community-windows-win-domain-user-module)
> :   Manages Windows Active Directory user accounts.
>
> [ansible.windows.win_group](win_group_module.md#ansible-collections-ansible-windows-win-group-module)
> :   Add and remove local groups.
>
> [ansible.windows.win_group_membership](win_group_membership_module.md#ansible-collections-ansible-windows-win-group-membership-module)
> :   Manage Windows local group membership.
>
> [community.windows.win_user_profile](../../community/windows/win_user_profile_module.md#ansible-collections-community-windows-win-user-profile-module)
> :   Manages the Windows user profiles.

## [Examples](win_user_module.md#id5)

```yaml+jinja
- name: Ensure user bob is present
  ansible.windows.win_user:
    name: bob
    password: B0bP4ssw0rd
    state: present
    groups:
      - Users

- name: Ensure user bob is absent
  ansible.windows.win_user:
    name: bob
    state: absent
```

## [Return Values](win_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **account_disabled**  boolean | Whether the user is disabled.  Returned: user exists  Sample: `false` |
| **account_locked**  boolean | Whether the user is locked.  Returned: user exists  Sample: `false` |
| **description**  string | The description set for the user.  Returned: user exists  Sample: `"Username for test"` |
| **fullname**  string | The full name set for the user.  Returned: user exists  Sample: `"Test Username"` |
| **groups**  list / elements=string | A list of groups and their ADSI path the user is a member of.  Returned: user exists  Sample: `[{"name": "Administrators", "path": "WinNT://WORKGROUP/USER-PC/Administrators"}]` |
| **name**  string | The name of the user  Returned: always  Sample: `"username"` |
| **password_expired**  boolean | Whether the password is expired.  Returned: user exists  Sample: `false` |
| **password_never_expires**  boolean | Whether the password is set to never expire.  Returned: user exists  Sample: `true` |
| **path**  string | The ADSI path for the user.  Returned: user exists  Sample: `"WinNT://WORKGROUP/USER-PC/username"` |
| **sid**  string | The SID for the user.  Returned: user exists  Sample: `"S-1-5-21-3322259488-2828151810-3939402796-1001"` |
| **user_cannot_change_password**  boolean | Whether the user can change their own password.  Returned: user exists  Sample: `false` |

### Authors

- Paul Durivage (@angstwad)
- Chris Church (@cchurch)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
[Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
[Communication](index.md#communication-for-ansible-windows)
