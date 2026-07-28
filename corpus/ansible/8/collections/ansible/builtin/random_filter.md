---
collection: ansible
version: "8"
title: "ansible.builtin.random filter – random number or list item"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/random_filter.html
fetched_at: 2026-07-28T01:04:52+00:00
---
# ansible.builtin.random filter – random number or list item

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `random`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.random` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](random_filter.md#synopsis)
- [Input](random_filter.md#input)
- [Positional parameters](random_filter.md#positional-parameters)
- [Examples](random_filter.md#examples)
- [Return Value](random_filter.md#return-value)

## [Synopsis](random_filter.md#id1)

- Use the input to either select a random element of a list or generate a random number.

## [Input](random_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.random`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | A number or list/sequence, if it is a number it is the top bound for random number generation, if it is a sequence or list, the source of the random element selected. |

## [Positional parameters](random_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.random(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **start**  integer | Bottom bound for the random number/element generated. |
| **step**  integer | Subsets the defined range by only using this value to select the increments of it between start and end.  **Default:** `1` |
| **seed**  string | If specified use a pseudo random selection instead (repeatable). |

## [Examples](random_filter.md#id4)

```yaml+jinja
# can be any item from the list
random_item: "{{ ['a','b','c'] | random }}"

# cron line, select random minute repeatable for each host
"{{ 60 | random(seed=inventory_hostname) }} * * * * root /script/from/cron"
```

## [Return Value](random_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  any | Random number or list element.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
