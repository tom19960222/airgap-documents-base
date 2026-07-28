---
collection: ansible
version: "6"
title: "community.general.lmdb_kv lookup – fetch data from LMDB"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/lmdb_kv_lookup.html
fetched_at: 2026-07-27T17:15:06+00:00
---
# community.general.lmdb_kv lookup – fetch data from LMDB

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
> see [Requirements](lmdb_kv_lookup.md#ansible-collections-community-general-lmdb-kv-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.lmdb_kv`.

New in community.general 0.2.0

- [Synopsis](lmdb_kv_lookup.md#synopsis)
- [Requirements](lmdb_kv_lookup.md#requirements)
- [Terms](lmdb_kv_lookup.md#terms)
- [Keyword parameters](lmdb_kv_lookup.md#keyword-parameters)
- [Notes](lmdb_kv_lookup.md#notes)
- [Examples](lmdb_kv_lookup.md#examples)
- [Return Value](lmdb_kv_lookup.md#return-value)

## [Synopsis](lmdb_kv_lookup.md#id1)

- This lookup returns a list of results from an LMDB DB corresponding to a list of items given to it

## [Requirements](lmdb_kv_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- lmdb (python library <https://lmdb.readthedocs.io/en/release/>)

## [Terms](lmdb_kv_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string | list of keys to query |

## [Keyword parameters](lmdb_kv_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.lmdb_kv', key1=value1, key2=value2, ...)` and `query('community.general.lmdb_kv', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **db**  string | path to LMDB database  Default: `"ansible.mdb"` |

## [Notes](lmdb_kv_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.lmdb_kv', term1, term2, key1=value1, key2=value2)` and `query('community.general.lmdb_kv', term1, term2, key1=value1, key2=value2)`

## [Examples](lmdb_kv_lookup.md#id6)

```yaml+jinja
- name: query LMDB for a list of country codes
  ansible.builtin.debug:
    msg: "{{ query('community.general.lmdb_kv', 'nl', 'be', 'lu', db='jp.mdb') }}"

- name: use list of values in a loop by key wildcard
  ansible.builtin.debug:
    msg: "Hello from {{ item.0 }} a.k.a. {{ item.1 }}"
  vars:
    - lmdb_kv_db: jp.mdb
  with_community.general.lmdb_kv:
     - "n*"

- name: get an item by key
  ansible.builtin.assert:
    that:
      - item == 'Belgium'
    vars:
      - lmdb_kv_db: jp.mdb
    with_community.general.lmdb_kv:
      - be
```

## [Return Value](lmdb_kv_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=any | value(s) stored in LMDB  Returned: success |

### Authors

- Jan-Piet Mens (@jpmens)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
