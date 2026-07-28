---
collection: ansible
version: "8"
title: "ansible.builtin.reachable test – Task did not end due to unreachable host"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/reachable_test.html
fetched_at: 2026-07-28T01:08:53+00:00
---
# ansible.builtin.reachable test – Task did not end due to unreachable host

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `reachable`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.reachable` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](reachable_test.md#synopsis)
- [Input](reachable_test.md#input)
- [Examples](reachable_test.md#examples)
- [Return Value](reachable_test.md#return-value)

## [Synopsis](reachable_test.md#id1)

- Tests if task was able to reach the host for execution
- This test checks for the existance of a `unreachable` key in the input dictionary and that it is `False` if present

## [Input](reachable_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.reachable` or `is not ansible.builtin.reachable`.

| Parameter | Comments |
| --- | --- |
| **Input**  dictionary / required | registered result from an Ansible task |

## [Examples](reachable_test.md#id3)

```yaml+jinja
# test 'status' to know how to respond
{{ taskresults is reachable }}
```

## [Return Value](reachable_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the task did not flag the host as unreachable, `False` otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
