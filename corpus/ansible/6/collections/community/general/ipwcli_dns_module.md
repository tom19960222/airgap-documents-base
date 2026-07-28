---
collection: ansible
version: "6"
title: "community.general.ipwcli_dns module – Manage DNS Records for Ericsson IPWorks via ipwcli"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ipwcli_dns_module.html
fetched_at: 2026-07-27T17:10:05+00:00
---
# community.general.ipwcli_dns module – Manage DNS Records for Ericsson IPWorks via ipwcli

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
> see [Requirements](ipwcli_dns_module.md#ansible-collections-community-general-ipwcli-dns-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ipwcli_dns`.

New in community.general 0.2.0

- [Synopsis](ipwcli_dns_module.md#synopsis)
- [Requirements](ipwcli_dns_module.md#requirements)
- [Parameters](ipwcli_dns_module.md#parameters)
- [Notes](ipwcli_dns_module.md#notes)
- [Examples](ipwcli_dns_module.md#examples)
- [Return Values](ipwcli_dns_module.md#return-values)

## [Synopsis](ipwcli_dns_module.md#id1)

- Manage DNS records for the Ericsson IPWorks DNS server. The module will use the ipwcli to deploy the DNS records.

## [Requirements](ipwcli_dns_module.md#id2)

The below requirements are needed on the host that executes this module.

- ipwcli (installed on Ericsson IPWorks)

## [Parameters](ipwcli_dns_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **address**  string | The IP address for the A or AAAA record.  Required for *type=A* or *type=AAAA*. |
| **container**  string / required | Sets the container zone for the record. |
| **dnsname**  string / required | Name of the record. |
| **flags**  string | Sets one of the possible flags of NAPTR record.  Required for *type=NAPTR*.  Choices:   - `"S"` - `"A"` - `"U"` - `"P"` |
| **order**  integer | Sets the order of the NAPTR record.  Required for *type=NAPTR*. |
| **password**  string / required | Password to login on ipwcli. |
| **port**  integer | Sets the port of the SRV record.  Required for *type=SRV*. |
| **preference**  integer | Sets the preference of the NAPTR record.  Required for *type=NAPTR*. |
| **priority**  integer | Sets the priority of the SRV record.  Default: `10` |
| **replacement**  string | Sets the replacement of the NAPTR record.  Required for *type=NAPTR*. |
| **service**  string | Sets the service of the NAPTR record.  Required for *type=NAPTR*. |
| **state**  string | Whether the record should exist or not.  Choices:   - `"absent"` - `"present"` ← (default) |
| **target**  string | Sets the target of the SRV record.  Required for *type=SRV*. |
| **ttl**  integer | Sets the TTL of the record.  Default: `3600` |
| **type**  string / required | Type of the record.  Choices:   - `"NAPTR"` - `"SRV"` - `"A"` - `"AAAA"` |
| **username**  string / required | Username to login on ipwcli. |
| **weight**  integer | Sets the weight of the SRV record.  Default: `10` |

## [Notes](ipwcli_dns_module.md#id4)

> **Note:**
>
> - To make the DNS record changes effective, you need to run `update dnsserver` on the ipwcli.

## [Examples](ipwcli_dns_module.md#id5)

```yaml+jinja
- name: Create A record
  community.general.ipwcli_dns:
    dnsname: example.com
    type: A
    container: ZoneOne
    address: 127.0.0.1

- name: Remove SRV record if exists
  community.general.ipwcli_dns:
    dnsname: _sip._tcp.test.example.com
    type: SRV
    container: ZoneOne
    ttl: 100
    state: absent
    target: example.com
    port: 5060

- name: Create NAPTR record
  community.general.ipwcli_dns:
    dnsname: test.example.com
    type: NAPTR
    preference: 10
    container: ZoneOne
    ttl: 100
    order: 10
    service: 'SIP+D2T'
    replacement: '_sip._tcp.test.example.com.'
    flags: S
```

## [Return Values](ipwcli_dns_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **record**  string | The created record from the input params  Returned: always |

### Authors

- Christian Wollinger (@cwollinger)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
