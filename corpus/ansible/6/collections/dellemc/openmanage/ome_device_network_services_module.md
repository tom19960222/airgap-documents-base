---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_device_network_services module – Configure chassis network services settings on OpenManage Enterprise Modular"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_device_network_services_module.html
fetched_at: 2026-07-27T17:25:35+00:00
---
# dellemc.openmanage.ome_device_network_services module – Configure chassis network services settings on OpenManage Enterprise Modular

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
> see [Requirements](ome_device_network_services_module.md#ansible-collections-dellemc-openmanage-ome-device-network-services-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_device_network_services`.

New in dellemc.openmanage 4.3.0

- [Synopsis](ome_device_network_services_module.md#synopsis)
- [Requirements](ome_device_network_services_module.md#requirements)
- [Parameters](ome_device_network_services_module.md#parameters)
- [Notes](ome_device_network_services_module.md#notes)
- [Examples](ome_device_network_services_module.md#examples)
- [Return Values](ome_device_network_services_module.md#return-values)

## [Synopsis](ome_device_network_services_module.md#id1)

- This module allows to configure the network services on OpenManage Enterprise Modular.

## [Requirements](ome_device_network_services_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_device_network_services_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **device_id**  integer | The ID of the chassis for which the settings need to be updated.  If the device ID is not specified, this module updates the network services settings for the *hostname*.  *device_id* is mutually exclusive with *device_service_tag*. |
| **device_service_tag**  string | The service tag of the chassis for which the setting needs to be updated.  If the device service tag is not specified, this module updates the network services settings for the *hostname*.  *device_service_tag* is mutually exclusive with *device_id*. |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **remote_racadm_settings**  dictionary | The settings for remote RACADM configuration. |
| **enabled**  boolean / required | Enables or disables the remote RACADM settings.  Choices:   - `false` - `true` |
| **snmp_settings**  dictionary | The settings for SNMP configuration. |
| **community_name**  string | The SNMP community string.  Required when *enabled* is `true`. |
| **enabled**  boolean / required | Enables or disables the SNMP settings.  Choices:   - `false` - `true` |
| **port_number**  integer | The SNMP port number. |
| **ssh_settings**  dictionary | The settings for SSH configuration. |
| **enabled**  boolean / required | Enables or disables the SSH settings.  Choices:   - `false` - `true` |
| **idle_timeout**  float | SSH idle timeout in minutes. |
| **max_auth_retries**  integer | The number of retries when the SSH session fails. |
| **max_sessions**  integer | Number of SSH sessions. |
| **port_number**  integer | The port number for SSH service. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_device_network_services_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell EMC OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_device_network_services_module.md#id5)

```yaml+jinja
---
- name: Update network services settings of a chassis using the device ID
  dellemc.openmanage.ome_device_network_services:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_id: 25011
    snmp_settings:
      enabled: true
      port_number: 161
      community_name: public
    ssh_settings:
      enabled: false
    remote_racadm_settings:
      enabled: false

- name: Update network services settings of a chassis using the device service tag.
  dellemc.openmanage.ome_device_network_services:
    hostname: "192.168.0.2"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tag: GHRT2RL
    snmp_settings:
      enabled: false
    ssh_settings:
      enabled: true
      port_number: 22
      max_sessions: 1
      max_auth_retries: 3
      idle_timeout: 1
    remote_racadm_settings:
      enabled: false

- name: Update network services settings of the host chassis.
  dellemc.openmanage.ome_device_network_services:
    hostname: "192.168.0.3"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    snmp_settings:
      enabled: false
    ssh_settings:
      enabled: false
    remote_racadm_settings:
      enabled: true
```

## [Return Values](ome_device_network_services_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to update the network configuration because the SNMP PortNumber is already in use.", "MessageArgs": ["SNMP PortNumber"], "MessageId": "CAPP1042", "RelatedProperties": [], "Resolution": "Enter a different port number and retry the operation.", "Severity": "Informational"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the network services settings.  Returned: always  Sample: `"Successfully updated the network services settings."` |
| **network_services_details**  dictionary | returned when network services settings are updated successfully.  Returned: success  Sample: `{"EnableRemoteRacadm": true, "SettingType": "NetworkServices", "SnmpConfiguration": {"PortNumber": 161, "SnmpEnabled": true, "SnmpV1V2Credential": {"CommunityName": "public"}}, "SshConfiguration": {"IdleTimeout": 60, "MaxAuthRetries": 3, "MaxSessions": 1, "PortNumber": 22, "SshEnabled": false}}` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
