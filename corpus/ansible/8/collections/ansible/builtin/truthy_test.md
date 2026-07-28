---
collection: ansible
version: "8"
title: "ansible.builtin.truthy test – Pythonic true"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/truthy_test.html
fetched_at: 2026-07-28T01:08:59+00:00
---
# ansible.builtin.truthy test – Pythonic true

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `truthy`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.truthy` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

New in ansible-base 2.10

- [Synopsis](truthy_test.md#synopsis)
- [Input](truthy_test.md#input)
- [Keyword parameters](truthy_test.md#keyword-parameters)
- [Examples](truthy_test.md#examples)
- [Return Value](truthy_test.md#return-value)

## [Synopsis](truthy_test.md#id1)

- This check is a more Python version of what is ‘true’.
- It is the opposite of `falsy`.

## [Input](truthy_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.truthy` or `is not ansible.builtin.truthy`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | An expression that can be expressed in a boolean context. |

## [Keyword parameters](truthy_test.md#id3)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.builtin.truthy(key1=value1, key2=value2, ...)` and `input is not ansible.builtin.truthy(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **convert_bool**  boolean | Attempts to convert to strict python boolean vs normally acceptable values (`yes`/`no`, `on`/`off`, `0`/`1`, etc).  **Choices:**   - `false` ← (default) - `true` |

## [Examples](truthy_test.md#id4)

```yaml+jinja
thisistrue: '{{ "any string" is truthy }}'
thisisfalse: '{{ "" is truthy }}'
```

## [Return Value](truthy_test.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the condition is not “Python truthy”, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
