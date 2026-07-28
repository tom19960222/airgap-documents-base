---
collection: ansible
version: "6"
title: "dellemc.openmanage.idrac_redfish_storage_controller module – Configures the physical disk, virtual disk, and storage controller settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/idrac_redfish_storage_controller_module.html
fetched_at: 2026-07-27T17:25:17+00:00
---
# dellemc.openmanage.idrac_redfish_storage_controller module – Configures the physical disk, virtual disk, and storage controller settings

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/dellemc/openmanage) (version 5.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](idrac_redfish_storage_controller_module.md#ansible-collections-dellemc-openmanage-idrac-redfish-storage-controller-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_redfish_storage_controller`.

New in dellemc.openmanage 2.1.0

- [Synopsis](idrac_redfish_storage_controller_module.md#synopsis)
- [Requirements](idrac_redfish_storage_controller_module.md#requirements)
- [Parameters](idrac_redfish_storage_controller_module.md#parameters)
- [Notes](idrac_redfish_storage_controller_module.md#notes)
- [Examples](idrac_redfish_storage_controller_module.md#examples)
- [Return Values](idrac_redfish_storage_controller_module.md#return-values)

## [Synopsis](idrac_redfish_storage_controller_module.md#id1)

- This module allows the users to configure the settings of the physical disk, virtual disk, and storage controller.

## [Requirements](idrac_redfish_storage_controller_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](idrac_redfish_storage_controller_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseuri**  string / required | IP address of the target out-of-band controller. For example- <ipaddress>:<port>. |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **command**  string | These actions may require a system reset, depending on the capabilities of the controller.  `ResetConfig` - Deletes all the virtual disks and unassigns all hot spares on physical disks. *controller_id* is required for this operation.  `AssignSpare` - Assigns a physical disk as a dedicated or global hot spare for a virtual disk. *target* is required for this operation.  `SetControllerKey` - Sets the key on controllers, which is used to encrypt the drives in Local Key Management(LKM). *controller_id*, *key*, and *key_id* are required for this operation.  `RemoveControllerKey` - Deletes the encryption key on the controller. *controller_id* is required for this operation.  `ReKey` - Resets the key on the controller and it always reports as changes found when check mode is enabled. *controller_id*, *old_key*, *key_id*, and *key* is required for this operation.  `UnassignSpare` - To unassign the Global or Dedicated hot spare. *target* is required for this operation.  `EnableControllerEncryption` - To enable Local Key Management (LKM) or Secure Enterprise Key Manager (SEKM) on controllers that support encryption of the drives. *controller_id*, *key*, and *key_id* are required for this operation.  `BlinkTarget` - Blinks the target virtual drive or physical disk and it always reports as changes found when check mode is enabled. *target* or *volume_id* is required for this operation.  `UnBlinkTarget` - Unblink the target virtual drive or physical disk and and it always reports as changes found when check mode is enabled. *target* or *volume_id* is required for this operation.  `ConvertToRAID` - Converts the disk form non-Raid to Raid. *target* is required for this operation.  `ConvertToNonRAID` - Converts the disk form Raid to non-Raid. *target* is required for this operation.  `ChangePDStateToOnline` - To set the disk status to online. *target* is required for this operation.  `ChangePDStateToOffline` - To set the disk status to offline. *target* is required for this operation.  Choices:   - `"ResetConfig"` - `"AssignSpare"` ← (default) - `"SetControllerKey"` - `"RemoveControllerKey"` - `"ReKey"` - `"UnassignSpare"` - `"EnableControllerEncryption"` - `"BlinkTarget"` - `"UnBlinkTarget"` - `"ConvertToRAID"` - `"ConvertToNonRAID"` - `"ChangePDStateToOnline"` - `"ChangePDStateToOffline"` |
| **controller_id**  string | Fully Qualified Device Descriptor (FQDD) of the storage controller. For example-‘RAID.Slot.1-1’.  This option is mandatory when *command* is `ResetConfig`, `SetControllerKey`, `RemoveControllerKey`, `ReKey`, or `EnableControllerEncryption`. |
| **job_wait**  boolean | Provides the option if the module has to wait for the job to be completed.  Choices:   - `false` ← (default) - `true` |
| **job_wait_timeout**  integer | The maximum wait time of job completion in seconds before the job tracking is stopped.  This option is applicable when *job_wait* is `True`.  Default: `120` |
| **key**  string | A new security key passphrase that the encryption-capable controller uses to create the encryption key. The controller uses the encryption key to lock or unlock access to the Self-Encrypting Drive (SED). Only one encryption key can be created for each controller.  This is mandatory when *command* is `SetControllerKey`, `ReKey`, or `EnableControllerEncryption` and when *mode* is `LKM`.  The length of the key can be a maximum of 32 characters in length, where the expanded form of the special character is counted as a single character.  The key must contain at least one character from each of the character classes: uppercase, lowercase, number, and special character. |
| **key_id**  string | This is a user supplied text label associated with the passphrase.  This is mandatory when *command* is `SetControllerKey`, `ReKey`, or `EnableControllerEncryption` and when *mode* is `LKM`.  The length of *key_id* can be a maximum of 32 characters in length and should not have any spaces. |
| **mode**  string | Encryption mode of the encryption capable controller.  This option is applicable only when *command* is `ReKey` or `EnableControllerEncryption`.  `SEKM` requires secure enterprise key manager license on the iDRAC.  `LKM` to choose mode as local key mode.  Choices:   - `"LKM"` ← (default) - `"SEKM"` |
| **old_key**  string | Security key passphrase used by the encryption-capable controller.  This option is mandatory when *command* is `ReKey` and *mode* is `LKM`. |
| **password**  string / required | Password of the target out-of-band controller. |
| **target**  aliases: drive_id  list / elements=string | Fully Qualified Device Descriptor (FQDD) of the target physical drive.  This is mandatory when *command* is `AssignSpare`, `UnassisgnSpare`, `ChangePDStateToOnline`, `ChangePDStateToOffline`, `ConvertToRAID`, or `ConvertToNonRAID`.  If *volume_id* is not specified or empty, this physical drive will be assigned as a global hot spare when *command* is `AssignSpare`.  Notes: Global or Dedicated hot spare can be assigned only once for a physical disk, Re-assign cannot be done when *command* is `AssignSpare`. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | Username of the target out-of-band controller. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |
| **volume_id**  list / elements=string | Fully Qualified Device Descriptor (FQDD) of the volume.  Applicable if *command* is `AssignSpare`, `BlinkTarget`, and `UnBlinkTarget`.  *volume_id* or *target* is required when the *command* is `BlinkTarget` or `UnBlinkTarget`, if both are specified *target* is considered.  To know the number of volumes to which a hot spare can be assigned, refer iDRAC Redfish API documentation. |

## [Notes](idrac_redfish_storage_controller_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell EMC iDRAC.
> - This module always reports as changes found when `ReKey`, `BlinkTarget`, and `UnBlinkTarget`.
> - This module supports `check_mode`.

## [Examples](idrac_redfish_storage_controller_module.md#id5)

```yaml+jinja
---
- name: Assign dedicated hot spare
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    volume_id:
      - "Disk.Virtual.0:RAID.Slot.1-1"
    target: "Disk.Bay.0:Enclosure.Internal.0-1:RAID.Slot.1-1"
  tags:
    - assign_dedicated_hot_spare

- name: Assign global hot spare
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    target: "Disk.Bay.0:Enclosure.Internal.0-1:RAID.Slot.1-1"
  tags:
    - assign_global_hot_spare

- name: Unassign hot spare
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    target: "Disk.Bay.0:Enclosure.Internal.0-1:RAID.Slot.1-1"
    command: UnassignSpare
  tags:
    - un-assign-hot-spare

- name: Set controller encryption key
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "SetControllerKey"
    controller_id: "RAID.Slot.1-1"
    key: "PassPhrase@123"
    key_id: "mykeyid123"
  tags:
    - set_controller_key

- name: Rekey in LKM mode
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "ReKey"
    controller_id: "RAID.Slot.1-1"
    key: "NewPassPhrase@123"
    key_id: "newkeyid123"
    old_key: "OldPassPhrase@123"
  tags:
    - rekey_lkm

- name: Rekey in SEKM mode
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "ReKey"
    controller_id: "RAID.Slot.1-1"
    mode: "SEKM"
  tags:
    - rekey_sekm

- name: Remove controller key
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "RemoveControllerKey"
    controller_id: "RAID.Slot.1-1"
  tags:
    - remove_controller_key

- name: Reset controller configuration
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "ResetConfig"
    controller_id: "RAID.Slot.1-1"
  tags:
    - reset_config

- name: Enable controller encryption
  idrac_redfish_storage_controller:
    baseuri: "{{ baseuri }}"
    username: "{{ username }}"
    password: "{{ password }}"
    ca_path: "/path/to/ca_cert.pem"
    command: "EnableControllerEncryption"
    controller_id: "RAID.Slot.1-1"
    mode: "LKM"
    key: "your_Key@123"
    key_id: "your_Keyid@123"
  tags:
    - enable-encrypt

- name: Blink physical disk.
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: BlinkTarget
    target: "Disk.Bay.0:Enclosure.Internal.0-1:RAID.Slot.1-1"
  tags:
    - blink-target

- name: Blink virtual drive.
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: BlinkTarget
    volume_id: "Disk.Virtual.0:RAID.Slot.1-1"
  tags:
    - blink-volume

- name: Unblink physical disk.
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: UnBlinkTarget
    target: "Disk.Bay.0:Enclosure.Internal.0-1:RAID.Slot.1-1"
  tags:
    - unblink-target

- name: Unblink virtual drive.
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: UnBlinkTarget
    volume_id: "Disk.Virtual.0:RAID.Slot.1-1"
  tags:
    - unblink-drive

- name: Convert physical disk to RAID
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "ConvertToRAID"
    target: "Disk.Bay.0:Enclosure.Internal.0-1:RAID.Slot.1-1"
  tags:
    - convert-raid

- name: Convert physical disk to non-RAID
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "ConvertToNonRAID"
    target: "Disk.Bay.0:Enclosure.Internal.0-1:RAID.Slot.1-1"
  tags:
    - convert-non-raid

- name: Change physical disk state to online.
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "ChangePDStateToOnline"
    target: "Disk.Bay.1:Enclosure.Internal.0-1:RAID.Slot.1-1"
  tags:
    - pd-state-online

- name: Change physical disk state to offline.
  dellemc.openmanage.idrac_redfish_storage_controller:
    baseuri: "192.168.0.1:443"
    username: "user_name"
    password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: "ChangePDStateToOnline"
    target: "Disk.Bay.1:Enclosure.Internal.0-1:RAID.Slot.1-1"
  tags:
    - pd-state-offline
```

## [Return Values](idrac_redfish_storage_controller_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of a http error.  Returned: on http error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to run the method because the requested HTTP method is not allowed.", "MessageArgs": [], "MessageArgs@odata.count": 0, "MessageId": "iDRAC.1.6.SYS402", "RelatedProperties": [], "RelatedProperties@odata.count": 0, "Resolution": "Enter a valid HTTP method and retry the operation. For information about valid methods, see the Redfish Users Guide available on the support site.", "Severity": "Informational"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information"}}` |
| **msg**  string | Overall status of the storage controller configuration operation.  Returned: always  Sample: `"Successfully submitted the job that performs the AssignSpare operation"` |
| **status**  dictionary | status of the submitted job.  Returned: always  Sample: `{"ActualRunningStartTime": "2022-02-09T04:42:41", "ActualRunningStopTime": "2022-02-09T04:44:00", "CompletionTime": "2022-02-09T04:44:00", "Description": "Job Instance", "EndTime": "TIME_NA", "Id": "JID_444033604418", "JobState": "Completed", "JobType": "RealTimeNoRebootConfiguration", "Message": "Job completed successfully.", "MessageArgs": [], "MessageId": "PR19", "Name": "Configure: RAID.Integrated.1-1", "PercentComplete": 100, "StartTime": "2022-02-09T04:42:40", "TargetSettingsURI": null}` |
| **task**  dictionary | ID and URI resource of the job created.  Returned: success  Sample: `{"id": "JID_XXXXXXXXXXXXX", "uri": "/redfish/v1/Managers/iDRAC.Embedded.1/Jobs/JID_XXXXXXXXXXXXX"}` |

### Authors

- Jagadeesh N V (@jagadeeshnv)
- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
