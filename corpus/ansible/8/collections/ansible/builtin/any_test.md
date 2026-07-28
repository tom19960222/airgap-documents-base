---
collection: ansible
version: "8"
title: "ansible.builtin.any test – is any conditions in a list true"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/any_test.html
fetched_at: 2026-07-28T01:08:44+00:00
---
# ansible.builtin.any test – is any conditions in a list true

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `any`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.any` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](any_test.md#synopsis)
- [Input](any_test.md#input)
- [Examples](any_test.md#examples)
- [Return Value](any_test.md#return-value)

## [Synopsis](any_test.md#id1)

- This test checks each condition in a list for truthiness.
- Same as the `any` Python function.

## [Input](any_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.any` or `is not ansible.builtin.any`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=any / required | List of conditions, each can be a boolean or conditional expression that results in a boolean value. |

## [Examples](any_test.md#id3)

```yaml+jinja
varexpression: "{{ 3 == 3 }}"
# are all statements true?
{{ [false, booleanvar, varexpression] is any}}
```

## [Return Value](any_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if any element of the list was true, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
