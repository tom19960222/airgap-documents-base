---
collection: ansible
version: "8"
title: "purestorage.flasharray.purefa_ds module – Configure FlashArray Directory Service"
source_url: https://docs.ansible.com/projects/ansible/8/collections/purestorage/flasharray/purefa_ds_module.html
fetched_at: 2026-07-28T02:50:50+00:00
---
# purestorage.flasharray.purefa_ds module – Configure FlashArray Directory Service

> **Note:**
>
> This module is part of the [purestorage.flasharray collection](https://galaxy.ansible.com/ui/repo/published/purestorage/flasharray/) (version 1.24.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flasharray`.
> You need further requirements to be able to use this module,
> see [Requirements](purefa_ds_module.md#ansible-collections-purestorage-flasharray-purefa-ds-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flasharray.purefa_ds`.

New in purestorage.flasharray 1.0.0

- [Synopsis](purefa_ds_module.md#synopsis)
- [Requirements](purefa_ds_module.md#requirements)
- [Parameters](purefa_ds_module.md#parameters)
- [Notes](purefa_ds_module.md#notes)
- [Examples](purefa_ds_module.md#examples)

## [Synopsis](purefa_ds_module.md#id1)

- Set or erase configuration for the directory service. There is no facility to SSL certificates at this time. Use the FlashArray GUI for this additional configuration work.
- To modify an existing directory service configuration you must first delete an exisitng configuration and then recreate with new settings.

## [Requirements](purefa_ds_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.3
- purestorage >= 1.19
- py-pure-client >= 1.26.0
- netaddr
- requests
- pycountry
- packaging

## [Parameters](purefa_ds_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **aa_group**  string | Sets the common Name (CN) of the directory service group containing administrators with full privileges when managing the FlashArray. The name should be just the Common Name of the group without the CN= specifier. Common Names should not exceed 64 characters in length.  Not Supported from Purity 5.2.0 or higher. Use *purestorage.flasharray.purefa_dsrole* module. |
| **api_token**  string | FlashArray API token for admin privileged user. |
| **base_dn**  string | Sets the base of the Distinguished Name (DN) of the directory service groups. The base should consist of only Domain Components (DCs). The base_dn will populate with a default value when a URI is entered by parsing domain components from the URI. The base DN should specify DC= for each domain component and multiple DCs should be separated by commas. |
| **bind_password**  string | Sets the password of the bind_user user name account. |
| **bind_user**  string | Sets the user name that can be used to bind to and query the directory.  For Active Directory, enter the username - often referred to as sAMAccountName or User Logon Name - of the account that is used to perform directory lookups.  For OpenLDAP, enter the full DN of the user. |
| **certificate**  string  *added in purestorage.flasharray 1.24.0* | The certificate of the Certificate Authority (CA) that signed the certificates of the directory servers, which is used to validate the authenticity of the configured servers  A valid signed certicate in PEM format (Base64 encoded)  Includes the “—–BEGIN CERTIFICATE—–” and “—–END CERTIFICATE—–” lines  Does not exceed 3000 characters in length |
| **check_peer**  boolean  *added in purestorage.flasharray 1.24.0* | Whether or not server authenticity is enforced when a certificate is provided  **Choices:**   - `false` ← (default) - `true` |
| **dstype**  string | The type of directory service to work on  **Choices:**   - `"management"` ← (default) - `"data"` |
| **enable**  boolean | Whether to enable or disable directory service support.  **Choices:**   - `false` ← (default) - `true` |
| **fa_url**  string | FlashArray management IPv4 address or Hostname. |
| **force_bind_password**  boolean  *added in purestorage.flasharray 1.14.0* | Will force the bind password to be reset even if the bind user password is unchanged.  If set to *false* and *bind_user* is unchanged the password will not be reset.  **Choices:**   - `false` - `true` ← (default) |
| **group_base**  string | Specifies where the configured groups are located in the directory tree. This field consists of Organizational Units (OUs) that combine with the base DN attribute and the configured group CNs to complete the full Distinguished Name of the groups. The group base should specify OU= for each OU and multiple OUs should be separated by commas. The order of OUs is important and should get larger in scope from left to right. Each OU should not exceed 64 characters in length.  Not Supported from Purity 5.2.0 or higher. Use *purestorage.flasharray.purefa_dsrole* module. |
| **ro_group**  string | Sets the common Name (CN) of the configured directory service group containing users with read-only privileges on the FlashArray. This name should be just the Common Name of the group without the CN= specifier. Common Names should not exceed 64 characters in length.  Not Supported from Purity 5.2.0 or higher. Use *purestorage.flasharray.purefa_dsrole* module. |
| **sa_group**  string | Sets the common Name (CN) of the configured directory service group containing administrators with storage-related privileges on the FlashArray. This name should be just the Common Name of the group without the CN= specifier. Common Names should not exceed 64 characters in length.  Not Supported from Purity 5.2.0 or higher. Use *purestorage.flasharray.purefa_dsrole* module. |
| **state**  string | Create or delete directory service configuration  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **uri**  list / elements=string | A list of up to 30 URIs of the directory servers. Each URI must include the scheme <ldap://> or ldaps:// (for LDAP over SSL), a hostname, and a domain name or IP address. For example, ldap://ad.company.com configures the directory service with the hostname “ad” in the domain “company.com” while specifying the unencrypted LDAP protocol. |
| **user_login**  string | User login attribute in the structure of the configured LDAP servers. Typically the attribute field that holds the users unique login name. Default value is *sAMAccountName* for Active Directory or *uid* for all other directory services  Supported from Purity 6.0 or higher. |
| **user_object**  string | Value of the object class for a management LDAP user. Defaults to *User* for Active Directory servers, *posixAccount* or *shadowAccount* for OpenLDAP servers dependent on the group type of the server, or person for all other directory servers.  Supported from Purity 6.0 or higher. |

## [Notes](purefa_ds_module.md#id4)

> **Note:**
>
> - This module requires the `purestorage` and `py-pure-client` Python libraries
> - Additional Python librarues may be required for specific modules.
> - You must set `PUREFA_URL` and `PUREFA_API` environment variables if *fa_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefa_ds_module.md#id5)

```yaml+jinja
- name: Delete existing directory service
  purestorage.flasharray.purefa_ds:
    state: absent
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create directory service (disabled) - Pre-5.2.0
  purestorage.flasharray.purefa_ds:
    uri: "ldap://lab.purestorage.com"
    base_dn: "DC=lab,DC=purestorage,DC=com"
    bind_user: Administrator
    bind_password: password
    group_base: "OU=Pure-Admin"
    ro_group: PureReadOnly
    sa_group: PureStorage
    aa_group: PureAdmin
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create directory service (disabled) - 5.2.0 or higher
  purestorage.flasharray.purefa_ds:
    dstype: management
    uri: "ldap://lab.purestorage.com"
    base_dn: "DC=lab,DC=purestorage,DC=com"
    bind_user: Administrator
    bind_password: password
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Enable existing directory service
  purestorage.flasharray.purefa_ds:
    enable: true
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Disable existing directory service
  purestorage.flasharray.purefa_ds:
    enable: false
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create directory service (enabled) - Pre-5.2.0
  purestorage.flasharray.purefa_ds:
    enable: true
    uri: "ldap://lab.purestorage.com"
    base_dn: "DC=lab,DC=purestorage,DC=com"
    bind_user: Administrator
    bind_password: password
    group_base: "OU=Pure-Admin"
    ro_group: PureReadOnly
    sa_group: PureStorage
    aa_group: PureAdmin
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create directory service (enabled) - 5.2.0 or higher
  purestorage.flasharray.purefa_ds:
    enable: true
    dstype: management
    uri: "ldap://lab.purestorage.com"
    base_dn: "DC=lab,DC=purestorage,DC=com"
    bind_user: Administrator
    bind_password: password
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Upload CA certificate for management DNS and check peer
  purestorage.flasharray.purefa_ds:
    enable: true
    dstype: management
    certificate: "{{lookup('file', 'ca_cert.pem') }}"
    check_peer: True
    fa_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

- [Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues)
- [Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashArray-Collection)
- [Submit a bug report](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=bug&template=bug_report_template.md)
- [Request a feature](https://github.com/Pure-Storage-Ansible/FlashArray-Collection/issues/new?assignees=sdodsley&labels=enhancement&template=feature_request_template.md)
- [Communication](index.md#communication-for-purestorage-flasharray)
