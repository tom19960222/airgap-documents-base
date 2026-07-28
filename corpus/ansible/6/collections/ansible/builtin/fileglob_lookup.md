---
collection: ansible
version: "6"
title: "ansible.builtin.fileglob lookup – list files matching a pattern"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/fileglob_lookup.html
fetched_at: 2026-07-27T16:43:14+00:00
---
# ansible.builtin.fileglob lookup – list files matching a pattern

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `fileglob` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](fileglob_lookup.md#synopsis)
- [Terms](fileglob_lookup.md#terms)
- [Notes](fileglob_lookup.md#notes)
- [Examples](fileglob_lookup.md#examples)
- [Return Value](fileglob_lookup.md#return-value)

## [Synopsis](fileglob_lookup.md#id1)

- Matches all files in a single directory, non-recursively, that match a pattern. It calls Python’s “glob” library.

## [Terms](fileglob_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | path(s) of files to read |

## [Notes](fileglob_lookup.md#id3)

> **Note:**
>
> - Patterns are only supported on files, not directory/paths.
> - Matching is against local system files on the Ansible controller. To iterate a list of files on a remote node, use the [ansible.builtin.find](find_module.md#ansible-collections-ansible-builtin-find-module) module.
> - Returns a string list of paths joined by commas, or an empty list if no files match. For a ‘true list’ pass `wantlist=True` to the lookup.

## [Examples](fileglob_lookup.md#id4)

```yaml+jinja
- name: Display paths of all .txt files in dir
  ansible.builtin.debug: msg={{ lookup('ansible.builtin.fileglob', '/my/path/*.txt') }}

- name: Copy each file over that matches the given pattern
  ansible.builtin.copy:
    src: "{{ item }}"
    dest: "/etc/fooapp/"
    owner: "root"
    mode: 0600
  with_fileglob:
    - "/playbooks/files/fooapp/*"
```

## [Return Value](fileglob_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=path | list of files  Returned: success |

### Authors

- Michael DeHaan

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
