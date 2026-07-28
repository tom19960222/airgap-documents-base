---
collection: ansible
version: "8"
title: "wti.remote.cpm_time_config module – Set Time/Date parameters in WTI OOB and PDU devices."
source_url: https://docs.ansible.com/projects/ansible/8/collections/wti/remote/cpm_time_config_module.html
fetched_at: 2026-07-28T02:59:50+00:00
---
# wti.remote.cpm_time_config module – Set Time/Date parameters in WTI OOB and PDU devices.

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
> To use it in a playbook, specify: `wti.remote.cpm_time_config`.

New in wti.remote 2.10.0

- [Synopsis](cpm_time_config_module.md#synopsis)
- [Parameters](cpm_time_config_module.md#parameters)
- [Notes](cpm_time_config_module.md#notes)
- [Examples](cpm_time_config_module.md#examples)
- [Return Values](cpm_time_config_module.md#return-values)

## [Synopsis](cpm_time_config_module.md#id1)

- Set Time/Date and NTP parameters parameters in WTI OOB and PDU devices

## [Parameters](cpm_time_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **date**  string | Static date in the format of two digit month, two digit day, four digit year separated by a slash symbol. |
| **ipv4address**  string | Comma separated string of up to two addresses for a primary and secondary IPv4 base NTP server. |
| **ipv6address**  string | Comma separated string of up to two addresses for a primary and secondary IPv6 base NTP server. |
| **ntpenable**  integer | This enables or disables the NTP client service.  **Choices:**   - `0` - `1` |
| **time**  string | Static time in the format of two digit hour, two digit minute, two digit second separated by a colon symbol. |
| **timeout**  integer | Set the network timeout in seconds of contacting the NTP servers, valid options can be from 1-60. |
| **timezone**  integer | This is timezone that is assigned to the WTI device. |
| **use_https**  boolean | Designates to use an https connection or http connection.  **Choices:**   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](cpm_time_config_module.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.

## [Examples](cpm_time_config_module.md#id4)

```yaml+jinja
# Set a static time/date and timezone of a WTI device
- name: Set known fixed time/date of a WTI device
  cpm_time_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    date: "12/12/2019"
    time: "09:23:46"
    timezone: 5

# Enable NTP and set primary and seconday servers of a WTI device
- name: Set NTP primary and seconday servers of a WTI device
  cpm_time_config:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false
    timezone: 5
    ntpenable: 1
    ipv4address: "129.6.15.28.pool.ntp.org"
    timeout: 15
```

## [Return Values](cpm_time_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  **Returned:** always |
| **date**  string | Current Date of the WTI device after module execution.  **Returned:** success  **Sample:** `"11/14/2019"` |
| **ntp**  dictionary | Current k/v pairs of ntp info of the WTI device after module execution.  **Returned:** always  **Sample:** `{"enable": "0", "ietf-ipv4": {"address": [{"primary": "192.168.0.169", "secondary": "12.34.56.78"}]}, "ietf-ipv6": {"address": [{"primary": "", "secondary": ""}]}, "timeout": "4"}` |
| **time**  string | Current Time of the WTI device after module execution.  **Returned:** success  **Sample:** `"12:12:00"` |
| **timezone**  integer | Current Timezone of the WTI device after module execution.  **Returned:** success  **Sample:** `5` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

### Collection links

- [Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
- [Homepage](https://www.wti.com)
- [Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
