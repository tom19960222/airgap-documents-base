---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.na_santricity_asup module – NetApp E-Series manage auto-support settings"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/na_santricity_asup_module.html
fetched_at: 2026-07-28T02:44:04+00:00
---
# netapp_eseries.santricity.na_santricity_asup module – NetApp E-Series manage auto-support settings

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/ui/repo/published/netapp_eseries/santricity/) (version 1.4.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_asup`.

- [Synopsis](na_santricity_asup_module.md#synopsis)
- [Parameters](na_santricity_asup_module.md#parameters)
- [Notes](na_santricity_asup_module.md#notes)
- [Examples](na_santricity_asup_module.md#examples)
- [Return Values](na_santricity_asup_module.md#return-values)

## [Synopsis](na_santricity_asup_module.md#id1)

- Allow the auto-support settings to be configured for an individual E-Series storage-system

## [Parameters](na_santricity_asup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Enable active/proactive monitoring for ASUP. When a problem is detected by our monitoring systems, it’s possible that the bundle did not contain all of the required information at the time of the event. Enabling this option allows NetApp support personnel to manually request transmission or re-transmission of support data in order ot resolve the problem.  Only applicable if *state=enabled*.  **Choices:**   - `false` - `true` ← (default) |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **days**  aliases: schedule_days, days_of_week  list / elements=string | A list of days of the week that ASUP bundles will be sent. A larger, weekly bundle will be sent on one of the provided days.  **Choices:**   - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` - `"sunday"` |
| **email**  dictionary | Information particular to the e-mail delivery method.  Uses the SMTP protocol.  Required when **ERROR while parsing**: While parsing “M(method==email)” at index 15: Module name “method==email” is not a FQCN. |
| **sender**  string | Sender’s email account  Required when **ERROR while parsing**: While parsing “M(routing_type==email)” at index 15: Module name “routing_type==email” is not a FQCN. |
| **server**  string | Mail server’s IP address or fully qualified domain name.  Required when **ERROR while parsing**: While parsing “M(routing_type==email)” at index 15: Module name “routing_type==email” is not a FQCN. |
| **test_recipient**  string | Test verification email  Required when **ERROR while parsing**: While parsing “M(routing_type==email)” at index 15: Module name “routing_type==email” is not a FQCN. |
| **end**  integer | An end hour may be specified in a range from 1 to 24 hours.  ASUP bundles will be sent daily between the provided start and end time (UTC).  *start* must be less than *end*.  **Default:** `24` |
| **maintenance_duration**  integer | The duration of time the ASUP maintenance mode will be active.  Permittable range is between 1 and 72 hours.  Required when *state==maintenance_enabled*.  **Default:** `24` |
| **maintenance_emails**  list / elements=string | List of email addresses for maintenance notifications.  Required when *state==maintenance_enabled*. |
| **method**  string | AutoSupport dispatch delivery method.  **Choices:**   - `"https"` ← (default) - `"http"` - `"email"` |
| **proxy**  dictionary | Information particular to the proxy delivery method.  Required when **ERROR while parsing**: While parsing “M((method==https or method==http)” at index 15: Module name “(method==https or method==http” is not a FQCN and routing_type==proxy). |
| **host**  string | Proxy host IP address or fully qualified domain name.  Required when **ERROR while parsing**: While parsing “M(method==http or method==https)” at index 15: Module name “method==http or method==https” is not a FQCN and **ERROR while parsing**: While parsing “M(routing_type==proxy)” at index 52: Module name “routing_type==proxy” is not a FQCN. |
| **password**  string | Password for the proxy. |
| **port**  integer | Proxy host port.  Required when **ERROR while parsing**: While parsing “M(method==http or method==https)” at index 15: Module name “method==http or method==https” is not a FQCN and **ERROR while parsing**: While parsing “M(routing_type==proxy)” at index 52: Module name “routing_type==proxy” is not a FQCN. |
| **script**  string | Path to the AutoSupport routing script file.  Required when **ERROR while parsing**: While parsing “M(method==http or method==https)” at index 15: Module name “method==http or method==https” is not a FQCN and **ERROR while parsing**: While parsing “M(routing_type==script)” at index 52: Module name “routing_type==script” is not a FQCN. |
| **username**  string | Username for the proxy. |
| **routing_type**  string | AutoSupport routing  Required when **ERROR while parsing**: While parsing “M(method==https or method==http)” at index 15: Module name “method==https or method==http” is not a FQCN.  **Choices:**   - `"direct"` ← (default) - `"proxy"` - `"script"` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  **Default:** `"1"` |
| **start**  integer | A start hour may be specified in a range from 0 to 23 hours.  ASUP bundles will be sent daily between the provided start and end time (UTC).  *start* must be less than *end*.  **Default:** `0` |
| **state**  string | Enable/disable the E-Series auto-support configuration or maintenance mode.  When this option is enabled, configuration, logs, and other support-related information will be relayed to NetApp to help better support your system. No personally identifiable information, passwords, etc, will be collected.  The maintenance state enables the maintenance window which allows maintenance activities to be performed on the storage array without generating support cases.  Maintenance mode cannot be enabled unless ASUP has previously been enabled.  **Choices:**   - `"enabled"` ← (default) - `"disabled"` - `"maintenance_enabled"` - `"maintenance_disabled"` |
| **validate**  boolean | Validate ASUP configuration.  **Choices:**   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](na_santricity_asup_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - Enabling ASUP will allow our support teams to monitor the logs of the storage-system in order to proactively respond to issues with the system. It is recommended that all ASUP-related options be enabled, but they may be disabled if desired.
> - This API is currently only supported with the Embedded Web Services API v2.0 and higher.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing “M(netapp_e_storage_system)” at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_asup_module.md#id4)

```yaml+jinja
- name: Enable ASUP and allow pro-active retrieval of bundles
  na_santricity_asup:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    state: enabled
    active: true
    days: ["saturday", "sunday"]
    start: 17
    end: 20
- name: Set the ASUP schedule to only send bundles from 12 AM CST to 3 AM CST.
  na_santricity_asup:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    state: disabled
- name: Set the ASUP schedule to only send bundles from 12 AM CST to 3 AM CST.
  na_santricity_asup:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    state: maintenance_enabled
    maintenance_duration: 24
    maintenance_emails:
      - admin@example.com
- name: Set the ASUP schedule to only send bundles from 12 AM CST to 3 AM CST.
  na_santricity_asup:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    state: maintenance_disabled
```

## [Return Values](na_santricity_asup_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **active**  boolean | True if the active option has been enabled.  **Returned:** on success  **Sample:** `true` |
| **asup**  boolean | True if ASUP is enabled.  **Returned:** on success  **Sample:** `true` |
| **cfg**  complex | Provide the full ASUP configuration.  **Returned:** on success |
| **asupEnabled**  boolean | True if ASUP has been enabled.  **Returned:** success |
| **daysOfWeek**  list / elements=string | The days of the week that ASUP bundles will be sent.  **Returned:** success |
| **onDemandEnabled**  boolean | True if ASUP active monitoring has been enabled.  **Returned:** success |
| **msg**  string | Success message  **Returned:** on success  **Sample:** `"The settings have been updated."` |

### Authors

- Michael Price (@lmprice)
- Nathan Swartz (@ndswartz)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
