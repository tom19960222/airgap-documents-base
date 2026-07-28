---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_userpolicy module – Manage FlashBlade Object Store User Access Policies"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_userpolicy_module.html
fetched_at: 2026-07-28T00:19:05+00:00
---
# purestorage.flashblade.purefb_userpolicy module – Manage FlashBlade Object Store User Access Policies

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/purestorage/flashblade) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_userpolicy_module.md#ansible-collections-purestorage-flashblade-purefb-userpolicy-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_userpolicy`.

New in purestorage.flashblade 1.6.0

- [Synopsis](purefb_userpolicy_module.md#synopsis)
- [Requirements](purefb_userpolicy_module.md#requirements)
- [Parameters](purefb_userpolicy_module.md#parameters)
- [Notes](purefb_userpolicy_module.md#notes)
- [Examples](purefb_userpolicy_module.md#examples)
- [Return Values](purefb_userpolicy_module.md#return-values)

## [Synopsis](purefb_userpolicy_module.md#id1)

- Add or Remove FlashBlade Object Store Access Policies for Account User

## [Requirements](purefb_userpolicy_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_userpolicy_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **account**  string | Name of the Object Store Account associated with the user |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **name**  string | Name of the Object Store User  The user to have the policy request applied to |
| **policy**  list / elements=string | Policies to added or deleted from the Object Store User  Only valid policies can be used  use *list* to see available policies |
| **state**  string | Define whether the Access Policy should be added or deleted  Option to list all available policies  Choices:   - `"absent"` - `"present"` ← (default) - `"show"` |

## [Notes](purefb_userpolicy_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_userpolicy_module.md#id5)

```yaml+jinja
- name: List existng ruser access policies for a specific user
  purestorage.flashblade.purefb_userpolicy:
    state: show
    account: foo
    name: bar
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3
  register: policy_list

- name: List all available user access policies
  purestorage.flashblade.purefb_userpolicy:
    state: show
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3
  register: policy_list

- name: Add user access policies to account user foo/bar
  purestorage.flashblade.purefb_userpolicy:
    name: bar
    account: foo
    policy:
      - pure:policy/bucket-create
      - pure:policy/bucket-delete
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3

- name: Delete user access policies to account user foo/bar
  purestorage.flashblade.purefb_userpolicy:
    name: bar
    account: foo
    policy:
      - pure:policy/bucket-create
      - pure:policy/bucket-delete
    state: absent
    fb_url: 10.10.10.2
    api_token: T-68618f31-0c9e-4e57-aa44-5306a2cf10e3
```

## [Return Values](purefb_userpolicy_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **policy_list**  list / elements=string | Returns the list of access policies for a user  If no user specified returns all available access policies  Returned: always  Sample: `["pure:policy/object-list", "pure:policy/bucket-list", "pure:policy/object-read", "pure:policy/bucket-delete", "pure:policy/full-access"]` |

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
