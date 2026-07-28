---
collection: ansible
version: "8"
title: "ansible.builtin.vars lookup – Lookup templated value of variables"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/vars_lookup.html
fetched_at: 2026-07-28T01:03:58+00:00
---
# ansible.builtin.vars lookup – Lookup templated value of variables

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `vars`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.vars` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](vars_lookup.md#synopsis)
- [Terms](vars_lookup.md#terms)
- [Keyword parameters](vars_lookup.md#keyword-parameters)
- [Notes](vars_lookup.md#notes)
- [Examples](vars_lookup.md#examples)
- [Return Value](vars_lookup.md#return-value)

## [Synopsis](vars_lookup.md#id1)

- Retrieves the value of an Ansible variable. Note: Only returns top level variable names.

## [Terms](vars_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | The variable names to look up. |

## [Keyword parameters](vars_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.vars', key1=value1, key2=value2, ...)` and `query('ansible.builtin.vars', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **default**  string | What to return if a variable is undefined.  If no default is set, it will result in an error if any of the variables is undefined. |

## [Notes](vars_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('ansible.builtin.vars', term1, term2, key1=value1, key2=value2)` and `query('ansible.builtin.vars', term1, term2, key1=value1, key2=value2)`

## [Examples](vars_lookup.md#id5)

```yaml+jinja
- name: Show value of 'variablename'
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.vars', 'variabl' + myvar) }}"
  vars:
    variablename: hello
    myvar: ename

- name: Show default empty since i dont have 'variablnotename'
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.vars', 'variabl' + myvar, default='')}}"
  vars:
    variablename: hello
    myvar: notename

- name: Produce an error since i dont have 'variablnotename'
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.vars', 'variabl' + myvar)}}"
  ignore_errors: True
  vars:
    variablename: hello
    myvar: notename

- name: find several related variables
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.vars', 'ansible_play_hosts', 'ansible_play_batch', 'ansible_play_hosts_all') }}"

- name: Access nested variables
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.vars', 'variabl' + myvar).sub_var }}"
  ignore_errors: True
  vars:
    variablename:
        sub_var: 12
    myvar: ename

- name: alternate way to find some 'prefixed vars' in loop
  ansible.builtin.debug: msg="{{ lookup('ansible.builtin.vars', 'ansible_play_' + item) }}"
  loop:
    - hosts
    - batch
    - hosts_all
```

## [Return Value](vars_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=any | value of the variables requested.  **Returned:** success |

### Authors

- Ansible Core Team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
