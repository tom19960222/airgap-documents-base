---
collection: ansible
version: "6"
title: "community.general.udm_dns_record module – Manage dns entries on a univention corporate server"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/udm_dns_record_module.html
fetched_at: 2026-07-27T17:13:37+00:00
---
# community.general.udm_dns_record module – Manage dns entries on a univention corporate server

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](udm_dns_record_module.md#ansible-collections-community-general-udm-dns-record-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.udm_dns_record`.

- [Synopsis](udm_dns_record_module.md#synopsis)
- [Requirements](udm_dns_record_module.md#requirements)
- [Parameters](udm_dns_record_module.md#parameters)
- [Examples](udm_dns_record_module.md#examples)

## [Synopsis](udm_dns_record_module.md#id1)

- This module allows to manage dns records on a univention corporate server (UCS). It uses the python API of the UCS to create a new object or edit it.

## [Requirements](udm_dns_record_module.md#id2)

The below requirements are needed on the host that executes this module.

- Python >= 2.6
- Univention
- ipaddress (for *type=ptr_record*)

## [Parameters](udm_dns_record_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **data**  dictionary | Additional data for this record, e.g. [‘a’: ‘192.0.2.1’]. Required if *state=present*.  Default: `{}` |
| **name**  string / required | Name of the record, this is also the DNS record. E.g. www for www.example.com.  For PTR records this has to be the IP address. |
| **state**  string | Whether the dns record is present or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **type**  string / required | Define the record type. `host_record` is a A or AAAA record, `alias` is a CNAME, `ptr_record` is a PTR record, `srv_record` is a SRV record and `txt_record` is a TXT record.  The available choices are: `host_record`, `alias`, `ptr_record`, `srv_record`, `txt_record`. |
| **zone**  string / required | Corresponding DNS zone for this record, e.g. example.com.  For PTR records this has to be the full reverse zone (for example `1.1.192.in-addr.arpa`). |

## [Examples](udm_dns_record_module.md#id4)

```yaml+jinja
- name: Create a DNS record on a UCS
  community.general.udm_dns_record:
    name: www
    zone: example.com
    type: host_record
    data:
      a:
         - 192.0.2.1
         - 2001:0db8::42

- name: Create a DNS v4 PTR record on a UCS
  community.general.udm_dns_record:
    name: 192.0.2.1
    zone: 2.0.192.in-addr.arpa
    type: ptr_record
    data:
      ptr_record: "www.example.com."

- name: Create a DNS v6 PTR record on a UCS
  community.general.udm_dns_record:
    name: 2001:db8:0:0:0:ff00:42:8329
    zone: 2.4.0.0.0.0.f.f.0.0.0.0.0.0.0.0.0.0.0.0.8.b.d.0.1.0.0.2.ip6.arpa
    type: ptr_record
    data:
      ptr_record: "www.example.com."
```

### Authors

- Tobias Rüetschi (@keachi)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
