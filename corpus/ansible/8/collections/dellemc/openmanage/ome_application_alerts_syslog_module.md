---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_application_alerts_syslog module – Configure syslog forwarding settings on OpenManage Enterprise and OpenManage Enterprise Modular"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_application_alerts_syslog_module.html
fetched_at: 2026-07-28T02:04:18+00:00
---
# dellemc.openmanage.ome_application_alerts_syslog module – Configure syslog forwarding settings on OpenManage Enterprise and OpenManage Enterprise Modular

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
> see [Requirements](ome_application_alerts_syslog_module.md#ansible-collections-dellemc-openmanage-ome-application-alerts-syslog-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_application_alerts_syslog`.

New in dellemc.openmanage 4.3.0

- [Synopsis](ome_application_alerts_syslog_module.md#synopsis)
- [Requirements](ome_application_alerts_syslog_module.md#requirements)
- [Parameters](ome_application_alerts_syslog_module.md#parameters)
- [Notes](ome_application_alerts_syslog_module.md#notes)
- [Examples](ome_application_alerts_syslog_module.md#examples)
- [Return Values](ome_application_alerts_syslog_module.md#return-values)

## [Synopsis](ome_application_alerts_syslog_module.md#id1)

- This module allows to configure syslog forwarding settings on OpenManage Enterprise and OpenManage Enterprise Modular.

## [Requirements](ome_application_alerts_syslog_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_application_alerts_syslog_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **syslog_servers**  list / elements=dictionary | List of servers to forward syslog. |
| **destination_address**  string | The IP address, FQDN or hostname of the syslog server.  This is required if *enabled* is `True`. |
| **enabled**  boolean | Enable or disable syslog forwarding.  **Choices:**   - `false` - `true` |
| **id**  integer / required | The ID of the syslog server.  **Choices:**   - `1` - `2` - `3` - `4` |
| **port_number**  integer | The UDP port number of the syslog server. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_application_alerts_syslog_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise or Dell OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_application_alerts_syslog_module.md#id5)

```yaml+jinja
---
- name: Configure single server to forward syslog
  dellemc.openmanage.ome_application_alerts_syslog:
    hostname: 192.168.0.1
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    syslog_servers:
      - id: 1
        enabled: true
        destination_address: 192.168.0.2
        port_number: 514

- name: Configure multiple server to forward syslog
  dellemc.openmanage.ome_application_alerts_syslog:
    hostname: 192.168.0.1
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    syslog_servers:
      - id: 1
        port_number: 523
      - id: 2
        enabled: true
        destination_address: sysloghost1.lab.com
      - id: 3
        enabled: false
      - id: 4
        enabled: true
        destination_address: 192.168.0.4
        port_number: 514
```

## [Return Values](ome_application_alerts_syslog_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to update the Syslog settings because the request contains an invalid number of configurations. The request must contain no more than 4 configurations but contains 5.", "MessageArgs": ["4", "5"], "MessageId": "CAPP1108", "RelatedProperties": [], "Resolution": "Enter only the required number of configurations as identified in the message and retry the operation.", "Severity": "Warning"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the syslog forwarding operation.  **Returned:** always  **Sample:** `"Successfully updated the syslog forwarding settings."` |
| **syslog_details**  list / elements=string | Syslog forwarding settings list applied.  **Returned:** on success  **Sample:** `[{"DestinationAddress": "192.168.10.43", "Enabled": false, "Id": 1, "PortNumber": 514}, {"DestinationAddress": "192.168.10.46", "Enabled": true, "Id": 2, "PortNumber": 514}, {"DestinationAddress": "192.168.10.44", "Enabled": true, "Id": 3, "PortNumber": 514}, {"DestinationAddress": "192.168.10.42", "Enabled": true, "Id": 4, "PortNumber": 515}]` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
