---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_user module – Create, modify or delete FlashArray local user account"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_user_module.html
fetched_at: 2026-07-28T02:51:33+00:00
---
# purestorage.flasharray.purefa_user module – Create, modify or delete FlashArray local user account

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_user_module.md#ansible-collections-purestorage-flasharray-purefa-user-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_user`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_user_module.md#synopsis)
- [Requirements](purefa_user_module.md#requirements)
- [Parameters](purefa_user_module.md#parameters)
- [Notes](purefa_user_module.md#notes)
- [Examples](purefa_user_module.md#examples)

## [Synopsis](purefa_user_module.md#id1)

- Create, modify or delete local users on a Pure Stoage FlashArray.

## [Requirements](purefa_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api**  boolean | Define whether to create an API token for this user  Token can be exposed using the *debug* module  **Choices:**   - `false` ← (default) - `true` |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **name**  string / required | The name of the local user account |
| **old_password**  string | If changing an existing password, you must provide the old password for security |
| **password**  string | Password for the local user. |
| **role**  string | Sets the local user’s access level to the array  **Choices:**   - `"readonly"` - `"ops_admin"` - `"storage_admin"` - `"array_admin"` |
| **state**  string | Create, delete or update local user account  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Notes](purefa_user_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_user_module.md#id5)

```yaml+jinja
- name: Create new user ansible with API token
  purestorage.flasharray.purefa_user:
    name: ansible
    password: apassword
    role: storage_admin
    api: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
  register: result

  debug:
    msg: "API Token: {{ result['user_info']['user_api'] }}"

- name: Change role type for existing user
  purestorage.flasharray.purefa_user:
    name: ansible
    role: array_admin
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Change password type for existing user (NOT IDEMPOTENT)
  purestorage.flasharray.purefa_user:
    name: ansible
    password: anewpassword
    old_password: apassword
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Change API token for existing user
  purestorage.flasharray.purefa_user:
    name: ansible
    api: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
  register: result

  debug:
    msg: "API Token: {{ result['user_info']['user_api'] }}"
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
