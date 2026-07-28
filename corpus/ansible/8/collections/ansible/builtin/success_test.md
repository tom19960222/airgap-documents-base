---
collection: ansible
version: "8"
title: "ansible.builtin.success test – check task success"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/success_test.html
fetched_at: 2026-07-28T01:08:58+00:00
---
# ansible.builtin.success test – check task success

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `success`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.success` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](success_test.md#synopsis)
- [Input](success_test.md#input)
- [Examples](success_test.md#examples)
- [Return Value](success_test.md#return-value)

## [Synopsis](success_test.md#id1)

- Tests if task finished successfully, opposite of `failed`.
- This test checks for the existance of a `failed` key in the input dictionary and that it is `False` if present

Aliases: succeeded, successful

## [Input](success_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.success` or `is not ansible.builtin.success`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | registered result from an Ansible task |

## [Examples](success_test.md#id3)

```yaml+jinja
# test 'status' to know how to respond
{{ taskresults is success }}
```

## [Return Value](success_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the task was successfully completed, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
