---
collection: ansible
version: "6"
title: "dellemc.openmanage.dellemc_configure_idrac_services module – Configures the iDRAC services related attributes"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/dellemc_configure_idrac_services_module.html
fetched_at: 2026-07-27T17:25:04+00:00
---
# dellemc.openmanage.dellemc_configure_idrac_services module – Configures the iDRAC services related attributes

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
> see [Requirements](dellemc_configure_idrac_services_module.md#ansible-collections-dellemc-openmanage-dellemc-configure-idrac-services-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.dellemc_configure_idrac_services`.

New in dellemc.openmanage 1.0.0

- [Synopsis](dellemc_configure_idrac_services_module.md#synopsis)
- [Requirements](dellemc_configure_idrac_services_module.md#requirements)
- [Parameters](dellemc_configure_idrac_services_module.md#parameters)
- [Notes](dellemc_configure_idrac_services_module.md#notes)
- [Examples](dellemc_configure_idrac_services_module.md#examples)
- [Return Values](dellemc_configure_idrac_services_module.md#return-values)

## [Synopsis](dellemc_configure_idrac_services_module.md#id1)

- This module allows to configure the iDRAC services related attributes.

## [Requirements](dellemc_configure_idrac_services_module.md#id2)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.8.6

## [Parameters](dellemc_configure_idrac_services_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **alert_port**  integer | The iDRAC port number that must be used for SNMP traps. The default value is 162, and the acceptable range is between 1 to 65535.  Default: `162` |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **community_name**  string | SNMP community name for iDRAC. It is used by iDRAC to validate SNMP queries received from remote systems requesting SNMP data access. |
| **discovery_port**  integer | The SNMP agent port on the iDRAC. The default value is 161, and the acceptable range is between 1 to 65535.  Default: `161` |
| **enable_web_server**  string | Whether to Enable or Disable webserver configuration for iDRAC.  Choices:   - `"Enabled"` - `"Disabled"` |
| **http_port**  integer | HTTP access port. |
| **https_port**  integer | HTTPS access port. |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  Default: `443` |
| **idrac_user**  string / required | iDRAC username. |
| **ipmi_lan**  dictionary | Community name set on iDRAC for SNMP settings. |
| **community_name**  string | This option is used by iDRAC when it sends out SNMP and IPMI traps. The community name is checked by the remote system to which the traps are sent. |
| **share_mnt**  string | Local mount path of the network share with read-write permission for ansible user. This option is mandatory for Network Share. |
| **share_name**  string / required | Network share or a local path. |
| **share_password**  aliases: share_pwd  string | Network share user password. This option is mandatory for CIFS Network Share. |
| **share_user**  string | Network share user in the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\user’ if user is part of a domain else ‘user’. This option is mandatory for CIFS Network Share. |
| **snmp_enable**  string | Whether to Enable or Disable SNMP protocol for iDRAC.  Choices:   - `"Enabled"` - `"Disabled"` |
| **snmp_protocol**  string | Type of the SNMP protocol.  Choices:   - `"All"` - `"SNMPv3"` |
| **ssl_encryption**  string | Secure Socket Layer encryption for webserver.  Choices:   - `"Auto_Negotiate"` - `"T_128_Bit_or_higher"` - `"T_168_Bit_or_higher"` - `"T_256_Bit_or_higher"` |
| **timeout**  string | Timeout value. |
| **tls_protocol**  string | Transport Layer Security for webserver.  Choices:   - `"TLS_1_0_and_Higher"` - `"TLS_1_1_and_Higher"` - `"TLS_1_2_Only"` |
| **trap_format**  string | SNMP trap format for iDRAC.  Choices:   - `"SNMPv1"` - `"SNMPv2"` - `"SNMPv3"` |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](dellemc_configure_idrac_services_module.md#id4)

> **Note:**
>
> - This module requires ‘Administrator’ privilege for *idrac_user*.
> - Run this module from a system that has direct access to Dell EMC iDRAC.
> - This module supports `check_mode`.

## [Examples](dellemc_configure_idrac_services_module.md#id5)

```yaml+jinja
---
- name: Configure the iDRAC services attributes
  dellemc.openmanage.dellemc_configure_idrac_services:
       idrac_ip:   "192.168.0.1"
       idrac_user: "user_name"
       idrac_password:  "user_password"
       ca_path: "/path/to/ca_cert.pem"
       share_name: "192.168.0.1:/share"
       share_mnt: "/mnt/share"
       enable_web_server: "Enabled"
       http_port: 80
       https_port: 443
       ssl_encryption: "Auto_Negotiate"
       tls_protocol: "TLS_1_2_Only"
       timeout: "1800"
       snmp_enable: "Enabled"
       snmp_protocol: "SNMPv3"
       community_name: "public"
       alert_port: 162
       discovery_port: 161
       trap_format: "SNMPv3"
       ipmi_lan:
         community_name: "public"
```

## [Return Values](dellemc_configure_idrac_services_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of iDRAC service attributes configuration.  Returned: always  Sample: `"Successfully configured the iDRAC services settings."` |
| **service_status**  dictionary | Details of iDRAC services attributes configuration.  Returned: success  Sample: `{"CompletionTime": "2020-04-02T02:43:28", "Description": "Job Instance", "EndTime": null, "Id": "JID_12345123456", "JobState": "Completed", "JobType": "ImportConfiguration", "Message": "Successfully imported and applied Server Configuration Profile.", "MessageArgs": [], "MessageId": "SYS053", "Name": "Import Configuration", "PercentComplete": 100, "StartTime": "TIME_NOW", "Status": "Success", "TargetSettingsURI": null, "retval": true}` |

### Authors

- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
