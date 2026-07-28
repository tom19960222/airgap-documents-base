---
collection: ansible
version: "8"
title: "purestorage.flashblade.purefb_user module – Modify FlashBlade user accounts"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flashblade/purefb_user_module.html
fetched_at: 2026-07-28T02:52:26+00:00
---
# purestorage.flashblade.purefb_user module – Modify FlashBlade user accounts

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flashblade/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_user_module.md#ansible-collections-purestorage-flashblade-purefb-user-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_user`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_user_module.md#synopsis)
- [Requirements](purefb_user_module.md#requirements)
- [Parameters](purefb_user_module.md#parameters)
- [Notes](purefb_user_module.md#notes)
- [Examples](purefb_user_module.md#examples)

## [Synopsis](purefb_user_module.md#id1)

- Modify user on a Pure Stoage FlashBlade.

## [Requirements](purefb_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **clear_lock**  boolean  *added in purestorage.flashblade 1.8.0* | Clear user lockout flag  **Choices:**   - `false` ← (default) - `true` |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **name**  string | The name of the user account |
| **old_password**  string | If changing an existing password, you must provide the old password for security  Only applies to the local user ‘pureuser’ |
| **password**  string | Password for the local user.  Only applies to the local user ‘pureuser’ |
| **public_key**  string  *added in purestorage.flashblade 1.8.0* | The API clients PEM formatted (Base64 encoded) RSA public key.  Include the *—–BEGIN PUBLIC KEY—–* and *—–END PUBLIC KEY—–* lines |

## [Notes](purefb_user_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_user_module.md#id5)

```yaml+jinja
- name: Change password for local user (NOT IDEMPOTENT)
  purestorage.flashblade.purefb_user:
    name: pureuser
    password: anewpassword
    old_password: apassword
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6

- name: Set public key for user
  purestorage.flashblade.purefb_user:
    name: fred
    public_key: "{{lookup('file', 'public_pem_file') }}"
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6

- name: Clear user lockout
  purestorage.flashblade.purefb_user:
    name: fred
    clear_lock: true
    fb_url: 10.10.10.2
    api_token: T-9f276a18-50ab-446e-8a0c-666a3529a1b6
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
