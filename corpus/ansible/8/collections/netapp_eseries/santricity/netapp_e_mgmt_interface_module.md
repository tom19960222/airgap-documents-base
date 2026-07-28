---
collection: ansible
version: "8"
title: "netapp_eseries.santricity.netapp_e_mgmt_interface module – NetApp E-Series management interface configuration"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp_eseries/santricity/netapp_e_mgmt_interface_module.html
fetched_at: 2026-07-28T02:44:36+00:00
---
# netapp_eseries.santricity.netapp_e_mgmt_interface module – NetApp E-Series management interface configuration

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
> To use it in a playbook, specify: `netapp_eseries.santricity.netapp_e_mgmt_interface`.

New in netapp_eseries.santricity 2.7

- [Synopsis](netapp_e_mgmt_interface_module.md#synopsis)
- [Parameters](netapp_e_mgmt_interface_module.md#parameters)
- [Notes](netapp_e_mgmt_interface_module.md#notes)
- [Examples](netapp_e_mgmt_interface_module.md#examples)
- [Return Values](netapp_e_mgmt_interface_module.md#return-values)

## [Synopsis](netapp_e_mgmt_interface_module.md#id1)

- Configure the E-Series management interfaces

## [Parameters](netapp_e_mgmt_interface_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **address**  string | The IPv4 address to assign to the interface.  Should be specified in xx.xx.xx.xx form.  Mutually exclusive with *config_method=dhcp* |
| **api_password**  string / required | The password to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **api_url**  string / required | The url to the SANtricity Web Services Proxy or Embedded Web Services API. Example <https://prod-1.wahoo.acme.com/devmgr/v2> |
| **api_username**  string / required | The username to authenticate with the SANtricity Web Services Proxy or Embedded Web Services API. |
| **channel**  integer | The port to modify the configuration for.  The channel represents the port number (typically from left to right on the controller), beginning with a value of 1.  Mutually exclusive with *name*. |
| **config_method**  string | The configuration method type to use for network interface ports.  dhcp is mutually exclusive with *address*, *subnet_mask*, and *gateway*.  **Choices:**   - `"dhcp"` - `"static"` |
| **controller**  string / required | The controller that owns the port you want to configure.  Controller names are represented alphabetically, with the first controller as A, the second as B, and so on.  Current hardware models have either 1 or 2 available controllers, but that is not a guaranteed hard limitation and could change in the future.  **Choices:**   - `"A"` - `"B"` |
| **dns_address**  string | Primary IPv4 DNS server address |
| **dns_address_backup**  string | Backup IPv4 DNS server address  Queried when primary DNS server fails |
| **dns_config_method**  string | The configuration method type to use for DNS services.  dhcp is mutually exclusive with *dns_address*, and *dns_address_backup*.  **Choices:**   - `"dhcp"` - `"static"` |
| **gateway**  string | The IPv4 gateway address to utilize for the interface.  Should be specified in xx.xx.xx.xx form.  Mutually exclusive with *config_method=dhcp* |
| **log_path**  string | A local path to a file to be used for debug logging |
| **name**  aliases: port, iface  string | The port to modify the configuration for.  The list of choices is not necessarily comprehensive. It depends on the number of ports that are present in the system.  The name represents the port number (typically from left to right on the controller), beginning with a value of 1.  Mutually exclusive with *channel*. |
| **ntp_address**  string | Primary IPv4 NTP server address |
| **ntp_address_backup**  string | Backup IPv4 NTP server address  Queried when primary NTP server fails |
| **ntp_config_method**  string | The configuration method type to use for NTP services.  disable is mutually exclusive with *ntp_address* and *ntp_address_backup*.  dhcp is mutually exclusive with *ntp_address* and *ntp_address_backup*.  **Choices:**   - `"disable"` - `"dhcp"` - `"static"` |
| **ssh**  boolean | Enable ssh access to the controller for debug purposes.  This is a controller-level setting.  rlogin/telnet will be enabled for ancient equipment where ssh is not available.  **Choices:**   - `false` - `true` |
| **ssid**  string | The ID of the array to manage. This value must be unique for each array.  **Default:** `"1"` |
| **state**  aliases: enable_interface  string | Enable or disable IPv4 network interface configuration.  Either IPv4 or IPv6 must be enabled otherwise error will occur.  Only required when enabling or disabling IPv4 network interface  **Choices:**   - `"enable"` - `"disable"` |
| **subnet_mask**  string | The subnet mask to utilize for the interface.  Should be specified in xx.xx.xx.xx form.  Mutually exclusive with *config_method=dhcp* |
| **validate_certs**  boolean | Should https certificates be validated?  **Choices:**   - `false` - `true` ← (default) |

## [Notes](netapp_e_mgmt_interface_module.md#id3)

> **Note:**
>
> - Check mode is supported.
> - The interface settings are applied synchronously, but changes to the interface itself (receiving a new IP address via dhcp, etc), can take seconds or minutes longer to take effect.
> - Known issue: Changes specifically to down ports will result in a failure. However, this may not be the case in up coming NetApp E-Series firmware releases (released after firmware version 11.40.2).
> - The E-Series Ansible modules require either an instance of the Web Services Proxy (WSP), to be available to manage the storage-system, or an E-Series storage-system that supports the Embedded Web Services API.
> - Embedded Web Services is currently available on the E2800, E5700, EF570, and newer hardware models.
> - **ERROR while parsing**: While parsing “M(netapp_e_storage_system)” at index 1: Module name “netapp_e_storage_system” is not a FQCN may be utilized for configuring the systems managed by a WSP instance.

## [Examples](netapp_e_mgmt_interface_module.md#id4)

```yaml+jinja
- name: Configure the first port on the A controller with a static IPv4 address
  netapp_e_mgmt_interface:
    channel: 1
    controller: "A"
    config_method: static
    address: "192.168.1.100"
    subnet_mask: "255.255.255.0"
    gateway: "192.168.1.1"
    ssid: "1"
    api_url: "10.1.1.1:8443"
    api_username: "admin"
    api_password: "myPass"

- name: Disable ipv4 connectivity for the second port on the B controller
  netapp_e_mgmt_interface:
    channel: 2
    controller: "B"
    enable_interface: no
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"

- name: Enable ssh access for ports one and two on controller A
  netapp_e_mgmt_interface:
    channel: "{{ item }}"
    controller: "A"
    ssh: yes
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
  loop:
    - 1
    - 2

- name: Configure static DNS settings for the first port on controller A
  netapp_e_mgmt_interface:
    channel: 1
    controller: "A"
    dns_config_method: static
    dns_address: "192.168.1.100"
    dns_address_backup: "192.168.1.1"
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"

- name: Configure static NTP settings for ports one and two on controller B
  netapp_e_mgmt_interface:
    channel: "{{ item }}"
    controller: "B"
    ntp_config_method: static
    ntp_address: "129.100.1.100"
    ntp_address_backup: "127.100.1.1"
    ssid: "{{ ssid }}"
    api_url: "{{ netapp_api_url }}"
    api_username: "{{ netapp_api_username }}"
    api_password: "{{ netapp_api_password }}"
  loop:
    - 1
    - 2
```

## [Return Values](netapp_e_mgmt_interface_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **enabled**  boolean | Indicates whether IPv4 connectivity has been enabled or disabled.  This does not necessarily indicate connectivity. If dhcp was enabled absent a dhcp server, for instance, it is unlikely that the configuration will actually be valid.  **Returned:** on success  **Sample:** `true` |
| **msg**  string | Success message  **Returned:** on success  **Sample:** `"The interface settings have been updated."` |

### Authors

- Michael Price (@lmprice)
- Nathan Swartz (@ndswartz)

### Collection links

- [Issue Tracker](https://github.com/netappeseries/santricity/issues)
- [Repository (Sources)](https://www.github.com/netapp-eseries/santricity)
