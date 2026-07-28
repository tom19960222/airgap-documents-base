---
collection: ansible
version: "8"
title: "ansible.builtin.failed test – did the task fail"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/failed_test.html
fetched_at: 2026-07-28T01:08:47+00:00
---
# ansible.builtin.failed test – did the task fail

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `failed`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.failed` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](failed_test.md#synopsis)
- [Input](failed_test.md#input)
- [Examples](failed_test.md#examples)
- [Return Value](failed_test.md#return-value)

## [Synopsis](failed_test.md#id1)

- Tests if task finished in failure, opposite of `succeeded`.
- This test checks for the existance of a `failed` key in the input dictionary and that it is `True` if present.
- Tasks that get skipped or not executed due to other failures (syntax, templating, unreachable host, etc) do not return a ‘failed’ status.

Aliases: failure

## [Input](failed_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.failed` or `is not ansible.builtin.failed`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | registered result from an Ansible task |

## [Examples](failed_test.md#id3)

```yaml+jinja
# test 'status' to know how to respond
{{ taskresults is failed }}
```

## [Return Value](failed_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the task was failed, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
