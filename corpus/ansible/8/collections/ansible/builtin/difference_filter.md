---
collection: ansible
version: "8"
title: "ansible.builtin.difference filter – the difference of one list from another"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/difference_filter.html
fetched_at: 2026-07-28T01:08:01+00:00
---
# ansible.builtin.difference filter – the difference of one list from another

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `difference`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.difference` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](difference_filter.md#synopsis)
- [Input](difference_filter.md#input)
- [Keyword parameters](difference_filter.md#keyword-parameters)
- [See Also](difference_filter.md#see-also)
- [Examples](difference_filter.md#examples)
- [Return Value](difference_filter.md#return-value)

## [Synopsis](difference_filter.md#id1)

- Provide a unique list of all the elements of the first list that do not appear in the second one.

## [Input](difference_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.difference`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | A list. |

## [Keyword parameters](difference_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.difference(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **_second_list**  list / elements=string / required | A list. |

## [See Also](difference_filter.md#id4)

> **See also:**
>
> [ansible.builtin.intersect](intersect_filter.md#ansible-collections-ansible-builtin-intersect-filter) filter plugin
> :   intersection of lists.
>
> [ansible.builtin.symmetric_difference](symmetric_difference_filter.md#ansible-collections-ansible-builtin-symmetric-difference-filter) filter plugin
> :   different items from two lists.
>
> [ansible.builtin.union](union_filter.md#ansible-collections-ansible-builtin-union-filter) filter plugin
> :   union of lists.
>
> [ansible.builtin.unique](unique_filter.md#ansible-collections-ansible-builtin-unique-filter) filter plugin
> :   set of unique items of a list.

## [Examples](difference_filter.md#id5)

```yaml+jinja
# return the elements of list1 not in list2
# list1: [1, 2, 5, 1, 3, 4, 10]
# list2: [1, 2, 3, 4, 5, 11, 99]
{{ list1 | difference(list2) }}
# => [10]
```

## [Return Value](difference_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A unique list of the elements from the first list that do not appear on the second.  **Returned:** success |

### Authors

- Brian Coca (@bcoca)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
