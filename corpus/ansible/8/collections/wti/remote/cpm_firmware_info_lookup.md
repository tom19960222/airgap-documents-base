---
collection: ansible
version: "8"
title: "wti.remote.cpm_firmware_info lookup – Get firmware information from WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_firmware_info_lookup.html
fetched_at: 2026-07-28T02:59:56+00:00
---
# wti.remote.cpm_firmware_info lookup – Get firmware information from WTI OOB and PDU devices

> **Note:**
>
> This lookup plugin is part of the [wti.remote collection](https://galaxy.ansible.com/ui/repo/published/wti/remote/) (version 1.0.5).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install wti.remote`.
>
> To use it in a playbook, specify: `wti.remote.cpm_firmware_info`.

New in wti.remote 2.9.0

- [Synopsis](cpm_firmware_info_lookup.md#synopsis)
- [Keyword parameters](cpm_firmware_info_lookup.md#keyword-parameters)
- [Notes](cpm_firmware_info_lookup.md#notes)
- [Examples](cpm_firmware_info_lookup.md#examples)
- [Return Value](cpm_firmware_info_lookup.md#return-value)

## [Synopsis](cpm_firmware_info_lookup.md#id1)

- Get firmware information from WTI OOB and PDU devices

## [Keyword parameters](cpm_firmware_info_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('wti.remote.cpm_firmware_info', key1=value1, key2=value2, ...)` and `query('wti.remote.cpm_firmware_info', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cpm_firmware_info_lookup.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.)

## [Examples](cpm_firmware_info_lookup.md#id4)

```yaml+jinja
- name: Get the Firmware Information for a WTI device
  cpm_firmware_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false

- name: Get the Firmware Information for a WTI device
  cpm_firmware_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: false
    validate_certs: false
```

## [Return Value](cpm_firmware_info_lookup.md#id5)

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  **Returned:** always |
| **family**  string | Current family type (Console = 1 or Power = 0) of the WTI device.  **Returned:** success  **Sample:** `"1"` |
| **firmware**  string | Current Firmware version of the WTI device.  **Returned:** success  **Sample:** `"6.60"` |
| **status**  dictionary | Return status after module completion  **Returned:** always  **Sample:** `{"code": "0", "text": "OK"}` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

- [Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
- [Homepage](https://www.wti.com)
- [Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
