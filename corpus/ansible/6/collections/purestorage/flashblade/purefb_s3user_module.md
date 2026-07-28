---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_s3user module – Create or delete FlashBlade Object Store account users"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_s3user_module.html
fetched_at: 2026-07-28T00:18:58+00:00
---
# purestorage.flashblade.purefb_s3user module – Create or delete FlashBlade Object Store account users

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
> see [Requirements](purefb_s3user_module.md#ansible-collections-purestorage-flashblade-purefb-s3user-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_s3user`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_s3user_module.md#synopsis)
- [Requirements](purefb_s3user_module.md#requirements)
- [Parameters](purefb_s3user_module.md#parameters)
- [Notes](purefb_s3user_module.md#notes)
- [Examples](purefb_s3user_module.md#examples)

## [Synopsis](purefb_s3user_module.md#id1)

- Create or delete object store account users on a Pure Stoage FlashBlade.

## [Requirements](purefb_s3user_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_s3user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_key**  boolean | Create secret access key.  Key can be exposed using the *debug* module  If enabled this will override *imported_key*  Choices:   - `false` ← (default) - `true` |
| **account**  string / required | The name of object store account associated with user |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **imported_key**  string  added in purestorage.flashblade 1.4.0 | Access key of imported credentials |
| **imported_secret**  string  added in purestorage.flashblade 1.4.0 | Access key secret for access key to import |
| **name**  string / required | The name of object store user |
| **policy**  list / elements=string  added in purestorage.flashblade 1.6.0 | User Access Policies to be assigned to user on creation  To amend policies use the *purestorage.flashblade.purefb_userpolicy* module  If not specified, *pure\:policy/full-access* will be added |
| **remove_key**  string  added in purestorage.flashblade 1.5.0 | Access key to be removed from user |
| **state**  string | Create or delete object store account user  Remove a specified access key for a user  Choices:   - `"absent"` - `"present"` ← (default) - `"remove_key"` |

## [Notes](purefb_s3user_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_s3user_module.md#id5)

```yaml+jinja
- name: Create object store user (with access ID and key) foo in account bar
  purestorage.flashblade.purefb_s3user:
    name: foo
    account: bar
    access_key: true
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
  register: result

- debug:
    msg: "S3 User: {{ result['s3user_info'] }}"

- name: Create object store user (with access ID and key) foo in account bar with access policy (Purity 3.2 and higher)
  purestorage.flashblade.purefb_s3user:
    name: foo
    account: bar
    access_key: true
    policy:
      - pure:policy/safemode-configure
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create object store user foo using imported key/secret in account bar
  purestorage.flashblade.purefb_s3user:
    name: foo
    account: bar
    imported_key: "PSABSSZRHPMEDKHMAAJPJBONPJGGDDAOFABDGLBJLHO"
    imported_secret: "BAG61F63105e0d3669/e066+5C5DFBE2c127d395LBGG"
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Delete object store user foo in account bar
  purestorage.flashblade.purefb_s3user:
    name: foo
    account: bar
    state: absent
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
