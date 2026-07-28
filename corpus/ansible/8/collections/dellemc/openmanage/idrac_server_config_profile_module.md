---
collection: ansible
version: "8"
title: "dellemc.openmanage.idrac_server_config_profile module – Export or Import iDRAC Server Configuration Profile (SCP)"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/idrac_server_config_profile_module.html
fetched_at: 2026-07-28T02:04:11+00:00
---
# dellemc.openmanage.idrac_server_config_profile module – Export or Import iDRAC Server Configuration Profile (SCP)

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

- Export the Server Configuration Profile (SCP) from the iDRAC or import from a network share (CIFS, NFS, HTTP, HTTPS) or a local path.

## [Requirements](idrac_server_config_profile_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9.14

## [Parameters](idrac_server_config_profile_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **command**  string | If `import`, the module performs SCP import operation.  If `export`, the module performs SCP export operation.  If `preview`, the module performs SCP preview operation.  **Choices:**   - `"import"` - `"export"` ← (default) - `"preview"` |
| **end_host_power_state**  string | This option is applicable for `import` command.  If `On`, End host power state is on.  If `Off`, End host power state is off.  **Choices:**   - `"On"` ← (default) - `"Off"` |
| **export_format**  string | Specify the output file format. This option is applicable for `export` command.  **Choices:**   - `"JSON"` - `"XML"` ← (default) |
| **export_use**  string  *added in dellemc.openmanage 7.3.0* | Specify the type of Server Configuration Profile (SCP) to be exported.  This option is applicable when *command* is `export`.  `Default` Creates a non-destructive snapshot of the configuration.  `Replace` Replaces a server with another or restores the servers settings to a known baseline.  `Clone` Clones settings from one server to another server with the identical hardware setup. All settings except I/O identity are updated (e.g. will reset RAID). The settings in this export will be destructive when uploaded to another system.  **Choices:**   - `"Default"` ← (default) - `"Clone"` - `"Replace"` |
| **idrac_ip**  string / required | iDRAC IP Address. |
| **idrac_password**  aliases: idrac_pwd  string / required | iDRAC user password. |
| **idrac_port**  integer | iDRAC port.  **Default:** `443` |
| **idrac_user**  string / required | iDRAC username. |
| **ignore_certificate_warning**  string  *added in dellemc.openmanage 7.3.0* | If `ignore`, it ignores the certificate warnings.  If `showerror`, it shows the certificate warnings.  *ignore_certificate_warning* is considered only when *share_name* is of type HTTPS and is supported only on iDRAC9.  **Choices:**   - `"ignore"` ← (default) - `"showerror"` |
| **import_buffer**  string  *added in dellemc.openmanage 7.3.0* | Used to import the buffer input of xml or json into the iDRAC.  This option is applicable when *command* is `import` and `preview`.  *import_buffer* is mutually exclusive with *share_name*. |
| **include_in_export**  string  *added in dellemc.openmanage 7.3.0* | This option is applicable when *command* is `export`.  If `default`, it exports the default Server Configuration Profile.  If `readonly`, it exports the SCP with readonly attributes.  If `passwordhashvalues`, it exports the SCP with password hash values.  If `customtelemetry`, exports the SCP with custom telemetry attributes supported only in the iDRAC9.  **Choices:**   - `"default"` ← (default) - `"readonly"` - `"passwordhashvalues"` - `"customtelemetry"` |
| **job_wait**  boolean / required | Whether to wait for job completion or not.  **Choices:**   - `false` - `true` |
| **proxy_password**  string  *added in dellemc.openmanage 7.3.0* | Proxy password to authenticate.  *proxy_password* is considered only when *share_name* is of type HTTP or HTTPS and is supported only on iDRAC9. |
| **proxy_port**  string  *added in dellemc.openmanage 7.3.0* | Proxy port to authenticate.  *proxy_port* is required when *share_name* is of type HTTPS or HTTP and *proxy_support* is `true`.  *proxy_port* is considered only when *share_name* is of type HTTP or HTTPS and is supported only on iDRAC9.  **Default:** `"80"` |
| **proxy_server**  string  *added in dellemc.openmanage 7.3.0* | *proxy_server* is required when *share_name* is of type HTTPS or HTTP and *proxy_support* is `true`.  *proxy_server* is considered only when *share_name* is of type HTTP or HTTPS and is supported only on iDRAC9. |
| **proxy_support**  boolean  *added in dellemc.openmanage 7.3.0* | Proxy to be enabled or disabled.  *proxy_support* is considered only when *share_name* is of type HTTP or HTTPS and is supported only on iDRAC9.  **Choices:**   - `false` ← (default) - `true` |
| **proxy_type**  string  *added in dellemc.openmanage 7.3.0* | `http` to select HTTP type proxy.  `socks4` to select SOCKS4 type proxy.  *proxy_type* is considered only when *share_name* is of type HTTP or HTTPS and is supported only on iDRAC9.  **Choices:**   - `"http"` ← (default) - `"socks4"` |
| **proxy_username**  string  *added in dellemc.openmanage 7.3.0* | Proxy username to authenticate.  *proxy_username* is considered only when *share_name* is of type HTTP or HTTPS and is supported only on iDRAC9. |
| **scp_components**  aliases: target  list / elements=string | If `ALL`, this module exports or imports all components configurations from SCP file.  If `IDRAC`, this module exports or imports iDRAC configuration from SCP file.  If `BIOS`, this module exports or imports BIOS configuration from SCP file.  If `NIC`, this module exports or imports NIC configuration from SCP file.  If `RAID`, this module exports or imports RAID configuration from SCP file.  When *command* is `export` or `import` *target* with multiple components is supported only on iDRAC9 with firmware 6.10.00.00 and above.  **Choices:**   - `"ALL"` ← (default) - `"IDRAC"` - `"BIOS"` - `"NIC"` - `"RAID"`   **Default:** `["ALL"]` |
| **scp_file**  string | Name of the server configuration profile (SCP) file.  This option is mandatory if *command* is `import`.  The default format <idrac_ip>_YYmmdd_HHMMSS_scp is used if this option is not specified for `import`.  *export_format* is used if the valid extension file is not provided for `import`. |
| **share_name**  string | Network share or local path.  CIFS, NFS, HTTP, and HTTPS network share types are supported.  *share_name* is mutually exclusive with *import_buffer*. |
| **share_password**  aliases: share_pwd  string | Network share user password. This option is mandatory for CIFS Network Share. |
| **share_user**  string | Network share user in the format [‘user@domain](mailto:'user%40domain)’ or ‘domain\\user’ if user is part of a domain else ‘user’. This option is mandatory for CIFS Network Share. |
| **shutdown_type**  string | This option is applicable for `import` command.  If `Graceful`, the job gracefully shuts down the operating system and turns off the server.  If `Forced`, it forcefully shuts down the server.  If `NoReboot`, the job that applies the SCP will pause until you manually reboot the server.  **Choices:**   - `"Graceful"` ← (default) - `"Forced"` - `"NoReboot"` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](idrac_server_config_profile_module.md#id4)

> **Note:**
>
> - This module requires ‘Administrator’ privilege for *idrac_user*.
> - Run this module from a system that has direct access to Dell iDRAC.
> - This module supports `check_mode`.
> - To import Server Configuration Profile (SCP) on the iDRAC7 and iDRAC8-based servers, the servers must have iDRAC Enterprise license or later.
> - For `import` operation, `check_mode` is supported only when *target* is `ALL`.

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
    scp_components:
      - IDRAC
    scp_file: example_file
    export_format: JSON
    export_use: Clone
    job_wait: true

- name: Import SCP with IDRAC components in JSON format from a local path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "/scp_folder"
    command: import
    scp_components:
      - IDRAC
    scp_file: example_file.json
    shutdown_type: Graceful
    end_host_power_state: "On"
    job_wait: false

- name: Export SCP with BIOS components in XML format to a NFS share path with auto-generated file name
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "192.168.0.2:/share"
    scp_components:
      - BIOS
    export_format: XML
    export_use: Default
    job_wait: true

- name: Import SCP with BIOS components in XML format from a NFS share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "192.168.0.2:/share"
    command: import
    scp_components:
      - BIOS
    scp_file: 192.168.0.1_20210618_162856.xml
    shutdown_type: NoReboot
    end_host_power_state: "Off"
    job_wait: false

- name: Export SCP with RAID components in XML format to a CIFS share path with share user domain name
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "\\\\192.168.0.2\\share"
    share_user: share_username@domain
    share_password: share_password
    scp_file: example_file.xml
    scp_components:
      - RAID
    export_format: XML
    export_use: Default
    job_wait: true

- name: Import SCP with RAID components in XML format from a CIFS share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "\\\\192.168.0.2\\share"
    share_user: share_username
    share_password: share_password
    command: import
    scp_components:
      - RAID
    scp_file: example_file.xml
    shutdown_type: Forced
    end_host_power_state: "On"
    job_wait: true

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
    scp_components:
      - ALL
    export_format: JSON
    job_wait: false

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
    job_wait: true

- name: Export SCP with ALL components in XML format to a HTTPS share path without SCP file name
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "192.168.0.1"
    idrac_user: "user_name"
    idrac_password: "user_password"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "https://192.168.0.4/share"
    share_user: share_username
    share_password: share_password
    scp_components:
      - ALL
    export_format: XML
    export_use: Replace
    job_wait: true

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
    job_wait: false

- name: Preview SCP with IDRAC components in XML format from a CIFS share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_password }}"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "\\\\192.168.0.2\\share"
    share_user: share_username
    share_password: share_password
    command: preview
    scp_components:
      - ALL
    scp_file: example_file.xml
    job_wait: true

