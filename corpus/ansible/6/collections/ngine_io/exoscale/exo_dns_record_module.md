---
collection: ansible
version: "6"
title: "ngine_io.exoscale.exo_dns_record module – Manages DNS records on Exoscale DNS."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/exoscale/exo_dns_record_module.html
fetched_at: 2026-07-28T00:16:00+00:00
---
# ngine_io.exoscale.exo_dns_record module – Manages DNS records on Exoscale DNS.

> **Note:**
>
> This module is part of the [ngine_io.exoscale collection](https://galaxy.ansible.com/ngine_io/exoscale) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.exoscale`.
> You need further requirements to be able to use this module,
> see [Requirements](exo_dns_record_module.md#ansible-collections-ngine-io-exoscale-exo-dns-record-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.exoscale.exo_dns_record`.

New in ngine_io.exoscale 0.1.0

- [Synopsis](exo_dns_record_module.md#synopsis)
- [Requirements](exo_dns_record_module.md#requirements)
- [Parameters](exo_dns_record_module.md#parameters)
- [Notes](exo_dns_record_module.md#notes)
- [Examples](exo_dns_record_module.md#examples)
- [Return Values](exo_dns_record_module.md#return-values)

## [Synopsis](exo_dns_record_module.md#id1)

- Create, update and delete records.

## [Requirements](exo_dns_record_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](exo_dns_record_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_key**  string | API key of the Exoscale DNS API.  The ENV variable `CLOUDSTACK_KEY` is used as default, when defined. |
| **api_region**  string | Name of the ini section in the `cloustack.ini` file.  The ENV variable `CLOUDSTACK_REGION` is used as default, when defined.  Default: `"cloudstack"` |
| **api_secret**  string | Secret key of the Exoscale DNS API.  The ENV variable `CLOUDSTACK_SECRET` is used as default, when defined. |
| **api_timeout**  integer | HTTP timeout to Exoscale DNS API.  The ENV variable `CLOUDSTACK_TIMEOUT` is used as default, when defined.  Default: `10` |
| **content**  aliases: value, address  string | Content of the record.  Required if `state=present` or `multiple=yes`. |
| **domain**  string / required | Domain the record is related to. |
| **multiple**  boolean | Whether there are more than one records with similar *name* and *record_type*.  Only allowed for a few record types, e.g. `record_type=A`, `record_type=NS` or `record_type=MX`.  *content* will not be updated, instead it is used as a key to find existing records.  Choices:   - `false` ← (default) - `true` |
| **name**  string | Name of the record.  Default: `""` |
| **prio**  aliases: priority  integer | Priority of the record. |
| **record_type**  aliases: rtype, type  string | Type of the record.  Choices:   - `"A"` ← (default) - `"ALIAS"` - `"CNAME"` - `"MX"` - `"SPF"` - `"URL"` - `"TXT"` - `"NS"` - `"SRV"` - `"NAPTR"` - `"PTR"` - `"AAAA"` - `"SSHFP"` - `"HINFO"` - `"POOL"` |
| **state**  string | State of the record.  Choices:   - `"present"` ← (default) - `"absent"` |
| **ttl**  integer | TTL of the record in seconds.  Default: `3600` |
| **validate_certs**  boolean | Validate SSL certs of the Exoscale DNS API.  Choices:   - `false` - `true` ← (default) |

## [Notes](exo_dns_record_module.md#id4)

> **Note:**
>
> - As Exoscale DNS uses the same API key and secret for all services, we reuse the config used for Exscale Compute based on CloudStack. The config is read from several locations, in the following order. The `CLOUDSTACK_KEY`, `CLOUDSTACK_SECRET` environment variables. A `CLOUDSTACK_CONFIG` environment variable pointing to an `.ini` file, A `cloudstack.ini` file in the current working directory. A `.cloudstack.ini` file in the users home directory. Optionally multiple credentials and endpoints can be specified using ini sections in `cloudstack.ini`. Use the argument `api_region` to select the section name, default section is `cloudstack`.
> - This module does not support multiple A records and will complain properly if you try.
> - More information Exoscale DNS can be found on <https://community.exoscale.ch/documentation/dns/>.
> - This module supports check mode and diff.

## [Examples](exo_dns_record_module.md#id5)

```yaml+jinja
- name: Create or update an A record
  ngine_io.exoscale.exo_dns_record:
    name: web-vm-1
    domain: example.com
    content: 1.2.3.4

- name: Update an existing A record with a new IP
  ngine_io.exoscale.exo_dns_record:
    name: web-vm-1
    domain: example.com
    content: 1.2.3.5

- name: Create another A record with same name
  ngine_io.exoscale.exo_dns_record:
    name: web-vm-1
    domain: example.com
    content: 1.2.3.6
    multiple: yes

- name: Create or update a CNAME record
  ngine_io.exoscale.exo_dns_record:
    name: www
    domain: example.com
    record_type: CNAME
    content: web-vm-1

- name: Create another MX record
  ngine_io.exoscale.exo_dns_record:
    domain: example.com
    record_type: MX
    content: mx1.example.com
    prio: 10
    multiple: yes

- name: Delete one MX record out of multiple
  ngine_io.exoscale.exo_dns_record:
    domain: example.com
    record_type: MX
    content: mx1.example.com
    multiple: yes
    state: absent

- name: Remove a single A record
  ngine_io.exoscale.exo_dns_record:
    name: www
    domain: example.com
    state: absent
```

## [Return Values](exo_dns_record_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **exo_dns_record**  complex | API record results  Returned: success |
| **content**  string | value of the record  Returned: success  Sample: `"1.2.3.4"` |
| **created_at**  string | When the record was created  Returned: success  Sample: `"2016-08-12T15:24:23.989Z"` |
| **domain**  string | Name of the domain  Returned: success  Sample: `"example.com"` |
| **domain_id**  integer | ID of the domain  Returned: success  Sample: `254324` |
| **id**  integer | ID of the record  Returned: success  Sample: `254324` |
| **name**  string | name of the record  Returned: success  Sample: `"www"` |
| **parent_id**  integer | ID of the parent  Returned: success |
| **prio**  integer | Priority of the record  Returned: success  Sample: `10` |
| **record_type**  string | Priority of the record  Returned: success  Sample: `"A"` |
| **system_record**  boolean | Whether the record is a system record or not  Returned: success  Sample: `false` |
| **ttl**  integer | Time to live of the record  Returned: success  Sample: `3600` |
| **updated_at**  string | When the record was updated  Returned: success  Sample: `"2016-08-12T15:24:23.989Z"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-exoscale/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-exoscale)
