---
collection: ansible
version: "6"
title: "wti.remote.cpm_status_info lookup – Get general status information from WTI OOB and PDU devices"
source_url: https://docs.ansible.com/projects/ansible/6/collections/wti/remote/cpm_status_info_lookup.html
fetched_at: 2026-07-28T00:24:16+00:00
---
# wti.remote.cpm_status_info lookup – Get general status information from WTI OOB and PDU devices

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
> To use it in a playbook, specify: `wti.remote.cpm_status_info`.

New in wti.remote 2.9.0

- [Synopsis](cpm_status_info_lookup.md#synopsis)
- [Keyword parameters](cpm_status_info_lookup.md#keyword-parameters)
- [Notes](cpm_status_info_lookup.md#notes)
- [Examples](cpm_status_info_lookup.md#examples)
- [Return Value](cpm_status_info_lookup.md#return-value)

## [Synopsis](cpm_status_info_lookup.md#id1)

- Get temperature general status from WTI OOB and PDU devices

## [Keyword parameters](cpm_status_info_lookup.md#id2)

This describes keyword parameters of the lookup. These are the values `key1=value1`, `key2=value2` and so on in the following
examples: `lookup('wti.remote.cpm_status_info', key1=value1, key2=value2, ...)` and `query('wti.remote.cpm_status_info', key1=value1, key2=value2, ...)`

| Parameter | Comments |
| --- | --- |
| **cpm_password**  string / required | This is the Password of the WTI device to send the module. |
| **cpm_url**  string / required | This is the URL of the WTI device to send the module. |
| **cpm_username**  string / required | This is the Username of the WTI device to send the module. |
| **use_https**  boolean | Designates to use an https connection or http connection.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | Flag to control if the lookup will observe HTTP proxy environment variables when present.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | If false, SSL certificates will not be validated. This should only be used  on personally controlled sites using self-signed certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](cpm_status_info_lookup.md#id3)

> **Note:**
>
> - Use `groups/cpm` in `module_defaults` to set common options used between CPM modules.)

## [Examples](cpm_status_info_lookup.md#id4)

```yaml+jinja
- name: Get the Status Information for a WTI device
  cpm_status_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: true
    validate_certs: false

- name: Get the Status Information for a WTI device
  cpm_status_info:
    cpm_url: "nonexist.wti.com"
    cpm_username: "super"
    cpm_password: "super"
    use_https: false
    validate_certs: false
```

## [Return Value](cpm_status_info_lookup.md#id5)

| Key | Description |
| --- | --- |
| **data**  complex | The output JSON returned from the commands sent  Returned: always |
| **analogmodemphonenumber**  string | Current Analog Modem (if installed) Phone number of the WTI device.  Returned: success  Sample: `"9495869959"` |
| **apacheversion**  string | Current Apache Web version running on the WTI device.  Returned: success  Sample: `"2.4.41"` |
| **apirelease**  string | Current Date of the API release of the WTI device.  Returned: success  Sample: `"March 2020"` |
| **assettag**  string | Current Asset Tag of the WTI device.  Returned: success  Sample: `"ARTE121"` |
| **cpu_boardprogramdate**  string | Current Board and Program date of the WTI device.  Returned: success  Sample: `"ARM, 4-30-2019"` |
| **currentmonitor**  string | Identifies if the unit has current monitoring capabilites.  Returned: success  Sample: `"Yes"` |
| **energywise**  string | Current Energywise version of the WTI device.  Returned: success  Sample: `"1.2.0"` |
| **gig_dualphy**  string | Identifies dual ethernet port and gigabyte ethernet ports in the WTI device.  Returned: success  Sample: `"Yes, Yes"` |
| **interface_list**  string | Current ethernet ports of the WTI device.  Returned: success  Sample: `"eth0"` |
| **keylength**  string | Current key length of the WTI device.  Returned: success  Sample: `"2048"` |
| **lineinputcount_rating**  string | Identifies total power inlets and their power rating.  Returned: success  Sample: `"1 ,  20 Amps"` |
| **macaddresses**  dictionary | Current mac addresses of the WTI device.  Returned: always  Sample: `{"mac": "00-09-9b-02-9a-26"}` |
| **modeminstalled**  string | Identifies if a modem is installed in the WTI device.  Returned: success  Sample: `"Yes, 4G/LTE"` |
| **modemmodel**  string | Identifies the modem model number (if installed) in the WTI device.  Returned: success  Sample: `"MTSMC-LVW2"` |
| **opensshversion**  string | Current OpenSSH running on the WTI device.  Returned: success  Sample: `"8.2p1"` |
| **opensslversion**  string | Current OpenSSL version running on the WTI device.  Returned: success  Sample: `"1.1.1d  10 Sep 2019"` |
| **option1/2**  string | Various Identity options of the WTI.  Returned: success  Sample: `"WPO-STRT-CPM8 / W4G-VZW-CPM8"` |
| **product**  string | Current Product Part Number of the WTI device.  Returned: success  Sample: `"CPM-800-1-CA"` |
| **ram_flash**  string | Total RAM and FLASH installed in the WTI device..  Returned: success  Sample: `"512 MB, 128 MB"` |
| **restful**  string | Current RESTful version of the WTI device.  Returned: success  Sample: `"v1.0, v2 (Mar20)"` |
| **serialnumber**  string | Current Serial number of the WTI device.  Returned: success  Sample: `"12345678901234"` |
| **siteid**  string | Current Site-ID of the WTI device.  Returned: success  Sample: `"GENEVARACK"` |
| **softwareversion**  string | Expanded Firmware version of the WTI device.  Returned: success  Sample: `"6.60 19 Feb 2020"` |
| **status**  dictionary | Return status after module completion  Returned: always  Sample: `{"code": "0", "text": "OK"}` |
| **totalplugs**  string | Total Power Outlet plugs of the WTI device.  Returned: success  Sample: `"8"` |
| **totalports**  string | Total serial ports of the WTI device.  Returned: success  Sample: `"9"` |
| **uptime**  string | Current uptime of the WTI device.  Returned: success  Sample: `"259308.26"` |
| **vendor**  string | Identifies WTI device as a WTI device.  Returned: success  Sample: `"wti"` |

### Authors

- Western Telematic Inc. (@wtinetworkgear)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/wtinetworkgear/wti-collection/issues)
[Homepage](https://www.wti.com)
[Repository (Sources)](https://github.com/wtinetworkgear/wti-collection)
