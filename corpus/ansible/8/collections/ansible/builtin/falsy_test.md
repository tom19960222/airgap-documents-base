---
collection: ansible
version: "8"
title: "ansible.builtin.falsy test – Pythonic false"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/falsy_test.html
fetched_at: 2026-07-28T01:08:48+00:00
---
# ansible.builtin.falsy test – Pythonic false

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `falsy`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.falsy` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

New in ansible-base 2.10

- [Synopsis](falsy_test.md#synopsis)
- [Input](falsy_test.md#input)
- [Keyword parameters](falsy_test.md#keyword-parameters)
- [Examples](falsy_test.md#examples)
- [Return Value](falsy_test.md#return-value)

## [Synopsis](falsy_test.md#id1)

- This check is a more Python version of what is ‘false’.
- It is the opposite of ‘truthy’.

## [Input](falsy_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.falsy` or `is not ansible.builtin.falsy`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | An expression that can be expressed in a boolean context. |

## [Keyword parameters](falsy_test.md#id3)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.builtin.falsy(key1=value1, key2=value2, ...)` and `input is not ansible.builtin.falsy(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **convert_bool**  boolean | Attempts to convert the result to a strict Python boolean vs normally acceptable values (`yes`/`no`, `on`/`off`, `0`/`1`, etc).  **Choices:**   - `false` ← (default) - `true` |

## [Examples](falsy_test.md#id4)

```yaml+jinja
thisisfalse: '{{ "any string" is falsy }}'
thisistrue: '{{ "" is falsy }}'
```

## [Return Value](falsy_test.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `False` if the condition is not “Python truthy”, `True` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
