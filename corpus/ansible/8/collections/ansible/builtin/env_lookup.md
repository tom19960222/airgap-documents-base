---
collection: ansible
version: "8"
title: "ansible.builtin.env lookup – Read the value of environment variables"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/env_lookup.html
fetched_at: 2026-07-28T01:08:30+00:00
---
# ansible.builtin.env lookup – Read the value of environment variables

> **Note:**
>
> This lookup plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `env`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.env` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same lookup plugin name.

- [Synopsis](env_lookup.md#synopsis)
- [Terms](env_lookup.md#terms)
- [Keyword parameters](env_lookup.md#keyword-parameters)
- [Notes](env_lookup.md#notes)
- [Examples](env_lookup.md#examples)
- [Return Value](env_lookup.md#return-value)

## [Synopsis](env_lookup.md#id1)

- Allows you to query the environment variables available on the controller when you invoked Ansible.

## [Terms](env_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | Environment variable or list of them to lookup the values for. |

## [Keyword parameters](env_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('ansible.builtin.env', key1=value1, key2=value2, ...)` and `query('ansible.builtin.env', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **default**  any  *added in ansible-core 2.13* | What return when the variable is undefined  **Default:** `""` |

## [Notes](env_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('ansible.builtin.env', term1, term2, key1=value1, key2=value2)` and `query('ansible.builtin.env', term1, term2, key1=value1, key2=value2)`
> - You can pass the `Undefined` object as `default` to force an undefined error

## [Examples](env_lookup.md#id5)

```yaml+jinja
- name: Basic usage
  ansible.builtin.debug:
    msg: "'{{ lookup('ansible.builtin.env', 'HOME') }}' is the HOME environment variable."

- name: Before 2.13, how to set default value if the variable is not defined.
        This cannot distinguish between USR undefined and USR=''.
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.env', 'USR')|default('nobody', True) }} is the user."

- name: Example how to set default value if the variable is not defined, ignores USR=''
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.env', 'USR', default='nobody') }} is the user."

- name: Set default value to Undefined, if the variable is not defined
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.env', 'USR', default=Undefined) }} is the user."

- name: Set default value to undef(), if the variable is not defined
  ansible.builtin.debug:
    msg: "{{ lookup('ansible.builtin.env', 'USR', default=undef()) }} is the user."
```

## [Return Value](env_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | Values from the environment variables.  **Returned:** success |

### Authors

- Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
