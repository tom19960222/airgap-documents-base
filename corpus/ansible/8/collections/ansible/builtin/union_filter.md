---
collection: ansible
version: "8"
title: "ansible.builtin.union filter – union of lists"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/union_filter.html
fetched_at: 2026-07-28T01:08:22+00:00
---
# ansible.builtin.union filter – union of lists

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `union`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.union` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](union_filter.md#synopsis)
- [Input](union_filter.md#input)
- [Keyword parameters](union_filter.md#keyword-parameters)
- [See Also](union_filter.md#see-also)
- [Examples](union_filter.md#examples)
- [Return Value](union_filter.md#return-value)

## [Synopsis](union_filter.md#id1)

- Provide a unique list of all the elements of two lists.

## [Input](union_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.union`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | A list. |

## [Keyword parameters](union_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.union(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **_second_list**  list / elements=string / required | A list. |

## [See Also](union_filter.md#id4)

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
> [ansible.builtin.unique](unique_filter.md#ansible-collections-ansible-builtin-unique-filter) filter plugin
> :   set of unique items of a list.

## [Examples](union_filter.md#id5)

```yaml+jinja
# return the unique elements of list1 added to list2
# list1: [1, 2, 5, 1, 3, 4, 10]
# list2: [1, 2, 3, 4, 5, 11, 99]
{{ list1 | union(list2) }}
# => [1, 2, 5, 1, 3, 4, 10, 11, 99]
```

## [Return Value](union_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A unique list of all the elements from both lists.  **Returned:** success |

### Authors

- Brian Coca (@bcoca)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
