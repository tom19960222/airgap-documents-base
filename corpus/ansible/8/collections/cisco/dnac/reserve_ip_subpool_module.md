---
collection: ansible
version: "8"
title: "cisco.dnac.reserve_ip_subpool module – Resource module for Reserve Ip Subpool"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/dnac/reserve_ip_subpool_module.html
fetched_at: 2026-07-28T01:24:19+00:00
---
# cisco.dnac.reserve_ip_subpool module – Resource module for Reserve Ip Subpool

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
> see [Requirements](reserve_ip_subpool_module.md#ansible-collections-cisco-dnac-reserve-ip-subpool-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.dnac.reserve_ip_subpool`.

New in cisco.dnac 3.1.0

- [Synopsis](reserve_ip_subpool_module.md#synopsis)
- [Requirements](reserve_ip_subpool_module.md#requirements)
- [Parameters](reserve_ip_subpool_module.md#parameters)
- [Notes](reserve_ip_subpool_module.md#notes)
- [See Also](reserve_ip_subpool_module.md#see-also)
- [Examples](reserve_ip_subpool_module.md#examples)
- [Return Values](reserve_ip_subpool_module.md#return-values)

## [Synopsis](reserve_ip_subpool_module.md#id1)

- Manage operations create, update and delete of the resource Reserve Ip Subpool.
- API to reserve an ip subpool from the global pool.
- API to delete the reserved ip subpool.
- API to update ip subpool from the global pool.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](reserve_ip_subpool_module.md#id2)

The below requirements are needed on the host that executes this module.

- dnacentersdk >= 2.5.5
- python >= 3.5

## [Parameters](reserve_ip_subpool_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **dnac_debug**  boolean | Flag for Cisco DNA Center SDK to enable debugging.  **Choices:**   - `false` ← (default) - `true` |
| **dnac_host**  string / required | The Cisco DNA Center hostname. |
| **dnac_password**  string | The Cisco DNA Center password to authenticate. |
| **dnac_port**  integer | The Cisco DNA Center port.  **Default:** `443` |
| **dnac_username**  aliases: user  string | The Cisco DNA Center username to authenticate.  **Default:** `"admin"` |
| **dnac_verify**  boolean | Flag to enable or disable SSL certificate verification.  **Choices:**   - `false` - `true` ← (default) |
| **dnac_version**  string | Informs the SDK which version of Cisco DNA Center to use.  **Default:** `"2.3.5.3"` |
| **id**  string | Id path parameter. Id of reserve ip subpool to be deleted. |
| **ipv4DhcpServers**  list / elements=string | IPv4 input for dhcp server ip example 1.1.1.1. |
| **ipv4DnsServers**  list / elements=string | IPv4 input for dns server ip example 4.4.4.4. |
| **ipv4GateWay**  string  *added in cisco.dnac 4.0.0* | Gateway ip address details, example 175.175.0.1. |
| **ipv4GlobalPool**  string | IP v4 Global pool address with cidr, example 175.175.0.0/16. |
| **ipv4Prefix**  boolean | IPv4 prefix value is true, the ip4 prefix length input field is enabled , if it is false ipv4 total Host input is enable.  **Choices:**   - `false` - `true` |
| **ipv4PrefixLength**  integer | The ipv4 prefix length is required when ipv4prefix value is true. |
| **ipv4Subnet**  string | IPv4 Subnet address, example 175.175.0.0. |
| **ipv4TotalHost**  integer | IPv4 total host is required when ipv4prefix value is false. |
| **ipv6AddressSpace**  boolean | If the value is false only ipv4 input are required, otherwise both ipv6 and ipv4 are required.  **Choices:**   - `false` - `true` |
| **ipv6DhcpServers**  list / elements=string | IPv6 format dhcp server as input example 2001 db8 1234. |
| **ipv6DnsServers**  list / elements=string | IPv6 format dns server input example 2001 db8 1234. |
| **ipv6GateWay**  string | Gateway ip address details, example 2001 db8 85a3 0 100 1. |
| **ipv6GlobalPool**  string | IPv6 Global pool address with cidr this is required when Ipv6AddressSpace value is true, example 2001 db8 85a3 /64. |
| **ipv6Prefix**  boolean | Ipv6 prefix value is true, the ip6 prefix length input field is enabled , if it is false ipv6 total Host input is enable.  **Choices:**   - `false` - `true` |
| **ipv6PrefixLength**  integer | IPv6 prefix length is required when the ipv6prefix value is true. |
| **ipv6Subnet**  string | IPv6 Subnet address, example 2001 db8 85a3 0 100. |
| **ipv6TotalHost**  integer | IPv6 total host is required when ipv6prefix value is false. |
| **name**  string | Name of the reserve ip sub pool. |
| **siteId**  string | SiteId path parameter. Site id to reserve the ip sub pool. |
| **slaacSupport**  boolean | Slaac Support.  **Choices:**   - `false` - `true` |
| **type**  string | Type of the reserve ip sub pool. |
| **validate_response_schema**  boolean | Flag for Cisco DNA Center SDK to enable the validation of request bodies against a JSON schema.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](reserve_ip_subpool_module.md#id4)

> **Note:**
>
> - SDK Method used are network_settings.NetworkSettings.release_reserve_ip_subpool, network_settings.NetworkSettings.reserve_ip_subpool, network_settings.NetworkSettings.update_reserve_ip_subpool,
> - Paths used are post /dna/intent/api/v1/reserve-ip-subpool/{siteId}, delete /dna/intent/api/v1/reserve-ip-subpool/{id}, put /dna/intent/api/v1/reserve-ip-subpool/{siteId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](reserve_ip_subpool_module.md#id5)

> **See also:**
>
> [Cisco DNA Center documentation for Network Settings ReserveIPSubpool](https://developer.cisco.com/docs/dna-center/#!reserve-ip-subpool)
> :   Complete reference of the ReserveIPSubpool API.
>
> [Cisco DNA Center documentation for Network Settings ReleaseReserveIPSubpool](https://developer.cisco.com/docs/dna-center/#!release-reserve-ip-subpool)
> :   Complete reference of the ReleaseReserveIPSubpool API.
>
> [Cisco DNA Center documentation for Network Settings UpdateReserveIPSubpool](https://developer.cisco.com/docs/dna-center/#!update-reserve-ip-subpool)
> :   Complete reference of the UpdateReserveIPSubpool API.

## [Examples](reserve_ip_subpool_module.md#id6)

```yaml+jinja
- name: Delete by id
  cisco.dnac.reserve_ip_subpool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string

- name: Create
  cisco.dnac.reserve_ip_subpool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    ipv4DhcpServers:
    - string
    ipv4DnsServers:
    - string
    ipv4GateWay: string
    ipv4GlobalPool: string
    ipv4Prefix: true
    ipv4PrefixLength: 0
    ipv4Subnet: string
    ipv4TotalHost: 0
    ipv6AddressSpace: true
    ipv6DhcpServers:
    - string
    ipv6DnsServers:
    - string
    ipv6GateWay: string
    ipv6GlobalPool: string
    ipv6Prefix: true
    ipv6PrefixLength: 0
    ipv6Subnet: string
    ipv6TotalHost: 0
    name: string
    siteId: string
    slaacSupport: true
    type: string

- name: Update by id
  cisco.dnac.reserve_ip_subpool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    id: string
    ipv4DhcpServers:
    - string
    ipv4DnsServers:
    - string
    ipv4GateWay: string
    ipv6AddressSpace: true
    ipv6DhcpServers:
    - string
    ipv6DnsServers:
    - string
    ipv6GateWay: string
    ipv6GlobalPool: string
    ipv6Prefix: true
    ipv6PrefixLength: 0
    ipv6Subnet: string
    ipv6TotalHost: 0
    name: string
    siteId: string
    slaacSupport: true
```

## [Return Values](reserve_ip_subpool_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **dnac_response**  dictionary | A dictionary or list with the response returned by the Cisco DNAC Python SDK  **Returned:** always  **Sample:** `{"executionId": "string", "executionStatusUrl": "string", "message": "string"}` |

### Authors

- Rafael Campos (@racampos)

### Collection links

- [Issue Tracker](https://github.com/cisco-en-programmability/dnacenter-ansible/issues)
- [Repository (Sources)](https://github.com/cisco-en-programmability/dnacenter-ansible)
