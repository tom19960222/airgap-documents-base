---
collection: ansible
version: "6"
title: "cisco.iosxr.iosxr_user module – Module to manage the aggregates of local users."
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/iosxr/iosxr_user_module.html
fetched_at: 2026-07-27T16:55:58+00:00
---
# cisco.iosxr.iosxr_user module – Module to manage the aggregates of local users.

> **Note:**
>
> This module is part of the [cisco.iosxr collection](https://galaxy.ansible.com/cisco/iosxr) (version 3.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.iosxr`.
> You need further requirements to be able to use this module,
> see [Requirements](iosxr_user_module.md#ansible-collections-cisco-iosxr-iosxr-user-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.iosxr.iosxr_user`.

New in cisco.iosxr 1.0.0

- [Synopsis](iosxr_user_module.md#synopsis)
- [Requirements](iosxr_user_module.md#requirements)
- [Parameters](iosxr_user_module.md#parameters)
- [Notes](iosxr_user_module.md#notes)
- [Examples](iosxr_user_module.md#examples)
- [Return Values](iosxr_user_module.md#return-values)

## [Synopsis](iosxr_user_module.md#id1)

- This module provides declarative management of the local usernames configured on network devices. It allows playbooks to manage either individual usernames or the aggregate of usernames in the current running config. It also supports purging usernames from the configuration that are not explicitly defined.

## [Requirements](iosxr_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient >= 0.5.3 when using netconf
- lxml >= 4.1.1 when using netconf
- base64 when using *public_key_contents* or *public_key*

## [Parameters](iosxr_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **admin**  boolean | Enters into administration configuration mode for making config changes to the device.  Applicable only when using network_cli transport  Choices:   - `false` ← (default) - `true` |
| **aggregate**  aliases: users, collection  list / elements=dictionary | The set of username objects to be configured on the remote Cisco IOS XR device. The list entries can either be the username or a hash of username and properties. This argument is mutually exclusive with the `name` argument. |
| **admin**  boolean | Enters into administration configuration mode for making config changes to the device.  Applicable only when using network_cli transport  Choices:   - `false` - `true` |
| **configured_password**  string | The password to be configured on the Cisco IOS XR device. The password needs to be provided in clear text. Password is encrypted on the device when used with *cli* and by Ansible when used with *netconf* using the same MD5 hash technique with salt size of 3. Please note that this option is not same as `provider password`. |
| **group**  aliases: role  string | Configures the group for the username in the device running configuration. The argument accepts a string value defining the group name. This argument does not check if the group has been configured on the device. |
| **groups**  list / elements=string | Configures the groups for the username in the device running configuration. The argument accepts a list of group names. This argument does not check if the group has been configured on the device. It is similar to the aggregate command for usernames, but lets you configure multiple groups for the user(s). |
| **name**  string / required | The username to be configured on the Cisco IOS XR device. This argument accepts a string value and is mutually exclusive with the `aggregate` argument. Please note that this option is not same as `provider username`. |
| **public_key**  string | Configures the contents of the public keyfile to upload to the IOS-XR node. This enables users to login using the accompanying private key. IOS-XR only accepts base64 decoded files, so this will be decoded and uploaded to the node. Do note that this requires an OpenSSL public key file, PuTTy generated files will not work! Mutually exclusive with public_key_contents. If used with multiple users in aggregates, then the same key file is used for all users. |
| **public_key_contents**  string | Configures the contents of the public keyfile to upload to the IOS-XR node. This enables users to login using the accompanying private key. IOS-XR only accepts base64 decoded files, so this will be decoded and uploaded to the node. Do note that this requires an OpenSSL public key file, PuTTy generated files will not work! Mutually exclusive with public_key.If used with multiple users in aggregates, then the same key file is used for all users. |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  Choices:   - `"present"` - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  Choices:   - `"on_create"` - `"always"` |
| **configured_password**  string | The password to be configured on the Cisco IOS XR device. The password needs to be provided in clear text. Password is encrypted on the device when used with *cli* and by Ansible when used with *netconf* using the same MD5 hash technique with salt size of 3. Please note that this option is not same as `provider password`. |
| **group**  aliases: role  string | Configures the group for the username in the device running configuration. The argument accepts a string value defining the group name. This argument does not check if the group has been configured on the device. |
| **groups**  list / elements=string | Configures the groups for the username in the device running configuration. The argument accepts a list of group names. This argument does not check if the group has been configured on the device. It is similar to the aggregate command for usernames, but lets you configure multiple groups for the user(s). |
| **name**  string | The username to be configured on the Cisco IOS XR device. This argument accepts a string value and is mutually exclusive with the `aggregate` argument. Please note that this option is not same as `provider username`. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli`.  For more information please see the [Network Guide](../network/getting_started/network_differences.md#multiple-communication-protocols).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Specifies the type of connection based transport.  Choices:   - `"cli"` ← (default) - `"netconf"` |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **public_key**  string | Configures the contents of the public keyfile to upload to the IOS-XR node. This enables users to login using the accompanying private key. IOS-XR only accepts base64 decoded files, so this will be decoded and uploaded to the node. Do note that this requires an OpenSSL public key file, PuTTy generated files will not work! Mutually exclusive with public_key_contents. If used with multiple users in aggregates, then the same key file is used for all users. |
| **public_key_contents**  string | Configures the contents of the public keyfile to upload to the IOS-XR node. This enables users to login using the accompanying private key. IOS-XR only accepts base64 decoded files, so this will be decoded and uploaded to the node. Do note that this requires an OpenSSL public key file, PuTTy generated files will not work! Mutually exclusive with public_key.If used with multiple users in aggregates, then the same key file is used for all users. |
| **purge**  boolean | Instructs the module to consider the resource definition absolute. It will remove any previously configured usernames on the device with the exception of the `admin` user and the current defined set of users.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  Choices:   - `"on_create"` - `"always"` ← (default) |

## [Notes](iosxr_user_module.md#id4)

> **Note:**
>
> - This module works with connection `network_cli` and `netconf`. See [the IOS-XR Platform Options](../network/user_guide/platform_iosxr.md).
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](iosxr_user_module.md#id5)

```yaml+jinja
- name: create a new user
  cisco.iosxr.iosxr_user:
    name: ansible
    configured_password: mypassword
    state: present
- name: create a new user in admin configuration mode
  cisco.iosxr.iosxr_user:
    name: ansible
    configured_password: mypassword
    admin: true
    state: present
- name: remove all users except admin
  cisco.iosxr.iosxr_user:
    purge: true
- name: set multiple users to group sys-admin
  cisco.iosxr.iosxr_user:
    aggregate:
    - name: netop
    - name: netend
    group: sysadmin
    state: present
- name: set multiple users to multiple groups
  cisco.iosxr.iosxr_user:
    aggregate:
    - name: netop
    - name: netend
    groups:
    - sysadmin
    - root-system
    state: present
- name: Change Password for User netop
  cisco.iosxr.iosxr_user:
    name: netop
    configured_password: '{{ new_password }}'
    update_password: always
    state: present
- name: Add private key authentication for user netop
  cisco.iosxr.iosxr_user:
    name: netop
    state: present
    public_key_contents: "{{ lookup('file', '/home/netop/.ssh/id_rsa.pub' }}"
```

## [Return Values](iosxr_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["username ansible secret password group sysadmin", "username admin secret admin"]` |
| **xml**  list / elements=string | NetConf rpc xml sent to device with transport `netconf`  Returned: always (empty list when no xml rpc to send)  Sample: `["<config xmlns:xc=\"urn:ietf:params:xml:ns:netconf:base:1.0\"> <aaa xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-aaa-lib-cfg\"> <usernames xmlns=\"http://cisco.com/ns/yang/Cisco-IOS-XR-aaa-locald-cfg\"> <username xc:operation=\"merge\"> <name>test7</name> <usergroup-under-usernames> <usergroup-under-username> <name>sysadmin</name> </usergroup-under-username> </usergroup-under-usernames> <secret>$1$ZsXC$zZ50wqhDC543ZWQkkAHLW0</secret> </username> </usernames> </aaa> </config>"]` |

### Authors

- Trishna Guha (@trishnaguha)
- Sebastiaan van Doesselaar (@sebasdoes)
- Kedar Kekan (@kedarX)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/cisco.iosxr/issues)
[Repository (Sources)](https://github.com/ansible-collections/cisco.iosxr)
