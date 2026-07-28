---
collection: ansible
version: "8"
title: "ansible.builtin.contains test – does the list contain this element"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/contains_test.html
fetched_at: 2026-07-28T01:08:45+00:00
---
# ansible.builtin.contains test – does the list contain this element

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `contains`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.contains` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](contains_test.md#synopsis)
- [Input](contains_test.md#input)
- [Keyword parameters](contains_test.md#keyword-parameters)
- [Examples](contains_test.md#examples)
- [Return Value](contains_test.md#return-value)

## [Synopsis](contains_test.md#id1)

- Checks the supplied element against the input list to see if it exists within it.

## [Input](contains_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.contains` or `is not ansible.builtin.contains`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=any / required | List of elements to compare. |

## [Keyword parameters](contains_test.md#id3)

This describes keyword parameters of the test. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `input is ansible.builtin.contains(key1=value1, key2=value2, ...)` and `input is not ansible.builtin.contains(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **_contained**  any / required | Element to test for. |

## [Examples](contains_test.md#id4)

```yaml+jinja
# simple expression
{{ listofthings is contains('this') }}

# as a selector
- action: module=doessomething
  when: lacp_groups|selectattr('interfaces', 'contains', 'em1')|first).master
  vars:
    lacp_groups:
      - master: lacp0
        network: 10.65.100.0/24
        gateway: 10.65.100.1
        dns4:
          - 10.65.100.10
          - 10.65.100.11
        interfaces:
          - em1
          - em2

      - master: lacp1
        network: 10.65.120.0/24
        gateway: 10.65.120.1
        dns4:
          - 10.65.100.10
          - 10.65.100.11
        interfaces:
            - em3
            - em4
```

## [Return Value](contains_test.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the specified element is contained in the supplied sequence, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
