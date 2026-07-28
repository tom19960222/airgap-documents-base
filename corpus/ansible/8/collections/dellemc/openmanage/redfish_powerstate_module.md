---
collection: ansible
version: "8"
title: "dellemc.openmanage.redfish_powerstate module – Manage device power state"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/redfish_powerstate_module.html
fetched_at: 2026-07-28T02:04:57+00:00
---
# dellemc.openmanage.redfish_powerstate module – Manage device power state

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](redfish_powerstate_module.md#ansible-collections-dellemc-openmanage-redfish-powerstate-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.redfish_powerstate`.

New in dellemc.openmanage 2.1.0

- [Synopsis](redfish_powerstate_module.md#synopsis)
- [Requirements](redfish_powerstate_module.md#requirements)
- [Parameters](redfish_powerstate_module.md#parameters)
- [Notes](redfish_powerstate_module.md#notes)
- [Examples](redfish_powerstate_module.md#examples)
- [Return Values](redfish_powerstate_module.md#return-values)

## [Synopsis](redfish_powerstate_module.md#id1)

- This module allows to manage the different power states of the specified device.

## [Requirements](redfish_powerstate_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](redfish_powerstate_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **baseuri**  string / required | IP address of the target out-of-band controller. For example- <ipaddress>:<port>. |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **password**  string / required | Password of the target out-of-band controller. |
| **reset_type**  string / required | This option resets the device.  If `ForceOff`, Turns off the device immediately.  If `ForceOn`, Turns on the device immediately.  If `ForceRestart`, Turns off the device immediately, and then restarts the device.  If `GracefulRestart`, Performs graceful shutdown of the device, and then restarts the device.  If `GracefulShutdown`, Performs a graceful shutdown of the device, and the turns off the device.  If `Nmi`, Sends a diagnostic interrupt to the device. This is usually a non-maskable interrupt (NMI) on x86 device.  If `On`, Turns on the device.  If `PowerCycle`, Performs power cycle on the device.  If `PushPowerButton`, Simulates the pressing of a physical power button on the device.  When a power control operation is performed, which is not supported on the device, an error message is displayed with the list of operations that can be performed.  **Choices:**   - `"ForceOff"` - `"ForceOn"` - `"ForceRestart"` - `"GracefulRestart"` - `"GracefulShutdown"` - `"Nmi"` - `"On"` - `"PowerCycle"` - `"PushPowerButton"` |
| **resource_id**  string | The unique identifier of the device being managed. For example- <https://%3CI(baseuri>>/redfish/v1/Systems/<*resource_id*>).  This option is mandatory for *base_uri* with multiple devices.  To get the device details, use the API <https://%3CI(baseuri>>/redfish/v1/Systems). |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | Username of the target out-of-band controller. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](redfish_powerstate_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Redfish APIs.
> - This module supports `check_mode`.

## [Examples](redfish_powerstate_module.md#id5)

```yaml+jinja
---
- name: Manage power state of the first device
  dellemc.openmanage.redfish_powerstate:
       baseuri: "192.168.0.1"
       username: "username"
       password: "password"
       ca_path: "/path/to/ca_cert.pem"
       reset_type: "On"

- name: Manage power state of a specified device
  dellemc.openmanage.redfish_powerstate:
       baseuri: "192.168.0.1"
       username: "username"
       password: "password"
       ca_path: "/path/to/ca_cert.pem"
       reset_type: "ForceOff"
       resource_id: "System.Embedded.1"
```

## [Return Values](redfish_powerstate_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP error.  **Returned:** on http error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to complete the operation because the resource /redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset entered in not found.", "MessageArgs": ["/redfish/v1/Systems/System.Embedded.1/Actions/ComputerSystem.Reset"], "MessageArgs@odata.count": 1, "MessageId": "IDRAC.2.1.SYS403", "RelatedProperties": [], "RelatedProperties@odata.count": 0, "Resolution": "Enter the correct resource and retry the operation. For information about valid resource, see the Redfish Users Guide available on the support site.", "Severity": "Critical"}], "code": "Base.1.5.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information"}}` |
| **msg**  string | Overall status of the reset operation.  **Returned:** always  **Sample:** `"Successfully performed the reset type operation 'On'."` |

### Authors

- Sajna Shetty(@Sajna-Shetty)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
