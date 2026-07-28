---
collection: ansible
version: "6"
title: "community.general.dig lookup – query DNS using the dnspython library"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/dig_lookup.html
fetched_at: 2026-07-27T17:15:00+00:00
---
# community.general.dig lookup – query DNS using the dnspython library

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
> see [Requirements](dig_lookup.md#ansible-collections-community-general-dig-lookup-requirements) for details.
>
> To use it in a playbook, specify: `community.general.dig`.

- [Synopsis](dig_lookup.md#synopsis)
- [Requirements](dig_lookup.md#requirements)
- [Terms](dig_lookup.md#terms)
- [Keyword parameters](dig_lookup.md#keyword-parameters)
- [Notes](dig_lookup.md#notes)
- [Examples](dig_lookup.md#examples)
- [Return Value](dig_lookup.md#return-value)

## [Synopsis](dig_lookup.md#id1)

- The dig lookup runs queries against DNS servers to retrieve DNS records for a specific name (FQDN - fully qualified domain name). It is possible to lookup any DNS record in this manner.
- There is a couple of different syntaxes that can be used to specify what record should be retrieved, and for which name. It is also possible to explicitly specify the DNS server(s) to use for lookups.
- In its simplest form, the dig lookup plugin can be used to retrieve an IPv4 address (DNS A record) associated with FQDN
- In addition to (default) A record, it is also possible to specify a different record type that should be queried. This can be done by either passing-in additional parameter of format qtype=TYPE to the dig lookup, or by appending /TYPE to the FQDN being queried.
- If multiple values are associated with the requested record, the results will be returned as a comma-separated list. In such cases you may want to pass option wantlist=True to the plugin, which will result in the record values being returned as a list over which you can iterate later on.
- By default, the lookup will rely on system-wide configured DNS servers for performing the query. It is also possible to explicitly specify DNS servers to query using the @DNS_SERVER_1,DNS_SERVER_2,…,DNS_SERVER_N notation. This needs to be passed-in as an additional parameter to the lookup

## [Requirements](dig_lookup.md#id2)

The below requirements are needed on the local controller node that executes this lookup.

- dnspython (python library, <http://www.dnspython.org/>)

## [Terms](dig_lookup.md#id3)

| Parameter | Comments |
| --- | --- |
| **Terms**  string | Domain(s) to query. |

## [Keyword parameters](dig_lookup.md#id4)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('community.general.dig', key1=value1, key2=value2, ...)` and `query('community.general.dig', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **fail_on_error**  boolean  added in community.general 5.4.0 | Abort execution on lookup errors.  The default for this option will likely change to `true` in the future. The current default, `false`, is used for backwards compatibility, and will result in empty strings or the string `NXDOMAIN` in the result in case of errors.  Choices:   - `false` ← (default) - `true` |
| **flat**  string | If 0 each record is returned as a dictionary, otherwise a string.  Default: `1` |
| **qtype**  string | Record type to query.  `DLV` is deprecated and will be removed in community.general 6.0.0.  Choices:   - `"A"` ← (default) - `"ALL"` - `"AAAA"` - `"CNAME"` - `"DNAME"` - `"DLV"` - `"DNSKEY"` - `"DS"` - `"HINFO"` - `"LOC"` - `"MX"` - `"NAPTR"` - `"NS"` - `"NSEC3PARAM"` - `"PTR"` - `"RP"` - `"RRSIG"` - `"SOA"` - `"SPF"` - `"SRV"` - `"SSHFP"` - `"TLSA"` - `"TXT"` |
| **retry_servfail**  boolean  added in community.general 3.6.0 | Retry a nameserver if it returns SERVFAIL.  Choices:   - `false` ← (default) - `true` |

## [Notes](dig_lookup.md#id5)

> **Note:**
>
> - When keyword and positional parameters are used together, positional parameters must be listed before keyword parameters:
>   `lookup('community.general.dig', term1, term2, key1=value1, key2=value2)` and `query('community.general.dig', term1, term2, key1=value1, key2=value2)`
> - ALL is not a record per-se, merely the listed fields are available for any record results you retrieve in the form of a dictionary.
> - While the ‘dig’ lookup plugin supports anything which dnspython supports out of the box, only a subset can be converted into a dictionary.
> - If you need to obtain the AAAA record (IPv6 address), you must specify the record type explicitly. Syntax for specifying the record type is shown in the examples below.
> - The trailing dot in most of the examples listed is purely optional, but is specified for completeness/correctness sake.

## [Examples](dig_lookup.md#id6)

```yaml+jinja
- name: Simple A record (IPV4 address) lookup for example.com
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.dig', 'example.com.')}}"

- name: "The TXT record for example.org."
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.dig', 'example.org.', 'qtype=TXT') }}"

- name: "The TXT record for example.org, alternative syntax."
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.dig', 'example.org./TXT') }}"

- name: use in a loop
  ansible.builtin.debug:
    msg: "MX record for gmail.com {{ item }}"
  with_items: "{{ lookup('community.general.dig', 'gmail.com./MX', wantlist=True) }}"

- ansible.builtin.debug:
    msg: "Reverse DNS for 192.0.2.5 is {{ lookup('community.general.dig', '192.0.2.5/PTR') }}"
- ansible.builtin.debug:
    msg: "Reverse DNS for 192.0.2.5 is {{ lookup('community.general.dig', '5.2.0.192.in-addr.arpa./PTR') }}"
- ansible.builtin.debug:
    msg: "Reverse DNS for 192.0.2.5 is {{ lookup('community.general.dig', '5.2.0.192.in-addr.arpa.', 'qtype=PTR') }}"
- ansible.builtin.debug:
    msg: "Querying 198.51.100.23 for IPv4 address for example.com. produces {{ lookup('dig', 'example.com', '@198.51.100.23') }}"

- ansible.builtin.debug:
    msg: "XMPP service for gmail.com. is available at {{ item.target }} on port {{ item.port }}"
  with_items: "{{ lookup('community.general.dig', '_xmpp-server._tcp.gmail.com./SRV', 'flat=0', wantlist=True) }}"

- name: Retry nameservers that return SERVFAIL
  ansible.builtin.debug:
    msg: "{{ lookup('community.general.dig', 'example.org./A', 'retry_servfail=True') }}"
```

## [Return Value](dig_lookup.md#id7)

| Key | Description |
| --- | --- |
| **Return value**  list / elements=any | List of composed strings or dictionaries with key and value If a dictionary, fields shows the keys returned depending on query type  Returned: success |
| **A**  string | address  Returned: success |
| **AAAA**  string | address  Returned: success |
| **ALL**  string | owner, ttl, type  Returned: success |
| **CNAME**  string | target  Returned: success |
| **DLV**  string | algorithm, digest_type, key_tag, digest  Returned: success |
| **DNAME**  string | target  Returned: success |
| **DNSKEY**  string | flags, algorithm, protocol, key  Returned: success |
| **DS**  string | algorithm, digest_type, key_tag, digest  Returned: success |
| **HINFO**  string | cpu, os  Returned: success |
| **LOC**  string | latitude, longitude, altitude, size, horizontal_precision, vertical_precision  Returned: success |
| **MX**  string | preference, exchange  Returned: success |
| **NAPTR**  string | order, preference, flags, service, regexp, replacement  Returned: success |
| **NS**  string | target  Returned: success |
| **NSEC3PARAM**  string | algorithm, flags, iterations, salt  Returned: success |
| **PTR**  string | target  Returned: success |
| **RP**  string | mbox, txt  Returned: success |
| **SOA**  string | mname, rname, serial, refresh, retry, expire, minimum  Returned: success |
| **SPF**  string | strings  Returned: success |
| **SRV**  string | priority, weight, port, target  Returned: success |
| **SSHFP**  string | algorithm, fp_type, fingerprint  Returned: success |
| **TLSA**  string | usage, selector, mtype, cert  Returned: success |
| **TXT**  string | strings  Returned: success |

### Authors

- Jan-Piet Mens (@jpmens) <jpmens(at)gmail.com>

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
