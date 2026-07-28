---
collection: ansible
version: "6"
title: "ansible.builtin.list lookup – simply returns what it is given."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/list_lookup.html
fetched_at: 2026-07-27T16:44:21+00:00
---
# ansible.builtin.list lookup – simply returns what it is given.

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `list` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](list_lookup.md#synopsis)
- [Examples](list_lookup.md#examples)
- [Return Value](list_lookup.md#return-value)

## [Synopsis](list_lookup.md#id1)

- this is mostly a noop, to be used as a with_list loop when you dont want the content transformed in any way.

## [Examples](list_lookup.md#id2)

```yaml+jinja
- name: unlike with_items you will get 3 items from this loop, the 2nd one being a list
  ansible.builtin.debug: var=item
  with_list:
    - 1
    - [2,3]
    - 4
```

## [Return Value](list_lookup.md#id3)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=any | basically the same as you fed in  Returned: success |

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
