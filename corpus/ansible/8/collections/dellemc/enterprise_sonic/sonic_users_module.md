---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_users module – Manage users and its parameters"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_users_module.html
fetched_at: 2026-07-28T02:03:51+00:00
---
# dellemc.enterprise_sonic.sonic_users module – Manage users and its parameters

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_users`.

New in dellemc.enterprise_sonic 1.1.0

- [Synopsis](sonic_users_module.md#synopsis)
- [Parameters](sonic_users_module.md#parameters)
- [Notes](sonic_users_module.md#notes)
- [Examples](sonic_users_module.md#examples)
- [Return Values](sonic_users_module.md#return-values)

## [Synopsis](sonic_users_module.md#id1)

- This module provides configuration management of users parameters on devices running Enterprise SONiC.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_users_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary | Specifies the users related configuration. |
| **name**  string / required | Specifies the name of the user. |
| **password**  string | Specifies the password of the user. |
| **role**  string | Specifies the role of the user.  **Choices:**   - `"admin"` - `"operator"` - `"netadmin"` - `"secadmin"` |
| **update_password**  string | Specifies the update password flag.  In case of always, password will be updated every time.  In case of on_create, password will be updated only when user is created.  **Choices:**   - `"always"` ← (default) - `"on_create"` |
| **state**  string | Specifies the operation to be performed on the users configured on the device.  In case of merged, the input configuration will be merged with the existing users configuration on the device.  In case of deleted the existing users configuration will be removed from the device.  In case of replaced, the existing specified user configuration will be replaced with provided configuration.  In case of overridden, the existing users configuration will be overridden with the provided configuration.  **Choices:**   - `"merged"` ← (default) - `"deleted"` - `"overridden"` - `"replaced"` |

## [Notes](sonic_users_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_users_module.md#id4)

```yaml+jinja
# Using deleted
#
# Before state:
# -------------
#
# sonic# show users configured
# ----------------------------------------------------------------------
# User                              Role(s)
# ----------------------------------------------------------------------
# admin                             admin
# sysadmin                          admin
# sysoperator                       operator

- name: Delete user
  dellemc.enterprise_sonic.sonic_users:
    config:
      - name: sysoperator
    state: deleted

# After state:
# ------------
#
# sonic# show users configured
# ----------------------------------------------------------------------
# User                              Role(s)
# ----------------------------------------------------------------------
# admin                             admin
# sysadmin                          admin

# Using deleted
#
# Before state:
# -------------
#
# sonic# show users configured
# ----------------------------------------------------------------------
# User                              Role(s)
# ----------------------------------------------------------------------
# admin                             admin
# sysadmin                          admin
# sysoperator                       operator

- name: Delete all users configurations except admin
  dellemc.enterprise_sonic.sonic_users:
    config:
    state: deleted

# After state:
# ------------
#
# sonic# show users configured
# ----------------------------------------------------------------------
# User                              Role(s)
# ----------------------------------------------------------------------
# admin                             admin

# Using merged
#
# Before state:
# -------------
#
# sonic# show users configured
# ----------------------------------------------------------------------
# User                              Role(s)
# ----------------------------------------------------------------------
# admin                             admin

- name: Merge users configurations
  dellemc.enterprise_sonic.sonic_users:
    config:
      - name: sysadmin
        role: admin
        password: admin
        update_password: always
      - name: sysoperator
        role: operator
        password: operator
        update_password: always
    state: merged

# After state:
# ------------
#
# sonic# show users configured
# ----------------------------------------------------------------------
# User                              Role(s)
# ----------------------------------------------------------------------
# admin                             admin
# sysadmin                          admin
# sysoperator                       operator

# Using Overridden
#
# Before state:
# -------------
#
# sonic# show users configured
# ----------------------------------------------------------------------
# User                              Role(s)
# ----------------------------------------------------------------------
# admin                             admin
# sysadmin                          admin
# sysoperator                       operator

- name: Override users configurations
  dellemc.enterprise_sonic.sonic_users:
    config:
      - name: user1
        role: secadmin
        password: 123abc
        update_password: always
    state: overridden

# After state:
# ------------
#
# sonic# show users configured
# ----------------------------------------------------------------------
# User                              Role(s)
# ----------------------------------------------------------------------
# admin                             admin
# user1                             secadmin

# Using Replaced
#
# Before state:
# -------------
#
# sonic# show users configured
# ----------------------------------------------------------------------
# User                              Role(s)
# ----------------------------------------------------------------------
# admin                             admin
# user1                             secadmin
# user2                             operator

- name: Replace users configurations
  dellemc.enterprise_sonic.sonic_users:
    config:
      - name: user1
        role: operator
        password: 123abc
        update_password: always
      - name: user2
        role: netadmin
        password: 123abc
        update_password: always
    state: replaced

# After state:
# ------------
#
# sonic# show users configured
# ----------------------------------------------------------------------
# User                              Role(s)
# ----------------------------------------------------------------------
# admin                             admin
# user1                             operator
# user2                             netadmin
```

## [Return Values](sonic_users_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **after**  list / elements=string | The resulting configuration model invocation.  **Returned:** when changed  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **before**  list / elements=string | The configuration prior to the model invocation.  **Returned:** always  **Sample:** `["The configuration returned will always be in the same format\n of the parameters above.\n"]` |
| **commands**  list / elements=string | The set of commands pushed to the remote device.  **Returned:** always  **Sample:** `["command 1", "command 2", "command 3"]` |

### Authors

- Niraimadaiselvam M (@niraimadaiselvamm)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
