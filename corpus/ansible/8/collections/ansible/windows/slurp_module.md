---
collection: ansible
version: "8"
title: "ansible.windows.slurp module – Slurps a file from remote nodes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/windows/slurp_module.html
fetched_at: 2026-07-28T01:10:27+00:00
---
# ansible.windows.slurp module – Slurps a file from remote nodes

> **Note:**
>
> This module is part of the [ansible.windows collection](https://galaxy.ansible.com/ui/repo/published/ansible/windows/) (version 1.14.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ansible.windows`.
>
> To use it in a playbook, specify: `ansible.windows.slurp`.

- [Synopsis](slurp_module.md#synopsis)
- [Parameters](slurp_module.md#parameters)
- [Notes](slurp_module.md#notes)
- [See Also](slurp_module.md#see-also)
- [Examples](slurp_module.md#examples)
- [Return Values](slurp_module.md#return-values)

## [Synopsis](slurp_module.md#id1)

- This module works like [ansible.builtin.fetch](../builtin/fetch_module.md#ansible-collections-ansible-builtin-fetch-module). It is used for fetching a base64- encoded blob containing the data in a remote file.

## [Parameters](slurp_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **src**  aliases: path  path / required | The file on the remote system to fetch. This *must* be a file, not a directory. |

## [Notes](slurp_module.md#id3)

> **Note:**
>
> - This module returns an ‘in memory’ base64 encoded version of the file, take into account that this will require at least twice the RAM as the original file size.

## [See Also](slurp_module.md#id4)

> **See also:**
>
> [ansible.builtin.fetch](../builtin/fetch_module.md#ansible-collections-ansible-builtin-fetch-module)
> :   Fetch files from remote nodes.
>
> [ansible.builtin.slurp](../builtin/slurp_module.md#ansible-collections-ansible-builtin-slurp-module)
> :   Slurps a file from remote nodes.

## [Examples](slurp_module.md#id5)

```yaml+jinja
- name: Retrieve remote ini file on a Windows host
  ansible.builtin.slurp:
    src: C:\Program Files\Program\program.ini
  register: program_conf

- name: Print returned information
  ansible.builtin.debug:
    msg: "{{ program_conf['content'] | b64decode }}"
```

## [Return Values](slurp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **content**  string | Encoded file content  **Returned:** success  **Sample:** `"MjE3OQo="` |
| **encoding**  string | Type of encoding used for file  **Returned:** success  **Sample:** `"base64"` |
| **source**  string | Actual path of file slurped  **Returned:** success  **Sample:** `"C:\\Program Files\\Program\\program.ini"` |

### Authors

- Ansible Core Team

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/ansible.windows/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/ansible.windows)
- [Communication](index.md#communication-for-ansible-windows)
