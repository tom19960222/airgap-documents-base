---
collection: ansible
version: "8"
title: "ansible.builtin.product filter – cartesian product of lists"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/product_filter.html
fetched_at: 2026-07-28T01:08:13+00:00
---
# ansible.builtin.product filter – cartesian product of lists

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `product`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.product` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](product_filter.md#synopsis)
- [Input](product_filter.md#input)
- [Positional parameters](product_filter.md#positional-parameters)
- [Notes](product_filter.md#notes)
- [Examples](product_filter.md#examples)
- [Return Value](product_filter.md#return-value)

## [Synopsis](product_filter.md#id1)

- Combines two lists into one with each element being the product of the elements of the input lists.
- Creates ‘nested loops’. Looping over `listA` and `listB` is the same as looping over `listA | product(listB`).

## [Input](product_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.product`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | First list. |

## [Positional parameters](product_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.product(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **_additional_lists**  list / elements=string | Additional list for the product. |
| **repeat**  integer | Number of times to repeat the product against itself.  **Default:** `1` |

## [Notes](product_filter.md#id4)

> **Note:**
>
> - This is a passthrough to Python’s `itertools.product`

## [Examples](product_filter.md#id5)

```yaml+jinja
# product => [ [ 1, "a" ], [ 1, "b" ], [ 1, "c" ], [ 2, "a" ], [ 2, "b" ], [ 2, "c" ], [ 3, "a" ], [ 3, "b" ], [ 3, "c" ], [ 4, "a" ], [ 4, "b" ], [ 4, "c" ], [ 5, "a" ], [ 5, "b" ], [ 5, "c" ] ]
product:  "{{ [1,2,3,4,5] | product(['a', 'b', 'c']) }}"

# repeat_original => [ [ 1, 1 ], [ 1, 2 ], [ 2, 1 ], [ 2, 2 ] ]
repeat_original: "{{ [1,2] | product(repeat=2) }}"

# repeat_product => [ [ 1, "a", 1, "a" ], [ 1, "a", 1, "b" ], [ 1, "a", 2, "a" ], [ 1, "a", 2, "b" ], [ 1, "b", 1, "a" ], [ 1, "b", 1, "b" ], [ 1, "b", 2, "a" ], [ 1, "b", 2, "b" ], [ 2, "a", 1, "a" ], [ 2, "a", 1, "b" ], [ 2, "a", 2, "a" ], [ 2, "a", 2, "b" ], [ 2, "b", 1, "a" ], [ 2, "b", 1, "b" ], [ 2, "b", 2, "a" ], [ 2, "b", 2, "b" ] ]
repeat_product:  "{{ [1,2] | product(['a', 'b'], repeat=2) }}"

# domains => [ 'example.com', 'ansible.com', 'redhat.com' ]
domains: "{{ [ 'example', 'ansible', 'redhat'] | product(['com']) | map('join', '.') }}"
```

## [Return Value](product_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=list | List of lists of combined elements from the input lists.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
