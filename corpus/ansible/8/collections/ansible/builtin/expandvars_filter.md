---
collection: ansible
version: "8"
title: "ansible.builtin.expandvars filter – expand environment variables"
source_url: https://docs.ansible.com/projects/ansible/8/collections/ansible/builtin/expandvars_filter.html
fetched_at: 2026-07-28T01:08:03+00:00
---
# ansible.builtin.expandvars filter – expand environment variables

> **Note:**
>
> This filter plugin is part of `ansible-core` and included in all Ansible
> installations. In most cases, you can use the short
> plugin name
> `expandvars`.
> However, we recommend you use the [Fully Qualified Collection Name (FQCN)](../../../reference_appendices/glossary.md#term-Fully-Qualified-Collection-Name-FQCN) `ansible.builtin.expandvars` for easy linking to the
> plugin documentation and to avoid conflicting with other collections that may have
> the same filter plugin name.

- [Synopsis](expandvars_filter.md#synopsis)
- [Input](expandvars_filter.md#input)
- [Examples](expandvars_filter.md#examples)
- [Return Value](expandvars_filter.md#return-value)

## [Synopsis](expandvars_filter.md#id1)

- Will do a shell-like substitution of environment variables on the provided input.

## [Input](expandvars_filter.md#id2)

This describes the input of the filter, the value before `| ansible.builtin.expandvars`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A string that contains environment variables. |

## [Examples](expandvars_filter.md#id3)

```yaml+jinja
# To get '/home/myuser/stuff.txt' from '$HOME/stuff.txt'
{{ mypath | expandvars }}
```

## [Return Value](expandvars_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | The string with translated environment variable values.  **Returned:** success |

### Authors

- ansible core team

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible/ansible/issues)
- [Repository (Sources)](https://github.com/ansible/ansible)
- [Communication](index.md#communication-for-ansible-builtin)
