---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_network_port_breakout module – This module allows to automate the port portioning or port breakout to logical sub ports"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_network_port_breakout_module.html
fetched_at: 2026-07-28T02:04:41+00:00
---
# dellemc.openmanage.ome_network_port_breakout module – This module allows to automate the port portioning or port breakout to logical sub ports

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
> see [Requirements](ome_network_port_breakout_module.md#ansible-collections-dellemc-openmanage-ome-network-port-breakout-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_network_port_breakout`.

New in dellemc.openmanage 2.1.0

- [Synopsis](ome_network_port_breakout_module.md#synopsis)
- [Requirements](ome_network_port_breakout_module.md#requirements)
- [Parameters](ome_network_port_breakout_module.md#parameters)
- [Notes](ome_network_port_breakout_module.md#notes)
- [Examples](ome_network_port_breakout_module.md#examples)
- [Return Values](ome_network_port_breakout_module.md#return-values)

## [Synopsis](ome_network_port_breakout_module.md#id1)

- This module allows to automate breaking out of IOMs in fabric mode into logical sub ports.
- The port breakout operation is only supported in OpenManage Enterprise Modular.

## [Requirements](ome_network_port_breakout_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_network_port_breakout_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **breakout_type**  string / required | The preferred breakout type. For example, 4X10GE.  To revoke the default breakout configuration, enter ‘HardwareDefault’. |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **target_port**  string / required | The ID of the port in the switch to breakout. Enter the port ID in the format: service <tag:port>. For example, 2HB7NX2:ethernet1/1/13. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_network_port_breakout_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_network_port_breakout_module.md#id5)

```yaml+jinja
---
- name: Port breakout configuration
  dellemc.openmanage.ome_network_port_breakout:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    target_port: "2HB7NX2:phy-port1/1/11"
    breakout_type: "1X40GE"

- name: Revoke the default breakout configuration
  dellemc.openmanage.ome_network_port_breakout:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    target_port: "2HB7NX2:phy-port1/1/11"
    breakout_type: "HardwareDefault"
```

## [Return Values](ome_network_port_breakout_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **breakout_status**  dictionary | Details of the OpenManage Enterprise jobs.  **Returned:** success  **Sample:** `{"Builtin": false, "CreatedBy": "root", "Editable": true, "EndTime": null, "Id": 11111, "JobDescription": "", "JobName": "Breakout Port", "JobStatus": {"Id": 1112, "Name": "New"}, "JobType": {"Id": 3, "Internal": false, "Name": "DeviceAction_Task"}, "LastRun": null, "LastRunStatus": {"Id": 1113, "Name": "NotRun"}, "NextRun": null, "Params": [{"JobId": 11111, "Key": "operationName", "Value": "CONFIGURE_PORT_BREAK_OUT"}, {"JobId": 11111, "Key": "interfaceId", "Value": "2HB7NX2:phy-port1/1/11"}, {"JobId": 11111, "Key": "breakoutType", "Value": "1X40GE"}], "Schedule": "startnow", "StartTime": null, "State": "Enabled", "Targets": [{"Data": "", "Id": 11112, "JobId": 34206, "TargetType": {"Id": 1000, "Name": "DEVICE"}}], "UpdatedBy": null, "UserGenerated": true, "Visible": true}` |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the port configuration.  **Returned:** always  **Sample:** `"Port breakout configuration job submitted successfully."` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
