---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_device_local_access_configuration module – Configure local access settings on OpenManage Enterprise Modular."
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_device_local_access_configuration_module.html
fetched_at: 2026-07-27T17:25:33+00:00
---
# dellemc.openmanage.ome_device_local_access_configuration module – Configure local access settings on OpenManage Enterprise Modular.

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
> see [Requirements](ome_device_local_access_configuration_module.md#ansible-collections-dellemc-openmanage-ome-device-local-access-configuration-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_device_local_access_configuration`.

New in dellemc.openmanage 4.4.0

- [Synopsis](ome_device_local_access_configuration_module.md#synopsis)
- [Requirements](ome_device_local_access_configuration_module.md#requirements)
- [Parameters](ome_device_local_access_configuration_module.md#parameters)
- [Notes](ome_device_local_access_configuration_module.md#notes)
- [Examples](ome_device_local_access_configuration_module.md#examples)
- [Return Values](ome_device_local_access_configuration_module.md#return-values)

## [Synopsis](ome_device_local_access_configuration_module.md#id1)

- This module allows to configure the local access settings of the power button, quick sync, KVM, LCD, and chassis direct access on OpenManage Enterprise Modular.

## [Requirements](ome_device_local_access_configuration_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_device_local_access_configuration_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **chassis_power_button**  dictionary | The settings for the chassis power button. |
| **disabled_button_lcd_override_pin**  integer | The six digit LCD override pin to change the power state of the chassis.  This is required when *enable_lcd_override_pin* is `True`.  The module will always report change when *disabled_button_lcd_override_pin* is `True`. |
| **enable_chassis_power_button**  boolean / required | Enables or disables the chassis power button.  If `False`, the chassis cannot be turn on or turn off using the power button.  Choices:   - `false` - `true` |
| **enable_lcd_override_pin**  boolean | Enables or disables the LCD override pin.  This is required when *enable_chassis_power_button* is `False`.  Choices:   - `false` - `true` |
| **device_id**  integer | The ID of the chassis for which the local access configuration to be updated.  If the device ID is not specified, this module updates the local access settings for the *hostname*.  *device_id* is mutually exclusive with *device_service_tag*. |
| **device_service_tag**  string | The service tag of the chassis for which the local access settings needs to be updated.  If the device service tag is not specified, this module updates the local access settings for the *hostname*.  *device_service_tag* is mutually exclusive with *device_id*. |
| **enable_chassis_direct_access**  boolean | Enables or disables the access to management consoles such as iDRAC and the management module of the device on the chassis.  Choices:   - `false` - `true` |
| **enable_kvm_access**  boolean | Enables or disables the keyboard, video, and mouse (KVM) interfaces.  Choices:   - `false` - `true` |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **lcd**  dictionary | The settings for LCD.  The *lcd* options are ignored if the LCD hardware is not present in the chassis. |
| **lcd_access**  string | Option to configure the quick sync settings using LCD.  `VIEW_AND_MODIFY` to set access level to view and modify.  `VIEW_ONLY` to set access level to view.  `DISABLED` to disable the access.  Choices:   - `"VIEW_AND_MODIFY"` - `"VIEW_ONLY"` - `"DISABLED"` |
| **lcd_language**  string | The language code in which the text on the LCD must be displayed.  en to set English language.  fr to set French language.  de to set German language.  es to set Spanish language.  ja to set Japanese language.  zh to set Chinese language. |
| **user_defined**  string | The text to display on the LCD Home screen. The LCD Home screen is displayed when the system is reset to factory default settings. The user-defined text can have a maximum of 62 characters. |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **quick_sync**  dictionary | The settings for quick sync.  The *quick_sync* options are ignored if the quick sync hardware is not present. |
| **enable_inactivity_timeout**  boolean | Enables or disables the inactivity timeout.  Choices:   - `false` - `true` |
| **enable_quick_sync_wifi**  boolean | Enables or disables the Wi-Fi communication path to the chassis.  Choices:   - `false` - `true` |
| **enable_read_authentication**  boolean | Enables or disables the option to log in using your user credentials and to read the inventory in a secure data center.  Choices:   - `false` - `true` |
| **quick_sync_access**  string | Users with administrator privileges can set the following types of *quick_sync_access*.  `READ_WRITE` enables writing configuration using quick sync.  `READ_ONLY` enables read only access to Wi-Fi and Bluetooth Low Energy(BLE).  `DISABLED` disables reading or writing configuration through quick sync.  Choices:   - `"READ_WRITE"` - `"READ_ONLY"` - `"DISABLED"` |
| **timeout_limit**  integer | Inactivity timeout in seconds or minutes.  The range is 120 to 3600 in seconds, or 2 to 60 in minutes.  This option is required when *enable_inactivity_timeout* is `True`. |
| **timeout_limit_unit**  string | Inactivity timeout limit unit.  `SECONDS` to set *timeout_limit* in seconds.  `MINUTES` to set *timeout_limit* in minutes.  This option is required when *enable_inactivity_timeout* is `True`.  Choices:   - `"SECONDS"` - `"MINUTES"` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_device_local_access_configuration_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to OpenManage Enterprise Modular.
> - This module supports `check_mode`.
> - The module will always report change when *enable_chassis_power_button* is `True`.

## [Examples](ome_device_local_access_configuration_module.md#id5)

```yaml+jinja
---
- name: Configure KVM, direct access and power button settings of the chassis using device ID.
  dellemc.openmanage.ome_device_local_access_configuration:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_id: 25011
    enable_kvm_access: true
    enable_chassis_direct_access: false
    chassis_power_button:
      enable_chassis_power_button: false
      enable_lcd_override_pin: true
      disabled_button_lcd_override_pin: 123456

- name: Configure Quick sync and LCD settings of the chassis using device service tag.
  dellemc.openmanage.ome_device_local_access_configuration:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tag: GHRT2RL
    quick_sync:
      quick_sync_access: READ_ONLY
      enable_read_authentication: true
      enable_quick_sync_wifi: true
      enable_inactivity_timeout: true
      timeout_limit: 10
      timeout_limit_unit: MINUTES
    lcd:
      lcd_access: VIEW_ONLY
      lcd_language: en
      user_defined: "LCD Text"

- name: Configure all local access settings of the host chassis.
  dellemc.openmanage.ome_device_local_access_configuration:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    enable_kvm_access: true
    enable_chassis_direct_access: false
    chassis_power_button:
      enable_chassis_power_button: false
      enable_lcd_override_pin: true
      disabled_button_lcd_override_pin: 123456
    quick_sync:
      quick_sync_access: READ_WRITE
      enable_read_authentication: true
      enable_quick_sync_wifi: true
      enable_inactivity_timeout: true
      timeout_limit: 120
      timeout_limit_unit: SECONDS
    lcd:
      lcd_access: VIEW_MODIFY
      lcd_language: en
      user_defined: "LCD Text"
```

## [Return Values](ome_device_local_access_configuration_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **location_details**  dictionary | returned when local access settings are updated successfully.  Returned: success  Sample: `{"EnableChassisDirect": false, "EnableChassisPowerButton": false, "EnableKvmAccess": true, "EnableLcdOverridePin": false, "LcdAccess": "VIEW_ONLY", "LcdCustomString": "LCD Text", "LcdLanguage": "en", "LcdOverridePin": "", "LcdPinLength": null, "LcdPresence": "Present", "LedPresence": null, "QuickSync": {"EnableInactivityTimeout": true, "EnableQuickSyncWifi": false, "EnableReadAuthentication": false, "QuickSyncAccess": "READ_ONLY", "QuickSyncHardware": "Present", "TimeoutLimit": 7, "TimeoutLimitUnit": "MINUTES"}, "SettingType": "LocalAccessConfiguration"}` |
| **msg**  string | Overall status of the device local access settings.  Returned: always  Sample: `"Successfully updated the local access settings."` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
