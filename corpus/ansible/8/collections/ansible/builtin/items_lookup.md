---
collection: ansible
version: "8"
title: "ansible.builtin.items lookup – list of items"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/items_lookup.html
fetched_at: 2026-07-28T01:05:18+00:00
---
# ansible.builtin.items lookup – list of items

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `items`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.items` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](items_lookup.md#synopsis)
- [Terms](items_lookup.md#terms)
- [Notes](items_lookup.md#notes)
- [Examples](items_lookup.md#examples)
- [Return Value](items_lookup.md#return-value)

## [Synopsis](items_lookup.md#id1)

- this lookup returns a list of items given to it, if any of the top level items is also a list it will flatten it, but it will not recurse

## [Terms](items_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | list of items |

## [Notes](items_lookup.md#id3)

> **Note:**
>
> - this is the standard lookup used for loops in most examples
> - check out the ‘flattened’ lookup for recursive flattening
> - if you do not want flattening nor any other transformation look at the ‘list’ lookup.

## [Examples](items_lookup.md#id4)

```yaml+jinja
- name: "loop through list"
  ansible.builtin.debug:
    msg: "An item: {{ item }}"
  with_items:
    - 1
    - 2
    - 3

- name: add several users
  ansible.builtin.user:
    name: "{{ item }}"
    groups: "wheel"
    state: present
  with_items:
     - testuser1
     - testuser2

- name: "loop through list from a variable"
  ansible.builtin.debug:
    msg: "An item: {{ item }}"
  with_items: "{{ somelist }}"

- name: more complex items to add several users
  ansible.builtin.user:
    name: "{{ item.name }}"
    uid: "{{ item.uid }}"
    groups: "{{ item.groups }}"
    state: present
  with_items:
     - { name: testuser1, uid: 1002, groups: "wheel, staff" }
     - { name: testuser2, uid: 1003, groups: staff }
```

## [Return Value](items_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | once flattened list  **Returned:** success |

### Authors

- Michael DeHaan

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
