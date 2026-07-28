---
collection: ansible
version: "8"
title: "dellemc.openmanage.ome_application_network_address module – Updates the network configuration on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/openmanage/ome_application_network_address_module.html
fetched_at: 2026-07-28T02:04:20+00:00
---
# dellemc.openmanage.ome_application_network_address module – Updates the network configuration on OpenManage Enterprise

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
> see [Requirements](ome_application_network_address_module.md#ansible-collections-dellemc-openmanage-ome-application-network-address-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_application_network_address`.

New in dellemc.openmanage 2.1.0

- [Synopsis](ome_application_network_address_module.md#synopsis)
- [Requirements](ome_application_network_address_module.md#requirements)
- [Parameters](ome_application_network_address_module.md#parameters)
- [Notes](ome_application_network_address_module.md#notes)
- [Examples](ome_application_network_address_module.md#examples)
- [Return Values](ome_application_network_address_module.md#return-values)

## [Synopsis](ome_application_network_address_module.md#id1)

- This module allows the configuration of a DNS and an IPV4 or IPV6 network on OpenManage Enterprise.

## [Requirements](ome_application_network_address_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_application_network_address_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  *added in dellemc.openmanage 5.0.0* | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **dns_configuration**  dictionary | Domain Name System(DNS) settings. |
| **dns_domain_name**  string | Static DNS domain name  This is applicable when *use_dhcp_for_dns_domain_name* is false. |
| **dns_name**  string | DNS name for *hostname*  This is applicable when *register_with_dns* is true. |
| **register_with_dns**  boolean | Register/Unregister *dns_name* on the DNS Server.  This option cannot be updated if vLAN configuration changes.  **Choices:**   - `false` - `true` |
| **use_dhcp_for_dns_domain_name**  boolean | Get the *dns_domain_name* using a DHCP server.  **Choices:**   - `false` - `true` |
| **enable_nic**  boolean | Enable or disable Network Interface Card (NIC) configuration.  **Choices:**   - `false` - `true` ← (default) |
| **hostname**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular IP address or hostname. |
| **interface_name**  string | If there are multiple interfaces, network configuration changes can be applied to a single interface using the interface name of the NIC.  If this option is not specified, Primary interface is chosen by default. |
| **ipv4_configuration**  dictionary | IPv4 network configuration.  *Warning* Ensure that you have an alternate interface to access OpenManage Enterprise as these options can change the current IPv4 address for *hostname*. |
| **enable**  boolean / required | Enable or disable access to the network using IPv4.  **Choices:**   - `false` - `true` |
| **enable_dhcp**  boolean | Enable or disable the automatic request to get an IPv4 address from the IPv4 Dynamic Host Configuration Protocol (DHCP) server  If *enable_dhcp* option is true, OpenManage Enterprise retrieves the IP configuration—IPv4 address, subnet mask, and gateway from a DHCP server on the existing network.  **Choices:**   - `false` - `true` |
| **static_alternate_dns_server**  string | Static IPv4 DNS alternate server  This option is applicable when *use_dhcp_for_dns_server_names* is false. |
| **static_gateway**  string | Static IPv4 gateway address  This option is applicable when *enable_dhcp* is false. |
| **static_ip_address**  string | Static IPv4 address  This option is applicable when *enable_dhcp* is false. |
| **static_preferred_dns_server**  string | Static IPv4 DNS preferred server  This option is applicable when *use_dhcp_for_dns_server_names* is false. |
| **static_subnet_mask**  string | Static IPv4 subnet mask address  This option is applicable when *enable_dhcp* is false. |
| **use_dhcp_for_dns_server_names**  boolean | This option allows to automatically request and obtain a DNS server IPv4 address from the DHCP server.  This option is applicable when *enable_dhcp* is true.  **Choices:**   - `false` - `true` |
| **ipv6_configuration**  dictionary | IPv6 network configuration.  *Warning* Ensure that you have an alternate interface to access OpenManage Enterprise as these options can change the current IPv6 address for *hostname*. |
| **enable**  boolean / required | Enable or disable access to the network using the IPv6.  **Choices:**   - `false` - `true` |
| **enable_auto_configuration**  boolean | Enable or disable the automatic request to get an IPv6 address from the IPv6 DHCP server or router advertisements(RA)  If *enable_auto_configuration* is true, OME retrieves IP configuration-IPv6 address, prefix, and gateway, from a DHCPv6 server on the existing network  **Choices:**   - `false` - `true` |
| **static_alternate_dns_server**  string | Static IPv6 DNS alternate server  This option is applicable when *use_dhcp_for_dns_server_names* is false. |
| **static_gateway**  string | Static IPv6 gateway address  This option is applicable when *enable_auto_configuration* is false. |
| **static_ip_address**  string | Static IPv6 address  This option is applicable when *enable_auto_configuration* is false. |
| **static_preferred_dns_server**  string | Static IPv6 DNS preferred server  This option is applicable when *use_dhcp_for_dns_server_names* is false. |
| **static_prefix_length**  integer | Static IPv6 prefix length  This option is applicable when *enable_auto_configuration* is false. |
| **use_dhcp_for_dns_server_names**  boolean | This option allows to automatically request and obtain a DNS server IPv6 address from the DHCP server.  This option is applicable when *enable_auto_configuration* is true  **Choices:**   - `false` - `true` |
| **management_vlan**  dictionary | vLAN configuration.  These settings are applicable for OpenManage Enterprise Modular. |
| **enable_vlan**  boolean / required | Enable or disable vLAN for management.  The vLAN configuration cannot be updated if the *register_with_dns* field under *dns_configuration* is true.  *WARNING* Ensure that the network cable is plugged to the correct port after the vLAN configuration changes have been made. If not, the configuration change may not be effective.  **Choices:**   - `false` - `true` |
| **vlan_id**  integer | vLAN ID.  This option is applicable when *enable_vlan* is true. |
| **password**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular password. |
| **port**  integer | OpenManage Enterprise or OpenManage Enterprise Modular HTTPS port.  **Default:** `443` |
| **reboot_delay**  integer | The time in seconds, after which settings are applied.  This option is not mandatory. |
| **timeout**  integer  *added in dellemc.openmanage 5.0.0* | The socket level timeout in seconds.  **Default:** `30` |
| **username**  string / required | OpenManage Enterprise or OpenManage Enterprise Modular username. |
| **validate_certs**  boolean  *added in dellemc.openmanage 5.0.0* | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](ome_application_network_address_module.md#id4)

> **Note:**
>
> - The configuration changes can only be applied to one interface at a time.
> - The system management consoles might be unreachable for some time after the configuration changes are applied.
> - This module supports `check_mode`.

## [Examples](ome_application_network_address_module.md#id5)

```yaml+jinja
---
- name: IPv4 network configuration for primary interface
  dellemc.openmanage.ome_application_network_address:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    enable_nic: true
    ipv4_configuration:
      enable: true
      enable_dhcp: false
      static_ip_address: 192.168.0.2
      static_subnet_mask: 255.255.254.0
      static_gateway: 192.168.0.3
      use_dhcp_for_dns_server_names: false
      static_preferred_dns_server: 192.168.0.4
      static_alternate_dns_server: 192.168.0.5
    reboot_delay: 5

- name: IPv6 network configuration for primary interface
  dellemc.openmanage.ome_application_network_address:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    ipv6_configuration:
      enable: true
      enable_auto_configuration: true
      static_ip_address: 2626:f2f2:f081:9:1c1c:f1f1:4747:1
      static_prefix_length: 10
      static_gateway: 2626:f2f2:f081:9:1c1c:f1f1:4747:2
      use_dhcp_for_dns_server_names: true
      static_preferred_dns_server: 2626:f2f2:f081:9:1c1c:f1f1:4747:3
      static_alternate_dns_server: 2626:f2f2:f081:9:1c1c:f1f1:4747:4

- name: Management vLAN configuration for primary interface
  dellemc.openmanage.ome_application_network_address:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    management_vlan:
      enable_vlan: true
      vlan_id: 3344
    dns_configuration:
      register_with_dns: false
    reboot_delay: 1

- name: DNS settings
  dellemc.openmanage.ome_application_network_address:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    ipv4_configuration:
      enable: true
      use_dhcp_for_dns_server_names: false
      static_preferred_dns_server: 192.168.0.4
      static_alternate_dns_server: 192.168.0.5
    dns_configuration:
      register_with_dns: true
      use_dhcp_for_dns_domain_name: false
      dns_name: "MX-SVCTAG"
      dns_domain_name: "dnslocaldomain"

- name: Disbale nic interface eth1
  dellemc.openmanage.ome_application_network_address:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    enable_nic: false
    interface_name: eth1

- name: Complete network settings for interface eth1
  dellemc.openmanage.ome_application_network_address:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    enable_nic: true
    interface_name: eth1
    ipv4_configuration:
      enable: true
      enable_dhcp: false
      static_ip_address: 192.168.0.2
      static_subnet_mask: 255.255.254.0
      static_gateway: 192.168.0.3
      use_dhcp_for_dns_server_names: false
      static_preferred_dns_server: 192.168.0.4
      static_alternate_dns_server: 192.168.0.5
    ipv6_configuration:
      enable: true
      enable_auto_configuration: true
      static_ip_address: 2626:f2f2:f081:9:1c1c:f1f1:4747:1
      static_prefix_length: 10
      static_gateway: ffff::2607:f2b1:f081:9
      use_dhcp_for_dns_server_names: true
      static_preferred_dns_server: 2626:f2f2:f081:9:1c1c:f1f1:4747:3
      static_alternate_dns_server: 2626:f2f2:f081:9:1c1c:f1f1:4747:4
    dns_configuration:
      register_with_dns: true
      use_dhcp_for_dns_domain_name: false
      dns_name: "MX-SVCTAG"
      dns_domain_name: "dnslocaldomain"
    reboot_delay: 5
```

## [Return Values](ome_application_network_address_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **error_info**  dictionary | Details of the HTTP error.  **Returned:** on HTTP error  **Sample:** `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to update the address configuration because a dependent field is missing for  Use DHCP for DNS Domain Name, Enable DHCP for ipv4 or Enable Autoconfig for ipv6 settings for valid configuration .", "MessageArgs": ["Use DHCP for DNS Domain Name, Enable DHCP for ipv4 or Enable Autoconfig for ipv6 settings for valid configuration"], "MessageId": "CAPP1304", "RelatedProperties": [], "Resolution": "Make sure that all dependent fields contain valid content and retry the operation.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **job_info**  dictionary | Details of the job to update in case OME version is >= 3.3.  **Returned:** on success  **Sample:** `{"Builtin": false, "CreatedBy": "system", "Editable": true, "EndTime": null, "Id": 14902, "JobDescription": "Generic OME runtime task", "JobName": "OMERealtime_Task", "JobStatus": {"Id": 2080, "Name": "New"}, "JobType": {"Id": 207, "Internal": true, "Name": "OMERealtime_Task"}, "LastRun": null, "LastRunStatus": {"Id": 2080, "Name": "New"}, "NextRun": null, "Params": [{"JobId": 14902, "Key": "Nmcli_Update", "Value": "{\"interfaceName\":\"eth0\",\"profileName\":\"eth0\",\"enableNIC\":true, \"ipv4Configuration\":{\"enable\":true,\"enableDHCP\":true,\"staticIPAddress\":\"\", \"staticSubnetMask\":\"\",\"staticGateway\":\"\",\"useDHCPForDNSServerNames\":true, \"staticPreferredDNSServer\":\"\",\"staticAlternateDNSServer\":\"\"}, \"ipv6Configuration\":{\"enable\":false,\"enableAutoConfiguration\":true,\"staticIPAddress\":\"\", \"staticPrefixLength\":0,\"staticGateway\":\"\",\"useDHCPForDNSServerNames\":false, \"staticPreferredDNSServer\":\"\",\"staticAlternateDNSServer\":\"\"}, \"managementVLAN\":{\"enableVLAN\":false,\"id\":0},\"dnsConfiguration\":{\"registerWithDNS\":false, \"dnsName\":\"\",\"useDHCPForDNSDomainName\":false,\"dnsDomainName\":\"\",\"fqdndomainName\":\"\", \"ipv4CurrentPreferredDNSServer\":\"\",\"ipv4CurrentAlternateDNSServer\":\"\", \"ipv6CurrentPreferredDNSServer\":\"\",\"ipv6CurrentAlternateDNSServer\":\"\"}, \"currentSettings\":{\"ipv4Address\":[],\"ipv4Gateway\":\"\",\"ipv4Dns\":[],\"ipv4Domain\":\"\", \"ipv6Address\":[],\"ipv6LinkLocalAddress\":\"\",\"ipv6Gateway\":\"\",\"ipv6Dns\":[], \"ipv6Domain\":\"\"},\"delay\":0,\"primaryInterface\":true,\"modifiedConfigs\":{}}"}], "Schedule": "startnow", "StartTime": null, "State": "Enabled", "Targets": [], "UpdatedBy": null, "Visible": true}` |
| **msg**  string | Overall status of the network address configuration change.  **Returned:** always  **Sample:** `"Successfully updated network address configuration"` |
| **network_configuration**  dictionary | Updated application network address configuration.  **Returned:** on success  **Sample:** `{"Delay": 0, "DnsConfiguration": {"DnsDomainName": "", "DnsName": "MX-SVCTAG", "RegisterWithDNS": false, "UseDHCPForDNSDomainName": true}, "EnableNIC": true, "InterfaceName": "eth0", "Ipv4Configuration": {"Enable": true, "EnableDHCP": false, "StaticAlternateDNSServer": "", "StaticGateway": "192.168.0.2", "StaticIPAddress": "192.168.0.3", "StaticPreferredDNSServer": "192.168.0.4", "StaticSubnetMask": "255.255.254.0", "UseDHCPForDNSServerNames": false}, "Ipv6Configuration": {"Enable": true, "EnableAutoConfiguration": true, "StaticAlternateDNSServer": "", "StaticGateway": "", "StaticIPAddress": "", "StaticPreferredDNSServer": "", "StaticPrefixLength": 0, "UseDHCPForDNSServerNames": true}, "ManagementVLAN": {"EnableVLAN": false, "Id": 1}, "PrimaryInterface": true}` |

### Authors

- Jagadeesh N V(@jagadeeshnv)

### Collection links

- [Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
- [Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
- [Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
