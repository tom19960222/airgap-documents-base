---
collection: ansible
version: "6"
title: "community.windows.win_auto_logon module – Adds or Sets auto logon registry keys."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_auto_logon_module.html
fetched_at: 2026-07-27T17:23:10+00:00
---
# community.windows.win_auto_logon module – Adds or Sets auto logon registry keys.

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_auto_logon`.

- [Synopsis](win_auto_logon_module.md#synopsis)
- [Parameters](win_auto_logon_module.md#parameters)
- [Examples](win_auto_logon_module.md#examples)

## [Synopsis](win_auto_logon_module.md#id1)

- Used to apply auto logon registry setting.

## [Parameters](win_auto_logon_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **logon_count**  integer | The number of times to do an automatic logon.  This count is deremented by Windows everytime an automatic logon is performed.  Once the count reaches `0` then the automatic logon process is disabled. |
| **password**  string | Password to be used for automatic login.  Must be set when `state=present`.  Value of this input will be used as password for *username*.  While this value is encrypted by LSA it is decryptable to any user who is an Administrator on the remote host. |
| **state**  string | Whether the registry key should be `present` or `absent`.  Choices:   - `"absent"` - `"present"` ← (default) |
| **username**  string | Username to login automatically.  Must be set when `state=present`.  This can be the Netlogon or UPN of a domain account and is automatically parsed to the `DefaultUserName` and `DefaultDomainName` registry properties. |

## [Examples](win_auto_logon_module.md#id3)

```yaml+jinja
- name: Set autologon for user1
  community.windows.win_auto_logon:
    username: User1
    password: str0ngp@ssword

- name: Set autologon for abc.com\user1
  community.windows.win_auto_logon:
    username: abc.com\User1
    password: str0ngp@ssword

- name: Remove autologon for user1
  community.windows.win_auto_logon:
    state: absent

- name: Set autologon for user1 with a limited logon count
  community.windows.win_auto_logon:
    username: User1
    password: str0ngp@ssword
    logon_count: 5
```

### Authors

- Prasoon Karunan V (@prasoonkarunan)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
