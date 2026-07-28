---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_server_powerstate role – Role to manage the different power states of the specified device"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_server_powerstate_role.html
fetched_at: 2026-07-28T02:05:05+00:00
---
# dellemc.openmanage.idrac_server_powerstate role – Role to manage the different power states of the specified device

> **Note:**
>
> This role is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it use: `ansible-galaxy collection install dellemc.openmanage`.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_server_powerstate`.

- [Entry point `main` – Role to manage the different power states of the specified device](idrac_server_powerstate_role.md#entry-point-main-role-to-manage-the-different-power-states-of-the-specified-device)

  - [Synopsis](idrac_server_powerstate_role.md#synopsis)
  - [Parameters](idrac_server_powerstate_role.md#parameters)

## [Entry point `main` – Role to manage the different power states of the specified device](idrac_server_powerstate_role.md#id1)

New in dellemc.openmanage 7.4.0

### [Synopsis](idrac_server_powerstate_role.md#id2)

- Role to manage the different power states of the specified device using iDRACs (iDRAC7/8 and iDRAC9 only) for Dell PowerEdge servers.

### [Parameters](idrac_server_powerstate_role.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | iDRAC IP Address. |
| **https_port**  integer | iDRAC port.  **Default:** `443` |
| **https_timeout**  integer | The HTTPS socket level timeout in seconds.  **Default:** `30` |
| **password**  string / required | iDRAC user password. |
| **reset_type**  string | This option resets the device.  If `ForceOff`, Turns off the device immediately.  If `ForceOn`, Turns on the device immediately.  If `ForceRestart`, Turns off the device immediately, and then restarts the device.  If `GracefulRestart`, Performs graceful shutdown of the device, and then restarts the device.  If `GracefulShutdown`, Performs a graceful shutdown of the device, and the turns off the device.  If `Nmi`, Sends a diagnostic interrupt to the device. This is usually a non-maskable interrupt (NMI) on x86 device.  If `On`, Turns on the device.  If `PowerCycle`, Performs power cycle on the device.  If `PushPowerButton`, Simulates the pressing of a physical power button on the device.  When a power control operation is performed, which is not supported on the device, an error message is displayed with the list of operations that can be performed.  **Choices:**   - `"ForceOff"` - `"ForceOn"` - `"ForceRestart"` - `"GracefulRestart"` - `"GracefulShutdown"` - `"Nmi"` - `"On"` ← (default) - `"PowerCycle"` - `"PushPowerButton"` |
| **resource_id**  string | The unique identifier of the device being managed.  This option is mandatory for *hostname* with multiple devices. |
| **username**  string / required | iDRAC username. |
| **validate_certs**  boolean | If `false`, the SSL certificates will not be validated.  Configure `false` only on personally controlled sites where self-signed certificates are used.  **Choices:**   - `false` - `true` ← (default) |

#### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
