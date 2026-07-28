---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_alerts_syslog module – NetApp E-Series manage syslog servers receiving storage system alerts."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_alerts_syslog_module.html
fetched_at: 2026-07-28T00:13:51+00:00
---
# netapp_eseries.santricity.na_santricity_alerts_syslog module – NetApp E-Series manage syslog servers receiving storage system alerts.

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
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_alerts_syslog`.

- [Synopsis](na_santricity_alerts_syslog_module.md#synopsis)
- [Parameters](na_santricity_alerts_syslog_module.md#parameters)
- [Notes](na_santricity_alerts_syslog_module.md#notes)
- [Examples](na_santricity_alerts_syslog_module.md#examples)
- [Return Values](na_santricity_alerts_syslog_module.md#return-values)

## [Synopsis](na_santricity_alerts_syslog_module.md#id1)

- Manage the list of syslog servers that will notifications on potentially critical events.

## [Parameters](na_santricity_alerts_syslog_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **servers**  list / elements=string | List of dictionaries where each dictionary contains a syslog server entry. |
| **address**  string / required | Syslog server address can be a fully qualified domain name, IPv4 address, or IPv6 address. |
| **port**  string | UDP Port must be a numerical value between 0 and 65535. Typically, the UDP Port for syslog is 514.  Default: `514` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **test**  boolean | This forces a test syslog message to be sent to the stated syslog server.  Test will only be issued when a change is made.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_santricity_alerts_syslog_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - This API is currently only supported with the Embedded Web Services API v2.12 (bundled with SANtricity OS 11.40.2) and higher.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_alerts_syslog_module.md#id4)

```yaml+jinja
- name: Add two syslog server configurations to NetApp E-Series storage array.
  na_santricity_alerts_syslog:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    servers:
        - address: "192.168.1.100"
        - address: "192.168.2.100"
          port: 514
        - address: "192.168.3.100"
          port: 1000
```

## [Return Values](na_santricity_alerts_syslog_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: on success  Sample: `"The settings have been updated."` |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
