---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_firmware module – NetApp E-Series manage firmware."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_firmware_module.html
fetched_at: 2026-07-28T00:13:57+00:00
---
# netapp_eseries.santricity.na_santricity_firmware module – NetApp E-Series manage firmware.

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
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_firmware`.

- [Synopsis](na_santricity_firmware_module.md#synopsis)
- [Parameters](na_santricity_firmware_module.md#parameters)
- [Notes](na_santricity_firmware_module.md#notes)
- [Examples](na_santricity_firmware_module.md#examples)
- [Return Values](na_santricity_firmware_module.md#return-values)

## [Synopsis](na_santricity_firmware_module.md#id1)

- Ensure specific firmware versions are activated on E-Series storage system.

## [Parameters](na_santricity_firmware_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **clear_mel_events**  boolean | This flag will force firmware to be activated in spite of the storage system mel-event issues.  Warning! This will clear all storage system mel-events. Use at your own risk!  Choices:   - `false` ← (default) - `true` |
| **firmware**  string / required | Path to the firmware file.  Due to concurrency issues, use **ERROR while parsing**: While parsing M() at index 32: Module name “na_santricity_proxy_firmware_upload” is not a FQCN to upload firmware and nvsram to SANtricity Web Services Proxy when upgrading multiple systems at the same time on the same instance of the proxy. |
| **nvsram**  string | Path to the NVSRAM file.  NetApp recommends upgrading the NVSRAM when upgrading firmware.  Due to concurrency issues, use **ERROR while parsing**: While parsing M() at index 32: Module name “na_santricity_proxy_firmware_upload” is not a FQCN to upload firmware and nvsram to SANtricity Web Services Proxy when upgrading multiple systems at the same time on the same instance of the proxy. |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |
| **wait_for_completion**  boolean | This flag will cause module to wait for any upgrade actions to complete.  When changes are required to both firmware and nvsram and task is executed against SANtricity Web Services Proxy, the firmware will have to complete before nvsram can be installed.  Choices:   - `false` ← (default) - `true` |

## [Notes](na_santricity_firmware_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_firmware_module.md#id4)

```yaml+jinja
- name: Ensure correct firmware versions
  na_santricity_firmware:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    nvsram: "path/to/nvsram"
    firmware: "path/to/bundle"
    wait_for_completion: true
    clear_mel_events: true
- name: Ensure correct firmware versions
  na_santricity_firmware:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    nvsram: "path/to/nvsram"
    firmware: "path/to/firmware"
```

## [Return Values](na_santricity_firmware_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Status and version of firmware and NVSRAM.  Returned: always |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
