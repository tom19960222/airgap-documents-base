---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_device_mgmt_network module – Configure network settings of devices on OpenManage Enterprise Modular"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_device_mgmt_network_module.html
fetched_at: 2026-07-28T02:04:29+00:00
---
# dellemc.openmanage.ome_device_mgmt_network module – Configure network settings of devices on OpenManage Enterprise Modular

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/ui/repo/published/dellemc/openmanage/) (version 7.6.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_device_mgmt_network_module.md#ansible-collections-dellemc-openmanage-ome-device-mgmt-network-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_device_mgmt_network`.

New in dellemc.openmanage 4.2.0

- [Synopsis](ome_device_mgmt_network_module.md#synopsis)
- [Requirements](ome_device_mgmt_network_module.md#requirements)
- [Parameters](ome_device_mgmt_network_module.md#parameters)
- [Notes](ome_device_mgmt_network_module.md#notes)
- [Examples](ome_device_mgmt_network_module.md#examples)
- [Return Values](ome_device_mgmt_network_module.md#return-values)

## [Synopsis](ome_device_mgmt_network_module.md#id1)

- This module allows to configure network settings on Chassis, Servers, and I/O Modules on OpenManage Enterprise Modular.

## [Requirements](ome_device_mgmt_network_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_device_mgmt_network_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **delay**  integer | The time in seconds, after which settings are applied.  This option is applicable only for Chassis.  **Default:** `0` |
| **device_id**  integer | ID of the device.  This option is mutually exclusive with *device_service_tag*. |
| **device_service_tag**  string | Service tag of the device.  This option is mutually exclusive with *device_id*. |
| **dns_configuration**  dictionary | Domain Name System(DNS) settings. |
| **auto_negotiation**  boolean | Enables or disables the auto negation of the network speed.  `NOTE`: Setting *auto_negotiation* to false and choosing a network port speed may result in the chassis loosing link to the top of rack network switch, or to the neighboring chassis in case of MCM mode. It is recommended that the *auto_negotiation* is set to `true` for most use cases.  This is applicable when *use_dhcp_for_dns_domain_name* is false.  This is applicable only for Chassis.  **Choices:**   - `false` - `true` |
| **dns_domain_name**  string | Static DNS domain name  This is applicable when *use_dhcp_for_dns_domain_name* is false. |
| **dns_name**  string | DNS name for *hostname*  This is applicable when *register_with_dns* is true. |
| **network_speed**  string | The speed of the network port.  This is applicable when *auto_negotiation* is false.  `10_MB` to select network speed of 10 MB.  `100_MB` to select network speed of 100 MB.  This is applicable only for Chassis.  **Choices:**   - `"10_MB"` - `"100_MB"` |
| **register_with_dns**  boolean | Register/Unregister *dns_name* on the DNS Server.  `WARNING` This option cannot be updated if VLAN configuration changes.  **Choices:**   - `false` - `true` |
| **use_dhcp_for_dns_domain_name**  boolean | Get the *dns_domain_name* using a DHCP server.  **Choices:**   - `false` - `true` |
| **dns_server_settings**  dictionary | DNS server settings.  This is applicable only for I/O Module. |
| **alternate_dns_server1**  string | Enter the IP address of the first alternate DNS server. |
| **alternate_dns_server2**  string | Enter the IP address of the second alternate DNS server. |
| **preferred_dns_server**  string | Enter the IP address of the preferred DNS server. |
| **enable_nic**  boolean | Enable or disable Network Interface Card (NIC) configuration of the device.  This option is not applicable to I/O Module.  **Choices:**   - `false` - `true` ← (default) |
| **hostname**  string / required | OpenManage Enterprise Modular IP address or hostname. |
| **ipv4_configuration**  dictionary | IPv4 network configuration.  `WARNING` Ensure that you have an alternate interface to access OpenManage Enterprise Modular because these options can change the current IPv4 address for *hostname*. |
| **enable_dhcp**  boolean | Enable or disable the automatic request to obtain an IPv4 address from the IPv4 Dynamic Host Configuration Protocol (DHCP) server.  `NOTE` If this option is `True`, the values provided for *static_ip_address*, *static_subnet_mask*, and *static_gateway* are not applied for these fields. However, the module may report changes.  **Choices:**   - `false` - `true` |
| **enable_ipv4**  boolean / required | Enable or disable access to the network using IPv4.  **Choices:**   - `false` - `true` |
| **static_alternate_dns_server**  string | Static IPv4 DNS alternate server  This option is applicable when *use_dhcp_for_dns_server_names* is false. |
| **static_gateway**  string | Static IPv4 gateway address  This option is applicable when *enable_dhcp* is false. |
| **static_ip_address**  string | Static IPv4 address  This option is applicable when *enable_dhcp* is false. |
| **static_preferred_dns_server**  string | Static IPv4 DNS preferred server  This option is applicable when *use_dhcp_for_dns_server_names* is false. |
| **static_subnet_mask**  string | Static IPv4 subnet mask address  This option is applicable when *enable_dhcp* is false. |
| **use_dhcp_to_obtain_dns_server_address**  boolean | This option allows to automatically request and obtain IPv4 address for the DNS Server from the DHCP server.  This option is applicable when *enable_dhcp* is true.  `NOTE` If this option is `True`, the values provided for *static_preferred_dns_server* and *static_alternate_dns_server* are not applied for these fields. However, the module may report changes.  **Choices:**   - `false` - `true` |
| **ipv6_configuration**  dictionary | IPv6 network configuration.  `WARNING` Ensure that you have an alternate interface to access OpenManage Enterprise Modular because these options can change the current IPv6 address for *hostname*. |
| **enable_auto_configuration**  boolean | Enable or disable the automatic request to obtain an IPv6 address from the IPv6 DHCP server or router advertisements(RA)  If *enable_auto_configuration* is `true`, OpenManage Enterprise Modular retrieves IP configuration (IPv6 address, prefix, and gateway address) from a DHCPv6 server on the existing network.  `NOTE` If this option is `True`, the values provided for *static_ip_address*, *static_prefix_length*, and *static_gateway* are not applied for these fields. However, the module may report changes.  **Choices:**   - `false` - `true` |
| **enable_ipv6**  boolean / required | Enable or disable access to the network using the IPv6.  **Choices:**   - `false` - `true` |
| **static_alternate_dns_server**  string | Static IPv6 DNS alternate server  This option is applicable when *use_dhcp_for_dns_server_names* is false. |
| **static_gateway**  string | Static IPv6 gateway address  This option is applicable when *enable_auto_configuration* is false. |
| **static_ip_address**  string | Static IPv6 address  This option is applicable when *enable_auto_configuration* is false. |
| **static_preferred_dns_server**  string | Static IPv6 DNS preferred server  This option is applicable when *use_dhcp_for_dns_server_names* is false. |
| **static_prefix_length**  integer | Static IPv6 prefix length  This option is applicable when *enable_auto_configuration* is false. |
| **use_dhcpv6_to_obtain_dns_server_address**  boolean | This option allows to automatically request and obtain a IPv6 address for the DNS server from the DHCP server.  This option is applicable when *enable_auto_configuration* is true  `NOTE` If this option is `True`, the values provided for *static_preferred_dns_server* and *static_alternate_dns_server* are not applied for these fields. However, the module may report changes.  **Choices:**   - `false` - `true` |
| **management_vlan**  dictionary | VLAN configuration. |
| **enable_vlan**  boolean / required | Enable or disable VLAN for management.  The VLAN configuration cannot be updated if the *register_with_dns* field under *dns_configuration* is true.  `WARNING` Ensure that the network cable is connected to the correct port after the VLAN configuration is changed. If not, the VLAN configuration changes may not be applied.  **Choices:**   - `false` - `true` |
| **vlan_id**  integer | VLAN ID.  The valid VLAN IDs are: 1 to 4000, and 4021 to 4094.  This option is applicable when *enable_vlan* is true. |
| **password**  string / required | OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_device_mgmt_network_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell OpenManage Enterprise Modular.
> - This module supports `check_mode`.

## [Examples](ome_device_mgmt_network_module.md#id5)

```yaml+jinja
---
- name: Network settings for chassis
  dellemc.openmanage.ome_device_mgmt_network:
    hostname: 192.168.0.1
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tag: CHAS123
    ipv4_configuration:
      enable_ipv4: true
      enable_dhcp: false
      static_ip_address: 192.168.0.2
      static_subnet_mask: 255.255.254.0
      static_gateway: 192.168.0.3
      use_dhcp_to_obtain_dns_server_address: false
      static_preferred_dns_server: 192.168.0.4
      static_alternate_dns_server: 192.168.0.5
    ipv6_configuration:
      enable_ipv6: true
      enable_auto_configuration: false
      static_ip_address: 2626:f2f2:f081:9:1c1c:f1f1:4747:1
      static_prefix_length: 10
      static_gateway: ffff::2607:f2b1:f081:9
      use_dhcpv6_to_obtain_dns_server_address: false
      static_preferred_dns_server: 2626:f2f2:f081:9:1c1c:f1f1:4747:3
      static_alternate_dns_server: 2626:f2f2:f081:9:1c1c:f1f1:4747:4
    dns_configuration:
      register_with_dns: true
      use_dhcp_for_dns_domain_name: false
      dns_name: "MX-SVCTAG"
      dns_domain_name: "dnslocaldomain"
      auto_negotiation: no
      network_speed: 100_MB

- name: Network settings for server
  dellemc.openmanage.ome_device_mgmt_network:
    hostname: 192.168.0.1
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tag: SRVR123
    ipv4_configuration:
      enable_ipv4: true
      enable_dhcp: false
      static_ip_address: 192.168.0.2
      static_subnet_mask: 255.255.254.0
      static_gateway: 192.168.0.3
      use_dhcp_to_obtain_dns_server_address: false
      static_preferred_dns_server: 192.168.0.4
      static_alternate_dns_server: 192.168.0.5
    ipv6_configuration:
      enable_ipv6: true
      enable_auto_configuration: false
      static_ip_address: 2626:f2f2:f081:9:1c1c:f1f1:4747:1
      static_prefix_length: 10
      static_gateway: ffff::2607:f2b1:f081:9
      use_dhcpv6_to_obtain_dns_server_address: false
      static_preferred_dns_server: 2626:f2f2:f081:9:1c1c:f1f1:4747:3
      static_alternate_dns_server: 2626:f2f2:f081:9:1c1c:f1f1:4747:4

- name: Network settings for I/O module
  dellemc.openmanage.ome_device_mgmt_network:
    hostname: 192.168.0.1
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_service_tag: IOM1234
    ipv4_configuration:
      enable_ipv4: true
      enable_dhcp: false
      static_ip_address: 192.168.0.2
      static_subnet_mask: 255.255.254.0
      static_gateway: 192.168.0.3
    ipv6_configuration:
      enable_ipv6: true
      enable_auto_configuration: false
      static_ip_address: 2626:f2f2:f081:9:1c1c:f1f1:4747:1
      static_prefix_length: 10
      static_gateway: ffff::2607:f2b1:f081:9
    dns_server_settings:
      preferred_dns_server: 192.168.0.4
      alternate_dns_server1: 192.168.0.5

- name: Management VLAN configuration of chassis using device id
  dellemc.openmanage.ome_device_mgmt_network:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    device_id : 12345
    management_vlan:
      enable_vlan: true
      vlan_id: 2345
    dns_configuration:
      register_with_dns: false
```

## [Return Values](ome_device_mgmt_network_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP Error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to complete the request because IPV4 Settings Capability is not Supported does not exist or is not applicable for the resource URI.", "MessageArgs": ["IPV4 Settings Capability is not Supported"], "MessageId": "CGEN1004", "RelatedProperties": [], "Resolution": "Check the request resource URI. Refer to the OpenManage Enterprise-Modular User's Guide for more information about resource URI and its properties.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the network config operation.  **Returned:** always  **Sample:** `"Successfully applied the network settings."` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
