---
collection: ansible
version: "8"
title: "cisco.dnac.network_settings_intent module – Resource module for IP Address pools and network functions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/network_settings_intent_module.html
fetched_at: 2026-07-28T01:23:43+00:00
---
# cisco.dnac.network_settings_intent module – Resource module for IP Address pools and network functions

> **Note:**
>
> This module is part of the [cisco.dnac collection](https://galaxy.ansible.com/ui/repo/published/cisco/dnac/) (version 6.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.dnac`.
> You need further requirements to be able to use this module,
> see [Requirements](network_settings_intent_module.md#ansible-collections-cisco-dnac-network-settings-intent-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.network_settings_intent`.

New in cisco.dnac 6.6.0

- [Synopsis](network_settings_intent_module.md#synopsis)
- [Requirements](network_settings_intent_module.md#requirements)
- [Parameters](network_settings_intent_module.md#parameters)
- [Notes](network_settings_intent_module.md#notes)
- [Examples](network_settings_intent_module.md#examples)
- [Return Values](network_settings_intent_module.md#return-values)

## [Synopsis](network_settings_intent_module.md#id1)

- Manage operations on Global Pool, Reserve Pool, Network resources.
- API to create/update/delete global pool.
- API to reserve/update/delete an ip subpool from the global pool.
- API to update network settings for DHCP, Syslog, SNMP, NTP, Network AAA, Client and Endpoint AAA, and/or DNS center server settings.

## [Requirements](network_settings_intent_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk == 2.4.5
- python >= 3.5

## [Parameters](network_settings_intent_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **config**  list / elements=dictionary / required | List of details of global pool, reserved pool, network being managed. |
| **GlobalPoolDetails**  dictionary | Global ip pool manages IPv4 and IPv6 IP pools. |
| **settings**  dictionary | Global Pool’s settings. |
| **ippool**  list / elements=dictionary | Global Pool’s ippool. |
| **dhcpServerIps**  list / elements=string | Dhcp Server Ips. |
| **dnsServerIps**  list / elements=string | Dns Server Ips. |
| **gateway**  string | Gateway. |
| **IpAddressSpace**  string | Ip address space. |
| **ipPoolCidr**  string | Ip pool cidr. |
| **ipPoolName**  string | Ip Pool Name. |
| **prev_name**  string | previous name. |
| **NetworkManagementDetails**  dictionary | Set default network settings for the site |
| **settings**  dictionary | Network management details settings. |
| **clientAndEndpoint_aaa**  dictionary | Network V2’s clientAndEndpoint_aaa. |
| **ipAddress**  string | IP address for ISE serve (eg 1.1.1.4). |
| **network**  string | IP address for AAA or ISE server (eg 2.2.2.1). |
| **protocol**  string | Protocol for AAA or ISE serve (eg RADIUS). |
| **servers**  string | Server type AAA or ISE server (eg AAA). |
| **sharedSecret**  string | Shared secret for ISE server. |
| **dhcpServer**  list / elements=string | DHCP Server IP (eg 1.1.1.1). |
| **dnsServer**  dictionary | Network V2’s dnsServer. |
| **domainName**  string | Domain Name of DHCP (eg; cisco). |
| **primaryIpAddress**  string | Primary IP Address for DHCP (eg 2.2.2.2). |
| **secondaryIpAddress**  string | Secondary IP Address for DHCP (eg 3.3.3.3). |
| **messageOfTheday**  dictionary | Network V2’s messageOfTheday. |
| **bannerMessage**  string | Massage for Banner message (eg; Good day). |
| **retainExistingBanner**  string | Retain existing Banner Message (eg “true” or “false”). |
| **netflowcollector**  dictionary | Network V2’s netflowcollector. |
| **ipAddress**  string | IP Address for NetFlow collector (eg 3.3.3.1). |
| **port**  integer | Port for NetFlow Collector (eg; 443). |
| **network_aaa**  dictionary | Network V2’s network_aaa. |
| **ipAddress**  string | IP address for AAA and ISE server (eg 1.1.1.1). |
| **network**  string | IP Address for AAA or ISE server (eg 2.2.2.2). |
| **protocol**  string | Protocol for AAA or ISE serve (eg RADIUS). |
| **servers**  string | Server type for AAA Network (eg AAA). |
| **sharedSecret**  string | Shared secret for ISE Server. |
| **ntpServer**  list / elements=string | IP address for NTP server (eg 1.1.1.2). |
| **snmpServer**  dictionary | Network V2’s snmpServer. |
| **configureDnacIP**  boolean | Configuration Cisco DNA Center IP for SNMP Server (eg true).  **Choices:**   - `false` - `true` |
| **ipAddresses**  list / elements=string | IP Address for SNMP Server (eg 4.4.4.1). |
| **syslogServer**  dictionary | Network V2’s syslogServer. |
| **configureDnacIP**  boolean | Configuration Cisco DNA Center IP for syslog server (eg true).  **Choices:**   - `false` - `true` |
| **ipAddresses**  list / elements=string | IP Address for syslog server (eg 4.4.4.4). |
| **timezone**  string | Input for time zone (eg Africa/Abidjan). |
| **siteName**  string | Site name path parameter. |
| **ReservePoolDetails**  dictionary | Reserving IP subpool from the global pool |
| **ipv4DhcpServers**  list / elements=string | IPv4 input for dhcp server ip example 1.1.1.1. |
| **ipv4DnsServers**  list / elements=string | IPv4 input for dns server ip example 4.4.4.4. |
| **ipv4GateWay**  string  *added in cisco.dnac 4.0.0* | Gateway ip address details, example 175.175.0.1. |
| **ipv4GlobalPool**  string | IP v4 Global pool address with cidr, example 175.175.0.0/16. |
| **ipv4Prefix**  boolean | ip4 prefix length is enabled or ipv4 total Host input is enabled  **Choices:**   - `false` - `true` |
| **ipv4PrefixLength**  integer | The ipv4 prefix length is required when ipv4prefix value is true. |
| **ipv4Subnet**  string | IPv4 Subnet address, example 175.175.0.0. |
| **ipv4TotalHost**  integer | IPv4 total host is required when ipv4prefix value is false. |
| **ipv6AddressSpace**  boolean | If the value is false only ipv4 input are required, otherwise both ipv6 and ipv4 are required.  **Choices:**   - `false` - `true` |
| **ipv6DhcpServers**  list / elements=string | IPv6 format dhcp server as input example 2001 db8 1234. |
| **ipv6DnsServers**  list / elements=string | IPv6 format dns server input example 2001 db8 1234. |
| **ipv6GateWay**  string | Gateway ip address details, example 2001 db8 85a3 0 100 1. |
| **ipv6GlobalPool**  string | IPv6 Global pool address with cidr this is required when Ipv6AddressSpace value is true, example 2001 db8 85a3 /64. |
| **ipv6Prefix**  boolean | Ipv6 prefix value is true, the ip6 prefix length input field is enabled, if it is false ipv6 total Host input is enable.  **Choices:**   - `false` - `true` |
| **ipv6PrefixLength**  integer | IPv6 prefix length is required when the ipv6prefix value is true. |
| **ipv6Subnet**  string | IPv6 Subnet address, example 2001 db8 85a3 0 100. |
| **ipv6TotalHost**  integer | IPv6 total host is required when ipv6prefix value is false. |
| **name**  string | Name of the reserve ip sub pool. |
| **prev_name**  string | Previous name of the reserve ip sub pool. |
| **siteName**  string | Site name path parameter. Site name to reserve the ip sub pool. |
| **slaacSupport**  boolean | Slaac Support.  **Choices:**   - `false` - `true` |
| **type**  string | Type of the reserve ip sub pool. |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_log**  boolean | Flag for logging playbook execution details. If set to true the log file will be created at the location of the execution with the name dnac.log  **Choices:**   - `false` ← (default) - `true` |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  string | The Cisco DNA Center port.  **Default:** `"443"` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.2.3.3"` |
| **state**  string | The state of Cisco DNA Center after module completion.  **Choices:**   - `"merged"` ← (default) - `"deleted"` |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](network_settings_intent_module.md#id4)

> **Note:**
>
> - SDK Method used are network_settings.NetworkSettings.create_global_pool, network_settings.NetworkSettings.delete_global_ip_pool, network_settings.NetworkSettings.update_global_pool, network_settings.NetworkSettings.release_reserve_ip_subpool, network_settings.NetworkSettings.reserve_ip_subpool, network_settings.NetworkSettings.update_reserve_ip_subpool, network_settings.NetworkSettings.update_network_v2,
> - Paths used are post /dna/intent/api/v1/global-pool, delete /dna/intent/api/v1/global-pool/{id}, put /dna/intent/api/v1/global-pool, post /dna/intent/api/v1/reserve-ip-subpool/{siteId}, delete /dna/intent/api/v1/reserve-ip-subpool/{id}, put /dna/intent/api/v1/reserve-ip-subpool/{siteId}, put /dna/intent/api/v2/network/{siteId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [Examples](network_settings_intent_module.md#id5)

```yaml+jinja
- name: Create global pool, reserve an ip pool and network
  cisco.dnac.network_settings_intent:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    dnac_log: True
    state: merged
    config:
    - GlobalPoolDetails:
        settings:
          ippool:
          - ipPoolName: string
            gateway: string
            IpAddressSpace: string
            ipPoolCidr: string
            type: Generic
            dhcpServerIps: list
            dnsServerIps: list
      ReservePoolDetails:
        ipv6AddressSpace: True
        ipv4GlobalPool: string
        ipv4Prefix: True
        ipv4PrefixLength: 9
        ipv4Subnet: string
        name: string
        ipv6Prefix: True
        ipv6PrefixLength: 64
        ipv6GlobalPool: string
        ipv6Subnet: string
        siteName: string
        slaacSupport: True
        type: LAN
      NetworkManagementDetails:
        settings:
          dhcpServer: list
          dnsServer:
            domainName: string
            primaryIpAddress: string
            secondaryIpAddress: string
          clientAndEndpoint_aaa:
            network: string
            protocol: string
            servers: string
          messageOfTheday:
            bannerMessage: string
            retainExistingBanner: string
          netflowcollector:
            ipAddress: string
            port: 443
          network_aaa:
            network: string
            protocol: string
            servers: string
          ntpServer: list
          snmpServer:
            configureDnacIP: True
            ipAddresses: list
          syslogServer:
            configureDnacIP: True
            ipAddresses: list
        siteName: string
```

## [Return Values](network_settings_intent_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **response_1**  dictionary | A dictionary or list with the response returned by the Cisco DNA Center Python SDK  **Returned:** always  **Sample:** `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |
| **response_2**  dictionary | A dictionary or list with the response returned by the Cisco DNA Center Python SDK  **Returned:** always  **Sample:** `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |
| **response_3**  dictionary | A dictionary or list with the response returned by the Cisco DNA Center Python SDK  **Returned:** always  **Sample:** `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |

### Authors

- Muthu Rakesh (@MUTHU-RAKESH-27) Madhan Sankaranarayanan (@madhansansel)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
