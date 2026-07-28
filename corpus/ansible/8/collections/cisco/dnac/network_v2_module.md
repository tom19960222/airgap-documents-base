---
collection: ansible
version: "8"
title: "cisco.dnac.network_v2 module – Resource module for Network V2"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/network_v2_module.html
fetched_at: 2026-07-28T01:23:44+00:00
---
# cisco.dnac.network_v2 module – Resource module for Network V2

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
> see [Requirements](network_v2_module.md#ansible-collections-cisco-dnac-network-v2-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.network_v2`.

New in cisco.dnac 6.7.0

- [Synopsis](network_v2_module.md#synopsis)
- [Requirements](network_v2_module.md#requirements)
- [Parameters](network_v2_module.md#parameters)
- [Notes](network_v2_module.md#notes)
- [See Also](network_v2_module.md#see-also)
- [Examples](network_v2_module.md#examples)
- [Return Values](network_v2_module.md#return-values)

## [Synopsis](network_v2_module.md#id1)

- Manage operations create and update of the resource Network V2.
- API to create network settings for DHCP, Syslog, SNMP, NTP, Network AAA, Client and Endpoint AAA, and/or DNS center server settings.
- API to update network settings for DHCP, Syslog, SNMP, NTP, Network AAA, Client and Endpoint AAA, and/or DNS center server settings.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](network_v2_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](network_v2_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **settings**  dictionary | Network V2’s settings. |
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
| **configureDnacIP**  boolean | Configuration DNAC IP for SNMP Server (eg true).  **Choices:**   - `false` - `true` |
| **ipAddresses**  list / elements=string | IP Address for SNMP Server (eg 4.4.4.1). |
| **syslogServer**  dictionary | Network V2’s syslogServer. |
| **configureDnacIP**  boolean | Configuration DNAC IP for syslog server (eg true).  **Choices:**   - `false` - `true` |
| **ipAddresses**  list / elements=string | IP Address for syslog server (eg 4.4.4.4). |
| **timezone**  string | Input for time zone (eg Africa/Abidjan). |
| **siteId**  string | SiteId path parameter. Site Id to which site details to associate with the network settings. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](network_v2_module.md#id4)

> **Note:**
>
> - SDK Method used are network_settings.NetworkSettings.create_network_v2, network_settings.NetworkSettings.update_network_v2,
> - Paths used are post /dna/intent/api/v2/network/{siteId}, put /dna/intent/api/v2/network/{siteId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](network_v2_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Network Settings CreateNetworkV2](https://developer.cisco.com/docs/dna-center/#!create-network-v-2)
> :   Complete reference of the CreateNetworkV2 API.
>
> [Cisco DNA Center documentation for Network Settings UpdateNetworkV2](https://developer.cisco.com/docs/dna-center/#!update-network-v-2)
> :   Complete reference of the UpdateNetworkV2 API.

## [Examples](network_v2_module.md#id6)

```yaml+jinja
- name: Create
  cisco.dnac.network_v2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    settings:
      clientAndEndpoint_aaa:
        ipAddress: string
        network: string
        protocol: string
        servers: string
        sharedSecret: string
      dhcpServer:
      - string
      dnsServer:
        domainName: string
        primaryIpAddress: string
        secondaryIpAddress: string
      messageOfTheday:
        bannerMessage: string
        retainExistingBanner: string
      netflowcollector:
        ipAddress: string
        port: 0
      network_aaa:
        ipAddress: string
        network: string
        protocol: string
        servers: string
        sharedSecret: string
      ntpServer:
      - string
      snmpServer:
        configureDnacIP: true
        ipAddresses:
        - string
      syslogServer:
        configureDnacIP: true
        ipAddresses:
        - string
      timezone: string
    siteId: string

- name: Update by id
  cisco.dnac.network_v2:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    settings:
      clientAndEndpoint_aaa:
        ipAddress: string
        network: string
        protocol: string
        servers: string
        sharedSecret: string
      dhcpServer:
      - string
      dnsServer:
        domainName: string
        primaryIpAddress: string
        secondaryIpAddress: string
      messageOfTheday:
        bannerMessage: string
        retainExistingBanner: string
      netflowcollector:
        ipAddress: string
        port: 0
      network_aaa:
        ipAddress: string
        network: string
        protocol: string
        servers: string
        sharedSecret: string
      ntpServer:
      - string
      snmpServer:
        configureDnacIP: true
        ipAddresses:
        - string
      syslogServer:
        configureDnacIP: true
        ipAddresses:
        - string
      timezone: string
    siteId: string
```

## [Return Values](network_v2_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"taskId": "string", "url": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
