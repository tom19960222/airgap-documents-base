---
collection: ansible
version: "8"
title: "community.general.ipa_otpconfig module – Manage FreeIPA OTP Configuration Settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ipa_otpconfig_module.html
fetched_at: 2026-07-28T01:46:40+00:00
---
# community.general.ipa_otpconfig module – Manage FreeIPA OTP Configuration Settings

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
> To use it in a playbook, specify: `community.general.ipa_otpconfig`.

New in community.general 2.5.0

- [Synopsis](ipa_otpconfig_module.md#synopsis)
- [Parameters](ipa_otpconfig_module.md#parameters)
- [Attributes](ipa_otpconfig_module.md#attributes)
- [Examples](ipa_otpconfig_module.md#examples)
- [Return Values](ipa_otpconfig_module.md#return-values)

## [Synopsis](ipa_otpconfig_module.md#id1)

- Modify global configuration settings of a FreeIPA Server with respect to OTP (One Time Passwords).

Aliases: identity.ipa.ipa_otpconfig

## [Parameters](ipa_otpconfig_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ipa_host**  string | IP or hostname of IPA server.  If the value is not specified in the task, the value of environment variable `IPA_HOST` will be used instead.  If both the environment variable `IPA_HOST` and the value are not specified in the task, then DNS will be used to try to discover the FreeIPA server.  The relevant entry needed in FreeIPA is the ‘ipa-ca’ entry.  If neither the DNS entry, nor the environment `IPA_HOST`, nor the value are available in the task, then the default value will be used.  Environment variable fallback mechanism is added in Ansible 2.5.  **Default:** `"ipa.example.com"` |
| **ipa_pass**  string | Password of administrative user.  If the value is not specified in the task, the value of environment variable `IPA_PASS` will be used instead.  Note that if the `urllib_gssapi` library is available, it is possible to use GSSAPI to authenticate to FreeIPA.  If the environment variable `KRB5CCNAME` is available, the module will use this kerberos credentials cache to authenticate to the FreeIPA server.  If the environment variable `KRB5_CLIENT_KTNAME` is available, and `KRB5CCNAME` is not; the module will use this kerberos keytab to authenticate.  If GSSAPI is not available, the usage of `ipa_pass` is required.  Environment variable fallback mechanism is added in Ansible 2.5. |
| **ipa_port**  integer | Port of FreeIPA / IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PORT` will be used instead.  If both the environment variable `IPA_PORT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  **Default:** `443` |
| **ipa_prot**  string | Protocol used by IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PROT` will be used instead.  If both the environment variable `IPA_PROT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **ipa_timeout**  integer | Specifies idle timeout (in seconds) for the connection.  For bulk operations, you may want to increase this in order to avoid timeout from IPA server.  If the value is not specified in the task, the value of environment variable `IPA_TIMEOUT` will be used instead.  If both the environment variable `IPA_TIMEOUT` and the value are not specified in the task, then default value is set.  **Default:** `10` |
| **ipa_user**  string | Administrative account used on IPA server.  If the value is not specified in the task, the value of environment variable `IPA_USER` will be used instead.  If both the environment variable `IPA_USER` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  **Default:** `"admin"` |
| **ipatokenhotpauthwindow**  aliases: hotpauthwindow  integer | HOTP authentication window in number of hops. |
| **ipatokenhotpsyncwindow**  aliases: hotpsyncwindow  integer | HOTP synchronization window in hops. |
| **ipatokentotpauthwindow**  aliases: totpauthwindow  integer | TOTP authentication window in seconds. |
| **ipatokentotpsyncwindow**  aliases: totpsyncwindow  integer | TOTP synchronization window in seconds. |
| **validate_certs**  boolean | This only applies if `ipa_prot` is `https`.  If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](ipa_otpconfig_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](ipa_otpconfig_module.md#id4)

```yaml+jinja
- name: Ensure the TOTP authentication window is set to 300 seconds
  community.general.ipa_otpconfig:
    ipatokentotpauthwindow: '300'
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the TOTP synchronization window is set to 86400 seconds
  community.general.ipa_otpconfig:
    ipatokentotpsyncwindow: '86400'
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the HOTP authentication window is set to 10 hops
  community.general.ipa_otpconfig:
    ipatokenhotpauthwindow: '10'
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the HOTP synchronization window is set to 100 hops
  community.general.ipa_otpconfig:
    ipatokenhotpsyncwindow: '100'
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret
```

## [Return Values](ipa_otpconfig_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **otpconfig**  dictionary | OTP configuration as returned by IPA API.  **Returned:** always |

### Authors

- justchris1 (@justchris1)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
