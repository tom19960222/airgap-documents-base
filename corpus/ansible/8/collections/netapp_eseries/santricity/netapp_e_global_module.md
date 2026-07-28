---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.netapp_e_global module – NetApp E-Series manage global settings configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/netapp_e_global_module.html
fetched_at: 2026-07-28T02:44:31+00:00
---
# netapp_eseries.santricity.netapp_e_global module – NetApp E-Series manage global settings configuration

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
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_global`.

New in netapp_eseries.santricity 2.7

- [Synopsis](netapp_e_global_module.md#synopsis)
- [Parameters](netapp_e_global_module.md#parameters)
- [Notes](netapp_e_global_module.md#notes)
- [Examples](netapp_e_global_module.md#examples)
- [Return Values](netapp_e_global_module.md#return-values)

## [Synopsis](netapp_e_global_module.md#id1)

- Allow the user to configure several of the global settings associated with an E-Series storage-system

## [Parameters](netapp_e_global_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API. Example <https://prod-1.wahoo.acme.com/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **log_path**  string | A local path to a file to be used for debug logging |
| **name**  aliases: label  string | Set the name of the E-Series storage-system  This label/name doesn’t have to be unique.  May be up to 30 characters in length. |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  **Default:** `"1"` |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](netapp_e_global_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - This module requires Web Services API v1.3 or newer.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing “M(netapp_e_storage_system)” at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](netapp_e_global_module.md#id4)

```yaml+jinja
- name: Set the storage-system name
  netapp_e_global:
    name: myArrayName
    api_url: "10.1.1.1:8443"
    api_username: "admin"
    api_password: "myPass"
```

## [Return Values](netapp_e_global_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  **Returned:** on success  **Sample:** `"The settings have been updated."` |
| **name**  string | The current name/label of the storage-system.  **Returned:** on success  **Sample:** `"myArrayName"` |

### Authors

- Michael Price (@lmprice)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
