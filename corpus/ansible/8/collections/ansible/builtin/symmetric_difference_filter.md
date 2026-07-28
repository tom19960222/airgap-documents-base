---
collection: ansible
version: "8"
title: "ansible.builtin.symmetric_difference filter – different items from two lists"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/symmetric_difference_filter.html
fetched_at: 2026-07-28T01:08:19+00:00
---
# ansible.builtin.symmetric_difference filter – different items from two lists

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `symmetric_difference`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.symmetric_difference` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](symmetric_difference_filter.md#synopsis)
- [Input](symmetric_difference_filter.md#input)
- [Keyword parameters](symmetric_difference_filter.md#keyword-parameters)
- [See Also](symmetric_difference_filter.md#see-also)
- [Examples](symmetric_difference_filter.md#examples)
- [Return Value](symmetric_difference_filter.md#return-value)

## [Synopsis](symmetric_difference_filter.md#id1)

- Provide a unique list of all the elements unique to each list.

## [Input](symmetric_difference_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.symmetric_difference`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | A list. |

## [Keyword parameters](symmetric_difference_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.symmetric_difference(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **_second_list**  list / elements=string / required | A list. |

## [See Also](symmetric_difference_filter.md#id4)

> **See also:**
>
> [ansible.builtin.difference](difference_filter.md#ansible-collections-ansible-builtin-difference-filter) filter plugin
> :   the difference of one list from another.
>
> [ansible.builtin.intersect](intersect_filter.md#ansible-collections-ansible-builtin-intersect-filter) filter plugin
> :   intersection of lists.
>
> [ansible.builtin.union](union_filter.md#ansible-collections-ansible-builtin-union-filter) filter plugin
> :   union of lists.
>
> [ansible.builtin.unique](unique_filter.md#ansible-collections-ansible-builtin-unique-filter) filter plugin
> :   set of unique items of a list.

## [Examples](symmetric_difference_filter.md#id5)

```yaml+jinja
# return the elements of list1 not in list2 and the elements in list2 not in list1
# list1: [1, 2, 5, 1, 3, 4, 10]
# list2: [1, 2, 3, 4, 5, 11, 99]
{{ list1 | symmetric_difference(list2) }}
# => [10, 11, 99]
```

## [Return Value](symmetric_difference_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | A unique list of the elements from two lists that are unique to each one.  **Returned:** success |

### Authors

- Brian Coca (@bcoca)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
