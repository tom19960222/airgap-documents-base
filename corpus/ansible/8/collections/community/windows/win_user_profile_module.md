---
collection: ansible
version: "8"
title: "community.windows.win_user_profile module – Manages the Windows user profiles."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_user_profile_module.html
fetched_at: 2026-07-28T02:02:33+00:00
---
# community.windows.win_user_profile module – Manages the Windows user profiles.

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
> To use it in a playbook, specify: `community.windows.win_user_profile`.

- [Synopsis](win_user_profile_module.md#synopsis)
- [Parameters](win_user_profile_module.md#parameters)
- [See Also](win_user_profile_module.md#see-also)
- [Examples](win_user_profile_module.md#examples)
- [Return Values](win_user_profile_module.md#return-values)

## [Synopsis](win_user_profile_module.md#id1)

- Used to create or remove user profiles on a Windows host.
- This can be used to create a profile before a user logs on or delete a profile when removing a user account.
- A profile can be created for both a local or domain account.

## [Parameters](win_user_profile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **name**  string | Specifies the base name for the profile path.  When *state* is `present` this is used to create the profile for *username* at a specific path within the profile directory.  This cannot be used to specify a path outside of the profile directory but rather it specifies a folder(s) within this directory.  If a profile for another user already exists at the same path, then a 3 digit incremental number is appended by Windows automatically.  When *state* is `absent` and *username* is not set, then the module will remove all profiles that point to the profile path derived by this value.  This is useful if the account no longer exists but the profile still remains. |
| **remove_multiple**  boolean | When *state* is `absent` and the value for *name* matches multiple profiles the module will fail.  Set this value to `yes` to force the module to delete all the profiles found.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Will ensure the profile exists when set to `present`.  When creating a profile the *username* option must be set to a valid account.  Will remove the profile(s) when set to `absent`.  When removing a profile either *username* must be set to a valid account, or *name* is set to the profile’s base name.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **username**  sid | The account name of security identifier (SID) for the profile.  This must be set when *state* is `present` and must be a valid account or the SID of a valid account.  When *state* is `absent` then this must still be a valid account number but the SID can be a deleted user’s SID. |

## [See Also](win_user_profile_module.md#id3)

> **See also:**
>
> [ansible.windows.win_user](../../ansible/windows/win_user_module.md#ansible-collections-ansible-windows-win-user-module)
> :   Manages local Windows user accounts.
>
> [community.windows.win_domain_user](win_domain_user_module.md#ansible-collections-community-windows-win-domain-user-module)
> :   Manages Windows Active Directory user accounts.

## [Examples](win_user_profile_module.md#id4)

```yaml+jinja
- name: Create a profile for an account
  community.windows.win_user_profile:
    username: ansible-account
    state: present

- name: Create a profile for an account at C:\Users\ansible
  community.windows.win_user_profile:
    username: ansible-account
    name: ansible
    state: present

- name: Remove a profile for a still valid account
  community.windows.win_user_profile:
    username: ansible-account
    state: absent

- name: Remove a profile for a deleted account
  community.windows.win_user_profile:
    name: ansible
    state: absent

- name: Remove a profile for a deleted account based on the SID
  community.windows.win_user_profile:
    username: S-1-5-21-3233007181-2234767541-1895602582-1305
    state: absent

- name: Remove multiple profiles that exist at the basename path
  community.windows.win_user_profile:
    name: ansible
    state: absent
    remove_multiple: yes
```

## [Return Values](win_user_profile_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **path**  string | The full path to the profile for the account. This will be null if `state=absent` and no profile was deleted.  **Returned:** always  **Sample:** `"C:\\Users\\ansible"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