- name: Preview SCP with IDRAC components in JSON format from a NFS share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_password }}"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "192.168.0.2:/share"
    command: preview
    scp_components:
      - IDRAC
    scp_file: example_file.xml
    job_wait: true

- name: Preview SCP with IDRAC components in XML format from a HTTP share path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_password }}"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "http://192.168.0.1/http-share"
    share_user: share_username
    share_password: share_password
    command: preview
    scp_components:
      - ALL
    scp_file: example_file.xml
    job_wait: true

- name: Preview SCP with IDRAC components in XML format from a local path
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_password }}"
    ca_path: "/path/to/ca_cert.pem"
    share_name: "/scp_folder"
    command: preview
    scp_components:
      - IDRAC
    scp_file: example_file.json
    job_wait: false

- name: Import SCP with IDRAC components in XML format from the XML content.
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_password }}"
    ca_path: "/path/to/ca_cert.pem"
    command: import
    scp_components:
      - IDRAC
    job_wait: True
    import_buffer: "<SystemConfiguration><Component FQDD='iDRAC.Embedded.1'><Attribute Name='IPMILan.1#Enable'>
      Disabled</Attribute></Component></SystemConfiguration>"

- name: Export SCP with ALL components in XML format using HTTP proxy.
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_password }}"
    ca_path: "/path/to/ca_cert.pem"
    scp_components:
      - ALL
    share_name: "http://192.168.0.1/http-share"
    proxy_support: true
    proxy_server: 192.168.0.5
    proxy_port: 8080
    proxy_username: proxy_username
    proxy_password: proxy_password
    proxy_type: http
    include_in_export: passwordhashvalues
    job_wait: true

