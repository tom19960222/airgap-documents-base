---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_bios module – Modify and clear BIOS attributes, reset BIOS settings and configure boot sources"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_bios_module.html
fetched_at: 2026-07-28T02:04:02+00:00
---
# dellemc.openmanage.idrac_bios module – Modify and clear BIOS attributes, reset BIOS settings and configure boot sources

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

- This module allows to modify the BIOS attributes. Also clears pending BIOS attributes and resets BIOS to default settings.
- Boot sources can be enabled or disabled. Boot sequence can be configured.

## [Requirements](idrac_bios_module.md#id2)

The below requirements are needed on the host that executes this module.

- omsdk >= 1.2.490
- python >= 3.9.6

## [Parameters](idrac_bios_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **apply_time**  string | Apply time of the *attributes*.  This is applicable only to *attributes*.  `Immediate` Allows the user to immediately reboot the host and apply the changes. *job_wait* is applicable.  `OnReset` Allows the user to apply the changes on the next reboot of the host server.  `AtMaintenanceWindowStart` Allows the user to apply at the start of a maintenance window as specified in *maintenance_window*. A reboot job will be scheduled.  `InMaintenanceWindowOnReset` Allows to apply after a manual reset but within the maintenance window as specified in *maintenance_window*.  **Choices:**   - `"Immediate"` ← (default) - `"OnReset"` - `"AtMaintenanceWindowStart"` - `"InMaintenanceWindowOnReset"` |
| **attributes**  dictionary | Dictionary of BIOS attributes and value pair. Attributes should be part of the Redfish Dell BIOS Attribute Registry. Use <https://I(idrac_ip>/redfish/v1/Systems/System.Embedded.1/Bios) to view the Redfish URI.  This is mutually exclusive with *boot_sources*, *clear_pending*, and *reset_bios*. |
| **boot_sources**  list / elements=any | (deprecated)List of boot devices to set the boot sources settings.  *boot_sources* is mutually exclusive with *attributes*, *clear_pending*, and *reset_bios*.  *job_wait* is not applicable. The module waits till the completion of this task.  This feature is deprecated, please use [dellemc.openmanage.idrac_boot](idrac_boot_module.md#ansible-collections-dellemc-openmanage-idrac-boot-module) for configuring boot sources. |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **clear_pending**  boolean | Allows the user to clear all pending BIOS attributes changes.  `true` will discard any pending changes to bios attributes or remove job if in scheduled state.  This operation will not create any job.  `false` will not perform any operation.  This is mutually exclusive with *boot_sources*, *attributes*, and *reset_bios*.  `Note` Any BIOS job scheduled due to boot sources configuration will not be cleared.  **Choices:**   - `false` - `true` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  **Default:** `443` |
| **idrac_user**  string / required | iDRAC username. |
| **job_wait**  boolean | Provides the option to wait for job completion.  This is applicable for *attributes* when *apply_time* is `Immediate`.  **Choices:**   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer | The maximum wait time of *job_wait* in seconds. The job is tracked only for this duration.  This option is applicable when *job_wait* is `True`.  **Default:** `1200` |
| **maintenance_window**  dictionary | Option to schedule the maintenance window.  This is required when *apply_time* is `AtMaintenanceWindowStart` or `InMaintenanceWindowOnReset`. |
| **duration**  integer / required | The duration in seconds for the maintenance window. |
| **start_time**  string / required | The start time for the maintenance window to be scheduled.  The format is YYYY-MM-DDThh:mm:ss<offset>  <offset> is the time offset from UTC that the current timezone set in iDRAC in the format: +05:30 for IST. |
| **reset_bios**  boolean | Resets the BIOS to default settings and triggers a reboot of host system.  This is applied to the host after the restart.  This operation will not create any job.  `false` will not perform any operation.  This is mutually exclusive with *boot_sources*, *attributes*, and *clear_pending*.  When `true`, this action will always report as changes found to be applicable.  **Choices:**   - `false` - `true` |
| **reset_type**  string | `force_restart` Forcefully reboot the host system.  `graceful_restart` Gracefully reboot the host system.  This is applicable for *reset_bios*, and *attributes* when *apply_time* is `Immediate`.  **Choices:**   - `"graceful_restart"` ← (default) - `"force_restart"` |
| **share_mnt**  string | (deprecated)Local mount path of the network share with read-write permission for ansible user. This option is mandatory for network shares. |
| **share_name**  string | (deprecated)Network share or a local path. |
| **share_password**  aliases: share_pwd  string | (deprecated)Network share user password. This option is mandatory for CIFS share. |
| **share_user**  string | (deprecated)Network share user name. Use the format [‘user@domain](mailto:'user%40domain)’ or domain//user if user is part of a domain. This option is mandatory for CIFS share. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](idrac_bios_module.md#id4)

> **Note:**
>
> - omsdk is required to be installed only for *boot_sources* operation.
> - This module requires ‘Administrator’ privilege for *idrac_user*.
> - Run this module from a system that has direct access to Dell iDRAC.
> - This module supports both IPv4 and IPv6 address for *idrac_ip*.
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

- name: Configure BIOS attributes at Maintenance window
  dellemc.openmanage.idrac_bios:
    idrac_ip:   "192.168.0.1"
    idrac_user: "user_name"
    idrac_password:  "user_password"
    ca_path: "/path/to/ca_cert.pem"
    apply_time: AtMaintenanceWindowStart
    maintenance_window:
      start_time: "2022-09-30T05:15:40-05:00"
      duration: 600
    attributes:
      BootMode : "Bios"
      OneTimeBootMode: "Enabled"
      BootSeqRetry: "Enabled"

- name: Clear pending BIOS attributes
  dellemc.openmanage.idrac_bios:
    idrac_ip:   "192.168.0.1"
    idrac_user: "user_name"
    idrac_password:  "user_password"
    ca_path: "/path/to/ca_cert.pem"
    clear_pending: yes

- name: Reset BIOS attributes to default settings.
  dellemc.openmanage.idrac_bios:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_pwd }}"
    validate_certs: False
    reset_bios: yes

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
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **invalid_attributes**  dictionary | Dict of invalid attributes provided.  **Returned:** on invalid attributes or values.  **Sample:** `{"AcPwrRcvryUserDelay": "Integer out of valid range.", "AssetTag": "Attribute does not exist.", "BootSeqRetry": "Invalid value for Enumeration.", "Proc1Brand": "Read only Attribute cannot be modified.", "PxeDev1VlanId": "Not a valid integer."}` |
| **msg**  dictionary | Status of the job for *boot_sources* or status of the action performed on bios.  **Returned:** success  **Sample:** `{"CompletionTime": "2020-04-20T18:50:20", "Description": "Job Instance", "EndTime": null, "Id": "JID_873888162305", "JobState": "Completed", "JobType": "ImportConfiguration", "Message": "Successfully imported and applied Server Configuration Profile.", "MessageArgs": [], "MessageId": "SYS053", "Name": "Import Configuration", "PercentComplete": 100, "StartTime": "TIME_NOW", "Status": "Success", "TargetSettingsURI": null, "retval": true}` |
| **status_msg**  string | Overall status of the bios operation.  **Returned:** success  **Sample:** `"Successfully cleared pending BIOS attributes."` |

### Authors

- Felix Stephen (@felixs88)
- Anooja Vardhineni (@anooja-vardhineni)
- Jagadeesh N V (@jagadeeshnv)
- Shivam Sharma (@shivam-sharma)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
