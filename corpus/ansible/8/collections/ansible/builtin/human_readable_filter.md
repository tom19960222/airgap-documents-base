---
collection: ansible
version: "8"
title: "ansible.builtin.human_readable filter – Make bytes/bits human readable"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/human_readable_filter.html
fetched_at: 2026-07-28T01:08:07+00:00
---
# ansible.builtin.human_readable filter – Make bytes/bits human readable

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `human_readable`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.human_readable` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](human_readable_filter.md#synopsis)
- [Input](human_readable_filter.md#input)
- [Positional parameters](human_readable_filter.md#positional-parameters)
- [Examples](human_readable_filter.md#examples)
- [Return Value](human_readable_filter.md#return-value)

## [Synopsis](human_readable_filter.md#id1)

- Convert byte or bit figures to more human readable formats.

## [Input](human_readable_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.human_readable`.

| Parameter | Comments |
| --- | --- |
| **Input**  integer / required | Number of bytes, or bits. Depends on *isbits*. |

## [Positional parameters](human_readable_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.human_readable(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **isbits**  boolean | Whether the input is bits, instead of bytes.  **Choices:**   - `false` ← (default) - `true` |
| **unit**  string | Unit to force output into. If none specified the largest unit arrived at will be used.  **Choices:**   - `"Y"` - `"Z"` - `"E"` - `"P"` - `"T"` - `"G"` - `"M"` - `"K"` - `"B"` |

## [Examples](human_readable_filter.md#id4)

```yaml+jinja
# size => "1.15 GB"
size: "{{ 1232345345 | human_readable }}"

# size => "1.15 Gb"
size_bits: "{{ 1232345345 | human_readable(true) }}"

# size => "1175.26 MB"
size_MB: "{{ 1232345345 | human_readable(unit='M') }}"
```

## [Return Value](human_readable_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | Human readable byte or bit size.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
