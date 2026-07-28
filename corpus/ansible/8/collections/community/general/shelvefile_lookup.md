---
collection: ansible
version: "8"
title: "community.general.shelvefile lookup – read keys from Python shelve file"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/shelvefile_lookup.html
fetched_at: 2026-07-28T01:53:01+00:00
---
# community.general.shelvefile lookup – read keys from Python shelve file

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
> To use it in a playbook, specify: `community.general.shelvefile`.

- [Synopsis](shelvefile_lookup.md#synopsis)
- [Terms](shelvefile_lookup.md#terms)
- [Keyword parameters](shelvefile_lookup.md#keyword-parameters)
- [Notes](shelvefile_lookup.md#notes)
- [Examples](shelvefile_lookup.md#examples)
- [Return Value](shelvefile_lookup.md#return-value)

## [Synopsis](shelvefile_lookup.md#id1)

- Read keys from Python shelve file.

## [Terms](shelvefile_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  string | Sets of key value pairs of parameters. |

## [Keyword parameters](shelvefile_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.shelvefile', key1=value1, key2=value2, ...)` and `query('community.general.shelvefile', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **file**  string / required | Path to shelve file. |
| **key**  string / required | Key to query. |

## [Notes](shelvefile_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.shelvefile', term1, term2, key1=value1, key2=value2)` and `query('community.general.shelvefile', term1, term2, key1=value1, key2=value2)`

## [Examples](shelvefile_lookup.md#id5)

```yaml+jinja
- name: Retrieve a string value corresponding to a key inside a Python shelve file
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.shelvefile', 'file=path_to_some_shelve_file.db key=key_to_retrieve') }}"
```

## [Return Value](shelvefile_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | Value(s) of key(s) in shelve file(s).  **Returned:** success |

### Authors

- Alejandro Guirao

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
