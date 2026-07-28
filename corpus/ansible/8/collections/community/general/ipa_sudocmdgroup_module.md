---
collection: ansible
version: "8"
title: "community.general.ipa_sudocmdgroup module – Manage FreeIPA sudo command group"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ipa_sudocmdgroup_module.html
fetched_at: 2026-07-28T01:46:45+00:00
---
# community.general.ipa_sudocmdgroup module – Manage FreeIPA sudo command group

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
> To use it in a playbook, specify: `community.general.ipa_sudocmdgroup`.

- [Synopsis](ipa_sudocmdgroup_module.md#synopsis)
- [Parameters](ipa_sudocmdgroup_module.md#parameters)
- [Attributes](ipa_sudocmdgroup_module.md#attributes)
- [Examples](ipa_sudocmdgroup_module.md#examples)
- [Return Values](ipa_sudocmdgroup_module.md#return-values)

## [Synopsis](ipa_sudocmdgroup_module.md#id1)

- Add, modify or delete sudo command group within IPA server using IPA API.

Aliases: identity.ipa.ipa_sudocmdgroup

## [Parameters](ipa_sudocmdgroup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cn**  aliases: name  string / required | Sudo Command Group. |
| **description**  string | Group description. |
| **ipa_host**  string | IP or hostname of IPA server.  If the value is not specified in the task, the value of environment variable `IPA_HOST` will be used instead.  If both the environment variable `IPA_HOST` and the value are not specified in the task, then DNS will be used to try to discover the FreeIPA server.  The relevant entry needed in FreeIPA is the ‘ipa-ca’ entry.  If neither the DNS entry, nor the environment `IPA_HOST`, nor the value are available in the task, then the default value will be used.  Environment variable fallback mechanism is added in Ansible 2.5.  **Default:** `"ipa.example.com"` |
| **ipa_pass**  string | Password of administrative user.  If the value is not specified in the task, the value of environment variable `IPA_PASS` will be used instead.  Note that if the `urllib_gssapi` library is available, it is possible to use GSSAPI to authenticate to FreeIPA.  If the environment variable `KRB5CCNAME` is available, the module will use this kerberos credentials cache to authenticate to the FreeIPA server.  If the environment variable `KRB5_CLIENT_KTNAME` is available, and `KRB5CCNAME` is not; the module will use this kerberos keytab to authenticate.  If GSSAPI is not available, the usage of `ipa_pass` is required.  Environment variable fallback mechanism is added in Ansible 2.5. |
| **ipa_port**  integer | Port of FreeIPA / IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PORT` will be used instead.  If both the environment variable `IPA_PORT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  **Default:** `443` |
| **ipa_prot**  string | Protocol used by IPA server.  If the value is not specified in the task, the value of environment variable `IPA_PROT` will be used instead.  If both the environment variable `IPA_PROT` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **ipa_timeout**  integer | Specifies idle timeout (in seconds) for the connection.  For bulk operations, you may want to increase this in order to avoid timeout from IPA server.  If the value is not specified in the task, the value of environment variable `IPA_TIMEOUT` will be used instead.  If both the environment variable `IPA_TIMEOUT` and the value are not specified in the task, then default value is set.  **Default:** `10` |
| **ipa_user**  string | Administrative account used on IPA server.  If the value is not specified in the task, the value of environment variable `IPA_USER` will be used instead.  If both the environment variable `IPA_USER` and the value are not specified in the task, then default value is set.  Environment variable fallback mechanism is added in Ansible 2.5.  **Default:** `"admin"` |
| **state**  string | State to ensure.  **Choices:**   - `"absent"` - `"disabled"` - `"enabled"` - `"present"` ← (default) |
| **sudocmd**  list / elements=string | List of sudo commands to assign to the group.  If an empty list is passed all assigned commands will be removed from the group.  If option is omitted sudo commands will not be checked or changed. |
| **validate_certs**  boolean | This only applies if `ipa_prot` is `https`.  If set to `false`, the SSL certificates will not be validated.  This should only set to `false` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](ipa_sudocmdgroup_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Examples](ipa_sudocmdgroup_module.md#id4)

```yaml+jinja
- name: Ensure sudo command group exists
  community.general.ipa_sudocmdgroup:
    name: group01
    description: Group of important commands
    sudocmd:
    - su
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret

- name: Ensure sudo command group does not exist
  community.general.ipa_sudocmdgroup:
    name: group01
    state: absent
    ipa_host: ipa.example.com
    ipa_user: admin
    ipa_pass: topsecret
```

## [Return Values](ipa_sudocmdgroup_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **sudocmdgroup**  dictionary | Sudo command group as returned by IPA API  **Returned:** always |

### Authors

- Thomas Krahn (@Nosmoht)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
