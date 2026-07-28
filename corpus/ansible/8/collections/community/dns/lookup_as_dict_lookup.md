---
collection: ansible
version: "8"
title: "community.dns.lookup_as_dict lookup – Look up DNS records as dictionaries"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/lookup_as_dict_lookup.html
fetched_at: 2026-07-28T01:43:39+00:00
---
# community.dns.lookup_as_dict lookup – Look up DNS records as dictionaries

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
> see [Requirements](lookup_as_dict_lookup.md#ansible-collections-community-dns-lookup-as-dict-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.dns.lookup_as_dict`.

New in community.dns 2.6.0

- [Synopsis](lookup_as_dict_lookup.md#synopsis)
- [Requirements](lookup_as_dict_lookup.md#requirements)
- [Terms](lookup_as_dict_lookup.md#terms)
- [Keyword parameters](lookup_as_dict_lookup.md#keyword-parameters)
- [Notes](lookup_as_dict_lookup.md#notes)
- [Examples](lookup_as_dict_lookup.md#examples)
- [Return Value](lookup_as_dict_lookup.md#return-value)

## [Synopsis](lookup_as_dict_lookup.md#id1)

- Look up DNS records and return them as interpreted dictionaries.

## [Requirements](lookup_as_dict_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- dnspython >= 1.15.0 (maybe older versions also work)
- ipaddress (on Python 2.7 when using `server`)

## [Terms](lookup_as_dict_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  list / elements=string / required | Domain name(s) to query. |

## [Keyword parameters](lookup_as_dict_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.dns.lookup_as_dict', key1=value1, key2=value2, ...)` and `query('community.dns.lookup_as_dict', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **nxdomain_handling**  string | How to handle NXDOMAIN errors. These appear if an unknown domain name is queried.  `empty` (default) returns an empty result for that domain name. This means that for the corresponding domain name, nothing is added to `_result`.  `fail` makes the lookup fail.  **Choices:**   - `"empty"` ← (default) - `"fail"` |
| **query_retry**  integer | Number of retries for DNS query timeouts.  **Default:** `3` |
| **query_timeout**  float | Timeout per DNS query in seconds.  **Default:** `10.0` |
| **server**  list / elements=string | The DNS server(s) to use to look up the result.  By default, the system’s standard resolver is used. |
| **servfail_retries**  integer | How often to retry on SERVFAIL errors.  **Default:** `0` |
| **type**  string | The record type to retrieve.  **Choices:**   - `"A"` ← (default) - `"ALL"` - `"AAAA"` - `"CAA"` - `"CNAME"` - `"DNAME"` - `"DNSKEY"` - `"DS"` - `"HINFO"` - `"LOC"` - `"MX"` - `"NAPTR"` - `"NS"` - `"NSEC"` - `"NSEC3"` - `"NSEC3PARAM"` - `"PTR"` - `"RP"` - `"RRSIG"` - `"SOA"` - `"SPF"` - `"SRV"` - `"SSHFP"` - `"TLSA"` - `"TXT"` |

## [Notes](lookup_as_dict_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.dns.lookup_as_dict', term1, term2, key1=value1, key2=value2)` and `query('community.dns.lookup_as_dict', term1, term2, key1=value1, key2=value2)`
> - Note that when using this lookup plugin with `lookup()`, and the result is a one-element list, Ansible simply returns the one element not as a list. Since this behavior is surprising and can cause problems, it is better to use `query()` instead of `lookup()`. See the examples and also [Forcing lookups to return lists](../../../plugins/lookup.md#query) in the Ansible documentation.

## [Examples](lookup_as_dict_lookup.md#id6)

```yaml+jinja
- name: Look up A (IPv4) records for example.org as a list of dictionaries
  ansible.builtin.debug:
    msg: "{{ query('community.dns.lookup_as_dict', 'example.org.') }}"

- name: Look up AAAA (IPv6) records for example.org as a list of IPv6 addresses
  ansible.builtin.debug:
    msg: "{{ query('community.dns.lookup_as_dict', 'example.org.', type='AAAA' ) | map(attribute='address') }}"

- name: Look up TXT records for ansible.com as a list of strings
  ansible.builtin.debug:
    msg: "{{ query('community.dns.lookup_as_dict', 'ansible.com.', type='TXT' ) | map(attribute='value') }}"
```

## [Return Value](lookup_as_dict_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=dictionary | The records of type `type` for all queried DNS names.  If multiple DNS names are queried in `_terms`, the resulting lists have been concatenated.  Depending on `type`, different fields are returned.  For `type=TXT` and `type=SPF`, also the concatenated value is returned as `_result[].value`.  **Returned:** success  **Sample:** `[{"address": "127.0.0.1"}]` |
| **address**  string | A IPv4 respectively IPv6 address.  **Returned:** if `type=A` or `type=AAAA` |
| **algorithm**  integer | The algorithm ID.  **Returned:** if `type=DNSKEY` or `type=DS` or `type=NSEC3` or `type=NSEC3PARAM` or `type=RRSIG` or `type=SSHFP` |
| **altitude**  float | The altitude.  **Returned:** if `type=LOC` |
| **cert**  string | The certificate.  **Returned:** if `type=TLSA` |
| **cpu**  string | The CPU.  **Returned:** if `type=HINFO` |
| **digest**  string | The digest.  **Returned:** if `type=DS` |
| **digest_type**  integer | The digest’s type.  **Returned:** if `type=DS` |
| **exchange**  string | The exchange server.  **Returned:** if `type=MX` |
| **expiration**  integer | The expiration Unix timestamp.  **Returned:** if `type=RRSIG` |
| **expire**  integer | Number of seconds after which secondary name servers should stop answering request for this zone if the main name server does not respond.  **Returned:** if `type=SOA` |
| **fingerprint**  string | The fingerprint.  **Returned:** if `type=SSHFP` |
| **flags**  integer | Flags.  This is actually of type `string` for `type=NAPTR`.  **Returned:** if `type=CAA` or `type=DNSKEY` or `type=NAPTR` or `type=NSEC3` or `type=NSEC3PARAM` |
| **fp_type**  integer | The fingerprint’s type.  **Returned:** if `type=SSHFP` |
| **horizontal_precision**  float | The horizontal precision of the location.  **Returned:** if `type=LOC` |
| **inception**  integer | The inception Unix timestamp.  **Returned:** if `type=RRSIG` |
| **iterations**  integer | The number of iterations.  **Returned:** if `type=NSEC3` or `type=NSEC3PARAM` |
| **key**  string | The key.  **Returned:** if `type=DNSKEY` |
| **key_tag**  integer | The key’s tag.  **Returned:** if `type=DS` or `type=RRSIG` |
| **labels**  integer | The labels.  **Returned:** if `type=RRSIG` |
| **latitude**  list / elements=integer | The location’s latitude.  **Returned:** if `type=LOC` |
| **longitude**  list / elements=integer | The location’s longitude.  **Returned:** if `type=LOC` |
| **mbox**  string | The mbox.  **Returned:** if `type=RP` |
| **minimum**  integer | Used to calculate the TTL for purposes of negative caching.  **Returned:** if `type=SOA` |
| **mname**  string | Primary main name server for this zone.  **Returned:** if `type=SOA` |
| **mtype**  integer | The mtype.  **Returned:** if `type=TLSA` |
| **next**  string | The next value.  **Returned:** if `type=NSEC` or `type=NSEC3` |
| **order**  integer | The order value.  **Returned:** if `type=NAPTR` |
| **original_ttl**  integer | The original TTL.  **Returned:** if `type=RRSIG` |
| **os**  string | The operating system.  **Returned:** if `type=HINFO` |
| **port**  integer | The port.  **Returned:** if `type=SRV` |
| **preference**  integer | The preference value for this record.  **Returned:** if `type=MX` or `type=NAPTR` |
| **priority**  integer | The priority value for this record.  **Returned:** if `type=SRV` |
| **protocol**  integer | The protocol.  **Returned:** if `type=DNSKEY` |
| **refresh**  integer | Number of seconds after which secondary name servers should query the main name server for the SOA record to detect zone changes.  **Returned:** if `type=SOA` |
| **regexp**  string | A regular expression.  **Returned:** if `type=NAPTR` |
| **replacement**  string | The replacement.  **Returned:** if `type=NAPTR` |
| **retry**  integer | Number of seconds after which secondary name servers should retry to request the serial number from the main name server if the main name server does not respond.  **Returned:** if `type=SOA` |
| **rname**  string | E-mail address of the administrator responsible for this zone.  **Returned:** if `type=SOA` |
| **salt**  string | The salt.  **Returned:** if `type=NSEC3` or `type=NSEC3PARAM` |
| **selector**  integer | The selector.  **Returned:** if `type=TLSA` |
| **serial**  integer | Serial number for this zone.  **Returned:** if `type=SOA` |
| **service**  string | The service.  **Returned:** if `type=NAPTR` |
| **signature**  string | The signature.  **Returned:** if `type=RRSIG` |
| **signer**  string | The signer.  **Returned:** if `type=RRSIG` |
| **size**  float | The size of the location.  **Returned:** if `type=LOC` |
| **strings**  list / elements=string | List of strings for this record.  See `_result[].value` for the concatenated result.  **Returned:** if `type=SPF` or `type=TXT` |
| **tag**  string | The tag.  **Returned:** if `type=CAA` |
| **target**  string | The target.  **Returned:** if `type=CNAME` or `type=DNAME` or `type=NS` or `type=PTR` or `type=SRV` |
| **txt**  string | The TXT value.  **Returned:** if `type=RP` |
| **type_covered**  string | The type covered.  **Returned:** if `type=RRSIG` |
| **usage**  integer | The usage flag.  **Returned:** if `type=TLSA` |
| **value**  string | The value.  For `type=SPF` or `type=TXT`, this is the concatenation of `_result[].strings`.  **Returned:** if `type=CAA` or `type=SPF` or `type=TXT` |
| **vertical_precision**  float | The vertical precision of the location.  **Returned:** if `type=LOC` |
| **weight**  integer | The service’s weight.  **Returned:** if `type=SRV` |
| **windows**  string | The windows.  **Returned:** if `type=NSEC` or `type=NSEC3` |

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
