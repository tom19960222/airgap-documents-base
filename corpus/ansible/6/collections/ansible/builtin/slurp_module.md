---
collection: ansible
version: "6"
title: "ansible.builtin.slurp module – Slurps a file from remote nodes"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/slurp_module.html
fetched_at: 2026-07-27T16:44:08+00:00
---
# ansible.builtin.slurp module – Slurps a file from remote nodes

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `slurp` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](slurp_module.md#synopsis)
- [Parameters](slurp_module.md#parameters)
- [Attributes](slurp_module.md#attributes)
- [Notes](slurp_module.md#notes)
- [See Also](slurp_module.md#see-also)
- [Examples](slurp_module.md#examples)
- [Return Values](slurp_module.md#return-values)

## [Synopsis](slurp_module.md#id1)

- This module works like [ansible.builtin.fetch](fetch_module.md#ansible-collections-ansible-builtin-fetch-module). It is used for fetching a base64- encoded blob containing the data in a remote file.
- This module is also supported for Windows targets.

## [Parameters](slurp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **src**  aliases: path  path / required | The file on the remote system to fetch. This *must* be a file, not a directory. |

## [Attributes](slurp_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | Support: full | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | Support: none | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | Platforms: posix, windows | Target OS/families that can be operated against |

## [Notes](slurp_module.md#id4)

> **Note:**
>
> - This module returns an ‘in memory’ base64 encoded version of the file, take into account that this will require at least twice the RAM as the original file size.

## [See Also](slurp_module.md#id5)

> **See also:**
>
> [ansible.builtin.fetch](fetch_module.md#ansible-collections-ansible-builtin-fetch-module)
> :   Fetch files from remote nodes.

## [Examples](slurp_module.md#id6)

```yaml+jinja
- name: Find out what the remote machine's mounts are
  ansible.builtin.slurp:
    src: /proc/mounts
  register: mounts

- name: Print returned information
  ansible.builtin.debug:
    msg: "{{ mounts['content'] | b64decode }}"

# From the commandline, find the pid of the remote machine's sshd
# $ ansible host -m ansible.builtin.slurp -a 'src=/var/run/sshd.pid'
# host | SUCCESS => {
#     "changed": false,
#     "content": "MjE3OQo=",
#     "encoding": "base64",
#     "source": "/var/run/sshd.pid"
# }
# $ echo MjE3OQo= | base64 -d
# 2179
```

## [Return Values](slurp_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **content**  string | Encoded file content  Returned: success  Sample: `"MjE3OQo="` |
| **encoding**  string | Type of encoding used for file  Returned: success  Sample: `"base64"` |
| **source**  string | Actual path of file slurped  Returned: success  Sample: `"/var/run/sshd.pid"` |

### Authors

- Ansible Core Team
- Michael DeHaan (@mpdehaan)

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
