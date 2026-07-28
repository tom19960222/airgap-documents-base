---
collection: ansible
version: "8"
title: "community.routeros.list_to_dict filter – Convert a list of arguments to a dictionary"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/routeros/list_to_dict_filter.html
fetched_at: 2026-07-28T01:59:06+00:00
---
# community.routeros.list_to_dict filter – Convert a list of arguments to a dictionary

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
> To use it in a playbook, specify: `community.routeros.list_to_dict`.

New in community.routeros 2.0.0

- [Synopsis](list_to_dict_filter.md#synopsis)
- [Input](list_to_dict_filter.md#input)
- [Keyword parameters](list_to_dict_filter.md#keyword-parameters)
- [Examples](list_to_dict_filter.md#examples)
- [Return Value](list_to_dict_filter.md#return-value)

## [Synopsis](list_to_dict_filter.md#id1)

- Convert a list of arguments to a dictionary.

## [Input](list_to_dict_filter.md#id2)

This describes the input of the filter, the value before `| community.routeros.list_to_dict`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | A list of assignments. Can be the result of the [community.routeros.split](split_filter.md#ansible-collections-community-routeros-split-filter) filter. |

## [Keyword parameters](list_to_dict_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | community.routeros.list_to_dict(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **require_assignment**  boolean | Allows to accept arguments without values when set to `false`.  **Choices:**   - `false` - `true` ← (default) |
| **skip_empty_values**  boolean | Allows to skip arguments whose value is empty when set to `true`.  **Choices:**   - `false` ← (default) - `true` |

## [Examples](list_to_dict_filter.md#id4)

```yaml+jinja
- name: Convert a list to a dictionary
  ansible.builtin.set_fact:
    dictionary: "{{ ['foo=bar', 'comment=foo is bar'] | community.routeros.list_to_dict }}"
    # dictionary == {'foo': 'bar', 'comment': 'foo is bar'}
```

## [Return Value](list_to_dict_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | A dictionary representation of the input data.  **Returned:** success |

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
