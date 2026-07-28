---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.netapp_e_drive_firmware module – NetApp E-Series manage drive firmware"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/netapp_e_drive_firmware_module.html
fetched_at: 2026-07-28T00:14:15+00:00
---
# netapp_eseries.santricity.netapp_e_drive_firmware module – NetApp E-Series manage drive firmware

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/netapp_eseries/santricity) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_drive_firmware`.

New in netapp_eseries.santricity 2.9

- [Synopsis](netapp_e_drive_firmware_module.md#synopsis)
- [Parameters](netapp_e_drive_firmware_module.md#parameters)
- [Notes](netapp_e_drive_firmware_module.md#notes)
- [Examples](netapp_e_drive_firmware_module.md#examples)
- [Return Values](netapp_e_drive_firmware_module.md#return-values)

## [Synopsis](netapp_e_drive_firmware_module.md#id1)

- Ensure drive firmware version is activated on specified drive model.

## [Parameters](netapp_e_drive_firmware_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API. Example <https://prod-1.wahoo.acme.com/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **firmware**  list / elements=string / required | list of drive firmware file paths.  NetApp E-Series drives require special firmware which can be downloaded from <https://mysupport.netapp.com/NOW/download/tools/diskfw_eseries/> |
| **ignore_inaccessible_drives**  boolean | This flag will determine whether drive firmware upgrade should fail if any affected drives are inaccessible.  Choices:   - `false` ← (default) - `true` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **upgrade_drives_online**  boolean | This flag will determine whether drive firmware can be upgrade while drives are accepting I/O.  When *upgrade_drives_online==False* stop all I/O before running task.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |
| **wait_for_completion**  boolean | This flag will cause module to wait for any upgrade actions to complete.  Choices:   - `false` ← (default) - `true` |

## [Notes](netapp_e_drive_firmware_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](netapp_e_drive_firmware_module.md#id4)

```yaml+jinja
- name: Ensure correct firmware versions
  nac_santricity_drive_firmware:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    firmware: "path/to/drive_firmware"
    wait_for_completion: true
    ignore_inaccessible_drives: false
```

## [Return Values](netapp_e_drive_firmware_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Whether any drive firmware was upgraded and whether it is in progress.  Returned: always  Sample: `"{'changed': True, 'upgrade_in_process': True}"` |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
