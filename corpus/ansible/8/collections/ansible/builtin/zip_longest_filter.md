---
collection: ansible
version: "8"
title: "ansible.builtin.zip_longest filter – combine list elements, with filler"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/zip_longest_filter.html
fetched_at: 2026-07-28T01:04:48+00:00
---
# ansible.builtin.zip_longest filter – combine list elements, with filler

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `zip_longest`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.zip_longest` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](zip_longest_filter.md#synopsis)
- [Input](zip_longest_filter.md#input)
- [Positional parameters](zip_longest_filter.md#positional-parameters)
- [Keyword parameters](zip_longest_filter.md#keyword-parameters)
- [Notes](zip_longest_filter.md#notes)
- [Examples](zip_longest_filter.md#examples)
- [Return Value](zip_longest_filter.md#return-value)

## [Synopsis](zip_longest_filter.md#id1)

- Make an iterator that aggregates elements from each of the iterables. If the iterables are of uneven length, missing values are filled-in with *fillvalue*. Iteration continues until the longest iterable is exhausted.

## [Input](zip_longest_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.zip_longest`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=any / required | Original list. |

## [Positional parameters](zip_longest_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.zip_longest(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **_additional_lists**  list / elements=any / required | Additional list(s). |

## [Keyword parameters](zip_longest_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.zip_longest(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **fillvalue**  any | Filler value to add to output when one of the lists does not contain enough elements to match the others. |

## [Notes](zip_longest_filter.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | ansible.builtin.zip_longest(positional1, positional2, key1=value1, key2=value2)`
> - This is mostly a passhtrough to Python’s `itertools.zip_longest` function

## [Examples](zip_longest_filter.md#id6)

```yaml+jinja
# X_fill => [[1, "a", 21], [2, "b", 22], [3, "c", 23], ["X", "d", "X"], ["X", "e", "X"], ["X", "f", "X"]]
X_fill: "{{ [1,2,3] | zip_longest(['a','b','c','d','e','f'], [21, 22, 23], fillvalue='X') }}"
```

## [Return Value](zip_longest_filter.md#id7)

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
