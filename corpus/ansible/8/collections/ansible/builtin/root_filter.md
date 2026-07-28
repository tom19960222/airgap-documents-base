---
collection: ansible
version: "8"
title: "ansible.builtin.root filter – root of (math operation)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/root_filter.html
fetched_at: 2026-07-28T01:08:16+00:00
---
# ansible.builtin.root filter – root of (math operation)

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `root`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.root` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](root_filter.md#synopsis)
- [Input](root_filter.md#input)
- [Positional parameters](root_filter.md#positional-parameters)
- [Examples](root_filter.md#examples)
- [Return Value](root_filter.md#return-value)

## [Synopsis](root_filter.md#id1)

- Math operation that returns the Nth root of inputed number `X ^^ N`.

## [Input](root_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.root`.

| Parameter | Comments |
| --- | --- |
| **Input**  float / required | Number to operate on. |

## [Positional parameters](root_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.root(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **base**  float | Which root to take.  **Default:** `2.0` |

## [Examples](root_filter.md#id4)

```yaml+jinja
# => 8
fiveroot: "{{ 32768 | root (5) }}"

# 2
sqrt_of_2: "{{ 4 | root }}"

# me ^^ 3
cuberoot_me: "{{ me | root(3) }}"
```

## [Return Value](root_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  float | Resulting number.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
