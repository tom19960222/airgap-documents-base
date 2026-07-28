---
collection: ansible
version: "8"
title: "ansible.builtin.zip filter – combine list elements"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/zip_filter.html
fetched_at: 2026-07-28T01:04:47+00:00
---
# ansible.builtin.zip filter – combine list elements

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `zip`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.zip` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](zip_filter.md#synopsis)
- [Input](zip_filter.md#input)
- [Positional parameters](zip_filter.md#positional-parameters)
- [Keyword parameters](zip_filter.md#keyword-parameters)
- [Notes](zip_filter.md#notes)
- [Examples](zip_filter.md#examples)
- [Return Value](zip_filter.md#return-value)

## [Synopsis](zip_filter.md#id1)

- Iterate over several iterables in parallel, producing tuples with an item from each one.

## [Input](zip_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.zip`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=any / required | Original list. |

## [Positional parameters](zip_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.zip(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **_additional_lists**  list / elements=any / required | Additional list(s). |

## [Keyword parameters](zip_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.zip(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **strict**  boolean | If `True` return an error on mismatching list length, otherwise shortest list determines output.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](zip_filter.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | ansible.builtin.zip(positional1, positional2, key1=value1, key2=value2)`
> - This is mostly a passhtrough to Python’s `zip` function.

## [Examples](zip_filter.md#id6)

```yaml+jinja
# two => [[1, "a"], [2, "b"], [3, "c"], [4, "d"], [5, "e"], [6, "f"]]
two: "{{ [1,2,3,4,5,6] | zip(['a','b','c','d','e','f']) }}"

# three => [ [ 1, "a", "d" ], [ 2, "b", "e" ], [ 3, "c", "f" ] ]
three: "{{ [1,2,3] | zip(['a','b','c'], ['d','e','f']) }}"

# shorter => [[1, "a"], [2, "b"], [3, "c"]]
shorter: "{{ [1,2,3] | zip(['a','b','c','d','e','f']) }}"

# compose dict from lists of keys and values
mydcit: "{{ dict(keys_list | zip(values_list)) }}"
```

## [Return Value](zip_filter.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=list | List of lists made of elements matching the positions of the input lists.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
