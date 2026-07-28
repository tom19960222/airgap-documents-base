---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_token module – Create or delete an API token for an existing admin user"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_token_module.html
fetched_at: 2026-07-28T02:51:32+00:00
---
# purestorage.flasharray.purefa_token module – Create or delete an API token for an existing admin user

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_token`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_token_module.md#synopsis)
- [Parameters](purefa_token_module.md#parameters)
- [Examples](purefa_token_module.md#examples)
- [Return Values](purefa_token_module.md#return-values)

## [Synopsis](purefa_token_module.md#id1)

- Create or delete an API token for an existing admin user.
- Uses username/password to create/delete the API token.

## [Parameters](purefa_token_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **password**  string | Password of the admin user to create API token for. |
| **recreate**  boolean | Recreates the API token, overwriting the existing API token if present  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Create or delete API token  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **timeout**  string | The duration of API token validity.  Valid values are weeks (w), days(d), hours(h), minutes(m) and seconds(s). |
| **username**  string | Username of the admin user to create API token for |

## [Examples](purefa_token_module.md#id3)

```yaml+jinja
- name: Create API token with no expiration
  purefa_token:
    username: pureuser
    password: secret
    state: present
    fa_url: 10.10.10.2
- name: Create API token with 23 days expiration
  purefa_token:
    username: pureuser
    password: secret
    state: present
    timeout: 23d
    fa_url: 10.10.10.2
- name: Delete API token
  purefa_token:
    username: pureuser
    password: secret
    state: absent
    fa_url: 10.10.10.2
```

## [Return Values](purefa_token_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **purefa_token**  string | API token for user  **Returned:** changed  **Sample:** `"e649f439-49be-3806-f774-a35cbbc4c2d2"` |

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
