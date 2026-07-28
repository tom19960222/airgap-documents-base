---
collection: ansible
version: "8"
title: "dellemc.openmanage.redfish_storage_volume role – Role to manage the storage volume configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/redfish_storage_volume_role.html
fetched_at: 2026-07-28T02:05:07+00:00
---
# dellemc.openmanage.redfish_storage_volume role – Role to manage the storage volume configuration

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
> To use it in a playbook, specify: `dellemc.openmanage.redfish_storage_volume`.

- [Entry point `main` – Role to manage the storage volume configuration](redfish_storage_volume_role.md#entry-point-main-role-to-manage-the-storage-volume-configuration)

  - [Synopsis](redfish_storage_volume_role.md#synopsis)
  - [Parameters](redfish_storage_volume_role.md#parameters)

## [Entry point `main` – Role to manage the storage volume configuration](redfish_storage_volume_role.md#id1)

New in dellemc.openmanage 7.5.0

### [Synopsis](redfish_storage_volume_role.md#id2)

- Role to create, modify, initialize, or delete a single storage volume.

### [Parameters](redfish_storage_volume_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **block_size_bytes**  integer | Block size in bytes.Only applicable when *state* is `present`. |
| **ca_path**  path | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **capacity_bytes**  string | Volume size in bytes.  Only applicable when *state* is `present`. |
| **command**  string | `initialize` initializes an existing storage volume for a specified *volume_id*.  **Choices:**   - `"initialize"` |
| **controller_id**  string | Fully Qualified Device Descriptor (FQDD) of the storage controller.  For example- RAID.Slot.1-1.  This option is mandatory when *state* is `present` while creating a volume. |
| **drives**  list / elements=string | FQDD of the Physical disks.  For example- Disk.Bay.0:Enclosure.Internal.0-1:RAID.Slot.1-1.  Only applicable when *state* is `present` when creating a new volume. |
| **encrypted**  boolean | Indicates whether volume is currently utilizing encryption or not.  Only applicable when *state* is `present`.  **Choices:**   - `false` - `true` |
| **encryption_types**  string | The following encryption types can be selected.  `ControllerAssisted` The volume is encrypted by the storage controller entity.  `NativeDriveEncryption` The volume utilizes the native drive encryption capabilities of the drive hardware.  `SoftwareAssisted` The volume is encrypted by the software running on the system or the operating system.  Only applicable when *state* is `present`.  **Choices:**   - `"NativeDriveEncryption"` - `"ControllerAssisted"` - `"SoftwareAssisted"` |
| **hostname**  string / required | iDRAC IP Address or hostname. |
| **https_port**  integer | iDRAC port.  **Default:** `443` |
| **https_timeout**  integer | The HTTPS socket level timeout in seconds.  **Default:** `30` |
| **initialize_type**  string | Initialization type of existing volume.  Only applicable when *command* is `initialize`.  **Choices:**   - `"Fast"` ← (default) - `"Slow"` |
| **job_wait**  boolean | Determines whether to wait for the job completion or not.  **Choices:**   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer | The maximum wait time of *job_wait* in seconds. The job is tracked only for this duration.  This option is applicable when *job_wait* is `True`.  **Default:** `300` |
| **name**  string | Name of the volume to be created.  Only applicable when *state* is `present`. |
| **oem**  dictionary | Includes OEM extended payloads.  Only applicable when *state* is *present*. |
| **optimum_io_size_bytes**  integer | Stripe size value must be in multiples of 64 \* 1024.  Only applicable when *state* is `present`. |
| **password**  string / required | iDRAC user password. |
| **raid_type**  string | One of the following raid types must be selected to create a volume for firmware version 4.40 and above.  `RAID0` to create a RAID0 type volume.  `RAID1` to create a RAID1 type volume.  `RAID5` to create a RAID5 type volume.  `RAID10` to create a RAID10 type volume.  `RAID50` to create a RAID50 type volume.  **Choices:**   - `"RAID0"` - `"RAID1"` - `"RAID5"` - `"RAID10"` - `"RAID50"` |
| **state**  string | `present` creates a storage volume for the specified I (controller_id), or modifies the storage volume for the specified I (volume_id). “Note: Modification of an existing volume properties depends on drive and controller capabilities”.  `absent` deletes the volume for the specified *volume_id*.  **Choices:**   - `"present"` - `"absent"` |
| **username**  string / required | iDRAC username with admin privilages. |
| **validate_certs**  boolean | If `false`, the SSL certificates will not be validated.  Configure `false` only on personally controlled sites where self-signed certificates are used.  **Choices:**   - `false` - `true` ← (default) |
| **volume_id**  string | FQDD of existing volume.  For example- Disk.Virtual.4:RAID.Slot.1-1.  This option is mandatory in the following scenarios,  *state* is `present`, when updating a volume.  *state* is `absent`, when deleting a volume.  *command* is `initialize`, when initializing a volume. |

#### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
