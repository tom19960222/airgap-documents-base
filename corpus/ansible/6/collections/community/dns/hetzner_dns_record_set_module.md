---
collection: ansible
version: "6"
title: "community.dns.hetzner_dns_record_set module – Add or delete record sets in Hetzner DNS service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/dns/hetzner_dns_record_set_module.html
fetched_at: 2026-07-27T17:07:04+00:00
---
# community.dns.hetzner_dns_record_set module – Add or delete record sets in Hetzner DNS service

> **Note:**
>
> This module is part of the [community.dns collection](https://galaxy.ansible.com/community/dns) (version 2.4.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.dns`.
>
> To use it in a playbook, specify: `community.dns.hetzner_dns_record_set`.

New in community.dns 2.0.0

- [Synopsis](hetzner_dns_record_set_module.md#synopsis)
- [Parameters](hetzner_dns_record_set_module.md#parameters)
- [Attributes](hetzner_dns_record_set_module.md#attributes)
- [Examples](hetzner_dns_record_set_module.md#examples)
- [Return Values](hetzner_dns_record_set_module.md#return-values)

## [Synopsis](hetzner_dns_record_set_module.md#id1)

- Creates and deletes DNS record sets in Hetzner DNS service.

## [Parameters](hetzner_dns_record_set_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **bulk_operation_threshold**  integer | Determines the threshold from when on bulk operations are used.  The default value 2 means that if 2 or more operations of a kind are planned, and the API supports bulk operations for this kind of operation, they will be used.  Default: `2` |
| **hetzner_token**  aliases: api_token  string / required | The token for the Hetzner API.  If not provided, will be read from the environment variable `HETZNER_DNS_TOKEN`. |
| **on_existing**  string | This option defines the behavior if the record set already exists, but differs from the specified record set. For this comparison, *value* and *ttl* are used for all records of type *type* matching the *prefix* resp. *record*.  If set to `replace`, the record will be updated (*state=present*) or removed (*state=absent*). This is the old *overwrite=true* behavior.  If set to `keep_and_fail`, the module will fail and not modify the records. This is the old *overwrite=false* behavior if *state=present*.  If set to `keep_and_warn`, the module will warn and not modify the records.  If set to `keep`, the module will not modify the records. This is the old *overwrite=false* behavior if *state=absent*.  If *state=absent* and the value is not `replace`, *value* must be specified.  Choices:   - `"replace"` ← (default) - `"keep_and_fail"` - `"keep_and_warn"` - `"keep"` |
| **prefix**  aliases: name  string  added in community.dns 0.2.0 | The prefix of the DNS record.  This is the part of *record* before *zone_name*. For example, if the record to be modified is `www.example.com` for the zone `example.com`, the prefix is `www`. If the record in this example would be `example.com`, the prefix would be `''` (empty string).  Exactly one of *record* and *prefix* must be specified. |
| **record**  string | The full DNS record to create or delete.  Exactly one of *record* and *prefix* must be specified. |
| **state**  string / required | Specifies the state of the resource record.  Choices:   - `"present"` - `"absent"` |
| **ttl**  integer | The TTL to give the new record, in seconds.  Will be ignored if *state=absent* and *on_existing=replace*. |
| **txt_transformation**  string | Determines how TXT entry values are converted between the API and this module’s input and output.  The value `api` means that values are returned from this module as they are returned from the API, and pushed to the API as they have been passed to this module. For idempotency checks, the input string will be compared to the strings returned by the API. The API might automatically transform some values, like splitting long values or adding quotes, which can cause problems with idempotency.  The value `unquoted` automatically transforms values so that you can pass in unquoted values, and the module will return unquoted values. If you pass in quoted values, they will be double-quoted.  The value `quoted` automatically transforms values so that you must use quoting for values that contain spaces, characters such as quotation marks and backslashes, and that are longer than 255 bytes. It also makes sure to return values from the API in a normalized encoding.  The default value, `unquoted`, ensures that you can work with values without having to care about how to correctly quote for DNS. Most users should use one of `unquoted` or `quoted`, but not `api`.  **Note:** the conversion code assumes UTF-8 encoding for values. If you need another encoding use *txt_transformation=api* and handle the encoding yourself.  Choices:   - `"api"` - `"quoted"` - `"unquoted"` ← (default) |
| **type**  string / required | The type of DNS record to create or delete.  Choices:   - `"A"` - `"AAAA"` - `"CAA"` - `"CNAME"` - `"DANE"` - `"DS"` - `"HINFO"` - `"MX"` - `"NS"` - `"RP"` - `"SOA"` - `"SRV"` - `"TLSA"` - `"TXT"` |
| **value**  list / elements=string | The new value when creating a DNS record.  YAML lists or multiple comma-spaced values are allowed.  When deleting a record all values for the record must be specified or it will not be deleted.  Must be specified if *state=present* or when *on_existing* is not `replace`.  Will be ignored if *state=absent* and *on_existing=replace*. |
| **zone_id**  string  added in community.dns 0.2.0 | The ID of the DNS zone to modify.  Exactly one of *zone_name* and *zone_id* must be specified. |
| **zone_name**  aliases: zone  string | The DNS zone to modify.  Exactly one of *zone_name* and *zone_id* must be specified. |

## [Attributes](hetzner_dns_record_set_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **action_group** | Action group: community.dns.hetzner  added in community.dns 2.4.0 | Use `group/community.dns.hetzner` in `module_defaults` to set defaults for this module. |
| **check_mode** | Support: full | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | Support: full | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](hetzner_dns_record_set_module.md#id4)

```yaml+jinja
- name: Add new.foo.com as an A record with 3 IPs
  community.dns.hetzner_dns_record_set:
    state: present
    zone: foo.com
    record: new.foo.com
    type: A
    ttl: 7200
    value: 1.1.1.1,2.2.2.2,3.3.3.3
    hetzner_token: access_token

- name: Update new.foo.com as an A record with a list of 3 IPs
  community.dns.hetzner_dns_record_set:
    state: present
    zone: foo.com
    record: new.foo.com
    type: A
    ttl: 7200
    value:
      - 1.1.1.1
      - 2.2.2.2
      - 3.3.3.3
    hetzner_token: access_token

- name: Retrieve the details for new.foo.com
  community.dns.hetzner_dns_record_set_info:
    zone: foo.com
    record: new.foo.com
    type: A
    hetzner_token: access_token
  register: rec

- name: Delete new.foo.com A record using the results from the facts retrieval command
  community.dns.hetzner_dns_record_set:
    state: absent
    zone: foo.com
    record: "{{ rec.set.record }}"
    ttl: "{{ rec.set.ttl }}"
    type: "{{ rec.set.type }}"
    value: "{{ rec.set.value }}"
    hetzner_token: access_token

- name: Add an AAAA record
  # Note that because there are colons in the value that the IPv6 address must be quoted!
  community.dns.hetzner_dns_record_set:
    state: present
    zone: foo.com
    record: localhost.foo.com
    type: AAAA
    ttl: 7200
    value: "::1"
    hetzner_token: access_token

- name: Add a TXT record
  community.dns.hetzner_dns_record_set:
    state: present
    zone: foo.com
    record: localhost.foo.com
    type: TXT
    ttl: 7200
    value: 'bar'
    hetzner_token: access_token

- name: Remove the TXT record
  community.dns.hetzner_dns_record_set:
    state: absent
    zone: foo.com
    record: localhost.foo.com
    type: TXT
    ttl: 7200
    value: 'bar'
    hetzner_token: access_token

- name: Add a CAA record
  community.dns.hetzner_dns_record_set:
    state: present
    zone: foo.com
    record: foo.com
    type: CAA
    ttl: 3600
    value:
    - "128 issue letsencrypt.org"
    - "128 iodef mailto:webmaster@foo.com"
    hetzner_token: access_token

- name: Add an MX record
  community.dns.hetzner_dns_record_set:
    state: present
    zone: foo.com
    record: foo.com
    type: MX
    ttl: 3600
    value:
    - "10 mail.foo.com"
    hetzner_token: access_token

- name: Add a CNAME record
  community.dns.hetzner_dns_record_set:
    state: present
    zone: bla.foo.com
    record: foo.com
    type: CNAME
    ttl: 3600
    value:
    - foo.foo.com
    hetzner_token: access_token

- name: Add a PTR record
  community.dns.hetzner_dns_record_set:
    state: present
    zone: foo.foo.com
    record: foo.com
    type: PTR
    ttl: 3600
    value:
    - foo.foo.com
    hetzner_token: access_token

- name: Add an SPF record
  community.dns.hetzner_dns_record_set:
    state: present
    zone: foo.com
    record: foo.com
    type: SPF
    ttl: 3600
    value:
    - "v=spf1 a mx ~all"
    hetzner_token: access_token

- name: Add a PTR record
  community.dns.hetzner_dns_record_set:
    state: present
    zone: foo.com
    record: foo.com
    type: PTR
    ttl: 3600
    value:
    - "10 100 3333 service.foo.com"
    hetzner_token: access_token
```

## [Return Values](hetzner_dns_record_set_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **zone_id**  string | The ID of the zone.  Returned: success  Sample: `"23"` |

### Authors

- Markus Bergholz (@markuman)
- Felix Fontein (@felixfontein)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.dns/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.dns)
[Submit a bug report](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.dns/issues/new?assignees=&labels=&template=feature_request.md)
[Communication](index.md#communication-for-community-dns)
