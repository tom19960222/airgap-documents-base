---
collection: ansible
version: "8"
title: "ansible.builtin.started test – Was async task started"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/started_test.html
fetched_at: 2026-07-28T01:08:57+00:00
---
# ansible.builtin.started test – Was async task started

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `started`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.started` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](started_test.md#synopsis)
- [Input](started_test.md#input)
- [Examples](started_test.md#examples)
- [Return Value](started_test.md#return-value)

## [Synopsis](started_test.md#id1)

- Used to check if an async task has started, will also work with non async tasks but will issue a warning.
- This test checks for the existance of a `started` key in the input dictionary and that it is `1` if present

## [Input](started_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.started` or `is not ansible.builtin.started`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | registered result from an Ansible task |

## [Examples](started_test.md#id3)

```yaml+jinja
# test 'status' to know how to respond
{{ (asynctaskpoll is started}}
```

## [Return Value](started_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the task has started, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
