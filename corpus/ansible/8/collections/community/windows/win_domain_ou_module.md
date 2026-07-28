---
collection: ansible
version: "8"
title: "community.windows.win_domain_ou module – Manage Active Directory Organizational Units"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/windows/win_domain_ou_module.html
fetched_at: 2026-07-28T02:01:49+00:00
---
# community.windows.win_domain_ou module – Manage Active Directory Organizational Units

> **Note:**
>
> This module is part of the [community.windows collection](https://galaxy.ansible.com/ui/repo/published/community/windows/) (version 1.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.windows`.
> You need further requirements to be able to use this module,
> see [Requirements](win_domain_ou_module.md#ansible-collections-community-windows-win-domain-ou-module-requirements) for details.
>
> To use it in a playbook, specify: `community.windows.win_domain_ou`.

New in community.windows 1.8.0

- [Synopsis](win_domain_ou_module.md#synopsis)
- [Requirements](win_domain_ou_module.md#requirements)
- [Parameters](win_domain_ou_module.md#parameters)
- [Examples](win_domain_ou_module.md#examples)
- [Return Values](win_domain_ou_module.md#return-values)

## [Synopsis](win_domain_ou_module.md#id1)

- Manage Active Directory Organizational Units
- Adds, Removes and Modifies Active Directory Organizational Units
- Task should be delegated to a Windows Active Directory Domain Controller

## [Requirements](win_domain_ou_module.md#id2)

The below requirements are needed on the host that executes this module.

- This module requires Windows Server 2012 or Newer
- Powershell ActiveDirectory Module

## [Parameters](win_domain_ou_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **domain_password**  string | The password for the domain you are accessing |
| **domain_server**  string | Specifies the Active Directory Domain Services instance to connect to.  Can be in the form of an FQDN or NetBIOS name.  If not specified then the value is based on the domain of the computer running PowerShell. |
| **domain_username**  string | The username to use when interacting with AD.  If this is not set then the user Ansible used to log in with will be used instead when using CredSSP or Kerberos with credential delegation. |
| **filter**  string | filter for lookup of ou.  **Default:** `"*"` |
| **name**  string / required | The name of the Organizational Unit |
| **path**  string | Specifies the X.500 path of the OU or container where the new object is created.  defaults to adding ou at base of domain connected to. |
| **properties**  dictionary | Free form dict of properties for the organizational unit. Follows LDAP property names, like `StreetAddress` or `PostalCode`. |
| **protected**  boolean | Indicates whether to prevent the object from being deleted. When this *protected=true*, you cannot delete the corresponding object without changing the value of the property.  **Choices:**   - `false` ← (default) - `true` |
| **recursive**  boolean | Removes the OU and any child items it contains.  You must specify this parameter to remove an OU that is not empty.  **Choices:**   - `false` ← (default) - `true` |
| **state**  string | Specifies the desired state of the OU.  When *state=present* the module will attempt to create the specified OU if it does not already exist.  When *state=absent*, the module will remove the specified OU.  When *state=absent* and *recursive=true*, the module will remove all the OU and all child OU’s.  **Choices:**   - `"present"` ← (default) - `"absent"` |

## [Examples](win_domain_ou_module.md#id4)

```yaml+jinja
---
- name: Ensure OU is present & protected
  community.windows.win_domain_ou:
    name: AnsibleFest
    state: present

- name: Ensure OU is present & protected
  community.windows.win_domain_ou:
    name: EUC Users
    path: "DC=euc,DC=vmware,DC=lan"
    state: present
    protected: true
  delegate_to: win-ad1.euc.vmware.lab

- name: Ensure OU is absent
  community.windows.win_domain_ou:
    name: EUC Users
    path: "DC=euc,DC=vmware,DC=lan"
    state: absent
  delegate_to: win-ad1.euc.vmware.lab

- name: Ensure OU is present with specific properties
  community.windows.win_domain_ou:
    name: WS1Users
    path: "CN=EUC Users,DC=euc,DC=vmware,DC=lan"
    protected: true
    properties:
      city: Sandy Springs
      state: Georgia
      StreetAddress: 1155 Perimeter Center West
      country: US
      description: EUC Business Unit
      PostalCode: 30189
  delegate_to: win-ad1.euc.vmware.lab

- name: Ensure OU updated with new properties
  community.windows.win_domain_ou:
    name: WS1Users
    path: DC=euc,DC=vmware,DC=lan
    protected: false
    properties:
      city: Atlanta
      state: Georgia
      managedBy: jzollo@vmware.com
  delegate_to: win-ad1.euc.vmware.lab
```

## [Return Values](win_domain_ou_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ou**  dictionary | New/Updated organizational unit parameters  **Returned:** When *state=present*  **Sample:** `{"AddedProperties": [], "City": "Sandy Springs", "Country": null, "DistinguishedName": "OU=VMW Atlanta,DC=ansible,DC=test", "LinkedGroupPolicyObjects": [], "ManagedBy": null, "ModifiedProperties": [], "Name": "VMW Atlanta", "ObjectClass": "organizationalUnit", "ObjectGUID": "3e987e30-93ad-4229-8cd0-cff6a91275e4", "PostalCode": null, "PropertyCount": 11, "PropertyNames": "City Country DistinguishedName LinkedGroupPolicyObjects ManagedBy Name ObjectClass ObjectGUID PostalCode State StreetAddress", "RemovedProperties": [], "State": "Georgia", "StreetAddress": "1155 Perimeter Center West"}` |
| **path**  string | Base ou path used by module either when provided *path=DC=Ansible,DC=Test* or derived by module.  **Returned:** always  **Sample:** `"{'path': 'DC=ansible,DC=test'}"` |

### Authors

- Joe Zollo (@joezollo)
- Larry Lane (@gamethis)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.windows/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.windows)
- [Communication](index.md#communication-for-community-windows)
