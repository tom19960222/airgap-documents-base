---
collection: ansible
version: "8"
title: "cisco.nxos.nxos_user module – Manage the collection of local users on Nexus devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/nxos/nxos_user_module.html
fetched_at: 2026-07-28T01:39:17+00:00
---
# cisco.nxos.nxos_user module – Manage the collection of local users on Nexus devices

> **Note:**
>
> This module is part of the [cisco.nxos collection](https://galaxy.ansible.com/ui/repo/published/cisco/nxos/) (version 4.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.nxos`.
>
> To use it in a playbook, specify: `cisco.nxos.nxos_user`.

New in cisco.nxos 1.0.0

- [Synopsis](nxos_user_module.md#synopsis)
- [Parameters](nxos_user_module.md#parameters)
- [Notes](nxos_user_module.md#notes)
- [Examples](nxos_user_module.md#examples)
- [Return Values](nxos_user_module.md#return-values)

## [Synopsis](nxos_user_module.md#id1)

- This module provides declarative management of the local usernames configured on Cisco Nexus devices. It allows playbooks to manage either individual usernames or the collection of usernames in the current running config. It also supports purging usernames from the configuration that are not explicitly defined.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

Aliases: user

## [Parameters](nxos_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  aliases: users, collection  list / elements=dictionary | The set of username objects to be configured on the remote Cisco Nexus device. The list entries can either be the username or a hash of username and properties. This argument is mutually exclusive with the `name` argument. |
| **configured_password**  string | The password to be configured on the network device. The password needs to be provided in cleartext and it will be encrypted on the device. |
| **hashed_password**  string | The hashed password to be configured on the network device. The password needs to already be encrypted. |
| **name**  string | The username to be configured on the remote Cisco Nexus device. This argument accepts a string value and is mutually exclusive with the `aggregate` argument. |
| **roles**  aliases: role  list / elements=string | The `role` argument configures the role for the username in the device running configuration. The argument accepts a string value defining the role name. This argument does not check if the role has been configured on the device. |
| **sshkey**  string | The `sshkey` argument defines the SSH public key to configure for the username. This argument accepts a valid SSH key value. |
| **state**  string | The `state` argument configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  **Choices:**   - `"present"` - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  **Choices:**   - `"on_create"` - `"always"` |
| **configured_password**  string | The password to be configured on the network device. The password needs to be provided in cleartext and it will be encrypted on the device. |
| **hashed_password**  string | The hashed password to be configured on the network device. The password needs to already be encrypted. |
| **name**  string | The username to be configured on the remote Cisco Nexus device. This argument accepts a string value and is mutually exclusive with the `aggregate` argument. |
| **purge**  boolean | The `purge` argument instructs the module to consider the resource definition absolute. It will remove any previously configured usernames on the device with the exception of the `admin` user which cannot be deleted per nxos constraints.  **Choices:**   - `false` ← (default) - `true` |
| **roles**  aliases: role  list / elements=string | The `role` argument configures the role for the username in the device running configuration. The argument accepts a string value defining the role name. This argument does not check if the role has been configured on the device. |
| **sshkey**  string | The `sshkey` argument defines the SSH public key to configure for the username. This argument accepts a valid SSH key value. |
| **state**  string | The `state` argument configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  **Choices:**   - `"on_create"` - `"always"` ← (default) |

## [Notes](nxos_user_module.md#id3)

> **Note:**
>
> - Limited Support for Cisco MDS
> - For information on using CLI and NX-API see the :ref:`NXOS Platform Options guide <nxos_platform_options>`
> - For more information on using Ansible to manage network devices see the :ref:`Ansible Network Guide <network_guide>`
> - For more information on using Ansible to manage Cisco devices see the `Cisco integration page <<https://www.ansible.com/integrations/networks/cisco>>`_.

## [Examples](nxos_user_module.md#id4)

```yaml+jinja
- name: create a new user
  cisco.nxos.nxos_user:
    name: ansible
    sshkey: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
    state: present

- name: remove all users except admin
  cisco.nxos.nxos_user:
    purge: true

- name: set multiple users role
  cisco.nxos.nxos_user:
    aggregate:
    - name: netop
    - name: netend
    role: network-operator
  state: present
```

## [Return Values](nxos_user_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  **Returned:** always  **Sample:** `["name ansible", "name ansible password password"]` |

### Authors

- Peter Sprygada (@privateip)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/cisco.nxos/issues)
- [Repository (Sources)](https://github.com/ansible-collections/cisco.nxos)
