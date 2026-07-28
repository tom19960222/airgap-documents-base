---
collection: ansible
version: "6"
title: "mellanox.onyx.onyx_username module – Configure username module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/mellanox/onyx/onyx_username_module.html
fetched_at: 2026-07-27T17:55:44+00:00
---
# mellanox.onyx.onyx_username module – Configure username module

> **Note:**
>
> This module is part of the [mellanox.onyx collection](https://galaxy.ansible.com/mellanox/onyx) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install mellanox.onyx`.
>
> To use it in a playbook, specify: `mellanox.onyx.onyx_username`.

New in mellanox.onyx 0.2.0

- [Synopsis](onyx_username_module.md#synopsis)
- [Parameters](onyx_username_module.md#parameters)
- [Examples](onyx_username_module.md#examples)
- [Return Values](onyx_username_module.md#return-values)

## [Synopsis](onyx_username_module.md#id1)

- This module provides declarative management of users/roles on Mellanox ONYX network devices.

## [Parameters](onyx_username_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **capability**  string | Grant capability to this user account  Choices:   - `"monitor"` - `"unpriv"` - `"v_admin"` - `"admin"` |
| **disabled**  string | Disable means of logging into this account  Choices:   - `"none"` - `"login"` - `"password"` - `"all"` |
| **disconnected**  boolean | Disconnect all sessions of this user  Choices:   - `false` ← (default) - `true` |
| **encrypted_password**  boolean | Decide the type of setted password (plain text or encrypted)  Choices:   - `false` ← (default) - `true` |
| **full_name**  string | Set the full name of this user |
| **nopassword**  boolean | Clear password for such user  Choices:   - `false` ← (default) - `true` |
| **password**  string | Set password fot such user |
| **reset_capability**  boolean | Reset capability to this user account  Choices:   - `false` ← (default) - `true` |
| **state**  string | Set state of the given account  Choices:   - `"present"` ← (default) - `"absent"` |
| **username**  string / required | Create/Edit user using username |

## [Examples](onyx_username_module.md#id3)

```yaml+jinja
- name: Create new user
  onyx_username:
      username: anass

- name: Set the user full-name
  onyx_username:
      username: anass
      full_name: anasshami

- name: Set the user encrypted password
  onyx_username:
      username: anass
      password: 12345
      encrypted_password: True

- name: Set the user capability
  onyx_username:
      username: anass
      capability: monitor

- name: Reset the user capability
  onyx_username:
      username: anass
      reset_capability: True

- name: Remove the user configuration
  onyx_username:
      username: anass
      state: absent
```

## [Return Values](onyx_username_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device.  Returned: always  Sample: `["username *", "username * password *", "username * nopassword", "username * disable login", "username * capability admin", "no username *", "no username * disable"]` |

### Authors

- Anas Shami (@anass)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/mellanox.onyx/issues)
[Repository (Sources)](https://github.com/ansible-collections/mellanox.onyx)
