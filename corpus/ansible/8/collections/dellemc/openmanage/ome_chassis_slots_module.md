---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_chassis_slots module – Rename sled slots on OpenManage Enterprise Modular"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_chassis_slots_module.html
fetched_at: 2026-07-28T02:04:24+00:00
---
# dellemc.openmanage.ome_chassis_slots module – Rename sled slots on OpenManage Enterprise Modular

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
> see [Requirements](ome_chassis_slots_module.md#ansible-collections-dellemc-openmanage-ome-chassis-slots-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_chassis_slots`.

New in dellemc.openmanage 3.6.0

- [Synopsis](ome_chassis_slots_module.md#synopsis)
- [Requirements](ome_chassis_slots_module.md#requirements)
- [Parameters](ome_chassis_slots_module.md#parameters)
- [Notes](ome_chassis_slots_module.md#notes)
- [Examples](ome_chassis_slots_module.md#examples)
- [Return Values](ome_chassis_slots_module.md#return-values)

## [Synopsis](ome_chassis_slots_module.md#id1)

- This module allows to rename sled slots on OpenManage Enterprise Modular either using device id or device service tag or using chassis service tag and slot number.

## [Requirements](ome_chassis_slots_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_chassis_slots_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_options**  list / elements=dictionary | The ID or service tag of the sled in the slot and the new name for the slot.  *device_options* is mutually exclusive with *slot_options*. |
| **device_id**  integer | Device ID of the sled in the slot.  This is mutually exclusive with *device_service_tag*. |
| **device_service_tag**  string | Service tag of the sled in the slot.  This is mutually exclusive with *device_id*. |
| **slot_name**  string / required | Provide name for the slot. |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **slot_options**  list / elements=dictionary | The service tag of the chassis, slot number of the slot to be renamed, and the new name for the slot.  *slot_options* is mutually exclusive with *device_options*. |
| **chassis_service_tag**  string / required | Service tag of the chassis. |
| **slots**  list / elements=dictionary / required | The slot number and the new name for the slot. |
| **slot_name**  string / required | Provide name for the slot. |
| **slot_number**  integer / required | The slot number of the slot to be renamed. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_chassis_slots_module.md#id4)

> **Note:**
>
> - This module initiates the refresh inventory task. It may take a minute for new names to be reflected. If the task exceeds 300 seconds to refresh, the task times out.
> - Run this module from a system that has direct access to Dell OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_chassis_slots_module.md#id5)

```yaml+jinja
---
- name: Rename the slots in multiple chassis using slot number and chassis service tag
  dellemc.openmanage.ome_chassis_slots:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    slot_options:
      - chassis_service_tag: ABC1234
        slots:
          - slot_number: 1
            slot_name: sled_name_1
          - slot_number: 2
            slot_name: sled_name_2
      - chassis_service_tag: ABC1235
        slots:
          - slot_number: 1
            slot_name: sled_name_1
          - slot_number: 2
            slot_name: sled_name_2

- name: Rename single slot name of the sled using sled ID
  dellemc.openmanage.ome_chassis_slots:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_options:
      - device_id: 10054
        slot_name: slot_device_name_1

- name: Rename single slot name of the sled using sled service tag
  dellemc.openmanage.ome_chassis_slots:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_options:
      - device_service_tag: ABC1234
        slot_name: service_tag_slot

- name: Rename multiple slot names of the devices
  dellemc.openmanage.ome_chassis_slots:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_options:
      - device_id: 10054
        slot_name: sled_name_1
      - device_service_tag: ABC1234
        slot_name: sled_name_2
      - device_id: 10055
        slot_name: sled_name_3
      - device_service_tag: PQR1234
        slot_name: sled_name_4
```

## [Return Values](ome_chassis_slots_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to complete the operation because an invalid value is entered for the property Invalid json type: STRING for Edm.Int64 property: Id .", "MessageArgs": ["Invalid json type: STRING for Edm.Int64 property: Id"], "MessageId": "CGEN1014", "RelatedProperties": [], "Resolution": "Enter a valid value for the property and retry the operation. For more information about valid values, see the OpenManage Enterprise-Modular User's Guide available on the support site.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the slot rename operation.  **Returned:** always  **Sample:** `"Successfully renamed the slot(s)."` |
| **rename_failed_slots**  list / elements=dictionary | Information of the valid slots that are not renamed.  `JobStatus` is shown if rename job fails.  `NOTE` Only slots which were not renamed are listed.  **Returned:** if at least one slot renaming fails  **Sample:** `[{"ChassisId": "12345", "ChassisName": "MX-ABCD123", "ChassisServiceTag": "ABCD123", "DeviceType": "4000", "JobId": 1234, "JobStatus": "Aborted", "SlotId": "10061", "SlotName": "c2", "SlotNumber": "1", "SlotType": "4000"}, {"ChassisId": "10053", "ChassisName": "MX-PQRS123", "ChassisServiceTag": "PQRS123", "DeviceType": "1000", "JobId": 0, "JobStatus": "HTTP Error 400: Bad Request", "SlotId": "10069", "SlotName": "b2", "SlotNumber": "3", "SlotType": "2000"}]` |
| **slot_info**  list / elements=dictionary | Information of the slots that are renamed successfully.  The `DeviceServiceTag` and `DeviceId` options are available only if *device_options* is used.  `NOTE` Only the slots which were renamed are listed.  **Returned:** if at least one slot renamed  **Sample:** `[{"ChassisId": 10053, "ChassisServiceTag": "ABCD123", "DeviceName": "", "DeviceType": 1000, "JobId": 15746, "SlotId": "10072", "SlotName": "slot_op2", "SlotNumber": "6", "SlotType": 2000}, {"ChassisId": 10053, "ChassisName": "MX-ABCD123", "ChassisServiceTag": "ABCD123", "DeviceType": "3000", "JobId": 15747, "SlotId": "10070", "SlotName": "slot_op2", "SlotNumber": "4", "SlotType": "2000"}, {"ChassisId": "10053", "ChassisName": "MX-PQRS123", "ChassisServiceTag": "PQRS123", "DeviceId": "10054", "DeviceServiceTag": "XYZ5678", "DeviceType": "1000", "JobId": 15761, "SlotId": "10067", "SlotName": "a1", "SlotNumber": "1", "SlotType": "2000"}]` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
