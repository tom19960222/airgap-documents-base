---
collection: ansible
version: "8"
title: "community.dns.hetzner_dns_zone_info module – Retrieve zone information in Hetzner DNS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/hetzner_dns_zone_info_module.html
fetched_at: 2026-07-28T01:43:27+00:00
---
# community.dns.hetzner_dns_zone_info module – Retrieve zone information in Hetzner DNS service

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
> To use it in a playbook, specify: `community.dns.hetzner_dns_zone_info`.

New in community.dns 2.0.0

- [Synopsis](hetzner_dns_zone_info_module.md#synopsis)
- [Parameters](hetzner_dns_zone_info_module.md#parameters)
- [Attributes](hetzner_dns_zone_info_module.md#attributes)
- [Examples](hetzner_dns_zone_info_module.md#examples)
- [Return Values](hetzner_dns_zone_info_module.md#return-values)

## [Synopsis](hetzner_dns_zone_info_module.md#id1)

- Retrieves zone information in Hetzner DNS service.

## [Parameters](hetzner_dns_zone_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **hetzner_token**  aliases: api_token  string / required | The token for the Hetzner API.  If not provided, will be read from the environment variable [`HETZNER_DNS_TOKEN`](../../environment_variables.md#envvar-HETZNER_DNS_TOKEN). |
| **zone_id**  string  *added in community.dns 0.2.0* | The ID of the DNS zone to query.  Exactly one of `zone_name` and `zone_id` must be specified. |
| **zone_name**  aliases: zone  string | The DNS zone to query.  Exactly one of `zone_name` and `zone_id` must be specified. |

## [Attributes](hetzner_dns_zone_info_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action group:** **community.dns.hetzner**  *added in community.dns 2.4.0* | Use `group/community.dns.hetzner` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](hetzner_dns_zone_info_module.md#id4)

```yaml+jinja
- name: Retrieve details for foo.com zone
  community.dns.hetzner_dns_zone_info:
    zone: foo.com
    hetzner_token: access_token
  register: rec

- name: Retrieve details for zone 23
  community.dns.hetzner_dns_zone_info:
    zone_id: 23
    hetzner_token: access_token
```

## [Return Values](hetzner_dns_zone_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **zone_id**  string | The ID of the zone.  **Returned:** success  **Sample:** `"23"` |
| **zone_info**  dictionary | Extra information returned by the API.  **Returned:** success |
| **created**  string | The time when the zone was created.  **Returned:** success  **Sample:** `"2021-07-15T19:23:58Z"` |
| **is_secondary_dns**  boolean | Indicates whether the zone is a secondary DNS zone.  **Returned:** success  **Sample:** `true` |
| **legacy_dns_host**  string | Unknown.  **Returned:** success |
| **legacy_ns**  list / elements=string | List of nameservers during import.  **Returned:** success |
| **modified**  string | The time the zone was last modified.  **Returned:** success  **Sample:** `"2021-07-15T19:23:58Z"` |
| **ns**  list / elements=string | List of nameservers the zone should have for using Hetzner’s DNS.  **Returned:** success |
| **owner**  string | Owner of the zone.  **Returned:** success |
| **paused**  boolean | Unknown.  **Returned:** success  **Sample:** `true` |
| **permission**  string | Zone’s permissions.  **Returned:** success |
| **project**  string | Unknown.  **Returned:** success |
| **records_count**  integer | Number of records associated to this zone.  **Returned:** success  **Sample:** `0` |
| **registrar**  string | Unknown.  **Returned:** success |
| **status**  string | Status of the zone.  Can be one of `verified`, `failed` and `pending`.  **Returned:** success  **Sample:** `"verified"` |
| **ttl**  integer | TTL of zone.  **Returned:** success  **Sample:** `0` |
| **txt_verification**  dictionary | Shape of the TXT record that has to be set to verify a zone.  If name and token are empty, no TXT record needs to be set.  **Returned:** success  **Sample:** `{"name": "", "token": ""}` |
| **name**  string | The TXT record’s name.  **Returned:** success |
| **token**  string | The TXT record’s content.  **Returned:** success |
| **verified**  string | Time when zone was verified.  **Returned:** success  **Sample:** `"2021-07-15T19:23:58Z"` |
| **zone_name**  integer | The name of the zone.  **Returned:** success  **Sample:** `"example.com"` |

### Authors

- Markus Bergholz (@markuman)
- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.dns)
- [Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-dns)
