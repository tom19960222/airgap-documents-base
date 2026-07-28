---
collection: ansible
version: "8"
title: "ansible.builtin.comment filter – comment out a string"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/comment_filter.html
fetched_at: 2026-07-28T01:04:59+00:00
---
# ansible.builtin.comment filter – comment out a string

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `comment`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.comment` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](comment_filter.md#synopsis)
- [Input](comment_filter.md#input)
- [Positional parameters](comment_filter.md#positional-parameters)
- [Keyword parameters](comment_filter.md#keyword-parameters)
- [Notes](comment_filter.md#notes)
- [Examples](comment_filter.md#examples)
- [Return Value](comment_filter.md#return-value)

## [Synopsis](comment_filter.md#id1)

- Use programming language conventions to turn the input string into an embeddable comment.

## [Input](comment_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.comment`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | String to comment. |

## [Positional parameters](comment_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.comment(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **style**  string | Comment style to use.  **Choices:**   - `"plain"` ← (default) - `"decoration"` - `"erlang"` - `"c"` - `"cblock"` - `"xml"` |

## [Keyword parameters](comment_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.comment(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **begining**  string | Indicator of the start of a comment block, only available for styles that support multiline comments. |
| **decoration**  string | Indicator for comment or intermediate comment depending on the style. |
| **end**  string | Indicator the end of a comment block, only available for styles that support multiline comments. |
| **newline**  string | Indicator of comment end of line, only available for styles that support multiline comments.  **Default:** `"\\n"` |
| **postfix**  string | Indicator of the end of each line inside a comment block, only available for styles that support multiline comments. |
| **postfix_count**  integer | Number of times to add a postfix at the end of a line, when a prefix exists and is usable.  **Default:** `1` |
| **prefix**  string | Token to start each line inside a comment block, only available for styles that support multiline comments. |
| **prefix_count**  integer | Number of times to add a prefix at the start of a line, when a prefix exists and is usable.  **Default:** `1` |

## [Notes](comment_filter.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | ansible.builtin.comment(positional1, positional2, key1=value1, key2=value2)`

## [Examples](comment_filter.md#id6)

```yaml+jinja
# commented =>  #
#               # Plain style (default)
#               #
commented: "{{ 'Plain style (default)' | comment }}"

# not going to show that here ...
verycustom: "{{ "Custom style" | comment('plain', prefix='#######\n#', postfix='#\n#######\n   ###\n    #') }}"
```

## [Return Value](comment_filter.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | The ‘commented out’ string.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
