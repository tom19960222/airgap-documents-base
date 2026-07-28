---
collection: ansible
version: "8"
title: "community.windows.win_domain_object_info module – Gather information an Active Directory object"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_domain_object_info_module.html
fetched_at: 2026-07-28T02:01:49+00:00
---
# community.windows.win_domain_object_info module – Gather information an Active Directory object

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_domain_object_info`.

- [Synopsis](win_domain_object_info_module.md#synopsis)
- [Parameters](win_domain_object_info_module.md#parameters)
- [Notes](win_domain_object_info_module.md#notes)
- [Examples](win_domain_object_info_module.md#examples)
- [Return Values](win_domain_object_info_module.md#return-values)

## [Synopsis](win_domain_object_info_module.md#id1)

- Gather information about multiple Active Directory object(s).

## [Parameters](win_domain_object_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **domain_password**  string | The password for `domain_username`. |
| **domain_server**  string | Specified the Active Directory Domain Services instance to connect to.  Can be in the form of an FQDN or NetBIOS name.  If not specified then the value is based on the default domain of the computer running PowerShell. |
| **domain_username**  string | The username to use when interacting with AD.  If this is not set then the user that is used for authentication will be the connection user.  Ansible will be unable to use the connection user unless auth is Kerberos with credential delegation or CredSSP, or become is used on the task. |
| **filter**  string | Specifies a query string using the PowerShell Expression Language syntax.  This follows the same rules and formatting as the `-Filter` parameter for the PowerShell AD cmdlets exception there is no variable substitutions.  This is mutually exclusive with *identity* and *ldap_filter*. |
| **identity**  string | Specifies a single Active Directory object by its distinguished name or its object GUID.  This is mutually exclusive with *filter* and *ldap_filter*.  This cannot be used with either the *search_base* or *search_scope* options. |
| **include_deleted**  boolean | Also search for deleted Active Directory objects.  **Choices:**   - `false` ← (default) - `true` |
| **ldap_filter**  string | Like *filter* but this is a tradiitional LDAP query string to filter the objects to return.  This is mutually exclusive with *filter* and *identity*. |
| **properties**  list / elements=string | A list of properties to return.  If a property is `*`, all properties that have a set value on the AD object will be returned.  If a property is valid on the object but not set, it is only returned if defined explicitly in this option list.  The properties `DistinguishedName`, `Name`, `ObjectClass`, and `ObjectGUID` are always returned.  Specifying multiple properties can have a performance impact, it is best to only return what is needed.  If an invalid property is specified then the module will display a warning for each object it is invalid on. |
| **search_base**  string | Specify the Active Directory path to search for objects in.  This cannot be set with *identity*.  By default the search base is the default naming context of the target AD instance which is the DN returned by “(Get-ADRootDSE).defaultNamingContext”. |
| **search_scope**  string | Specify the scope of when searching for an object in the `search_base`.  `base` will limit the search to the base object so the maximum number of objects returned is always one. This will not search any objects inside a container..  `one_level` will search the current path and any immediate objects in that path.  `subtree` will search the current path and all objects of that path recursively.  This cannot be set with *identity*.  **Choices:**   - `"base"` - `"one_level"` - `"subtree"` |

## [Notes](win_domain_object_info_module.md#id3)

> **Note:**
>
> - The `sAMAccountType_AnsibleFlags` and `userAccountControl_AnsibleFlags` return property is something set by the module itself as an easy way to view what those flags represent. These properties cannot be used as part of the *filter* or *ldap_filter* and are automatically added if those properties were requested.
> - This must be run on a host that has the ActiveDirectory powershell module installed.

## [Examples](win_domain_object_info_module.md#id4)

```yaml+jinja
- name: Get all properties for the specified account using its DistinguishedName
  community.windows.win_domain_object_info:
    identity: CN=Username,CN=Users,DC=domain,DC=com
    properties: '*'

- name: Get the SID for all user accounts as a filter
  community.windows.win_domain_object_info:
    filter: ObjectClass -eq 'user' -and objectCategory -eq 'Person'
    properties:
    - objectSid

- name: Get the SID for all user accounts as a LDAP filter
  community.windows.win_domain_object_info:
    ldap_filter: (&(objectClass=user)(objectCategory=Person))
    properties:
    - objectSid

- name: Search all computer accounts in a specific path that were added after February 1st
  community.windows.win_domain_object_info:
    filter: objectClass -eq 'computer' -and whenCreated -gt '20200201000000.0Z'
    properties: '*'
    search_scope: one_level
    search_base: CN=Computers,DC=domain,DC=com
```

## [Return Values](win_domain_object_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **objects**  list / elements=dictionary | A list of dictionaries that are the Active Directory objects found and the properties requested.  The dict’s keys are the property name and the value is the value for the property.  All date properties are return in the ISO 8601 format in the UTC timezone.  All SID properties are returned as a dict with the keys `Sid` as the SID string and `Name` as the translated SID account name.  All byte properties are returned as a base64 string.  All security descriptor properties are returned as the SDDL string of that descriptor.  The properties `DistinguishedName`, `Name`, `ObjectClass`, and `ObjectGUID` are always returned.  **Returned:** always  **Sample:** `"[{\n  \"accountExpires\": 0,\n  \"adminCount\": 1,\n  \"CanonicalName\": \"domain.com/Users/Administrator\",\n  \"CN\": \"Administrator\",\n  \"Created\": \"2020-01-13T09:03:22.0000000Z\",\n  \"Description\": \"Built-in account for administering computer/domain\",\n  \"DisplayName\": null,\n  \"DistinguishedName\": \"CN=Administrator,CN=Users,DC=domain,DC=com\",\n  \"memberOf\": [\n    \"CN=Group Policy Creator Owners,CN=Users,DC=domain,DC=com\",\n    \"CN=Domain Admins\",CN=Users,DC=domain,DC=com\"\n  ],\n  \"Name\": \"Administrator\",\n  \"nTSecurityDescriptor\": \"O:DAG:DAD:PAI(A;;LCRPLORC;;;AU)(A;;CCDCLCSWRPWPDTLOCRSDRCWDWO;;;SY)(A;;CCDCLCSWRPWPLOCRSDRCWDWO;;;BA)\",\n  \"ObjectCategory\": \"CN=Person,CN=Schema,CN=Configuration,DC=domain,DC=com\",\n  \"ObjectClass\": \"user\",\n  \"ObjectGUID\": \"c8c6569e-4688-4f3c-8462-afc4ff60817b\",\n  \"objectSid\": {\n    \"Sid\": \"S-1-5-21-2959096244-3298113601-420842770-500\",\n    \"Name\": \"DOMAIN\\Administrator\"\n  },\n  \"sAMAccountName\": \"Administrator\",\n}]\n"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
