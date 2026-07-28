---
collection: ansible
version: "8"
title: "dellemc.openmanage.redfish_storage_volume module – Manages the storage volume configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/redfish_storage_volume_module.html
fetched_at: 2026-07-28T02:04:57+00:00
---
# dellemc.openmanage.redfish_storage_volume module – Manages the storage volume configuration

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
> see [Requirements](redfish_storage_volume_module.md#ansible-collections-dellemc-openmanage-redfish-storage-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.redfish_storage_volume`.

New in dellemc.openmanage 2.1.0

- [Synopsis](redfish_storage_volume_module.md#synopsis)
- [Requirements](redfish_storage_volume_module.md#requirements)
- [Parameters](redfish_storage_volume_module.md#parameters)
- [Notes](redfish_storage_volume_module.md#notes)
- [Examples](redfish_storage_volume_module.md#examples)
- [Return Values](redfish_storage_volume_module.md#return-values)

## [Synopsis](redfish_storage_volume_module.md#id1)

- This module allows to create, modify, initialize, or delete a single storage volume.

## [Requirements](redfish_storage_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](redfish_storage_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseuri**  string / required | IP address of the target out-of-band controller. For example- <ipaddress>:<port>. |
| **block_size_bytes**  integer | Block size in bytes.Only applicable when *state* is `present`. |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **capacity_bytes**  string | Volume size in bytes.  Only applicable when *state* is `present`. |
| **command**  string | `initialize` initializes an existing storage volume for a specified *volume_id*.  **Choices:**   - `"initialize"` |
| **controller_id**  string | Fully Qualified Device Descriptor (FQDD) of the storage controller.  For example- RAID.Slot.1-1.  This option is mandatory when *state* is `present` while creating a volume. |
| **drives**  list / elements=string | FQDD of the Physical disks.  For example- Disk.Bay.0:Enclosure.Internal.0-1:RAID.Slot.1-1.  Only applicable when *state* is `present` when creating a new volume. |
| **encrypted**  boolean | Indicates whether volume is currently utilizing encryption or not.  Only applicable when *state* is `present`.  **Choices:**   - `false` - `true` |
| **encryption_types**  string | The following encryption types can be selected.  `ControllerAssisted` The volume is encrypted by the storage controller entity.  `NativeDriveEncryption` The volume utilizes the native drive encryption capabilities of the drive hardware.  `SoftwareAssisted` The volume is encrypted by the software running on the system or the operating system.  Only applicable when *state* is `present`.  **Choices:**   - `"NativeDriveEncryption"` - `"ControllerAssisted"` - `"SoftwareAssisted"` |
| **initialize_type**  string | Initialization type of existing volume.  Only applicable when *command* is `initialize`.  **Choices:**   - `"Fast"` ← (default) - `"Slow"` |
| **name**  string | Name of the volume to be created.  Only applicable when *state* is `present`. |
| **oem**  dictionary | Includes OEM extended payloads.  Only applicable when *state* is *present*. |
| **optimum_io_size_bytes**  integer | Stripe size value must be in multiples of 64 \* 1024.  Only applicable when *state* is `present`. |
| **password**  string / required | Password of the target out-of-band controller. |
| **state**  string | `present` creates a storage volume for the specified I (controller_id), or modifies the storage volume for the specified I (volume_id). “Note: Modification of an existing volume properties depends on drive and controller capabilities”.  `absent` deletes the volume for the specified *volume_id*.  **Choices:**   - `"present"` - `"absent"` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | Username of the target out-of-band controller. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |
| **volume_id**  string | FQDD of existing volume.  For example- Disk.Virtual.4:RAID.Slot.1-1.  This option is mandatory in the following scenarios,  *state* is `present`, when updating a volume.  *state* is `absent`, when deleting a volume.  *command* is `initialize`, when initializing a volume. |
| **volume_type**  string | One of the following volume types must be selected to create a volume.  `Mirrored` The volume is a mirrored device.  `NonRedundant` The volume is a non-redundant storage device.  `SpannedMirrors` The volume is a spanned set of mirrored devices.  `SpannedStripesWithParity` The volume is a spanned set of devices which uses parity to retain redundant information.  `StripedWithParity` The volume is a device which uses parity to retain redundant information.  **Choices:**   - `"NonRedundant"` - `"Mirrored"` - `"StripedWithParity"` - `"SpannedMirrors"` - `"SpannedStripesWithParity"` |

## [Notes](redfish_storage_volume_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Redfish APIs.
> - This module supports `check_mode`.
> - This module always reports changes when *name* and *volume_id* are not specified. Either *name* or *volume_id* is required to support `check_mode`.

## [Examples](redfish_storage_volume_module.md#id5)

```yaml+jinja
---
- name: Create a volume with supported options
  dellemc.openmanage.redfish_storage_volume:
    baseuri: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "present"
    volume_type: "Mirrored"
    name: "VD0"
    controller_id: "RAID.Slot.1-1"
    drives:
      - Disk.Bay.5:Enclosure.Internal.0-1:RAID.Slot.1-1
      - Disk.Bay.6:Enclosure.Internal.0-1:RAID.Slot.1-1
    block_size_bytes: 512
    capacity_bytes: 299439751168
    optimum_io_size_bytes: 65536
    encryption_types: NativeDriveEncryption
    encrypted: true

- name: Create a volume with minimum options
  dellemc.openmanage.redfish_storage_volume:
    baseuri: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "present"
    controller_id: "RAID.Slot.1-1"
    volume_type: "NonRedundant"
    drives:
       - Disk.Bay.1:Enclosure.Internal.0-1:RAID.Slot.1-1

- name: Modify a volume's encryption type settings
  dellemc.openmanage.redfish_storage_volume:
    baseuri: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "present"
    volume_id: "Disk.Virtual.5:RAID.Slot.1-1"
    encryption_types: "ControllerAssisted"
    encrypted: true

- name: Delete an existing volume
  dellemc.openmanage.redfish_storage_volume:
    baseuri: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    volume_id: "Disk.Virtual.5:RAID.Slot.1-1"

- name: Initialize an existing volume
  dellemc.openmanage.redfish_storage_volume:
    baseuri: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    command: "initialize"
    volume_id: "Disk.Virtual.6:RAID.Slot.1-1"
    initialize_type: "Slow"
```

## [Return Values](redfish_storage_volume_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of a http error.  **Returned:** on http error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to perform configuration operations because a configuration job for the device already exists.", "MessageArgs": [], "MessageArgs@odata.count": 0, "MessageId": "IDRAC.1.6.STOR023", "RelatedProperties": [], "RelatedProperties@odata.count": 0, "Resolution": "Wait for the current job for the device to complete or cancel the current job before attempting more configuration operations on the device.", "Severity": "Informational"}], "code": "Base.1.2.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information"}}` |
| **msg**  string | Overall status of the storage configuration operation.  **Returned:** always  **Sample:** `"Successfully submitted create volume task."` |
| **task**  dictionary | Returns ID and URI of the created task.  **Returned:** success  **Sample:** `{"id": "JID_XXXXXXXXXXXXX", "uri": "/redfish/v1/TaskService/Tasks/JID_XXXXXXXXXXXXX"}` |

### Authors

- Sajna Shetty(@Sajna-Shetty)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
