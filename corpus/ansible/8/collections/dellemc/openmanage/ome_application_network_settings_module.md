---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_application_network_settings module – This module allows you to configure the session inactivity timeout settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_application_network_settings_module.html
fetched_at: 2026-07-28T02:04:21+00:00
---
# dellemc.openmanage.ome_application_network_settings module – This module allows you to configure the session inactivity timeout settings

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
> see [Requirements](ome_application_network_settings_module.md#ansible-collections-dellemc-openmanage-ome-application-network-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_application_network_settings`.

New in dellemc.openmanage 4.4.0

- [Synopsis](ome_application_network_settings_module.md#synopsis)
- [Requirements](ome_application_network_settings_module.md#requirements)
- [Parameters](ome_application_network_settings_module.md#parameters)
- [Notes](ome_application_network_settings_module.md#notes)
- [Examples](ome_application_network_settings_module.md#examples)
- [Return Values](ome_application_network_settings_module.md#return-values)

## [Synopsis](ome_application_network_settings_module.md#id1)

- This module allows you to configure the session inactivity timeout settings on OpenManage Enterprise and OpenManage Enterprise Modular.

## [Requirements](ome_application_network_settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_application_network_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **session_inactivity_timeout**  dictionary | Session inactivity timeout settings. |
| **api_sessions**  integer | The maximum number of API sessions to be allowed. |
| **api_timeout**  float | Duration of inactivity in minutes after which the API session ends.  This is mutually exclusive with *universal_timeout*. |
| **enable_universal_timeout**  boolean | Enable or disable the universal inactivity timeout.  **Choices:**   - `false` - `true` |
| **gui_sessions**  integer | The maximum number of GUI sessions to be allowed. |
| **gui_timeout**  float | Duration of inactivity in minutes after which the web interface of Graphical User Interface (GUI) session ends.  This is mutually exclusive with *universal_timeout*. |
| **serial_sessions**  integer | The maximum number of serial console sessions to be allowed.  This is applicable only for OpenManage Enterprise Modular. |
| **serial_timeout**  float | Duration of inactivity in minutes after which the serial console session ends.  This is applicable only for OpenManage Enterprise Modular.  This is mutually exclusive with *universal_timeout*. |
| **ssh_sessions**  integer | The maximum number of SSH sessions to be allowed.  This is applicable to OME-M only. |
| **ssh_timeout**  float | Duration of inactivity in minutes after which the SSH session ends.  This is applicable only for OpenManage Enterprise Modular.  This is mutually exclusive with *universal_timeout*. |
| **universal_timeout**  float | Duration of inactivity in minutes after which all sessions end.  This is applicable when *enable_universal_timeout* is `true`.  This is mutually exclusive with *api_timeout*, *gui_timeout*, *ssh_timeout* and *serial_timeout*. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_application_network_settings_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise or OpenManage Enterprise Modular.
> - To configure other network settings such as network address, web server, and so on, refer to the respective OpenManage Enterprise application network setting modules.
> - This module supports `check_mode`.

## [Examples](ome_application_network_settings_module.md#id5)

```yaml+jinja
---
- name: Configure universal inactivity timeout
  ome_application_network_settings:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    session_inactivity_timeout:
      enable_universal_timeout: true
      universal_timeout: 30
      api_sessions: 90
      gui_sessions: 5
      ssh_sessions: 2
      serial_sessions: 1

- name: Configure API and GUI timeout and sessions
  ome_application_network_settings:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    session_inactivity_timeout:
      api_timeout: 20
      api_sessions: 100
      gui_timeout: 25
      gui_sessions: 5

- name: Configure timeout and sessions for all parameters
  ome_application_network_settings:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    session_inactivity_timeout:
      api_timeout: 20
      api_sessions: 100
      gui_timeout: 15
      gui_sessions: 5
      ssh_timeout: 30
      ssh_sessions: 2
      serial_timeout: 35
      serial_sessions: 1

- name: Disable universal timeout and configure timeout and sessions for other parameters
  ome_application_network_settings:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    session_inactivity_timeout:
      enable_universal_timeout: false
      api_timeout: 20
      api_sessions: 100
      gui_timeout: 15
      gui_sessions: 5
      ssh_timeout: 30
      ssh_sessions: 2
      serial_timeout: 35
      serial_sessions: 1
```

## [Return Values](ome_application_network_settings_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "The number of allowed concurrent sessions for API must be between 1 and 100 sessions.", "MessageArgs": ["API", "1", "100"], "MessageId": "CUSR1233", "RelatedProperties": [], "Resolution": "Enter values in the correct range and retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the Session timeout settings.  **Returned:** always  **Sample:** `"Successfully updated the session timeout settings."` |
| **session_inactivity_setting**  dictionary | Returned when session inactivity timeout settings are updated successfully.  **Returned:** success  **Sample:** `[{"MaxSessionTimeout": 86400000, "MaxSessions": 32, "MaxSessionsAllowed": 100, "MaxSessionsConfigurable": true, "MinSessionTimeout": 60000, "MinSessionsAllowed": 1, "SessionTimeout": 99600, "SessionTimeoutConfigurable": true, "SessionType": "API"}, {"MaxSessionTimeout": 7200000, "MaxSessions": 6, "MaxSessionsAllowed": 6, "MaxSessionsConfigurable": true, "MinSessionTimeout": 60000, "MinSessionsAllowed": 1, "SessionTimeout": 99600, "SessionTimeoutConfigurable": true, "SessionType": "GUI"}, {"MaxSessionTimeout": 10800000, "MaxSessions": 4, "MaxSessionsAllowed": 4, "MaxSessionsConfigurable": true, "MinSessionTimeout": 60000, "MinSessionsAllowed": 1, "SessionTimeout": 99600, "SessionTimeoutConfigurable": true, "SessionType": "SSH"}, {"MaxSessionTimeout": 86400000, "MaxSessions": 1, "MaxSessionsAllowed": 1, "MaxSessionsConfigurable": false, "MinSessionTimeout": 60000, "MinSessionsAllowed": 1, "SessionTimeout": 99600, "SessionTimeoutConfigurable": true, "SessionType": "Serial"}, {"MaxSessionTimeout": 86400000, "MaxSessions": 0, "MaxSessionsAllowed": 0, "MaxSessionsConfigurable": false, "MinSessionTimeout": -1, "MinSessionsAllowed": 0, "SessionTimeout": -1, "SessionTimeoutConfigurable": true, "SessionType": "UniversalTimeout"}]` |

### Authors

- Sachin Apagundi(@sachin-apa)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
