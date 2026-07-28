---
collection: ansible
version: "8"
title: "community.general.dnstxt lookup – query a domain(s)’s DNS txt fields"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/dnstxt_lookup.html
fetched_at: 2026-07-28T01:52:47+00:00
---
# community.general.dnstxt lookup – query a domain(s)’s DNS txt fields

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
> see [Requirements](dnstxt_lookup.md#ansible-collections-community-general-dnstxt-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.dnstxt`.

- [Synopsis](dnstxt_lookup.md#synopsis)
- [Requirements](dnstxt_lookup.md#requirements)
- [Terms](dnstxt_lookup.md#terms)
- [Keyword parameters](dnstxt_lookup.md#keyword-parameters)
- [Notes](dnstxt_lookup.md#notes)
- [Examples](dnstxt_lookup.md#examples)
- [Return Value](dnstxt_lookup.md#return-value)

## [Synopsis](dnstxt_lookup.md#id1)

- Uses a python library to return the DNS TXT record for a domain.

## [Requirements](dnstxt_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- dns/dns.resolver (python library)

## [Terms](dnstxt_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | domain or list of domains to query TXT records from |

## [Keyword parameters](dnstxt_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.dnstxt', key1=value1, key2=value2, ...)` and `query('community.general.dnstxt', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **real_empty**  boolean  *added in community.general 6.0.0* | Return empty result without empty strings, and return empty list instead of `NXDOMAIN`.  The default for this option will likely change to `true` in the future.  **Choices:**   - `false` ← (default) - `true` |

## [Notes](dnstxt_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.dnstxt', term1, term2, key1=value1, key2=value2)` and `query('community.general.dnstxt', term1, term2, key1=value1, key2=value2)`

## [Examples](dnstxt_lookup.md#id6)

```yaml+jinja
- name: show txt entry
  ansible.builtin.debug:
    msg: "{{lookup('community.general.dnstxt', ['test.example.com'])}}"

- name: iterate over txt entries
  ansible.builtin.debug:
    msg: "{{item}}"
  with_community.general.dnstxt:
    - 'test.example.com'
    - 'other.example.com'
    - 'last.example.com'

- name: iterate of a comma delimited DNS TXT entry
  ansible.builtin.debug:
    msg: "{{item}}"
  with_community.general.dnstxt: "{{lookup('community.general.dnstxt', ['test.example.com']).split(',')}}"
```

## [Return Value](dnstxt_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | values returned by the DNS TXT record.  **Returned:** success |

### Authors

- Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
