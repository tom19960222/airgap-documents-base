---
collection: ansible
version: "8"
title: "ansible.builtin.subset test – is the list a subset of this other list"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/subset_test.html
fetched_at: 2026-07-28T01:08:57+00:00
---
# ansible.builtin.subset test – is the list a subset of this other list

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `subset`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.subset` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](subset_test.md#synopsis)
- [Input](subset_test.md#input)
- [Keyword parameters](subset_test.md#keyword-parameters)
- [Examples](subset_test.md#examples)
- [Return Value](subset_test.md#return-value)

## [Synopsis](subset_test.md#id1)

- Validate if the first list is a sub set (is included) of the second list.
- Same as the `all` Python function.

Aliases: issubset

## [Input](subset_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.subset` or `is not ansible.builtin.subset`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=any / required | List. |

## [Keyword parameters](subset_test.md#id3)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.builtin.subset(key1=value1, key2=value2, ...)` and `input is not ansible.builtin.subset(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **_superset**  list / elements=any / required | List to test against. |

## [Examples](subset_test.md#id4)

```yaml+jinja
big: [1,2,3,4,5]
sml: [3,4]
issmallinbig: '{{ small is subset(big) }}'
```

## [Return Value](subset_test.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the specified list is a subset of the provided list, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
