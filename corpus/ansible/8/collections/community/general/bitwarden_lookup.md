---
collection: ansible
version: "8"
title: "community.general.bitwarden lookup – Retrieve secrets from Bitwarden"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/bitwarden_lookup.html
fetched_at: 2026-07-28T01:52:40+00:00
---
# community.general.bitwarden lookup – Retrieve secrets from Bitwarden

> **Note:**
>
> This lookup plugin is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](bitwarden_lookup.md#ansible-collections-community-general-bitwarden-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.bitwarden`.

New in community.general 5.4.0

- [Synopsis](bitwarden_lookup.md#synopsis)
- [Requirements](bitwarden_lookup.md#requirements)
- [Terms](bitwarden_lookup.md#terms)
- [Keyword parameters](bitwarden_lookup.md#keyword-parameters)
- [Notes](bitwarden_lookup.md#notes)
- [Examples](bitwarden_lookup.md#examples)
- [Return Value](bitwarden_lookup.md#return-value)

## [Synopsis](bitwarden_lookup.md#id1)

- Retrieve secrets from Bitwarden.

## [Requirements](bitwarden_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- bw (command line utility)
- be logged into bitwarden
- bitwarden vault unlocked
- `BW_SESSION` environment variable set

## [Terms](bitwarden_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | Key(s) to fetch values for from login info. |

## [Keyword parameters](bitwarden_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.bitwarden', key1=value1, key2=value2, ...)` and `query('community.general.bitwarden', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **collection_id**  string  *added in community.general 6.3.0* | Collection ID to filter results by collection. Leave unset to skip filtering. |
| **field**  string | Field to fetch. Leave unset to fetch whole response. |
| **search**  string  *added in community.general 5.7.0* | Field to retrieve, for example `name` or `id`.  **Default:** `"name"` |

## [Notes](bitwarden_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.bitwarden', term1, term2, key1=value1, key2=value2)` and `query('community.general.bitwarden', term1, term2, key1=value1, key2=value2)`

## [Examples](bitwarden_lookup.md#id6)

```yaml+jinja
- name: "Get 'password' from Bitwarden record named 'a_test'"
  ansible.builtin.debug:
    msg: >-
      {{ lookup('community.general.bitwarden', 'a_test', field='password') }}

- name: "Get 'password' from Bitwarden record with id 'bafba515-af11-47e6-abe3-af1200cd18b2'"
  ansible.builtin.debug:
    msg: >-
      {{ lookup('community.general.bitwarden', 'bafba515-af11-47e6-abe3-af1200cd18b2', search='id', field='password') }}

- name: "Get 'password' from Bitwarden record named 'a_test' from collection"
  ansible.builtin.debug:
    msg: >-
      {{ lookup('community.general.bitwarden', 'a_test', field='password', collection_id='bafba515-af11-47e6-abe3-af1200cd18b2') }}

- name: "Get full Bitwarden record named 'a_test'"
  ansible.builtin.debug:
    msg: >-
      {{ lookup('community.general.bitwarden', 'a_test') }}

- name: "Get custom field 'api_key' from Bitwarden record named 'a_test'"
  ansible.builtin.debug:
    msg: >-
      {{ lookup('community.general.bitwarden', 'a_test', field='api_key') }}
```

## [Return Value](bitwarden_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=any | List of requested field or JSON object of list of matches.  **Returned:** success |

### Authors

- Jonathan Lung (@lungj)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
