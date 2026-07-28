---
collection: ansible
version: "6"
title: "community.dns.hetzner_dns_record_sets module – Bulk synchronize DNS record sets in Hetzner DNS service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/dns/hetzner_dns_record_sets_module.html
fetched_at: 2026-07-27T17:07:06+00:00
---
# community.dns.hetzner_dns_record_sets module – Bulk synchronize DNS record sets in Hetzner DNS service

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
> To use it in a playbook, specify: `community.dns.hetzner_dns_record_sets`.

New in community.dns 2.0.0

- [Synopsis](hetzner_dns_record_sets_module.md#synopsis)
- [Parameters](hetzner_dns_record_sets_module.md#parameters)
- [Attributes](hetzner_dns_record_sets_module.md#attributes)
- [Examples](hetzner_dns_record_sets_module.md#examples)
- [Return Values](hetzner_dns_record_sets_module.md#return-values)

## [Synopsis](hetzner_dns_record_sets_module.md#id1)

- Bulk synchronize DNS record sets in Hetzner DNS service.
- It is possible to ignore certain record sets by specifying *ignore: true* for that record set.
- The module allows to set, modify and delete multiple DNS record sets at once.
- With the *purge* option, it is also possible to delete existing record sets that are not mentioned in the module parameters. With this, it is possible to synchronize the expected state of a DNS zone with the expected state.

## [Parameters](hetzner_dns_record_sets_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bulk_operation_threshold**  integer | Determines the threshold from when on bulk operations are used.  The default value 2 means that if 2 or more operations of a kind are planned, and the API supports bulk operations for this kind of operation, they will be used.  Default: `2` |
| **hetzner_token**  aliases: api_token  string / required | The token for the Hetzner API.  If not provided, will be read from the environment variable `HETZNER_DNS_TOKEN`. |
| **prune**  boolean | If set to `true`, will remove all existing records in the zone that are not listed in *records*.  Choices:   - `false` ← (default) - `true` |
| **record_sets**  aliases: records  list / elements=dictionary / required | The records that should be present in the zone. |
| **ignore**  boolean | If set to `true`, *value* will be ignored.  This is useful when *prune=true*, but you do not want certain entries to be removed without having to know their current value.  Choices:   - `false` ← (default) - `true` |
| **prefix**  string | The prefix of the DNS record.  This is the part of *record* before *zone_name*. For example, if the record to be modified is `www.example.com` for the zone `example.com`, the prefix is `www`. If the record in this example would be `example.com`, the prefix would be `''` (empty string).  Exactly one of *record* and *prefix* must be specified. |
| **record**  string | The full DNS record to create or delete.  Exactly one of *record* and *prefix* must be specified. |
| **ttl**  integer | The TTL to give the new record, in seconds. |
| **type**  string / required | The type of DNS record to create or delete.  Choices:   - `"A"` - `"AAAA"` - `"CAA"` - `"CNAME"` - `"DANE"` - `"DS"` - `"HINFO"` - `"MX"` - `"NS"` - `"RP"` - `"SOA"` - `"SRV"` - `"TLSA"` - `"TXT"` |
| **value**  list / elements=string | The new value when creating a DNS record.  YAML lists or multiple comma-spaced values are allowed.  When deleting a record all values for the record must be specified or it will not be deleted.  Must be specified if *ignore=false*. |
| **txt_transformation**  string | Determines how TXT entry values are converted between the API and this module’s input and output.  The value `api` means that values are returned from this module as they are returned from the API, and pushed to the API as they have been passed to this module. For idempotency checks, the input string will be compared to the strings returned by the API. The API might automatically transform some values, like splitting long values or adding quotes, which can cause problems with idempotency.  The value `unquoted` automatically transforms values so that you can pass in unquoted values, and the module will return unquoted values. If you pass in quoted values, they will be double-quoted.  The value `quoted` automatically transforms values so that you must use quoting for values that contain spaces, characters such as quotation marks and backslashes, and that are longer than 255 bytes. It also makes sure to return values from the API in a normalized encoding.  The default value, `unquoted`, ensures that you can work with values without having to care about how to correctly quote for DNS. Most users should use one of `unquoted` or `quoted`, but not `api`.  **Note:** the conversion code assumes UTF-8 encoding for values. If you need another encoding use *txt_transformation=api* and handle the encoding yourself.  Choices:   - `"api"` - `"quoted"` - `"unquoted"` ← (default) |
| **zone_id**  string | The ID of the DNS zone to modify.  Exactly one of *zone_name* and *zone_id* must be specified. |
| **zone_name**  aliases: zone  string | The DNS zone to modify.  Exactly one of *zone_name* and *zone_id* must be specified. |

## [Attributes](hetzner_dns_record_sets_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.dns.hetzner  added in community.dns 2.4.0 | Use `group/community.dns.hetzner` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](hetzner_dns_record_sets_module.md#id4)

```yaml+jinja
- name: Make sure some records exist and have the expected values
  community.dns.hetzner_dns_record_sets:
    zone: foo.com
    records:
      - prefix: new
        type: A
        ttl: 7200
        value:
          - 1.1.1.1
          - 2.2.2.2
      - prefix: new
        type: AAAA
        ttl: 7200
        value:
          - "::1"
      - record: foo.com
        type: TXT
        value:
          - test
    hetzner_token: access_token

- name: Synchronize DNS zone with a fixed set of records
  # If a record exists that is not mentioned here, it will be deleted
  community.dns.hetzner_dns_record_sets:
    zone_id: 23
    purge: true
    records:
      - prefix: ''
        type: A
        value: 127.0.0.1
      - prefix: ''
        type: AAAA
        value: "::1"
      - prefix: ''
        type: NS
        value:
          - ns-1.hoster.com
          - ns-2.hoster.com
          - ns-3.hoster.com
    hetzner_token: access_token
```

## [Return Values](hetzner_dns_record_sets_module.md#id5)

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
