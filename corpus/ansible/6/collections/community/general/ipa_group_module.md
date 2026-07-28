---
collection: ansible
version: "6"
title: "community.general.ipa_group module – Manage FreeIPA group"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/ipa_group_module.html
fetched_at: 2026-07-27T17:09:52+00:00
---
# community.general.ipa_group module – Manage FreeIPA group

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
> To use it in a playbook, specify: `community.general.ipa_group`.

- [Synopsis](ipa_group_module.md#synopsis)
- [Parameters](ipa_group_module.md#parameters)
- [Examples](ipa_group_module.md#examples)
- [Return Values](ipa_group_module.md#return-values)

## [Synopsis](ipa_group_module.md#id1)

- Add, modify and delete group within IPA server

## [Parameters](ipa_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **append**  boolean  added in community.general 4.0.0 | If `true`, add the listed *user* and *group* to the group members.  If `false`, only the listed *user* and *group* will be group members, removing any other members.  Choices:   - `false` ← (default) - `true` |
| **cn**  aliases: name  string / required | Canonical name.  Can not be changed as it is the unique identifier. |
| **description**  string | Description of the group. |
| **external**  boolean | Allow adding external non-IPA members from trusted domains.  Choices:   - `false` - `true` |
| **gidnumber**  aliases: gid  string | GID (use this option to set it manually). |
| **group**  list / elements=string | List of group names assigned to this group.  If *append=false* and an empty list is passed all groups will be removed from this group.  Groups that are already assigned but not passed will be removed.  If *append=true* the listed groups will be assigned without removing other groups.  If option is omitted assigned groups will not be checked or changed. |
| **ipa_host**  string | IP or hostname of IPA server.  If the value is not specified in the task, the value of environment variable `IPA_HOST` will be used instead.  If both the environment variable `IPA_HOST` and the value are not specified in the task, then DNS will be used to try to discover the FreeIPA server.  The relevant entry needed in FreeIPA is the ‘ipa-ca’ entry.  If neither the DNS entry, nor the environment `IPA_HOST`, nor the value are available in the task, then the default value will be used.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"ipa.example.com"` |
| **ipa_pass**  string | Password of administrative user.  If the value is not specified in the task, the value of environment variable `IPA_PASS` will be used instead.  Note that if the ‘urllib_gssapi’ library is available, it is possible to use GSSAPI to authenticate to FreeIPA.  If the environment variable `KRB5CCNAME` is available, the module will use this kerberos credentials cache to authenticate to the FreeIPA server.  If the environment variable `KRB5_CLIENT_KTNAME` is available, and `KRB5CCNAME` is not; the module will use this kerberos keytab to authenticate.  If GSSAPI is not available, the usage of ‘ipa_pass’ is required.  Environment variable fallback mechanism is added in Ansible 2.5. |
| **ipa_port**  integer | Port of FreeIPA / IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PORT` will be used instead.  If both the environment variable `IPA_PORT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `443` |
| **ipa_prot**  string | Protocol used by IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PROT` will be used instead.  If both the environment variable `IPA_PROT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Choices:   - `"http"` - `"https"` ← (default) |
| **ipa_timeout**  integer | Specifies idle timeout (in seconds) for the connection.  For bulk operations, you may want to increase this in order to avoid timeout from IPA server.  If the value is not specified in the task, the value of environment variable `IPA_TIMEOUT` will be used instead.  If both the environment variable `IPA_TIMEOUT` and the value are not specified in the task, then default value is set.  Default: `10` |
| **ipa_user**  string | Administrative account used on IPA server.  If the value is not specified in the task, the value of environment variable `IPA_USER` will be used instead.  If both the environment variable `IPA_USER` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  Default: `"admin"` |
| **nonposix**  boolean | Create as a non-POSIX group.  Choices:   - `false` - `true` |
| **state**  string | State to ensure  Choices:   - `"absent"` - `"present"` ← (default) |
| **user**  list / elements=string | List of user names assigned to this group.  If *append=false* and an empty list is passed all users will be removed from this group.  Users that are already assigned but not passed will be removed.  If *append=true* the listed users will be assigned without removing other users.  If option is omitted assigned users will not be checked or changed. |
| **validate_certs**  boolean | This only applies if `ipa_prot` is *https*.  If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Examples](ipa_group_module.md#id3)

```yaml+jinja
- name: Ensure group is present
  community.general.ipa_group:
    name: oinstall
    gidnumber: '54321'
    state: present
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Ensure that groups sysops and appops are assigned to ops but no other group
  community.general.ipa_group:
    name: ops
    group:
    - sysops
    - appops
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Ensure that users linus and larry are assign to the group, but no other user
  community.general.ipa_group:
    name: sysops
    user:
    - linus
    - larry
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Ensure that new starter named john is member of the group, without removing other members
  community.general.ipa_group:
    name: developers
    user:
    - john
    append: true
    state: present
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Ensure group is absent
  community.general.ipa_group:
    name: sysops
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
```

## [Return Values](ipa_group_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **group**  dictionary | Group as returned by IPA API  Returned: always |

### Authors

- Thomas Krahn (@Nosmoht)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
