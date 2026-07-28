---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.netapp_e_asup module – NetApp E-Series manage auto-support settings"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/netapp_e_asup_module.html
fetched_at: 2026-07-28T00:14:13+00:00
---
# netapp_eseries.santricity.netapp_e_asup module – NetApp E-Series manage auto-support settings

> **Note:**
>
> This module is part of the [netapp_eseries.santricity collection](https://galaxy.ansible.com/netapp_eseries/santricity) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp_eseries.santricity`.
>
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_asup`.

New in netapp_eseries.santricity 2.7

- [Synopsis](netapp_e_asup_module.md#synopsis)
- [Parameters](netapp_e_asup_module.md#parameters)
- [Notes](netapp_e_asup_module.md#notes)
- [Examples](netapp_e_asup_module.md#examples)
- [Return Values](netapp_e_asup_module.md#return-values)

## [Synopsis](netapp_e_asup_module.md#id1)

- Allow the auto-support settings to be configured for an individual E-Series storage-system

## [Parameters](netapp_e_asup_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **active**  boolean | Enable active/proactive monitoring for ASUP. When a problem is detected by our monitoring systems, it’s possible that the bundle did not contain all of the required information at the time of the event. Enabling this option allows NetApp support personnel to manually request transmission or re-transmission of support data in order ot resolve the problem.  Only applicable if *state=enabled*.  Choices:   - `false` - `true` ← (default) |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API. Example <https://prod-1.wahoo.acme.com/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **days**  aliases: days_of_week, schedule_days  list / elements=string | A list of days of the week that ASUP bundles will be sent. A larger, weekly bundle will be sent on one of the provided days.  Choices:   - `"monday"` - `"tuesday"` - `"wednesday"` - `"thursday"` - `"friday"` - `"saturday"` - `"sunday"` |
| **end**  aliases: end_time  integer | An end hour may be specified in a range from 1 to 24 hours.  ASUP bundles will be sent daily between the provided start and end time (UTC).  *start* must be less than *end*.  Default: `24` |
| **log_path**  string | A local path to a file to be used for debug logging |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **start**  aliases: start_time  integer | A start hour may be specified in a range from 0 to 23 hours.  ASUP bundles will be sent daily between the provided start and end time (UTC).  *start* must be less than *end*.  Default: `0` |
| **state**  aliases: asup, auto_support, autosupport  string | Enable/disable the E-Series auto-support configuration.  When this option is enabled, configuration, logs, and other support-related information will be relayed to NetApp to help better support your system. No personally identifiable information, passwords, etc, will be collected.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |
| **verbose**  boolean | Provide the full ASUP configuration in the return.  Choices:   - `false` ← (default) - `true` |

## [Notes](netapp_e_asup_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - Enabling ASUP will allow our support teams to monitor the logs of the storage-system in order to proactively respond to issues with the system. It is recommended that all ASUP-related options be enabled, but they may be disabled if desired.
> - This API is currently only supported with the Embedded Web Services API v2.0 and higher.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](netapp_e_asup_module.md#id4)

```yaml+jinja
- name: Enable ASUP and allow pro-active retrieval of bundles
  netapp_e_asup:
    state: enabled
    active: yes
    api_url: "10.1.1.1:8443"
    api_username: "admin"
    api_password: "myPass"

- name: Set the ASUP schedule to only send bundles from 12 AM CST to 3 AM CST.
  netapp_e_asup:
    start: 17
    end: 20
    api_url: "10.1.1.1:8443"
    api_username: "admin"
    api_password: "myPass"
```

## [Return Values](netapp_e_asup_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **active**  boolean | True if the active option has been enabled.  Returned: on success  Sample: `true` |
| **asup**  boolean | True if ASUP is enabled.  Returned: on success  Sample: `true` |
| **cfg**  complex | Provide the full ASUP configuration.  Returned: on success when *verbose=true*. |
| **asupEnabled**  boolean | True if ASUP has been enabled.  Returned: success |
| **daysOfWeek**  list / elements=string | The days of the week that ASUP bundles will be sent.  Returned: success |
| **onDemandEnabled**  boolean | True if ASUP active monitoring has been enabled.  Returned: success |
| **msg**  string | Success message  Returned: on success  Sample: `"The settings have been updated."` |

### Authors

- Michael Price (@lmprice)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
