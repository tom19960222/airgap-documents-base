---
collection: ansible
version: "8"
title: "community.general.counter filter – Counts hashable elements in a sequence"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/counter_filter.html
fetched_at: 2026-07-28T01:52:15+00:00
---
# community.general.counter filter – Counts hashable elements in a sequence

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
> To use it in a playbook, specify: `community.general.counter`.

New in community.general 4.3.0

- [Synopsis](counter_filter.md#synopsis)
- [Input](counter_filter.md#input)
- [Examples](counter_filter.md#examples)
- [Return Value](counter_filter.md#return-value)

## [Synopsis](counter_filter.md#id1)

- Counts hashable elements in a sequence.

## [Input](counter_filter.md#id2)

This describes the input of the filter, the value before `| community.general.counter`.

| Parameter | Comments |
| --- | --- |
| **Input**  list / elements=any / required | A sequence. |

## [Examples](counter_filter.md#id3)

```yaml+jinja
- name: Count occurrences
  ansible.builtin.debug:
    msg: >-
      {{ [1, 'a', 2, 2, 'a', 'b', 'a'] | community.general.counter }}
    # Produces: {1: 1, 'a': 3, 2: 2, 'b': 1}
```

## [Return Value](counter_filter.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  dictionary | A dictionary with the elements of the sequence as keys, and their number of occurrences in the sequence as values.  **Returned:** success |

### Authors

- Rémy Keil (@keilr)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
