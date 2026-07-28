---
collection: ansible
version: "6"
title: "community.general.ipa_role module – Manage FreeIPA role"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ipa_role_module.html
fetched_at: 2026-07-27T17:09:57+00:00
---
# community.general.ipa_role module – Manage FreeIPA role

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
> To use it in a playbook, specify: `community.general.ipa_role`.

- [Synopsis](ipa_role_module.md#synopsis)
- [Parameters](ipa_role_module.md#parameters)
- [Examples](ipa_role_module.md#examples)
- [Return Values](ipa_role_module.md#return-values)

## [Synopsis](ipa_role_module.md#id1)

- Add, modify and delete a role within FreeIPA server using FreeIPA API.

## [Parameters](ipa_role_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cn**  aliases: name  string / required | Role name.  Can not be changed as it is the unique identifier. |
| **description**  string | A description of this role-group. |
| **group**  list / elements=string | List of group names assign to this role.  If an empty list is passed all assigned groups will be unassigned from the role.  If option is omitted groups will not be checked or changed.  If option is passed all assigned groups that are not passed will be unassigned from the role. |
| **host**  list / elements=string | List of host names to assign.  If an empty list is passed all assigned hosts will be unassigned from the role.  If option is omitted hosts will not be checked or changed.  If option is passed all assigned hosts that are not passed will be unassigned from the role. |
| **hostgroup**  list / elements=string | List of host group names to assign.  If an empty list is passed all assigned host groups will be removed from the role.  If option is omitted host groups will not be checked or changed.  If option is passed all assigned hostgroups that are not passed will be unassigned from the role. |
| **ipa_host**  string | IP or hostname of IPA server.  If the value is not specified in the task, the value of environment variable `IPA_HOST` will be used instead.  If both the environment variable `IPA_HOST` and the value are not specified in the task, then DNS will be used to try to discover the FreeIPA server.  The relevant entry needed in FreeIPA is the ‘ipa-ca’ entry.  If neither the DNS entry, nor the environment `IPA_HOST`, nor the value are available in the task, then the default value will be used.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"ipa.example.com"` |
| **ipa_pass**  string | Password of administrative user.  If the value is not specified in the task, the value of environment variable `IPA_PASS` will be used instead.  Note that if the ‘urllib_gssapi’ library is available, it is possible to use GSSAPI to authenticate to FreeIPA.  If the environment variable `KRB5CCNAME` is available, the module will use this kerberos credentials cache to authenticate to the FreeIPA server.  If the environment variable `KRB5_CLIENT_KTNAME` is available, and `KRB5CCNAME` is not; the module will use this kerberos keytab to authenticate.  If GSSAPI is not available, the usage of ‘ipa_pass’ is required.  Environment variable fallback mechanism is added in Ansible 2.5. |
| **ipa_port**  integer | Port of FreeIPA / IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PORT` will be used instead.  If both the environment variable `IPA_PORT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `443` |
| **ipa_prot**  string | Protocol used by IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PROT` will be used instead.  If both the environment variable `IPA_PROT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Choices:   - `"http"` - `"https"` ← (default) |
| **ipa_timeout**  integer | Specifies idle timeout (in seconds) for the connection.  For bulk operations, you may want to increase this in order to avoid timeout from IPA server.  If the value is not specified in the task, the value of environment variable `IPA_TIMEOUT` will be used instead.  If both the environment variable `IPA_TIMEOUT` and the value are not specified in the task, then default value is set.  Default: `10` |
| **ipa_user**  string | Administrative account used on IPA server.  If the value is not specified in the task, the value of environment variable `IPA_USER` will be used instead.  If both the environment variable `IPA_USER` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"admin"` |
| **privilege**  list / elements=string | List of privileges granted to the role.  If an empty list is passed all assigned privileges will be removed.  If option is omitted privileges will not be checked or changed.  If option is passed all assigned privileges that are not passed will be removed. |
| **service**  list / elements=string | List of service names to assign.  If an empty list is passed all assigned services will be removed from the role.  If option is omitted services will not be checked or changed.  If option is passed all assigned services that are not passed will be removed from the role. |
| **state**  string | State to ensure.  Choices:   - `"absent"` - `"present"` ← (default) |
| **user**  list / elements=string | List of user names to assign.  If an empty list is passed all assigned users will be removed from the role.  If option is omitted users will not be checked or changed. |
| **validate_certs**  boolean | This only applies if `ipa_prot` is *https*.  If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](ipa_role_module.md#id3)

```yaml+jinja
- name: Ensure role is present
  community.general.ipa_role:
    name: dba
    description: Database Administrators
    state: present
    user:
    - pinky
    - brain
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Ensure role with certain details
  community.general.ipa_role:
    name: another-role
    description: Just another role
    group:
    - editors
    host:
    - host01.example.com
    hostgroup:
    - hostgroup01
    privilege:
    - Group Administrators
    - User Administrators
    service:
    - service01

- name: Ensure role is absent
  community.general.ipa_role:
    name: dba
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
```

## [Return Values](ipa_role_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **role**  dictionary | Role as returned by IPA API.  Returned: always |

### Authors

- Thomas Krahn (@Nosmoht)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
