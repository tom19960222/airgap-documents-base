---
collection: ansible
version: "8"
title: "ansible.builtin.abs test – is the path absolute"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/abs_test.html
fetched_at: 2026-07-28T01:08:42+00:00
---
# ansible.builtin.abs test – is the path absolute

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `abs`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.abs` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](abs_test.md#synopsis)
- [Input](abs_test.md#input)
- [Examples](abs_test.md#examples)
- [Return Value](abs_test.md#return-value)

## [Synopsis](abs_test.md#id1)

- Check if the provided path is absolute, not relative.
- An absolute path expresses the location of a filesystem object starting at the filesystem root and requires no context.
- A relative path does not start at the filesystem root and requires a ‘current’ directory as a context to resolve.

Aliases: is_abs

## [Input](abs_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.abs` or `is not ansible.builtin.abs`.

| Parameter | Comments |
| --- | --- |
| **Input**  path | A path. |

## [Examples](abs_test.md#id3)

```yaml+jinja
is_path_absolute: "{{ '/etc/hosts' is abs }}}"
relative_paths: "{{ all_paths | reject('abs') }}"
```

## [Return Value](abs_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the path is absolute, `False` if it is relative.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
