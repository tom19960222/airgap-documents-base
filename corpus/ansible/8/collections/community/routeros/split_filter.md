---
collection: ansible
version: "8"
title: "community.routeros.split filter – Split a command into arguments"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/routeros/split_filter.html
fetched_at: 2026-07-28T01:59:08+00:00
---
# community.routeros.split filter – Split a command into arguments

> **Note:**
>
> This filter plugin is part of the [community.routeros collection](https://galaxy.ansible.com/ui/repo/published/community/routeros/) (version 2.11.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.routeros`.
>
> To use it in a playbook, specify: `community.routeros.split`.

New in community.routeros 2.0.0

- [Synopsis](split_filter.md#synopsis)
- [Input](split_filter.md#input)
- [Examples](split_filter.md#examples)
- [Return Value](split_filter.md#return-value)

## [Synopsis](split_filter.md#id1)

- Split a command into arguments.

## [Input](split_filter.md#id2)

This describes the input of the filter, the value before `| community.routeros.split`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | A command. |

## [Examples](split_filter.md#id3)

```yaml+jinja
- name: Split command into list of arguments
  ansible.builtin.set_fact:
    argument_list: "{{ 'foo=bar comment="foo is bar" baz' | community.routeros.split }}"
    # Should result in ['foo=bar', 'comment=foo is bar', 'baz']
```

## [Return Value](split_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | The list of arguments.  **Returned:** success |

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.routeros/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.routeros)
- [Submit a bug report](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.routeros/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-routeros)
