---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_device_power_settings module – Configure chassis power settings on OpenManage Enterprise Modular"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_device_power_settings_module.html
fetched_at: 2026-07-27T17:25:35+00:00
---
# dellemc.openmanage.ome_device_power_settings module – Configure chassis power settings on OpenManage Enterprise Modular

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
> see [Requirements](ome_device_power_settings_module.md#ansible-collections-dellemc-openmanage-ome-device-power-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_device_power_settings`.

New in dellemc.openmanage 4.2.0

- [Synopsis](ome_device_power_settings_module.md#synopsis)
- [Requirements](ome_device_power_settings_module.md#requirements)
- [Parameters](ome_device_power_settings_module.md#parameters)
- [Notes](ome_device_power_settings_module.md#notes)
- [Examples](ome_device_power_settings_module.md#examples)
- [Return Values](ome_device_power_settings_module.md#return-values)

## [Synopsis](ome_device_power_settings_module.md#id1)

- This module allows to configure the chassis power settings on OpenManage Enterprise Modular.

## [Requirements](ome_device_power_settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_device_power_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_id**  integer | The ID of the chassis for which the settings need to be updated.  If the device ID is not specified, this module updates the power settings for the *hostname*.  *device_id* is mutually exclusive with *device_service_tag*. |
| **device_service_tag**  string | The service tag of the chassis for which the setting needs to be updated.  If the device service tag is not specified, this module updates the power settings for the *hostname*.  *device_service_tag* is mutually exclusive with *device_id*. |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **hot_spare_configuration**  dictionary | The settings for Hot Spare configuration. |
| **enable_hot_spare**  boolean / required | Enables or disables Hot Spare configuration to facilitate voltage regulation when power utilized by the Power Supply Unit (PSU) is low.  Choices:   - `false` - `true` |
| **primary_grid**  string | The choices for PSU grid.  `GRID_1` Hot Spare on Grid 1.  `GRID_2` Hot Spare on Grid 2.  Choices:   - `"GRID_1"` ← (default) - `"GRID_2"` |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **power_configuration**  dictionary | The settings for Power configuration. |
| **enable_power_cap**  boolean / required | Enables or disables the Power Cap Settings.  Choices:   - `false` - `true` |
| **power_cap**  integer | The maximum power consumption limit of the device. Specify the consumption limit in Watts.  This is required if *enable_power_cap* is set to true. |
| **redundancy_configuration**  dictionary | The settings for Redundancy configuration. |
| **redundancy_policy**  string | The choices to configure the redundancy policy.  `NO_REDUNDANCY` no redundancy policy is used.  `GRID_REDUNDANCY` to distributes power by dividing the PSUs into two grids.  `PSU_REDUNDANCY` to distribute power between all the PSUs.  Choices:   - `"NO_REDUNDANCY"` ← (default) - `"GRID_REDUNDANCY"` - `"PSU_REDUNDANCY"` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_device_power_settings_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell EMC OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_device_power_settings_module.md#id5)

```yaml+jinja
---
- name: Update power configuration settings of a chassis using the device ID.
  dellemc.openmanage.ome_device_power_settings:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_id: 25011
    power_configuration:
      enable_power_cap: true
      power_cap: 3424

- name: Update redundancy configuration settings of a chassis using the device service tag.
  dellemc.openmanage.ome_device_power_settings:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tag: GHRT2RL
    redundancy_configuration:
      redundancy_policy: GRID_REDUNDANCY

- name: Update hot spare configuration settings of a chassis using device ID.
  dellemc.openmanage.ome_device_power_settings:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_id: 25012
    hot_spare_configuration:
      enable_hot_spare: true
      primary_grid: GRID_1
```

## [Return Values](ome_device_power_settings_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the device power settings.  Returned: always  Sample: `"Successfully updated the power settings."` |
| **power_details**  dictionary | returned when power settings are updated successfully.  Returned: success  Sample: `{"EnableHotSpare": true, "EnablePowerCapSettings": true, "MaxPowerCap": "3424", "MinPowerCap": "3291", "PowerCap": "3425", "PrimaryGrid": "GRID_1", "RedundancyPolicy": "NO_REDUNDANCY", "SettingType": "Power"}` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
