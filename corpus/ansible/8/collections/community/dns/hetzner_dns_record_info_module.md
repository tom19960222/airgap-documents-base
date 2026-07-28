---
collection: ansible
version: "8"
title: "community.dns.hetzner_dns_record_info module – Retrieve records in Hetzner DNS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/hetzner_dns_record_info_module.html
fetched_at: 2026-07-28T01:43:24+00:00
---
# community.dns.hetzner_dns_record_info module – Retrieve records in Hetzner DNS service

> **Note:**
>
> This module is part of the [community.dns collection](https://galaxy.ansible.com/ui/repo/published/community/dns/) (version 2.6.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.dns`.
>
> To use it in a playbook, specify: `community.dns.hetzner_dns_record_info`.

New in community.dns 2.0.0

- [Synopsis](hetzner_dns_record_info_module.md#synopsis)
- [Parameters](hetzner_dns_record_info_module.md#parameters)
- [Attributes](hetzner_dns_record_info_module.md#attributes)
- [See Also](hetzner_dns_record_info_module.md#see-also)
- [Examples](hetzner_dns_record_info_module.md#examples)
- [Return Values](hetzner_dns_record_info_module.md#return-values)

## [Synopsis](hetzner_dns_record_info_module.md#id1)

- Retrieves DNS records in Hetzner DNS service.

## [Parameters](hetzner_dns_record_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hetzner_token**  aliases: api_token  string / required | The token for the Hetzner API.  If not provided, will be read from the environment variable [`HETZNER_DNS_TOKEN`](../../environment_variables.md#envvar-HETZNER_DNS_TOKEN). |
| **prefix**  string | The prefix of the DNS record.  This is the part of `record` before `zone_name`. For example, if the record to be modified is `www.example.com` for the zone `example.com`, the prefix is `www`. If the record in this example would be `example.com`, the prefix would be `''` (empty string).  If `what` is `single_record` or `all_types_for_record`, exactly one of `record` and `prefix` is required. |
| **record**  string | The full DNS record to retrieve.  If `what` is `single_record` or `all_types_for_record`, exactly one of `record` and `prefix` is required. |
| **txt_character_encoding**  string  *added in community.dns 2.5.0* | Whether to treat numeric escape sequences (`\xyz`) as octal or decimal numbers. This is only used when `txt_transformation=quoted`.  The current default is `octal` which is deprecated. It will change to `decimal` in community.dns 3.0.0. The value `decimal` is compatible to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt).  **Choices:**   - `"decimal"` - `"octal"` |
| **txt_transformation**  string | Determines how TXT entry values are converted between the API and this module’s input and output.  The value `api` means that values are returned from this module as they are returned from the API, and pushed to the API as they have been passed to this module. For idempotency checks, the input string will be compared to the strings returned by the API. The API might automatically transform some values, like splitting long values or adding quotes, which can cause problems with idempotency.  The value `unquoted` automatically transforms values so that you can pass in unquoted values, and the module will return unquoted values. If you pass in quoted values, they will be double-quoted.  The value `quoted` automatically transforms values so that you must use quoting for values that contain spaces, characters such as quotation marks and backslashes, and that are longer than 255 bytes. It also makes sure to return values from the API in a normalized encoding.  The default value, `unquoted`, ensures that you can work with values without having to care about how to correctly quote for DNS. Most users should use one of `unquoted` or `quoted`, but not `api`.  **Note:** the conversion code assumes UTF-8 encoding for values. If you need another encoding use `txt_transformation=api` and handle the encoding yourself.  **Choices:**   - `"api"` - `"quoted"` - `"unquoted"` ← (default) |
| **type**  string | The type of DNS record to retrieve.  Required if `what` is `single_record`.  **Choices:**   - `"A"` - `"AAAA"` - `"CAA"` - `"CNAME"` - `"DANE"` - `"DS"` - `"HINFO"` - `"MX"` - `"NS"` - `"RP"` - `"SOA"` - `"SRV"` - `"TLSA"` - `"TXT"` |
| **what**  string | Describes whether to fetch a single record and type combination, all types for a record, or all records. By default, a single record and type combination is fetched.  Note that the return value structure depends on this option.  **Choices:**   - `"single_record"` ← (default) - `"all_types_for_record"` - `"all_records"` |
| **zone_id**  string | The ID of the DNS zone to modify.  Exactly one of `zone_name` and `zone_id` must be specified. |
| **zone_name**  aliases: zone  string | The DNS zone to modify.  Exactly one of `zone_name` and `zone_id` must be specified. |

## [Attributes](hetzner_dns_record_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action group:** **community.dns.hetzner**  *added in community.dns 2.4.0* | Use `group/community.dns.hetzner` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [See Also](hetzner_dns_record_info_module.md#id4)

> **See also:**
>
> [community.dns.hetzner_dns_record_set_info](hetzner_dns_record_set_info_module.md#ansible-collections-community-dns-hetzner-dns-record-set-info-module)
> :   Retrieve record sets in Hetzner DNS service.
>
> [community.dns.hetzner_dns_records](hetzner_dns_records_inventory.md#ansible-collections-community-dns-hetzner-dns-records-inventory) inventory plugin
> :   Create inventory from Hetzner DNS records.

## [Examples](hetzner_dns_record_info_module.md#id5)

```yaml+jinja
- name: Retrieve the details for the A records of new.foo.com
  community.dns.hetzner_dns_record_info:
    zone: foo.com
    record: new.foo.com
    type: A
    hetzner_token: access_token
  register: rec

- name: Print the A records
  ansible.builtin.debug:
    msg: "{{ rec.records }}"
```

## [Return Values](hetzner_dns_record_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **records**  list / elements=dictionary | The list of fetched records.  **Returned:** success and `what` is not `single_record`  **Sample:** `[{"extra": {}, "record": "sample.example.com", "ttl": 3600, "type": "A", "value": "1.2.3.4"}]` |
| **extra**  dictionary | Extra information on records.  **Returned:** success  **Sample:** `{"created": "2021-07-09T11:18:37Z", "modified": "2021-07-09T11:18:37Z"}` |
| **prefix**  string | The record prefix.  **Returned:** success  **Sample:** `"sample"` |
| **record**  string | The record name.  **Returned:** success  **Sample:** `"sample.example.com"` |
| **ttl**  integer | The TTL.  Will return `none` if the zone’s default TTL is used.  **Returned:** success  **Sample:** `3600` |
| **type**  string | The DNS record type.  **Returned:** success  **Sample:** `"A"` |
| **value**  string | The DNS record’s value.  **Returned:** success  **Sample:** `"1.2.3.4"` |
| **zone_id**  string | The ID of the zone.  **Returned:** success  **Sample:** `"23"` |

### Authors

- Markus Bergholz (@markuman)
- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.dns)
- [Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-dns)
