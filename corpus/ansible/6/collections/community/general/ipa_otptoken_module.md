---
collection: ansible
version: "6"
title: "community.general.ipa_otptoken module – Manage FreeIPA OTPs"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ipa_otptoken_module.html
fetched_at: 2026-07-27T17:09:55+00:00
---
# community.general.ipa_otptoken module – Manage FreeIPA OTPs

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
> To use it in a playbook, specify: `community.general.ipa_otptoken`.

New in community.general 2.5.0

- [Synopsis](ipa_otptoken_module.md#synopsis)
- [Parameters](ipa_otptoken_module.md#parameters)
- [Examples](ipa_otptoken_module.md#examples)
- [Return Values](ipa_otptoken_module.md#return-values)

## [Synopsis](ipa_otptoken_module.md#id1)

- Add, modify, and delete One Time Passwords in IPA.

## [Parameters](ipa_otptoken_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **algorithm**  string | Token hash algorithm.  **Note:** Cannot be modified after OTP is created.  Choices:   - `"sha1"` - `"sha256"` - `"sha384"` - `"sha512"` |
| **counter**  integer | Initial counter for the HOTP token.  **Note:** Cannot be modified after OTP is created. |
| **description**  string | Description of the token (informational only). |
| **digits**  integer | Number of digits each token code will have.  **Note:** Cannot be modified after OTP is created.  Choices:   - `6` - `8` |
| **enabled**  boolean | Mark the token as enabled (default `true`).  Choices:   - `false` - `true` ← (default) |
| **interval**  integer | Length of TOTP token code validity in seconds.  **Note:** Cannot be modified after OTP is created. |
| **ipa_host**  string | IP or hostname of IPA server.  If the value is not specified in the task, the value of environment variable `IPA_HOST` will be used instead.  If both the environment variable `IPA_HOST` and the value are not specified in the task, then DNS will be used to try to discover the FreeIPA server.  The relevant entry needed in FreeIPA is the ‘ipa-ca’ entry.  If neither the DNS entry, nor the environment `IPA_HOST`, nor the value are available in the task, then the default value will be used.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"ipa.example.com"` |
| **ipa_pass**  string | Password of administrative user.  If the value is not specified in the task, the value of environment variable `IPA_PASS` will be used instead.  Note that if the ‘urllib_gssapi’ library is available, it is possible to use GSSAPI to authenticate to FreeIPA.  If the environment variable `KRB5CCNAME` is available, the module will use this kerberos credentials cache to authenticate to the FreeIPA server.  If the environment variable `KRB5_CLIENT_KTNAME` is available, and `KRB5CCNAME` is not; the module will use this kerberos keytab to authenticate.  If GSSAPI is not available, the usage of ‘ipa_pass’ is required.  Environment variable fallback mechanism is added in Ansible 2.5. |
| **ipa_port**  integer | Port of FreeIPA / IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PORT` will be used instead.  If both the environment variable `IPA_PORT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `443` |
| **ipa_prot**  string | Protocol used by IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PROT` will be used instead.  If both the environment variable `IPA_PROT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Choices:   - `"http"` - `"https"` ← (default) |
| **ipa_timeout**  integer | Specifies idle timeout (in seconds) for the connection.  For bulk operations, you may want to increase this in order to avoid timeout from IPA server.  If the value is not specified in the task, the value of environment variable `IPA_TIMEOUT` will be used instead.  If both the environment variable `IPA_TIMEOUT` and the value are not specified in the task, then default value is set.  Default: `10` |
| **ipa_user**  string | Administrative account used on IPA server.  If the value is not specified in the task, the value of environment variable `IPA_USER` will be used instead.  If both the environment variable `IPA_USER` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"admin"` |
| **model**  string | Token model (informational only). |
| **newuniqueid**  string | If specified, the unique id specified will be changed to this. |
| **notafter**  string | Last date/time the token can be used.  In the format `YYYYMMddHHmmss`.  For example, `20200121182022` will allow the token to be used until 21 January 2020 at 18:20:22. |
| **notbefore**  string | First date/time the token can be used.  In the format `YYYYMMddHHmmss`.  For example, `20180121182022` will allow the token to be used starting on 21 January 2018 at 18:20:22. |
| **offset**  integer | TOTP token / IPA server time difference.  **Note:** Cannot be modified after OTP is created. |
| **otptype**  string | Type of OTP.  **Note:** Cannot be modified after OTP is created.  Choices:   - `"totp"` - `"hotp"` |
| **owner**  string | Assigned user of the token. |
| **secretkey**  string | Token secret (Base64).  If OTP is created and this is not specified, a random secret will be generated by IPA.  **Note:** Cannot be modified after OTP is created. |
| **serial**  string | Token serial (informational only). |
| **state**  string | State to ensure.  Choices:   - `"present"` ← (default) - `"absent"` |
| **uniqueid**  aliases: name  string / required | Unique ID of the token in IPA. |
| **validate_certs**  boolean | This only applies if `ipa_prot` is *https*.  If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |
| **vendor**  string | Token vendor name (informational only). |

## [Examples](ipa_otptoken_module.md#id3)

```yaml+jinja
- name: Create a totp for pinky, allowing the IPA server to generate using defaults
  community.general.ipa_otptoken:
    uniqueid: Token123
    otptype: totp
    owner: pinky
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Create a 8 digit hotp for pinky with sha256 with specified validity times
  community.general.ipa_otptoken:
    uniqueid: Token123
    enabled: true
    otptype: hotp
    digits: 8
    secretkey: UMKSIER00zT2T2tWMUlTRmNlekRCbFQvWFBVZUh2dElHWGR6T3VUR3IzK2xjaFk9
    algorithm: sha256
    notbefore: 20180121182123
    notafter: 20220121182123
    owner: pinky
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Update Token123 to indicate a vendor, model, serial number (info only), and description
  community.general.ipa_otptoken:
    uniqueid: Token123
    vendor: Acme
    model: acme101
    serial: SerialNumber1
    description: Acme OTP device
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Disable Token123
  community.general.ipa_otptoken:
    uniqueid: Token123
    enabled: false
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Rename Token123 to TokenABC and enable it
  community.general.ipa_otptoken:
    uniqueid: Token123
    newuniqueid: TokenABC
    enabled: true
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
```

## [Return Values](ipa_otptoken_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **otptoken**  dictionary | OTP Token as returned by IPA API  Returned: always |

### Authors

- justchris1 (@justchris1)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
