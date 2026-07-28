---
collection: ansible
version: "8"
title: "ansible.builtin.regex_escape filter – escape regex chars"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/regex_escape_filter.html
fetched_at: 2026-07-28T01:05:02+00:00
---
# ansible.builtin.regex_escape filter – escape regex chars

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `regex_escape`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.regex_escape` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

New in Ansible 2.8

- [Synopsis](regex_escape_filter.md#synopsis)
- [Input](regex_escape_filter.md#input)
- [Positional parameters](regex_escape_filter.md#positional-parameters)
- [Notes](regex_escape_filter.md#notes)
- [Examples](regex_escape_filter.md#examples)
- [Return Value](regex_escape_filter.md#return-value)

## [Synopsis](regex_escape_filter.md#id1)

- Escape special characters in a string for use in a regular expression.

## [Input](regex_escape_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.regex_escape`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | String to escape. |

## [Positional parameters](regex_escape_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.regex_escape(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **re_type**  string | Which type of escaping to use.  **Choices:**   - `"python"` ← (default) - `"posix_basic"` |

## [Notes](regex_escape_filter.md#id4)

> **Note:**
>
> - posix_extended is not implemented yet

## [Examples](regex_escape_filter.md#id5)

```yaml+jinja
# safe_for_regex => '\^f\.\*o\(\.\*\)\$'
safe_for_regex: "{{ '^f.*o(.*)$' | regex_escape() }}"
```

## [Return Value](regex_escape_filter.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  string | Escaped string.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
