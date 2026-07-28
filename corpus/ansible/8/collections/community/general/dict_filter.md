---
collection: ansible
version: "8"
title: "community.general.dict filter – Convert a list of tuples into a dictionary"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/dict_filter.html
fetched_at: 2026-07-28T01:52:16+00:00
---
# community.general.dict filter – Convert a list of tuples into a dictionary

> **Note:**
>
> This filter plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.dict`.

New in community.general 3.0.0

- [Synopsis](dict_filter.md#synopsis)
- [Input](dict_filter.md#input)
- [Examples](dict_filter.md#examples)
- [Return Value](dict_filter.md#return-value)

## [Synopsis](dict_filter.md#id1)

- Convert a list of tuples into a dictionary. This is a filter version of the `dict` function.

## [Input](dict_filter.md#id2)

This describes the input of the filter, the value before `| community.general.dict`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=list / required | A list of tuples (with exactly two elements). |

## [Examples](dict_filter.md#id3)

```yaml+jinja
- name: Convert list of tuples into dictionary
  ansible.builtin.set_fact:
    dictionary: "{{ [[1, 2], ['a', 'b']] | community.general.dict }}"
    # Result is {1: 2, 'a': 'b'}

- name: Create a list of dictionaries with map and the community.general.dict filter
  ansible.builtin.debug:
    msg: >-
      {{ values | map('zip', ['k1', 'k2', 'k3'])
                | map('map', 'reverse')
                | map('community.general.dict') }}
  vars:
    values:
      - - foo
        - 23
        - a
      - - bar
        - 42
        - b
  # Produces the following list of dictionaries:
  #   {
  #     "k1": "foo",
  #     "k2": 23,
  #     "k3": "a"
  #   },
  #   {
  #     "k1": "bar",
  #     "k2": 42,
  #     "k3": "b"
  #   }
```

## [Return Value](dict_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  boolean | The dictionary having the provided key-value pairs.  **Returned:** success |

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
