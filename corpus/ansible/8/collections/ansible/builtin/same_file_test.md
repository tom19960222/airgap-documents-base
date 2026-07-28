---
collection: ansible
version: "8"
title: "ansible.builtin.same_file test – compares two paths to see if they resolve to the same filesystem object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/same_file_test.html
fetched_at: 2026-07-28T01:08:55+00:00
---
# ansible.builtin.same_file test – compares two paths to see if they resolve to the same filesystem object

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `same_file`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.same_file` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](same_file_test.md#synopsis)
- [Input](same_file_test.md#input)
- [Keyword parameters](same_file_test.md#keyword-parameters)
- [Examples](same_file_test.md#examples)
- [Return Value](same_file_test.md#return-value)

## [Synopsis](same_file_test.md#id1)

- Check if the provided paths map to the same location on the controller’s filesystem (localhost).

Aliases: is_file, is_same_file

## [Input](same_file_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.same_file` or `is not ansible.builtin.same_file`.

| Parameter | Comments |
| --- | --- |
| **Input**  path / required | A path. |

## [Keyword parameters](same_file_test.md#id3)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.builtin.same_file(key1=value1, key2=value2, ...)` and `input is not ansible.builtin.same_file(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **_path2**  path / required | Another path. |

## [Examples](same_file_test.md#id4)

```yaml+jinja
amionelevelfromroot: "{{ '/etc/hosts' is same_file('../etc/hosts') }}"
```

## [Return Value](same_file_test.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the paths correspond to the same location on the filesystem on the controller, `False` if otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
