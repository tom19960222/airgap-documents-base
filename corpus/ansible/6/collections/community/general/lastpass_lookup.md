---
collection: ansible
version: "6"
title: "community.general.lastpass lookup – fetch data from LastPass"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/lastpass_lookup.html
fetched_at: 2026-07-27T17:15:06+00:00
---
# community.general.lastpass lookup – fetch data from LastPass

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](lastpass_lookup.md#ansible-collections-community-general-lastpass-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.lastpass`.

- [Synopsis](lastpass_lookup.md#synopsis)
- [Requirements](lastpass_lookup.md#requirements)
- [Terms](lastpass_lookup.md#terms)
- [Keyword parameters](lastpass_lookup.md#keyword-parameters)
- [Notes](lastpass_lookup.md#notes)
- [Examples](lastpass_lookup.md#examples)
- [Return Value](lastpass_lookup.md#return-value)

## [Synopsis](lastpass_lookup.md#id1)

- Use the lpass command line utility to fetch specific fields from LastPass.

## [Requirements](lastpass_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- lpass (command line utility)
- must have already logged into LastPass

## [Terms](lastpass_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | Key from which you want to retrieve the field. |

## [Keyword parameters](lastpass_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.lastpass', key1=value1, key2=value2, ...)` and `query('community.general.lastpass', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **field**  string | Field to return from LastPass.  Default: `"password"` |

## [Notes](lastpass_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.lastpass', term1, term2, key1=value1, key2=value2)` and `query('community.general.lastpass', term1, term2, key1=value1, key2=value2)`

## [Examples](lastpass_lookup.md#id6)

```yaml+jinja
- name: get 'custom_field' from LastPass entry 'entry-name'
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.lastpass', 'entry-name', field='custom_field') }}"
```

## [Return Value](lastpass_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | secrets stored  Returned: success |

### Authors

- Andrew Zenk

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
