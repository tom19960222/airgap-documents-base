---
collection: ansible
version: "8"
title: "ansible.builtin.combinations filter – combinations from the elements of a list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/combinations_filter.html
fetched_at: 2026-07-28T01:07:59+00:00
---
# ansible.builtin.combinations filter – combinations from the elements of a list

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `combinations`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.combinations` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](combinations_filter.md#synopsis)
- [Input](combinations_filter.md#input)
- [Positional parameters](combinations_filter.md#positional-parameters)
- [Examples](combinations_filter.md#examples)
- [Return Value](combinations_filter.md#return-value)

## [Synopsis](combinations_filter.md#id1)

- Create a list of combinations of sets from the elements of a list.

## [Input](combinations_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.combinations`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | Elements to combine. |

## [Positional parameters](combinations_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.combinations(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **set_size**  integer / required | The size of the set for each combination. |

## [Examples](combinations_filter.md#id4)

```yaml+jinja
# combos_of_two => [ [ 1, 2 ], [ 1, 3 ], [ 1, 4 ], [ 1, 5 ], [ 2, 3 ], [ 2, 4 ], [ 2, 5 ], [ 3, 4 ], [ 3, 5 ], [ 4, 5 ] ]
combos_of_two: "{{ [1,2,3,4,5] | combinations(2) }}"
```

## [Return Value](combinations_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | List of combination sets resulting from the supplied elements and set size.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
