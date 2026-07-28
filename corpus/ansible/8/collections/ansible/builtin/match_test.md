---
collection: ansible
version: "8"
title: "ansible.builtin.match test – Does string match regular expression from the start"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/match_test.html
fetched_at: 2026-07-28T01:08:51+00:00
---
# ansible.builtin.match test – Does string match regular expression from the start

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `match`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.match` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](match_test.md#synopsis)
- [Input](match_test.md#input)
- [Keyword parameters](match_test.md#keyword-parameters)
- [Examples](match_test.md#examples)
- [Return Value](match_test.md#return-value)

## [Synopsis](match_test.md#id1)

- Compare string against regular expression using Python’s match function, this means the regex is automatically anchored at the start of the string.

## [Input](match_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.match` or `is not ansible.builtin.match`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | String to match. |

## [Keyword parameters](match_test.md#id3)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.builtin.match(key1=value1, key2=value2, ...)` and `input is not ansible.builtin.match(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **ignorecase**  boolean | Use case insenstive matching.  **Choices:**   - `false` ← (default) - `true` |
| **multiline**  boolean | Match against mulitple lines in string.  **Choices:**   - `false` ← (default) - `true` |
| **pattern**  string / required | Regex to match against. |

## [Examples](match_test.md#id4)

```yaml+jinja
url: "https://example.com/users/foo/resources/bar"
foundmatch: url is match("https://example.com/users/.*/resources")
nomatch: url is match("/users/.*/resources")
```

## [Return Value](match_test.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if there is a match, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
