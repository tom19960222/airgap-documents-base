---
collection: ansible
version: "6"
title: "community.general.collection_version lookup – Retrieves the version of an installed collection"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/collection_version_lookup.html
fetched_at: 2026-07-27T17:14:56+00:00
---
# community.general.collection_version lookup – Retrieves the version of an installed collection

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
> To use it in a playbook, specify: `community.general.collection_version`.

New in community.general 4.0.0

- [Synopsis](collection_version_lookup.md#synopsis)
- [Terms](collection_version_lookup.md#terms)
- [Keyword parameters](collection_version_lookup.md#keyword-parameters)
- [Notes](collection_version_lookup.md#notes)
- [Examples](collection_version_lookup.md#examples)
- [Return Value](collection_version_lookup.md#return-value)

## [Synopsis](collection_version_lookup.md#id1)

- This lookup allows to query the version of an installed collection, and to determine whether a collection is installed at all.
- By default it returns `none` for non-existing collections and `*` for collections without a version number. The latter should only happen in development environments, or when installing a collection from git which has no version in its `galaxy.yml`. This behavior can be adjusted by providing other values with *result_not_found* and *result_no_version*.

## [Terms](collection_version_lookup.md#id2)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | The collections to look for.  For example `community.general`. |

## [Keyword parameters](collection_version_lookup.md#id3)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.collection_version', key1=value1, key2=value2, ...)` and `query('community.general.collection_version', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **result_no_version**  string | The value to return when the collection has no version number.  This can happen for collections installed from git which do not have a version number in `galaxy.yml`.  By default, `*` is returned.  Default: `"*"` |
| **result_not_found**  string | The value to return when the collection could not be found.  By default, `none` is returned. |

## [Notes](collection_version_lookup.md#id4)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.collection_version', term1, term2, key1=value1, key2=value2)` and `query('community.general.collection_version', term1, term2, key1=value1, key2=value2)`

## [Examples](collection_version_lookup.md#id5)

```yaml+jinja
- name: Check version of community.general
  ansible.builtin.debug:
    msg: "community.general version {{ lookup('community.general.collection_version', 'community.general') }}"
```

## [Return Value](collection_version_lookup.md#id6)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | The version number of the collections listed as input.  If a collection can not be found, it will return the value provided in *result_not_found*. By default, this is `none`.  If a collection can be found, but the version not identified, it will return the value provided in *result_no_version*. By default, this is `*`. This can happen for collections installed from git which do not have a version number in `galaxy.yml`.  Returned: success |

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
