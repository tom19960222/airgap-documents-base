---
collection: ansible
version: "8"
title: "ansible.posix.authorized_key module – Adds or removes an SSH authorized key"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/posix/authorized_key_module.html
fetched_at: 2026-07-28T01:09:25+00:00
---
# ansible.posix.authorized_key module – Adds or removes an SSH authorized key

> **Note:**
>
> This module is part of the [ansible.posix collection](https://galaxy.ansible.com/ui/repo/published/ansible/posix/) (version 1.5.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.posix`.
>
> To use it in a playbook, specify: `ansible.posix.authorized_key`.

New in ansible.posix 1.0.0

- [Synopsis](authorized_key_module.md#synopsis)
- [Parameters](authorized_key_module.md#parameters)
- [Examples](authorized_key_module.md#examples)
- [Return Values](authorized_key_module.md#return-values)

## [Synopsis](authorized_key_module.md#id1)

- Adds or removes SSH authorized keys for particular user accounts.

## [Parameters](authorized_key_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **comment**  string | Change the comment on the public key.  Rewriting the comment is useful in cases such as fetching it from GitHub or GitLab.  If no comment is specified, the existing comment will be kept. |
| **exclusive**  boolean | Whether to remove all other non-specified keys from the authorized_keys file.  Multiple keys can be specified in a single `key` string value by separating them by newlines.  This option is not loop aware, so if you use `with_` , it will be exclusive per iteration of the loop.  If you want multiple keys in the file you need to pass them all to `key` in a single batch as mentioned above.  **Choices:**   - `false` ← (default) - `true` |
| **follow**  boolean | Follow path symlink instead of replacing it.  **Choices:**   - `false` ← (default) - `true` |
| **key**  string / required | The SSH public key(s), as a string or (since Ansible 1.9) url (<https://github.com/username.keys>). |
| **key_options**  string | A string of ssh key options to be prepended to the key in the authorized_keys file. |
| **manage_dir**  boolean | Whether this module should manage the directory of the authorized key file.  If set to `true`, the module will create the directory, as well as set the owner and permissions of an existing directory.  Be sure to set `manage_dir=false` if you are using an alternate directory for authorized_keys, as set with `path`, since you could lock yourself out of SSH access.  See the example below.  **Choices:**   - `false` - `true` ← (default) |
| **path**  path | Alternate path to the authorized_keys file.  When unset, this value defaults to *~/.ssh/authorized_keys*. |
| **state**  string | Whether the given key (with the given key_options) should or should not be in the file.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **user**  string / required | The username on the remote host whose authorized_keys file will be modified. |
| **validate_certs**  boolean | This only applies if using a https url as the source of the keys.  If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates as it avoids verifying the source site.  Prior to 2.1 the code worked as if this was set to `true`.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](authorized_key_module.md#id3)

```yaml+jinja
- name: Set authorized key taken from file
  ansible.posix.authorized_key:
    user: charlie
    state: present
    key: "{{ lookup('file', '/home/charlie/.ssh/id_rsa.pub') }}"

- name: Set authorized keys taken from url
  ansible.posix.authorized_key:
    user: charlie
    state: present
    key: https://github.com/charlie.keys

- name: Set authorized keys taken from url using lookup
  ansible.posix.authorized_key:
    user: charlie
    state: present
    key: "{{ lookup('url', 'https://github.com/charlie.keys', split_lines=False) }}"

- name: Set authorized key in alternate location
  ansible.posix.authorized_key:
    user: charlie
    state: present
    key: "{{ lookup('file', '/home/charlie/.ssh/id_rsa.pub') }}"
    path: /etc/ssh/authorized_keys/charlie
    manage_dir: false

- name: Set up multiple authorized keys
  ansible.posix.authorized_key:
    user: deploy
    state: present
    key: '{{ item }}'
  with_file:
    - public_keys/doe-jane
    - public_keys/doe-john

- name: Set authorized key defining key options
  ansible.posix.authorized_key:
    user: charlie
    state: present
    key: "{{ lookup('file', '/home/charlie/.ssh/id_rsa.pub') }}"
    key_options: 'no-port-forwarding,from="10.0.1.1"'

- name: Set authorized key without validating the TLS/SSL certificates
  ansible.posix.authorized_key:
    user: charlie
    state: present
    key: https://github.com/user.keys
    validate_certs: false

- name: Set authorized key, removing all the authorized keys already set
  ansible.posix.authorized_key:
    user: root
    key: "{{ lookup('file', 'public_keys/doe-jane') }}"
    state: present
    exclusive: true

- name: Set authorized key for user ubuntu copying it from current user
  ansible.posix.authorized_key:
    user: ubuntu
    state: present
    key: "{{ lookup('file', lookup('env','HOME') + '/.ssh/id_rsa.pub') }}"
```

## [Return Values](authorized_key_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **exclusive**  boolean | If the key has been forced to be exclusive or not.  **Returned:** success  **Sample:** `false` |
| **key**  string | The key that the module was running against.  **Returned:** success  **Sample:** `"https://github.com/user.keys"` |
| **key_option**  string | Key options related to the key.  **Returned:** success |
| **keyfile**  string | Path for authorized key file.  **Returned:** success  **Sample:** `"/home/user/.ssh/authorized_keys"` |
| **manage_dir**  boolean | Whether this module managed the directory of the authorized key file.  **Returned:** success  **Sample:** `true` |
| **path**  string | Alternate path to the authorized_keys file  **Returned:** success |
| **state**  string | Whether the given key (with the given key_options) should or should not be in the file  **Returned:** success  **Sample:** `"present"` |
| **unique**  boolean | Whether the key is unique  **Returned:** success  **Sample:** `false` |
| **user**  string | The username on the remote host whose authorized_keys file will be modified  **Returned:** success  **Sample:** `"user"` |
| **validate_certs**  boolean | This only applies if using a https url as the source of the keys. If set to `false`, the SSL certificates will not be validated.  **Returned:** success  **Sample:** `true` |

### Authors

- Ansible Core Team

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.posix)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.posix)
