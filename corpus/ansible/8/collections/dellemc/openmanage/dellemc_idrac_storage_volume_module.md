---
collection: ansible
version: "8"
title: "dellemc.openmanage.dellemc_idrac_storage_volume module – Configures the RAID configuration attributes"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/dellemc_idrac_storage_volume_module.html
fetched_at: 2026-07-28T02:04:00+00:00
---
# dellemc.openmanage.dellemc_idrac_storage_volume module – Configures the RAID configuration attributes

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
> see [Requirements](dellemc_idrac_storage_volume_module.md#ansible-collections-dellemc-openmanage-dellemc-idrac-storage-volume-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.dellemc_idrac_storage_volume`.

New in dellemc.openmanage 2.0.0

- [Synopsis](dellemc_idrac_storage_volume_module.md#synopsis)
- [Requirements](dellemc_idrac_storage_volume_module.md#requirements)
- [Parameters](dellemc_idrac_storage_volume_module.md#parameters)
- [Notes](dellemc_idrac_storage_volume_module.md#notes)
- [Examples](dellemc_idrac_storage_volume_module.md#examples)
- [Return Values](dellemc_idrac_storage_volume_module.md#return-values)

## [Synopsis](dellemc_idrac_storage_volume_module.md#id1)

- This module is responsible for configuring the RAID attributes.

## [Requirements](dellemc_idrac_storage_volume_module.md#id2)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.9.6

## [Parameters](dellemc_idrac_storage_volume_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **capacity**  float | Virtual disk size in GB. |
| **controller_id**  string | Fully Qualified Device Descriptor (FQDD) of the storage controller, for example ‘RAID.Integrated.1-1’. Controller FQDD is required for `create` RAID configuration. |
| **disk_cache_policy**  string | Disk Cache Policy.  **Choices:**   - `"Default"` ← (default) - `"Enabled"` - `"Disabled"` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  **Default:** `443` |
| **idrac_user**  string / required | iDRAC username. |
| **media_type**  string | Media type.  **Choices:**   - `"HDD"` - `"SSD"` |
| **number_dedicated_hot_spare**  integer | Number of Dedicated Hot Spare.  **Default:** `0` |
| **protocol**  string | Bus protocol.  **Choices:**   - `"SAS"` - `"SATA"` |
| **raid_init_operation**  string | This option represents initialization configuration operation to be performed on the virtual disk.  **Choices:**   - `"None"` - `"Fast"` |
| **raid_reset_config**  string | This option represents whether a reset config operation needs to be performed on the RAID controller. Reset Config operation deletes all the virtual disks present on the RAID controller.  **Choices:**   - `"True"` - `"False"` ← (default) |
| **read_cache_policy**  string | Read cache policy.  **Choices:**   - `"NoReadAhead"` ← (default) - `"ReadAhead"` - `"AdaptiveReadAhead"` |
| **span_depth**  integer | Number of spans in the RAID configuration.  *span_depth* is required for `create` and its value depends on *volume_type*.  **Default:** `1` |
| **span_length**  integer | Number of disks in a span.  *span_length* is required for `create` and its value depends on *volume_type*.  **Default:** `1` |
| **state**  string | `create`, performs create volume operation.  `delete`, performs remove volume operation.  `view`, returns storage view.  **Choices:**   - `"create"` - `"delete"` - `"view"` ← (default) |
| **stripe_size**  integer | Stripe size value to be provided in multiples of 64 \* 1024.  **Default:** `65536` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |
| **volume_id**  string | Fully Qualified Device Descriptor (FQDD) of the virtual disk, for example ‘Disk.virtual.0:RAID.Slot.1-1’. This option is used to get the virtual disk information. |
| **volume_type**  string | Provide the the required RAID level.  **Choices:**   - `"RAID 0"` ← (default) - `"RAID 1"` - `"RAID 5"` - `"RAID 6"` - `"RAID 10"` - `"RAID 50"` - `"RAID 60"` |
| **volumes**  list / elements=dictionary | A list of virtual disk specific iDRAC attributes. This is applicable for `create` and `delete` operations.  For `create` operation, name and drives are applicable options, other volume options can also be specified.  The drives is a required option for `create` operation and accepts either location (list of drive slot) or id (list of drive fqdd).  For `delete` operation, only name option is applicable.  See the examples for more details. |
| **write_cache_policy**  string | Write cache policy.  **Choices:**   - `"WriteThrough"` ← (default) - `"WriteBack"` - `"WriteBackForce"` |

## [Notes](dellemc_idrac_storage_volume_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell iDRAC.
> - This module supports both IPv4 and IPv6 address for *idrac_ip*.
> - This module supports `check_mode`.

## [Examples](dellemc_idrac_storage_volume_module.md#id5)

```yaml+jinja
---
- name: Create single volume
  dellemc.openmanage.dellemc_idrac_storage_volume:
    idrac_ip: "192.168.0.1"
    idrac_user: "username"
    idrac_password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "create"
    controller_id: "RAID.Slot.1-1"
    volumes:
      - drives:
        location: [5]

- name: Create multiple volume
  dellemc.openmanage.dellemc_idrac_storage_volume:
    idrac_ip: "192.168.0.1"
    idrac_user: "username"
    idrac_password: "password"
    ca_path: "/path/to/ca_cert.pem"
    raid_reset_config: "True"
    state: "create"
    controller_id: "RAID.Slot.1-1"
    volume_type: "RAID 1"
    span_depth: 1
    span_length: 2
    number_dedicated_hot_spare: 1
    disk_cache_policy: "Enabled"
    write_cache_policy: "WriteBackForce"
    read_cache_policy: "ReadAhead"
    stripe_size: 65536
    capacity: 100
    raid_init_operation: "Fast"
    volumes:
      - name: "volume_1"
        drives:
          id: ["Disk.Bay.1:Enclosure.Internal.0-1:RAID.Slot.1-1", "Disk.Bay.2:Enclosure.Internal.0-1:RAID.Slot.1-1"]
      - name: "volume_2"
        volume_type: "RAID 5"
        span_length: 3
        span_depth: 1
        drives:
           location: [7,3,5]
        disk_cache_policy: "Disabled"
        write_cache_policy: "WriteBack"
        read_cache_policy: "NoReadAhead"
        stripe_size: 131072
        capacity: "200"
        raid_init_operation: "None"

- name: View all volume details
  dellemc.openmanage.dellemc_idrac_storage_volume:
    idrac_ip: "192.168.0.1"
    idrac_user: "username"
    idrac_password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "view"

- name: View specific volume details
  dellemc.openmanage.dellemc_idrac_storage_volume:
    idrac_ip: "192.168.0.1"
    idrac_user: "username"
    idrac_password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "view"
    controller_id: "RAID.Slot.1-1"
    volume_id: "Disk.Virtual.0:RAID.Slot.1-1"

- name: Delete single volume
  dellemc.openmanage.dellemc_idrac_storage_volume:
    idrac_ip: "192.168.0.1"
    idrac_user: "username"
    idrac_password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "delete"
    volumes:
      - name: "volume_1"

- name: Delete multiple volume
  dellemc.openmanage.dellemc_idrac_storage_volume:
    idrac_ip: "192.168.0.1"
    idrac_user: "username"
    idrac_password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "delete"
    volumes:
      - name: "volume_1"
      - name: "volume_2"
```

## [Return Values](dellemc_idrac_storage_volume_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Overall status of the storage configuration operation.  **Returned:** always  **Sample:** `"Successfully completed the view storage volume operation"` |
| **storage_status**  dictionary | Storage configuration job and progress details from the iDRAC.  **Returned:** success  **Sample:** `{"Id": "JID_XXXXXXXXX", "JobState": "Completed", "JobType": "ImportConfiguration", "Message": "Successfully imported and applied Server Configuration Profile.", "MessageId": "XXX123", "Name": "Import Configuration", "PercentComplete": 100, "StartTime": "TIME_NOW", "Status": "Success", "TargetSettingsURI": null, "retval": true}` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
