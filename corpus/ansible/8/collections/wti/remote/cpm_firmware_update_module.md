---
collection: ansible
version: "8"
title: "wti.remote.cpm_firmware_update module – Set Serial port parameters in WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_firmware_update_module.html
fetched_at: 2026-07-28T02:59:33+00:00
---
# wti.remote.cpm_firmware_update module – Set Serial port parameters in WTI OOB and PDU devices

> **Note:**
>
> This module is part of the [wti.remote collection](https://galaxy.ansible.com/ui/repo/published/wti/remote/) (version 1.0.5).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install wti.remote`.
>
> To use it in a playbook, specify: `wti.remote.cpm_firmware_update`.

New in wti.remote 2.9.0

- [Synopsis](cpm_firmware_update_module.md#synopsis)
- [Parameters](cpm_firmware_update_module.md#parameters)
- [Notes](cpm_firmware_update_module.md#notes)
- [Examples](cpm_firmware_update_module.md#examples)
- [Return Values](cpm_firmware_update_module.md#return-values)

## [Synopsis](cpm_firmware_update_module.md#id1)

- Set Serial port parameters in WTI OOB and PDU devices

## [Parameters](cpm_firmware_update_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cpm_file**  string | If a file is defined, this file will be used to update the WTI device. |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_path**  string | This is the directory path to store the WTI device configuration file.  **Default:** `"/tmp/"` |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **family**  integer | Force the download to both either Console (1) or Power (0)  **Choices:**   - `0` - `1` ← (default) |
| **removefileonexit**  integer | After an upgrade, remove the upgrade OS image  **Choices:**   - `0` - `1` ← (default) |
| **use_force**  boolean | If set to True, the upgrade will happen even if the device doesnt need it.  **Choices:**   - `false` ← (default) - `true` |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used - on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cpm_firmware_update_module.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.

## [Examples](cpm_firmware_update_module.md#id4)

```yaml+jinja
# Upgrade the firmware of a WTI device
- name: Upgrade the firmware of a WTI device
  cpm_firmware_update:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false

# Upgrade the firmware of a WTI device and keep the download OS image after exit
- name: Upgrade the firmware of a WTI device and keep the download OS image after exit
  cpm_firmware_update:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    removefileonexit: "0"
```

## [Return Values](cpm_firmware_update_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | The output XML configuration of the WTI device being updated  **Returned:** always |
| **filelength**  integer | Length of the file uploaded in bytes  **Returned:** success  **Sample:** `[{"filelength": 329439}]` |
| **status**  list / elements=string | List of status returns from backup operation  **Returned:** success  **Sample:** `[{"code": 0}, {"text": "ok"}, {"unittimestamp": "2020-02-14T00:18:57+00:00"}]` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

### Collection links

- [Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
- [Homepage](https://www.wti.com)
- [Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
