---
collection: ansible
version: "6"
title: "community.general.pacman_key module – Manage pacman’s list of trusted keys"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/pacman_key_module.html
fetched_at: 2026-07-27T17:11:44+00:00
---
# community.general.pacman_key module – Manage pacman’s list of trusted keys

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](pacman_key_module.md#ansible-collections-community-general-pacman-key-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.pacman_key`.

New in community.general 3.2.0

- [Synopsis](pacman_key_module.md#synopsis)
- [Requirements](pacman_key_module.md#requirements)
- [Parameters](pacman_key_module.md#parameters)
- [Notes](pacman_key_module.md#notes)
- [Examples](pacman_key_module.md#examples)

## [Synopsis](pacman_key_module.md#id1)

- Add or remove gpg keys from the pacman keyring.

## [Requirements](pacman_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- gpg
- pacman-key

## [Parameters](pacman_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **data**  string | The keyfile contents to add to the keyring.  Must be of `PGP PUBLIC KEY BLOCK` type. |
| **file**  path | The path to a keyfile on the remote server to add to the keyring.  Remote file must be of `PGP PUBLIC KEY BLOCK` type. |
| **force_update**  boolean | This forces the key to be updated if it already exists in the keyring.  Choices:   - `false` ← (default) - `true` |
| **id**  string / required | The 40 character identifier of the key.  Including this allows check mode to correctly report the changed state.  Do not specify a subkey ID, instead specify the primary key ID. |
| **keyring**  path | The full path to the keyring folder on the remote server.  If not specified, module will use pacman’s default (`/etc/pacman.d/gnupg`).  Useful if the remote system requires an alternative gnupg directory.  Default: `"/etc/pacman.d/gnupg"` |
| **keyserver**  string | The keyserver used to retrieve key from. |
| **state**  string | Ensures that the key is present (added) or absent (revoked).  Choices:   - `"absent"` - `"present"` ← (default) |
| **url**  string | The URL to retrieve keyfile from.  Remote file must be of `PGP PUBLIC KEY BLOCK` type. |
| **verify**  boolean | Whether or not to verify the keyfile’s key ID against specified key ID.  Choices:   - `false` - `true` ← (default) |

## [Notes](pacman_key_module.md#id4)

> **Note:**
>
> - Use full-length key ID (40 characters).
> - Keys will be verified when using *data*, *file*, or *url* unless *verify* is overridden.
> - Keys will be locally signed after being imported into the keyring.
> - If the key ID exists in the keyring, the key will not be added unless *force_update* is specified.
> - *data*, *file*, *url*, and *keyserver* are mutually exclusive.
> - Supports `check_mode`.

## [Examples](pacman_key_module.md#id5)

```yaml+jinja
- name: Import a key via local file
  community.general.pacman_key:
    data: "{{ lookup('file', 'keyfile.asc') }}"
    state: present

- name: Import a key via remote file
  community.general.pacman_key:
    file: /tmp/keyfile.asc
    state: present

- name: Import a key via url
  community.general.pacman_key:
    id: 01234567890ABCDE01234567890ABCDE12345678
    url: https://domain.tld/keys/keyfile.asc
    state: present

- name: Import a key via keyserver
  community.general.pacman_key:
    id: 01234567890ABCDE01234567890ABCDE12345678
    keyserver: keyserver.domain.tld

- name: Import a key into an alternative keyring
  community.general.pacman_key:
    id: 01234567890ABCDE01234567890ABCDE12345678
    file: /tmp/keyfile.asc
    keyring: /etc/pacman.d/gnupg-alternative

- name: Remove a key from the keyring
  community.general.pacman_key:
    id: 01234567890ABCDE01234567890ABCDE12345678
    state: absent
```

### Authors

- George Rawlinson (@grawlinson)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
