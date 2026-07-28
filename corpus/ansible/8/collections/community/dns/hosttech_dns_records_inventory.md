---
collection: ansible
version: "8"
title: "community.dns.hosttech_dns_records inventory – Create inventory from Hosttech DNS records"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/hosttech_dns_records_inventory.html
fetched_at: 2026-07-28T01:43:38+00:00
---
# community.dns.hosttech_dns_records inventory – Create inventory from Hosttech DNS records

> **Note:**
>
> This inventory plugin is part of the [community.dns collection](https://galaxy.ansible.com/ui/repo/published/community/dns/) (version 2.6.4).
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
- [See Also](hosttech_dns_records_inventory.md#see-also)
- [Examples](hosttech_dns_records_inventory.md#examples)

## [Synopsis](hosttech_dns_records_inventory.md#id1)

- For Ansible to be able to identify a YAML file as an inventory for this plugin, the inventory file must contain `plugin: community.dns.hosttech_dns_records` and its filename must end with `hosttech_dns.yaml` or `hosttech_dns.yml`
- Records are matched by prefix / record name and value.
- This plugin allows to create an inventory from Hosttech DNS records.

## [Requirements](hosttech_dns_records_inventory.md#id2)

The below requirements are needed on the local controller node that executes this inventory.

- lxml

## [Parameters](hosttech_dns_records_inventory.md#id3)

| Parameter | Comments |
| --- | --- |
| **filters**  dictionary | A dictionary of filter value pairs.  **Default:** `{}` |
| **type**  list / elements=string | Record types whose values to use.  **Choices:**   - `"A"` ← (default) - `"AAAA"` ← (default) - `"CAA"` - `"CNAME"` ← (default) - `"MX"` - `"NS"` - `"PTR"` - `"SPF"` - `"SRV"` - `"TXT"`   **Default:** `["A", "AAAA", "CNAME"]` |
| **hosttech_password**  string | The password for the Hosttech API user.  If provided, `hosttech_username` must also be provided.  Mutually exclusive with `hosttech_token`.  **Configuration:**   - Environment variable: [`ANSIBLE_HOSTTECH_API_PASSWORD`](../../environment_variables.md#envvar-ANSIBLE_HOSTTECH_API_PASSWORD)  *added in community.dns 2.5.0* |
| **hosttech_token**  aliases: api_token  string  *added in community.dns 0.2.0* | The password for the Hosttech API user.  Mutually exclusive with `hosttech_username` and `hosttech_password`.  Since community.dns 1.2.0, the alias `api_token` can be used.  **Configuration:**   - Environment variable: [`ANSIBLE_HOSTTECH_DNS_TOKEN`](../../environment_variables.md#envvar-ANSIBLE_HOSTTECH_DNS_TOKEN)  *added in community.dns 2.5.0* |
| **hosttech_username**  string | The username for the Hosttech API user.  If provided, `hosttech_password` must also be provided.  Mutually exclusive with `hosttech_token`.  **Configuration:**   - Environment variable: [`ANSIBLE_HOSTTECH_API_USERNAME`](../../environment_variables.md#envvar-ANSIBLE_HOSTTECH_API_USERNAME)  *added in community.dns 2.5.0* |
| **plugin**  string | The name of this plugin. Should always be set to `community.dns.hosttech_dns_records` for this plugin to recognize it as its own.  **Choices:**   - `"community.dns.hosttech_dns_records"` |
| **txt_character_encoding**  string  *added in community.dns 2.5.0* | Whether to treat numeric escape sequences (`\xyz`) as octal or decimal numbers. This is only used when `txt_transformation=quoted`.  The current default is `octal` which is deprecated. It will change to `decimal` in community.dns 3.0.0. The value `decimal` is compatible to [RFC 1035](https://www.ietf.org/rfc/rfc1035.txt).  **Choices:**   - `"decimal"` - `"octal"` |
| **txt_transformation**  string | Determines how TXT entry values are converted between the API and this module’s input and output.  The value `api` means that values are returned from this module as they are returned from the API, and pushed to the API as they have been passed to this module. For idempotency checks, the input string will be compared to the strings returned by the API. The API might automatically transform some values, like splitting long values or adding quotes, which can cause problems with idempotency.  The value `unquoted` automatically transforms values so that you can pass in unquoted values, and the module will return unquoted values. If you pass in quoted values, they will be double-quoted.  The value `quoted` automatically transforms values so that you must use quoting for values that contain spaces, characters such as quotation marks and backslashes, and that are longer than 255 bytes. It also makes sure to return values from the API in a normalized encoding.  The default value, `unquoted`, ensures that you can work with values without having to care about how to correctly quote for DNS. Most users should use one of `unquoted` or `quoted`, but not `api`.  **Note:** the conversion code assumes UTF-8 encoding for values. If you need another encoding use `txt_transformation=api` and handle the encoding yourself.  **Choices:**   - `"api"` - `"quoted"` - `"unquoted"` ← (default) |
| **zone_id**  any | The ID of the DNS zone to modify.  Exactly one of `zone_name` and `zone_id` must be specified. |
| **zone_name**  aliases: zone  string | The DNS zone to modify.  Exactly one of `zone_name` and `zone_id` must be specified. |

## [Notes](hosttech_dns_records_inventory.md#id4)

> **Note:**
>
> - The provider-specific `hosttech_username`, `hosttech_password`, and `hosttech_token` options can be templated.
> - The `zone_name` and `zone_id` options can be templated.

## [See Also](hosttech_dns_records_inventory.md#id5)

> **See also:**
>
> [community.dns.hosttech_dns_record_set_info](hosttech_dns_record_set_info_module.md#ansible-collections-community-dns-hosttech-dns-record-set-info-module)
> :   Retrieve record sets in Hosttech DNS service.
>
> [community.dns.hosttech_dns_record_info](hosttech_dns_record_info_module.md#ansible-collections-community-dns-hosttech-dns-record-info-module)
> :   Retrieve records in Hosttech DNS service.

## [Examples](hosttech_dns_records_inventory.md#id6)

```yaml+jinja
# filename must end with hosttech_dns.yaml or hosttech_dns.yml

plugin: community.dns.hosttech_dns_records
zone_name: domain.ch
filters:
  type:
    - AAAA

# You can also configure the token by putting secret value into this file,
# but this is discouraged. Use a lookup like below, or leave it away and
# set it with the ANSIBLE_HOSTTECH_DNS_TOKEN environment variable.
hosttech_token: >-
    {{ (lookup('community.sops.sops', 'keys/hosttech.sops.yml') | from_yaml).hosttech_dns_token }}
```

### Authors

- Markus Bergholz (@markuman)
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
