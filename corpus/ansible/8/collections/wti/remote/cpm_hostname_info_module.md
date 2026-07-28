---
collection: ansible
version: "8"
title: "wti.remote.cpm_hostname_info module – Get Hostname (Site ID), Location, Asset Tag parameters in WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_hostname_info_module.html
fetched_at: 2026-07-28T02:59:34+00:00
---
# wti.remote.cpm_hostname_info module – Get Hostname (Site ID), Location, Asset Tag parameters in WTI OOB and PDU devices

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
> To use it in a playbook, specify: `wti.remote.cpm_hostname_info`.

New in wti.remote 2.11.0

- [Synopsis](cpm_hostname_info_module.md#synopsis)
- [Parameters](cpm_hostname_info_module.md#parameters)
- [Notes](cpm_hostname_info_module.md#notes)
- [Examples](cpm_hostname_info_module.md#examples)
- [Return Values](cpm_hostname_info_module.md#return-values)

## [Synopsis](cpm_hostname_info_module.md#id1)

- Get Hostname (Site ID), Location, Asset Tag parameters from WTI OOB and PDU devices

## [Parameters](cpm_hostname_info_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cpm_hostname_info_module.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.)

## [Examples](cpm_hostname_info_module.md#id4)

```yaml+jinja
- name: Get the Hostname parameters for a WTI device
  cpm_hostname_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false

- name: Get the Hostname parameters for a WTI device
  cpm_hostname_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: false
    validate_certs: false
```

## [Return Values](cpm_hostname_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  **Returned:** always |
| **assettag**  integer | Current Asset Tag of the WTI device after module execution.  **Returned:** success  **Sample:** `"irvine92395"` |
| **hostname**  string | Current Hostname (Site-ID) of the WTI device after module execution.  **Returned:** success  **Sample:** `"myhostname"` |
| **location**  integer | Current Location of the WTI device after module execution.  **Returned:** success  **Sample:** `"Irvine"` |
| **timestamp**  string | Current timestamp of the WTI device after module execution.  **Returned:** success  **Sample:** `"2021-08-17T21:33:50+00:00"` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

### Collection links

- [Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
- [Homepage](https://www.wti.com)
- [Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
