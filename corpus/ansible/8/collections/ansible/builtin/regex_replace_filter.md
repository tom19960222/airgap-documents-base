---
collection: ansible
version: "8"
title: "ansible.builtin.regex_replace filter – replace a string via regex"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/regex_replace_filter.html
fetched_at: 2026-07-28T01:05:02+00:00
---
# ansible.builtin.regex_replace filter – replace a string via regex

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `regex_replace`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.regex_replace` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](regex_replace_filter.md#synopsis)
- [Input](regex_replace_filter.md#input)
- [Positional parameters](regex_replace_filter.md#positional-parameters)
- [Keyword parameters](regex_replace_filter.md#keyword-parameters)
- [Notes](regex_replace_filter.md#notes)
- [Examples](regex_replace_filter.md#examples)
- [Return Value](regex_replace_filter.md#return-value)

## [Synopsis](regex_replace_filter.md#id1)

- Replace a substring defined by a regular expression with another defined by another regular expression based on the first match.

## [Input](regex_replace_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.regex_replace`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | String to match against. |

## [Positional parameters](regex_replace_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | ansible.builtin.regex_replace(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **_regex_match**  integer / required | Regular expression string that defines the match. |
| **_regex_replace**  integer / required | Regular expression string that defines the replacement. |

## [Keyword parameters](regex_replace_filter.md#id4)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | ansible.builtin.regex_replace(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ignorecase**  boolean | Force the search to be case insensitive if `True`, case sensitive otherwise.  **Choices:**   - `false` ← (default) - `true` |
| **multiline**  boolean | Search across line endings if `True`, do not if otherwise.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](regex_replace_filter.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `input | ansible.builtin.regex_replace(positional1, positional2, key1=value1, key2=value2)`
> - Maps to Python’s `re.replace`.

## [Examples](regex_replace_filter.md#id6)

```yaml+jinja
# whatami => 'able'
whatami: "{{ 'ansible' | regex_replace('^a.*i(.*)$', 'a\\1') }}"

# commalocal => 'localhost, 80'
commalocal: "{{ 'localhost:80' | regex_replace('^(?P<host>.+):(?P<port>\\d+)$', '\\g<host>, \\g<port>') }}"

# piratecomment => '#CAR\n#tar\nfoo\n#bar\n'
piratecomment: "{{ 'CAR\ntar\nfoo\nbar\n' | regex_replace('^(.ar)$', '#\\1', multiline=True, ignorecase=True) }}"
```

## [Return Value](regex_replace_filter.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  string | String with substitution (or original if no match).  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
