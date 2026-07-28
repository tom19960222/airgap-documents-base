---
collection: ansible
version: "8"
title: "community.general.cartesian lookup – returns the cartesian product of lists"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/cartesian_lookup.html
fetched_at: 2026-07-28T01:52:41+00:00
---
# community.general.cartesian lookup – returns the cartesian product of lists

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.cartesian`.

- [Synopsis](cartesian_lookup.md#synopsis)
- [Terms](cartesian_lookup.md#terms)
- [Examples](cartesian_lookup.md#examples)
- [Return Value](cartesian_lookup.md#return-value)

## [Synopsis](cartesian_lookup.md#id1)

- Takes the input lists and returns a list that represents the product of the input lists.
- It is clearer with an example, it turns [1, 2, 3], [a, b] into [1, a], [1, b], [2, a], [2, b], [3, a], [3, b]. You can see the exact syntax in the examples section.

## [Terms](cartesian_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=list / required | a set of lists |

## [Examples](cartesian_lookup.md#id3)

```yaml+jinja
- name: Example of the change in the description
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.cartesian', [1,2,3], [a, b])}}"

- name: loops over the cartesian product of the supplied lists
  ansible.builtin.debug:
    msg: "{{item}}"
  with_community.general.cartesian:
    - "{{list1}}"
    - "{{list2}}"
    - [1,2,3,4,5,6]
```

## [Return Value](cartesian_lookup.md#id4)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=list | list of lists composed of elements of the input lists  **Returned:** success |

### Authors

- Unknown

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
