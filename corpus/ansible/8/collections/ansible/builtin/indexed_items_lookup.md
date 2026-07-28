---
collection: ansible
version: "8"
title: "ansible.builtin.indexed_items lookup – rewrites lists to return ‘indexed items’"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/indexed_items_lookup.html
fetched_at: 2026-07-28T01:05:23+00:00
---
# ansible.builtin.indexed_items lookup – rewrites lists to return ‘indexed items’

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `indexed_items`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.indexed_items` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](indexed_items_lookup.md#synopsis)
- [Terms](indexed_items_lookup.md#terms)
- [Examples](indexed_items_lookup.md#examples)
- [Return Value](indexed_items_lookup.md#return-value)

## [Synopsis](indexed_items_lookup.md#id1)

- use this lookup if you want to loop over an array and also get the numeric index of where you are in the array as you go
- any list given will be transformed with each resulting element having the it’s previous position in item.0 and its value in item.1

## [Terms](indexed_items_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | list of items |

## [Examples](indexed_items_lookup.md#id3)

```yaml+jinja
- name: indexed loop demo
  ansible.builtin.debug:
    msg: "at array position {{ item.0 }} there is a value {{ item.1 }}"
  with_indexed_items:
    - "{{ some_list }}"
```

## [Return Value](indexed_items_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=list | list with each item.0 giving you the position and item.1 the value  **Returned:** success |

### Authors

- Michael DeHaan

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
