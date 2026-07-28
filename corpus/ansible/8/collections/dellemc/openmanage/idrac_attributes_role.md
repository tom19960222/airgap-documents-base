---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_attributes role – Role to configure the iDRAC attribute"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_attributes_role.html
fetched_at: 2026-07-28T02:04:59+00:00
---
# dellemc.openmanage.idrac_attributes role – Role to configure the iDRAC attribute

> **Note:**
>
> This role is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it use: `ansible-galaxy collection install dellemc.openmanage`.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_attributes`.

- [Entry point `main` – Role to configure the iDRAC attribute](idrac_attributes_role.md#entry-point-main-role-to-configure-the-idrac-attribute)

  - [Synopsis](idrac_attributes_role.md#synopsis)
  - [Parameters](idrac_attributes_role.md#parameters)

## [Entry point `main` – Role to configure the iDRAC attribute](idrac_attributes_role.md#id1)

New in dellemc.openmanage 7.6.0

### [Synopsis](idrac_attributes_role.md#id2)

- Role to configure the iDRAC system, manager and lifecycle attributes for Dell PowerEdge servers.

### [Parameters](idrac_attributes_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | iDRAC IP Address or hostname. |
| **https_port**  integer | iDRAC port.  **Default:** `443` |
| **https_timeout**  integer | The HTTPS socket level timeout in seconds.  **Default:** `30` |
| **idrac_attributes**  dictionary | Dictionary of iDRAC attributes and value. The attributes should be part of the Integrated Dell Remote Access Controller Attribute Registry.  To view the list of attributes in Attribute Registry for iDRAC9 and above, use the Role idrac_gather_facts with idrac components.  For iDRAC8 based servers, derive the manager attribute name from Server Configuration Profile.  If the manager attribute name in Server Configuration Profile is <GroupName>.<Instance>#<AttributeName> (for Example, ‘SNMP.1#AgentCommunity’) then the equivalent attribute name for Redfish is <GroupName>. <Instance>.<AttributeName> (for Example, ‘SNMP.1.AgentCommunity’). |
| **lifecycle_controller_attributes**  dictionary | Dictionary of Lifecycle Controller attributes and value. The attributes should be part of the Integrated Dell Remote Access Controller Attribute Registry.  To view the list of attributes in Attribute Registry for iDRAC9 and above, use the Role idrac_gather_facts with idrac components  For iDRAC8 based servers, derive the manager attribute name from Server Configuration Profile.  If the manager attribute name in Server Configuration Profile is <GroupName>.<Instance>#<AttributeName> (for Example, ‘LCAttributes.1#AutoUpdate’) then the equivalent attribute name for Redfish is <GroupName>.<Instance>.<AttributeName> (for Example, ‘LCAttributes.1.AutoUpdate’).” |
| **manager_id**  string | Redfish ID of the resource. If the Redfish ID of the resource is not specified, then the first ID from the Manager IDs list will be picked up. |
| **password**  string / required | iDRAC user password. |
| **system_attributes**  dictionary | Dictionary of System attributes and value. The attributes should be part of the Integrated Dell Remote Access Controller Attribute Registry.  To view the list of attributes in Attribute Registry for iDRAC9 and above, use the Role idrac_gather_facts with idrac components  For iDRAC8 based servers, derive the manager attribute name from Server Configuration Profile.  If the manager attribute name in Server Configuration Profile is <GroupName>.<Instance>#<AttributeName> (for Example, ‘ThermalSettings.1#ThermalProfile’) then the equivalent attribute name for Redfish is <GroupName>.<Instance>.<AttributeName> (for Example, ‘ThermalSettings.1.ThermalProfile’). |
| **username**  string / required | iDRAC username with admin privileges. |
| **validate_certs**  boolean | If `false`, the SSL certificates will not be validated.  Configure `false` only on personally controlled sites where self-signed certificates are used.  **Choices:**   - `false` - `true` ← (default) |

#### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
