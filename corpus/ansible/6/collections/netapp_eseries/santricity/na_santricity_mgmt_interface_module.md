---
collection: ansible
version: "6"
title: "netapp_eseries.santricity.na_santricity_mgmt_interface module – NetApp E-Series manage management interface configuration"
source_url: https://docs.ansible.com/projects/ansible/6/collections/netapp_eseries/santricity/na_santricity_mgmt_interface_module.html
fetched_at: 2026-07-28T00:14:03+00:00
---
# netapp_eseries.santricity.na_santricity_mgmt_interface module – NetApp E-Series manage management interface configuration

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
> To use it in a playbook, specify: `netapp_eseries.santricity.na_santricity_mgmt_interface`.

- [Synopsis](na_santricity_mgmt_interface_module.md#synopsis)
- [Parameters](na_santricity_mgmt_interface_module.md#parameters)
- [Notes](na_santricity_mgmt_interface_module.md#notes)
- [Examples](na_santricity_mgmt_interface_module.md#examples)
- [Return Values](na_santricity_mgmt_interface_module.md#return-values)

## [Synopsis](na_santricity_mgmt_interface_module.md#id1)

- Configure the E-Series management interfaces

## [Parameters](na_santricity_mgmt_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | The IPv4 address to assign to the interface.  Should be specified in xx.xx.xx.xx form.  Mutually exclusive with *config_method=dhcp* |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API.  Example <https://prod-1.wahoo.acme.com:8443/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **config_method**  string | The configuration method type to use for network interface ports.  dhcp is mutually exclusive with *address*, *subnet_mask*, and *gateway*.  Choices:   - `"dhcp"` - `"static"` |
| **controller**  string / required | The controller that owns the port you want to configure.  Controller names are represented alphabetically, with the first controller as A, the second as B, and so on.  Current hardware models have either 1 or 2 available controllers, but that is not a guaranteed hard limitation and could change in the future.  Choices:   - `"A"` - `"B"` |
| **dns_address**  string | Primary IPv4 or IPv6 DNS server address |
| **dns_address_backup**  string | Secondary IPv4 or IPv6 DNS server address |
| **dns_config_method**  string | The configuration method type to use for DNS services.  dhcp is mutually exclusive with *dns_address*, and *dns_address_backup*.  Choices:   - `"dhcp"` - `"static"` |
| **gateway**  string | The IPv4 gateway address to utilize for the interface.  Should be specified in xx.xx.xx.xx form.  Mutually exclusive with *config_method=dhcp* |
| **ntp_address**  string | Primary IPv4, IPv6, or FQDN NTP server address |
| **ntp_address_backup**  string | Secondary IPv4, IPv6, or FQDN NTP server address |
| **ntp_config_method**  string | The configuration method type to use for NTP services.  disable is mutually exclusive with *ntp_address* and *ntp_address_backup*.  dhcp is mutually exclusive with *ntp_address* and *ntp_address_backup*.  Choices:   - `"disabled"` - `"dhcp"` - `"static"` |
| **port**  integer / required | The ethernet port configuration to modify.  The channel represents the port number left to right on the controller, beginning with 1. |
| **ssh**  boolean | Enable ssh access to the controller for debug purposes.  This is a controller-level setting.  rlogin/telnet will be enabled for ancient equipment where ssh is not available.  Choices:   - `false` - `true` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  Default: `"1"` |
| **state**  string | Enable or disable IPv4 network interface configuration.  Either IPv4 or IPv6 must be enabled otherwise error will occur.  Choices:   - `"enabled"` ← (default) - `"disabled"` |
| **subnet_mask**  string | The subnet mask to utilize for the interface.  Should be specified in xx.xx.xx.xx form.  Mutually exclusive with *config_method=dhcp* |
| **validate_certs**  boolean | Should https certificates be validated?  Choices:   - `false` - `true` ← (default) |

## [Notes](na_santricity_mgmt_interface_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - It is highly recommended to have a minimum of one up management port on each controller.
> - When using SANtricity Web Services Proxy, use **ERROR while parsing**: While parsing M() at index 47: Module name “na_santricity_storage_system” is not a FQCN to update management paths. This is required because of a known issue and will be addressed in the proxy version 4.1. After the resolution the management ports should automatically be updated.
> - The interface settings are applied synchronously, but changes to the interface itself (receiving a new IP address via dhcp, etc), can take seconds or minutes longer to take effect.
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing M() at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](na_santricity_mgmt_interface_module.md#id4)

```yaml+jinja
- name: Configure the first port on the A controller with a static IPv4 address
  na_santricity_mgmt_interface:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    port: "1"
    controller: "A"
    config_method: static
    address: "192.168.1.100"
    subnet_mask: "255.255.255.0"
    gateway: "192.168.1.1"

- name: Disable ipv4 connectivity for the second port on the B controller
  na_santricity_mgmt_interface:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    port: "2"
    controller: "B"
    enable_interface: no

- name: Enable ssh access for ports one and two on controller A
  na_santricity_mgmt_interface:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    port: "1"
    controller: "A"
    ssh: yes

- name: Configure static DNS settings for the first port on controller A
  na_santricity_mgmt_interface:
    ssid: "1"
    api_url: "https://192.168.1.100:8443/devmgr/v2"
    api_username: "admin"
    api_password: "adminpass"
    validate_certs: true
    port: "1"
    controller: "A"
    dns_config_method: static
    dns_address: "192.168.1.100"
    dns_address_backup: "192.168.1.1"
```

## [Return Values](na_santricity_mgmt_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **available_embedded_api_urls**  list / elements=string | List containing available web services embedded REST API urls  Returned: on success |
| **msg**  string | Success message  Returned: on success  Sample: `"The interface settings have been updated."` |

### Authors

- Michael Price (@lmprice)
- Nathan Swartz (@ndswartz)

### Collection links

[Issue Tracker](https://github.com/netappeseries/santricity/issues)
[Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
