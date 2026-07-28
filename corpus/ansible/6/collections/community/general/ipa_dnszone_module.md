---
collection: ansible
version: "6"
title: "community.general.ipa_dnszone module – Manage FreeIPA DNS Zones"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ipa_dnszone_module.html
fetched_at: 2026-07-27T17:09:51+00:00
---
# community.general.ipa_dnszone module – Manage FreeIPA DNS Zones

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
> To use it in a playbook, specify: `community.general.ipa_dnszone`.

- [Synopsis](ipa_dnszone_module.md#synopsis)
- [Parameters](ipa_dnszone_module.md#parameters)
- [Examples](ipa_dnszone_module.md#examples)
- [Return Values](ipa_dnszone_module.md#return-values)

## [Synopsis](ipa_dnszone_module.md#id1)

- Add and delete an IPA DNS Zones using IPA API

## [Parameters](ipa_dnszone_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **allowsyncptr**  boolean  added in community.general 4.3.0 | Allow synchronization of forward and reverse records in the zone.  Choices:   - `false` ← (default) - `true` |
| **dynamicupdate**  boolean | Apply dynamic update to zone.  Choices:   - `false` ← (default) - `true` |
| **ipa_host**  string | IP or hostname of IPA server.  If the value is not specified in the task, the value of environment variable `IPA_HOST` will be used instead.  If both the environment variable `IPA_HOST` and the value are not specified in the task, then DNS will be used to try to discover the FreeIPA server.  The relevant entry needed in FreeIPA is the ‘ipa-ca’ entry.  If neither the DNS entry, nor the environment `IPA_HOST`, nor the value are available in the task, then the default value will be used.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"ipa.example.com"` |
| **ipa_pass**  string | Password of administrative user.  If the value is not specified in the task, the value of environment variable `IPA_PASS` will be used instead.  Note that if the ‘urllib_gssapi’ library is available, it is possible to use GSSAPI to authenticate to FreeIPA.  If the environment variable `KRB5CCNAME` is available, the module will use this kerberos credentials cache to authenticate to the FreeIPA server.  If the environment variable `KRB5_CLIENT_KTNAME` is available, and `KRB5CCNAME` is not; the module will use this kerberos keytab to authenticate.  If GSSAPI is not available, the usage of ‘ipa_pass’ is required.  Environment variable fallback mechanism is added in Ansible 2.5. |
| **ipa_port**  integer | Port of FreeIPA / IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PORT` will be used instead.  If both the environment variable `IPA_PORT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `443` |
| **ipa_prot**  string | Protocol used by IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PROT` will be used instead.  If both the environment variable `IPA_PROT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Choices:   - `"http"` - `"https"` ← (default) |
| **ipa_timeout**  integer | Specifies idle timeout (in seconds) for the connection.  For bulk operations, you may want to increase this in order to avoid timeout from IPA server.  If the value is not specified in the task, the value of environment variable `IPA_TIMEOUT` will be used instead.  If both the environment variable `IPA_TIMEOUT` and the value are not specified in the task, then default value is set.  Default: `10` |
| **ipa_user**  string | Administrative account used on IPA server.  If the value is not specified in the task, the value of environment variable `IPA_USER` will be used instead.  If both the environment variable `IPA_USER` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"admin"` |
| **state**  string | State to ensure  Choices:   - `"absent"` - `"present"` ← (default) |
| **validate_certs**  boolean | This only applies if `ipa_prot` is *https*.  If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **zone_name**  string / required | The DNS zone name to which needs to be managed. |

## [Examples](ipa_dnszone_module.md#id3)

```yaml+jinja
- name: Ensure dns zone is present
  community.general.ipa_dnszone:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: present
    zone_name: example.com

- name: Ensure dns zone is present and is dynamic update
  community.general.ipa_dnszone:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: present
    zone_name: example.com
    dynamicupdate: true

- name: Ensure that dns zone is removed
  community.general.ipa_dnszone:
    zone_name: example.com
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: topsecret
    state: absent

- name: Ensure dns zone is present and is allowing sync
  community.general.ipa_dnszone:
    ipa_host: spider.example.com
    ipa_pass: Passw0rd!
    state: present
    zone_name: example.com
    allowsyncptr: true
```

## [Return Values](ipa_dnszone_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **zone**  dictionary | DNS zone as returned by IPA API.  Returned: always |

### Authors

- Fran Fitzpatrick (@fxfitz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
