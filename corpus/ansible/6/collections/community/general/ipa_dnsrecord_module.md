---
collection: ansible
version: "6"
title: "community.general.ipa_dnsrecord module – Manage FreeIPA DNS records"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ipa_dnsrecord_module.html
fetched_at: 2026-07-27T17:09:51+00:00
---
# community.general.ipa_dnsrecord module – Manage FreeIPA DNS records

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.ipa_dnsrecord`.

- [Synopsis](ipa_dnsrecord_module.md#synopsis)
- [Parameters](ipa_dnsrecord_module.md#parameters)
- [Examples](ipa_dnsrecord_module.md#examples)
- [Return Values](ipa_dnsrecord_module.md#return-values)

## [Synopsis](ipa_dnsrecord_module.md#id1)

- Add, modify and delete an IPA DNS Record using IPA API.

## [Parameters](ipa_dnsrecord_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ipa_host**  string | IP or hostname of IPA server.  If the value is not specified in the task, the value of environment variable `IPA_HOST` will be used instead.  If both the environment variable `IPA_HOST` and the value are not specified in the task, then DNS will be used to try to discover the FreeIPA server.  The relevant entry needed in FreeIPA is the ‘ipa-ca’ entry.  If neither the DNS entry, nor the environment `IPA_HOST`, nor the value are available in the task, then the default value will be used.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"ipa.example.com"` |
| **ipa_pass**  string | Password of administrative user.  If the value is not specified in the task, the value of environment variable `IPA_PASS` will be used instead.  Note that if the ‘urllib_gssapi’ library is available, it is possible to use GSSAPI to authenticate to FreeIPA.  If the environment variable `KRB5CCNAME` is available, the module will use this kerberos credentials cache to authenticate to the FreeIPA server.  If the environment variable `KRB5_CLIENT_KTNAME` is available, and `KRB5CCNAME` is not; the module will use this kerberos keytab to authenticate.  If GSSAPI is not available, the usage of ‘ipa_pass’ is required.  Environment variable fallback mechanism is added in Ansible 2.5. |
| **ipa_port**  integer | Port of FreeIPA / IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PORT` will be used instead.  If both the environment variable `IPA_PORT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `443` |
| **ipa_prot**  string | Protocol used by IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PROT` will be used instead.  If both the environment variable `IPA_PROT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Choices:   - `"http"` - `"https"` ← (default) |
| **ipa_timeout**  integer | Specifies idle timeout (in seconds) for the connection.  For bulk operations, you may want to increase this in order to avoid timeout from IPA server.  If the value is not specified in the task, the value of environment variable `IPA_TIMEOUT` will be used instead.  If both the environment variable `IPA_TIMEOUT` and the value are not specified in the task, then default value is set.  Default: `10` |
| **ipa_user**  string | Administrative account used on IPA server.  If the value is not specified in the task, the value of environment variable `IPA_USER` will be used instead.  If both the environment variable `IPA_USER` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"admin"` |
| **record_name**  aliases: name  string / required | The DNS record name to manage. |
| **record_ttl**  integer | Set the TTL for the record.  Applies only when adding a new or changing the value of *record_value* or *record_values*. |
| **record_type**  string | The type of DNS record name.  Currently, ‘A’, ‘AAAA’, ‘A6’, ‘CNAME’, ‘DNAME’, ‘PTR’, ‘TXT’, ‘SRV’ and ‘MX’ are supported.  ‘A6’, ‘CNAME’, ‘DNAME’ and ‘TXT’ are added in version 2.5.  ‘SRV’ and ‘MX’ are added in version 2.8.  Choices:   - `"A"` ← (default) - `"AAAA"` - `"A6"` - `"CNAME"` - `"DNAME"` - `"MX"` - `"PTR"` - `"SRV"` - `"TXT"` |
| **record_value**  string | Manage DNS record name with this value.  Mutually exclusive with *record_values*, and exactly one of *record_value* and *record_values* has to be specified.  Use *record_values* if you need to specify multiple values.  In the case of ‘A’ or ‘AAAA’ record types, this will be the IP address.  In the case of ‘A6’ record type, this will be the A6 Record data.  In the case of ‘CNAME’ record type, this will be the hostname.  In the case of ‘DNAME’ record type, this will be the DNAME target.  In the case of ‘PTR’ record type, this will be the hostname.  In the case of ‘TXT’ record type, this will be a text.  In the case of ‘SRV’ record type, this will be a service record.  In the case of ‘MX’ record type, this will be a mail exchanger record. |
| **record_values**  list / elements=string | Manage DNS record name with this value.  Mutually exclusive with *record_values*, and exactly one of *record_value* and *record_values* has to be specified.  In the case of ‘A’ or ‘AAAA’ record types, this will be the IP address.  In the case of ‘A6’ record type, this will be the A6 Record data.  In the case of ‘CNAME’ record type, this will be the hostname.  In the case of ‘DNAME’ record type, this will be the DNAME target.  In the case of ‘PTR’ record type, this will be the hostname.  In the case of ‘TXT’ record type, this will be a text.  In the case of ‘SRV’ record type, this will be a service record.  In the case of ‘MX’ record type, this will be a mail exchanger record. |
| **state**  string | State to ensure  Choices:   - `"absent"` - `"present"` ← (default) |
| **validate_certs**  boolean | This only applies if `ipa_prot` is *https*.  If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **zone_name**  string / required | The DNS zone name to which DNS record needs to be managed. |

## [Examples](ipa_dnsrecord_module.md#id3)

```yaml+jinja
- name: Ensure dns record is present
  community.general.ipa_dnsrecord:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: present
    zone_name: example.com
    record_name: vm-001
    record_type: 'AAAA'
    record_value: '::1'

- name: Ensure that dns records exists with a TTL
  community.general.ipa_dnsrecord:
    name: host02
    zone_name: example.com
    record_type: 'AAAA'
    record_values: '::1,fe80::1'
    record_ttl: 300
    ipa_host: ipa.example.com
    ipa_pass: topsecret
    state: present

- name: Ensure a PTR record is present
  community.general.ipa_dnsrecord:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: present
    zone_name: 2.168.192.in-addr.arpa
    record_name: 5
    record_type: 'PTR'
    record_value: 'internal.ipa.example.com'

- name: Ensure a TXT record is present
  community.general.ipa_dnsrecord:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: present
    zone_name: example.com
    record_name: _kerberos
    record_type: 'TXT'
    record_value: 'EXAMPLE.COM'

- name: Ensure an SRV record is present
  community.general.ipa_dnsrecord:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: present
    zone_name: example.com
    record_name: _kerberos._udp.example.com
    record_type: 'SRV'
    record_value: '10 50 88 ipa.example.com'

- name: Ensure an MX records are present
  community.general.ipa_dnsrecord:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: present
    zone_name: example.com
    record_name: '@'
    record_type: 'MX'
    record_values:
      - '1 mailserver-01.example.com'
      - '2 mailserver-02.example.com'

- name: Ensure that dns record is removed
  community.general.ipa_dnsrecord:
    name: host01
    zone_name: example.com
    record_type: 'AAAA'
    record_value: '::1'
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
    state: absent
```

## [Return Values](ipa_dnsrecord_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnsrecord**  dictionary | DNS record as returned by IPA API.  Returned: always |

### Authors

- Abhijeet Kasurde (@Akasurde)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
