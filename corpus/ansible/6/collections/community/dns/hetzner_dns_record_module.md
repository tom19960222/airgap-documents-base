---
collection: ansible
version: "6"
title: "community.dns.hetzner_dns_record module – Add or delete a single record in Hetzner DNS service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/dns/hetzner_dns_record_module.html
fetched_at: 2026-07-27T17:07:03+00:00
---
# community.dns.hetzner_dns_record module – Add or delete a single record in Hetzner DNS service

> **Note:**
>
> This module is part of the [community.dns collection](https://galaxy.ansible.com/community/dns) (version 2.4.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.dns`.
>
> To use it in a playbook, specify: `community.dns.hetzner_dns_record`.

New in community.dns 2.0.0

- [Synopsis](hetzner_dns_record_module.md#synopsis)
- [Parameters](hetzner_dns_record_module.md#parameters)
- [Attributes](hetzner_dns_record_module.md#attributes)
- [Examples](hetzner_dns_record_module.md#examples)
- [Return Values](hetzner_dns_record_module.md#return-values)

## [Synopsis](hetzner_dns_record_module.md#id1)

- Creates and deletes single DNS records in Hetzner DNS service.
- If you do not want to add/remove values, but replace values, you will be interested in modifying a **record set** and not a single record. This is in particular important when working with `CNAME` and `SOA` records. Use the [community.dns.hetzner_dns_record_set](hetzner_dns_record_set_module.md#ansible-collections-community-dns-hetzner-dns-record-set-module) module for working with record sets.
- Records are matched by prefix / record name and value.

## [Parameters](hetzner_dns_record_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hetzner_token**  aliases: api_token  string / required | The token for the Hetzner API.  If not provided, will be read from the environment variable `HETZNER_DNS_TOKEN`. |
| **prefix**  aliases: name  string | The prefix of the DNS record.  This is the part of *record* before *zone_name*. For example, if the record to be modified is `www.example.com` for the zone `example.com`, the prefix is `www`. If the record in this example would be `example.com`, the prefix would be `''` (empty string).  Exactly one of *record* and *prefix* must be specified. |
| **record**  string | The full DNS record to create or delete.  Exactly one of *record* and *prefix* must be specified. |
| **state**  string / required | Specifies the state of the resource record.  Choices:   - `"present"` - `"absent"` |
| **ttl**  integer | The TTL to give the new record, in seconds.  This is not used for record deletion. |
| **txt_transformation**  string | Determines how TXT entry values are converted between the API and this module’s input and output.  The value `api` means that values are returned from this module as they are returned from the API, and pushed to the API as they have been passed to this module. For idempotency checks, the input string will be compared to the strings returned by the API. The API might automatically transform some values, like splitting long values or adding quotes, which can cause problems with idempotency.  The value `unquoted` automatically transforms values so that you can pass in unquoted values, and the module will return unquoted values. If you pass in quoted values, they will be double-quoted.  The value `quoted` automatically transforms values so that you must use quoting for values that contain spaces, characters such as quotation marks and backslashes, and that are longer than 255 bytes. It also makes sure to return values from the API in a normalized encoding.  The default value, `unquoted`, ensures that you can work with values without having to care about how to correctly quote for DNS. Most users should use one of `unquoted` or `quoted`, but not `api`.  **Note:** the conversion code assumes UTF-8 encoding for values. If you need another encoding use *txt_transformation=api* and handle the encoding yourself.  Choices:   - `"api"` - `"quoted"` - `"unquoted"` ← (default) |
| **type**  string / required | The type of DNS record to create or delete.  Choices:   - `"A"` - `"AAAA"` - `"CAA"` - `"CNAME"` - `"DANE"` - `"DS"` - `"HINFO"` - `"MX"` - `"NS"` - `"RP"` - `"SOA"` - `"SRV"` - `"TLSA"` - `"TXT"` |
| **value**  string / required | The new value when creating a DNS record.  When deleting a record all values for the record must be specified or it will not be deleted. |
| **zone_id**  string | The ID of the DNS zone to modify.  Exactly one of *zone_name* and *zone_id* must be specified. |
| **zone_name**  aliases: zone  string | The DNS zone to modify.  Exactly one of *zone_name* and *zone_id* must be specified. |

## [Attributes](hetzner_dns_record_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.dns.hetzner  added in community.dns 2.4.0 | Use `group/community.dns.hetzner` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](hetzner_dns_record_module.md#id4)

```yaml+jinja
- name: Add a new.foo.com A record
  community.dns.hetzner_dns_record:
    state: present
    zone: foo.com
    record: new.foo.com
    type: A
    ttl: 7200
    value: 1.1.1.1
    hetzner_token: access_token

- name: Remove a new.foo.com A record
  community.dns.hetzner_dns_record:
    state: absent
    zone_name: foo.com
    record: new.foo.com
    type: A
    ttl: 7200
    value: 2.2.2.2
    hetzner_token: access_token
```

## [Return Values](hetzner_dns_record_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **zone_id**  string | The ID of the zone.  Returned: success  Sample: `"23"` |

### Authors

- Markus Bergholz (@markuman)
- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.dns)
[Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-dns)
