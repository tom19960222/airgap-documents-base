---
collection: ansible
version: "6"
title: "community.general.flattened lookup – return single list completely flattened"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/flattened_lookup.html
fetched_at: 2026-07-27T17:15:04+00:00
---
# community.general.flattened lookup – return single list completely flattened

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.flattened`.

- [Synopsis](flattened_lookup.md#synopsis)
- [Terms](flattened_lookup.md#terms)
- [Notes](flattened_lookup.md#notes)
- [Examples](flattened_lookup.md#examples)
- [Return Value](flattened_lookup.md#return-value)

## [Synopsis](flattened_lookup.md#id1)

- given one or more lists, this lookup will flatten any list elements found recursively until only 1 list is left.

## [Terms](flattened_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string / required | lists to flatten |

## [Notes](flattened_lookup.md#id3)

> **Note:**
>
> - unlike ‘items’ which only flattens 1 level, this plugin will continue to flatten until it cannot find lists anymore.
> - aka highlander plugin, there can only be one (list).

## [Examples](flattened_lookup.md#id4)

```yaml+jinja
- name: "'unnest' all elements into single list"
  ansible.builtin.debug:
    msg: "all in one list {{lookup('community.general.flattened', [1,2,3,[5,6]], ['a','b','c'], [[5,6,1,3], [34,'a','b','c']])}}"
```

## [Return Value](flattened_lookup.md#id5)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | flattened list  Returned: success |

### Authors

- Serge van Ginderachter

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
