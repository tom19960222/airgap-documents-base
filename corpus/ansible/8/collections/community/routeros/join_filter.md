---
collection: ansible
version: "8"
title: "community.routeros.join filter – Join a list of arguments to a command"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/routeros/join_filter.html
fetched_at: 2026-07-28T01:59:05+00:00
---
# community.routeros.join filter – Join a list of arguments to a command

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
> To use it in a playbook, specify: `community.routeros.join`.

New in community.routeros 2.0.0

- [Synopsis](join_filter.md#synopsis)
- [Input](join_filter.md#input)
- [Examples](join_filter.md#examples)
- [Return Value](join_filter.md#return-value)

## [Synopsis](join_filter.md#id1)

- Join and quotes a list of arguments to a command.

## [Input](join_filter.md#id2)

This describes the input of the filter, the value before `| community.routeros.join`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | A list of arguments to quote and join. |

## [Examples](join_filter.md#id3)

```yaml+jinja
- name: Join arguments for a RouterOS CLI command
  ansible.builtin.set_fact:
    arguments: "{{ ['foo=bar', 'comment=foo is bar'] | community.routeros.join }}"
    # Should result in 'foo=bar comment="foo is bar"'
```

## [Return Value](join_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  string | The joined and quoted result.  **Returned:** success |

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
