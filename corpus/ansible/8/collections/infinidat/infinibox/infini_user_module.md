---
collection: ansible
version: "8"
title: "infinidat.infinibox.infini_user module – Create, Delete and Modify a User on Infinibox"
source_url: https://docs.ansible.com/projects/ansible/8/collections/infinidat/infinibox/infini_user_module.html
fetched_at: 2026-07-28T02:35:52+00:00
---
# infinidat.infinibox.infini_user module – Create, Delete and Modify a User on Infinibox

> **Note:**
>
> This module is part of the [infinidat.infinibox collection](https://galaxy.ansible.com/ui/repo/published/infinidat/infinibox/) (version 1.3.12).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install infinidat.infinibox`.
> You need further requirements to be able to use this module,
> see [Requirements](infini_user_module.md#ansible-collections-infinidat-infinibox-infini-user-module-requirements) for details.
>
> To use it in a playbook, specify: `infinidat.infinibox.infini_user`.

New in infinidat.infinibox 2.9.0

- [Synopsis](infini_user_module.md#synopsis)
- [Requirements](infini_user_module.md#requirements)
- [Parameters](infini_user_module.md#parameters)
- [Notes](infini_user_module.md#notes)
- [Examples](infini_user_module.md#examples)

## [Synopsis](infini_user_module.md#id1)

- This module creates, deletes or modifies a user on Infinibox.

## [Requirements](infini_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python2 >= 2.7 or python3 >= 3.6
- infinisdk (<https://infinisdk.readthedocs.io/en/latest/>)

## [Parameters](infini_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **password**  string / required | Infinibox User password. |
| **state**  string | Creates/Modifies user when present or removes when absent  **Choices:**   - `"stat"` - `"reset_password"` - `"present"` ← (default) - `"absent"` |
| **system**  string / required | Infinibox Hostname or IPv4 Address. |
| **user**  string / required | Infinibox User username with sufficient priveledges ( see notes ). |
| **user_email**  string | The new user’s Email address |
| **user_enabled**  boolean | Specify whether to enable the user  **Choices:**   - `false` - `true` ← (default) |
| **user_name**  string / required | The new user’s Name. Once a user is created, the user_name may not be changed from this module. It may be changed from the UI or from infinishell. |
| **user_password**  string | The new user’s password |
| **user_pool**  string | Use with role==pool_admin. Specify the new user’s pool. |
| **user_role**  string | The user’s role  **Choices:**   - `"admin"` - `"pool_admin"` - `"read_only"` |

## [Notes](infini_user_module.md#id4)

> **Note:**
>
> - This module requires infinisdk python library
> - You must set INFINIBOX_USER and INFINIBOX_PASSWORD environment variables if user and password arguments are not passed to the module directly
> - Ansible uses the infinisdk configuration file `~/.infinidat/infinisdk.ini` if no credentials are provided. See <http://infinisdk.readthedocs.io/en/latest/getting_started.html>
> - All Infinidat modules support check mode (–check). However, a dryrun that creates resources may fail if the resource dependencies are not met for a task. For example, consider a task that creates a volume in a pool. If the pool does not exist, the volume creation task will fail. It will fail even if there was a previous task in the playbook that would have created the pool but did not because the pool creation was also part of the dry run.

## [Examples](infini_user_module.md#id5)

```yaml+jinja
- name: Create new user
  infini_user:
    user_name: foo_user
    user_email: foo@example.com
    user_password: secret2
    user_role: pool_admin
    user_enabled: false
    pool: foo_pool
    state: present
    password: secret1
    system: ibox001
```

### Authors

- David Ohlemacher (@ohlemacher)

### Collection links

- [Issue Tracker](https://www.github.com/infinidat/ansible-infinidat-collection/issues)
- [Repository (Sources)](https://www.github.com/infinidat/ansible-infinidat-collection)
