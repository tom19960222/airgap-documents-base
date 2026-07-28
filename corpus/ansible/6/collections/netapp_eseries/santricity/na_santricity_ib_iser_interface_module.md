---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_ib_iser_interface module – NetApp E-Series manage InfiniBand iSER interface configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_ib_iser_interface_module.html
fetched_at: 2026-07-28T00:13:59+00:00
---
# netapp_eseries.santricity.na_santricity_ib_iser_interface module – NetApp E-Series manage InfiniBand iSER interface configuration

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
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_ib_iser_interface`.

- [Synopsis](na_santricity_ib_iser_interface_module.md#synopsis)
- [Parameters](na_santricity_ib_iser_interface_module.md#parameters)
- [Notes](na_santricity_ib_iser_interface_module.md#notes)
- [Examples](na_santricity_ib_iser_interface_module.md#examples)
- [Return Values](na_santricity_ib_iser_interface_module.md#return-values)

## [Synopsis](na_santricity_ib_iser_interface_module.md#id1)

- Configure settings of an E-Series InfiniBand iSER interface IPv4 address configuration.

## [Parameters](na_santricity_ib_iser_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string / required | The IPv4 address to assign to the interface.  Should be specified in xx.xx.xx.xx form. |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **channel**  integer / required | The InfiniBand HCA port you wish to modify.  Ports start left to right and start with 1. |
| **controller**  string / required | The controller that owns the port you want to configure.  Controller names are presented alphabetically, with the first controller as A, the second as B, and so on.  Current hardware models have either 1 or 2 available controllers, but that is not a guaranteed hard limitation and could change in the future.  Choices:   - `"A"` - `"B"` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_santricity_ib_iser_interface_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_ib_iser_interface_module.md#id4)

```yaml+jinja
- name: Configure the first port on the A controller with a static IPv4 address
  na_santricity_ib_iser_interface:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    controller: "A"
    channel: "1"
    address: "192.168.1.100"
```

## [Return Values](na_santricity_ib_iser_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **enabled**  boolean | Indicates whether IPv4 connectivity has been enabled or disabled.  This does not necessarily indicate connectivity. If dhcp was enabled without a dhcp server, for instance, it is unlikely that the configuration will actually be valid.  Returned: on success  Sample: `true` |
| **msg**  string | Success message  Returned: on success  Sample: `"The interface settings have been updated."` |

### Authors

- Michael Price (@lmprice)
- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
