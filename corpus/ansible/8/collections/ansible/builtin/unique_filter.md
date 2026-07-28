---
collection: ansible
version: "8"
title: "ansible.builtin.unique filter – set of unique items of a list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/unique_filter.html
fetched_at: 2026-07-28T01:08:23+00:00
---
# ansible.builtin.unique filter – set of unique items of a list

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `unique`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.unique` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](unique_filter.md#synopsis)
- [Input](unique_filter.md#input)
- [See Also](unique_filter.md#see-also)
- [Examples](unique_filter.md#examples)
- [Return Value](unique_filter.md#return-value)

## [Synopsis](unique_filter.md#id1)

- Creates a list of unique elements (a set) from the provided input list.

## [Input](unique_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.unique`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | A list. |

## [See Also](unique_filter.md#id3)

> **See also:**
>
> [ansible.builtin.difference](difference_filter.md#ansible-collections-ansible-builtin-difference-filter) filter plugin
> :   the difference of one list from another.
>
> [ansible.builtin.intersect](intersect_filter.md#ansible-collections-ansible-builtin-intersect-filter) filter plugin
> :   intersection of lists.
>
> [ansible.builtin.symmetric_difference](symmetric_difference_filter.md#ansible-collections-ansible-builtin-symmetric-difference-filter) filter plugin
> :   different items from two lists.
>
> [ansible.builtin.union](union_filter.md#ansible-collections-ansible-builtin-union-filter) filter plugin
> :   union of lists.

## [Examples](unique_filter.md#id4)

```yaml+jinja
# return only the unique elements of list1
# list1: [1, 2, 5, 1, 3, 4, 10]
{{ list1 | unique }}
# => [1, 2, 5, 3, 4, 10]
```

## [Return Value](unique_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A list with unique elements, also known as a set.  **Returned:** success |

### Authors

- Brian Coca (@bcoca)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
