---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.netapp_e_auditlog module – NetApp E-Series manage audit-log configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/netapp_e_auditlog_module.html
fetched_at: 2026-07-28T00:14:13+00:00
---
# netapp_eseries.santricity.netapp_e_auditlog module – NetApp E-Series manage audit-log configuration

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
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_auditlog`.

New in netapp_eseries.santricity 2.7

- [Synopsis](netapp_e_auditlog_module.md#synopsis)
- [Parameters](netapp_e_auditlog_module.md#parameters)
- [Notes](netapp_e_auditlog_module.md#notes)
- [Examples](netapp_e_auditlog_module.md#examples)
- [Return Values](netapp_e_auditlog_module.md#return-values)

## [Synopsis](netapp_e_auditlog_module.md#id1)

- This module allows an e-series storage system owner to set audit-log configuration parameters.

## [Parameters](netapp_e_auditlog_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API. Example <https://prod-1.wahoo.acme.com/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **force**  boolean | Forces the audit-log configuration to delete log history when log messages fullness cause immediate warning or full condition.  Warning! This will cause any existing audit-log messages to be deleted.  This is only applicable for *full_policy=preventSystemAccess*.  Choices:   - `false` ← (default) - `true` |
| **full_policy**  string | Specifies what audit-log should do once the number of entries approach the record limit.  Choices:   - `"overWrite"` ← (default) - `"preventSystemAccess"` |
| **log_level**  string | Filters the log messages according to the specified log level selection.  Choices:   - `"all"` - `"writeOnly"` ← (default) |
| **log_path**  string | A local path to a file to be used for debug logging. |
| **max_records**  integer | The maximum number log messages audit-log will retain.  Max records must be between and including 100 and 50000.  Default: `50000` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **threshold**  integer | This is the memory full percent threshold that audit-log will start issuing warning messages.  Percent range must be between and including 60 and 90.  Default: `90` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](netapp_e_auditlog_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - This module is currently only supported with the Embedded Web Services API v3.0 and higher.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](netapp_e_auditlog_module.md#id4)

```yaml+jinja
- name: Define audit-log to prevent system access if records exceed 50000 with warnings occurring at 60% capacity.
  netapp_e_auditlog:
     api_url: "https://{{ netapp_e_api_host }}/devmgr/v2"
     api_username: "{{ netapp_e_api_username }}"
     api_password: "{{ netapp_e_api_password }}"
     ssid: "{{ netapp_e_ssid }}"
     validate_certs: no
     max_records: 50000
     log_level: all
     full_policy: preventSystemAccess
     threshold: 60
     log_path: /path/to/log_file.log
- name: Define audit-log utilize the default values.
  netapp_e_auditlog:
     api_url: "https://{{ netapp_e_api_host }}/devmgr/v2"
     api_username: "{{ netapp_e_api_username }}"
     api_password: "{{ netapp_e_api_password }}"
     ssid: "{{ netapp_e_ssid }}"
- name: Force audit-log configuration when full or warning conditions occur while enacting preventSystemAccess policy.
  netapp_e_auditlog:
     api_url: "https://{{ netapp_e_api_host }}/devmgr/v2"
     api_username: "{{ netapp_e_api_username }}"
     api_password: "{{ netapp_e_api_password }}"
     ssid: "{{ netapp_e_ssid }}"
     max_records: 5000
     log_level: all
     full_policy: preventSystemAccess
     threshold: 60
     force: yes
```

## [Return Values](netapp_e_auditlog_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: on success  Sample: `"The settings have been updated."` |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
