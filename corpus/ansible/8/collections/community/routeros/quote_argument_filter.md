---
collection: ansible
version: "8"
title: "community.routeros.quote_argument filter – Quote an argument"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/routeros/quote_argument_filter.html
fetched_at: 2026-07-28T01:59:07+00:00
---
# community.routeros.quote_argument filter – Quote an argument

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
> To use it in a playbook, specify: `community.routeros.quote_argument`.

New in community.routeros 2.0.0

- [Synopsis](quote_argument_filter.md#synopsis)
- [Input](quote_argument_filter.md#input)
- [Examples](quote_argument_filter.md#examples)
- [Return Value](quote_argument_filter.md#return-value)

## [Synopsis](quote_argument_filter.md#id1)

- Quote an argument.

## [Input](quote_argument_filter.md#id2)

This describes the input of the filter, the value before `| community.routeros.quote_argument`.

| Parameter | Comments |
| --- | --- |
| **Input**  string / required | An argument to quote. |

## [Examples](quote_argument_filter.md#id3)

```yaml+jinja
- name: Quote a RouterOS CLI command argument
  ansible.builtin.set_fact:
    quoted: "{{ 'comment=this is a "comment"' | community.routeros.quote_argument }}"
    # Should result in 'comment="this is a \"comment\""'
```

## [Return Value](quote_argument_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | The quoted argument.  **Returned:** success |

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
