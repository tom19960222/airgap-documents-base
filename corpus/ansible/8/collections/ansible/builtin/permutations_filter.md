---
collection: ansible
version: "8"
title: "ansible.builtin.permutations filter – permutations from the elements of a list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/permutations_filter.html
fetched_at: 2026-07-28T01:08:12+00:00
---
# ansible.builtin.permutations filter – permutations from the elements of a list

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `permutations`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.permutations` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](permutations_filter.md#synopsis)
- [Input](permutations_filter.md#input)
- [Positional parameters](permutations_filter.md#positional-parameters)
- [Examples](permutations_filter.md#examples)
- [Return Value](permutations_filter.md#return-value)

## [Synopsis](permutations_filter.md#id1)

- Create a list of the permutations of lists from the elements of a list.
- Unlike combinations, in permutations order is significant.

## [Input](permutations_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.permutations`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | Elements to base the permutations on. |

## [Positional parameters](permutations_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.permutations(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **list_size**  integer / required | The size of the list for each permutation. |

## [Examples](permutations_filter.md#id4)

```yaml+jinja
# ptrs_of_two => [ [ 1, 2 ], [ 1, 3 ], [ 1, 4 ], [ 1, 5 ], [ 2, 1 ], [ 2, 3 ], [ 2, 4 ], [ 2, 5 ], [ 3, 1 ], [ 3, 2 ], [ 3, 4 ], [ 3, 5 ], [ 4, 1 ], [ 4, 2 ], [ 4, 3 ], [ 4, 5 ], [ 5, 1 ], [ 5, 2 ], [ 5, 3 ], [ 5, 4 ] ]
prts_of_two:  "{{ [1,2,3,4,5] | permutations(2) }}"
```

## [Return Value](permutations_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | List of permutations lists resulting from the supplied elements and list size.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
