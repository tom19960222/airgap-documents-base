---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_auth module – NetApp E-Series set or update the password for a storage array device or SANtricity Web Services Proxy."
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_auth_module.html
fetched_at: 2026-07-28T00:13:53+00:00
---
# netapp_eseries.santricity.na_santricity_auth module – NetApp E-Series set or update the password for a storage array device or SANtricity Web Services Proxy.

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
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_auth`.

- [Synopsis](na_santricity_auth_module.md#synopsis)
- [Parameters](na_santricity_auth_module.md#parameters)
- [Notes](na_santricity_auth_module.md#notes)
- [Examples](na_santricity_auth_module.md#examples)
- [Return Values](na_santricity_auth_module.md#return-values)

## [Synopsis](na_santricity_auth_module.md#id1)

- Sets or updates the password for a storage array device or SANtricity Web Services Proxy.

## [Parameters](na_santricity_auth_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **current_admin_password**  string | The current admin password.  When making changes to the embedded web services’s login passwords, api_password will be used and current_admin_password will be ignored.  When making changes to the proxy web services’s login passwords, api_password will be used and current_admin_password will be ignored.  Only required when the password has been set and will be ignored if not set. |
| **minimum_password_length**  integer | This option defines the minimum password length. |
| **password**  string | The password you would like to set.  Cannot be more than 30 characters. |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **user**  string | The local user account password to update  For systems prior to E2800, use admin to change the rw (system password).  For systems prior to E2800, all choices except admin will be ignored.  Choices:   - `"admin"` ← (default) - `"monitor"` - `"support"` - `"security"` - `"storage"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_santricity_auth_module.md#id3)

> **Note:**
>
> - Set *ssid==”0”* or *ssid==”proxy”* when attempting to change the password for SANtricity Web Services Proxy.
> - SANtricity Web Services Proxy storage password will be updated when changing the password on a managed storage system from the proxy; This is only true when the storage system has been previously contacted.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_auth_module.md#id4)

```yaml+jinja
- name: Set the initial password
  na_santricity_auth:
    ssid: 1
    api_url: https://192.168.1.100:8443/devmgr/v2
    api_username: admin
    api_password: adminpass
    validate_certs: true
    current_admin_password: currentadminpass
    password: newpassword123
    user: admin
```

## [Return Values](na_santricity_auth_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: success  Sample: `"Password Updated Successfully"` |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
