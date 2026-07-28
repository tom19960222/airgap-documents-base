---
collection: ansible
version: "6"
title: "junipernetworks.junos.junos_user module – Manage local user accounts on Juniper JUNOS devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/junipernetworks/junos/junos_user_module.html
fetched_at: 2026-07-27T17:54:43+00:00
---
# junipernetworks.junos.junos_user module – Manage local user accounts on Juniper JUNOS devices

> **Note:**
>
> This module is part of the [junipernetworks.junos collection](https://galaxy.ansible.com/junipernetworks/junos) (version 3.1.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install junipernetworks.junos`.
> You need further requirements to be able to use this module,
> see [Requirements](junos_user_module.md#ansible-collections-junipernetworks-junos-junos-user-module-requirements) for details.
>
> To use it in a playbook, specify: `junipernetworks.junos.junos_user`.

New in junipernetworks.junos 1.0.0

- [Synopsis](junos_user_module.md#synopsis)
- [Requirements](junos_user_module.md#requirements)
- [Parameters](junos_user_module.md#parameters)
- [Notes](junos_user_module.md#notes)
- [Examples](junos_user_module.md#examples)
- [Return Values](junos_user_module.md#return-values)

## [Synopsis](junos_user_module.md#id1)

- This module manages locally configured user accounts on remote network devices running the JUNOS operating system. It provides a set of arguments for creating, removing and updating locally defined accounts

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](junos_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- ncclient (>=v0.5.2)

## [Parameters](junos_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  Choices:   - `false` - `true` ← (default) |
| **aggregate**  aliases: users, collection  list / elements=dictionary | The `aggregate` argument defines a list of users to be configured on the remote device. The list of users will be compared against the current users and only changes will be added or removed from the device configuration. This argument is mutually exclusive with the name argument. |
| **active**  boolean | Specifies whether or not the configuration is active or deactivated  Choices:   - `false` - `true` |
| **encrypted_password**  string | The `encrypted_password` argument set already hashed password for the user account on the remote system. |
| **full_name**  string | The `full_name` argument provides the full name of the user account to be created on the remote device. This argument accepts any text string value. |
| **name**  string / required | The `name` argument defines the username of the user to be created on the system. This argument must follow appropriate usernaming conventions for the target device running JUNOS. This argument is mutually exclusive with the `aggregate` argument. |
| **purge**  boolean | The `purge` argument instructs the module to consider the users definition absolute. It will remove any previously configured users on the device with the exception of the current defined set of aggregate.  Choices:   - `false` ← (default) - `true` |
| **role**  string | The `role` argument defines the role of the user account on the remote system. User accounts can have more than one role configured.  Choices:   - `"operator"` - `"read-only"` - `"super-user"` - `"unauthorized"` |
| **sshkey**  string | The `sshkey` argument defines the public SSH key to be configured for the user account on the remote system. This argument must be a valid SSH key |
| **state**  string | The `state` argument configures the state of the user definitions as it relates to the device operational configuration. When set to *present*, the user should be configured in the device active configuration and when set to *absent* the user should not be in the device active configuration  Choices:   - `"present"` - `"absent"` |
| **encrypted_password**  string | The `encrypted_password` argument set already hashed password for the user account on the remote system. |
| **full_name**  string | The `full_name` argument provides the full name of the user account to be created on the remote device. This argument accepts any text string value. |
| **name**  string | The `name` argument defines the username of the user to be created on the system. This argument must follow appropriate usernaming conventions for the target device running JUNOS. This argument is mutually exclusive with the `aggregate` argument. |
| **provider**  dictionary | **Deprecated**  Starting with Ansible 2.5 we recommend using `connection: network_cli` or `connection: netconf`.  For more information please see the [Junos OS Platform Options guide](../network/user_guide/platform_junos.md).   ---   A dict object containing connection details. |
| **host**  string | Specifies the DNS host name or address for connecting to the remote device over the specified transport. The value of host is used as the destination address for the transport. |
| **password**  string | Specifies the password to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_PASSWORD` will be used instead. |
| **port**  integer | Specifies the port to use when building the connection to the remote device. The port value will default to the well known SSH port of 22 (for `transport=cli`) or port 830 (for `transport=netconf`) device. |
| **ssh_keyfile**  path | Specifies the SSH key to use to authenticate the connection to the remote device. This value is the path to the key used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_SSH_KEYFILE` will be used instead. |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"cli"` - `"netconf"` ← (default) |
| **username**  string | Configures the username to use to authenticate the connection to the remote device. This value is used to authenticate the SSH session. If the value is not specified in the task, the value of environment variable `ANSIBLE_NET_USERNAME` will be used instead. |
| **purge**  boolean | The `purge` argument instructs the module to consider the users definition absolute. It will remove any previously configured users on the device with the exception of the current defined set of aggregate.  Choices:   - `false` ← (default) - `true` |
| **role**  string | The `role` argument defines the role of the user account on the remote system. User accounts can have more than one role configured.  Choices:   - `"operator"` - `"read-only"` - `"super-user"` - `"unauthorized"` |
| **sshkey**  string | The `sshkey` argument defines the public SSH key to be configured for the user account on the remote system. This argument must be a valid SSH key |
| **state**  string | The `state` argument configures the state of the user definitions as it relates to the device operational configuration. When set to *present*, the user should be configured in the device active configuration and when set to *absent* the user should not be in the device active configuration  Choices:   - `"present"` ← (default) - `"absent"` |

## [Notes](junos_user_module.md#id4)

> **Note:**
>
> - This module requires the netconf system service be enabled on the remote device being managed.
> - Tested against vSRX JUNOS version 15.1X49-D15.4, vqfx-10000 JUNOS Version 15.1X53-D60.4.
> - Recommended connection is `netconf`. See [the Junos OS Platform Options](../network/user_guide/platform_junos.md).
> - This module also works with `local` connections for legacy playbooks.
> - For information on using CLI and netconf see the :ref:`Junos OS Platform Options guide <junos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Juniper network devices see <https://www.ansible.com/ansible-juniper>.

## [Examples](junos_user_module.md#id5)

```yaml+jinja
- name: create new user account
  junipernetworks.junos.junos_user:
    name: ansible
    role: super-user
    sshkey: "{{ lookup('file', '~/.ssh/ansible.pub') }}"
    state: present

- name: remove a user account
  junipernetworks.junos.junos_user:
    name: ansible
    state: absent

- name: remove all user accounts except ansible
  junipernetworks.junos.junos_user:
    aggregate:
    - name: ansible
    purge: yes

- name: set user password
  junipernetworks.junos.junos_user:
    name: ansible
    role: super-user
    encrypted_password: "{{ 'my-password' | password_hash('sha512') }}"
    state: present

- name: Create list of users
  junipernetworks.junos.junos_user:
    aggregate:
    - {name: test_user1, full_name: test_user2, role: operator, state: present}
    - {name: test_user2, full_name: test_user2, role: read-only, state: present}

- name: Delete list of users
  junipernetworks.junos.junos_user:
    aggregate:
    - {name: test_user1, full_name: test_user2, role: operator, state: absent}
    - {name: test_user2, full_name: test_user2, role: read-only, state: absent}
```

## [Return Values](junos_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **diff.prepared**  string | Configuration difference before and after applying change.  Returned: when configuration is changed and diff option is enabled.  Sample: `"[edit system login] +    user test-user { +        uid 2005; +        class read-only; +    }\n"` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/junipernetworks.junos/issues)
[Repository (Sources)](https://github.com/ansible-collections/junipernetworks.junos)
