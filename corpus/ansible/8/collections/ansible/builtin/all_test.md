---
collection: ansible
version: "8"
title: "ansible.builtin.all test – are all conditions in a list true"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/all_test.html
fetched_at: 2026-07-28T01:08:43+00:00
---
# ansible.builtin.all test – are all conditions in a list true

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `all`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.all` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](all_test.md#synopsis)
- [Input](all_test.md#input)
- [Examples](all_test.md#examples)
- [Return Value](all_test.md#return-value)

## [Synopsis](all_test.md#id1)

- This test checks each condition in a list for truthiness.
- Same as the `all` Python function.

## [Input](all_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.all` or `is not ansible.builtin.all`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=any / required | List of conditions, each can be a boolean or conditional expression that results in a boolean value. |

## [Examples](all_test.md#id3)

```yaml+jinja
varexpression: "{{ 3 == 3 }}"
# are all statements true?
{{ [true, booleanvar, varexpression] is all }}
```

## [Return Value](all_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if all elements of the list were True, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
