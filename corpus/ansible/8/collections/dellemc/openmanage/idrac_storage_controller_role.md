---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_storage_controller role – Configures the physical disk, virtual disk, and storage controller settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_storage_controller_role.html
fetched_at: 2026-07-28T02:05:06+00:00
---
# dellemc.openmanage.idrac_storage_controller role – Configures the physical disk, virtual disk, and storage controller settings

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
> To use it in a playbook, specify: `dellemc.openmanage.idrac_storage_controller`.

- [Entry point `main` – Configures the physical disk, virtual disk, and storage controller settings](idrac_storage_controller_role.md#entry-point-main-configures-the-physical-disk-virtual-disk-and-storage-controller-settings)

  - [Synopsis](idrac_storage_controller_role.md#synopsis)
  - [Parameters](idrac_storage_controller_role.md#parameters)

## [Entry point `main` – Configures the physical disk, virtual disk, and storage controller settings](idrac_storage_controller_role.md#id1)

New in dellemc.openmanage 7.6.0

### [Synopsis](idrac_storage_controller_role.md#id2)

- This role allows the users to configure the settings of the physical disk, virtual disk, and storage controller on iDRAC9 based PowerEdge servers.

### [Parameters](idrac_storage_controller_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **apply_time**  string | Apply time of the *attributes*.  This is applicable only to *attributes*.  `Immediate` Allows the user to immediately reboot the host and apply the changes. *job_wait* is applicable.  `OnReset` Allows the user to apply the changes on the next reboot of the host server.  `AtMaintenanceWindowStart` Allows the user to apply the changes at the start of a maintenance window as specified in *maintenance_window*.  `InMaintenanceWindowOnReset` Allows the users to apply after a manual reset but within the maintenance window as specified in *maintenance_window*.  **Choices:**   - `"Immediate"` ← (default) - `"OnReset"` - `"AtMaintenanceWindowStart"` - `"InMaintenanceWindowOnReset"` |
| **attributes**  dictionary | Dictionary of controller attributes and value pair.  This feature is only supported for iDRAC9 with firmware version 6.00.00.00 and above.  *controller_id* is required for this operation.  *apply_time* and *maintenance_window* is applicable for *attributes*.  Use <https://I(idrac_ip>/redfish/v1/Schemas/DellOemStorageController.json) to view the attributes. |
| **ca_path**  path | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **controller_id**  string / required | The ID of the controller on which the operations need to be performed. |
| **disks**  dictionary | List of physical disks that belongs to *controller_id*. |
| **blink**  boolean | Blinks the target physical disk and it always reports as changes found when check mode is enabled.  **Choices:**   - `false` - `true` |
| **global_hot_spare**  boolean | Assigns a global hot spare or unassigns a hot spare.  `true` assigns the disk as a global hot spare.  `false` unassigns the disk as a hot spare.  **Choices:**   - `false` - `true` |
| **id**  string / required | Fully Qualified Device Descriptor (FQDD) of the physical disk. |
| **raid_state**  string | Converts the disk form Non-Raid to Raid and vice versa.  `raid` converts the physical disk to Raid.  `nonraid` converts the physical disk to Non Raid.  **Choices:**   - `"raid"` - `"nonraid"` |
| **status**  string | Converts the disk form online to offline and vice versa.  `online` converts the physical disk status to online.  `offline` converts the physical disk status to offline.  **Choices:**   - `"online"` - `"offline"` |
| **hostname**  string / required | iDRAC IP Address. |
| **https_port**  integer | iDRAC port.  **Default:** `443` |
| **https_timeout**  integer | The socket level timeout in seconds.  **Default:** `30` |
| **key**  string | A new security key passphrase that the encryption-capable controller uses to create the encryption key. The controller uses the encryption key to lock or unlock access to the Self-Encrypting Drive (SED). Only one encryption key can be created for each controller.  This is mandatory when *set_controller_key* is `true`, *rekey* is `true`.  The length of the key can be a maximum of 32 characters in length, where the expanded form of the special character is counted as a single character.  The key must contain at least one character from each of the character classes are uppercase, lowercase, number, and special character. |
| **key_id**  string | This is a user supplied text label associated with the passphrase.  This is mandatory when *set_controller_key* is `true`, *rekey* is `true`.  The length of *key_id* can be a maximum of 32 characters in length and should not have any spaces. |
| **maintenance_window**  dictionary | Option to schedule the maintenance window.  This is required when *apply_time* is `AtMaintenanceWindowStart` or `InMaintenanceWindowOnReset`. |
| **duration**  integer | The duration in seconds for the maintenance window.  **Default:** `900` |
| **start_time**  string / required | The start time for the maintenance window to be scheduled.  The format is YYYY-MM-DDThh:mm:ss<offset>  <offset> is the time offset from UTC that the current timezone set in iDRAC in the format is +05:30 for IST. |
| **mode**  string | Encryption mode of the encryption capable controller.  This option is mandatory when *rekey* is `true` and for enabling controller encryption.  `SEKM` to choose mode as secure enterprise key manager.  `LKM` to choose mode as local key management.  **Choices:**   - `"LKM"` - `"SEKM"` |
| **old_key**  string | Security key passphrase used by the encryption-capable controller.  This option is mandatory when *rekey* is `true`. |
| **password**  string / required | iDRAC user password. |
| **rekey**  boolean | Resets the key on the controller and it always reports as changes found when check mode is enabled.  **Choices:**   - `false` - `true` |
| **remove_key**  boolean | Remove the key on controllers.  **Choices:**   - `false` - `true` |
| **reset_config**  boolean | To reset the controller.  **Choices:**   - `false` - `true` |
| **set_controller_key**  boolean | Set the security key or enable controller encryption.  If *mode* is provided controller encryption operation is performed, otherwise sets the controller security key.  *key*, and *key_id* are required for this operation.  **Choices:**   - `false` - `true` |
| **username**  string / required | iDRAC username. |
| **validate_certs**  boolean | If `false`, the SSL certificates will not be validated.  Configure `false` only on personally controlled sites where self-signed certificates are used.  **Choices:**   - `false` - `true` ← (default) |
| **volumes**  dictionary | List of volume that belongs to *controller_id*. |
| **blink**  boolean | Blinks the target virtual disk and it always reports as changes found when check mode is enabled.  **Choices:**   - `false` - `true` |
| **dedicated_hot_spare**  string | Fully Qualified Device Descriptor (FQDD) of the physical disk to assign the volume as a dedicated hot spare to a disk. |
| **encrypted**  boolean | To encrypt the virtual disk.  **Choices:**   - `false` - `true` |
| **expand_capacity_disk**  string | Fully Qualified Device Descriptor (FQDD) of the disk for expanding the capacity with the existing disk.  *expand_capacity_size* is mutually exclusive with *expand_capacity_disk*. |
| **expand_capacity_size**  string | Capacity of the virtual disk to be expanded in MB.  Check mode and Idempotency is not supported for *expand_capacity_size*.  Minimum Online Capacity Expansion size must be greater than 100 MB of the current size.  *expand_capacity_disk* is mutually exclusive with *expand_capacity_size*. |
| **id**  string / required | Fully Qualified Device Descriptor (FQDD) of the volume. |

#### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
