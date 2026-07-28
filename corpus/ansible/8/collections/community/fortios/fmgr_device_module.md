---
collection: ansible
version: "8"
title: "community.fortios.fmgr_device module – Add or remove device from FortiManager."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/fortios/fmgr_device_module.html
fetched_at: 2026-07-28T01:44:06+00:00
---
# community.fortios.fmgr_device module – Add or remove device from FortiManager.

> **Note:**
>
> This module is part of the [community.fortios collection](https://galaxy.ansible.com/ui/repo/published/community/fortios/) (version 1.0.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.fortios`.
>
> To use it in a playbook, specify: `community.fortios.fmgr_device`.

- [Synopsis](fmgr_device_module.md#synopsis)
- [Parameters](fmgr_device_module.md#parameters)
- [Notes](fmgr_device_module.md#notes)
- [Examples](fmgr_device_module.md#examples)
- [Return Values](fmgr_device_module.md#return-values)

## [Synopsis](fmgr_device_module.md#id1)

- Add or remove a device or list of devices from FortiManager Device Manager using JSON RPC API.

## [Parameters](fmgr_device_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string / required | The ADOM the configuration should belong to.  **Default:** `"root"` |
| **blind_add**  string | When adding a device, module will check if it exists, and skip if it does.  If enabled, this option will stop the module from checking if it already exists, and blindly add the device.  **Choices:**   - `"enable"` - `"disable"` ← (default) |
| **device_ip**  string | The IP of the device being added to FortiManager. Supports both IPv4 and IPv6. |
| **device_password**  string | The password of the device being added to FortiManager. |
| **device_serial**  string | The serial number of the device being added to FortiManager. |
| **device_unique_name**  string | The desired “friendly” name of the device being added to FortiManager. |
| **device_username**  string | The username of the device being added to FortiManager. |
| **mode**  string | The desired mode of the specified object.  **Choices:**   - `"add"` ← (default) - `"delete"` |

## [Notes](fmgr_device_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_device_module.md#id4)

```yaml+jinja
- name: DISCOVER AND ADD DEVICE FGT1
  community.fortios.fmgr_device:
    adom: "root"
    device_username: "admin"
    device_password: "admin"
    device_ip: "10.10.24.201"
    device_unique_name: "FGT1"
    device_serial: "FGVM000000117994"
    mode: "add"
    blind_add: "enable"

- name: DISCOVER AND ADD DEVICE FGT2
  community.fortios.fmgr_device:
    adom: "root"
    device_username: "admin"
    device_password: "admin"
    device_ip: "10.10.24.202"
    device_unique_name: "FGT2"
    device_serial: "FGVM000000117992"
    mode: "delete"
```

## [Return Values](fmgr_device_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  **Returned:** always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.fortios)
