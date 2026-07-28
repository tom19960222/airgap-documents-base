---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_nvme_interface module – NetApp E-Series manage NVMe interface configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_nvme_interface_module.html
fetched_at: 2026-07-28T00:14:03+00:00
---
# netapp_eseries.santricity.na_santricity_nvme_interface module – NetApp E-Series manage NVMe interface configuration

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
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_nvme_interface`.

- [Synopsis](na_santricity_nvme_interface_module.md#synopsis)
- [Parameters](na_santricity_nvme_interface_module.md#parameters)
- [Notes](na_santricity_nvme_interface_module.md#notes)
- [Examples](na_santricity_nvme_interface_module.md#examples)
- [Return Values](na_santricity_nvme_interface_module.md#return-values)

## [Synopsis](na_santricity_nvme_interface_module.md#id1)

- Configure settings of an E-Series NVMe interface

## [Parameters](na_santricity_nvme_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | The IPv4 address to assign to the NVMe interface |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **channel**  integer | This option specifies the which NVMe controller channel to configure.  The list of choices is not necessarily comprehensive. It depends on the number of ports that are available in the system.  The numerical value represents the number of the channel (typically from left to right on the HIC), beginning with a value of 1. |
| **config_method**  string | The configuration method type to use for this interface.  Only applicable when configuring RoCE  dhcp is mutually exclusive with *address*, *subnet_mask*, and *gateway*.  Choices:   - `"dhcp"` ← (default) - `"static"` |
| **controller**  string | The controller that owns the port you want to configure.  Controller names are presented alphabetically, with the first controller as A and the second as B.  Choices:   - `"A"` - `"B"` |
| **gateway**  string | The IPv4 gateway address to utilize for the interface.  Only applicable when configuring RoCE  Mutually exclusive with *config_method=dhcp* |
| **mtu**  aliases: max_frame_size  integer | The maximum transmission units (MTU), in bytes.  Only applicable when configuring RoCE  This allows you to configure a larger value for the MTU, in order to enable jumbo frames (any value > 1500).  Generally, it is necessary to have your host, switches, and other components not only support jumbo frames, but also have it configured properly. Therefore, unless you know what you’re doing, it’s best to leave this at the default.  Default: `1500` |
| **speed**  string | This is the ethernet port speed measured in Gb/s.  Value must be a supported speed or auto for automatically negotiating the speed with the port.  Only applicable when configuring RoCE  The configured ethernet port speed should match the speed capability of the SFP on the selected port.  Default: `"auto"` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **state**  string | Whether or not the specified RoCE interface should be enabled.  Only applicable when configuring RoCE  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **subnet_mask**  string | The subnet mask to utilize for the interface.  Only applicable when configuring RoCE  Mutually exclusive with *config_method=dhcp* |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_santricity_nvme_interface_module.md#id3)

> **Note:**
>
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_nvme_interface_module.md#id4)

```yaml+jinja

```

## [Return Values](na_santricity_nvme_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | Success message  Returned: on success  Sample: `"The interface settings have been updated."` |

### Authors

- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
