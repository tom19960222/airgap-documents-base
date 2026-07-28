---
collection: ansible
version: "8"
title: "community.dns.nameserver_record_info module – Look up all records of a type from all nameservers for a DNS name"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/nameserver_record_info_module.html
fetched_at: 2026-07-28T01:43:32+00:00
---
# community.dns.nameserver_record_info module – Look up all records of a type from all nameservers for a DNS name

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
> see [Requirements](nameserver_record_info_module.md#ansible-collections-community-dns-nameserver-record-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.dns.nameserver_record_info`.

New in community.dns 2.6.0

- [Synopsis](nameserver_record_info_module.md#synopsis)
- [Requirements](nameserver_record_info_module.md#requirements)
- [Parameters](nameserver_record_info_module.md#parameters)
- [Attributes](nameserver_record_info_module.md#attributes)
- [Notes](nameserver_record_info_module.md#notes)
- [Examples](nameserver_record_info_module.md#examples)
- [Return Values](nameserver_record_info_module.md#return-values)

## [Synopsis](nameserver_record_info_module.md#id1)

- Given a DNS name and a record type, will retrieve all nameservers that are responsible for this DNS name, and from them all records for this name of the given type.

## [Requirements](nameserver_record_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnspython >= 1.15.0 (maybe older versions also work)

## [Parameters](nameserver_record_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **always_ask_default_resolver**  boolean | When set to `true` (default), will use the default resolver to find the authoritative nameservers of a subzone.  When set to `false`, will use the authoritative nameservers of the parent zone to find the authoritative nameservers of a subzone. This only makes sense when the nameservers were recently changed and have not yet propagated.  **Choices:**   - `false` - `true` ← (default) |
| **name**  list / elements=string / required | A list of DNS names whose nameservers to retrieve. |
| **query_retry**  integer | Number of retries for DNS query timeouts.  **Default:** `3` |
| **query_timeout**  float | Timeout per DNS query in seconds.  **Default:** `10.0` |
| **servfail_retries**  integer | How often to retry on SERVFAIL errors.  **Default:** `0` |
| **type**  string / required | The record type to retrieve.  **Choices:**   - `"A"` - `"ALL"` - `"AAAA"` - `"CAA"` - `"CNAME"` - `"DNAME"` - `"DNSKEY"` - `"DS"` - `"HINFO"` - `"LOC"` - `"MX"` - `"NAPTR"` - `"NS"` - `"NSEC"` - `"NSEC3"` - `"NSEC3PARAM"` - `"PTR"` - `"RP"` - `"RRSIG"` - `"SOA"` - `"SPF"` - `"SRV"` - `"SSHFP"` - `"TLSA"` - `"TXT"` |

## [Attributes](nameserver_record_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](nameserver_record_info_module.md#id5)

> **Note:**
>
> - dnspython before 2.0.0 does not correctly support (un-)escaping UTF-8 in TXT-like records. This can result in wrongly decoded TXT records. Please use dnspython 2.0.0 or later to fix this issue; see also <https://github.com/rthalley/dnspython/issues/321>. Unfortunately dnspython 2.0.0 requires Python 3.6 or newer.

## [Examples](nameserver_record_info_module.md#id6)

```yaml+jinja
- name: Retrieve TXT values from all nameservers for two DNS names
  community.dns.nameserver_record_info:
    name:
      - www.example.com
      - example.org
    type: TXT
  register: result

- name: Show TXT values for www.example.com for all nameservers
  ansible.builtin.debug:
    msg: '{{ result.results[0].result }}'
```

## [Return Values](nameserver_record_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **results**  list / elements=dictionary | Information on the records for every DNS name provided in `name`.  **Returned:** always  **Sample:** `[{"name": "www.example.com", "result": [{"nameserver": "ns1.example.com", "values": [{"address": "127.0.0.1"}]}, {"nameserver": "ns2.example.com", "values": [{"address": "127.0.0.1"}]}]}, {"name": "example.org", "result": [{"nameserver": "ns1.example.org", "values": [{"address": "127.0.0.1"}, {"address": "127.0.0.2"}]}, {"nameserver": "ns2.example.org", "values": [{"address": "127.0.0.2"}]}, {"nameserver": "ns3.example.org", "values": [{"address": "127.0.0.1"}]}]}]` |
| **name**  string | The DNS name this entry is for.  **Returned:** always  **Sample:** `"www.example.com"` |
| **result**  list / elements=dictionary | A list of values per nameserver.  **Returned:** success  **Sample:** `[{"nameserver": "ns1.example.com", "values": ["X"]}, {"nameserver": "ns2.example.com", "values": ["X"]}]` |
| **nameserver**  string | The nameserver.  **Returned:** success  **Sample:** `"ns1.example.com"` |
| **values**  list / elements=dictionary | The records of type `type`.  Depending on `type`, different fields are returned.  For `type=TXT` and `type=SPF`, also the concatenated value is returned as `results[].result[].values[].value`.  **Returned:** success  **Sample:** `[{"address": "127.0.0.1"}]` |
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
| **strings**  list / elements=string | List of strings for this record.  See `results[].result[].values[].value` for the concatenated result.  **Returned:** if `type=SPF` or `type=TXT` |
| **tag**  string | The tag.  **Returned:** if `type=CAA` |
| **target**  string | The target.  **Returned:** if `type=CNAME` or `type=DNAME` or `type=NS` or `type=PTR` or `type=SRV` |
| **txt**  string | The TXT value.  **Returned:** if `type=RP` |
| **type_covered**  string | The type covered.  **Returned:** if `type=RRSIG` |
| **usage**  integer | The usage flag.  **Returned:** if `type=TLSA` |
| **value**  string | The value.  For `type=SPF` or `type=TXT`, this is the concatenation of `results[].result[].values[].strings`.  **Returned:** if `type=CAA` or `type=SPF` or `type=TXT` |
| **vertical_precision**  float | The vertical precision of the location.  **Returned:** if `type=LOC` |
| **weight**  integer | The service’s weight.  **Returned:** if `type=SRV` |
| **windows**  string | The windows.  **Returned:** if `type=NSEC` or `type=NSEC3` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.dns)
- [Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-dns)
