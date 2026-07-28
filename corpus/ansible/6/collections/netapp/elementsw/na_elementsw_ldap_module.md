---
collection: ansible
version: "6"
title: "netapp.elementsw.na_elementsw_ldap module – NetApp Element Software Manage ldap admin users"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp/elementsw/na_elementsw_ldap_module.html
fetched_at: 2026-07-28T00:11:50+00:00
---
# netapp.elementsw.na_elementsw_ldap module – NetApp Element Software Manage ldap admin users

> **Note:**
>
> This module is part of the [netapp.elementsw collection](https://galaxy.ansible.com/netapp/elementsw) (version 21.7.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.elementsw`.
> You need further requirements to be able to use this module,
> see [Requirements](na_elementsw_ldap_module.md#ansible-collections-netapp-elementsw-na-elementsw-ldap-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.elementsw.na_elementsw_ldap`.

New in netapp.elementsw 2.7.0

- [Synopsis](na_elementsw_ldap_module.md#synopsis)
- [Requirements](na_elementsw_ldap_module.md#requirements)
- [Parameters](na_elementsw_ldap_module.md#parameters)
- [Notes](na_elementsw_ldap_module.md#notes)
- [Examples](na_elementsw_ldap_module.md#examples)

## [Synopsis](na_elementsw_ldap_module.md#id1)

- Enable, disable ldap, and add ldap users

## [Requirements](na_elementsw_ldap_module.md#id2)

The below requirements are needed on the host that executes this module.

- The modules were developed with SolidFire 10.1
- solidfire-sdk-python (1.1.0.92) or greater. Install using ‘pip install solidfire-sdk-python’

## [Parameters](na_elementsw_ldap_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **authType**  string | Identifies which user authentication method to use.  Choices:   - `"DirectBind"` - `"SearchAndBind"` |
| **groupSearchBaseDn**  string | The base DN of the tree to start the group search (will do a subtree search from here) |
| **groupSearchCustomFilter**  string | For use with the CustomFilter Search type |
| **groupSearchType**  string | Controls the default group search filter used  Choices:   - `"NoGroup"` - `"ActiveDirectory"` - `"MemberDN"` |
| **hostname**  string / required | The hostname or IP address of the SolidFire cluster.  For na_elementsw_cluster, the Management IP (MIP) or hostname of the node to initiate the cluster creation from. |
| **password**  aliases: pass  string / required | Password for the specified user. |
| **searchBindDN**  string | A dully qualified DN to log in with to perform an LDAp search for the user (needs read access to the LDAP directory). |
| **searchBindPassword**  string | The password for the searchBindDN account used for searching |
| **serverURIs**  string | A comma-separated list of LDAP server URIs |
| **state**  string | Whether the specified volume should exist or not.  Choices:   - `"present"` ← (default) - `"absent"` |
| **userDNTemplate**  string | A string that is used form a fully qualified user DN. |
| **username**  aliases: user  string / required | Please ensure that the user has the adequate permissions. For more information, please read the official documentation <https://mysupport.netapp.com/documentation/docweb/index.html?productID%3D62636%26language%3Den-US>. |
| **userSearchBaseDN**  string | The base DN of the tree to start the search (will do a subtree search from here) |
| **userSearchFilter**  string | the LDAP Filter to use |

## [Notes](na_elementsw_ldap_module.md#id4)

> **Note:**
>
> - The modules prefixed with na\\_elementsw are built to support the SolidFire storage platform.

## [Examples](na_elementsw_ldap_module.md#id5)

```yaml+jinja
- name: disable ldap authentication
  na_elementsw_ldap:
    state: absent
    username: "{{ admin username }}"
    password: "{{ admin password }}"
    hostname: "{{ hostname }}"

- name: Enable ldap authentication
  na_elementsw_ldap:
    state: present
    username: "{{ admin username }}"
    password: "{{ admin password }}"
    hostname: "{{ hostname }}"
    authType: DirectBind
    serverURIs: ldap://svmdurlabesx01spd_ldapclnt
    groupSearchType: MemberDN
    userDNTemplate:  uid=%USERNAME%,cn=users,cn=accounts,dc=corp,dc="{{ company name }}",dc=com
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/netapp.elementsw/issues)
[Homepage](https://netapp.io/configuration-management-and-automation/)
[Repository (Sources)](https://github.com/ansible-collections/netapp.elementsw)
