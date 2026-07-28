---
collection: ansible
version: "6"
title: "community.hrobot.ssh_key_info module – Query information on SSH keys"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/hrobot/ssh_key_info_module.html
fetched_at: 2026-07-27T17:15:56+00:00
---
# community.hrobot.ssh_key_info module – Query information on SSH keys

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
> To use it in a playbook, specify: `community.hrobot.ssh_key_info`.

New in community.hrobot 1.2.0

- [Synopsis](ssh_key_info_module.md#synopsis)
- [Parameters](ssh_key_info_module.md#parameters)
- [Attributes](ssh_key_info_module.md#attributes)
- [See Also](ssh_key_info_module.md#see-also)
- [Examples](ssh_key_info_module.md#examples)
- [Return Values](ssh_key_info_module.md#return-values)

## [Synopsis](ssh_key_info_module.md#id1)

- List information on all your SSH keys stored in Hetzner’s Robot.

## [Parameters](ssh_key_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hetzner_password**  string / required | The password for the Robot webservice user. |
| **hetzner_user**  string / required | The username for the Robot webservice user. |

## [Attributes](ssh_key_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.hrobot.robot  added in community.hrobot 1.6.0 | Use `group/community.hrobot.robot` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](ssh_key_info_module.md#id4)

> **See also:**
>
> [community.hrobot.ssh_key](ssh_key_module.md#ansible-collections-community-hrobot-ssh-key-module)
> :   Add, remove or update SSH key

## [Examples](ssh_key_info_module.md#id5)

```yaml+jinja
- name: List all SSH keys
  community.hrobot.ssh_key_info:
    hetzner_user: foo
    hetzner_password: bar
  register: ssh_keys

- name: Show how many keys were found
  ansible.builtin.debug:
    msg: "Found {{ ssh_keys.ssh_keys | length }} keys"
```

## [Return Values](ssh_key_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ssh_keys**  list / elements=dictionary | The list of all SSH keys stored in Hetzner’s Robot for your user.  Returned: success |
| **data**  string | The key data in OpenSSH’s format.  Returned: success  Sample: `"ecdsa-sha2-nistp521 AAAAE2VjZHNh ..."` |
| **fingerprint**  string | The key’s MD5 fingerprint.  Returned: success  Sample: `"56:29:99:a4:5d:ed:ac:95:c1:f5:88:82:90:5d:dd:10"` |
| **name**  string | The key’s name shown in the UI.  Returned: success  Sample: `"key1"` |
| **size**  integer | The key’s size in bits.  Returned: success  Sample: `521` |
| **type**  string | The key’s algorithm type.  Returned: success  Sample: `"ECDSA"` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.hrobot/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.hrobot)
[Submit a bug report](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.hrobot/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-hrobot)
