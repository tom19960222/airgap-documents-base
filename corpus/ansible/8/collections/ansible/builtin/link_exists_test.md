---
collection: ansible
version: "8"
title: "ansible.builtin.link_exists test – does the path exist, no follow"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/link_exists_test.html
fetched_at: 2026-07-28T01:08:50+00:00
---
# ansible.builtin.link_exists test – does the path exist, no follow

> **Note:**
>
> This test plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `link_exists`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.link_exists` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same test plugin name.

- [Synopsis](link_exists_test.md#synopsis)
- [Input](link_exists_test.md#input)
- [Examples](link_exists_test.md#examples)
- [Return Value](link_exists_test.md#return-value)

## [Synopsis](link_exists_test.md#id1)

- Check if the provided path maps to an existing symlink on the controller’s filesystem (localhost).
- Does not follow symlinks, so it only verifies that the link itself exists.

## [Input](link_exists_test.md#id2)

This describes the input of the test, the value before `is ansible.builtin.link_exists` or `is not ansible.builtin.link_exists`.

| Parameter | Comments |
| --- | --- |
| **Input**  path | A path. |

## [Examples](link_exists_test.md#id3)

```yaml+jinja
ismyhostsalink: "{{ '/etc/hosts' is link_exists}}"
list_of_symlinks: "{{ list_of_paths | select('link_exists') }}"
```

## [Return Value](link_exists_test.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | Returns `True` if the path corresponds to an existing filesystem object on the controller, `False` if otherwise.  **Returned:** success |

### Authors

- Ansible Core

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
