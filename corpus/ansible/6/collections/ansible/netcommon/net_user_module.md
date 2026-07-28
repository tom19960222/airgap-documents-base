---
collection: ansible
version: "6"
title: "ansible.netcommon.net_user module – (deprecated, removed after 2022-06-01) Manage the aggregate of local users on network device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/netcommon/net_user_module.html
fetched_at: 2026-07-27T16:44:33+00:00
---
# ansible.netcommon.net_user module – (deprecated, removed after 2022-06-01) Manage the aggregate of local users on network device

> **Note:**
>
> This module is part of the [ansible.netcommon collection](https://galaxy.ansible.com/ansible/netcommon) (version 3.1.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.netcommon`.
>
> To use it in a playbook, specify: `ansible.netcommon.net_user`.

New in ansible.netcommon 1.0.0

- [DEPRECATED](net_user_module.md#deprecated)
- [Synopsis](net_user_module.md#synopsis)
- [Parameters](net_user_module.md#parameters)
- [Notes](net_user_module.md#notes)
- [Examples](net_user_module.md#examples)
- [Return Values](net_user_module.md#return-values)
- [Status](net_user_module.md#status)

## [DEPRECATED](net_user_module.md#id1)

Removed in:
:   major release after 2022-06-01

Why:
:   Updated modules released with more functionality

Alternative:
:   Use platform-specific “[netos]_user” module

## [Synopsis](net_user_module.md#id2)

- This module provides declarative management of the local usernames configured on network devices. It allows playbooks to manage either individual usernames or the aggregate of usernames in the current running config. It also supports purging usernames from the configuration that are not explicitly defined.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](net_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aggregate**  string | The set of username objects to be configured on the remote network device. The list entries can either be the username or a hash of username and properties. This argument is mutually exclusive with the `name` argument. |
| **configured_password**  string | The password to be configured on the remote network device. The password needs to be provided in clear and it will be encrypted on the device. Please note that this option is not same as `provider password`. |
| **name**  string | The username to be configured on the remote network device. This argument accepts a string value and is mutually exclusive with the `aggregate` argument. Please note that this option is not same as `provider username`. |
| **nopassword**  boolean | Defines the username without assigning a password. This will allow the user to login to the system without being authenticated by a password.  Choices:   - `false` - `true` |
| **privilege**  string | The `privilege` argument configures the privilege level of the user when logged into the system. This argument accepts integer values in the range of 1 to 15. |
| **purge**  boolean | Instructs the module to consider the resource definition absolute. It will remove any previously configured usernames on the device with the exception of the `admin` user (the current defined set of users).  Choices:   - `false` ← (default) - `true` |
| **role**  string | Configures the role for the username in the device running configuration. The argument accepts a string value defining the role name. This argument does not check if the role has been configured on the device. |
| **sshkey**  string | Specifies the SSH public key to configure for the given username. This argument accepts a valid SSH key value. |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  Choices:   - `"on_create"` - `"always"` ← (default) |

## [Notes](net_user_module.md#id4)

> **Note:**
>
> - This module is supported on `ansible_network_os` network platforms. See the :ref:`Network Platform Options <platform_options>` for details.

## [Examples](net_user_module.md#id5)

```yaml+jinja
- name: create a new user
  ansible.netcommon.net_user:
    name: ansible
    sshkey: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
    state: present

- name: remove all users except admin
  ansible.netcommon.net_user:
    purge: yes

- name: set multiple users to privilege level 15
  ansible.netcommon.net_user:
    aggregate:
    - {name: netop}
    - {name: netend}
    privilege: 15
    state: present

- name: Change Password for User netop
  ansible.netcommon.net_user:
    name: netop
    configured_password: '{{ new_password }}'
    update_password: always
    state: present
```

## [Return Values](net_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["username ansible secret password", "username admin secret admin"]` |

## [Status](net_user_module.md#id7)

- This module will be removed in a major release after 2022-06-01.
  *[deprecated]*
- For more information see [DEPRECATED](net_user_module.md#deprecated).

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/ansible.netcommon/issues)
[Repository (Sources)](https://github.com/ansible-collections/ansible.netcommon)
