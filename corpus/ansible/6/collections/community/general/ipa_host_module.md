---
collection: ansible
version: "6"
title: "community.general.ipa_host module – Manage FreeIPA host"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ipa_host_module.html
fetched_at: 2026-07-27T17:09:53+00:00
---
# community.general.ipa_host module – Manage FreeIPA host

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
> To use it in a playbook, specify: `community.general.ipa_host`.

- [Synopsis](ipa_host_module.md#synopsis)
- [Parameters](ipa_host_module.md#parameters)
- [Examples](ipa_host_module.md#examples)
- [Return Values](ipa_host_module.md#return-values)

## [Synopsis](ipa_host_module.md#id1)

- Add, modify and delete an IPA host using IPA API.

## [Parameters](ipa_host_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **description**  string | A description of this host. |
| **force**  boolean | Force host name even if not in DNS.  Choices:   - `false` - `true` |
| **fqdn**  aliases: name  string / required | Full qualified domain name.  Can not be changed as it is the unique identifier. |
| **ip_address**  string | Add the host to DNS with this IP address. |
| **ipa_host**  string | IP or hostname of IPA server.  If the value is not specified in the task, the value of environment variable `IPA_HOST` will be used instead.  If both the environment variable `IPA_HOST` and the value are not specified in the task, then DNS will be used to try to discover the FreeIPA server.  The relevant entry needed in FreeIPA is the ‘ipa-ca’ entry.  If neither the DNS entry, nor the environment `IPA_HOST`, nor the value are available in the task, then the default value will be used.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"ipa.example.com"` |
| **ipa_pass**  string | Password of administrative user.  If the value is not specified in the task, the value of environment variable `IPA_PASS` will be used instead.  Note that if the ‘urllib_gssapi’ library is available, it is possible to use GSSAPI to authenticate to FreeIPA.  If the environment variable `KRB5CCNAME` is available, the module will use this kerberos credentials cache to authenticate to the FreeIPA server.  If the environment variable `KRB5_CLIENT_KTNAME` is available, and `KRB5CCNAME` is not; the module will use this kerberos keytab to authenticate.  If GSSAPI is not available, the usage of ‘ipa_pass’ is required.  Environment variable fallback mechanism is added in Ansible 2.5. |
| **ipa_port**  integer | Port of FreeIPA / IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PORT` will be used instead.  If both the environment variable `IPA_PORT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `443` |
| **ipa_prot**  string | Protocol used by IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PROT` will be used instead.  If both the environment variable `IPA_PROT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Choices:   - `"http"` - `"https"` ← (default) |
| **ipa_timeout**  integer | Specifies idle timeout (in seconds) for the connection.  For bulk operations, you may want to increase this in order to avoid timeout from IPA server.  If the value is not specified in the task, the value of environment variable `IPA_TIMEOUT` will be used instead.  If both the environment variable `IPA_TIMEOUT` and the value are not specified in the task, then default value is set.  Default: `10` |
| **ipa_user**  string | Administrative account used on IPA server.  If the value is not specified in the task, the value of environment variable `IPA_USER` will be used instead.  If both the environment variable `IPA_USER` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"admin"` |
| **mac_address**  aliases: macaddress  list / elements=string | List of Hardware MAC address(es) off this host.  If option is omitted MAC addresses will not be checked or changed.  If an empty list is passed all assigned MAC addresses will be removed.  MAC addresses that are already assigned but not passed will be removed. |
| **ns_hardware_platform**  aliases: nshardwareplatform  string | Host hardware platform (e.g. “Lenovo T61”) |
| **ns_host_location**  aliases: nshostlocation  string | Host location (e.g. “Lab 2”) |
| **ns_os_version**  aliases: nsosversion  string | Host operating system and version (e.g. “Fedora 9”) |
| **random_password**  boolean | Generate a random password to be used in bulk enrollment.  Choices:   - `false` - `true` |
| **state**  string | State to ensure.  Choices:   - `"absent"` - `"disabled"` - `"enabled"` - `"present"` ← (default) |
| **update_dns**  boolean | If set `"True"` with state as `"absent"`, then removes DNS records of the host managed by FreeIPA DNS.  This option has no effect for states other than “absent”.  Choices:   - `false` - `true` |
| **user_certificate**  aliases: usercertificate  list / elements=string | List of Base-64 encoded server certificates.  If option is omitted certificates will not be checked or changed.  If an empty list is passed all assigned certificates will be removed.  Certificates already assigned but not passed will be removed. |
| **validate_certs**  boolean | This only applies if `ipa_prot` is *https*.  If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](ipa_host_module.md#id3)

```yaml+jinja
- name: Ensure host is present
  community.general.ipa_host:
    name: host01.example.com
    description: Example host
    ip_address: 192.168.0.123
    ns_host_location: Lab
    ns_os_version: CentOS 7
    ns_hardware_platform: Lenovo T61
    mac_address:
    - "08:00:27:E3:B1:2D"
    - "52:54:00:BD:97:1E"
    state: present
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Generate a random password for bulk enrolment
  community.general.ipa_host:
    name: host01.example.com
    description: Example host
    ip_address: 192.168.0.123
    state: present
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
    validate_certs: false
    random_password: true

- name: Ensure host is disabled
  community.general.ipa_host:
    name: host01.example.com
    state: disabled
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Ensure that all user certificates are removed
  community.general.ipa_host:
    name: host01.example.com
    user_certificate: []
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Ensure host is absent
  community.general.ipa_host:
    name: host01.example.com
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Ensure host and its DNS record is absent
  community.general.ipa_host:
    name: host01.example.com
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
    update_dns: true
```

## [Return Values](ipa_host_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **host**  dictionary | Host as returned by IPA API.  Returned: always |
| **host_diff**  list / elements=string | List of options that differ and would be changed  Returned: if check mode and a difference is found |

### Authors

- Thomas Krahn (@Nosmoht)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
