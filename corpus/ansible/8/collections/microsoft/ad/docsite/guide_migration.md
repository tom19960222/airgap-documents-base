---
collection: ansible
version: "8"
title: "Migration guide"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/docsite/guide_migration.html
fetched_at: 2026-07-28T02:40:47+00:00
---
# Migration guide

Some of the modules in this collection have come from the [ansible.windows collection](https://galaxy.ansible.com/ansible/windows) or the [community.windows collection](https://galaxy.ansible.com/community/windows). This document will go through some of the changes made to help ease the transition from the older modules to the ones in this collection.

- [Migrated Modules](guide_migration.md#migrated-modules)

## [Migrated Modules](guide_migration.md#id1)

The following modules have been migrated in some shape or form into this collection

- `ansible.windows.win_domain` -> `microsoft.ad.domain` - [details](guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain)
- `ansible.windows.win_domain_controller` -> `microsoft.ad.domain_controller` - [details](guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-controller)
- `ansible.windows.win_domain_membership` -> `microsoft.ad.membership` - [details](guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-membership)
- `community.windows.win_domain_computer` -> `microsoft.ad.computer` - [details](guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-computer)
- `community.windows.win_domain_group` -> `microsoft.ad.group` - [details](guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-group)
- `community.windows.win_domain_group_membership` -> `microsoft.ad.group` - [details](guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-group-membership)
- `community.windows.win_domain_object_info` -> `microsoft.ad.object_info` - [details](guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-object-info)
- `community.windows.win_domain_ou` -> `microsoft.ad.ou` - [details](guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-ou)
- `community.windows.win_domain_user` -> `microsoft.ad.user` - [details](guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-user)

While these modules are mostly drop in place compatible there are some breaking changes that need to be considered. See each module entry for more information.

### Module `win_domain`

Migrated to [microsoft.ad.domain](../domain_module.md#ansible-collections-microsoft-ad-domain-module).

There are no known breaking changes and should work as a drop in replacement. The `reboot` option has been added to have the module handle any reboots that are needed instead of a separate `ansible.windows.win_reboot` task. Due to the operations involved with promoting a domain controller, it is highly recommended to use this option.

### Module `win_domain_controller`

Migrated to [microsoft.ad.domain_controller](../domain_controller_module.md#ansible-collections-microsoft-ad-domain-controller-module).

The following options have been removed:

- `log_path` - Creating a debug log of module actions is not supported

The `reboot` option has been added to have the module handle any reboots instead of a separate `ansible.windows.win_reboot` task. Due to the operations involved with promoting a domain controller, it is highly recommended to use this option.

### Module `win_domain_membership`

Migrated to [microsoft.ad.membership](../membership_module.md#ansible-collections-microsoft-ad-membership-module).

The following options have been removed:

- `log_path` - Creating a debug log of module actions is not supported

The `reboot` option has been added to have the module handle any reboots instead of a separate `ansible.windows.win_reboot` task.

### Module `win_domain_computer`

Migrated to [microsoft.ad.computer](../computer_module.md#ansible-collections-microsoft-ad-computer-module).

The option `dns_host_name` is not required when `state: present`, the computer object is created without the `dnsHostName` LDAP attribute set if it is not defined.

The default for `enabled` is nothing, the group will still be enabled when created but it will use the existing status if the option is omitted.

The option `ou` is now named `path` to match the standard set by other modules.

The options `offline_domain_join` and `odj_blob_path` has been removed. Use the new module `microsoft.ad.offline_join` to generate the offline join blob. For example:

```yaml
- name: create computer object
  microsoft.ad.computer:
    name: MyComputer
    state: present
  register: computer_obj

- name: create offline blob
  microsoft.ad.offline_join:
    identity: '{{ computer_obj.object_guid }}'
  when: computer_obj is changed
  register: offline_blob

- name: display offline blob
  debug:
    var: offline_blob.blob
  when: computer_obj is changed
```

### Module `win_domain_group`

Migrated to [microsoft.ad.group](../group_module.md#ansible-collections-microsoft-ad-group-module).

The following options have changed:

- `attributes` - changed format as outlined in [Attributes guid](guide_attributes.md#ansible-collections-microsoft-ad-docsite-guide-attributes)
- `ignore_protection` - Has been removed and `state: absent` will also remove objects regardless of the protection status
- `organizational_unit` and `ou` - Have been removed, use `path` instead
- `protect` - Has been renamed to `protect_from_deletion` and is now not needed to be unset for `state: absent` to remove the group

The return values for `win_domain_group` have also been simplified to only return:

- `distinguished_name` - The Distinguished Name (`DN`) of the managed OU
- `object_guid` - The Object GUID of the managed OU
- `sid` - The Security Identifier of the managed user

All other return values have been removed, use `microsoft.ad.object_info` to get extra values if needed.

### Module `win_domain_group_membership`

Migrated to [microsoft.ad.group](../group_module.md#ansible-collections-microsoft-ad-group-module).

The functionality of this module has been merged with `microsoft.ad.group`. Use the `members` option to `add`, `remove`, or `set` to add, remove, or set group members respectively.

### Module `win_domain_object_info`

Migrated to [microsoft.ad.object_info](../object_info_module.md#ansible-collections-microsoft-ad-object-info-module).

There are no known breaking changes and should work as a drop in replacement.

### Module `win_domain_ou`

Migrated to [microsoft.ad.ou](../ou_module.md#ansible-collections-microsoft-ad-ou-module).

The following options have changed:

- `protected` - Has been renamed to `protect_from_deletion` and is now not needed to be unset for `state: absent` to remove the OU
- `recursive` - Has been removed and `state: absent` will also remove objects recursively
- `filter` - Has been removed, the `name` object refers to the OU name and `identity` can be used to select the OU by `DistinguishedName` or `ObjectGUID` if a rename or move is needed
- `properties` - Has been removed, use the new `attributes` option

The return values for `win_domain_ou` have also been simplified to only return:

- `distinguished_name` - The Distinguished Name (`DN`) of the managed OU
- `object_guid` - The Object GUID of the managed OU

All other return values have been removed, use `microsoft.ad.object_info` to get extra values if needed.

### Module `win_domain_user`

Migrated to [microsoft.ad.user](../user_module.md#ansible-collections-microsoft-ad-user-module).

The following options have changed:

- `attributes` - changed format as outlined in [Attributes guid](guide_attributes.md#ansible-collections-microsoft-ad-docsite-guide-attributes)
- `delegates` - changed format as outlined in [Setting list values](guide_list_values.md#ansible-collections-microsoft-ad-docsite-guide-list-values)
- `groups` - changed format as outlined in [Setting list values](guide_list_values.md#ansible-collections-microsoft-ad-docsite-guide-list-values)
- `groups_action` - has been removed in favour of the new `groups` format
- `groups_missing_behaviour` - has been moved into the `group` dictionary value as `missing_behaviour`
- `spn`- changed format as outlined in [Setting list values](guide_list_values.md#ansible-collections-microsoft-ad-docsite-guide-list-values)
- `spn_action` - has been removed in favour of the new `spn` format
- `state` - No query option - use `microsoft.ad.object_info` instead
- `enabled` - Does not default to `true`. Creating a new user without a password will use `enabled=false` but setting a password will use `enabled=true`

The `groups_action` and `spn_action` `set` value was renamed to align with common practice. The `state=query` functionality has been removed to simplify the module and favour `microsoft.ad.object_info` which is designed to return information about AD objects. The `enabled` default was removed to allow setting other attributes on an existing AD object without always having to specify `enabled`.

The return values for `win_domain_user` have also been simplified to only return:

- `distinguished_name` - The Distinguished Name (`DN`) of the managed user
- `object_guid` - The Object GUID of the managed user
- `sid` - The Security Identifier of the managed user

All other return values have been removed, use `microsoft.ad.object_info` to get extra values if needed.
