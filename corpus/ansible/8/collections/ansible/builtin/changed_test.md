---
collection: ansible
version: "8"
title: "ansible.builtin.changed test – did the task require changes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/changed_test.html
fetched_at: 2026-07-28T01:08:44+00:00
---
# ansible.builtin.changed test – did the task require changes

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `changed`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.changed` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](changed_test.md#synopsis)
- [Input](changed_test.md#input)
- [Examples](changed_test.md#examples)
- [Return Value](changed_test.md#return-value)

## [Synopsis](changed_test.md#id1)

- Tests if task required changes to complete
- This test checks for the existance of a `changed` key in the input dictionary and that it is `True` if present

Aliases: change

## [Input](changed_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.changed` or `is not ansible.builtin.changed`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | registered result from an Ansible task |

## [Examples](changed_test.md#id3)

```yaml+jinja
# test 'status' to know how to respond
{{ taskresults is changed }}
```

## [Return Value](changed_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the task was required changes, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
