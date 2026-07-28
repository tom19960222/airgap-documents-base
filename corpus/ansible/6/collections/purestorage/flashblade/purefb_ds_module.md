---
collection: ansible
version: "6"
title: "purestorage.flashblade.purefb_ds module – Configure FlashBlade Directory Service"
source_url: https://docs.ansible.com/projects/ansible/6/collections/purestorage/flashblade/purefb_ds_module.html
fetched_at: 2026-07-28T00:18:45+00:00
---
# purestorage.flashblade.purefb_ds module – Configure FlashBlade Directory Service

> **Note:**
>
> This module is part of the [purestorage.flashblade collection](https://galaxy.ansible.com/purestorage/flashblade) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install purestorage.flashblade`.
> You need further requirements to be able to use this module,
> see [Requirements](purefb_ds_module.md#ansible-collections-purestorage-flashblade-purefb-ds-module-requirements) for details.
>
> To use it in a playbook, specify: `purestorage.flashblade.purefb_ds`.

New in purestorage.flashblade 1.0.0

- [Synopsis](purefb_ds_module.md#synopsis)
- [Requirements](purefb_ds_module.md#requirements)
- [Parameters](purefb_ds_module.md#parameters)
- [Notes](purefb_ds_module.md#notes)
- [Examples](purefb_ds_module.md#examples)

## [Synopsis](purefb_ds_module.md#id1)

- Create, modify or erase directory services configurations. There is no facility to SSL certificates at this time. Use the FlashBlade GUI for this additional configuration work.
- If updating a directory service and i(bind_password) is provided this will always cause a change, even if the password given isn’t different from the current. This makes this part of the module non-idempotent..

## [Requirements](purefb_ds_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.7
- purity_fb >= 1.9
- netaddr
- pytz

## [Parameters](purefb_ds_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_token**  string | FlashBlade API token for admin privileged user. |
| **base_dn**  string | Sets the base of the Distinguished Name (DN) of the directory service groups. The base should consist of only Domain Components (DCs). The base_dn will populate with a default value when a URI is entered by parsing domain components from the URI. The base DN should specify DC= for each domain component and multiple DCs should be separated by commas. |
| **bind_password**  string | Sets the password of the bind_user user name account. |
| **bind_user**  string | Sets the user name that can be used to bind to and query the directory.  For Active Directory, enter the username - often referred to as sAMAccountName or User Logon Name - of the account that is used to perform directory lookups.  For OpenLDAP, enter the full DN of the user. |
| **dstype**  string / required | The type of directory service to work on  Choices:   - `"management"` - `"nfs"` - `"smb"` |
| **enable**  boolean | Whether to enable or disable directory service support.  Choices:   - `false` ← (default) - `true` |
| **fb_url**  string | FlashBlade management IP address or Hostname. |
| **join_ou**  string | The optional organizational unit (OU) where the machine account for the directory service will be created. |
| **nis_domain**  string | The NIS domain to search  This cannot be used in conjunction with LDAP configurations. |
| **nis_servers**  list / elements=string | A list of up to 30 IP addresses or FQDNs for NIS servers.  This cannot be used in conjunction with LDAP configurations. |
| **state**  string | Create or delete directory service configuration  Choices:   - `"absent"` - `"present"` ← (default) |
| **uri**  list / elements=string | A list of up to 30 URIs of the directory servers. Each URI must include the scheme <ldap://> or ldaps:// (for LDAP over SSL), a hostname, and a domain name or IP address. For example, ldap://ad.company.com configures the directory service with the hostname “ad” in the domain “company.com” while specifying the unencrypted LDAP protocol. |

## [Notes](purefb_ds_module.md#id4)

> **Note:**
>
> - This module requires the `purity_fb` Python library
> - You must set `PUREFB_URL` and `PUREFB_API` environment variables if *fb_url* and *api_token* arguments are not passed to the module directly

## [Examples](purefb_ds_module.md#id5)

```yaml+jinja
- name: Delete existing management directory service
  purestorage.flashblade.purefb_ds:
    dstype: management
    state: absent
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create NFS directory service (disabled)
  purestorage.flashblade.purefb_ds:
    dstype: nfs
    uri: "ldaps://lab.purestorage.com"
    base_dn: "DC=lab,DC=purestorage,DC=com"
    bind_user: Administrator
    bind_password: password
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Enable existing SMB directory service
  purestorage.flashblade.purefb_ds:
    dstypr: smb
    enable: true
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Disable existing management directory service
  purestorage.flashblade.purefb_ds:
    dstype: management
    enable: false
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592

- name: Create NFS directory service (enabled)
  purestorage.flashblade.purefb_ds:
    dstype: nfs
    enable: true
    uri: "ldaps://lab.purestorage.com"
    base_dn: "DC=lab,DC=purestorage,DC=com"
    bind_user: Administrator
    bind_password: password
    fb_url: 10.10.10.2
    api_token: e31060a7-21fc-e277-6240-25983c6c4592
```

### Authors

- Pure Storage Ansible Team (@sdodsley)

### Collection links

[Issue Tracker](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection/issues)
[Repository (Sources)](https://github.com/Pure-Storage-Ansible/FlashBlade-Collection)
