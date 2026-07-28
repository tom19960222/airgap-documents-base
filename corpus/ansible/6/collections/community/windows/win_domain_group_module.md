---
collection: ansible
version: "6"
title: "community.windows.win_domain_group module – Creates, modifies or removes domain groups"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/windows/win_domain_group_module.html
fetched_at: 2026-07-27T17:23:19+00:00
---
# community.windows.win_domain_group module – Creates, modifies or removes domain groups

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/community/windows) (version 1.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
>
> To use it in a playbook, specify: `community.windows.win_domain_group`.

- [Synopsis](win_domain_group_module.md#synopsis)
- [Parameters](win_domain_group_module.md#parameters)
- [Notes](win_domain_group_module.md#notes)
- [See Also](win_domain_group_module.md#see-also)
- [Examples](win_domain_group_module.md#examples)
- [Return Values](win_domain_group_module.md#return-values)

## [Synopsis](win_domain_group_module.md#id1)

- Creates, modifies or removes groups in Active Directory.
- For local groups, use the [ansible.windows.win_group](../../ansible/windows/win_group_module.md#ansible-collections-ansible-windows-win-group-module) module instead.

## [Parameters](win_domain_group_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | A dict of custom LDAP attributes to set on the group.  This can be used to set custom attributes that are not exposed as module parameters, e.g. `mail`.  See the examples on how to format this parameter. |
| **category**  string | The category of the group, this is the value to assign to the LDAP `groupType` attribute.  If a new group is created then `security` will be used by default.  Choices:   - `"distribution"` - `"security"` |
| **description**  string | The value to be assigned to the LDAP `description` attribute. |
| **display_name**  string | The value to assign to the LDAP `displayName` attribute. |
| **domain_password**  string | The password for `username`. |
| **domain_server**  string | Specifies the Active Directory Domain Services instance to connect to.  Can be in the form of an FQDN or NetBIOS name.  If not specified then the value is based on the domain of the computer running PowerShell. |
| **domain_username**  string | The username to use when interacting with AD.  If this is not set then the user Ansible used to log in with will be used instead. |
| **ignore_protection**  boolean | Will ignore the `ProtectedFromAccidentalDeletion` flag when deleting or moving a group.  The module will fail if one of these actions need to occur and this value is set to `no`.  Choices:   - `false` ← (default) - `true` |
| **managed_by**  string | The value to be assigned to the LDAP `managedBy` attribute.  This value can be in the forms `Distinguished Name`, `objectGUID`, `objectSid` or `sAMAccountName`, see examples for more details. |
| **name**  string / required | The name of the group to create, modify or remove.  This value can be in the forms `Distinguished Name`, `objectGUID`, `objectSid` or `sAMAccountName`, see examples for more details. |
| **organizational_unit**  aliases: ou, path  string | The full LDAP path to create or move the group to.  This should be the path to the parent object to create or move the group to.  See examples for details of how this path is formed. |
| **protect**  boolean | Will set the `ProtectedFromAccidentalDeletion` flag based on this value.  This flag stops a user from deleting or moving a group to a different path.  Choices:   - `false` - `true` |
| **scope**  string | The scope of the group.  If `state=present` and the group doesn’t exist then this must be set.  Choices:   - `"domainlocal"` - `"global"` - `"universal"` |
| **state**  string | If `state=present` this module will ensure the group is created and is configured accordingly.  If `state=absent` this module will delete the group if it exists  Choices:   - `"absent"` - `"present"` ← (default) |

## [Notes](win_domain_group_module.md#id3)

> **Note:**
>
> - This must be run on a host that has the ActiveDirectory powershell module installed.

## [See Also](win_domain_group_module.md#id4)

> **See also:**
>
> [ansible.windows.win_domain](../../ansible/windows/win_domain_module.md#ansible-collections-ansible-windows-win-domain-module)
> :   Ensures the existence of a Windows domain.
>
> [ansible.windows.win_domain_controller](../../ansible/windows/win_domain_controller_module.md#ansible-collections-ansible-windows-win-domain-controller-module)
> :   Manage domain controller/member server state for a Windows host.
>
> [community.windows.win_domain_computer](win_domain_computer_module.md#ansible-collections-community-windows-win-domain-computer-module)
> :   Manage computers in Active Directory.
>
> [ansible.windows.win_domain_membership](../../ansible/windows/win_domain_membership_module.md#ansible-collections-ansible-windows-win-domain-membership-module)
> :   Manage domain/workgroup membership for a Windows host.
>
> [community.windows.win_domain_user](win_domain_user_module.md#ansible-collections-community-windows-win-domain-user-module)
> :   Manages Windows Active Directory user accounts.
>
> [ansible.windows.win_group](../../ansible/windows/win_group_module.md#ansible-collections-ansible-windows-win-group-module)
> :   Add and remove local groups.
>
> [ansible.windows.win_group_membership](../../ansible/windows/win_group_membership_module.md#ansible-collections-ansible-windows-win-group-membership-module)
> :   Manage Windows local group membership.

## [Examples](win_domain_group_module.md#id5)

```yaml+jinja
- name: Ensure the group Cow exists using sAMAccountName
  community.windows.win_domain_group:
    name: Cow
    scope: global
    path: OU=groups,DC=ansible,DC=local

- name: Ensure the group Cow doesn't exist using the Distinguished Name
  community.windows.win_domain_group:
    name: CN=Cow,OU=groups,DC=ansible,DC=local
    state: absent

- name: Delete group ignoring the protection flag
  community.windows.win_domain_group:
    name: Cow
    state: absent
    ignore_protection: yes

- name: Create group with delete protection enabled and custom attributes
  community.windows.win_domain_group:
    name: Ansible Users
    scope: domainlocal
    category: security
    attributes:
      mail: helpdesk@ansible.com
      wWWHomePage: www.ansible.com
    ignore_protection: yes

- name: Change the OU of a group using the SID and ignore the protection flag
  community.windows.win_domain_group:
    name: S-1-5-21-2171456218-3732823212-122182344-1189
    scope: global
    organizational_unit: OU=groups,DC=ansible,DC=local
    ignore_protection: yes

- name: Add managed_by user
  community.windows.win_domain_group:
    name: Group Name Here
    managed_by: Domain Admins

- name: Add group and specify the AD domain services to use for the create
  community.windows.win_domain_group:
    name: Test Group
    domain_username: user@CORP.ANSIBLE.COM
    domain_password: Password01!
    domain_server: corp-DC12.corp.ansible.com
    scope: domainlocal
```

## [Return Values](win_domain_group_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **attributes**  dictionary | Custom attributes that were set by the module. This does not show all the custom attributes rather just the ones that were set by the module.  Returned: group exists and attributes are set on the module invocation  Sample: `{"mail": "helpdesk@ansible.com", "wWWHomePage": "www.ansible.com"}` |
| **canonical_name**  string | The canonical name of the group.  Returned: group exists  Sample: `"ansible.local/groups/Cow"` |
| **category**  string | The Group type value of the group, i.e. Security or Distribution.  Returned: group exists  Sample: `"Security"` |
| **created**  boolean | Whether a group was created  Returned: always  Sample: `true` |
| **description**  string | The Description of the group.  Returned: group exists  Sample: `"Group Description"` |
| **display_name**  string | The Display name of the group.  Returned: group exists  Sample: `"Users who connect through RDP"` |
| **distinguished_name**  string | The full Distinguished Name of the group.  Returned: group exists  Sample: `"CN=Cow,OU=groups,DC=ansible,DC=local"` |
| **group_scope**  string | The Group scope value of the group.  Returned: group exists  Sample: `"Universal"` |
| **guid**  string | The guid of the group.  Returned: group exists  Sample: `"512a9adb-3fc0-4a26-9df0-e6ea1740cf45"` |
| **managed_by**  string | The full Distinguished Name of the AD object that is set on the managedBy attribute.  Returned: group exists  Sample: `"CN=Domain Admins,CN=Users,DC=ansible,DC=local"` |
| **name**  string | The name of the group.  Returned: group exists  Sample: `"Cow"` |
| **protected_from_accidental_deletion**  boolean | Whether the group is protected from accidental deletion.  Returned: group exists  Sample: `true` |
| **sid**  string | The Security ID of the group.  Returned: group exists  Sample: `"S-1-5-21-2171456218-3732823212-122182344-1189"` |

### Authors

- Jordan Borean (@jborean93)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.windows)
[Communication](index.md#communication-for-community-windows)
