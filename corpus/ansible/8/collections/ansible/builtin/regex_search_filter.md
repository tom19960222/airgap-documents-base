---
collection: ansible
version: "8"
title: "ansible.builtin.regex_search filter – extract regex match from string"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/regex_search_filter.html
fetched_at: 2026-07-28T01:05:00+00:00
---
# ansible.builtin.regex_search filter – extract regex match from string

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `regex_search`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.regex_search` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](regex_search_filter.md#synopsis)
- [Input](regex_search_filter.md#input)
- [Positional parameters](regex_search_filter.md#positional-parameters)
- [Keyword parameters](regex_search_filter.md#keyword-parameters)
- [Notes](regex_search_filter.md#notes)
- [Examples](regex_search_filter.md#examples)
- [Return Value](regex_search_filter.md#return-value)

## [Synopsis](regex_search_filter.md#id1)

- Search in a string to extract the part that matches the regular expression.

## [Input](regex_search_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.regex_search`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | String to match against. |

## [Positional parameters](regex_search_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.regex_search(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **_regex**  string | Regular expression string that defines the match. |

## [Keyword parameters](regex_search_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.regex_search(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ignorecase**  boolean | Force the search to be case insensitive if `True`, case sensitive otherwise.  **Choices:**   - `false` ← (default) - `true` |
| **multiline**  boolean | Search across line endings if `True`, do not if otherwise.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](regex_search_filter.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | ansible.builtin.regex_search(positional1, positional2, key1=value1, key2=value2)`
> - Maps to Python’s `re.search`.

## [Examples](regex_search_filter.md#id6)

```yaml+jinja
# db => 'database42'
db: "{{ 'server1/database42' | regex_search('database[0-9]+') }}"

# drinkat => 'BAR'
drinkat: "{{ 'foo\nBAR' | regex_search('^bar', multiline=True, ignorecase=True) }}"
```

## [Return Value](regex_search_filter.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | Matched string or empty string if no match.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
