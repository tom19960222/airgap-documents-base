---
collection: ansible
version: "8"
title: "ansible.builtin.log filter – log of (math operation)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/log_filter.html
fetched_at: 2026-07-28T01:08:09+00:00
---
# ansible.builtin.log filter – log of (math operation)

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `log`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.log` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](log_filter.md#synopsis)
- [Input](log_filter.md#input)
- [Positional parameters](log_filter.md#positional-parameters)
- [Notes](log_filter.md#notes)
- [Examples](log_filter.md#examples)
- [Return Value](log_filter.md#return-value)

## [Synopsis](log_filter.md#id1)

- Math operation that returns the [logarithm](https://en.wikipedia.org/wiki/Logarithm) to base N of the input number.
- By default, computes the [natural logarithm](https://en.wikipedia.org/wiki/Natural_logarithm).

## [Input](log_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.log`.

| Parameter | Comments |
| --- | --- |
| **Input**  float / required | Number to operate on. |

## [Positional parameters](log_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.log(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **base**  float | Which base to use. Defaults to [Euler’s number](https://en.wikipedia.org/wiki/Euler%2527s_number).  **Default:** `2.718281828459045` |

## [Notes](log_filter.md#id4)

> **Note:**
>
> - This is a passthrough to Python’s `math.log`.

## [Examples](log_filter.md#id5)

```yaml+jinja
# 1.2920296742201791
eightlogfive: "{{ 8 | log(5) }}"

# 0.9030899869919435
eightlog10: "{{ 8 | log() }}"
```

## [Return Value](log_filter.md#id6)

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
