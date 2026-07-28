---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_profile module – Create, modify, delete, assign, unassign and migrate a profile on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_profile_module.html
fetched_at: 2026-07-28T02:04:44+00:00
---
# dellemc.openmanage.ome_profile module – Create, modify, delete, assign, unassign and migrate a profile on OpenManage Enterprise

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
> see [Requirements](ome_profile_module.md#ansible-collections-dellemc-openmanage-ome-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_profile`.

New in dellemc.openmanage 3.1.0

- [Synopsis](ome_profile_module.md#synopsis)
- [Requirements](ome_profile_module.md#requirements)
- [Parameters](ome_profile_module.md#parameters)
- [Notes](ome_profile_module.md#notes)
- [Examples](ome_profile_module.md#examples)
- [Return Values](ome_profile_module.md#return-values)

## [Synopsis](ome_profile_module.md#id1)

- This module allows to create, modify, delete, assign, unassign, and migrate a profile on OpenManage Enterprise.

## [Requirements](ome_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | Attributes for `modify` and `assign`. |
| **Attributes**  list / elements=dictionary | List of attributes to be modified, when *command* is `modify`.  List of attributes to be overridden when *command* is `assign`.  Use the *Id* If the attribute Id is available. If not, use the comma separated I (DisplayName). For more details about using the *DisplayName*, see the example provided. |
| **Options**  dictionary | Provides the different shut down options.  This is applicable when *command* is `assign`. |
| **Schedule**  dictionary | Schedule for profile deployment.  This is applicable when *command* is `assign`. |
| **boot_to_network_iso**  dictionary | Details of the Share iso.  Applicable when *command* is `create`, `assign`, and `modify`. |
| **boot_to_network**  boolean / required | Enable or disable a network share.  **Choices:**   - `false` - `true` |
| **iso_path**  string | Specify the full ISO path including the share name. |
| **iso_timeout**  integer | Set the number of hours that the network ISO file will remain mapped to the target device(s).  **Choices:**   - `1` - `2` - `4` ← (default) - `8` - `16` |
| **share_ip**  string | IP address of the network share. |
| **share_password**  string | User password when *share_type* is `CIFS`. |
| **share_type**  string | Type of network share.  **Choices:**   - `"NFS"` - `"CIFS"` |
| **share_user**  string | User name when *share_type* is `CIFS`. |
| **workgroup**  string | User workgroup when *share_type* is `CIFS`. |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **command**  string | `create` creates new profiles.  `modify` modifies an existing profile. Only *name*, *description*, *boot_to_network_iso*, and *attributes* can be modified.  `delete` deletes an existing profile.  `assign` Deploys an existing profile on a target device and returns a task ID.  `unassign` unassigns a profile from a specified target and returns a task ID.  `migrate` migrates an existing profile and returns a task ID.  **Choices:**   - `"create"` ← (default) - `"modify"` - `"delete"` - `"assign"` - `"unassign"` - `"migrate"` |
| **description**  string | Description of the profile. |
| **device_id**  integer | ID of the target device.  This is applicable when *command* is `assign` and `migrate`.  This option is mutually exclusive with *device_service_tag*. |
| **device_service_tag**  string | Identifier of the target device.  This is typically 7 to 8 characters in length.  Applicable when *command* is `assign`, and `migrate`.  This option is mutually exclusive with *device_id*.  If the device does not exist when *command* is `assign` then the profile is auto-deployed. |
| **filters**  dictionary | Filters the profiles based on selected criteria.  This is applicable when *command* is `delete` or `unassign`.  This supports suboption *ProfileIds* which takes a list of profile IDs.  This also supports OData filter expressions with the suboption *Filters*.  See OpenManage Enterprise REST API guide for the filtering options available.  *WARNING* When this option is used in case of `unassign`, task ID is not returned for any of the profiles affected. |
| **force**  boolean | Provides the option to force the migration of a profile even if the source device cannot be contacted.  This option is applicable when *command* is `migrate`.  **Choices:**   - `false` ← (default) - `true` |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **name**  string | Name of the profile.  This is applicable for modify, delete, assign, unassign, and migrate operations.  This option is mutually exclusive with *name_prefix* and *number_of_profiles*. |
| **name_prefix**  string | The name provided when creating a profile is used a prefix followed by the number assigned to it by OpenManage Enterprise.  This is applicable only for a create operation.  This option is mutually exclusive with *name*.  **Default:** `"Profile"` |
| **new_name**  string | New name of the profile.  Applicable when *command* is `modify`. |
| **number_of_profiles**  integer | Provide the number of profiles to be created.  This is applicable when *name_prefix* is used with `create`.  This option is mutually exclusive with *name*.  Openmanage Enterprise can create a maximum of 100 profiles.  **Default:** `1` |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **template_id**  integer | ID of the template.  This is applicable when *command* is `create`.  This option is mutually exclusive with *template_name*. |
| **template_name**  string | Name of the template for creating the profile(s).  This is applicable when *command* is `create`.  This option is mutually exclusive with *template_id*. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_profile_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise.
> - This module supports `check_mode`.
> - `assign` operation on a already assigned profile will not redeploy.

## [Examples](ome_profile_module.md#id5)

```yaml+jinja
---
- name: Create two profiles from a template
  dellemc.openmanage.ome_profile:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    template_name: "template 1"
    name_prefix: "omam_profile"
    number_of_profiles: 2

- name: Create profile with NFS share
  dellemc.openmanage.ome_profile:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: create
    template_name: "template 1"
    name_prefix: "omam_profile"
    number_of_profiles: 1
    boot_to_network_iso:
      boot_to_network: True
      share_type: NFS
      share_ip: "192.168.0.1"
      iso_path: "path/to/my_iso.iso"
      iso_timeout: 8

- name: Create profile with CIFS share
  dellemc.openmanage.ome_profile:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: create
    template_name: "template 1"
    name_prefix: "omam_profile"
    number_of_profiles: 1
    boot_to_network_iso:
      boot_to_network: True
      share_type: CIFS
      share_ip: "192.168.0.2"
      share_user: "username"
      share_password: "password"
      workgroup: "workgroup"
      iso_path: "\\path\\to\\my_iso.iso"
      iso_timeout: 8

- name: Modify profile name with NFS share and attributes
  dellemc.openmanage.ome_profile:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: modify
    name: "Profile 00001"
    new_name: "modified profile"
    description: "new description"
    boot_to_network_iso:
      boot_to_network: True
      share_type: NFS
      share_ip: "192.168.0.3"
      iso_path: "path/to/my_iso.iso"
      iso_timeout: 8
    attributes:
      Attributes:
        - Id: 4506
          Value: "server attr 1"
          IsIgnored: false
        - Id: 4507
          Value: "server attr 2"
          IsIgnored: false
        # Enter the comma separated string as appearing in the Detailed view on GUI
        # System -> Server Topology -> ServerTopology 1 Aisle Name
        - DisplayName: 'System, Server Topology, ServerTopology 1 Aisle Name'
          Value: Aisle 5
          IsIgnored: false

- name: Delete a profile using profile name
  dellemc.openmanage.ome_profile:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "delete"
    name: "Profile 00001"

- name: Delete profiles using filters
  dellemc.openmanage.ome_profile:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "delete"
    filters:
      SelectAll: True
      Filters: =contains(ProfileName,'Profile 00002')

- name: Delete profiles using profile list filter
  dellemc.openmanage.ome_profile:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "delete"
    filters:
      ProfileIds:
        - 17123
        - 16124

- name: Assign a profile to target along with network share
  dellemc.openmanage.ome_profile:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: assign
    name: "Profile 00001"
    device_id: 12456
    boot_to_network_iso:
      boot_to_network: True
      share_type: NFS
      share_ip: "192.168.0.1"
      iso_path: "path/to/my_iso.iso"
      iso_timeout: 8
    attributes:
      Attributes:
        - Id: 4506
          Value: "server attr 1"
          IsIgnored: true
      Options:
        ShutdownType: 0
        TimeToWaitBeforeShutdown: 300
        EndHostPowerState: 1
        StrictCheckingVlan: True
      Schedule:
        RunNow: True
        RunLater: False

- name: Unassign a profile using profile name
  dellemc.openmanage.ome_profile:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "unassign"
    name: "Profile 00003"

- name: Unassign profiles using filters
  dellemc.openmanage.ome_profile:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "unassign"
    filters:
      SelectAll: True
      Filters: =contains(ProfileName,'Profile 00003')

- name: Unassign profiles using profile list filter
  dellemc.openmanage.ome_profile:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "unassign"
    filters:
      ProfileIds:
        - 17123
        - 16123

- name: Migrate a profile
  dellemc.openmanage.ome_profile:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "migrate"
    name: "Profile 00001"
    device_id: 12456
```

## [Return Values](ome_profile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **job_id**  integer | Task ID created when *command* is `assign`, `migrate` or `unassign`.  `assign` and `unassign` operations do not trigger a task if a profile is auto-deployed.  **Returned:** when *command* is `assign`, `migrate` or `unassign`  **Sample:** `14123` |
| **msg**  string | Overall status of the profile operation.  **Returned:** always  **Sample:** `"Successfully created 2 profile(s)."` |
| **profile_ids**  list / elements=string | IDs of the profiles created.  **Returned:** when *command* is `create`  **Sample:** `[1234, 5678]` |

### Authors

- Jagadeesh N V (@jagadeeshnv)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
