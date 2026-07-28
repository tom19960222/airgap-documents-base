---
collection: ansible
version: "6"
title: "community.dns.hosttech_dns_records inventory – Create inventory from Hosttech DNS records"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/dns/hosttech_dns_records_inventory.html
fetched_at: 2026-07-27T17:07:13+00:00
---
# community.dns.hosttech_dns_records inventory – Create inventory from Hosttech DNS records

> **Note:**
>
> This inventory plugin is part of the [community.dns collection](https://galaxy.ansible.com/community/dns) (version 2.4.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.dns`.
> You need further requirements to be able to use this inventory plugin,
> see [Requirements](hosttech_dns_records_inventory.md#ansible-collections-community-dns-hosttech-dns-records-inventory-requirements) for details.
>
> To use it in a playbook, specify: `community.dns.hosttech_dns_records`.

New in community.dns 2.0.0

- [Synopsis](hosttech_dns_records_inventory.md#synopsis)
- [Requirements](hosttech_dns_records_inventory.md#requirements)
- [Parameters](hosttech_dns_records_inventory.md#parameters)
- [Notes](hosttech_dns_records_inventory.md#notes)

## [Synopsis](hosttech_dns_records_inventory.md#id1)

- Records are matched by prefix / record name and value.

## [Requirements](hosttech_dns_records_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- lxml

## [Parameters](hosttech_dns_records_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **filters**  dictionary | A dictionary of filter value pairs.  Default: `{}` |
| **type**  list / elements=string | Record types whose values to use.  Choices:   - `"A"` ← (default) - `"AAAA"` ← (default) - `"CAA"` - `"CNAME"` ← (default) - `"MX"` - `"NS"` - `"PTR"` - `"SPF"` - `"SRV"` - `"TXT"`   Default: `["A", "AAAA", "CNAME"]` |
| **hosttech_password**  string | The password for the Hosttech API user.  If provided, *hosttech_username* must also be provided.  Mutually exclusive with *hosttech_token*. |
| **hosttech_token**  aliases: api_token  string  added in community.dns 0.2.0 | The password for the Hosttech API user.  Mutually exclusive with *hosttech_username* and *hosttech_password*.  Since community.dns 1.2.0, the alias *api_token* can be used. |
| **hosttech_username**  string | The username for the Hosttech API user.  If provided, *hosttech_password* must also be provided.  Mutually exclusive with *hosttech_token*. |
| **txt_transformation**  string | Determines how TXT entry values are converted between the API and this module’s input and output.  The value `api` means that values are returned from this module as they are returned from the API, and pushed to the API as they have been passed to this module. For idempotency checks, the input string will be compared to the strings returned by the API. The API might automatically transform some values, like splitting long values or adding quotes, which can cause problems with idempotency.  The value `unquoted` automatically transforms values so that you can pass in unquoted values, and the module will return unquoted values. If you pass in quoted values, they will be double-quoted.  The value `quoted` automatically transforms values so that you must use quoting for values that contain spaces, characters such as quotation marks and backslashes, and that are longer than 255 bytes. It also makes sure to return values from the API in a normalized encoding.  The default value, `unquoted`, ensures that you can work with values without having to care about how to correctly quote for DNS. Most users should use one of `unquoted` or `quoted`, but not `api`.  **Note:** the conversion code assumes UTF-8 encoding for values. If you need another encoding use *txt_transformation=api* and handle the encoding yourself.  Choices:   - `"api"` - `"quoted"` - `"unquoted"` ← (default) |
| **zone_id**  any | The ID of the DNS zone to modify.  Exactly one of *zone_name* and *zone_id* must be specified. |
| **zone_name**  aliases: zone  string | The DNS zone to modify.  Exactly one of *zone_name* and *zone_id* must be specified. |

## [Notes](hosttech_dns_records_inventory.md#id4)

> **Note:**
>
> - The provider-specific *hosttech_username*, *hosttech_password*, and *hosttech_token* options can be templated.
> - The *zone_name* and *zone_id* options can be templated.

### Authors

- Markus Bergholz (@markuman)
- Felix Fontein (@felixfontein)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.dns)
[Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-dns)
