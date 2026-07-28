---
collection: ansible
version: "8"
title: "community.general.udm_dns_zone module – Manage dns zones on a univention corporate server"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/udm_dns_zone_module.html
fetched_at: 2026-07-28T01:51:01+00:00
---
# community.general.udm_dns_zone module – Manage dns zones on a univention corporate server

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
> To use it in a playbook, specify: `community.general.udm_dns_zone`.

- [Synopsis](udm_dns_zone_module.md#synopsis)
- [Parameters](udm_dns_zone_module.md#parameters)
- [Attributes](udm_dns_zone_module.md#attributes)
- [Examples](udm_dns_zone_module.md#examples)

## [Synopsis](udm_dns_zone_module.md#id1)

- This module allows to manage dns zones on a univention corporate server (UCS). It uses the python API of the UCS to create a new object or edit it.

Aliases: cloud.univention.udm_dns_zone

## [Parameters](udm_dns_zone_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **contact**  string | Contact person in the SOA record.  **Default:** `""` |
| **expire**  integer | Specifies the upper limit on the time interval that can elapse before the zone is no longer authoritative.  **Default:** `604800` |
| **interfaces**  list / elements=string | List of interface IP addresses, on which the server should response this zone. Required if `state=present`.  **Default:** `[]` |
| **mx**  list / elements=string | List of MX servers. (Must declared as A or AAAA records).  **Default:** `[]` |
| **nameserver**  list / elements=string | List of appropriate name servers. Required if `state=present`.  **Default:** `[]` |
| **refresh**  integer | Interval before the zone should be refreshed.  **Default:** `3600` |
| **retry**  integer | Interval that should elapse before a failed refresh should be retried.  **Default:** `1800` |
| **state**  string | Whether the dns zone is present or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **ttl**  integer | Minimum TTL field that should be exported with any RR from this zone.  **Default:** `600` |
| **type**  string / required | Define if the zone is a forward or reverse DNS zone.  The available choices are: `forward_zone`, `reverse_zone`. |
| **zone**  aliases: name  string / required | DNS zone name, for example `example.com`. |

## [Attributes](udm_dns_zone_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **partial** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](udm_dns_zone_module.md#id4)

```yaml+jinja
- name: Create a DNS zone on a UCS
  community.general.udm_dns_zone:
    zone: example.com
    type: forward_zone
    nameserver:
      - ucs.example.com
    interfaces:
      - 192.0.2.1
```

### Authors

- Tobias Rüetschi (@keachi)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
