---
collection: ansible
version: "8"
title: "microsoft.ad.object module – Manage Active Directory objects"
source_url: https://docs.ansible.com/projects/ansible/8/collections/microsoft/ad/object_module.html
fetched_at: 2026-07-28T02:40:52+00:00
---
# microsoft.ad.object module – Manage Active Directory objects

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
> see [Requirements](object_module.md#ansible-collections-microsoft-ad-object-module-requirements) for details.
>
> To use it in a playbook, specify: `microsoft.ad.object`.

- [Synopsis](object_module.md#synopsis)
- [Requirements](object_module.md#requirements)
- [Parameters](object_module.md#parameters)
- [Attributes](object_module.md#attributes)
- [Notes](object_module.md#notes)
- [See Also](object_module.md#see-also)
- [Examples](object_module.md#examples)
- [Return Values](object_module.md#return-values)

## [Synopsis](object_module.md#id1)

- Manages Active Directory objects and their attributes.

## [Requirements](object_module.md#id2)

The below requirements are needed on the host that executes this module.

- `ActiveDirectory` PowerShell module

## [Parameters](object_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | The attributes to either add, remove, or set on the AD object.  The value of each attribute option should be a dictionary where the key is the LDAP attribute, e.g. `firstName`, `comment` and the value is the value, or list of values, to set for that attribute.  The attribute value(s) can either be the raw string, integer, or bool value to add, remove, or set on the attribute in question.  The value can also be a dictionary with the *type* key set to `bytes`, `date_time`, `security_descriptor`, or `raw` and the value for this entry under the *value* key.  The `bytes` type has a value that is a base64 encoded string of the raw bytes to set.  The `date_time` type has a value that is the ISO 8601 DateTime string of the DateTime to set. The DateTime will be set as the Microsoft FILETIME integer value which is the number of 100 nanoseconds since 1601-01-01 in UTC.  The `security_descriptor` type has a value that is the Security Descriptor SDDL string used for the `nTSecurityDescriptor` attribute.  The `raw` type is the int, string, or boolean value to set.  String attribute values are compared using a case sensitive match on the AD object being managed.  See [LDAP attributes help](docsite/guide_attributes.md#ansible-collections-microsoft-ad-docsite-guide-attributes) for more information.  **Default:** `{}` |
| **add**  dictionary | A dictionary of all the attributes and their value(s) to add to the AD object being managed if they are not already present.  This is used for attributes that can contain multiple values, if the attribute only allows a single value, use *set* instead.  **Default:** `{}` |
| **remove**  dictionary | A dictionary of all the attributes and their value(s) to remove from the AD object being managed if they are present.  This is used for attributes that can contain multiple values, if the attribute only allows a single value, use *set* instead.  **Default:** `{}` |
| **set**  dictionary | A dictionary of all attributes and their value(s) to set on the AD object being managed.  This will replace any existing values if they do not match the ones being requested.  The order of attribute values are not checked only, only that the values requested are the only values on the object attribute.  Set this to null or an empty list to clear any values for the attribute.  **Default:** `{}` |
| **description**  string | The description of the AD object to set.  This is the value set on the `description` LDAP attribute. |
| **display_name**  string | The display name of the AD object to set.  This is the value of the `displayName` LDAP attribute. |
| **domain_password**  string | The password for *domain_username*. |
| **domain_server**  string | Specified the Active Directory Domain Services instance to connect to.  Can be in the form of an FQDN or NetBIOS name.  If not specified then the value is based on the default domain of the computer running PowerShell. |
| **domain_username**  string | The username to use when interacting with AD.  If this is not set then the user that is used for authentication will be the connection user.  Ansible will be unable to use the connection user unless auth is Kerberos with credential delegation or CredSSP, or become is used on the task. |
| **identity**  string | The identity of the AD object used to find the AD object to manage.  Must be specified if *name* is not set, when trying to rename the object with a new *name*, or when trying to move the object into a different *path*.  The identity can be in the form of a GUID representing the `objectGUID` value, the `userPrincipalName`, `sAMAccountName`, `objectSid`, or `distinguishedName`.  If omitted, the AD object to managed is selected by the `distinguishedName` using the format `CN={{ name }},{{ path }}`. If *path* is not defined, the `defaultNamingContext` is used instead. |
| **name**  string | The `name` of the AD object to manage.  If *identity* is specified, and the name of the object it found does not match this value, the object will be renamed.  This if *identity* must be set to find the object to manage.  This is not always going to be the same as the `sAMAccountName` for user objects. It is strictly the `name` of the object in the path specified. Use *identity* to select an object to manage by `sAMAccountName`. |
| **path**  string | The path of the OU or the container where the new object should exist in.  If creating a new object, the new object will be created at the path specified. If no path is specified then the `defaultNamingContext` of the domain will be used as the path for most object types.  If managing an existing object found by *identity*, the path of the found object will be moved to the one specified by this option. If no path is specified, the object will not be moved.  The modules [microsoft.ad.computer](computer_module.md#ansible-collections-microsoft-ad-computer-module), [microsoft.ad.user](user_module.md#ansible-collections-microsoft-ad-user-module), and [microsoft.ad.group](group_module.md#ansible-collections-microsoft-ad-group-module) have their own default path that is configured on the Active Directory domain controller.  This can be set to `microsoft.ad.default_path` which will equal the default value used when creating a new object. |
| **protect_from_deletion**  boolean | Marks the object as protected from accidental deletion.  This applies a deny access right from deleting the object normally and the protection needs to be removed before the object can be deleted through the GUI or any other tool outside Ansible.  Using *state=absent* will still delete the AD object even if it is marked as protected from deletion.  **Choices:**   - `false` - `true` |
| **state**  string | Set to `present` to ensure the AD object exists.  Set to `absent` to remove the AD object if it exists.  The option *name* must be set when *state=present*.  Using `absent` will recursively remove the AD object and any child objects if it’s a container. It will also remove the AD object even if the object is marked as protected from accidental deletion.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **type**  string | The object type of the AD object.  This corresponds to the `objectClass` of the AD object.  Some examples of a type are `user`, `computer`, `group`, `subnet`, `contact`, `container`.  This is required when *state=present*. |

## [Attributes](object_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full** | Can run in check_mode and return changed status prediction without modifying target |
| **diff_mode** | **Support:** **full** | Will return details on what has changed (or possibly needs changing in check_mode), when in diff mode |
| **platform** | **Platform:** **windows** | Target OS/families that can be operated against |

## [Notes](object_module.md#id5)

> **Note:**
>
> - This is a generic module used to create and manage any object type in Active Directory. It will not validate all the correct defaults are set for each type when it is created. If a type specific module is available to manage that AD object type it is recommend to use that.
> - Some LDAP attributes can have only a single value set while others can have multiple. Some attributes are also read only and cannot be changed. It is recommended to look at the schema metadata for an attribute where `System-Only` are read only values and `Is-Single-Value` are attributes with only 1 value.
> - Attempting to set multiple values to a `Is-Single-Value` attribute results in undefined behaviour.
> - If running on a server that is not a Domain Controller, credential delegation through CredSSP or Kerberos with delegation must be used or the *domain_username*, *domain_password* must be set.

## [See Also](object_module.md#id6)

> **See also:**
>
> [microsoft.ad.domain](domain_module.md#ansible-collections-microsoft-ad-domain-module)
> :   Ensures the existence of a Windows domain.
>
> [microsoft.ad.domain_controller](domain_controller_module.md#ansible-collections-microsoft-ad-domain-controller-module)
> :   Manage domain controller/member server state for a Windows host.
>
> [microsoft.ad.object_info](object_info_module.md#ansible-collections-microsoft-ad-object-info-module)
> :   Gather information an Active Directory object.
>
> [microsoft.ad.user](user_module.md#ansible-collections-microsoft-ad-user-module)
> :   Manage Active Directory users.
>
> [microsoft.ad.computer](computer_module.md#ansible-collections-microsoft-ad-computer-module)
> :   Manage Active Directory computer objects.
>
> [microsoft.ad.group](group_module.md#ansible-collections-microsoft-ad-group-module)
> :   Manage Active Directory group objects.

## [Examples](object_module.md#id7)

```yaml+jinja
# Use this to get all valid types in a domain environment
# (Get-ADObject -SearchBase (Get-ADRootDSE).subschemaSubentry -Filter * -Properties objectClasses).objectClasses |
#     Select-String -Pattern "Name\s+'(\w+)'" |
#     ForEach-Object { $_.Matches.Groups[1].Value } |
#     Sort-Object

- name: Create a contact object
  microsoft.ad.object:
    name: MyContact
    description: My Contact Description
    type: contact
    state: present

- name: Rename a contact object
  microsoft.ad.object:
    identity: '{{ contact_obj.object_guid }}'
    name: RenamedContact
    type: contact
    state: present

- name: Move a contact object
  microsoft.ad.object:
    identity: '{{ contact_object.object_guid }}'
    name: MyContact
    path: OU=Contacts,DC=domain,DC=test
    type: contact
    state: present

- name: Remove a contact object in default path
  microsoft.ad.object:
    name: MyContact
    state: absent

- name: Remove a contact object in custom path
  microsoft.ad.object:
    name: MyContact
    path: OU=Contacts,DC=domain,DC=test
    state: absent

- name: Remove a contact by identity
  microsoft.ad.object:
    identity: '{{ contact_obj.object_guid }}'
    state: absent

- name: Create container object with custom attributes
  microsoft.ad.object:
    name: App
    attributes:
      set:
        wWWHomePage: https://ansible.com
    type: container
    state: present

- name: Clear attribute of any value
  microsoft.ad.object:
    name: App
    attributes:
      set:
        wWWHomePage: ~
    type: container
    state: present

- name: Edit object security with Everyone Allow All access
  microsoft.ad.object:
    name: App
    attributes:
      add:
        nTSecurityDescriptor:
          type: security_descriptor
          value: O:DAG:DAD:PAI(A;CI;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;WD)
    type: container
    state: present

- name: Ensure multiple values are present in attribute
  microsoft.ad.object:
    name: App
    attributes:
      add:
        extensionName:
        - value 1
        - value 2
    type: container
    state: present

- name: Ensure multiple values are not present in attribute
  microsoft.ad.object:
    name: App
    attributes:
      remove:
        extensionName:
        - value 1
        - value 3
    type: container
    state: present
```

## [Return Values](object_module.md#id8)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **distinguished_name**  string | The `distinguishedName` of the AD object that was created, removed, or edited.  **Returned:** always  **Sample:** `"CN=TestUser,CN=Users,DC=domain,DC=test"` |
| **object_guid**  string | The `objectGUID` of the AD object that was created, removed, or edited.  If a new object was created in check mode, a GUID of 0s will be returned.  **Returned:** always  **Sample:** `"d84a141f-2b99-4f08-9da0-ed2d26864ba1"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/microsoft.ad/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Repository (Sources)](https://github.com/ansible-collections/microsoft.ad)
- [Report an issue](https://github.com/ansible-collections/microsoft.ad/issues/new/choose)
- [Communication](index.md#communication-for-microsoft-ad)
