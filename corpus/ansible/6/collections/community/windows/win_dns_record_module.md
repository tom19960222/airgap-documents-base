---
collection: ansible
version: "6"
title: "community.windows.win_dns_record module – Manage Windows Server DNS records"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_dns_record_module.html
fetched_at: 2026-07-27T17:23:17+00:00
---
# community.windows.win_dns_record module – Manage Windows Server DNS records

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_dns_record_module.md#ansible-collections-community-windows-win-dns-record-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_dns_record`.

- [Synopsis](win_dns_record_module.md#synopsis)
- [Requirements](win_dns_record_module.md#requirements)
- [Parameters](win_dns_record_module.md#parameters)
- [Examples](win_dns_record_module.md#examples)

## [Synopsis](win_dns_record_module.md#id1)

- Manage DNS records within an existing Windows Server DNS zone.

## [Requirements](win_dns_record_module.md#id2)

The below requirements are needed on the host that executes this module.

- This module requires Windows 8, Server 2012, or newer.

## [Parameters](win_dns_record_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **computer_name**  string | Specifies a DNS server.  You can specify an IP address or any value that resolves to an IP address, such as a fully qualified domain name (FQDN), host name, or NETBIOS name. |
| **name**  string / required | The name of the record. |
| **port**  integer  added in community.windows 1.0.0 | The port number of the record.  Required when `type=SRV`.  Supported only for `type=SRV`. |
| **priority**  integer  added in community.windows 1.0.0 | The priority number for each service in SRV record.  Required when `type=SRV`.  Supported only for `type=SRV`. |
| **state**  string | Whether the record should exist or not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **ttl**  integer | The “time to live” of the record, in seconds.  Ignored when `state=absent`.  Valid range is 1 - 31557600.  Note that an Active Directory forest can specify a minimum TTL, and will dynamically “round up” other values to that minimum.  Default: `3600` |
| **type**  string / required | The type of DNS record to manage.  `SRV` was added in the 1.0.0 release of this collection.  `NS` was added in the 1.1.0 release of this collection.  `TXT` was added in the 1.6.0 release of this collection.  Choices:   - `"A"` - `"AAAA"` - `"CNAME"` - `"NS"` - `"PTR"` - `"SRV"` - `"TXT"` |
| **value**  aliases: values  list / elements=string | The value(s) to specify. Required when `state=present`.  When `type=PTR` only the partial part of the IP should be given.  Multiple values can be passed when `type=NS`  Default: `[]` |
| **weight**  integer  added in community.windows 1.0.0 | Weightage given to each service record in SRV record.  Required when `type=SRV`.  Supported only for `type=SRV`. |
| **zone**  string / required | The name of the zone to manage (eg `example.com`).  The zone must already exist. |

## [Examples](win_dns_record_module.md#id4)

```yaml+jinja
# Demonstrate creating a matching A and PTR record.

- name: Create database server record
  community.windows.win_dns_record:
    name: "cgyl1404p.amer.example.com"
    type: "A"
    value: "10.1.1.1"
    zone: "amer.example.com"

- name: Create matching PTR record
  community.windows.win_dns_record:
    name: "1.1.1"
    type: "PTR"
    value: "db1"
    zone: "10.in-addr.arpa"

# Demonstrate replacing an A record with a CNAME

- name: Remove static record
  community.windows.win_dns_record:
    name: "db1"
    type: "A"
    state: absent
    zone: "amer.example.com"

- name: Create database server alias
  community.windows.win_dns_record:
    name: "db1"
    type: "CNAME"
    value: "cgyl1404p.amer.example.com"
    zone: "amer.example.com"

# Demonstrate creating multiple A records for the same name

- name: Create multiple A record values for www
  community.windows.win_dns_record:
    name: "www"
    type: "A"
    values:
      - 10.0.42.5
      - 10.0.42.6
      - 10.0.42.7
    zone: "example.com"

# Demonstrates a partial update (replace some existing values with new ones)
# for a pre-existing name

- name: Update www host with new addresses
  community.windows.win_dns_record:
    name: "www"
    type: "A"
    values:
      - 10.0.42.5  # this old value was kept (others removed)
      - 10.0.42.12  # this new value was added
    zone: "example.com"

# Demonstrate creating a SRV record

- name: Creating a SRV record with port number and priority
  community.windows.win_dns_record:
    name: "test"
    priority: 5
    port: 995
    state: present
    type: "SRV"
    weight: 2
    value: "amer.example.com"
    zone: "example.com"

# Demonstrate creating a NS record with multiple values

- name: Creating NS record
  community.windows.win_dns_record:
    name: "ansible.prog"
    state: present
    type: "NS"
    values:
      - 10.0.0.1
      - 10.0.0.2
      - 10.0.0.3
      - 10.0.0.4
    zone: "example.com"

# Demonstrate creating a TXT record

- name: Creating a TXT record with descriptive Text
  community.windows.win_dns_record:
    name: "test"
    state: present
    type: "TXT"
    value: "justavalue"
    zone: "example.com"
```

### Authors

- Sebastian Gruber (@sgruber94)
- John Nelson (@johnboy2)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
