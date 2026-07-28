---
collection: ansible
version: "8"
title: "community.general.groupby_as_dict filter – Transform a sequence of dictionaries to a dictionary where the dictionaries are indexed by an attribute"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/groupby_as_dict_filter.html
fetched_at: 2026-07-28T01:52:18+00:00
---
# community.general.groupby_as_dict filter – Transform a sequence of dictionaries to a dictionary where the dictionaries are indexed by an attribute

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
> To use it in a playbook, specify: `community.general.groupby_as_dict`.

New in community.general 3.1.0

- [Synopsis](groupby_as_dict_filter.md#synopsis)
- [Input](groupby_as_dict_filter.md#input)
- [Positional parameters](groupby_as_dict_filter.md#positional-parameters)
- [Examples](groupby_as_dict_filter.md#examples)
- [Return Value](groupby_as_dict_filter.md#return-value)

## [Synopsis](groupby_as_dict_filter.md#id1)

- Transform a sequence of dictionaries to a dictionary where the dictionaries are indexed by an attribute.

## [Input](groupby_as_dict_filter.md#id2)

This describes the input of the filter, the value before `| community.general.groupby_as_dict`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=dictionary / required | A list of dictionaries |

## [Positional parameters](groupby_as_dict_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | community.general.groupby_as_dict(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **attribute**  string / required | The attribute to use as the key. |

## [Examples](groupby_as_dict_filter.md#id4)

```yaml+jinja
- name: Arrange a list of dictionaries as a dictionary of dictionaries
  ansible.builtin.debug:
    msg: "{{ sequence | community.general.groupby_as_dict('key') }}"
  vars:
    sequence:
      - key: value
        foo: bar
      - key: other_value
        baz: bar
  # Produces the following nested structure:
  #
  #  value:
  #    key: value
  #    foo: bar
  #  other_value:
  #    key: other_value
  #    baz: bar
```

## [Return Value](groupby_as_dict_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | A dictionary containing the dictionaries from the list as values.  **Returned:** success |

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
