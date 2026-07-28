---
collection: ansible
version: "6"
title: "community.fortios.fmgr_device_config module – Edit device configurations"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/fortios/fmgr_device_config_module.html
fetched_at: 2026-07-27T17:07:37+00:00
---
# community.fortios.fmgr_device_config module – Edit device configurations

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
> To use it in a playbook, specify: `community.fortios.fmgr_device_config`.

- [Synopsis](fmgr_device_config_module.md#synopsis)
- [Parameters](fmgr_device_config_module.md#parameters)
- [Notes](fmgr_device_config_module.md#notes)
- [Examples](fmgr_device_config_module.md#examples)
- [Return Values](fmgr_device_config_module.md#return-values)

## [Synopsis](fmgr_device_config_module.md#id1)

- Edit device configurations from FortiManager Device Manager using JSON RPC API.

## [Parameters](fmgr_device_config_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **adom**  string | The ADOM the configuration should belong to.  Default: `"root"` |
| **device_hostname**  string | The device’s new hostname. |
| **device_unique_name**  string / required | The unique device’s name that you are editing. A.K.A. Friendly name of the device in FortiManager. |
| **install_config**  string | Tells FMGR to attempt to install the config after making it.  Default: `"disable"` |
| **interface**  string | The interface/port number you are editing. |
| **interface_allow_access**  string | Specify what protocols are allowed on the interface, comma-separated list (see examples). |
| **interface_ip**  string | The IP and subnet of the interface/port you are editing. |

## [Notes](fmgr_device_config_module.md#id3)

> **Note:**
>
> - Full Documentation at <https://ftnt-ansible-docs.readthedocs.io/en/latest/>.

## [Examples](fmgr_device_config_module.md#id4)

```yaml+jinja
- name: CHANGE HOSTNAME
  community.fortios.fmgr_device_config:
    device_hostname: "ChangedbyAnsible"
    device_unique_name: "FGT1"

- name: EDIT INTERFACE INFORMATION
  community.fortios.fmgr_device_config:
    adom: "root"
    device_unique_name: "FGT2"
    interface: "port3"
    interface_ip: "10.1.1.1/24"
    interface_allow_access: "ping, telnet, https"

- name: INSTALL CONFIG
  community.fortios.fmgr_device_config:
    adom: "root"
    device_unique_name: "FGT1"
    install_config: "enable"
```

## [Return Values](fmgr_device_config_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **api_result**  string | full API response, includes status code and message  Returned: always |

### Authors

- Luke Weighall (@lweighall)
- Andrew Welsh (@Ghilli3)
- Jim Huber (@p4r4n0y1ng)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.fortios/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.fortios)
