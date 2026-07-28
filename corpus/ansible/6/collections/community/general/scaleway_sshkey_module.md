---
collection: ansible
version: "6"
title: "community.general.scaleway_sshkey module – Scaleway SSH keys management module"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/scaleway_sshkey_module.html
fetched_at: 2026-07-27T17:13:04+00:00
---
# community.general.scaleway_sshkey module – Scaleway SSH keys management module

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.scaleway_sshkey`.

- [Synopsis](scaleway_sshkey_module.md#synopsis)
- [Parameters](scaleway_sshkey_module.md#parameters)
- [Notes](scaleway_sshkey_module.md#notes)
- [Examples](scaleway_sshkey_module.md#examples)
- [Return Values](scaleway_sshkey_module.md#return-values)

## [Synopsis](scaleway_sshkey_module.md#id1)

- This module manages SSH keys on Scaleway account <https://developer.scaleway.com>

## [Parameters](scaleway_sshkey_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_timeout**  aliases: timeout  integer | HTTP timeout to Scaleway API in seconds.  Default: `30` |
| **api_token**  aliases: oauth_token  string / required | Scaleway OAuth token. |
| **api_url**  aliases: base_url  string | Scaleway API URL  Default: `"https://account.scaleway.com"` |
| **query_parameters**  dictionary | List of parameters passed to the query string.  Default: `{}` |
| **ssh_pub_key**  string / required | The public SSH key as a string to add. |
| **state**  string | Indicate desired state of the SSH key.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Scaleway API.  Choices:   - `false` - `true` ← (default) |

## [Notes](scaleway_sshkey_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://developer.scaleway.com/>
> - If `api_token` is not set within the module, the following environment variables can be used in decreasing order of precedence `SCW_TOKEN`, `SCW_API_KEY`, `SCW_OAUTH_TOKEN` or `SCW_API_TOKEN`.
> - If one wants to use a different `api_url` one can also set the `SCW_API_URL` environment variable.

## [Examples](scaleway_sshkey_module.md#id4)

```yaml+jinja
- name: "Add SSH key"
  community.general.scaleway_sshkey:
    ssh_pub_key: "ssh-rsa AAAA..."
    state: "present"

- name: "Delete SSH key"
  community.general.scaleway_sshkey:
    ssh_pub_key: "ssh-rsa AAAA..."
    state: "absent"

- name: "Add SSH key with explicit token"
  community.general.scaleway_sshkey:
    ssh_pub_key: "ssh-rsa AAAA..."
    state: "present"
    oauth_token: "6ecd2c9b-6f4f-44d4-a187-61a92078d08c"
```

## [Return Values](scaleway_sshkey_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  dictionary | This is only present when `state=present`  Returned: when `state=present`  Sample: `{"ssh_public_keys": [{"key": "ssh-rsa AAAA...."}]}` |

### Authors

- Remy Leone (@remyleone)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
