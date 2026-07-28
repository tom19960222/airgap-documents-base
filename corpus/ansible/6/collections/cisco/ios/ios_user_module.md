---
collection: ansible
version: "6"
title: "cisco.ios.ios_user module – Module to manage the aggregates of local users."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/ios/ios_user_module.html
fetched_at: 2026-07-27T16:55:31+00:00
---
# cisco.ios.ios_user module – Module to manage the aggregates of local users.

> **Note:**
>
> This module is part of the [cisco.ios collection](https://galaxy.ansible.com/cisco/ios) (version 3.3.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ios`.
>
> To use it in a playbook, specify: `cisco.ios.ios_user`.

New in cisco.ios 1.0.0

- [Synopsis](ios_user_module.md#synopsis)
- [Parameters](ios_user_module.md#parameters)
- [Notes](ios_user_module.md#notes)
- [Examples](ios_user_module.md#examples)
- [Return Values](ios_user_module.md#return-values)

## [Synopsis](ios_user_module.md#id1)

- This module provides declarative management of the local usernames configured on network devices. It allows playbooks to manage either individual usernames or the aggregate of usernames in the current running config. It also supports purging usernames from the configuration that are not explicitly defined.

## [Parameters](ios_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  aliases: users, collection  list / elements=dictionary | The set of username objects to be configured on the remote Cisco IOS device. The list entries can either be the username or a hash of username and properties. This argument is mutually exclusive with the `name` argument. |
| **configured_password**  string | The password to be configured on the Cisco IOS device. The password needs to be provided in clear and it will be encrypted on the device. Please note that this option is not same as `provider password`. |
| **hashed_password**  dictionary | This option allows configuring hashed passwords on Cisco IOS devices. |
| **type**  integer / required | Specifies the type of hash (e.g., 5 for MD5, 8 for PBKDF2, etc.)  For this to work, the device needs to support the desired hash type |
| **value**  string / required | The actual hashed password to be configured on the device |
| **name**  string / required | The username to be configured on the Cisco IOS device. This argument accepts a string value and is mutually exclusive with the `aggregate` argument. Please note that this option is not same as `provider username`. |
| **nopassword**  boolean | Defines the username without assigning a password. This will allow the user to login to the system without being authenticated by a password.  Choices:   - `false` - `true` |
| **password_type**  string | This argument determines whether a ‘password’ or ‘secret’ will be configured.  Choices:   - `"secret"` - `"password"` |
| **privilege**  integer | The `privilege` argument configures the privilege level of the user when logged into the system. This argument accepts integer values in the range of 1 to 15. |
| **sshkey**  list / elements=string | Specifies one or more SSH public key(s) to configure for the given username.  This argument accepts a valid SSH key value. |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  Choices:   - `"present"` - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  Choices:   - `"on_create"` - `"always"` |
| **view**  aliases: role  string | Configures the view for the username in the device running configuration. The argument accepts a string value defining the view name. This argument does not check if the view has been configured on the device. |
| **configured_password**  string | The password to be configured on the Cisco IOS device. The password needs to be provided in clear and it will be encrypted on the device. Please note that this option is not same as `provider password`. |
| **hashed_password**  dictionary | This option allows configuring hashed passwords on Cisco IOS devices. |
| **type**  integer / required | Specifies the type of hash (e.g., 5 for MD5, 8 for PBKDF2, etc.)  For this to work, the device needs to support the desired hash type |
| **value**  string / required | The actual hashed password to be configured on the device |
| **name**  string | The username to be configured on the Cisco IOS device. This argument accepts a string value and is mutually exclusive with the `aggregate` argument. Please note that this option is not same as `provider username`. |
| **nopassword**  boolean | Defines the username without assigning a password. This will allow the user to login to the system without being authenticated by a password.  Choices:   - `false` - `true` |
| **password_type**  string | This argument determines whether a ‘password’ or ‘secret’ will be configured.  Choices:   - `"secret"` ← (default) - `"password"` |
| **privilege**  integer | The `privilege` argument configures the privilege level of the user when logged into the system. This argument accepts integer values in the range of 1 to 15. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>.   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **purge**  boolean | Instructs the module to consider the resource definition absolute. It will remove any previously configured usernames on the device with the exception of the `admin` user (the current defined set of users).  Choices:   - `false` ← (default) - `true` |
| **sshkey**  list / elements=string | Specifies one or more SSH public key(s) to configure for the given username.  This argument accepts a valid SSH key value. |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  Choices:   - `"on_create"` - `"always"` ← (default) |
| **view**  aliases: role  string | Configures the view for the username in the device running configuration. The argument accepts a string value defining the view name. This argument does not check if the view has been configured on the device. |

## [Notes](ios_user_module.md#id3)

> **Note:**
>
> - Tested against IOS 15.6
> - This module works with connection `network_cli`. See <https://docs.ansible.com/ansible/latest/network/user_guide/platform_ios.html>
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](ios_user_module.md#id4)

```yaml+jinja
- name: create a new user
  cisco.ios.ios_user:
    name: ansible
    nopassword: true
    sshkey: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
    state: present

- name: create a new user with multiple keys
  cisco.ios.ios_user:
    name: ansible
    sshkey:
    - "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
    - "{{ lookup('file', '~/path/to/public_key') }}"
    state: present

- name: remove all users except admin
  cisco.ios.ios_user:
    purge: yes

- name: remove all users except admin and these listed users
  cisco.ios.ios_user:
    aggregate:
    - name: testuser1
    - name: testuser2
    - name: testuser3
    purge: yes

- name: set multiple users to privilege level 15
  cisco.ios.ios_user:
    aggregate:
    - name: netop
    - name: netend
    privilege: 15
    state: present

- name: set user view/role
  cisco.ios.ios_user:
    name: netop
    view: network-operator
    state: present

- name: Change Password for User netop
  cisco.ios.ios_user:
    name: netop
    configured_password: '{{ new_password }}'
    update_password: always
    state: present

- name: Aggregate of users
  cisco.ios.ios_user:
    aggregate:
    - name: ansibletest2
    - name: ansibletest3
    view: network-admin

- name: Add a user specifying password type
  cisco.ios.ios_user:
    name: ansibletest4
    configured_password: '{{ new_password }}'
    password_type: password

- name: Add a user with MD5 hashed password
  cisco.ios.ios_user:
    name: ansibletest5
    hashed_password:
      type: 5
      value: $3$8JcDilcYgFZi.yz4ApaqkHG2.8/

- name: Delete users with aggregate
  cisco.ios.ios_user:
    aggregate:
    - name: ansibletest1
    - name: ansibletest2
    - name: ansibletest3
    state: absent
```

## [Return Values](ios_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["username ansible secret password", "username admin secret admin"]` |

### Authors

- Trishna Guha (@trishnaguha)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.ios/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.ios)
