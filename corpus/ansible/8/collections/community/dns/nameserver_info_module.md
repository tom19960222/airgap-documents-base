---
collection: ansible
version: "8"
title: "community.dns.nameserver_info module – Look up nameservers for a DNS name"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/nameserver_info_module.html
fetched_at: 2026-07-28T01:43:32+00:00
---
# community.dns.nameserver_info module – Look up nameservers for a DNS name

> **Note:**
>
> This module is part of the [community.dns collection](https://galaxy.ansible.com/ui/repo/published/community/dns/) (version 2.6.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.dns`.
> You need further requirements to be able to use this module,
> see [Requirements](nameserver_info_module.md#ansible-collections-community-dns-nameserver-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.dns.nameserver_info`.

New in community.dns 2.6.0

- [Synopsis](nameserver_info_module.md#synopsis)
- [Requirements](nameserver_info_module.md#requirements)
- [Parameters](nameserver_info_module.md#parameters)
- [Attributes](nameserver_info_module.md#attributes)
- [Examples](nameserver_info_module.md#examples)
- [Return Values](nameserver_info_module.md#return-values)

## [Synopsis](nameserver_info_module.md#id1)

- Retrieve all nameservers that are responsible for a DNS name.

## [Requirements](nameserver_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnspython >= 1.15.0 (maybe older versions also work)

## [Parameters](nameserver_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **always_ask_default_resolver**  boolean | When set to `true` (default), will use the default resolver to find the authoritative nameservers of a subzone.  When set to `false`, will use the authoritative nameservers of the parent zone to find the authoritative nameservers of a subzone. This only makes sense when the nameservers were recently changed and have not yet propagated.  **Choices:**   - `false` - `true` ← (default) |
| **name**  list / elements=string / required | A list of DNS names whose nameservers to retrieve. |
| **query_retry**  integer | Number of retries for DNS query timeouts.  **Default:** `3` |
| **query_timeout**  float | Timeout per DNS query in seconds.  **Default:** `10.0` |
| **resolve_addresses**  boolean | Whether to resolve the nameserver names to IP addresses.  **Choices:**   - `false` ← (default) - `true` |
| **servfail_retries**  integer | How often to retry on SERVFAIL errors.  **Default:** `0` |

## [Attributes](nameserver_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](nameserver_info_module.md#id5)

```yaml+jinja
- name: Retrieve name servers of two DNS names
  community.dns.nameserver_info:
    name:
      - www.example.com
      - example.org
  register: result

- name: Show nameservers for www.example.com
  ansible.builtin.debug:
    msg: '{{ result.results[0].nameserver }}'
```

## [Return Values](nameserver_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **results**  list / elements=dictionary | Information on the nameservers for every DNS name provided in `name`.  **Returned:** always  **Sample:** `[{"name": "www.example.com", "nameservers": ["ns1.example.com", "ns2.example.com"]}, {"name": "example.org", "nameservers": ["ns1.example.org", "ns2.example.org", "ns3.example.org"]}]` |
| **name**  string | The DNS name this entry is for.  **Returned:** always  **Sample:** `"www.example.com"` |
| **nameservers**  list / elements=string | A list of nameservers for this DNS name.  **Returned:** success  **Sample:** `["ns1.example.com", "ns2.example.com"]` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.dns)
- [Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-dns)
