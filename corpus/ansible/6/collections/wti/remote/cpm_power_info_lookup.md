---
collection: ansible
version: "6"
title: "wti.remote.cpm_power_info lookup – Get the Power Information of a WTI device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/wti/remote/cpm_power_info_lookup.html
fetched_at: 2026-07-28T00:24:11+00:00
---
# wti.remote.cpm_power_info lookup – Get the Power Information of a WTI device

> **Note:**
>
> This lookup plugin is part of the [wti.remote collection](https://galaxy.ansible.com/wti/remote) (version 1.0.4).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install wti.remote`.
>
> To use it in a playbook, specify: `wti.remote.cpm_power_info`.

New in wti.remote 2.9.0

- [Synopsis](cpm_power_info_lookup.md#synopsis)
- [Keyword parameters](cpm_power_info_lookup.md#keyword-parameters)
- [Notes](cpm_power_info_lookup.md#notes)
- [Examples](cpm_power_info_lookup.md#examples)
- [Return Value](cpm_power_info_lookup.md#return-value)

## [Synopsis](cpm_power_info_lookup.md#id1)

- Get the Power Information of a WTI device

## [Keyword parameters](cpm_power_info_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('wti.remote.cpm_power_info', key1=value1, key2=value2, ...)` and `query('wti.remote.cpm_power_info', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **cpm_enddate**  string | End date of the range to look for power data |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_startdate**  string | Start date of the range to look for power data |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **use_https**  boolean | Designates to use an https connection or http connection.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](cpm_power_info_lookup.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.)

## [Examples](cpm_power_info_lookup.md#id4)

```yaml+jinja
- name: Get the Power Information of a WTI device
  cpm_power_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false

- name: Get the Power Information of a WTI device
  cpm_power_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: false
    validate_certs: false
    startdate: 01-12-2020"
    enddate: 02-16-2020"
```

## [Return Value](cpm_power_info_lookup.md#id5)

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  Returned: always |
| **ats**  string | Identifies if the WTI device is an ATS type of power device.  Returned: success  Sample: `"1"` |
| **outletmetering**  string | Identifies if the WTI device has Poiwer Outlet metering.  Returned: success  Sample: `"1"` |
| **plugcount**  string | Current outlet plug count of the WTI device after module execution.  Returned: success  Sample: `"8"` |
| **powerdata**  dictionary | Power data of the WTI device after module execution.  Returned: success  Sample: `[{"branch1": [{"current1": "0.00", "current2": "0.00", "current3": "0.00", "current4": "0.00", "current5": "0.00", "current6": "0.00", "current7": "0.00", "current8": "0.00", "voltage1": "118.00"}], "timestamp": "2020-02-24T21:45:18+00:00"}]` |
| **powerdatacount**  string | Total powerdata samples returned after module execution.  Returned: success  Sample: `"1"` |
| **powereff**  string | Power efficiency of the WTI device after module execution.  Returned: success  Sample: `"100"` |
| **powerfactor**  string | Power factor of the WTI device after module execution.  Returned: success  Sample: `"100"` |
| **powerunit**  string | Identifies if the WTI device is a power type device.  Returned: success  Sample: `"1"` |
| **status**  dictionary | Return status after module completion  Returned: always  Sample: `{"code": "0", "text": "OK"}` |
| **timestamp**  string | Current timestamp of the WTI device after module execution.  Returned: success  Sample: `"2020-02-24T20:54:03+00:00"` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
[Homepage](https://www.wti.com)
[Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
