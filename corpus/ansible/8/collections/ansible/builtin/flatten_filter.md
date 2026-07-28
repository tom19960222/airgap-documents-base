---
collection: ansible
version: "8"
title: "ansible.builtin.flatten filter – flatten lists within a list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/flatten_filter.html
fetched_at: 2026-07-28T01:08:05+00:00
---
# ansible.builtin.flatten filter – flatten lists within a list

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `flatten`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.flatten` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](flatten_filter.md#synopsis)
- [Input](flatten_filter.md#input)
- [Positional parameters](flatten_filter.md#positional-parameters)
- [Examples](flatten_filter.md#examples)
- [Return Value](flatten_filter.md#return-value)

## [Synopsis](flatten_filter.md#id1)

- For a given list, take any elements that are lists and insert their elements into the parent list directly.

## [Input](flatten_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.flatten`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | First dictionary to combine. |

## [Positional parameters](flatten_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.flatten(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **levels**  integer | Number of recursive list depths to flatten. |
| **skip_nulls**  boolean | Skip `null`/`None` elements when inserting into the top list.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](flatten_filter.md#id4)

```yaml+jinja
# [1,2,3,4,5,6]
flat: "{{ [1 , 2, [3, [4, 5]], 6] | flatten }}"

# [1,2,3,[4,5],6]
flatone: "{{ [1, 2, [3, [4, 5]], 6] | flatten(1) }}"
```

## [Return Value](flatten_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | The flattened list.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
