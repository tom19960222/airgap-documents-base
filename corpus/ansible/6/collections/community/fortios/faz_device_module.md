---
collection: ansible
version: "6"
title: "community.fortios.faz_device module – Add or remove device"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/fortios/faz_device_module.html
fetched_at: 2026-07-27T17:07:36+00:00
---
# community.fortios.faz_device module – Add or remove device

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/community/fortios) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.faz_device`.

- [Synopsis](faz_device_module.md#synopsis)
- [Parameters](faz_device_module.md#parameters)
- [Examples](faz_device_module.md#examples)
- [Return Values](faz_device_module.md#return-values)

## [Synopsis](faz_device_module.md#id1)

- Add or remove a device or list of devices to FortiAnalyzer Device Manager. ADOM Capable.

## [Parameters](faz_device_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | The ADOM the configuration should belong to.  Default: `"root"` |
| **device_ip**  string | The IP of the device being added to FortiAnalyzer. |
| **device_password**  string | The password of the device being added to FortiAnalyzer. |
| **device_serial**  string | The serial number of the device being added to FortiAnalyzer. |
| **device_unique_name**  string | The desired “friendly” name of the device being added to FortiAnalyzer. |
| **device_username**  string | The username of the device being added to FortiAnalyzer. |
| **faz_quota**  string | Specifies the quota for the device in FAZ |
| **mgmt_mode**  string / required | Management Mode of the device you are adding.  Choices:   - `"unreg"` - `"fmg"` - `"faz"` - `"fmgfaz"` |
| **mode**  string | Add or delete devices. Or promote unregistered devices that are in the FortiAnalyzer “waiting pool”  Choices:   - `"add"` ← (default) - `"delete"` - `"promote"` |
| **os_minor_vers**  string / required | Minor OS rev of the device. |
| **os_type**  string / required | The os type of the device being added (default 0).  Choices:   - `"unknown"` - `"fos"` - `"fsw"` - `"foc"` - `"fml"` - `"faz"` - `"fwb"` - `"fch"` - `"fct"` - `"log"` - `"fmg"` - `"fsa"` - `"fdd"` - `"fac"` |
| **os_ver**  string / required | Major OS rev of the device  Choices:   - `"unknown"` - `"0.0"` - `"1.0"` - `"2.0"` - `"3.0"` - `"4.0"` - `"5.0"` - `"6.0"` |
| **platform_str**  string | Required for determine the platform for VM platforms. ie FortiGate-VM64 |

## [Examples](faz_device_module.md#id3)

```yaml+jinja
- name: DISCOVER AND ADD DEVICE A PHYSICAL FORTIGATE
  community.fortios.faz_device:
    adom: "root"
    device_username: "admin"
    device_password: "admin"
    device_ip: "10.10.24.201"
    device_unique_name: "FGT1"
    device_serial: "FGVM000000117994"
    state: "present"
    mgmt_mode: "faz"
    os_type: "fos"
    os_ver: "5.0"
    minor_rev: 6

- name: DISCOVER AND ADD DEVICE A VIRTUAL FORTIGATE
  community.fortios.faz_device:
    adom: "root"
    device_username: "admin"
    device_password: "admin"
    device_ip: "10.10.24.202"
    device_unique_name: "FGT2"
    mgmt_mode: "faz"
    os_type: "fos"
    os_ver: "5.0"
    minor_rev: 6
    state: "present"
    platform_str: "FortiGate-VM64"

- name: DELETE DEVICE FGT01
  community.fortios.faz_device:
    adom: "root"
    device_unique_name: "ansible-fgt01"
    mode: "delete"

- name: DELETE DEVICE FGT02
  community.fortios.faz_device:
    adom: "root"
    device_unique_name: "ansible-fgt02"
    mode: "delete"

- name: PROMOTE FGT01 IN FAZ BY IP
  community.fortios.faz_device:
    adom: "root"
    device_password: "fortinet"
    device_ip: "10.7.220.151"
    device_username: "ansible"
    mgmt_mode: "faz"
    mode: "promote"

- name: PROMOTE FGT02 IN FAZ
  community.fortios.faz_device:
    adom: "root"
    device_password: "fortinet"
    device_unique_name: "ansible-fgt02"
    device_username: "ansible"
    mgmt_mode: "faz"
    mode: "promote"
```

## [Return Values](faz_device_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  Returned: always |

### Authors

- Luke Weighall (@lweighall)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.fortios)
