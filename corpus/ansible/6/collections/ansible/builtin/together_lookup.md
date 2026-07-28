---
collection: ansible
version: "6"
title: "ansible.builtin.together lookup – merges lists into synchronized list"
source_url: https://docs.ansible.com/projects/ansible/6/collections/ansible/builtin/together_lookup.html
fetched_at: 2026-07-27T16:44:24+00:00
---
# ansible.builtin.together lookup – merges lists into synchronized list

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `together` even without specifying the `collections:` keyword.
> However, we recommend you use the FQCN for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](together_lookup.md#synopsis)
- [Terms](together_lookup.md#terms)
- [Examples](together_lookup.md#examples)
- [Return Value](together_lookup.md#return-value)

## [Synopsis](together_lookup.md#id1)

- Creates a list with the iterated elements of the supplied lists
- To clarify with an example, [ ‘a’, ‘b’ ] and [ 1, 2 ] turn into [ (‘a’,1), (‘b’, 2) ]
- This is basically the same as the ‘zip_longest’ filter and Python function
- Any ‘unbalanced’ elements will be substituted with ‘None’

## [Terms](together_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | list of lists to merge |

## [Examples](together_lookup.md#id3)

```yaml+jinja
- name: item.0 returns from the 'a' list, item.1 returns from the '1' list
  ansible.builtin.debug:
    msg: "{{ item.0 }} and {{ item.1 }}"
  with_together:
    - ['a', 'b', 'c', 'd']
    - [1, 2, 3, 4]
```

## [Return Value](together_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=list | synchronized list  Returned: success |

### Authors

- Bradley Young

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible/ansible/issues)
[Repository (Sources)](https://github.com/ansible/ansible)
[Communication](index.md#communication-for-ansible-builtin)
