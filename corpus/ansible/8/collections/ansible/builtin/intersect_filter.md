---
collection: ansible
version: "8"
title: "ansible.builtin.intersect filter – intersection of lists"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/intersect_filter.html
fetched_at: 2026-07-28T01:08:08+00:00
---
# ansible.builtin.intersect filter – intersection of lists

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `intersect`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.intersect` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](intersect_filter.md#synopsis)
- [Input](intersect_filter.md#input)
- [Keyword parameters](intersect_filter.md#keyword-parameters)
- [See Also](intersect_filter.md#see-also)
- [Examples](intersect_filter.md#examples)
- [Return Value](intersect_filter.md#return-value)

## [Synopsis](intersect_filter.md#id1)

- Provide a list with the common elements from other lists.

## [Input](intersect_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.intersect`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | A list. |

## [Keyword parameters](intersect_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.intersect(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **_second_list**  list / elements=string / required | A list. |

## [See Also](intersect_filter.md#id4)

> **See also:**
>
> [ansible.builtin.difference](difference_filter.md#ansible-collections-ansible-builtin-difference-filter) filter plugin
> :   the difference of one list from another.
>
> [ansible.builtin.symmetric_difference](symmetric_difference_filter.md#ansible-collections-ansible-builtin-symmetric-difference-filter) filter plugin
> :   different items from two lists.
>
> [ansible.builtin.unique](unique_filter.md#ansible-collections-ansible-builtin-unique-filter) filter plugin
> :   set of unique items of a list.
>
> [ansible.builtin.union](union_filter.md#ansible-collections-ansible-builtin-union-filter) filter plugin
> :   union of lists.

## [Examples](intersect_filter.md#id5)

```yaml+jinja
# return only the common elements of list1 and list2
# list1: [1, 2, 5, 3, 4, 10]
# list2: [1, 2, 3, 4, 5, 11, 99]
{{ list1 | intersect(list2) }}
# => [1, 2, 5, 3, 4]
```

## [Return Value](intersect_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A list with unique elements common to both lists, also known as a set.  **Returned:** success |

### Authors

- Brian Coca (@bcoca)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
