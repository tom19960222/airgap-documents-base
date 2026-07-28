---
collection: ansible
version: "6"
title: "community.general.ipa_config module – Manage Global FreeIPA Configuration Settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ipa_config_module.html
fetched_at: 2026-07-27T17:09:50+00:00
---
# community.general.ipa_config module – Manage Global FreeIPA Configuration Settings

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
> To use it in a playbook, specify: `community.general.ipa_config`.

- [Synopsis](ipa_config_module.md#synopsis)
- [Parameters](ipa_config_module.md#parameters)
- [Examples](ipa_config_module.md#examples)
- [Return Values](ipa_config_module.md#return-values)

## [Synopsis](ipa_config_module.md#id1)

- Modify global configuration settings of a FreeIPA Server.

## [Parameters](ipa_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **ipa_host**  string | IP or hostname of IPA server.  If the value is not specified in the task, the value of environment variable `IPA_HOST` will be used instead.  If both the environment variable `IPA_HOST` and the value are not specified in the task, then DNS will be used to try to discover the FreeIPA server.  The relevant entry needed in FreeIPA is the ‘ipa-ca’ entry.  If neither the DNS entry, nor the environment `IPA_HOST`, nor the value are available in the task, then the default value will be used.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"ipa.example.com"` |
| **ipa_pass**  string | Password of administrative user.  If the value is not specified in the task, the value of environment variable `IPA_PASS` will be used instead.  Note that if the ‘urllib_gssapi’ library is available, it is possible to use GSSAPI to authenticate to FreeIPA.  If the environment variable `KRB5CCNAME` is available, the module will use this kerberos credentials cache to authenticate to the FreeIPA server.  If the environment variable `KRB5_CLIENT_KTNAME` is available, and `KRB5CCNAME` is not; the module will use this kerberos keytab to authenticate.  If GSSAPI is not available, the usage of ‘ipa_pass’ is required.  Environment variable fallback mechanism is added in Ansible 2.5. |
| **ipa_port**  integer | Port of FreeIPA / IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PORT` will be used instead.  If both the environment variable `IPA_PORT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `443` |
| **ipa_prot**  string | Protocol used by IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PROT` will be used instead.  If both the environment variable `IPA_PROT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Choices:   - `"http"` - `"https"` ← (default) |
| **ipa_timeout**  integer | Specifies idle timeout (in seconds) for the connection.  For bulk operations, you may want to increase this in order to avoid timeout from IPA server.  If the value is not specified in the task, the value of environment variable `IPA_TIMEOUT` will be used instead.  If both the environment variable `IPA_TIMEOUT` and the value are not specified in the task, then default value is set.  Default: `10` |
| **ipa_user**  string | Administrative account used on IPA server.  If the value is not specified in the task, the value of environment variable `IPA_USER` will be used instead.  If both the environment variable `IPA_USER` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"admin"` |
| **ipaconfigstring**  aliases: configstring  list / elements=string  added in community.general 2.5.0 | Extra hashes to generate in password plug-in.  Choices:   - `"AllowNThash"` - `"KDC:Disable Last Success"` - `"KDC:Disable Lockout"` - `"KDC:Disable Default Preauth for SPNs"` |
| **ipadefaultemaildomain**  aliases: emaildomain  string | Default e-mail domain for new users. |
| **ipadefaultloginshell**  aliases: loginshell  string | Default shell for new users. |
| **ipadefaultprimarygroup**  aliases: primarygroup  string  added in community.general 2.5.0 | Default group for new users. |
| **ipagroupsearchfields**  aliases: groupsearchfields  list / elements=string  added in community.general 2.5.0 | A list of fields to search in when searching for groups. |
| **ipahomesrootdir**  aliases: homesrootdir  string  added in community.general 2.5.0 | Default location of home directories. |
| **ipakrbauthzdata**  aliases: krbauthzdata  list / elements=string  added in community.general 2.5.0 | Default types of PAC supported for services.  Choices:   - `"MS-PAC"` - `"PAD"` - `"nfs:NONE"` |
| **ipamaxusernamelength**  aliases: maxusernamelength  integer  added in community.general 2.5.0 | Maximum length of usernames. |
| **ipapwdexpadvnotify**  aliases: pwdexpadvnotify  integer  added in community.general 2.5.0 | Notice of impending password expiration, in days. |
| **ipasearchrecordslimit**  aliases: searchrecordslimit  integer  added in community.general 2.5.0 | Maximum number of records to search (-1 or 0 is unlimited). |
| **ipasearchtimelimit**  aliases: searchtimelimit  integer  added in community.general 2.5.0 | Maximum amount of time (seconds) for a search (-1 or 0 is unlimited). |
| **ipaselinuxusermaporder**  aliases: selinuxusermaporder  list / elements=string  added in community.general 3.7.0 | The SELinux user map order (order in increasing priority of SELinux users). |
| **ipauserauthtype**  aliases: userauthtype  list / elements=string  added in community.general 2.5.0 | The authentication type to use by default.  Choices:   - `"password"` - `"radius"` - `"otp"` - `"pkinit"` - `"hardened"` - `"disabled"` |
| **ipausersearchfields**  aliases: usersearchfields  list / elements=string  added in community.general 2.5.0 | A list of fields to search in when searching for users. |
| **validate_certs**  boolean | This only applies if `ipa_prot` is *https*.  If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](ipa_config_module.md#id3)

```yaml+jinja
- name: Ensure password plugin features DC:Disable Last Success and KDC:Disable Lockout are enabled
  community.general.ipa_config:
    ipaconfigstring: ["KDC:Disable Last Success", "KDC:Disable Lockout"]
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the default login shell is bash
  community.general.ipa_config:
    ipadefaultloginshell: /bin/bash
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the default e-mail domain is ansible.com
  community.general.ipa_config:
    ipadefaultemaildomain: ansible.com
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the default primary group is set to ipausers
  community.general.ipa_config:
    ipadefaultprimarygroup: ipausers
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the group search fields are set to 'cn,description'
  community.general.ipa_config:
    ipagroupsearchfields: ['cn', 'description']
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the home directory location is set to /home
  community.general.ipa_config:
    ipahomesrootdir: /home
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the default types of PAC supported for services is set to MS-PAC and PAD
  community.general.ipa_config:
    ipakrbauthzdata: ["MS-PAC", "PAD"]
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the maximum user name length is set to 32
  community.general.ipa_config:
    ipamaxusernamelength: 32
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the password expiration notice is set to 4 days
  community.general.ipa_config:
    ipapwdexpadvnotify: 4
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the search record limit is set to 100
  community.general.ipa_config:
    ipasearchrecordslimit: 100
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the search time limit is set to 2 seconds
  community.general.ipa_config:
    ipasearchtimelimit: 2
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the default user auth type is password
  community.general.ipa_config:
    ipauserauthtype: ['password']
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the user search fields is set to 'uid,givenname,sn,ou,title'
  community.general.ipa_config:
    ipausersearchfields: ['uid', 'givenname', 'sn', 'ou', 'title']
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret

- name: Ensure the SELinux user map order is set
  community.general.ipa_config:
    ipaselinuxusermaporder:
      - "guest_u:s0"
      - "xguest_u:s0"
      - "user_u:s0"
      - "staff_u:s0-s0:c0.c1023"
      - "unconfined_u:s0-s0:c0.c1023"
    ipa_host: localhost
    ipa_user: admin
    ipa_pass: supersecret
```

## [Return Values](ipa_config_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **config**  dictionary | Configuration as returned by IPA API.  Returned: always |

### Authors

- Fran Fitzpatrick (@fxfitz)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
