---
collection: ansible
version: "8"
title: "ansible.builtin.dict lookup – returns key/value pair items from dictionaries"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/dict_lookup.html
fetched_at: 2026-07-28T01:08:29+00:00
---
# ansible.builtin.dict lookup – returns key/value pair items from dictionaries

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `dict`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.dict` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](dict_lookup.md#synopsis)
- [Terms](dict_lookup.md#terms)
- [Examples](dict_lookup.md#examples)
- [Return Value](dict_lookup.md#return-value)

## [Synopsis](dict_lookup.md#id1)

- Takes dictionaries as input and returns a list with each item in the list being a dictionary with ‘key’ and ‘value’ as keys to the previous dictionary’s structure.

## [Terms](dict_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | A list of dictionaries |

## [Examples](dict_lookup.md#id3)

```yaml+jinja
vars:
  users:
    alice:
      name: Alice Appleworth
      telephone: 123-456-7890
    bob:
      name: Bob Bananarama
      telephone: 987-654-3210
tasks:
  # with predefined vars
  - name: Print phone records
    ansible.builtin.debug:
      msg: "User {{ item.key }} is {{ item.value.name }} ({{ item.value.telephone }})"
    loop: "{{ lookup('ansible.builtin.dict', users) }}"
  # with inline dictionary
  - name: show dictionary
    ansible.builtin.debug:
      msg: "{{item.key}}: {{item.value}}"
    with_dict: {a: 1, b: 2, c: 3}
  # Items from loop can be used in when: statements
  - name: set_fact when alice in key
    ansible.builtin.set_fact:
      alice_exists: true
    loop: "{{ lookup('ansible.builtin.dict', users) }}"
    when: "'alice' in item.key"
```

## [Return Value](dict_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | list of composed dictonaries with key and value  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
