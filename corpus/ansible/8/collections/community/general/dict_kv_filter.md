---
collection: ansible
version: "8"
title: "community.general.dict_kv filter – Convert a value to a dictionary with a single key-value pair"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/dict_kv_filter.html
fetched_at: 2026-07-28T01:52:17+00:00
---
# community.general.dict_kv filter – Convert a value to a dictionary with a single key-value pair

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
> To use it in a playbook, specify: `community.general.dict_kv`.

New in community.general 1.3.0

- [Synopsis](dict_kv_filter.md#synopsis)
- [Input](dict_kv_filter.md#input)
- [Positional parameters](dict_kv_filter.md#positional-parameters)
- [Examples](dict_kv_filter.md#examples)
- [Return Value](dict_kv_filter.md#return-value)

## [Synopsis](dict_kv_filter.md#id1)

- Convert a value to a dictionary with a single key-value pair.

## [Input](dict_kv_filter.md#id2)

This describes the input of the filter, the value before `| community.general.dict_kv`.

| Parameter | Comments |
| --- | --- |
| **Input**  any / required | The value for the single key-value pair. |

## [Positional parameters](dict_kv_filter.md#id3)

This describes positional parameters of the filter. These are the values `positional1`, `positional2` and so on in the following
example: `input | community.general.dict_kv(positional1, positional2, ...)`

| Parameter | Comments |
| --- | --- |
| **key**  any / required | The key for the single key-value pair. |

## [Examples](dict_kv_filter.md#id4)

```yaml+jinja
- name: Create a one-element dictionary from a value
  ansible.builtin.debug:
    msg: "{{ 'myvalue' | dict_kv('mykey') }}"
    # Produces the dictionary {'mykey': 'myvalue'}
```

## [Return Value](dict_kv_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | A dictionary with a single key-value pair.  **Returned:** success |

### Authors

- Stanislav German-Evtushenko (@giner)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
