---
collection: ansible
version: "8"
title: "ansible.builtin.varnames lookup – Lookup matching variable names"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/varnames_lookup.html
fetched_at: 2026-07-28T01:08:40+00:00
---
# ansible.builtin.varnames lookup – Lookup matching variable names

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `varnames`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.varnames` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

New in Ansible 2.8

- [Synopsis](varnames_lookup.md#synopsis)
- [Terms](varnames_lookup.md#terms)
- [Examples](varnames_lookup.md#examples)
- [Return Value](varnames_lookup.md#return-value)

## [Synopsis](varnames_lookup.md#id1)

- Retrieves a list of matching Ansible variable names.

## [Terms](varnames_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | List of Python regex patterns to search for in variable names. |

## [Examples](varnames_lookup.md#id3)

```yaml+jinja
- name: List variables that start with qz_
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.varnames', '^qz_.+')}}"
  vars:
    qz_1: hello
    qz_2: world
    qa_1: "I won't show"
    qz_: "I won't show either"

- name: Show all variables
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.varnames', '.+')}}"

- name: Show variables with 'hosts' in their names
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.varnames', 'hosts')}}"

- name: Find several related variables that end specific way
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.varnames', '.+_zone$', '.+_location$') }}"
```

## [Return Value](varnames_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | List of the variable names requested.  **Returned:** success |

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
