---
collection: ansible
version: "8"
title: "Microsoft.Ad"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/index.html
fetched_at: 2026-07-28T01:02:45+00:00
---
# Microsoft.Ad

Collection version 1.4.1

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Scenario Guides](index.md#scenario-guides)
- [Plugin Index](index.md#plugin-index)

## [Description](index.md#id1)

Ansible collection for Active Directory management

**Authors:**

- Jordan Borean @jborean93
- Matt Davis @nitzmahone

**Supported ansible-core versions:**

- 2.14 or newer

- [Issue Tracker](https://github.com/ansible-collections/microsoft.ad/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/microsoft.ad)
- [Report an issue](https://github.com/ansible-collections/microsoft.ad/issues/new/choose)

## [Communication](index.md#id2)

- Matrix room `#windows:ansible.im`: [General usage and support questions](https://matrix.to/#/#windows:ansible.im).
- IRC channel `#ansible-windows` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible-windows).
- Mailing list: [Ansible Project List](https://groups.google.com/g/ansible-project).
  ([Subscribe](mailto:ansible-project+subscribe%40googlegroups.com?subject=subscribe))

## [Scenario Guides](index.md#id3)

- [Attributes guide](docsite/guide_attributes.md)
- [LDAP Connection guide](docsite/guide_ldap_connection.md)
- [LDAP Inventory guide](docsite/guide_ldap_inventory.md)
- [Setting list option values guide](docsite/guide_list_values.md)
- [Migration guide](docsite/guide_migration.md)

## [Plugin Index](index.md#id4)

These are the plugins in the microsoft.ad collection:

### Modules

- [computer module](computer_module.md#ansible-collections-microsoft-ad-computer-module) – Manage Active Directory computer objects
- [debug_ldap_client module](debug_ldap_client_module.md#ansible-collections-microsoft-ad-debug-ldap-client-module) – Get host information for debugging LDAP connections
- [domain module](domain_module.md#ansible-collections-microsoft-ad-domain-module) – Ensures the existence of a Windows domain
- [domain_controller module](domain_controller_module.md#ansible-collections-microsoft-ad-domain-controller-module) – Manage domain controller/member server state for a Windows host
- [group module](group_module.md#ansible-collections-microsoft-ad-group-module) – Manage Active Directory group objects
- [membership module](membership_module.md#ansible-collections-microsoft-ad-membership-module) – Manage domain/workgroup membership for a Windows host
- [object module](object_module.md#ansible-collections-microsoft-ad-object-module) – Manage Active Directory objects
- [object_info module](object_info_module.md#ansible-collections-microsoft-ad-object-info-module) – Gather information an Active Directory object
- [offline_join module](offline_join_module.md#ansible-collections-microsoft-ad-offline-join-module) – Get the Offline Domain Join BLOB
- [ou module](ou_module.md#ansible-collections-microsoft-ad-ou-module) – Manage Active Directory organizational units
- [user module](user_module.md#ansible-collections-microsoft-ad-user-module) – Manage Active Directory users

### Filter Plugins

- [as_datetime filter](as_datetime_filter.md#ansible-collections-microsoft-ad-as-datetime-filter) – Converts an LDAP value to a datetime string
- [as_guid filter](as_guid_filter.md#ansible-collections-microsoft-ad-as-guid-filter) – Converts an LDAP value to a GUID string
- [as_sid filter](as_sid_filter.md#ansible-collections-microsoft-ad-as-sid-filter) – Converts an LDAP value to a Security Identifier string

### Inventory Plugins

- [ldap inventory](ldap_inventory.md#ansible-collections-microsoft-ad-ldap-inventory) – Inventory plugin for Active Directory

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
