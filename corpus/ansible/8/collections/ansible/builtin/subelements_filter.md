---
collection: ansible
version: "8"
title: "ansible.builtin.subelements filter – returns a product of a list and its elements"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/subelements_filter.html
fetched_at: 2026-07-28T01:04:49+00:00
---
# ansible.builtin.subelements filter – returns a product of a list and its elements

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `subelements`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.subelements` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

New in Ansible 2.7

- [Synopsis](subelements_filter.md#synopsis)
- [Input](subelements_filter.md#input)
- [Positional parameters](subelements_filter.md#positional-parameters)
- [Examples](subelements_filter.md#examples)
- [Return Value](subelements_filter.md#return-value)

## [Synopsis](subelements_filter.md#id1)

- This produces a product of an object and the subelement values of that object, similar to the subelements lookup. This lets you specify individual subelements to use in a template *_input*.

## [Input](subelements_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.subelements`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=any / required | Original list. |

## [Positional parameters](subelements_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.subelements(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **_subelement**  string / required | Label of property to extract from original list items. |
| **skip_missing**  boolean | If `True`, ignore missing subelements, otherwise missing subelements generate an error.  **Choices:**   - `false` ← (default) - `true` |

## [Examples](subelements_filter.md#id4)

```yaml+jinja
# data
users:
  - groups: [1,2,3]
    name: lola
  - name: fernando
    groups: [2,3,4]

# user_w_groups =>[ { "groups": [ 1, 2, 3 ], "name": "lola" }, 1 ], [ { "groups": [ 1, 2, 3 ], "name": "lola" }, 2 ], [ { "groups": [ 1, 2, 3 ], "name": "lola" }, 3 ], [ { "groups": [ 2, 3, 4 ], "name": "fernando" }, 2 ], [ { "groups": [ 2, 3, 4 ], "name": "fernando" }, 3 ], [ { "groups": [ 2, 3, 4 ], "name": "fernando" }, 4 ] ]
users_w_groups: {{ users | subelements('groups', skip_missing=True) }}
```

## [Return Value](subelements_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=any | List made of original list and product of the subelement list.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
