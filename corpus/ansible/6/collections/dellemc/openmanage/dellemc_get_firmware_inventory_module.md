---
collection: ansible
version: "6"
title: "dellemc.openmanage.dellemc_get_firmware_inventory module – Get Firmware Inventory"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/dellemc_get_firmware_inventory_module.html
fetched_at: 2026-07-27T17:25:05+00:00
---
# dellemc.openmanage.dellemc_get_firmware_inventory module – Get Firmware Inventory

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/dellemc/openmanage) (version 5.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](dellemc_get_firmware_inventory_module.md#ansible-collections-dellemc-openmanage-dellemc-get-firmware-inventory-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.dellemc_get_firmware_inventory`.

New in dellemc.openmanage 1.0.0

- [DEPRECATED](dellemc_get_firmware_inventory_module.md#deprecated)
- [Synopsis](dellemc_get_firmware_inventory_module.md#synopsis)
- [Requirements](dellemc_get_firmware_inventory_module.md#requirements)
- [Parameters](dellemc_get_firmware_inventory_module.md#parameters)
- [Notes](dellemc_get_firmware_inventory_module.md#notes)
- [Examples](dellemc_get_firmware_inventory_module.md#examples)
- [Status](dellemc_get_firmware_inventory_module.md#status)

## [DEPRECATED](dellemc_get_firmware_inventory_module.md#id1)

Removed in:
:   major release after 2023-01-15

Why:
:   Replaced with [dellemc.openmanage.idrac_firmware_info](idrac_firmware_info_module.md#ansible-collections-dellemc-openmanage-idrac-firmware-info-module).

Alternative:
:   Use [dellemc.openmanage.idrac_firmware_info](idrac_firmware_info_module.md#ansible-collections-dellemc-openmanage-idrac-firmware-info-module) instead.

## [Synopsis](dellemc_get_firmware_inventory_module.md#id2)

- Get Firmware Inventory.

## [Requirements](dellemc_get_firmware_inventory_module.md#id3)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.8.6

## [Parameters](dellemc_get_firmware_inventory_module.md#id4)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  Default: `443` |
| **idrac_user**  string / required | iDRAC username. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](dellemc_get_firmware_inventory_module.md#id5)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC iDRAC.
> - This module supports `check_mode`.

## [Examples](dellemc_get_firmware_inventory_module.md#id6)

```yaml+jinja
---
- name: Get Installed Firmware Inventory
  dellemc.openmanage.dellemc_get_firmware_inventory:
      idrac_ip:   "192.168.0.1"
      idrac_user: "user_name"
      idrac_password:  "user_password"
      ca_path: "/path/to/ca_cert.pem"
```

## [Status](dellemc_get_firmware_inventory_module.md#id7)

- This module will be removed in a major release after 2023-01-15.
  *[deprecated]*
- For more information see [DEPRECATED](dellemc_get_firmware_inventory_module.md#deprecated).

### Authors

- Rajeev Arakkal (@rajeevarakkal)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
