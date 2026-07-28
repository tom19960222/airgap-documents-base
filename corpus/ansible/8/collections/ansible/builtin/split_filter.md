---
collection: ansible
version: "8"
title: "ansible.builtin.split filter – split a string into a list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/split_filter.html
fetched_at: 2026-07-28T01:08:18+00:00
---
# ansible.builtin.split filter – split a string into a list

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `split`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.split` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

New in ansible-core 2.11

- [Synopsis](split_filter.md#synopsis)
- [Input](split_filter.md#input)
- [Positional parameters](split_filter.md#positional-parameters)
- [Notes](split_filter.md#notes)
- [Examples](split_filter.md#examples)
- [Return Value](split_filter.md#return-value)

## [Synopsis](split_filter.md#id1)

- Using Python’s text object method `split` we turn strings into lists via a ‘splitting character’.

## [Input](split_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.split`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A string to split. |

## [Positional parameters](split_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.split(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **_split_string**  string | A string on which to split the original.  **Default:** `" "` |

## [Notes](split_filter.md#id4)

> **Note:**
>
> - This is a passthrough to Python’s `str.split`.

## [Examples](split_filter.md#id5)

```yaml+jinja
# listjojo => [ "jojo", "is", "a" ]
listjojo: "{{ 'jojo is a' | split }}"

# listjojocomma => [ "jojo is", "a" ]
listjojocomma: "{{ 'jojo is, a' | split(',') }}"
```

## [Return Value](split_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | List of substrings split from the original.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
