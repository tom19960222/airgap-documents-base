---
collection: ansible
version: "8"
title: "ansible.builtin.unreachable test – Did task end due to the host was unreachable"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/unreachable_test.html
fetched_at: 2026-07-28T01:09:00+00:00
---
# ansible.builtin.unreachable test – Did task end due to the host was unreachable

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `unreachable`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.unreachable` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](unreachable_test.md#synopsis)
- [Input](unreachable_test.md#input)
- [Examples](unreachable_test.md#examples)
- [Return Value](unreachable_test.md#return-value)

## [Synopsis](unreachable_test.md#id1)

- Tests if task was not able to reach the host for execution
- This test checks for the existance of a `unreachable` key in the input dictionary and that it’s value is `True`

## [Input](unreachable_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.unreachable` or `is not ansible.builtin.unreachable`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | registered result from an Ansible task |

## [Examples](unreachable_test.md#id3)

```yaml+jinja
# test 'status' to know how to respond
{{ taskresults is unreachable }}
```

## [Return Value](unreachable_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the task flagged the host as unreachable, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
