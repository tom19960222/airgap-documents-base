---
collection: ansible
version: "8"
title: "ansible.builtin.urn test – is the string a valid URN"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/urn_test.html
fetched_at: 2026-07-28T01:09:02+00:00
---
# ansible.builtin.urn test – is the string a valid URN

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `urn`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.urn` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

New in ansible-core 2.14

- [Synopsis](urn_test.md#synopsis)
- [Input](urn_test.md#input)
- [Examples](urn_test.md#examples)
- [Return Value](urn_test.md#return-value)

## [Synopsis](urn_test.md#id1)

- Validates that the input string conforms to the URN standard.

## [Input](urn_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.urn` or `is not ansible.builtin.urn`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | Possible URN. |

## [Examples](urn_test.md#id3)

```yaml+jinja
# ISBN in URN format
{{ 'urn:isbn:9780302376463' is urn }}
# this is URL/URI but not URN
{{ 'mailto://nowone@example.com' is not urn }}
```

## [Return Value](urn_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `true` if the string is a URN and `false` if it is not.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
