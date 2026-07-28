---
collection: ansible
version: "8"
title: "community.general.hiera lookup – get info from hiera data"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/hiera_lookup.html
fetched_at: 2026-07-28T01:52:51+00:00
---
# community.general.hiera lookup – get info from hiera data

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
> see [Requirements](hiera_lookup.md#ansible-collections-community-general-hiera-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.hiera`.

- [Synopsis](hiera_lookup.md#synopsis)
- [Requirements](hiera_lookup.md#requirements)
- [Terms](hiera_lookup.md#terms)
- [Keyword parameters](hiera_lookup.md#keyword-parameters)
- [Notes](hiera_lookup.md#notes)
- [Examples](hiera_lookup.md#examples)
- [Return Value](hiera_lookup.md#return-value)

## [Synopsis](hiera_lookup.md#id1)

- Retrieves data from an Puppetmaster node using Hiera as ENC.

## [Requirements](hiera_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- hiera (command line utility)

## [Terms](hiera_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | The list of keys to lookup on the Puppetmaster. |

## [Keyword parameters](hiera_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.hiera', key1=value1, key2=value2, ...)` and `query('community.general.hiera', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **config_file**  string | File that describes the hierarchy of Hiera.  **Default:** `"/etc/hiera.yaml"`  **Configuration:**   - Environment variable: [`ANSIBLE_HIERA_CFG`](../../environment_variables.md#envvar-ANSIBLE_HIERA_CFG) |
| **executable**  string | Binary file to execute Hiera.  **Default:** `"/usr/bin/hiera"`  **Configuration:**   - Environment variable: [`ANSIBLE_HIERA_BIN`](../../environment_variables.md#envvar-ANSIBLE_HIERA_BIN) |

## [Notes](hiera_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.hiera', term1, term2, key1=value1, key2=value2)` and `query('community.general.hiera', term1, term2, key1=value1, key2=value2)`

## [Examples](hiera_lookup.md#id6)

```yaml+jinja
# All this examples depends on hiera.yml that describes the hierarchy

- name: "a value from Hiera 'DB'"
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.hiera', 'foo') }}"

- name: "a value from a Hiera 'DB' on other environment"
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.hiera', 'foo environment=production') }}"

- name: "a value from a Hiera 'DB' for a concrete node"
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.hiera', 'foo fqdn=puppet01.localdomain') }}"
```

## [Return Value](hiera_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | a value associated with input key  **Returned:** success |

### Authors

- Juan Manuel Parrilla (@jparrill)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
