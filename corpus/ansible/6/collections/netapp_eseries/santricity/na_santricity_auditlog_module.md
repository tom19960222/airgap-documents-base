---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_auditlog module – NetApp E-Series manage audit-log configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_auditlog_module.html
fetched_at: 2026-07-28T00:13:53+00:00
---
# netapp_eseries.santricity.na_santricity_auditlog module – NetApp E-Series manage audit-log configuration

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
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_auditlog`.

- [Synopsis](na_santricity_auditlog_module.md#synopsis)
- [Parameters](na_santricity_auditlog_module.md#parameters)
- [Notes](na_santricity_auditlog_module.md#notes)
- [Examples](na_santricity_auditlog_module.md#examples)
- [Return Values](na_santricity_auditlog_module.md#return-values)

## [Synopsis](na_santricity_auditlog_module.md#id1)

- This module allows an e-series storage system owner to set audit-log configuration parameters.

## [Parameters](na_santricity_auditlog_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **force**  boolean | Forces the audit-log configuration to delete log history when log messages fullness cause immediate warning or full condition.  Warning! This will cause any existing audit-log messages to be deleted.  This is only applicable for *full_policy=preventSystemAccess*.  Choices:   - `false` ← (default) - `true` |
| **full_policy**  string | Specifies what audit-log should do once the number of entries approach the record limit.  Choices:   - `"overWrite"` ← (default) - `"preventSystemAccess"` |
| **log_level**  string | Filters the log messages according to the specified log level selection.  Choices:   - `"all"` - `"writeOnly"` ← (default) |
| **max_records**  integer | The maximum number log messages audit-log will retain.  Max records must be between and including 100 and 50000.  Default: `50000` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **threshold**  integer | This is the memory full percent threshold that audit-log will start issuing warning messages.  Percent range must be between and including 60 and 90.  Default: `90` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_santricity_auditlog_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - Use *ssid==”0”* or *ssid==”proxy”* to configure SANtricity Web Services Proxy auditlog settings otherwise.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_auditlog_module.md#id4)

```yaml+jinja
- name: Define audit-log to prevent system access if records exceed 50000 with warnings occurring at 60% capacity.
  na_santricity_auditlog:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    max_records: 50000
    log_level: all
    full_policy: preventSystemAccess
    threshold: 60
```

## [Return Values](na_santricity_auditlog_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: on success  Sample: `"The settings have been updated."` |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
