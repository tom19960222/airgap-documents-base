---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_attributes module – Configure the iDRAC attributes."
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_attributes_module.html
fetched_at: 2026-07-28T02:04:01+00:00
---
# dellemc.openmanage.idrac_attributes module – Configure the iDRAC attributes.

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
> see [Requirements](idrac_attributes_module.md#ansible-collections-dellemc-openmanage-idrac-attributes-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_attributes`.

New in dellemc.openmanage 6.0.0

- [Synopsis](idrac_attributes_module.md#synopsis)
- [Requirements](idrac_attributes_module.md#requirements)
- [Parameters](idrac_attributes_module.md#parameters)
- [Notes](idrac_attributes_module.md#notes)
- [Examples](idrac_attributes_module.md#examples)
- [Return Values](idrac_attributes_module.md#return-values)

## [Synopsis](idrac_attributes_module.md#id1)

- This module allows to configure the iDRAC attributes.

## [Requirements](idrac_attributes_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](idrac_attributes_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **idrac_attributes**  dictionary | Dictionary of iDRAC attributes and value. The attributes should be part of the Integrated Dell Remote Access Controller Attribute Registry. To view the list of attributes in Attribute Registry for iDRAC9 and above, see, <https://I(idrac_ip>/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/iDRAC.Embedded.1) and <https://I(idrac_ip>/redfish/v1/Registries/ManagerAttributeRegistry).  For iDRAC7 and iDRAC8 based servers, derive the manager attribute name from Server Configuration Profile. If the manager attribute name in Server Configuration Profile is <GroupName>.<Instance>#<AttributeName> (for Example, ‘SNMP.1#AgentCommunity’) then the equivalent attribute name for Redfish is <GroupName>.<Instance>.<AttributeName> (for Example, ‘SNMP.1.AgentCommunity’). |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  **Default:** `443` |
| **idrac_user**  string / required | iDRAC username. |
| **lifecycle_controller_attributes**  dictionary | Dictionary of Lifecycle Controller attributes and value. The attributes should be part of the Integrated Dell Remote Access Controller Attribute Registry.To view the list of attributes in Attribute Registry for iDRAC9 and above, see, <https://I(idrac_ip>/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/LifecycleController.Embedded.1) and <https://I(idrac_ip>/redfish/v1/Registries/ManagerAttributeRegistry).  For iDRAC7 and iDRAC8 based servers, derive the manager attribute name from Server Configuration Profile. If the manager attribute name in Server Configuration Profile is <GroupName>.<Instance>#<AttributeName> (for Example, ‘LCAttributes.1#AutoUpdate’) then the equivalent attribute name for Redfish is <GroupName>.<Instance>.<AttributeName> (for Example, ‘LCAttributes.1.AutoUpdate’). |
| **resource_id**  string | Redfish ID of the resource. |
| **system_attributes**  dictionary | Dictionary of System attributes and value. The attributes should be part of the Integrated Dell Remote Access Controller Attribute Registry. To view the list of attributes in Attribute Registry for iDRAC9 and above, see, <https://I(idrac_ip>/redfish/v1/Managers/iDRAC.Embedded.1/Oem/Dell/DellAttributes/System.Embedded.1) and <https://I(idrac_ip>/redfish/v1/Registries/ManagerAttributeRegistry).  For iDRAC7 and iDRAC8 based servers, derive the manager attribute name from Server Configuration Profile. If the manager attribute name in Server Configuration Profile is <GroupName>.<Instance>#<AttributeName> (for Example, ‘ThermalSettings.1#ThermalProfile’) then the equivalent attribute name for Redfish is <GroupName>.<Instance>.<AttributeName> (for Example, ‘ThermalSettings.1.ThermalProfile’). |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](idrac_attributes_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell iDRAC.
> - This module supports `check_mode`.
> - For iDRAC7 and iDRAC8 based servers, the value provided for the attributes are not be validated. Ensure appropriate values are passed.

## [Examples](idrac_attributes_module.md#id5)

```yaml+jinja
---
- name: Configure iDRAC attributes
  dellemc.openmanage.idrac_attributes:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    idrac_attributes:
      SNMP.1.AgentCommunity: public

- name: Configure System attributes
  dellemc.openmanage.idrac_attributes:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    system_attributes:
      ThermalSettings.1.ThermalProfile: Sound Cap

- name: Configure Lifecycle Controller attributes
  dellemc.openmanage.idrac_attributes:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    lifecycle_controller_attributes:
      LCAttributes.1.AutoUpdate: Enabled

- name: Configure the iDRAC attributes for email alert settings.
  dellemc.openmanage.idrac_attributes:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    idrac_attributes:
      EmailAlert.1.CustomMsg: Display Message
      EmailAlert.1.Enable: Enabled
      EmailAlert.1.Address: test@test.com

- name: Configure the iDRAC attributes for SNMP alert settings.
  dellemc.openmanage.idrac_attributes:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    idrac_attributes:
      SNMPAlert.1.Destination: 192.168.0.2
      SNMPAlert.1.State: Enabled
      SNMPAlert.1.SNMPv3Username: username

- name: Configure the iDRAC attributes for SMTP alert settings.
  dellemc.openmanage.idrac_attributes:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    idrac_attributes:
      RemoteHosts.1.SMTPServerIPAddress: 192.168.0.3
      RemoteHosts.1.SMTPAuthentication: Enabled
      RemoteHosts.1.SMTPPort: 25
      RemoteHosts.1.SMTPUserName: username
      RemoteHosts.1.SMTPPassword: password

- name: Configure the iDRAC attributes for webserver settings.
  dellemc.openmanage.idrac_attributes:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    idrac_attributes:
      WebServer.1.SSLEncryptionBitLength: 128-Bit or higher
      WebServer.1.TLSProtocol: TLS 1.1 and Higher

- name: Configure the iDRAC attributes for SNMP settings.
  dellemc.openmanage.idrac_attributes:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    idrac_attributes:
      SNMP.1.SNMPProtocol: All
      SNMP.1.AgentEnable: Enabled
      SNMP.1.TrapFormat: SNMPv1
      SNMP.1.AlertPort: 162
      SNMP.1.AgentCommunity: public

- name: Configure the iDRAC LC attributes for collecting system inventory.
  dellemc.openmanage.idrac_attributes:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    lifecycle_controller_attributes:
      LCAttributes.1.CollectSystemInventoryOnRestart: Enabled

- name: Configure the iDRAC system attributes for LCD configuration.
  dellemc.openmanage.idrac_attributes:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    system_attributes:
      LCD.1.Configuration: Service Tag
      LCD.1.vConsoleIndication: Enabled
      LCD.1.FrontPanelLocking: Full-Access
      LCD.1.UserDefinedString: custom string

- name: Configure the iDRAC attributes for Timezone settings.
  dellemc.openmanage.idrac_attributes:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    idrac_attributes:
      Time.1.TimeZone: CST6CDT
      NTPConfigGroup.1.NTPEnable: Enabled
      NTPConfigGroup.1.NTP1: 192.168.0.5
      NTPConfigGroup.1.NTP2: 192.168.0.6
      NTPConfigGroup.1.NTP3: 192.168.0.7

- name: Configure all attributes
  dellemc.openmanage.idrac_attributes:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    idrac_attributes:
      SNMP.1.AgentCommunity: test
      SNMP.1.AgentEnable: Enabled
      SNMP.1.DiscoveryPort: 161
    system_attributes:
      ServerOS.1.HostName: demohostname
    lifecycle_controller_attributes:
      LCAttributes.1.AutoUpdate: Disabled
```

## [Return Values](idrac_attributes_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Error information of the operation.  **Returned:** when attribute value is invalid.  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "The value 'false' for the property LCAttributes.1.BIOSRTDRequested is of a different type than the property can accept.", "MessageArgs": ["false", "LCAttributes.1.BIOSRTDRequested"], "MessageArgs@odata.count": 2, "MessageId": "Base.1.12.PropertyValueTypeError", "RelatedProperties": ["#/Attributes/LCAttributes.1.BIOSRTDRequested"], "RelatedProperties@odata.count": 1, "Resolution": "Correct the value for the property in the request body and resubmit the request if the operation failed.", "Severity": "Warning"}], "code": "Base.1.12.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information"}}` |
| **invalid_attributes**  dictionary | Dict of invalid attributes provided.  **Returned:** on invalid attributes or values.  **Sample:** `{"LCAttributes.1.AutoUpdate": "Invalid value for Enumeration.", "LCAttributes.1.StorageHealthRollupStatus": "Read only Attribute cannot be modified.", "SNMP.1.AlertPort": "Not a valid integer.", "SNMP.1.AlertPorty": "Attribute does not exist.", "SysLog.1.PowerLogInterval": "Integer out of valid range.", "ThermalSettings.1.AirExhaustTemp": "Invalid value for Enumeration."}` |
| **msg**  string | Status of the attribute update operation.  **Returned:** always  **Sample:** `"Successfully updated the attributes."` |

### Authors

- Husniya Abdul Hameed (@husniya-hameed)
- Felix Stephen (@felixs88)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
