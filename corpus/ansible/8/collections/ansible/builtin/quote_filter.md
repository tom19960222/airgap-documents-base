---
collection: ansible
version: "8"
title: "ansible.builtin.quote filter – shell quoting"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/quote_filter.html
fetched_at: 2026-07-28T01:05:04+00:00
---
# ansible.builtin.quote filter – shell quoting

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `quote`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.quote` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

New in ansible-base 2.10

- [Synopsis](quote_filter.md#synopsis)
- [Input](quote_filter.md#input)
- [Notes](quote_filter.md#notes)
- [Examples](quote_filter.md#examples)
- [Return Value](quote_filter.md#return-value)

## [Synopsis](quote_filter.md#id1)

- Quote a string to safely use as in a POSIX shell.

## [Input](quote_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.quote`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | String to quote. |

## [Notes](quote_filter.md#id3)

> **Note:**
>
> - This is a passthrough to Python’s `shlex.quote`.

## [Examples](quote_filter.md#id4)

```yaml+jinja
- name: Run a shell command
  shell: echo {{ string_value | quote }}
```

## [Return Value](quote_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | Quoted string.  **Returned:** success |

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
