---
collection: ansible
version: "8"
title: "ansible.builtin.human_to_bytes filter – Get bytes from string"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/human_to_bytes_filter.html
fetched_at: 2026-07-28T01:08:07+00:00
---
# ansible.builtin.human_to_bytes filter – Get bytes from string

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `human_to_bytes`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.human_to_bytes` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](human_to_bytes_filter.md#synopsis)
- [Input](human_to_bytes_filter.md#input)
- [Positional parameters](human_to_bytes_filter.md#positional-parameters)
- [Examples](human_to_bytes_filter.md#examples)
- [Return Value](human_to_bytes_filter.md#return-value)

## [Synopsis](human_to_bytes_filter.md#id1)

- Convert a human readable byte or bit string into a number bytes.

## [Input](human_to_bytes_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.human_to_bytes`.

| Parameter | Comments |
| --- | --- |
| **Input**  integer / required | Human readable description of a number of bytes. |

## [Positional parameters](human_to_bytes_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.human_to_bytes(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **default_unit**  string | Unit to assume when input does not specify it.  **Choices:**   - `"Y"` - `"Z"` - `"E"` - `"P"` - `"T"` - `"G"` - `"M"` - `"K"` - `"B"` |
| **isbits**  boolean | If `True`, force to interpret only bit input; if `False`, force bytes. Otherwise use the notation to guess.  **Choices:**   - `false` - `true` |

## [Examples](human_to_bytes_filter.md#id4)

```yaml+jinja
# size => 1234803098
size: '{{ "1.15 GB" | human_to_bytes }}'

# size => 1234803098
size: '{{ "1.15" | human_to_bytes(deafult_unit="G") }}'

# this is an error, wants bits, got bytes
ERROR: '{{ "1.15 GB" | human_to_bytes(isbits=true) }}'
```

## [Return Value](human_to_bytes_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  integer | Integer representing the bytes from the input.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
