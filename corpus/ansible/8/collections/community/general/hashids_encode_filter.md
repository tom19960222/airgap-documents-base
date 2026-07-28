---
collection: ansible
version: "8"
title: "community.general.hashids_encode filter – Encodes YouTube-like hashes from a sequence of integers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/hashids_encode_filter.html
fetched_at: 2026-07-28T01:52:20+00:00
---
# community.general.hashids_encode filter – Encodes YouTube-like hashes from a sequence of integers

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
> To use it in a playbook, specify: `community.general.hashids_encode`.

New in community.general 3.0.0

- [Synopsis](hashids_encode_filter.md#synopsis)
- [Input](hashids_encode_filter.md#input)
- [Keyword parameters](hashids_encode_filter.md#keyword-parameters)
- [Examples](hashids_encode_filter.md#examples)
- [Return Value](hashids_encode_filter.md#return-value)

## [Synopsis](hashids_encode_filter.md#id1)

- Encodes YouTube-like hashes from a sequence of integers.

## [Input](hashids_encode_filter.md#id2)

This describes the input of the filter, the value before `| community.general.hashids_encode`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=integer / required | A list of integers. |

## [Keyword parameters](hashids_encode_filter.md#id3)

This describes keyword parameters of the filter. These are the values `key1=value1`, `key2=value2` and so on in the following
example: `input | community.general.hashids_encode(key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **alphabet**  list / elements=string | String of 16 or more unique characters to produce a hash. |
| **min_length**  integer | Minimum length of hash produced. |
| **salt**  string | String to use as salt when hashing.  **Default:** `"excel"` |

## [Examples](hashids_encode_filter.md#id4)

```yaml+jinja
- name: Convert list of integers to hash
  ansible.builtin.debug:
    msg: "{{ [1, 2, 3] | community.general.hashids_encode }}"
    # Produces: 'o2fXhV'
```

## [Return Value](hashids_encode_filter.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  string | A YouTube-like hash.  **Returned:** success |

### Authors

- Andrew Pantuso (@Ajpantuso)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
