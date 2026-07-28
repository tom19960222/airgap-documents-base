---
collection: ansible
version: "8"
title: "community.dns.lookup lookup – Look up DNS records"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/lookup_lookup.html
fetched_at: 2026-07-28T01:43:38+00:00
---
# community.dns.lookup lookup – Look up DNS records

> **Note:**
>
> This lookup plugin is part of the [community.dns collection](https://galaxy.ansible.com/ui/repo/published/community/dns/) (version 2.6.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.dns`.
> You need further requirements to be able to use this lookup plugin,
> see [Requirements](lookup_lookup.md#ansible-collections-community-dns-lookup-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.dns.lookup`.

New in community.dns 2.6.0

- [Synopsis](lookup_lookup.md#synopsis)
- [Requirements](lookup_lookup.md#requirements)
- [Terms](lookup_lookup.md#terms)
- [Keyword parameters](lookup_lookup.md#keyword-parameters)
- [Notes](lookup_lookup.md#notes)
- [Examples](lookup_lookup.md#examples)
- [Return Value](lookup_lookup.md#return-value)

## [Synopsis](lookup_lookup.md#id1)

- Look up DNS records.

## [Requirements](lookup_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- dnspython >= 1.15.0 (maybe older versions also work)
- ipaddress (on Python 2.7 when using `server`)

## [Terms](lookup_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | Domain name(s) to query. |

## [Keyword parameters](lookup_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.dns.lookup', key1=value1, key2=value2, ...)` and `query('community.dns.lookup', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **nxdomain_handling**  string | How to handle NXDOMAIN errors. These appear if an unknown domain name is queried.  `empty` (default) returns an empty result for that domain name. This means that for the corresponding domain name, nothing is added to `_result`.  `fail` makes the lookup fail.  `message` adds the string `NXDOMAIN` to `_result`.  **Choices:**   - `"empty"` ← (default) - `"fail"` - `"message"` |
| **query_retry**  integer | Number of retries for DNS query timeouts.  **Default:** `3` |
| **query_timeout**  float | Timeout per DNS query in seconds.  **Default:** `10.0` |
| **server**  list / elements=string | The DNS server(s) to use to look up the result.  By default, the system’s standard resolver is used. |
| **servfail_retries**  integer | How often to retry on SERVFAIL errors.  **Default:** `0` |
| **type**  string | The record type to retrieve.  **Choices:**   - `"A"` ← (default) - `"ALL"` - `"AAAA"` - `"CAA"` - `"CNAME"` - `"DNAME"` - `"DNSKEY"` - `"DS"` - `"HINFO"` - `"LOC"` - `"MX"` - `"NAPTR"` - `"NS"` - `"NSEC"` - `"NSEC3"` - `"NSEC3PARAM"` - `"PTR"` - `"RP"` - `"RRSIG"` - `"SOA"` - `"SPF"` - `"SRV"` - `"SSHFP"` - `"TLSA"` - `"TXT"` |

## [Notes](lookup_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.dns.lookup', term1, term2, key1=value1, key2=value2)` and `query('community.dns.lookup', term1, term2, key1=value1, key2=value2)`
> - Note that when using this lookup plugin with `lookup()`, and the result is a one-element list, Ansible simply returns the one element not as a list. Since this behavior is surprising and can cause problems, it is better to use `query()` instead of `lookup()`. See the examples and also [Forcing lookups to return lists](../../../plugins/lookup.md#query) in the Ansible documentation.

## [Examples](lookup_lookup.md#id6)

```yaml+jinja
- name: Look up A (IPv4) records for example.org
  ansible.builtin.debug:
    msg: "{{ query('community.dns.lookup', 'example.org.') }}"

- name: Look up AAAA (IPv6) records for example.org
  ansible.builtin.debug:
    msg: "{{ query('community.dns.lookup', 'example.org.', type='AAAA' ) }}"
```

## [Return Value](lookup_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=string | The records of type `type` for all queried DNS names.  If multiple DNS names are queried in `_terms`, the resulting lists have been concatenated.  **Returned:** success  **Sample:** `["127.0.0.1"]` |

### Authors

- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.dns)
- [Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-dns)
