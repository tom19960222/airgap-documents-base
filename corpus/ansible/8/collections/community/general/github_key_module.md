---
collection: ansible
version: "8"
title: "community.general.github_key module – Manage GitHub access keys"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/github_key_module.html
fetched_at: 2026-07-28T01:45:42+00:00
---
# community.general.github_key module – Manage GitHub access keys

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
> To use it in a playbook, specify: `community.general.github_key`.

- [Synopsis](github_key_module.md#synopsis)
- [Parameters](github_key_module.md#parameters)
- [Attributes](github_key_module.md#attributes)
- [Examples](github_key_module.md#examples)
- [Return Values](github_key_module.md#return-values)

## [Synopsis](github_key_module.md#id1)

- Creates, removes, or updates GitHub access keys.

Aliases: source_control.github.github_key

## [Parameters](github_key_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **force**  boolean | The default is `true`, which will replace the existing remote key if it is different than `pubkey`. If `false`, the key will only be set if no key with the given `name` exists.  **Choices:**   - `false` - `true` ← (default) |
| **name**  string / required | SSH key name |
| **pubkey**  string | SSH public key value. Required when `state=present`. |
| **state**  string | Whether to remove a key, ensure that it exists, or update its value.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **token**  string / required | GitHub Access Token with permission to list and create public keys. |

## [Attributes](github_key_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](github_key_module.md#id4)

```yaml+jinja
- name: Read SSH public key to authorize
  ansible.builtin.shell: cat /home/foo/.ssh/id_rsa.pub
  register: ssh_pub_key

- name: Authorize key with GitHub
  local_action:
    module: github_key
    name: Access Key for Some Machine
    token: '{{ github_access_token }}'
    pubkey: '{{ ssh_pub_key.stdout }}'

# Alternatively, a single task can be used reading a key from a file on the controller
- name: Authorize key with GitHub
  community.general.github_key:
    name: Access Key for Some Machine
    token: '{{ github_access_token }}'
    pubkey: "{{ lookup('ansible.builtin.file', '/home/foo/.ssh/id_rsa.pub') }}"
```

## [Return Values](github_key_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **deleted_keys**  list / elements=string | An array of key objects that were deleted. Only present on state=absent  **Returned:** When state=absent  **Sample:** `[{"created_at": "YYYY-MM-DDTHH:MM:SZ", "id": 0, "key": "BASE64 encoded key", "read_only": false, "url": "http://example.com/github key"}]` |
| **key**  dictionary | Metadata about the key just created. Only present on state=present  **Returned:** success  **Sample:** `{"created_at": "YYYY-MM-DDTHH:MM:SZ", "id": 0, "key": "BASE64 encoded key", "read_only": false, "url": "http://example.com/github key"}` |
| **matching_keys**  list / elements=string | An array of keys matching the specified name. Only present on state=present  **Returned:** When state=present  **Sample:** `[{"created_at": "YYYY-MM-DDTHH:MM:SZ", "id": 0, "key": "BASE64 encoded key", "read_only": false, "url": "http://example.com/github key"}]` |

### Authors

- Robert Estelle (@erydo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
