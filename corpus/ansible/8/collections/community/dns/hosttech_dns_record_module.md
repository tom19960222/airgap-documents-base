---
collection: ansible
version: "8"
title: "community.dns.hosttech_dns_record module – Add or delete a single record in Hosttech DNS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/hosttech_dns_record_module.html
fetched_at: 2026-07-28T01:43:27+00:00
---
# community.dns.hosttech_dns_record module – Add or delete a single record in Hosttech DNS service

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
> see [Requirements](hosttech_dns_record_module.md#ansible-collections-community-dns-hosttech-dns-record-module-requirements) for details.
>
> To use it in a playbook, specify: `community.dns.hosttech_dns_record`.

New in community.dns 2.0.0

- [Synopsis](hosttech_dns_record_module.md#synopsis)
- [Requirements](hosttech_dns_record_module.md#requirements)
- [Parameters](hosttech_dns_record_module.md#parameters)
- [Attributes](hosttech_dns_record_module.md#attributes)
- [Examples](hosttech_dns_record_module.md#examples)
- [Return Values](hosttech_dns_record_module.md#return-values)

## [Synopsis](hosttech_dns_record_module.md#id1)

- Creates and deletes single DNS records in Hosttech DNS service.
- If you do not want to add/remove values, but replace values, you will be interested in modifying a **record set** and not a single record. This is in particular important when working with `CNAME` and `SOA` records. Use the [community.dns.hosttech_dns_record_set](hosttech_dns_record_set_module.md#ansible-collections-community-dns-hosttech-dns-record-set-module) module for working with record sets.
- Records are matched by prefix / record name and value.
- This module replaces `hosttech_dns_record` from community.dns before 2.0.0.

## [Requirements](hosttech_dns_record_module.md#id2)

The below requirements are needed on the host that executes this module.

- lxml

## [Parameters](hosttech_dns_record_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hosttech_password**  string | The password for the Hosttech API user.  If provided, `hosttech_username` must also be provided.  Mutually exclusive with `hosttech_token`. |
| **hosttech_token**  aliases: api_token  string  *added in community.dns 0.2.0* | The password for the Hosttech API user.  Mutually exclusive with `hosttech_username` and `hosttech_password`.  Since community.dns 1.2.0, the alias `api_token` can be used. |
| **hosttech_username**  string | The username for the Hosttech API user.  If provided, `hosttech_password` must also be provided.  Mutually exclusive with `hosttech_token`. |
| **prefix**  string | The prefix of the DNS record.  This is the part of `record` before `zone_name`. For example, if the record to be modified is `www.example.com` for the zone `example.com`, the prefix is `www`. If the record in this example would be `example.com`, the prefix would be `''` (empty string).  Exactly one of `record` and `prefix` must be specified. |
| **record**  string | The full DNS record to create or delete.  Exactly one of `record` and `prefix` must be specified. |
| **state**  string / required | Specifies the state of the resource record.  **Choices:**   - `"present"` - `"absent"` |
| **ttl**  integer | The TTL to give the new record, in seconds.  This is not used for record deletion.  **Default:** `3600` |
| **txt_character_encoding**  string  *added in community.dns 2.5.0* | Whether to treat numeric escape sequences (`\xyz`) as octal or decimal numbers. This is only used when `txt_transformation=quoted`.  The current default is `octal` which is deprecated. It will change to `decimal` in community.dns 3.0.0. The value `decimal` is compatible to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt).  **Choices:**   - `"decimal"` - `"octal"` |
| **txt_transformation**  string | Determines how TXT entry values are converted between the API and this module’s input and output.  The value `api` means that values are returned from this module as they are returned from the API, and pushed to the API as they have been passed to this module. For idempotency checks, the input string will be compared to the strings returned by the API. The API might automatically transform some values, like splitting long values or adding quotes, which can cause problems with idempotency.  The value `unquoted` automatically transforms values so that you can pass in unquoted values, and the module will return unquoted values. If you pass in quoted values, they will be double-quoted.  The value `quoted` automatically transforms values so that you must use quoting for values that contain spaces, characters such as quotation marks and backslashes, and that are longer than 255 bytes. It also makes sure to return values from the API in a normalized encoding.  The default value, `unquoted`, ensures that you can work with values without having to care about how to correctly quote for DNS. Most users should use one of `unquoted` or `quoted`, but not `api`.  **Note:** the conversion code assumes UTF-8 encoding for values. If you need another encoding use `txt_transformation=api` and handle the encoding yourself.  **Choices:**   - `"api"` - `"quoted"` - `"unquoted"` ← (default) |
| **type**  string / required | The type of DNS record to create or delete.  **Choices:**   - `"A"` - `"AAAA"` - `"CAA"` - `"CNAME"` - `"MX"` - `"NS"` - `"PTR"` - `"SPF"` - `"SRV"` - `"TXT"` |
| **value**  string / required | The new value when creating a DNS record.  When deleting a record all values for the record must be specified or it will not be deleted. |
| **zone_id**  integer | The ID of the DNS zone to modify.  Exactly one of `zone_name` and `zone_id` must be specified. |
| **zone_name**  aliases: zone  string | The DNS zone to modify.  Exactly one of `zone_name` and `zone_id` must be specified. |

## [Attributes](hosttech_dns_record_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action group:** **community.dns.hosttech**  *added in community.dns 2.4.0* | Use `group/community.dns.hosttech` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](hosttech_dns_record_module.md#id5)

```yaml+jinja
- name: Add a new.foo.com A record
  community.dns.hosttech_dns_record:
    state: present
    zone: foo.com
    record: new.foo.com
    type: A
    ttl: 7200
    value: 1.1.1.1
    hosttech_token: access_token

- name: Remove a new.foo.com A record
  community.dns.hosttech_dns_record:
    state: absent
    zone_name: foo.com
    record: new.foo.com
    type: A
    ttl: 7200
    value: 2.2.2.2
    hosttech_token: access_token
```

## [Return Values](hosttech_dns_record_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **zone_id**  integer | The ID of the zone.  **Returned:** success  **Sample:** `23` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.dns)
- [Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-dns)
