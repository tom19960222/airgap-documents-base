---
collection: ansible
version: "8"
title: "community.general.bitbucket_access_key module – Manages Bitbucket repository access keys"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/bitbucket_access_key_module.html
fetched_at: 2026-07-28T01:44:48+00:00
---
# community.general.bitbucket_access_key module – Manages Bitbucket repository access keys

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.bitbucket_access_key`.

- [Synopsis](bitbucket_access_key_module.md#synopsis)
- [Parameters](bitbucket_access_key_module.md#parameters)
- [Attributes](bitbucket_access_key_module.md#attributes)
- [Notes](bitbucket_access_key_module.md#notes)
- [Examples](bitbucket_access_key_module.md#examples)

## [Synopsis](bitbucket_access_key_module.md#id1)

- Manages Bitbucket repository access keys (also called deploy keys).

Aliases: source_control.bitbucket.bitbucket_access_key

## [Parameters](bitbucket_access_key_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **client_id**  string | The OAuth consumer key.  If not set the environment variable `BITBUCKET_CLIENT_ID` will be used. |
| **client_secret**  string | The OAuth consumer secret.  If not set the environment variable `BITBUCKET_CLIENT_SECRET` will be used. |
| **key**  string | The SSH public key. |
| **label**  string / required | The key label. |
| **password**  string  *added in community.general 4.0.0* | The App password.  If not set the environment variable `BITBUCKET_PASSWORD` will be used. |
| **repository**  string / required | The repository name. |
| **state**  string / required | Indicates desired state of the access key.  **Choices:**   - `"absent"` - `"present"` |
| **user**  aliases: username  string  *added in community.general 4.0.0* | The username.  If not set the environment variable `BITBUCKET_USERNAME` will be used.  `username` is an alias of `user` since community.general 6.0.0. It was an alias of `workspace` before. |
| **workspace**  string / required | The repository owner.  **Note:** `username` used to be an alias of this option. Since community.general 6.0.0 it is an alias of `user`. |

## [Attributes](bitbucket_access_key_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](bitbucket_access_key_module.md#id4)

> **Note:**
>
> - Bitbucket OAuth consumer or App password should have permissions to read and administrate account repositories.
> - Check mode is supported.
> - Bitbucket OAuth consumer key and secret can be obtained from Bitbucket profile -> Settings -> Access Management -> OAuth.
> - Bitbucket App password can be created from Bitbucket profile -> Personal Settings -> App passwords.
> - If both OAuth and Basic Auth credentials are passed, OAuth credentials take precedence.

## [Examples](bitbucket_access_key_module.md#id5)

```yaml+jinja
- name: Create access key
  community.general.bitbucket_access_key:
    repository: 'bitbucket-repo'
    workspace: bitbucket_workspace
    key: '{{lookup("file", "bitbucket.pub") }}'
    label: 'Bitbucket'
    state: present

- name: Delete access key
  community.general.bitbucket_access_key:
    repository: bitbucket-repo
    workspace: bitbucket_workspace
    label: Bitbucket
    state: absent
```

### Authors

- Evgeniy Krysanov (@catcombo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
