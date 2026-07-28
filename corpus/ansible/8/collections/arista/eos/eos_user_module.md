---
collection: ansible
version: "8"
title: "arista.eos.eos_user module – Manage the collection of local users on EOS devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/arista/eos/eos_user_module.html
fetched_at: 2026-07-28T01:11:17+00:00
---
# arista.eos.eos_user module – Manage the collection of local users on EOS devices

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/ui/repo/published/arista/eos/) (version 6.2.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install arista.eos`.
>
> To use it in a playbook, specify: `arista.eos.eos_user`.

New in arista.eos 1.0.0

- [Synopsis](eos_user_module.md#synopsis)
- [Parameters](eos_user_module.md#parameters)
- [Notes](eos_user_module.md#notes)
- [Examples](eos_user_module.md#examples)
- [Return Values](eos_user_module.md#return-values)

## [Synopsis](eos_user_module.md#id1)

- This module provides declarative management of the local usernames configured on Arista EOS devices. It allows playbooks to manage either individual usernames or the collection of usernames in the current running config. It also supports purging usernames from the configuration that are not explicitly defined.

Aliases: user

## [Parameters](eos_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  aliases: users, collection  list / elements=dictionary | The set of username objects to be configured on the remote Arista EOS device. The list entries can either be the username or a hash of username and properties. This argument is mutually exclusive with the `username` argument. |
| **configured_password**  string | The password to be configured on the remote Arista EOS device. The password needs to be provided in clear and it will be encrypted on the device. |
| **name**  string | The username to be configured on the remote Arista EOS device. This argument accepts a stringv value and is mutually exclusive with the `aggregate` argument. |
| **nopassword**  boolean | Defines the username without assigning a password. This will allow the user to login to the system without being authenticated by a password.  **Choices:**   - `false` - `true` |
| **privilege**  integer | The `privilege` argument configures the privilege level of the user when logged into the system. This argument accepts integer values in the range of 1 to 15. |
| **role**  string | Configures the role for the username in the device running configuration. The argument accepts a string value defining the role name. This argument does not check if the role has been configured on the device. |
| **sshkey**  string | Specifies the SSH public key to configure for the given username. This argument accepts a valid SSH key value. |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  **Choices:**   - `"present"` - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  **Choices:**   - `"on_create"` - `"always"` |
| **configured_password**  string | The password to be configured on the remote Arista EOS device. The password needs to be provided in clear and it will be encrypted on the device. |
| **name**  string | The username to be configured on the remote Arista EOS device. This argument accepts a stringv value and is mutually exclusive with the `aggregate` argument. |
| **nopassword**  boolean | Defines the username without assigning a password. This will allow the user to login to the system without being authenticated by a password.  **Choices:**   - `false` - `true` |
| **privilege**  integer | The `privilege` argument configures the privilege level of the user when logged into the system. This argument accepts integer values in the range of 1 to 15. |
| **purge**  boolean | Instructs the module to consider the resource definition absolute. It will remove any previously configured usernames on the device with the exception of the `admin` user which cannot be deleted per EOS constraints.  **Choices:**   - `false` ← (default) - `true` |
| **role**  string | Configures the role for the username in the device running configuration. The argument accepts a string value defining the role name. This argument does not check if the role has been configured on the device. |
| **sshkey**  string | Specifies the SSH public key to configure for the given username. This argument accepts a valid SSH key value. |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  **Choices:**   - `"on_create"` - `"always"` ← (default) |

## [Notes](eos_user_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F

## [Examples](eos_user_module.md#id4)

```yaml+jinja
- name: create a new user
  arista.eos.eos_user:
    name: ansible
    sshkey: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
    state: present

- name: remove all users except admin
  arista.eos.eos_user:
    purge: true

- name: set multiple users to privilege level 15
  arista.eos.eos_user:
    aggregate:
      - name: netop
      - name: netend
    privilege: 15
    state: present

- name: Change Password for User netop
  arista.eos.eos_user:
    username: netop
    configured_password: '{{ new_password }}'
    update_password: always
    state: present
```

## [Return Values](eos_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["name ansible secret password", "name admin secret admin"]` |
| **session_name**  string | The EOS config session name used to load the configuration  **Returned:** when changed is True  **Sample:** `"ansible_1479315771"` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/arista.eos)
