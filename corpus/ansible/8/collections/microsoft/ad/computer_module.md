---
collection: ansible
version: "8"
title: "microsoft.ad.computer module – Manage Active Directory computer objects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/computer_module.html
fetched_at: 2026-07-28T02:40:47+00:00
---
# microsoft.ad.computer module – Manage Active Directory computer objects

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
> see [Requirements](computer_module.md#ansible-collections-microsoft-ad-computer-module-requirements) for details.
>
> To use it in a playbook, specify: `microsoft.ad.computer`.

- [Synopsis](computer_module.md#synopsis)
- [Requirements](computer_module.md#requirements)
- [Parameters](computer_module.md#parameters)
- [Attributes](computer_module.md#attributes)
- [Notes](computer_module.md#notes)
- [See Also](computer_module.md#see-also)
- [Examples](computer_module.md#examples)
- [Return Values](computer_module.md#return-values)

## [Synopsis](computer_module.md#id1)

- Manages Active Directory computer objects and their attributes.

## [Requirements](computer_module.md#id2)

The below requirements are needed on the host that executes this module.

- `ActiveDirectory` PowerShell module

## [Parameters](computer_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | The attributes to either add, remove, or set on the AD object.  The value of each attribute option should be a dictionary where the key is the LDAP attribute, e.g. `firstName`, `comment` and the value is the value, or list of values, to set for that attribute.  The attribute value(s) can either be the raw string, integer, or bool value to add, remove, or set on the attribute in question.  The value can also be a dictionary with the *type* key set to `bytes`, `date_time`, `security_descriptor`, or `raw` and the value for this entry under the *value* key.  The `bytes` type has a value that is a base64 encoded string of the raw bytes to set.  The `date_time` type has a value that is the ISO 8601 DateTime string of the DateTime to set. The DateTime will be set as the Microsoft FILETIME integer value which is the number of 100 nanoseconds since 1601-01-01 in UTC.  The `security_descriptor` type has a value that is the Security Descriptor SDDL string used for the `nTSecurityDescriptor` attribute.  The `raw` type is the int, string, or boolean value to set.  String attribute values are compared using a case sensitive match on the AD object being managed.  See [LDAP attributes help](docsite/guide_attributes.md#ansible-collections-microsoft-ad-docsite-guide-attributes) for more information.  **Default:** `{}` |
| **add**  dictionary | A dictionary of all the attributes and their value(s) to add to the AD object being managed if they are not already present.  This is used for attributes that can contain multiple values, if the attribute only allows a single value, use *set* instead.  **Default:** `{}` |
| **remove**  dictionary | A dictionary of all the attributes and their value(s) to remove from the AD object being managed if they are present.  This is used for attributes that can contain multiple values, if the attribute only allows a single value, use *set* instead.  **Default:** `{}` |
| **set**  dictionary | A dictionary of all attributes and their value(s) to set on the AD object being managed.  This will replace any existing values if they do not match the ones being requested.  The order of attribute values are not checked only, only that the values requested are the only values on the object attribute.  Set this to null or an empty list to clear any values for the attribute.  **Default:** `{}` |
| **delegates**  aliases: principals_allowed_to_delegate  dictionary | The principal objects that the current AD object can trust for delegation to either add, remove or set.  The values for each sub option must be specified as a distinguished name `CN=shenetworks,CN=Users,DC=ansible,DC=test`  This is the value set on the `msDS-AllowedToActOnBehalfOfOtherIdentity` LDAP attribute.  This is a highly sensitive attribute as it allows the principals specified to impersonate any account when authenticating with the AD computer object being managed.  To clear all principals, use *set* with an empty list.  See [Setting list option values](docsite/guide_list_values.md#ansible-collections-microsoft-ad-docsite-guide-list-values) for more information on how to add/remove/set list options. |
| **add**  list / elements=string | The AD objects by their `DistinguishedName` to add as a principal allowed to delegate.  Any existing principals not specified by *add* will be untouched unless specified by *remove* or not in *set*. |
| **remove**  list / elements=string | The AD objects by their `DistinguishedName` to remove as a principal allowed to delegate.  Any existing pricipals not specified by *remove* will be untouched unless *set* is defined. |
| **set**  list / elements=string | The AD objects by their `DistinguishedName` to set as the only principals allowed to delegate.  This will remove any existing principals if not specified in this list.  Specify an empty list to remove all principals allowed to delegate. |
| **description**  string | The description of the AD object to set.  This is the value set on the `description` LDAP attribute. |
| **display_name**  string | The display name of the AD object to set.  This is the value of the `displayName` LDAP attribute. |
| **dns_hostname**  string | Specifies the fully qualified domain name (FQDN) of the computer.  This is the value set on the `dNSHostName` LDAP attribute. |
| **domain_password**  string | The password for *domain_username*. |
| **domain_server**  string | Specified the Active Directory Domain Services instance to connect to.  Can be in the form of an FQDN or NetBIOS name.  If not specified then the value is based on the default domain of the computer running PowerShell. |
| **domain_username**  string | The username to use when interacting with AD.  If this is not set then the user that is used for authentication will be the connection user.  Ansible will be unable to use the connection user unless auth is Kerberos with credential delegation or CredSSP, or become is used on the task. |
| **enabled**  boolean | `yes` will enable the group.  `no` will disable the group.  **Choices:**   - `false` - `true` |
| **identity**  string | The identity of the AD object used to find the AD object to manage.  Must be specified if *name* is not set, when trying to rename the object with a new *name*, or when trying to move the object into a different *path*.  The identity can be in the form of a GUID representing the `objectGUID` value, the `userPrincipalName`, `sAMAccountName`, `objectSid`, or `distinguishedName`.  If omitted, the AD object to managed is selected by the `distinguishedName` using the format `CN={{ name }},{{ path }}`. If *path* is not defined, the `defaultNamingContext` is used instead. |
| **kerberos_encryption_types**  dictionary | Specifies the Kerberos encryption types supported the AD computer account.  This is the value set on the `msDS-SupportedEncryptionTypes` LDAP attribute.  Avoid using `rc4` or `des` as they are older an insecure encryption protocols.  To clear all encryption types, use *set* with an empty list.  See [Setting list option values](docsite/guide_list_values.md#ansible-collections-microsoft-ad-docsite-guide-list-values) for more information on how to add/remove/set list options. |
| **add**  list / elements=string | The encryption types to add to the existing set.  Any existing encryption types not specified by *add* will be untouched unless specified by *remove* or not in *set*.  **Choices:**   - `"aes128"` - `"aes256"` - `"des"` - `"rc4"` |
| **remove**  list / elements=string | The encryption types to remove from the existing set.  Any existing encryption types not specified by *remove* will be untouched unless *set* is defined.  **Choices:**   - `"aes128"` - `"aes256"` - `"des"` - `"rc4"` |
| **set**  list / elements=string | The encryption types to set as the only encryption types allowed by the AD computer.  This will remove any existing encryption types if not specified in this list.  Specify an empty list to remove all encryption types.  **Choices:**   - `"aes128"` - `"aes256"` - `"des"` - `"rc4"` |
| **location**  string | Sets the location of the computer account.  This is the value set on the `location` LDAP attribute. |
| **managed_by**  string | The user or group that manages the object.  The value can be in the form of a `distinguishedName`, `objectGUID`, `objectSid`, or sAMAccountName).  This is the value set on the `managedBy` LDAP attribute. |
| **name**  string | The `name` of the AD object to manage.  If *identity* is specified, and the name of the object it found does not match this value, the object will be renamed.  This if *identity* must be set to find the object to manage.  This is not always going to be the same as the `sAMAccountName` for user objects. It is strictly the `name` of the object in the path specified. Use *identity* to select an object to manage by `sAMAccountName`. |
| **path**  string | The path of the OU or the container where the new object should exist in.  If creating a new object, the new object will be created at the path specified. If no path is specified then the `defaultNamingContext` of the domain will be used as the path for most object types.  If managing an existing object found by *identity*, the path of the found object will be moved to the one specified by this option. If no path is specified, the object will not be moved.  The modules [microsoft.ad.computer](computer_module.md#ansible-collections-microsoft-ad-computer-module), [microsoft.ad.user](user_module.md#ansible-collections-microsoft-ad-user-module), and [microsoft.ad.group](group_module.md#ansible-collections-microsoft-ad-group-module) have their own default path that is configured on the Active Directory domain controller.  This can be set to `microsoft.ad.default_path` which will equal the default value used when creating a new object. |
| **protect_from_deletion**  boolean | Marks the object as protected from accidental deletion.  This applies a deny access right from deleting the object normally and the protection needs to be removed before the object can be deleted through the GUI or any other tool outside Ansible.  Using *state=absent* will still delete the AD object even if it is marked as protected from deletion.  **Choices:**   - `false` - `true` |
| **sam_account_name**  string | The `sAMAccountName` value to set for the group.  If omitted, the *name* value is used when creating a new group.  It has a maximum of 256 characters, 15 is advised for older operating systems compatibility.  If ommitted the value is the same as `name$` when the computer is created.  Note that all computer `sAMAccountName` values need to end with a `$`.  If `$` is omitted, it will be added to the end. |
| **spn**  aliases: spns  dictionary | Specifies the service principal name(s) for the account to add, remove or set.  This is the value set on the `servicePrincipalName` LDAP attribute.  To clear all service principal names, use *set* with an empty list.  See [Setting list option values](docsite/guide_list_values.md#ansible-collections-microsoft-ad-docsite-guide-list-values) for more information on how to add/remove/set list options. |
| **add**  list / elements=string | The SPNs to add to `servicePrincipalName`. |
| **remove**  list / elements=string | The SPNs to remove from `servicePrincipalName`. |
| **set**  list / elements=string | The SPNs to set as the only values in `servicePrincipalName`.  This will clear out any existing SPNs if not in the specified list.  Set to an empty list to clear all SPNs on the AD object. |
| **state**  string | Set to `present` to ensure the AD object exists.  Set to `absent` to remove the AD object if it exists.  The option *name* must be set when *state=present*.  Using `absent` will recursively remove the AD object and any child objects if it’s a container. It will also remove the AD object even if the object is marked as protected from accidental deletion.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **trusted_for_delegation**  boolean | Specifies whether an account is trusted for Kerberos delegation.  This is also known as unconstrained Kerberos delegation.  This sets the `ADS_UF_TRUSTED_FOR_DELEGATION` flag in the `userAccountControl` LDAP attribute.  **Choices:**   - `false` - `true` |
| **upn**  string | Configures the User Principal Name (UPN) for the account.  The format is `<username>@<domain>`.  This is the value set on the `userPrincipalName` LDAP attribute. |

## [Attributes](computer_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **windows** | Target OS/families that can be operated against |

## [Notes](computer_module.md#id5)

> **Note:**
>
> - See [win_domain_computer migration](docsite/guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-computer) for help on migrating from [community.windows.win_domain_computer](../../community/windows/win_domain_computer_module.md#ansible-collections-community-windows-win-domain-computer-module) to this module.
> - Some LDAP attributes can have only a single value set while others can have multiple. Some attributes are also read only and cannot be changed. It is recommended to look at the schema metadata for an attribute where `System-Only` are read only values and `Is-Single-Value` are attributes with only 1 value.
> - Attempting to set multiple values to a `Is-Single-Value` attribute results in undefined behaviour.
> - If running on a server that is not a Domain Controller, credential delegation through CredSSP or Kerberos with delegation must be used or the *domain_username*, *domain_password* must be set.

## [See Also](computer_module.md#id6)

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
> [microsoft.ad.offline_join](offline_join_module.md#ansible-collections-microsoft-ad-offline-join-module)
> :   Get the Offline Domain Join BLOB.
>
> [microsoft.ad.group](group_module.md#ansible-collections-microsoft-ad-group-module)
> :   Manage Active Directory group objects.
>
> [Migration guide](docsite/guide_migration.md#ansible-collections-microsoft-ad-docsite-guide-migration-migrated-modules-win-domain-computer)
> :   This module replaces `community.windows.win_domain_computer`. See the migration guide for details.
>
> [community.windows.win_domain_computer](../../community/windows/win_domain_computer_module.md#ansible-collections-community-windows-win-domain-computer-module)
> :   Manage computers in Active Directory.

## [Examples](computer_module.md#id7)

```yaml+jinja
- name: Add linux computer to Active Directory OU using a windows machine
  microsoft.ad.computer:
    name: one_linux_server
    sam_account_name: linux_server$
    dns_hostname: one_linux_server.my_org.local
    path: OU=servers,DC=my_org,DC=local
    description: Example of linux server
    enabled: yes
    state: present

- name: Remove linux computer from Active Directory using a windows machine
  microsoft.ad.computer:
    name: one_linux_server
    state: absent

- name: Add SPNs to computer
  microsoft.ad.computer:
    name: TheComputer
    spn:
      add:
      - HOST/TheComputer
      - HOST/TheComputer.domain.test
      - HOST/TheComputer.domain.test:1234

- name: Remove SPNs on the computer
  microsoft.ad.computer:
    name: TheComputer
    spn:
      remove:
      - HOST/TheComputer
      - HOST/TheComputer.domain.test
      - HOST/TheComputer.domain.test:1234

- name: Set the principals the computer trusts for delegation from
  microsoft.ad.computer:
    name: TheComputer
    delegates:
      set:
      - CN=FileShare,OU=Computers,DC=domain,DC=test
      - CN=DC,OU=Domain Controllers,DC=domain,DC=test
```

## [Return Values](computer_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **distinguished_name**  string | The `distinguishedName` of the AD object that was created, removed, or edited.  **Returned:** always  **Sample:** `"CN=MyComputer,CN=Computers,DC=domain,DC=test"` |
| **object_guid**  string | The `objectGUID` of the AD object that was created, removed, or edited.  If a new object was created in check mode, a GUID of 0s will be returned.  **Returned:** always  **Sample:** `"d84a141f-2b99-4f08-9da0-ed2d26864ba1"` |
| **sid**  string | The Security Identifier (SID) of the account managed.  If a new computer was created in check mode, the SID will be `S-1-5-0000`.  **Returned:** always  **Sample:** `"S-1-5-21-4151808797-3430561092-2843464588-1104"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/microsoft.ad/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/microsoft.ad)
- [Report an issue](https://github.com/ansible-collections/microsoft.ad/issues/new/choose)
- [Communication](index.md#communication-for-microsoft-ad)
