---
collection: ansible
version: "8"
title: "ansible.builtin.finished test – Did async task finish"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/finished_test.html
fetched_at: 2026-07-28T01:08:49+00:00
---
# ansible.builtin.finished test – Did async task finish

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `finished`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.finished` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](finished_test.md#synopsis)
- [Input](finished_test.md#input)
- [Examples](finished_test.md#examples)
- [Return Value](finished_test.md#return-value)

## [Synopsis](finished_test.md#id1)

- Used to test if an async task has finished, it will aslo work with normal tasks but will issue a warning.
- This test checks for the existance of a `finished` key in the input dictionary and that it is `1` if present

## [Input](finished_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.finished` or `is not ansible.builtin.finished`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | registered result from an Ansible task |

## [Examples](finished_test.md#id3)

```yaml+jinja
# test 'status' to know how to respond
{{ (asynctaskpoll is finished}}
```

## [Return Value](finished_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the aysnc task has finished, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
