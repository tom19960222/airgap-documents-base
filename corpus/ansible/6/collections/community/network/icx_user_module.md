---
collection: ansible
version: "6"
title: "community.network.icx_user module – Manage the user accounts on Ruckus ICX 7000 series switches."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/icx_user_module.html
fetched_at: 2026-07-27T17:18:49+00:00
---
# community.network.icx_user module – Manage the user accounts on Ruckus ICX 7000 series switches.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.icx_user`.

- [Synopsis](icx_user_module.md#synopsis)
- [Parameters](icx_user_module.md#parameters)
- [Notes](icx_user_module.md#notes)
- [Examples](icx_user_module.md#examples)
- [Return Values](icx_user_module.md#return-values)

## [Synopsis](icx_user_module.md#id1)

- This module creates or updates user account on network devices. It allows playbooks to manage either individual usernames or the aggregate of usernames in the current running config. It also supports purging usernames from the configuration that are not explicitly defined.

## [Parameters](icx_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_time**  string | This parameter indicates the time the file’s access time should be set to. Should be preserve when no modification is required, YYYYMMDDHHMM.SS when using default time format, or now. Default is None meaning that preserve is the default for state=[file,directory,link,hard] and now is default for state=touch |
| **aggregate**  aliases: users, collection  list / elements=dictionary | The set of username objects to be configured on the remote ICX device. The list entries can either be the username or a hash of username and properties. This argument is mutually exclusive with the `name` argument. |
| **access_time**  string | This parameter indicates the time the file’s access time should be set to. Should be preserve when no modification is required, YYYYMMDDHHMM.SS when using default time format, or now. Default is None meaning that preserve is the default for state=[file,directory,link,hard] and now is default for state=touch |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  Choices:   - `false` - `true` |
| **configured_password**  string | The password to be configured on the ICX device. |
| **name**  string / required | The username to be configured on the ICX device. |
| **nopassword**  boolean | Defines the username without assigning a password. This will allow the user to login to the system without being authenticated by a password.  Choices:   - `false` - `true` |
| **privilege**  string | The privilege level to be granted to the user  Choices:   - `"0"` - `"4"` - `"5"` |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  Choices:   - `"present"` - `"absent"` |
| **update_password**  string | This argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  Choices:   - `"on_create"` - `"always"` |
| **check_running_config**  boolean | Check running configuration. This can be set as environment variable. Module will use environment variable value(default:True), unless it is overridden, by specifying it as module parameter.  Choices:   - `false` - `true` ← (default) |
| **configured_password**  string | The password to be configured on the ICX device. |
| **name**  string / required | The username to be configured on the ICX device. |
| **nopassword**  boolean | Defines the username without assigning a password. This will allow the user to login to the system without being authenticated by a password.  Choices:   - `false` ← (default) - `true` |
| **privilege**  string | The privilege level to be granted to the user  Choices:   - `"0"` - `"4"` - `"5"` |
| **purge**  boolean | If set to true module will remove any previously configured usernames on the device except the current defined set of users.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | This argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  Choices:   - `"on_create"` - `"always"` ← (default) |

## [Notes](icx_user_module.md#id3)

> **Note:**
>
> - Tested against ICX 10.1.
> - For information on using ICX platform, see [the ICX OS Platform Options guide](user_guide/platform_icx.md).

## [Examples](icx_user_module.md#id4)

```yaml+jinja
- name: Create a new user without password
  community.network.icx_user:
    name: user1
    nopassword: true

- name: Create a new user with password
  community.network.icx_user:
    name: user1
    configured_password: 'newpassword'

- name: Remove users
  community.network.icx_user:
    name: user1
    state: absent

- name: Set user privilege level to 5
  community.network.icx_user:
    name: user1
    privilege: 5
```

## [Return Values](icx_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["username ansible nopassword", "username ansible password-string alethea123", "no username ansible", "username ansible privilege 5", "username ansible enable"]` |

### Authors

- Ruckus Wireless (@Commscope)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
