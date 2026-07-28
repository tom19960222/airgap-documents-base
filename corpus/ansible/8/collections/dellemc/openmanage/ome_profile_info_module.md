---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_profile_info module – Retrieve profiles with attribute details"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_profile_info_module.html
fetched_at: 2026-07-28T02:04:44+00:00
---
# dellemc.openmanage.ome_profile_info module – Retrieve profiles with attribute details

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_profile_info_module.md#ansible-collections-dellemc-openmanage-ome-profile-info-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_profile_info`.

New in dellemc.openmanage 7.2.0

- [Synopsis](ome_profile_info_module.md#synopsis)
- [Requirements](ome_profile_info_module.md#requirements)
- [Parameters](ome_profile_info_module.md#parameters)
- [Notes](ome_profile_info_module.md#notes)
- [Examples](ome_profile_info_module.md#examples)
- [Return Values](ome_profile_info_module.md#return-values)

## [Synopsis](ome_profile_info_module.md#id1)

- This module retrieve profiles with attributes on OpenManage Enterprise or OpenManage Enterprise Modular.

## [Requirements](ome_profile_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9.6

## [Parameters](ome_profile_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **profile_id**  integer | Id of the profile.  This is mutually exclusive with *profile_name*, *system_query_options*, *template_id*, and *template_name*. |
| **profile_name**  string | Name of the profile.  This is mutually exclusive with *template_id*, *profile_id*, *system_query_options*, and *template_name*. |
| **system_query_options**  dictionary | Option for providing supported odata filters.  The profile list can be fetched and sorted based on ProfileName, TemplateName, TargetTypeId, TargetName, ChassisName, ProfileState, LastRunStatus, or ProfileModified.  This is mutually exclusive with *profile_name*, *profile_id*, *template_id*, and *template_name*.  `Note` If *profile_name*, *profile_id*, *template_id*, or *template_name* option is not provided, the module retrieves all the profiles. |
| **template_id**  integer | Provide the ID of the template to retrieve the list of profile(s) linked to it.  This is mutually exclusive with *profile_name*, *profile_id*, *system_query_options*, and *template_name*. |
| **template_name**  string | Provide the name of the template to retrieve the list of profile(s) linked to it.  This is mutually exclusive with *profile_name*, *profile_id*, *template_id*, and *system_query_options*. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_profile_info_module.md#id4)

> **Note:**
>
> - Run this module on a system that has direct access to Dell OpenManage Enterprise.
> - This module supports `check_mode`.

## [Examples](ome_profile_info_module.md#id5)

```yaml+jinja
---
- name: Retrieve all profiles
  dellemc.openmanage.ome_profile_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"

- name: Retrieve profile using the name
  dellemc.openmanage.ome_profile_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    profile_name: eprof 00001

- name: Retrieve profile using the id
  dellemc.openmanage.ome_profile_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    profile_id: 10129

- name: Retrieve the profiles using the template name
  dellemc.openmanage.ome_profile_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    template_name: t2

- name: Retrieve the profiles using the template id
  dellemc.openmanage.ome_profile_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    template_id: 11

- name: Retrieve the profiles based on the odata filters
  dellemc.openmanage.ome_profile_info:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    system_query_options:
      filter: TemplateName eq 'mytemplate'
      orderby: ProfileState
```

## [Return Values](ome_profile_info_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Status of profile information retrieval.  **Returned:** always  **Sample:** `"Successfully retrieved the profile information."` |
| **profile_info**  list / elements=dictionary | Information about the profile.  **Returned:** success  **Sample:** `[{"AttributeDetails": {"System": {"Server Operating System": {"ServerOS 1 Server Host Name": 4965}, "Server Topology": {"ServerTopology 1 Aisle Name": 4958, "ServerTopology 1 Data Center Name": 4957, "ServerTopology 1 Rack Name": 4959, "ServerTopology 1 Rack Slot": 4960, "ServerTopology 1 Room Name": 4963}}, "iDRAC": {"Active Directory": {"ActiveDirectory 1 Active Directory RAC Name": 4066}, "NIC Information": {"NIC 1 Enable VLAN": 4229, "NIC 1 VLAN ID": 4231}}}, "AttributeIdMap": {"4066": {"IsIgnored": true, "IsReadOnly": false, "Value": null}, "4229": {"IsIgnored": false, "IsReadOnly": false, "Value": "Disabled"}, "4231": {"IsIgnored": false, "IsReadOnly": false, "Value": "1"}, "4957": {"IsIgnored": true, "IsReadOnly": false, "Value": "Dell LAB"}, "4958": {"IsIgnored": true, "IsReadOnly": false, "Value": null}, "4959": {"IsIgnored": true, "IsReadOnly": false, "Value": "OMAMDEV"}, "4960": {"IsIgnored": true, "IsReadOnly": false, "Value": "10A"}, "4963": {"IsIgnored": true, "IsReadOnly": false, "Value": "second floor"}, "4965": {"IsIgnored": true, "IsReadOnly": false, "Value": "hostname"}}, "ChassisId": 0, "ChassisName": null, "CreatedBy": "admin", "CreatedDate": "2019-09-26 13:56:41.924966", "DataSchemaId": 8, "DeploymentTaskId": 0, "DeviceIdInSlot": 0, "EditedBy": null, "GroupId": 0, "GroupName": null, "Id": 71460, "LastDeployDate": "", "LastEditDate": "2020-12-11 08:27:20.500564", "LastRunStatus": 2200, "NetworkBootToIso": null, "ProfileDescription": "from source template: (Template)", "ProfileModified": 0, "ProfileName": "Profile 00001", "ProfileState": 0, "TargetId": 0, "TargetName": null, "TargetTypeId": 0, "TemplateId": 8, "TemplateName": "Template"}]` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
