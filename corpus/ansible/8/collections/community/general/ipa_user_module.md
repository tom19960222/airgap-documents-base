---
collection: ansible
version: "8"
title: "community.general.ipa_user module – Manage FreeIPA users"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ipa_user_module.html
fetched_at: 2026-07-28T01:46:47+00:00
---
# community.general.ipa_user module – Manage FreeIPA users

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](ipa_user_module.md#ansible-collections-community-general-ipa-user-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.ipa_user`.

- [Synopsis](ipa_user_module.md#synopsis)
- [Requirements](ipa_user_module.md#requirements)
- [Parameters](ipa_user_module.md#parameters)
- [Attributes](ipa_user_module.md#attributes)
- [Examples](ipa_user_module.md#examples)
- [Return Values](ipa_user_module.md#return-values)

## [Synopsis](ipa_user_module.md#id1)

- Add, modify and delete user within IPA server.

Aliases: identity.ipa.ipa_user

## [Requirements](ipa_user_module.md#id2)

The below requirements are needed on the host that executes this module.

- base64
- hashlib

## [Parameters](ipa_user_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **displayname**  string | Display name. |
| **gidnumber**  string | Posix Group ID. |
| **givenname**  string | First name.  If user does not exist and `state=present`, the usage of `givenname` is required. |
| **homedirectory**  string  *added in community.general 0.2.0* | Default home directory of the user. |
| **ipa_host**  string | IP or hostname of IPA server.  If the value is not specified in the task, the value of environment variable `IPA_HOST` will be used instead.  If both the environment variable `IPA_HOST` and the value are not specified in the task, then DNS will be used to try to discover the FreeIPA server.  The relevant entry needed in FreeIPA is the ‘ipa-ca’ entry.  If neither the DNS entry, nor the environment `IPA_HOST`, nor the value are available in the task, then the default value will be used.  Environment variable fallback mechanism is added in Ansible 2.5.  **Default:** `"ipa.example.com"` |
| **ipa_pass**  string | Password of administrative user.  If the value is not specified in the task, the value of environment variable `IPA_PASS` will be used instead.  Note that if the `urllib_gssapi` library is available, it is possible to use GSSAPI to authenticate to FreeIPA.  If the environment variable `KRB5CCNAME` is available, the module will use this kerberos credentials cache to authenticate to the FreeIPA server.  If the environment variable `KRB5_CLIENT_KTNAME` is available, and `KRB5CCNAME` is not; the module will use this kerberos keytab to authenticate.  If GSSAPI is not available, the usage of `ipa_pass` is required.  Environment variable fallback mechanism is added in Ansible 2.5. |
| **ipa_port**  integer | Port of FreeIPA / IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PORT` will be used instead.  If both the environment variable `IPA_PORT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  **Default:** `443` |
| **ipa_prot**  string | Protocol used by IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PROT` will be used instead.  If both the environment variable `IPA_PROT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **ipa_timeout**  integer | Specifies idle timeout (in seconds) for the connection.  For bulk operations, you may want to increase this in order to avoid timeout from IPA server.  If the value is not specified in the task, the value of environment variable `IPA_TIMEOUT` will be used instead.  If both the environment variable `IPA_TIMEOUT` and the value are not specified in the task, then default value is set.  **Default:** `10` |
| **ipa_user**  string | Administrative account used on IPA server.  If the value is not specified in the task, the value of environment variable `IPA_USER` will be used instead.  If both the environment variable `IPA_USER` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  **Default:** `"admin"` |
| **krbpasswordexpiration**  string | Date at which the user password will expire.  In the format YYYYMMddHHmmss.  e.g. 20180121182022 will expire on 21 January 2018 at 18:20:22. |
| **loginshell**  string | Login shell. |
| **mail**  list / elements=string | List of mail addresses assigned to the user.  If an empty list is passed all assigned email addresses will be deleted.  If None is passed email addresses will not be checked or changed. |
| **password**  string | Password for a user.  Will not be set for an existing user unless `update_password=always`, which is the default. |
| **sn**  string | Surname.  If user does not exist and `state=present`, the usage of `sn` is required. |
| **sshpubkey**  list / elements=string | List of public SSH key.  If an empty list is passed all assigned public keys will be deleted.  If None is passed SSH public keys will not be checked or changed. |
| **state**  string | State to ensure.  **Choices:**   - `"absent"` - `"disabled"` - `"enabled"` - `"present"` ← (default) |
| **telephonenumber**  list / elements=string | List of telephone numbers assigned to the user.  If an empty list is passed all assigned telephone numbers will be deleted.  If None is passed telephone numbers will not be checked or changed. |
| **title**  string | Title. |
| **uid**  aliases: name  string / required | uid of the user. |
| **uidnumber**  string | Account Settings UID/Posix User ID number. |
| **update_password**  string | Set password for a user.  **Choices:**   - `"always"` ← (default) - `"on_create"` |
| **userauthtype**  list / elements=string  *added in community.general 1.2.0* | The authentication type to use for the user.  **Choices:**   - `"password"` - `"radius"` - `"otp"` - `"pkinit"` - `"hardened"` |
| **validate_certs**  boolean | This only applies if `ipa_prot` is `https`.  If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](ipa_user_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](ipa_user_module.md#id5)

```yaml+jinja
- name: Ensure pinky is present and always reset password
  community.general.ipa_user:
    name: pinky
    state: present
    krbpasswordexpiration: 20200119235959
    givenname: Pinky
    sn: Acme
    mail:
    - pinky@acme.com
    telephonenumber:
    - '+555123456'
    sshpubkey:
    - ssh-rsa ....
    - ssh-dsa ....
    uidnumber: '1001'
    gidnumber: '100'
    homedirectory: /home/pinky
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Ensure brain is absent
  community.general.ipa_user:
    name: brain
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Ensure pinky is present but don't reset password if already exists
  community.general.ipa_user:
    name: pinky
    state: present
    givenname: Pinky
    sn: Acme
    password: zounds
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
    update_password: on_create

- name: Ensure pinky is present and using one time password and RADIUS authentication
  community.general.ipa_user:
    name: pinky
    state: present
    userauthtype:
      - otp
      - radius
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
```

## [Return Values](ipa_user_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **user**  dictionary | User as returned by IPA API  **Returned:** always |

### Authors

- Thomas Krahn (@Nosmoht)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
