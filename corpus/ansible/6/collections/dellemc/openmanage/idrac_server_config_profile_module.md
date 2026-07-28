---
collection: ansible
version: "6"
title: "dellemc.openmanage.idrac_server_config_profile module – Export or Import iDRAC Server Configuration Profile (SCP)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/idrac_server_config_profile_module.html
fetched_at: 2026-07-27T17:25:18+00:00
---
# dellemc.openmanage.idrac_server_config_profile module – Export or Import iDRAC Server Configuration Profile (SCP)

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
> see [Requirements](idrac_server_config_profile_module.md#ansible-collections-dellemc-openmanage-idrac-server-config-profile-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.idrac_server_config_profile`.

New in dellemc.openmanage 2.1.0

- [Synopsis](idrac_server_config_profile_module.md#synopsis)
- [Requirements](idrac_server_config_profile_module.md#requirements)
- [Parameters](idrac_server_config_profile_module.md#parameters)
- [Notes](idrac_server_config_profile_module.md#notes)
- [Examples](idrac_server_config_profile_module.md#examples)
- [Return Values](idrac_server_config_profile_module.md#return-values)

## [Synopsis](idrac_server_config_profile_module.md#id1)

- Export the Server Configuration Profile (SCP) from the iDRAC or import from a network share (CIFS, NFS, HTTP, HTTPS) or a local file.

## [Requirements](idrac_server_config_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](idrac_server_config_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **command**  string | If `import`, the module performs SCP import operation.  If `export`, the module performs SCP export operation.  If `preview`, the module performs SCP preview operation.  Choices:   - `"import"` - `"export"` ← (default) - `"preview"` |
| **end_host_power_state**  string | This option is applicable for `import` command.  If `On`, End host power state is on.  If `Off`, End host power state is off.  Choices:   - `"On"` ← (default) - `"Off"` |
| **export_format**  string | Specify the output file format. This option is applicable for `export` command.  Choices:   - `"JSON"` - `"XML"` ← (default) |
| **export_use**  string | Specify the type of server configuration profile (SCP) to be exported. This option is applicable for `export` command.  Choices:   - `"Default"` ← (default) - `"Clone"` - `"Replace"` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  Default: `443` |
| **idrac_user**  string / required | iDRAC username. |
| **job_wait**  boolean / required | Whether to wait for job completion or not.  Choices:   - `false` - `true` |
| **scp_components**  string | If `ALL`, this module exports or imports all components configurations from SCP file.  If `IDRAC`, this module exports or imports iDRAC configuration from SCP file.  If `BIOS`, this module exports or imports BIOS configuration from SCP file.  If `NIC`, this module exports or imports NIC configuration from SCP file.  If `RAID`, this module exports or imports RAID configuration from SCP file.  Choices:   - `"ALL"` ← (default) - `"IDRAC"` - `"BIOS"` - `"NIC"` - `"RAID"` |
| **scp_file**  string | Name of the server configuration profile (SCP) file.  This option is mandatory if *command* is `import`.  The default format <idrac_ip>_YYmmdd_HHMMSS_scp is used if this option is not specified for `import`.  *export_format* is used if the valid extension file is not provided for `import`. |
| **share_name**  string / required | Network share or local path.  CIFS, NFS, HTTP, and HTTPS network share types are supported. |
| **share_password**  aliases: share_pwd  string | Network share user password. This option is mandatory for CIFS Network Share. |
| **share_user**  string | Network share user in the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\\user’ if user is part of a domain else ‘user’. This option is mandatory for CIFS Network Share. |
| **shutdown_type**  string | This option is applicable for `import` command.  If `Graceful`, the job gracefully shuts down the operating system and turns off the server.  If `Forced`, it forcefully shuts down the server.  If `NoReboot`, the job that applies the SCP will pause until you manually reboot the server.  Choices:   - `"Graceful"` ← (default) - `"Forced"` - `"NoReboot"` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](idrac_server_config_profile_module.md#id4)

> **Note:**
>
> - This module requires ‘Administrator’ privilege for *idrac_user*.
> - Run this module from a system that has direct access to Dell EMC iDRAC.
> - This module supports `check_mode`.

## [Examples](idrac_server_config_profile_module.md#id5)

```yaml+jinja
---
- name: Export SCP with IDRAC components in JSON format to a local path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "/scp_folder"
    scp_components: IDRAC
    scp_file: example_file
    export_format: JSON
    export_use: Clone
    job_wait: True

- name: Import SCP with IDRAC components in JSON format from a local path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "/scp_folder"
    command: import
    scp_components: "IDRAC"
    scp_file: example_file.json
    shutdown_type: Graceful
    end_host_power_state: "On"
    job_wait: False

- name: Export SCP with BIOS components in XML format to a NFS share path with auto-generated file name
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "192.168.0.2:/share"
    scp_components: "BIOS"
    export_format: XML
    export_use: Default
    job_wait: True

- name: Import SCP with BIOS components in XML format from a NFS share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "192.168.0.2:/share"
    command: import
    scp_components: "BIOS"
    scp_file: 192.168.0.1_20210618_162856.xml
    shutdown_type: NoReboot
    end_host_power_state: "Off"
    job_wait: False

- name: Export SCP with RAID components in XML format to a CIFS share path with share user domain name
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "\\\\192.168.0.2\\share"
    share_user: share_username@domain
    share_password: share_password
    share_mnt: /mnt/cifs
    scp_file: example_file.xml
    scp_components: "RAID"
    export_format: XML
    export_use: Default
    job_wait: True

- name: Import SCP with RAID components in XML format from a CIFS share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "\\\\192.168.0.2\\share"
    share_user: share_username
    share_password: share_password
    share_mnt: /mnt/cifs
    command: import
    scp_components: "RAID"
    scp_file: example_file.xml
    shutdown_type: Forced
    end_host_power_state: "On"
    job_wait: True

- name: Export SCP with ALL components in JSON format to a HTTP share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "http://192.168.0.3/share"
    share_user: share_username
    share_password: share_password
    scp_file: example_file.json
    scp_components: ALL
    export_format: JSON
    job_wait: False

- name: Import SCP with ALL components in JSON format from a HTTP share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: import
    share_name: "http://192.168.0.3/share"
    share_user: share_username
    share_password: share_password
    scp_file: example_file.json
    shutdown_type: Graceful
    end_host_power_state: "On"
    job_wait: True

- name: Export SCP with ALL components in XML format to a HTTPS share path without SCP file name
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "https://192.168.0.4/share"
    share_user: share_username
    share_password: share_password
    scp_components: ALL
    export_format: XML
    export_use: Replace
    job_wait: True

- name: Import SCP with ALL components in XML format from a HTTPS share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    command: import
    share_name: "https://192.168.0.4/share"
    share_user: share_username
    share_password: share_password
    scp_file: 192.168.0.1_20160618_164647.xml
    shutdown_type: Graceful
    end_host_power_state: "On"
    job_wait: False

- name: Preview SCP with ALL components in XML format from a CIFS share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_password }}"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "\\\\192.168.0.2\\share"
    share_user: share_username
    share_password: share_password
    command: preview
    scp_components: "ALL"
    scp_file: example_file.xml
    job_wait: True

- name: Preview SCP with ALL components in JSON format from a NFS share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_password }}"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "192.168.0.2:/share"
    command: preview
    scp_components: "IDRAC"
    scp_file: example_file.xml
    job_wait: True

- name: Preview SCP with ALL components in XML format from a HTTP share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_password }}"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "http://192.168.0.1/http-share"
    share_user: share_username
    share_password: share_password
    command: preview
    scp_components: "ALL"
    scp_file: example_file.xml
    job_wait: True

- name: Preview SCP with ALL components in XML format from a local path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_password }}"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "/scp_folder"
    command: preview
    scp_components: "IDRAC"
    scp_file: example_file.json
    job_wait: False
```

## [Return Values](idrac_server_config_profile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Status of the import or export SCP job.  Returned: always  Sample: `"Successfully imported the Server Configuration Profile"` |
| **scp_status**  dictionary | SCP operation job and progress details from the iDRAC.  Returned: success  Sample: `{"Id": "JID_XXXXXXXXX", "JobState": "Completed", "JobType": "ImportConfiguration", "Message": "Successfully imported and applied Server Configuration Profile.", "MessageArgs": [], "MessageId": "XXX123", "Name": "Import Configuration", "PercentComplete": 100, "StartTime": "TIME_NOW", "Status": "Success", "TargetSettingsURI": null, "retval": true}` |

### Authors

- Jagadeesh N V(@jagadeeshnv)
- Felix Stephen (@felixs88)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
