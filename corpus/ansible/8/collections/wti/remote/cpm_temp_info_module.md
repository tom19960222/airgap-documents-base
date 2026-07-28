---
collection: ansible
version: "8"
title: "wti.remote.cpm_temp_info module – Get temperature information from WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_temp_info_module.html
fetched_at: 2026-07-28T02:59:49+00:00
---
# wti.remote.cpm_temp_info module – Get temperature information from WTI OOB and PDU devices

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
> To use it in a playbook, specify: `wti.remote.cpm_temp_info`.

New in wti.remote 2.9.0

- [Synopsis](cpm_temp_info_module.md#synopsis)
- [Parameters](cpm_temp_info_module.md#parameters)
- [Notes](cpm_temp_info_module.md#notes)
- [Examples](cpm_temp_info_module.md#examples)
- [Return Values](cpm_temp_info_module.md#return-values)

## [Synopsis](cpm_temp_info_module.md#id1)

- Get temperature information from WTI OOB and PDU devices

## [Parameters](cpm_temp_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cpm_temp_info_module.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.)

## [Examples](cpm_temp_info_module.md#id4)

```yaml+jinja
- name: Get the Temperature Information of a WTI device
  cpm_temp_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false

- name: Get the Temperature Information of a WTI device
  cpm_temp_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: false
    validate_certs: false
```

## [Return Values](cpm_temp_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  **Returned:** always |
| **format**  string | Current Temperature format (Celsius or Fahrenheit) of the WTI device after module execution.  **Returned:** success  **Sample:** `"F"` |
| **status**  dictionary | Return status after module completion  **Returned:** always  **Sample:** `{"code": "0", "text": "OK"}` |
| **temperature**  string | Current Temperature of the WTI device after module execution.  **Returned:** success  **Sample:** `"76"` |
| **timestamp**  string | Current timestamp of the WTI device after module execution.  **Returned:** success  **Sample:** `"2020-02-24T20:54:03+00:00"` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

### Collection links

- [Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
- [Homepage](https://www.wti.com)
- [Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
