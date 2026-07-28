---
collection: ansible
version: "8"
title: "community.dns.hosttech_dns_zone_info module – Retrieve zone information in Hosttech DNS service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/dns/hosttech_dns_zone_info_module.html
fetched_at: 2026-07-28T01:43:31+00:00
---
# community.dns.hosttech_dns_zone_info module – Retrieve zone information in Hosttech DNS service

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
> see [Requirements](hosttech_dns_zone_info_module.md#ansible-collections-community-dns-hosttech-dns-zone-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.dns.hosttech_dns_zone_info`.

New in community.dns 0.2.0

- [Synopsis](hosttech_dns_zone_info_module.md#synopsis)
- [Requirements](hosttech_dns_zone_info_module.md#requirements)
- [Parameters](hosttech_dns_zone_info_module.md#parameters)
- [Attributes](hosttech_dns_zone_info_module.md#attributes)
- [Examples](hosttech_dns_zone_info_module.md#examples)
- [Return Values](hosttech_dns_zone_info_module.md#return-values)

## [Synopsis](hosttech_dns_zone_info_module.md#id1)

- Retrieves zone information in Hosttech DNS service.

## [Requirements](hosttech_dns_zone_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- lxml

## [Parameters](hosttech_dns_zone_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hosttech_password**  string | The password for the Hosttech API user.  If provided, `hosttech_username` must also be provided.  Mutually exclusive with `hosttech_token`. |
| **hosttech_token**  aliases: api_token  string  *added in community.dns 0.2.0* | The password for the Hosttech API user.  Mutually exclusive with `hosttech_username` and `hosttech_password`.  Since community.dns 1.2.0, the alias `api_token` can be used. |
| **hosttech_username**  string | The username for the Hosttech API user.  If provided, `hosttech_password` must also be provided.  Mutually exclusive with `hosttech_token`. |
| **zone_id**  integer  *added in community.dns 0.2.0* | The ID of the DNS zone to query.  Exactly one of `zone_name` and `zone_id` must be specified. |
| **zone_name**  aliases: zone  string | The DNS zone to query.  Exactly one of `zone_name` and `zone_id` must be specified. |

## [Attributes](hosttech_dns_zone_info_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | **Action group:** **community.dns.hosttech**  *added in community.dns 2.4.0* | Use `group/community.dns.hosttech` in `module_defaults` to set defaults for this module. |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](hosttech_dns_zone_info_module.md#id5)

```yaml+jinja
- name: Retrieve details for foo.com zone
  community.dns.hosttech_dns_zone_info:
    zone_name: foo.com
    hosttech_username: foo
    hosttech_password: bar
  register: rec

- name: Retrieve details for zone 23
  community.dns.hosttech_dns_zone_info:
    zone_id: 23
    hosttech_token: access_token
```

## [Return Values](hosttech_dns_zone_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **zone_id**  integer | The ID of the zone.  **Returned:** success  **Sample:** `23` |
| **zone_info**  dictionary  *added in community.dns 2.0.0* | Extra information returned by the API.  **Returned:** success  **Sample:** `{"dnssec": true, "dnssec_email": "test@example.com", "ds_records": [], "email": "test@example.com", "ttl": 3600}` |
| **dnssec**  boolean | Whether DNSSEC is enabled for the zone or not.  **Returned:** When `hosttech_token` has been specified. |
| **dnssec_email**  string | The email address contacted when the DNSSEC key is changed.  Is `none` if DNSSEC is not enabled.  **Returned:** When `hosttech_token` has been specified. |
| **ds_records**  list / elements=dictionary | The DS records.  See [Section 5 of RFC 4034](https://datatracker.ietf.org/doc/html/rfc4034#section-5) and [Section 2.1 of RFC 4034](https://datatracker.ietf.org/doc/html/rfc4034#section-2.1) for details.  Is `none` if DNSSEC is not enabled.  **Returned:** When `hosttech_token` has been specified. |
| **algorithm**  integer | This value is the algorithm number of the DNSKEY RR referred to by the DS record.  A list of values can be found in [Appendix A.1 of RFC 4034](https://datatracker.ietf.org/doc/html/rfc4034#appendix-A.1).  **Returned:** success  **Sample:** `8` |
| **digest**  string | A digest of the DNSKEY RR record this DS record refers to.  **Returned:** success  **Sample:** `"012356789ABCDEF0123456789ABCDEF012345678"` |
| **digest_type**  integer | This value identifies the algorithm used to construct the digest.  A list of values can be found in [Appendix A.2 of RFC 4034](https://datatracker.ietf.org/doc/html/rfc4034#appendix-A.2).  **Returned:** success  **Sample:** `1` |
| **flags**  integer | The Zone Key flag. See [Section 2.1.1 of RFC 4034](https://datatracker.ietf.org/doc/html/rfc4034#section-2.1.1) for details.  **Returned:** success  **Sample:** `257` |
| **key_tag**  integer | The Key Tag field lists the key tag of the DNSKEY RR referred to by the DS record.  **Returned:** success  **Sample:** `12345` |
| **protocol**  integer | Must be 3 according to RFC 4034.  **Returned:** success  **Sample:** `3` |
| **public_key**  string | The public key material.  **Returned:** success  **Sample:** `"MuhdzsQdqEGShwjtJDKZZjdKqUSGluFzTTinpuEeIRzLLcgkwgAPKWFa eQntNlmcNDeCziGwpdvhJnvKXEMbFcZwsaDIJuWqERxAQNGABWfPlCLh HQPnbpRPNKipSdBaUhuOubvFvjBpFAwiwSAapRDVsAgKvjXucfXpFfYb pCundbAXBWhbpHVbqgmGoixXzFSwUsGVYLPpBCiDlLJwzjRKYYaoVYge kMtKFYUVnWIKbectWkDFdVqXwkKigCUDiuTTJxOBRJRNzGiDNMWBjYSm bBCAHMaMYaghLbYTwyKXltdHTHwBwtswGNfpnEdSpKFzZJonBZArQfHD lfceKgmKwEF="` |
| **email**  string | The zone’s DNS contact mail in the SOA record.  **Returned:** success |
| **ttl**  integer | The zone’s TTL.  **Returned:** success |
| **zone_name**  integer | The name of the zone.  **Returned:** success  **Sample:** `"example.com"` |

### Authors

- Felix Fontein (@felixfontein)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.dns)
- [Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
- [Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
- [Communication](index.md#communication-for-community-dns)