- name: Import SCP with IDRAC and BIOS components in XML format using SOCKS4 proxy
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_password }}"
    ca_path: "/path/to/ca_cert.pem"
    command: import
    scp_components:
      - IDRAC
      - BIOS
    share_name: "https://192.168.0.1/http-share"
    proxy_support: true
    proxy_server: 192.168.0.6
    proxy_port: 8080
    proxy_type: socks4
    scp_file: filename.xml
    job_wait: true

- name: Import SCP with IDRAC components in JSON format from the JSON content.
  dellemc.openmanage.idrac_server_config_profile:
    idrac_ip: "{{ idrac_ip }}"
    idrac_user: "{{ idrac_user }}"
    idrac_password: "{{ idrac_password }}"
    ca_path: "/path/to/ca_cert.pem"
    command: import
    scp_components:
      - IDRAC
    job_wait: true
    import_buffer: "{\"SystemConfiguration\": {\"Components\": [{\"FQDD\": \"iDRAC.Embedded.1\",\"Attributes\":
      [{\"Name\": \"SNMP.1#AgentCommunity\",\"Value\": \"public1\"}]}]}}"
```

## [Return Values](idrac_server_config_profile_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Status of the import or export SCP job.  **Returned:** always  **Sample:** `"Successfully imported the Server Configuration Profile"` |
| **scp_status**  dictionary | SCP operation job and progress details from the iDRAC.  **Returned:** success  **Sample:** `{"Id": "JID_XXXXXXXXX", "JobState": "Completed", "JobType": "ImportConfiguration", "Message": "Successfully imported and applied Server Configuration Profile.", "MessageArgs": [], "MessageId": "XXX123", "Name": "Import Configuration", "PercentComplete": 100, "StartTime": "TIME_NOW", "Status": "Success", "TargetSettingsURI": null, "retval": true}` |

### Authors

- Jagadeesh N V(@jagadeeshnv)
- Felix Stephen (@felixs88)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
