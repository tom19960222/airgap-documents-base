---
collection: ansible
version: "8"
title: "community.general.version_sort filter – Sort a list according to version order instead of pure alphabetical one"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/version_sort_filter.html
fetched_at: 2026-07-28T01:52:30+00:00
---
# community.general.version_sort filter – Sort a list according to version order instead of pure alphabetical one

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
> To use it in a playbook, specify: `community.general.version_sort`.

New in community.general 2.2.0

- [Synopsis](version_sort_filter.md#synopsis)
- [Input](version_sort_filter.md#input)
- [Examples](version_sort_filter.md#examples)
- [Return Value](version_sort_filter.md#return-value)

## [Synopsis](version_sort_filter.md#id1)

- Sort a list according to version order instead of pure alphabetical one.

## [Input](version_sort_filter.md#id2)

This describes the input of the filter, the value before `| community.general.version_sort`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=string / required | A list of strings to sort. |

## [Examples](version_sort_filter.md#id3)

```yaml+jinja
- name: Convert list of tuples into dictionary
  ansible.builtin.set_fact:
    dictionary: "{{ ['2.1', '2.10', '2.9'] | community.general.version_sort }}"
    # Result is ['2.1', '2.9', '2.10']
```

## [Return Value](version_sort_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | The list of strings sorted by version.  **Returned:** success |

### Authors

- Eric L. (@ericzolf)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
