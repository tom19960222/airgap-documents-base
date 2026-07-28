---
collection: ansible
version: "8"
title: "ansible.builtin.shuffle filter – randomize a list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/shuffle_filter.html
fetched_at: 2026-07-28T01:04:52+00:00
---
# ansible.builtin.shuffle filter – randomize a list

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `shuffle`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.shuffle` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](shuffle_filter.md#synopsis)
- [Input](shuffle_filter.md#input)
- [Keyword parameters](shuffle_filter.md#keyword-parameters)
- [Examples](shuffle_filter.md#examples)
- [Return Value](shuffle_filter.md#return-value)

## [Synopsis](shuffle_filter.md#id1)

- Take the elements of the input list and return in a random order.

## [Input](shuffle_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.shuffle`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=any / required | A number or list to randomize. |

## [Keyword parameters](shuffle_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.shuffle(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **seed**  string | If specified use a pseudo random selection instead (repeatable). |

## [Examples](shuffle_filter.md#id4)

```yaml+jinja
randomized_list: "{{ ['a','b','c'] | shuffle}}"
per_host_repeatable: "{{ ['a','b','c'] | shuffle(seed=inventory_hostname) }}"
```

## [Return Value](shuffle_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=any | Random number or list element.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
