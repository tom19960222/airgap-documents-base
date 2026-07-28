---
collection: ansible
version: "6"
title: "community.dns.hetzner_dns_record_set_info module – Retrieve record sets in Hetzner DNS service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/dns/hetzner_dns_record_set_info_module.html
fetched_at: 2026-07-27T17:07:05+00:00
---
# community.dns.hetzner_dns_record_set_info module – Retrieve record sets in Hetzner DNS service

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
> To use it in a playbook, specify: `community.dns.hetzner_dns_record_set_info`.

New in community.dns 2.0.0

- [Synopsis](hetzner_dns_record_set_info_module.md#synopsis)
- [Parameters](hetzner_dns_record_set_info_module.md#parameters)
- [Attributes](hetzner_dns_record_set_info_module.md#attributes)
- [Examples](hetzner_dns_record_set_info_module.md#examples)
- [Return Values](hetzner_dns_record_set_info_module.md#return-values)

## [Synopsis](hetzner_dns_record_set_info_module.md#id1)

- Retrieves DNS record sets in Hetzner DNS service.

## [Parameters](hetzner_dns_record_set_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hetzner_token**  aliases: api_token  string / required | The token for the Hetzner API.  If not provided, will be read from the environment variable `HETZNER_DNS_TOKEN`. |
| **prefix**  string  added in community.dns 0.2.0 | The prefix of the DNS record.  This is the part of *record* before *zone_name*. For example, if the record to be modified is `www.example.com` for the zone `example.com`, the prefix is `www`. If the record in this example would be `example.com`, the prefix would be `''` (empty string).  If *what* is `single_record` or `all_types_for_record`, exactly one of *record* and *prefix* is required. |
| **record**  string | The full DNS record to retrieve.  If *what* is `single_record` or `all_types_for_record`, exactly one of *record* and *prefix* is required. |
| **txt_transformation**  string | Determines how TXT entry values are converted between the API and this module’s input and output.  The value `api` means that values are returned from this module as they are returned from the API, and pushed to the API as they have been passed to this module. For idempotency checks, the input string will be compared to the strings returned by the API. The API might automatically transform some values, like splitting long values or adding quotes, which can cause problems with idempotency.  The value `unquoted` automatically transforms values so that you can pass in unquoted values, and the module will return unquoted values. If you pass in quoted values, they will be double-quoted.  The value `quoted` automatically transforms values so that you must use quoting for values that contain spaces, characters such as quotation marks and backslashes, and that are longer than 255 bytes. It also makes sure to return values from the API in a normalized encoding.  The default value, `unquoted`, ensures that you can work with values without having to care about how to correctly quote for DNS. Most users should use one of `unquoted` or `quoted`, but not `api`.  **Note:** the conversion code assumes UTF-8 encoding for values. If you need another encoding use *txt_transformation=api* and handle the encoding yourself.  Choices:   - `"api"` - `"quoted"` - `"unquoted"` ← (default) |
| **type**  string | The type of DNS record to retrieve.  Required if *what* is `single_record`.  Choices:   - `"A"` - `"AAAA"` - `"CAA"` - `"CNAME"` - `"DANE"` - `"DS"` - `"HINFO"` - `"MX"` - `"NS"` - `"RP"` - `"SOA"` - `"SRV"` - `"TLSA"` - `"TXT"` |
| **what**  string | Describes whether to fetch a single record and type combination, all types for a record, or all records. By default, a single record and type combination is fetched.  Note that the return value structure depends on this option.  Choices:   - `"single_record"` ← (default) - `"all_types_for_record"` - `"all_records"` |
| **zone_id**  string  added in community.dns 0.2.0 | The ID of the DNS zone to modify.  Exactly one of *zone_name* and *zone_id* must be specified. |
| **zone_name**  aliases: zone  string | The DNS zone to modify.  Exactly one of *zone* and *zone_id* must be specified. |

## [Attributes](hetzner_dns_record_set_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.dns.hetzner  added in community.dns 2.4.0 | Use `group/community.dns.hetzner` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support:  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](hetzner_dns_record_set_info_module.md#id4)

```yaml+jinja
- name: Retrieve the details for the A records of new.foo.com
  community.dns.hetzner_dns_record_set_info:
    zone: foo.com
    record: new.foo.com
    type: A
    hetzner_token: access_token
  register: rec

- name: Print the A record set
  ansible.builtin.debug:
    msg: "{{ rec.set }}"
```

## [Return Values](hetzner_dns_record_set_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **set**  dictionary | The fetched record set. Is empty if record set does not exist.  Returned: success and *what* is `single_record`  Sample: `{"record": "sample.example.com", "ttl": 3600, "type": "A", "value": ["1.2.3.4", "1.2.3.5"]}` |
| **prefix**  string  added in community.dns 0.2.0 | The record prefix.  Returned: success  Sample: `"sample"` |
| **record**  string | The record name.  Returned: success  Sample: `"sample.example.com"` |
| **ttl**  integer | The TTL.  If there are records in this set with different TTLs, the minimum of the TTLs will be presented here.  Will return `none` if the zone’s default TTL is used.  Returned: success  Sample: `3600` |
| **ttls**  list / elements=integer | If there are records with different TTL values in this set, this will be the list of TTLs appearing in the records.  Every distinct TTL will appear once, and the TTLs are in ascending order.  Returned: When there is more than one distinct TTL  Sample: `[300, 3600]` |
| **type**  string | The DNS record type.  Returned: success  Sample: `"A"` |
| **value**  list / elements=string | The DNS record set’s value.  Returned: success  Sample: `["1.2.3.4", "1.2.3.5"]` |
| **sets**  list / elements=dictionary | The list of fetched record sets.  Returned: success and *what* is not `single_record`  Sample: `[{"record": "sample.example.com", "ttl": 3600, "type": "A", "value": ["1.2.3.4", "1.2.3.5"]}]` |
| **prefix**  string  added in community.dns 0.2.0 | The record prefix.  Returned: success  Sample: `"sample"` |
| **record**  string | The record name.  Returned: success  Sample: `"sample.example.com"` |
| **ttl**  integer | The TTL.  If there are records in this set with different TTLs, the minimum of the TTLs will be presented here.  Will return `none` if the zone’s default TTL is used.  Returned: success  Sample: `3600` |
| **ttls**  list / elements=integer | If there are records with different TTL values in this set, this will be the list of TTLs appearing in the records.  Every distinct TTL will appear once, and the TTLs are in ascending order.  Returned: When there is more than one distinct TTL  Sample: `[300, 3600]` |
| **type**  string | The DNS record type.  Returned: success  Sample: `"A"` |
| **value**  list / elements=string | The DNS record set’s value.  Returned: success  Sample: `["1.2.3.4", "1.2.3.5"]` |
| **zone_id**  string  added in community.dns 0.2.0 | The ID of the zone.  Returned: success  Sample: `"23"` |

### Authors

- Markus Bergholz (@markuman)
- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.dns)
[Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-dns)
