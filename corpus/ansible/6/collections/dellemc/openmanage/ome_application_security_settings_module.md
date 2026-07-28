---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_application_security_settings module – Configure the login security properties"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_application_security_settings_module.html
fetched_at: 2026-07-27T17:25:29+00:00
---
# dellemc.openmanage.ome_application_security_settings module – Configure the login security properties

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
> see [Requirements](ome_application_security_settings_module.md#ansible-collections-dellemc-openmanage-ome-application-security-settings-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_application_security_settings`.

New in dellemc.openmanage 4.4.0

- [Synopsis](ome_application_security_settings_module.md#synopsis)
- [Requirements](ome_application_security_settings_module.md#requirements)
- [Parameters](ome_application_security_settings_module.md#parameters)
- [Notes](ome_application_security_settings_module.md#notes)
- [Examples](ome_application_security_settings_module.md#examples)
- [Return Values](ome_application_security_settings_module.md#return-values)

## [Synopsis](ome_application_security_settings_module.md#id1)

- This module allows you to configure the login security properties on OpenManage Enterprise or OpenManage Enterprise Modular

## [Requirements](ome_application_security_settings_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_application_security_settings_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **fips_mode_enable**  boolean | The FIPS mode is intended to meet the requirements of FIPS 140-2 level 1. For more information refer to the FIPS user guide  This is applicable only for OpenManage Enterprise Modular only  This is mutually exclusive with *restrict_allowed_ip_range* and *login_lockout_policy*.  `WARNING` Enabling or Disabling this option resets your chassis to default settings. This may cause change in IP settings and loss of network connectivity.  `WARNING` The FIPS mode cannot be enabled on a lead chassis in a multi-chassis management configuration. To toggle enable FIPS on a lead chassis, delete the chassis group, enable FIPS and recreate the group.  `WARNING` For a Standalone or member chassis, enabling the FIPS mode deletes any fabrics created. This may cause loss of network connectivity and data paths to the compute sleds.  Choices:   - `false` - `true` |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **job_wait**  boolean | Provides an option to wait for job completion.  Choices:   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer | The maximum wait time of *job_wait* in seconds. The job is tracked only for this duration.  This option is applicable when *job_wait* is `True`.  Default: `120` |
| **login_lockout_policy**  dictionary | Locks the application after multiple unsuccessful login attempts.  This is mutually exclusive with *fips_mode_enable*. |
| **by_ip_address**  boolean | Enable or disable lockout policy settings based on the IP address. This restricts the number of unsuccessful login attempts from a specific IP address for a specific time interval.  Choices:   - `false` - `true` |
| **by_user_name**  boolean | Enable or disable lockout policy settings based on the user name. This restricts the number of unsuccessful login attempts from a specific user for a specific time interval.  Choices:   - `false` - `true` |
| **lockout_fail_count**  integer | The number of unsuccessful login attempts that are allowed after which the appliance prevents log in from the specific username or IP Address. |
| **lockout_fail_window**  integer | Lockout fail window is the time in seconds within which the lockout fail count event must occur to trigger the lockout penalty time. Enter the duration for which OpenManage Enterprise must display information about a failed attempt. |
| **lockout_penalty_time**  integer | The duration of time, in seconds, that login attempts from the specific user or IP address must not be allowed. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  Default: `443` |
| **restrict_allowed_ip_range**  dictionary | Restrict to allow inbound connections only from the specified IP address range.  This is mutually exclusive with *fips_mode_enable*.  `NOTE` When *restrict_allowed_ip_range* is configured on the appliance, any inbound connection to the appliance, such as alert reception, firmware update, and network identities are blocked from the devices that are outside the specified IP address range. However, any outbound connection from the appliance will work on all devices. |
| **enable_ip_range**  boolean / required | Allow connections based on the IP address range.  Choices:   - `false` - `true` |
| **ip_range**  string | The IP address range in Classless Inter-Domain Routing (CIDR) format. For example: 192.168.100.14/24 or 2001:db8::/24 |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_application_security_settings_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to DellEMC OpenManage Enterprise or OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_application_security_settings_module.md#id5)

```yaml+jinja
---
- name: Configure restricted allowed IP range
  dellemc.openmanage.ome_application_security_settings:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    restrict_allowed_ip_range:
      enable_ip_range: true
      ip_range: 192.1.2.3/24

- name: Configure login lockout policy
  dellemc.openmanage.ome_application_security_settings:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    login_lockout_policy:
      by_user_name: true
      by_ip_address: true
      lockout_fail_count: 3
      lockout_fail_window: 30
      lockout_penalty_time: 900

- name: Configure restricted allowed IP range and login lockout policy with job wait time out of 60 seconds
  dellemc.openmanage.ome_application_security_settings:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    restrict_allowed_ip_range:
      enable_ip_range: true
      ip_range: 192.1.2.3/24
    login_lockout_policy:
      by_user_name: true
      by_ip_address: true
      lockout_fail_count: 3
      lockout_fail_window: 30
      lockout_penalty_time: 900
    job_wait_timeout: 60

- name: Enable FIPS mode
  dellemc.openmanage.ome_application_security_settings:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    fips_mode_enable: yes
```

## [Return Values](ome_application_security_settings_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of http error.  Returned: on http error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because the domain information cannot be retrieved.", "MessageArgs": [], "MessageId": "CGEN8007", "RelatedProperties": [], "Resolution": "Verify the status of the database and domain configuration, and then retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **job_id**  integer | Job ID of the security configuration task.  Returned: When security configuration properties are provided  Sample: `10123` |
| **msg**  string | Overall status of the login security configuration.  Returned: always  Sample: `"Successfully applied the security settings."` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
