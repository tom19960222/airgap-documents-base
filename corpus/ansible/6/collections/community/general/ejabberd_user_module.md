---
collection: ansible
version: "6"
title: "community.general.ejabberd_user module – Manages users for ejabberd servers"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ejabberd_user_module.html
fetched_at: 2026-07-27T17:08:50+00:00
---
# community.general.ejabberd_user module – Manages users for ejabberd servers

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](ejabberd_user_module.md#ansible-collections-community-general-ejabberd-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ejabberd_user`.

- [Synopsis](ejabberd_user_module.md#synopsis)
- [Requirements](ejabberd_user_module.md#requirements)
- [Parameters](ejabberd_user_module.md#parameters)
- [Notes](ejabberd_user_module.md#notes)
- [Examples](ejabberd_user_module.md#examples)

## [Synopsis](ejabberd_user_module.md#id1)

- This module provides user management for ejabberd servers

## [Requirements](ejabberd_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- ejabberd with mod_admin_extra

## [Parameters](ejabberd_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **host**  string / required | the ejabberd host associated with this username |
| **logging**  boolean | enables or disables the local syslog facility for this module  Choices:   - `false` ← (default) - `true` |
| **password**  string | the password to assign to the username |
| **state**  string | describe the desired state of the user to be managed  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | the name of the user to manage |

## [Notes](ejabberd_user_module.md#id4)

> **Note:**
>
> - Password parameter is required for state == present only
> - Passwords must be stored in clear text for this release
> - The ejabberd configuration file must include mod_admin_extra as a module.

## [Examples](ejabberd_user_module.md#id5)

```yaml+jinja
# Example playbook entries using the ejabberd_user module to manage users state.

- name: Create a user if it does not exist
  community.general.ejabberd_user:
    username: test
    host: server
    password: password

- name: Delete a user if it exists
  community.general.ejabberd_user:
    username: test
    host: server
    state: absent
```

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
