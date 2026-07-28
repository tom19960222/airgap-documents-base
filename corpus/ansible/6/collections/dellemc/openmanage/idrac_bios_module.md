---
collection: ansible
version: "6"
title: "dellemc.openmanage.idrac_bios module – Configure the BIOS attributes"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/idrac_bios_module.html
fetched_at: 2026-07-27T17:25:09+00:00
---
# dellemc.openmanage.idrac_bios module – Configure the BIOS attributes

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
> see [Requirements](idrac_bios_module.md#ansible-collections-dellemc-openmanage-idrac-bios-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_bios`.

New in dellemc.openmanage 2.1.0

- [Synopsis](idrac_bios_module.md#synopsis)
- [Requirements](idrac_bios_module.md#requirements)
- [Parameters](idrac_bios_module.md#parameters)
- [Notes](idrac_bios_module.md#notes)
- [Examples](idrac_bios_module.md#examples)
- [Return Values](idrac_bios_module.md#return-values)

## [Synopsis](idrac_bios_module.md#id1)

- This module allows to configure the BIOS attributes.

## [Requirements](idrac_bios_module.md#id2)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.488
- python >= 3.8.6

## [Parameters](idrac_bios_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **attributes**  dictionary | Dictionary of BIOS attributes and value pair. Attributes should be part of the Redfish Dell BIOS Attribute Registry. Use <https://I%28idrac_ip>/redfish/v1/Systems/System.Embedded.1/Bios) to view the Redfish URI.  If deprecated options are provided and the same is repeated in *attributes* then values in *attributes* will take precedence.  *attributes* is mutually exclusive with *boot_sources*. |
| **boot_mode**  string | (deprecated)Sets boot mode to BIOS or UEFI.  This option is deprecated, and will be removed in later version. Use *attributes* for configuring the BIOS attributes.  *boot_mode* is mutually exclusive with *boot_sources*.  Choices:   - `"Bios"` - `"Uefi"` |
| **boot_sequence**  string | (deprecated)Allows to set the boot sequence in BIOS boot mode or Secure UEFI boot mode by rearranging the boot entries in Fully Qualified Device Descriptor (FQDD).  TThis option is deprecated, and will be removed in later version. Use *attributes* for configuring the BIOS attributes.  *boot_sequence* is mutually exclusive with *boot_sources*. |
| **boot_sources**  list / elements=any | List of boot devices to set the boot sources settings.  *boot_sources* is mutually exclusive with *attributes*, *boot_sequence*, *onetime_boot_mode*, *secure_boot_mode*, *nvme_mode*, *boot_mode*. |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  Default: `443` |
| **idrac_user**  string / required | iDRAC username. |
| **nvme_mode**  string | (deprecated)Configures the NVME mode in the iDRAC 9 based PowerEdge Servers.  This option is deprecated, and will be removed in later version. Use *attributes* for configuring the BIOS attributes.  *nvme_mode* is mutually exclusive with *boot_sources*.  Choices:   - `"NonRaid"` - `"Raid"` |
| **onetime_boot_mode**  string | (deprecated)Configures the one time boot mode setting.  This option is deprecated, and will be removed in later version. Use *attributes* for configuring the BIOS attributes.  *onetime_boot_mode* is mutually exclusive with *boot_sources*.  Choices:   - `"Disabled"` - `"OneTimeBootSeq"` - `"OneTimeCustomBootSeqStr"` - `"OneTimeCustomHddSeqStr"` - `"OneTimeCustomUefiBootSeqStr"` - `"OneTimeHddSeq"` - `"OneTimeUefiBootSeq"` |
| **secure_boot_mode**  string | (deprecated)Configures how the BIOS uses the Secure Boot Policy Objects in iDRAC 9 based PowerEdge Servers.  This option is deprecated, and will be removed in later version. Use *attributes* for configuring the BIOS attributes.  *secure_boot_mode* is mutually exclusive with *boot_sources*.  Choices:   - `"AuditMode"` - `"DeployedMode"` - `"SetupMode"` - `"UserMode"` |
| **share_mnt**  string | Local mount path of the network share with read-write permission for ansible user. This option is mandatory for network shares. |
| **share_name**  string | Network share or a local path. |
| **share_password**  aliases: share_pwd  string | Network share user password. This option is mandatory for CIFS share. |
| **share_user**  string | Network share user name. Use the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\user’ if user is part of a domain. This option is mandatory for CIFS share. |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](idrac_bios_module.md#id4)

> **Note:**
>
> - This module requires ‘Administrator’ privilege for *idrac_user*.
> - Run this module from a system that has direct access to DellEMC iDRAC.
> - This module supports `check_mode`.

## [Examples](idrac_bios_module.md#id5)

```yaml+jinja
---
- name: Configure generic attributes of the BIOS
  dellemc.openmanage.idrac_bios:
    idrac_ip:   "192.168.0.1"
    idrac_user: "user_name"
    idrac_password:  "user_password"
    ca_path: "/path/to/ca_cert.pem"
    attributes:
      BootMode : "Bios"
      OneTimeBootMode: "Enabled"
      BootSeqRetry: "Enabled"

- name: Configure PXE generic attributes
  dellemc.openmanage.idrac_bios:
    idrac_ip:   "192.168.0.1"
    idrac_user: "user_name"
    idrac_password:  "user_password"
    ca_path: "/path/to/ca_cert.pem"
    attributes:
      PxeDev1EnDis: "Enabled"
      PxeDev1Protocol: "IPV4"
      PxeDev1VlanEnDis: "Enabled"
      PxeDev1VlanId: 1
      PxeDev1Interface: "NIC.Embedded.1-1-1"
      PxeDev1VlanPriority: 2

- name: Configure boot sources
  dellemc.openmanage.idrac_bios:
    idrac_ip:   "192.168.0.1"
    idrac_user: "user_name"
    idrac_password:  "user_password"
    ca_path: "/path/to/ca_cert.pem"
    boot_sources:
      - Name : "NIC.Integrated.1-2-3"
        Enabled : true
        Index : 0

- name: Configure multiple boot sources
  dellemc.openmanage.idrac_bios:
    idrac_ip:   "192.168.0.1"
    idrac_user: "user_name"
    idrac_password:  "user_password"
    ca_path: "/path/to/ca_cert.pem"
    boot_sources:
      - Name : "NIC.Integrated.1-1-1"
        Enabled : true
        Index : 0
      - Name : "NIC.Integrated.2-2-2"
        Enabled : true
        Index : 1
      - Name : "NIC.Integrated.3-3-3"
        Enabled : true
        Index : 2

- name: Configure boot sources - Enabling
  dellemc.openmanage.idrac_bios:
    idrac_ip:   "192.168.0.1"
    idrac_user: "user_name"
    idrac_password:  "user_password"
    ca_path: "/path/to/ca_cert.pem"
    boot_sources:
      - Name : "NIC.Integrated.1-1-1"
        Enabled : true

- name: Configure boot sources - Index
  dellemc.openmanage.idrac_bios:
    idrac_ip:   "192.168.0.1"
    idrac_user: "user_name"
    idrac_password:  "user_password"
    ca_path: "/path/to/ca_cert.pem"
    boot_sources:
      - Name : "NIC.Integrated.1-1-1"
        Index : 0
```

## [Return Values](idrac_bios_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  dictionary | Configures the BIOS configuration attributes.  Returned: success  Sample: `{"@odata.context": "/redfish/v1/$metadata#DellJob.DellJob", "@odata.id": "/redfish/v1/Managers/iDRAC.Embedded.1/Jobs/JID_873888162305", "@odata.type": "#DellJob.v1_0_0.DellJob", "CompletionTime": "2020-04-20T18:50:20", "Description": "Job Instance", "EndTime": null, "Id": "JID_873888162305", "JobState": "Completed", "JobType": "ImportConfiguration", "Message": "Successfully imported and applied Server Configuration Profile.", "MessageArgs": [], "MessageId": "SYS053", "Name": "Import Configuration", "PercentComplete": 100, "StartTime": "TIME_NOW", "Status": "Success", "TargetSettingsURI": null, "retval": true}` |

### Authors

- Felix Stephen (@felixs88)
- Anooja Vardhineni (@anooja-vardhineni)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
