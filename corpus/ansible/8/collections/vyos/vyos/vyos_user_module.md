---
collection: ansible
version: "8"
title: "vyos.vyos.vyos_user module – Manage the collection of local users on VyOS device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vyos/vyos/vyos_user_module.html
fetched_at: 2026-07-28T02:59:28+00:00
---
# vyos.vyos.vyos_user module – Manage the collection of local users on VyOS device

> **Note:**
>
> This module is part of the [vyos.vyos collection](https://galaxy.ansible.com/ui/repo/published/vyos/vyos/) (version 4.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vyos.vyos`.
>
> To use it in a playbook, specify: `vyos.vyos.vyos_user`.

New in vyos.vyos 1.0.0

- [Synopsis](vyos_user_module.md#synopsis)
- [Parameters](vyos_user_module.md#parameters)
- [Notes](vyos_user_module.md#notes)
- [Examples](vyos_user_module.md#examples)
- [Return Values](vyos_user_module.md#return-values)

## [Synopsis](vyos_user_module.md#id1)

- This module provides declarative management of the local usernames configured on network devices. It allows playbooks to manage either individual usernames or the collection of usernames in the current running config. It also supports purging usernames from the configuration that are not explicitly defined.

Aliases: user

## [Parameters](vyos_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  aliases: users, collection  list / elements=dictionary | The set of username objects to be configured on the remote VyOS device. The list entries can either be the username or a hash of username and properties. This argument is mutually exclusive with the `name` argument. |
| **configured_password**  string | The password to be configured on the VyOS device. The password needs to be provided in clear and it will be encrypted on the device. |
| **full_name**  string | The `full_name` argument provides the full name of the user account to be created on the remote device. This argument accepts any text string value. |
| **level**  aliases: role  string | The `level` argument configures the level of the user when logged into the system. This argument accepts string values admin or operator. |
| **name**  string / required | The username to be configured on the VyOS device. This argument accepts a string value and is mutually exclusive with the `aggregate` argument. |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  **Choices:**   - `"present"` - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  **Choices:**   - `"on_create"` - `"always"` |
| **configured_password**  string | The password to be configured on the VyOS device. The password needs to be provided in clear and it will be encrypted on the device. |
| **full_name**  string | The `full_name` argument provides the full name of the user account to be created on the remote device. This argument accepts any text string value. |
| **level**  aliases: role  string | The `level` argument configures the level of the user when logged into the system. This argument accepts string values admin or operator. |
| **name**  string | The username to be configured on the VyOS device. This argument accepts a string value and is mutually exclusive with the `aggregate` argument. |
| **purge**  boolean | Instructs the module to consider the resource definition absolute. It will remove any previously configured usernames on the device with the exception of the `admin` user (the current defined set of users).  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  **Choices:**   - `"on_create"` - `"always"` ← (default) |

## [Notes](vyos_user_module.md#id3)

> **Note:**
>
> - Tested against VyOS 1.1.8 (helium).
> - This module works with connection `ansible.netcommon.network_cli`. See [the VyOS OS Platform Options](../network/user_guide/platform_vyos.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`

## [Examples](vyos_user_module.md#id4)

```yaml+jinja
- name: create a new user
  vyos.vyos.vyos_user:
    name: ansible
    configured_password: password
    state: present
- name: remove all users except admin
  vyos.vyos.vyos_user:
    purge: yes
- name: set multiple users to level operator
  vyos.vyos.vyos_user:
    aggregate:
    - name: netop
    - name: netend
    level: operator
    state: present
- name: Change Password for User netop
  vyos.vyos.vyos_user:
    name: netop
    configured_password: '{{ new_password }}'
    update_password: always
    state: present
```

## [Return Values](vyos_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["set system login user test level operator", "set system login user authentication plaintext-password password"]` |

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vyos.vyos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/vyos.vyos)
