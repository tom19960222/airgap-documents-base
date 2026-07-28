---
collection: ansible
version: "8"
title: "microsoft.ad.group module – Manage Active Directory group objects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/group_module.html
fetched_at: 2026-07-28T02:40:50+00:00
---
# microsoft.ad.group module – Manage Active Directory group objects

> **Note:**
>
> This module is part of the [microsoft.ad collection](https://galaxy.ansible.com/ui/repo/published/microsoft/ad/) (version 1.4.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install microsoft.ad`.
> You need further requirements to be able to use this module,
> see [Requirements](group_module.md#ansible-collections-microsoft-ad-group-module-requirements) for details.
>
> To use it in a playbook, specify: `microsoft.ad.group`.

- [Synopsis](group_module.md#synopsis)
- [Requirements](group_module.md#requirements)
- [Parameters](group_module.md#parameters)
- [Attributes](group_module.md#attributes)
- [Notes](group_module.md#notes)
- [See Also](group_module.md#see-also)
- [Examples](group_module.md#examples)
- [Return Values](group_module.md#return-values)

## [Synopsis](group_module.md#id1)

- Manages Active Directory group objects and their attributes.

## [Requirements](group_module.md#id2)

The below requirements are needed on the host that executes this module.

- `ActiveDirectory` PowerShell module

## [Parameters](group_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | The attributes to either add, remove, or set on the AD object.  The value of each attribute option should be a dictionary where the key is the LDAP attribute, e.g. `firstName`, `comment` and the value is the value, or list of values, to set for that attribute.  The attribute value(s) can either be the raw string, integer, or bool value to add, remove, or set on the attribute in question.  The value can also be a dictionary with the *type* key set to `bytes`, `date_time`, `security_descriptor`, or `raw` and the value for this entry under the *value* key.  The `bytes` type has a value that is a base64 encoded string of the raw bytes to set.  The `date_time` type has a value that is the ISO 8601 DateTime string of the DateTime to set. The DateTime will be set as the Microsoft FILETIME integer value which is the number of 100 nanoseconds since 1601-01-01 in UTC.  The `security_descriptor` type has a value that is the Security Descriptor SDDL string used for the `nTSecurityDescriptor` attribute.  The `raw` type is the int, string, or boolean value to set.  String attribute values are compared using a case sensitive match on the AD object being managed.  See [LDAP attributes help](docsite/guide_attributes.md#ansible-collections-microsoft-ad-docsite-guide-attributes) for more information.  **Default:** `{}` |
| **add**  dictionary | A dictionary of all the attributes and their value(s) to add to the AD object being managed if they are not already present.  This is used for attributes that can contain multiple values, if the attribute only allows a single value, use *set* instead.  **Default:** `{}` |
| **remove**  dictionary | A dictionary of all the attributes and their value(s) to remove from the AD object being managed if they are present.  This is used for attributes that can contain multiple values, if the attribute only allows a single value, use *set* instead.  **Default:** `{}` |
| **set**  dictionary | A dictionary of all attributes and their value(s) to set on the AD object being managed.  This will replace any existing values if they do not match the ones being requested.  The order of attribute values are not checked only, only that the values requested are the only values on the object attribute.  Set this to null or an empty list to clear any values for the attribute.  **Default:** `{}` |
| **category**  string | The category of the group.  If a new group is created then `security` will be used by default.  A `security` group can be associated with access control lists whereas `distribution` groups are typically associated with mailing distribution lists.  This is the value set on the `groupType` LDAP attributes.  **Choices:**   - `"distribution"` - `"security"` |
| **description**  string | The description of the AD object to set.  This is the value set on the `description` LDAP attribute. |
| **display_name**  string | The display name of the AD object to set.  This is the value of the `displayName` LDAP attribute. |
| **domain_password**  string | The password for *domain_username*. |
| **domain_server**  string | Specified the Active Directory Domain Services instance to connect to.  Can be in the form of an FQDN or NetBIOS name.  If not specified then the value is based on the default domain of the computer running PowerShell. |
| **domain_username**  string | The username to use when interacting with AD.  If this is not set then the user that is used for authentication will be the connection user.  Ansible will be unable to use the connection user unless auth is Kerberos with credential delegation or CredSSP, or become is used on the task. |
| **homepage**  string | The homepage of the group.  This is the value set on the `wWWHomePage` LDAP attribute. |
| **identity**  string | The identity of the AD object used to find the AD object to manage.  Must be specified if *name* is not set, when trying to rename the object with a new *name*, or when trying to move the object into a different *path*.  The identity can be in the form of a GUID representing the `objectGUID` value, the `userPrincipalName`, `sAMAccountName`, `objectSid`, or `distinguishedName`.  If omitted, the AD object to managed is selected by the `distinguishedName` using the format `CN={{ name }},{{ path }}`. If *path* is not defined, the `defaultNamingContext` is used instead. |
| **managed_by**  string | The user or group that manages the group.  The value can be in the form of a `distinguishedName`, `objectGUID`, `objectSid`, or `sAMAccountName`.  This is the value set on the `managedBy` LDAP attribute. |
| **members**  dictionary | The members of the group to set.  The value is a dictionary that contains 3 keys, *add*, *remove*, and *set*.  Each subkey is set to a list of AD principal objects to add, remove or set as the members of this AD group respectively. A principal can be in the form of a `distinguishedName`, `objectGUID`, `objectSid`, or `sAMAccountName`.  The module will fail if it cannot find any of the members referenced. |
| **add**  list / elements=string | Adds the principals specified as members of the group, keeping the existing membership if they are not specified. |
| **remove**  list / elements=string | Removes the principals specified as members of the group, keeping the existing membership if they are not specified. |
| **set**  list / elements=string | Sets only the principals specified as members of the group.  Any other existing member will be removed from the group membership if not specified in this list.  Set this to an empty list to remove all members from a group. |
| **name**  string | The `name` of the AD object to manage.  If *identity* is specified, and the name of the object it found does not match this value, the object will be renamed.  This if *identity* must be set to find the object to manage.  This is not always going to be the same as the `sAMAccountName` for user objects. It is strictly the `name` of the object in the path specified. Use *identity* to select an object to manage by `sAMAccountName`. |
| **path**  string | The path of the OU or the container where the new object should exist in.  If creating a new object, the new object will be created at the path specified. If no path is specified then the `defaultNamingContext` of the domain will be used as the path for most object types.  If managing an existing object found by *identity*, the path of the found object will be moved to the one specified by this option. If no path is specified, the object will not be moved.  The modules [microsoft.ad.computer](computer_module.md#ansible-collections-microsoft-ad-computer-module), [microsoft.ad.user](user_module.md#ansible-collections-microsoft-ad-user-module), and [microsoft.ad.group](group_module.md#ansible-collections-microsoft-ad-group-module) have their own default path that is configured on the Active Directory domain controller.  This can be set to `microsoft.ad.default_path` which will equal the default value used when creating a new object. |
| **protect_from_deletion**  boolean | Marks the object as protected from accidental deletion.  This applies a deny access right from deleting the object normally and the protection needs to be removed before the object can be deleted through the GUI or any other tool outside Ansible.  Using *state=absent* will still delete the AD object even if it is marked as protected from deletion.  **Choices:**   - `false` - `true` |
| **sam_account_name**  string | The `sAMAccountName` value to set for the group.  If omitted, the *name* value is used when creating a new group. |
| **scope**  string | The scope of the group.  This is required when *state=present* and the group does not already exist.  See [Group scope](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2003/cc755692%2528v=ws.10%2529) for more information on the various domain group scopes.  This is the value set on the `groupType` LDAP attributes.  **Choices:**   - `"domainlocal"` - `"global"` - `"universal"` |
| **state**  string | Set to `present` to ensure the AD object exists.  Set to `absent` to remove the AD object if it exists.  The option *name* must be set when *state=present*.  Using `absent` will recursively remove the AD object and any child objects if it’s a container. It will also remove the AD object even if the object is marked as protected from accidental deletion.  **Choices:**   - `"absent"` - `"present"` ← (default) |

## [Attributes](group_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **windows** | Target OS/families that can be operated against |

## [Notes](group_module.md#id5)

> **Note:**
>
> - See [win_group migration](docsite/guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-group) for help on migrating from [community.windows.win_domain_group](../../community/windows/win_domain_group_module.md#ansible-collections-community-windows-win-domain-group-module) to this module.
> - Some LDAP attributes can have only a single value set while others can have multiple. Some attributes are also read only and cannot be changed. It is recommended to look at the schema metadata for an attribute where `System-Only` are read only values and `Is-Single-Value` are attributes with only 1 value.
> - Attempting to set multiple values to a `Is-Single-Value` attribute results in undefined behaviour.
> - If running on a server that is not a Domain Controller, credential delegation through CredSSP or Kerberos with delegation must be used or the *domain_username*, *domain_password* must be set.

## [See Also](group_module.md#id6)

> **See also:**
>
> [microsoft.ad.domain](domain_module.md#ansible-collections-microsoft-ad-domain-module)
> :   Ensures the existence of a Windows domain.
>
> [microsoft.ad.domain_controller](domain_controller_module.md#ansible-collections-microsoft-ad-domain-controller-module)
> :   Manage domain controller/member server state for a Windows host.
>
> [microsoft.ad.membership](membership_module.md#ansible-collections-microsoft-ad-membership-module)
> :   Manage domain/workgroup membership for a Windows host.
>
> [microsoft.ad.object_info](object_info_module.md#ansible-collections-microsoft-ad-object-info-module)
> :   Gather information an Active Directory object.
>
> [microsoft.ad.object](object_module.md#ansible-collections-microsoft-ad-object-module)
> :   Manage Active Directory objects.
>
> [microsoft.ad.user](user_module.md#ansible-collections-microsoft-ad-user-module)
> :   Manage Active Directory users.
>
> [Migration guide](docsite/guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-group)
> :   This module replaces `community.windows.win_domain_group`. See the migration guide for details.
>
> [community.windows.win_domain_group](../../community/windows/win_domain_group_module.md#ansible-collections-community-windows-win-domain-group-module)
> :   Creates, modifies or removes domain groups.

## [Examples](group_module.md#id7)

```yaml+jinja
- name: Ensure a group exists
  microsoft.ad.group:
    name: Cow
    scope: global

- name: Remove a group
  microsoft.ad.group:
    name: Cow
    state: absent

- name: Create a group in a custom path
  microsoft.ad.group:
    name: Cow
    scope: global
    path: OU=groups,DC=ansible,DC=local
    state: present

- name: Remove a group in a custom path
  microsoft.ad.group:
    name: Cow
    path: OU=groups,DC=ansible,DC=local
    state: absent

- name: Create group with delete protection enabled and custom attributes
  microsoft.ad.group:
    name: Ansible Users
    scope: domainlocal
    category: security
    homepage: www.ansible.com
    attributes:
      set:
        mail: helpdesk@ansible.com
    protect_from_deletion: true

- name: Change the path of a group
  microsoft.ad.group:
    name: MyGroup
    scope: global
    identity: S-1-5-21-2171456218-3732823212-122182344-1189
    path: OU=groups,DC=ansible,DC=local

- name: Add managed_by user
  microsoft.ad.group:
    name: Group Name Here
    scope: global
    managed_by: Domain Admins

- name: Add group and specify the AD domain services to use for the create
  microsoft.ad.group:
    name: Test Group
    domain_username: user@CORP.ANSIBLE.COM
    domain_password: Password01!
    domain_server: corp-DC12.corp.ansible.com
    scope: domainlocal

- name: Add members to the group, preserving existing membership
  microsoft.ad.group:
    name: Test Group
    scope: domainlocal
    members:
      add:
      - Domain Admins
      - Domain Users

- name: Remove members from the group, preserving existing membership
  microsoft.ad.group:
    name: Test Group
    scope: domainlocal
    members:
      remove:
      - Domain Admins
      - Domain Users

- name: Replace entire membership of group
  microsoft.ad.group:
    name: Test Group
    scope: domainlocal
    members:
      set:
      - Domain Admins
      - Domain Users
```

## [Return Values](group_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **distinguished_name**  string | The `distinguishedName` of the AD object that was created, removed, or edited.  **Returned:** always  **Sample:** `"CN=MyGroup,CN=Users,,DC=domain,DC=test"` |
| **object_guid**  string | The `objectGUID` of the AD object that was created, removed, or edited.  If a new object was created in check mode, a GUID of 0s will be returned.  **Returned:** always  **Sample:** `"d84a141f-2b99-4f08-9da0-ed2d26864ba1"` |
| **sid**  string | The Security Identifier (SID) of the group managed.  If a new group was created in check mode, the SID will be `S-1-5-0000`.  **Returned:** always  **Sample:** `"S-1-5-21-4151808797-3430561092-2843464588-1104"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/microsoft.ad/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/microsoft.ad)
- [Report an issue](https://github.com/ansible-collections/microsoft.ad/issues/new/choose)
- [Communication](index.md#communication-for-microsoft-ad)
