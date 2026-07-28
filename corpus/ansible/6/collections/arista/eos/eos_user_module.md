---
collection: ansible
version: "6"
title: "arista.eos.eos_user module – Manage the collection of local users on EOS devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/arista/eos/eos_user_module.html
fetched_at: 2026-07-27T16:45:19+00:00
---
# arista.eos.eos_user module – Manage the collection of local users on EOS devices

> **Note:**
>
> This module is part of the [arista.eos collection](https://galaxy.ansible.com/arista/eos) (version 5.0.1).
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

## [Parameters](eos_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  aliases: users, collection  list / elements=dictionary | The set of username objects to be configured on the remote Arista EOS device. The list entries can either be the username or a hash of username and properties. This argument is mutually exclusive with the `username` argument. |
| **configured_password**  string | The password to be configured on the remote Arista EOS device. The password needs to be provided in clear and it will be encrypted on the device. Please note that this option is not same as `provider password`. |
| **name**  string | The username to be configured on the remote Arista EOS device. This argument accepts a stringv value and is mutually exclusive with the `aggregate` argument. Please note that this option is not same as `provider username`. |
| **nopassword**  boolean | Defines the username without assigning a password. This will allow the user to login to the system without being authenticated by a password.  Choices:   - `false` - `true` |
| **privilege**  integer | The `privilege` argument configures the privilege level of the user when logged into the system. This argument accepts integer values in the range of 1 to 15. |
| **role**  string | Configures the role for the username in the device running configuration. The argument accepts a string value defining the role name. This argument does not check if the role has been configured on the device. |
| **sshkey**  string | Specifies the SSH public key to configure for the given username. This argument accepts a valid SSH key value. |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  Choices:   - `"present"` - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  Choices:   - `"on_create"` - `"always"` |
| **configured_password**  string | The password to be configured on the remote Arista EOS device. The password needs to be provided in clear and it will be encrypted on the device. Please note that this option is not same as `provider password`. |
| **name**  string | The username to be configured on the remote Arista EOS device. This argument accepts a stringv value and is mutually exclusive with the `aggregate` argument. Please note that this option is not same as `provider username`. |
| **nopassword**  boolean | Defines the username without assigning a password. This will allow the user to login to the system without being authenticated by a password.  Choices:   - `false` - `true` |
| **privilege**  integer | The `privilege` argument configures the privilege level of the user when logged into the system. This argument accepts integer values in the range of 1 to 15. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  Starting with Ansible 2.6 we recommend using `connection: httpapi` for eAPI.  This option will be removed in a release after 2022-06-01.  For more information please see the [EOS Platform Options guide](../network/user_guide/platform_eos.md).   ---   A dict object containing connection details. |
| **auth_pass**  string | Specifies the password to use if required to enter privileged mode on the remote device. If *authorize* is false, then this argument does nothing. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTH_PASS` will be used instead. |
| **authorize**  boolean | Instructs the module to enter privileged mode on the remote device before sending any commands. If not specified, the device will attempt to execute all commands in non-privileged mode. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_AUTHORIZE` will be used instead.  Choices:   - `false` ← (default) - `true` |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This is a common argument used for either *cli* or *eapi* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. This value applies to either *cli* or *eapi*.  The port value will default to the appropriate transport common port if none is provided in the task (cli=22, http=80, https=443).  Default: `0` |
| **ssh_keyfile**  path | Specifies the SSH keyfile to use to authenticate the connection to the remote device. This argument is only used for *cli* transports. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` ← (default) - `"eapi"` |
| **use_proxy**  boolean | If `no`, the environment variables `http_proxy` and `https_proxy` will be ignored.  Choices:   - `false` - `true` ← (default) |
| **use_ssl**  boolean | Configures the *transport* to use SSL if set to `yes` only when the `transport=eapi`. If the transport argument is not eapi, this value is ignored.  Choices:   - `false` - `true` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate either the CLI login or the eAPI authentication depending on which transport is used. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates. If the transport argument is not eapi, this value is ignored.  Choices:   - `false` - `true` ← (default) |
| **purge**  boolean | Instructs the module to consider the resource definition absolute. It will remove any previously configured usernames on the device with the exception of the `admin` user which cannot be deleted per EOS constraints.  Choices:   - `false` ← (default) - `true` |
| **role**  string | Configures the role for the username in the device running configuration. The argument accepts a string value defining the role name. This argument does not check if the role has been configured on the device. |
| **sshkey**  string | Specifies the SSH public key to configure for the given username. This argument accepts a valid SSH key value. |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  Choices:   - `"on_create"` - `"always"` ← (default) |

## [Notes](eos_user_module.md#id3)

> **Note:**
>
> - Tested against Arista EOS 4.24.6F
> - For information on using CLI, eAPI and privileged mode see the :ref:`EOS Platform Options guide <eos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Arista EOS devices see the `Arista integration page <<https://www.ansible.com/ansible-arista-networks>>`_.

## [Examples](eos_user_module.md#id4)

```yaml+jinja
- name: create a new user
  arista.eos.eos_user:
    name: ansible
    sshkey: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
    state: present

- name: remove all users except admin
  arista.eos.eos_user:
    purge: yes

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
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["name ansible secret password", "name admin secret admin"]` |
| **session_name**  string | The EOS config session name used to load the configuration  Returned: when changed is True  Sample: `"ansible_1479315771"` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/arista.eos/issues)
[Repository (Sources)](https://github.com/ansible-collections/arista.eos)
