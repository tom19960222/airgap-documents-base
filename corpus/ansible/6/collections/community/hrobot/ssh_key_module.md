---
collection: ansible
version: "6"
title: "community.hrobot.ssh_key module – Add, remove or update SSH key"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hrobot/ssh_key_module.html
fetched_at: 2026-07-27T17:15:56+00:00
---
# community.hrobot.ssh_key module – Add, remove or update SSH key

> **Note:**
>
> This module is part of the [community.hrobot collection](https://galaxy.ansible.com/community/hrobot) (version 1.6.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.hrobot`.
>
> To use it in a playbook, specify: `community.hrobot.ssh_key`.

New in community.hrobot 1.2.0

- [Synopsis](ssh_key_module.md#synopsis)
- [Parameters](ssh_key_module.md#parameters)
- [Attributes](ssh_key_module.md#attributes)
- [See Also](ssh_key_module.md#see-also)
- [Examples](ssh_key_module.md#examples)
- [Return Values](ssh_key_module.md#return-values)

## [Synopsis](ssh_key_module.md#id1)

- Add, remove or update an SSH key stored in Hetzner’s Robot.

## [Parameters](ssh_key_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **fingerprint**  string | The MD5 fingerprint of the public SSH key to remove.  One of *public_key* and *fingerprint* are required if *state=absent*. |
| **hetzner_password**  string / required | The password for the Robot webservice user. |
| **hetzner_user**  string / required | The username for the Robot webservice user. |
| **name**  string | The public key’s name.  Required if *state=present*, and ignored if *state=absent*. |
| **public_key**  string | The public key data in OpenSSH format.  Example: `ssh-rsa AAAAB3NzaC1yc+...`  One of *public_key* and *fingerprint* are required if *state=absent*.  Required if *state=present*. |
| **state**  string / required | Whether to make sure a public SSH key is present or absent.  `present` makes sure that the SSH key is available, and potentially updates names for existing SHS public keys.  `absent` makes sure that the SSH key is not available. The fingerprint or public key data is used for matching the key.  Choices:   - `"present"` - `"absent"` |

## [Attributes](ssh_key_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.hrobot.robot  added in community.hrobot 1.6.0 | Use `group/community.hrobot.robot` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](ssh_key_module.md#id4)

> **See also:**
>
> [community.hrobot.ssh_key_info](ssh_key_info_module.md#ansible-collections-community-hrobot-ssh-key-info-module)
> :   Query information on SSH keys

## [Examples](ssh_key_module.md#id5)

```yaml+jinja
- name: Add an SSH key
  community.hrobot.ssh_key:
    hetzner_user: foo
    hetzner_password: bar
    state: present
    name: newKey
    public_key: ssh-rsa AAAAB3NzaC1yc+...

- name: Remove a SSH key by fingerprint
  community.hrobot.ssh_key:
    hetzner_user: foo
    hetzner_password: bar
    state: absent
    fingerprint: cb:8b:ef:a7:fe:04:87:3f:e5:55:cd:12:e3:e8:9f:99
```

## [Return Values](ssh_key_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **fingerprint**  string | The MD5 fingerprint of the key.  This is the value used to reference the SSH public key, for example in the [community.hrobot.boot](boot_module.md#ansible-collections-community-hrobot-boot-module) module.  Returned: success  Sample: `"cb:8b:ef:a7:fe:04:87:3f:e5:55:cd:12:e3:e8:9f:99"` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hrobot/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hrobot)
[Submit a bug report](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-hrobot)
