---
collection: ansible
version: "8"
title: "ansible.builtin.pow filter – power of (math operation)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/pow_filter.html
fetched_at: 2026-07-28T01:08:13+00:00
---
# ansible.builtin.pow filter – power of (math operation)

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `pow`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.pow` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](pow_filter.md#synopsis)
- [Input](pow_filter.md#input)
- [Positional parameters](pow_filter.md#positional-parameters)
- [Notes](pow_filter.md#notes)
- [Examples](pow_filter.md#examples)
- [Return Value](pow_filter.md#return-value)

## [Synopsis](pow_filter.md#id1)

- Math operation that returns the Nth power of inputed number, `X ^ N`.

## [Input](pow_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.pow`.

| Parameter | Comments |
| --- | --- |
| **Input**  float / required | The base. |

## [Positional parameters](pow_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.pow(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **_power**  float / required | Which power (exponent) to use. |

## [Notes](pow_filter.md#id4)

> **Note:**
>
> - This is a passthrough to Python’s `math.pow`.

## [Examples](pow_filter.md#id5)

```yaml+jinja
# => 32768
eight_power_five: "{{ 8 | pow(5) }}"

# 4
square_of_2: "{{ 2 | pow(2) }}"

# me ^ 3
cube_me: "{{ me | pow(3) }}"
```

## [Return Value](pow_filter.md#id6)

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
