---
collection: ansible
version: "8"
title: "community.general.manageiq_user module – Management of users in ManageIQ"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/manageiq_user_module.html
fetched_at: 2026-07-28T01:47:52+00:00
---
# community.general.manageiq_user module – Management of users in ManageIQ

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](manageiq_user_module.md#ansible-collections-community-general-manageiq-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.manageiq_user`.

- [Synopsis](manageiq_user_module.md#synopsis)
- [Requirements](manageiq_user_module.md#requirements)
- [Parameters](manageiq_user_module.md#parameters)
- [Attributes](manageiq_user_module.md#attributes)
- [Examples](manageiq_user_module.md#examples)

## [Synopsis](manageiq_user_module.md#id1)

- The manageiq_user module supports adding, updating and deleting users in ManageIQ.

Aliases: remote_management.manageiq.manageiq_user

## [Requirements](manageiq_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- manageiq-client <https://github.com/ManageIQ/manageiq-api-client-python/>

## [Parameters](manageiq_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **email**  string | The users’ E-mail address. |
| **group**  string | The name of the group to which the user belongs. |
| **manageiq_connection**  dictionary | ManageIQ connection configuration information. |
| **ca_cert**  aliases: ca_bundle_path  string | The path to a CA bundle file or directory with certificates. |
| **password**  string | ManageIQ password. `MIQ_PASSWORD` environment variable if set. Otherwise, required if no token is passed in. |
| **token**  string | ManageIQ token. `MIQ_TOKEN` environment variable if set. Otherwise, required if no username or password is passed in. |
| **url**  string | ManageIQ environment URL. `MIQ_URL` environment variable if set. Otherwise, it is required to pass it. |
| **username**  string | ManageIQ username. `MIQ_USERNAME` environment variable if set. Otherwise, required if no token is passed in. |
| **validate_certs**  aliases: verify_ssl  boolean | Whether SSL certificates should be verified for HTTPS requests.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string | The users’ full name. |
| **password**  string | The users’ password. |
| **state**  string | absent - user should not exist, present - user should be.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **update_password**  string | `always` will update passwords unconditionally. `on_create` will only set the password for a newly created user.  **Choices:**   - `"always"` ← (default) - `"on_create"` |
| **userid**  string / required | The unique userid in manageiq, often mentioned as username. |

## [Attributes](manageiq_user_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](manageiq_user_module.md#id5)

```yaml+jinja
- name: Create a new user in ManageIQ
  community.general.manageiq_user:
    userid: 'jdoe'
    name: 'Jane Doe'
    password: 'VerySecret'
    group: 'EvmGroup-user'
    email: 'jdoe@example.com'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Create a new user in ManageIQ using a token
  community.general.manageiq_user:
    userid: 'jdoe'
    name: 'Jane Doe'
    password: 'VerySecret'
    group: 'EvmGroup-user'
    email: 'jdoe@example.com'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      token: 'sometoken'
      validate_certs: false

- name: Delete a user in ManageIQ
  community.general.manageiq_user:
    state: 'absent'
    userid: 'jdoe'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Delete a user in ManageIQ using a token
  community.general.manageiq_user:
    state: 'absent'
    userid: 'jdoe'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      token: 'sometoken'
      validate_certs: false

- name: Update email of user in ManageIQ
  community.general.manageiq_user:
    userid: 'jdoe'
    email: 'jaustine@example.com'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      username: 'admin'
      password: 'smartvm'
      validate_certs: false

- name: Update email of user in ManageIQ using a token
  community.general.manageiq_user:
    userid: 'jdoe'
    email: 'jaustine@example.com'
    manageiq_connection:
      url: 'http://127.0.0.1:3000'
      token: 'sometoken'
      validate_certs: false
```

### Authors

- Daniel Korn (@dkorn)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
