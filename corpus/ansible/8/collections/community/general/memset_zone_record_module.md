---
collection: ansible
version: "8"
title: "community.general.memset_zone_record module – Create and delete records in Memset DNS zones"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/memset_zone_record_module.html
fetched_at: 2026-07-28T01:47:59+00:00
---
# community.general.memset_zone_record module – Create and delete records in Memset DNS zones

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.memset_zone_record`.

- [Synopsis](memset_zone_record_module.md#synopsis)
- [Parameters](memset_zone_record_module.md#parameters)
- [Attributes](memset_zone_record_module.md#attributes)
- [Notes](memset_zone_record_module.md#notes)
- [Examples](memset_zone_record_module.md#examples)
- [Return Values](memset_zone_record_module.md#return-values)

## [Synopsis](memset_zone_record_module.md#id1)

- Manage DNS records in a Memset account.

Aliases: cloud.memset.memset_zone_record

## [Parameters](memset_zone_record_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  aliases: ip, data  string / required | The address for this record (can be IP or text string depending on record type). |
| **api_key**  string / required | The API key obtained from the Memset control panel. |
| **priority**  integer | `SRV` and `TXT` record priority, in the range 0 > 999 (inclusive).  **Default:** `0` |
| **record**  string | The subdomain to create.  **Default:** `""` |
| **relative**  boolean | If set then the current domain is added onto the address field for `CNAME`, `MX`, `NS` and `SRV`record types.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Indicates desired state of resource.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **ttl**  integer | The record’s TTL in seconds (will inherit zone’s TTL if not explicitly set). This must be a valid int from <https://www.memset.com/apidocs/methods_dns.html#dns.zone_record_create>.  **Choices:**   - `0` ← (default) - `300` - `600` - `900` - `1800` - `3600` - `7200` - `10800` - `21600` - `43200` - `86400` |
| **type**  string / required | The type of DNS record to create.  **Choices:**   - `"A"` - `"AAAA"` - `"CNAME"` - `"MX"` - `"NS"` - `"SRV"` - `"TXT"` |
| **zone**  string / required | The name of the zone to which to add the record to. |

## [Attributes](memset_zone_record_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](memset_zone_record_module.md#id4)

> **Note:**
>
> - Zones can be thought of as a logical group of domains, all of which share the same DNS records (i.e. they point to the same IP). An API key generated via the Memset customer control panel is needed with the following minimum scope - `dns.zone_create`, `dns.zone_delete`, `dns.zone_list`.
> - Currently this module can only create one DNS record at a time. Multiple records should be created using `loop`.

## [Examples](memset_zone_record_module.md#id5)

```yaml+jinja
# Create DNS record for www.domain.com
- name: Create DNS record
  community.general.memset_zone_record:
    api_key: dcf089a2896940da9ffefb307ef49ccd
    state: present
    zone: domain.com
    type: A
    record: www
    address: 1.2.3.4
    ttl: 300
    relative: false
  delegate_to: localhost

# create an SPF record for domain.com
- name: Create SPF record for domain.com
  community.general.memset_zone_record:
    api_key: dcf089a2896940da9ffefb307ef49ccd
    state: present
    zone: domain.com
    type: TXT
    address: "v=spf1 +a +mx +ip4:a1.2.3.4 ?all"
  delegate_to: localhost

# create multiple DNS records
- name: Create multiple DNS records
  community.general.memset_zone_record:
    api_key: dcf089a2896940da9ffefb307ef49ccd
    zone: "{{ item.zone }}"
    type: "{{ item.type }}"
    record: "{{ item.record }}"
    address: "{{ item.address }}"
  delegate_to: localhost
  with_items:
    - { 'zone': 'domain1.com', 'type': 'A', 'record': 'www', 'address': '1.2.3.4' }
    - { 'zone': 'domain2.com', 'type': 'A', 'record': 'mail', 'address': '4.3.2.1' }
```

## [Return Values](memset_zone_record_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **memset_api**  complex | Record info from the Memset API.  **Returned:** when state == present |
| **address**  string | Record content (may be an IP, string or blank depending on record type).  **Returned:** always  **Sample:** `"1.1.1.1"` |
| **id**  string | Record ID.  **Returned:** always  **Sample:** `"b0bb1ce851aeea6feeb2dc32fe83bf9c"` |
| **priority**  integer | Priority for `MX` and `SRV` records.  **Returned:** always  **Sample:** `10` |
| **record**  string | Name of record.  **Returned:** always  **Sample:** `"www"` |
| **relative**  boolean | Adds the current domain onto the address field for `CNAME`, `MX`, `NS` and `SRV` types.  **Returned:** always  **Sample:** `false` |
| **ttl**  integer | Record TTL.  **Returned:** always  **Sample:** `10` |
| **type**  string | Record type.  **Returned:** always  **Sample:** `"AAAA"` |
| **zone_id**  string | Zone ID.  **Returned:** always  **Sample:** `"b0bb1ce851aeea6feeb2dc32fe83bf9c"` |

### Authors

- Simon Weald (@glitchcrab)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
