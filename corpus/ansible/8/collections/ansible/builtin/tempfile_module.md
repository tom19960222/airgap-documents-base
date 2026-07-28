---
collection: ansible
version: "8"
title: "ansible.builtin.tempfile module – Creates temporary files and directories"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/tempfile_module.html
fetched_at: 2026-07-28T01:07:47+00:00
---
# ansible.builtin.tempfile module – Creates temporary files and directories

> **Note:**
>
> This module is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> module name
> `tempfile` even without specifying the [collections keyword](../../../collections_guide/collections_using_playbooks.md#collections-keyword).
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.tempfile` for easy linking to the
> module documentation and to avoid conflicting with other collections that may have
> the same module name.

- [Synopsis](tempfile_module.md#synopsis)
- [Parameters](tempfile_module.md#parameters)
- [Attributes](tempfile_module.md#attributes)
- [See Also](tempfile_module.md#see-also)
- [Examples](tempfile_module.md#examples)
- [Return Values](tempfile_module.md#return-values)

## [Synopsis](tempfile_module.md#id1)

- The `tempfile` module creates temporary files and directories. `mktemp` command takes different parameters on various systems, this module helps to avoid troubles related to that. Files/directories created by module are accessible only by creator. In case you need to make them world-accessible you need to use [ansible.builtin.file](file_module.md#ansible-collections-ansible-builtin-file-module) module.
- For Windows targets, use the [ansible.windows.win_tempfile](../windows/win_tempfile_module.md#ansible-collections-ansible-windows-win-tempfile-module) module instead.

## [Parameters](tempfile_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **path**  path | Location where temporary file or directory should be created.  If path is not specified, the default system temporary directory will be used. |
| **prefix**  string | Prefix of file/directory name created by module.  **Default:** `"ansible."` |
| **state**  string | Whether to create file or directory.  **Choices:**   - `"directory"` - `"file"` ← (default) |
| **suffix**  string | Suffix of file/directory name created by module.  **Default:** `""` |

## [Attributes](tempfile_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **posix** | Target OS/families that can be operated against |

## [See Also](tempfile_module.md#id4)

> **See also:**
>
> [ansible.builtin.file](file_module.md#ansible-collections-ansible-builtin-file-module)
> :   Manage files and file properties.
>
> [ansible.windows.win_tempfile](../windows/win_tempfile_module.md#ansible-collections-ansible-windows-win-tempfile-module)
> :   Creates temporary files and directories.

## [Examples](tempfile_module.md#id5)

```yaml+jinja
- name: Create temporary build directory
  ansible.builtin.tempfile:
    state: directory
    suffix: build

- name: Create temporary file
  ansible.builtin.tempfile:
    state: file
    suffix: temp
  register: tempfile_1

- name: Use the registered var and the file module to remove the temporary file
  ansible.builtin.file:
    path: "{{ tempfile_1.path }}"
    state: absent
  when: tempfile_1.path is defined
```

## [Return Values](tempfile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **path**  string | Path to created file or directory.  **Returned:** success  **Sample:** `"/tmp/ansible.bMlvdk"` |

### Authors

- Krzysztof Magosa (@krzysztof-magosa)

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
