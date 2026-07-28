---
collection: ansible
version: "6"
title: "community.network.cnos_user module – Manage the collection of local users on Lenovo CNOS devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/cnos_user_module.html
fetched_at: 2026-07-27T17:18:18+00:00
---
# community.network.cnos_user module – Manage the collection of local users on Lenovo CNOS devices

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
> To use it in a playbook, specify: `community.network.cnos_user`.

- [Synopsis](cnos_user_module.md#synopsis)
- [Parameters](cnos_user_module.md#parameters)
- [Examples](cnos_user_module.md#examples)
- [Return Values](cnos_user_module.md#return-values)

## [Synopsis](cnos_user_module.md#id1)

- This module provides declarative management of the local usernames configured on Lenovo CNOS devices. It allows playbooks to manage either individual usernames or the collection of usernames in the current running config. It also supports purging usernames from the configuration that are not explicitly defined.

## [Parameters](cnos_user_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **aggregate**  aliases: users, collection  string | The set of username objects to be configured on the remote Lenovo CNOS device. The list entries can either be the username or a hash of username and properties. This argument is mutually exclusive with the `name` argument. |
| **configured_password**  string | The password to be configured on the network device. The password needs to be provided in cleartext and it will be encrypted on the device. Please note that this option is not same as `provider password`. |
| **name**  string | The username to be configured on the remote Lenovo CNOS device. This argument accepts a string value and is mutually exclusive with the `aggregate` argument. |
| **purge**  boolean | The `purge` argument instructs the module to consider the resource definition absolute. It will remove any previously configured usernames on the device with the exception of the `admin` user which cannot be deleted per cnos constraints.  Choices:   - `false` ← (default) - `true` |
| **role**  aliases: roles  string | The `role` argument configures the role for the username in the device running configuration. The argument accepts a string value defining the role name. This argument does not check if the role has been configured on the device. |
| **sshkey**  string | The `sshkey` argument defines the SSH public key to configure for the username. This argument accepts a valid SSH key value. |
| **state**  string | The `state` argument configures the state of the username definition as it relates to the device operational configuration. When set to *present*, the username(s) should be configured in the device active configuration and when set to *absent* the username(s) should not be in the device active configuration  Choices:   - `"present"` ← (default) - `"absent"` |
| **update_password**  string | Since passwords are encrypted in the device running config, this argument will instruct the module when to change the password. When set to `always`, the password will always be updated in the device and when set to `on_create` the password will be updated only if the username is created.  Choices:   - `"on_create"` - `"always"` ← (default) |

## [Examples](cnos_user_module.md#id3)

```yaml+jinja
- name: Create a new user
  community.network.cnos_user:
    name: ansible
    sshkey: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"
    state: present

- name: Remove all users except admin
  community.network.cnos_user:
    purge: yes

- name: Set multiple users role
  aggregate:
    - name: Netop
    - name: Netend
  role: network-operator
  state: present
```

## [Return Values](cnos_user_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **commands**  list / elements=string | The list of configuration mode commands to send to the device  Returned: always  Sample: `["name ansible", "name ansible password password"]` |
| **delta**  string | The time elapsed to perform all operations  Returned: always  Sample: `"0:00:10.469466"` |
| **end**  string | The time the job ended  Returned: always  Sample: `"2016-11-16 10:38:25.595612"` |
| **start**  string | The time the job started  Returned: always  Sample: `"2016-11-16 10:38:15.126146"` |

### Authors

- Anil Kumar Muraleedharan (@amuraleedhar)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
