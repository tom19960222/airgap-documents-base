---
collection: ansible
version: "8"
title: "ansible.builtin.relpath filter – Make a path relative"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/relpath_filter.html
fetched_at: 2026-07-28T01:08:16+00:00
---
# ansible.builtin.relpath filter – Make a path relative

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `relpath`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.relpath` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](relpath_filter.md#synopsis)
- [Input](relpath_filter.md#input)
- [Positional parameters](relpath_filter.md#positional-parameters)
- [Examples](relpath_filter.md#examples)
- [Return Value](relpath_filter.md#return-value)

## [Synopsis](relpath_filter.md#id1)

- Converts the given path to a relative path from the *start*, or relative to the directory given in *start*.

## [Input](relpath_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.relpath`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A path. |

## [Positional parameters](relpath_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.relpath(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **start**  string | The directory the path should be relative to. If not supplied the current working directory will be used. |

## [Examples](relpath_filter.md#id4)

```yaml+jinja
# foobar => ../test/me.txt
testing: "{{ '/tmp/test/me.txt' | relpath('/tmp/other/') }}"
otherrelpath: "{{ mypath | relpath(mydir) }}"
```

## [Return Value](relpath_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | The relative path.  **Returned:** success |

### Authors

- Jakub Jirutka (@jirutka)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
