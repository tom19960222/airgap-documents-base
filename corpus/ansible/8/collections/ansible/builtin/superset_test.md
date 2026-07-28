---
collection: ansible
version: "8"
title: "ansible.builtin.superset test – is the list a superset of this other list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/superset_test.html
fetched_at: 2026-07-28T01:08:58+00:00
---
# ansible.builtin.superset test – is the list a superset of this other list

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `superset`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.superset` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](superset_test.md#synopsis)
- [Input](superset_test.md#input)
- [Keyword parameters](superset_test.md#keyword-parameters)
- [Examples](superset_test.md#examples)
- [Return Value](superset_test.md#return-value)

## [Synopsis](superset_test.md#id1)

- Validate if the first list is a super set (includes) the second list.
- Same as the `all` Python function.

Aliases: issuperset

## [Input](superset_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.superset` or `is not ansible.builtin.superset`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=any / required | List. |

## [Keyword parameters](superset_test.md#id3)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.builtin.superset(key1=value1, key2=value2, ...)` and `input is not ansible.builtin.superset(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **_subset**  list / elements=any / required | List to test against. |

## [Examples](superset_test.md#id4)

```yaml+jinja
big: [1,2,3,4,5]
sml: [3,4]
issmallinbig: '{{ big is superset(small) }}'
```

## [Return Value](superset_test.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the specified list is a superset of the provided list, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
