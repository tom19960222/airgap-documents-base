---
collection: ansible
version: "8"
title: "cisco.meraki.networks_switch_stacks_routing_interfaces_dhcp module – Resource module for networks _switch _stacks _routing _interfaces _dhcp"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_switch_stacks_routing_interfaces_dhcp_module.html
fetched_at: 2026-07-28T01:35:14+00:00
---
# cisco.meraki.networks_switch_stacks_routing_interfaces_dhcp module – Resource module for networks _switch _stacks _routing _interfaces _dhcp

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/ui/repo/published/cisco/meraki/) (version 2.17.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
> You need further requirements to be able to use this module,
> see [Requirements](networks_switch_stacks_routing_interfaces_dhcp_module.md#ansible-collections-cisco-meraki-networks-switch-stacks-routing-interfaces-dhcp-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_switch_stacks_routing_interfaces_dhcp`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_switch_stacks_routing_interfaces_dhcp_module.md#synopsis)
- [Requirements](networks_switch_stacks_routing_interfaces_dhcp_module.md#requirements)
- [Parameters](networks_switch_stacks_routing_interfaces_dhcp_module.md#parameters)
- [Notes](networks_switch_stacks_routing_interfaces_dhcp_module.md#notes)
- [See Also](networks_switch_stacks_routing_interfaces_dhcp_module.md#see-also)
- [Examples](networks_switch_stacks_routing_interfaces_dhcp_module.md#examples)
- [Return Values](networks_switch_stacks_routing_interfaces_dhcp_module.md#return-values)

## [Synopsis](networks_switch_stacks_routing_interfaces_dhcp_module.md#id1)

- Manage operation update of the resource networks _switch _stacks _routing _interfaces _dhcp.
- Update a layer 3 interface DHCP configuration for a switch stack.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_switch_stacks_routing_interfaces_dhcp_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_switch_stacks_routing_interfaces_dhcp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bootFileName**  string | The PXE boot server file name for the DHCP server running on the switch stack interface. |
| **bootNextServer**  string | The PXE boot server IP for the DHCP server running on the switch stack interface. |
| **bootOptionsEnabled**  boolean | Enable DHCP boot options to provide PXE boot options configs for the dhcp server running on the switch stack interface.  **Choices:**   - `false` - `true` |
| **dhcpLeaseTime**  string | The DHCP lease time config for the dhcp server running on switch stack interface (‘30 minutes’, ‘1 hour’, ‘4 hours’, ‘12 hours’, ‘1 day’ or ‘1 week’). |
| **dhcpMode**  string | The DHCP mode options for the switch stack interface (‘dhcpDisabled’, ‘dhcpRelay’ or ‘dhcpServer’). |
| **dhcpOptions**  list / elements=dictionary | Array of DHCP options consisting of code, type and value for the DHCP server running on the switch stack interface. |
| **code**  string | The code for DHCP option which should be from 2 to 254. |
| **type**  string | The type of the DHCP option which should be one of (‘text’, ‘ip’, ‘integer’ or ‘hex’). |
| **value**  string | The value of the DHCP option. |
| **dhcpRelayServerIps**  list / elements=string | The DHCP relay server IPs to which DHCP packets would get relayed for the switch stack interface. |
| **dnsCustomNameservers**  list / elements=string | The DHCP name server IPs when DHCP name server option is ‘custom’. |
| **dnsNameserversOption**  string | The DHCP name server option for the dhcp server running on the switch stack interface (‘googlePublicDns’, ‘openDns’ or ‘custom’). |
| **fixedIpAssignments**  list / elements=dictionary | Array of DHCP fixed IP assignments for the DHCP server running on the switch stack interface. |
| **ip**  string | The IP address of the client which has fixed IP address assigned to it. |
| **mac**  string | The MAC address of the client which has fixed IP address. |
| **name**  string | The name of the client which has fixed IP address. |
| **interfaceId**  string | InterfaceId path parameter. Interface ID. |
| **meraki_action_batch_retry_wait_time**  integer | meraki_action_batch_retry_wait_time (integer), action batch concurrency error retry wait time  **Default:** `60` |
| **meraki_api_key**  string / required | meraki_api_key (string), API key generated in dashboard; can also be set as an environment variable MERAKI_DASHBOARD_API_KEY |
| **meraki_base_url**  string | meraki_base_url (string), preceding all endpoint resources  **Default:** `"https://api.meraki.com/api/v1"` |
| **meraki_be_geo_id**  string | meraki_be_geo_id (string), optional partner identifier for API usage tracking; can also be set as an environment variable BE_GEO_ID  **Default:** `""` |
| **meraki_caller**  string | meraki_caller (string), optional identifier for API usage tracking; can also be set as an environment variable MERAKI_PYTHON_SDK_CALLER  **Default:** `""` |
| **meraki_certificate_path**  string | meraki_certificate_path (string), path for TLS/SSL certificate verification if behind local proxy  **Default:** `""` |
| **meraki_inherit_logging_config**  boolean | meraki_inherit_logging_config (boolean), Inherits your own logger instance  **Choices:**   - `false` ← (default) - `true` |
| **meraki_log_file_prefix**  string | meraki_log_file_prefix (string), log file name appended with date and timestamp  **Default:** `"meraki_api_"` |
| **meraki_log_path**  string | log_path (string), path to output log; by default, working directory of script if not specified  **Default:** `""` |
| **meraki_maximum_retries**  integer | meraki_maximum_retries (integer), retry up to this many times when encountering 429s or other server-side errors  **Default:** `2` |
| **meraki_nginx_429_retry_wait_time**  integer | meraki_nginx_429_retry_wait_time (integer), Nginx 429 retry wait time  **Default:** `60` |
| **meraki_output_log**  boolean | meraki_output_log (boolean), create an output log file?  **Choices:**   - `false` - `true` ← (default) |
| **meraki_print_console**  boolean | meraki_print_console (boolean), print logging output to console?  **Choices:**   - `false` - `true` ← (default) |
| **meraki_requests_proxy**  string | meraki_requests_proxy (string), proxy server and port, if needed, for HTTPS  **Default:** `""` |
| **meraki_retry_4xx_error**  boolean | meraki_retry_4xx_error (boolean), retry if encountering other 4XX error (besides 429)?  **Choices:**   - `false` ← (default) - `true` |
| **meraki_retry_4xx_error_wait_time**  integer | meraki_retry_4xx_error_wait_time (integer), other 4XX error retry wait time  **Default:** `60` |
| **meraki_simulate**  boolean | meraki_simulate (boolean), simulate POST/PUT/DELETE calls to prevent changes?  **Choices:**   - `false` ← (default) - `true` |
| **meraki_single_request_timeout**  integer | meraki_single_request_timeout (integer), maximum number of seconds for each API call  **Default:** `60` |
| **meraki_suppress_logging**  boolean | meraki_suppress_logging (boolean), disable all logging? you’re on your own then!  **Choices:**   - `false` ← (default) - `true` |
| **meraki_use_iterator_for_get_pages**  boolean | meraki_use_iterator_for_get_pages (boolean), list\* methods will return an iterator with each object instead of a complete list with all items  **Choices:**   - `false` ← (default) - `true` |
| **meraki_wait_on_rate_limit**  boolean | meraki_wait_on_rate_limit (boolean), retry if 429 rate limit error encountered?  **Choices:**   - `false` - `true` ← (default) |
| **networkId**  string | NetworkId path parameter. Network ID. |
| **reservedIpRanges**  list / elements=dictionary | Array of DHCP reserved IP assignments for the DHCP server running on the switch stack interface. |
| **comment**  string | The comment for the reserved IP range. |
| **end**  string | The ending IP address of the reserved IP range. |
| **start**  string | The starting IP address of the reserved IP range. |
| **switchStackId**  string | SwitchStackId path parameter. Switch stack ID. |

## [Notes](networks_switch_stacks_routing_interfaces_dhcp_module.md#id4)

> **Note:**
>
> - SDK Method used are switch.Switch.update_network_switch_stack_routing_interface_dhcp,
> - Paths used are put /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}/dhcp,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_switch_stacks_routing_interfaces_dhcp_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for switch updateNetworkSwitchStackRoutingInterfaceDhcp](https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface-dhcp)
> :   Complete reference of the updateNetworkSwitchStackRoutingInterfaceDhcp API.

## [Examples](networks_switch_stacks_routing_interfaces_dhcp_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.meraki.networks_switch_stacks_routing_interfaces_dhcp:
    meraki_api_key: "{{meraki_api_key}}"
    meraki_base_url: "{{meraki_base_url}}"
    meraki_single_request_timeout: "{{meraki_single_request_timeout}}"
    meraki_certificate_path: "{{meraki_certificate_path}}"
    meraki_requests_proxy: "{{meraki_requests_proxy}}"
    meraki_wait_on_rate_limit: "{{meraki_wait_on_rate_limit}}"
    meraki_nginx_429_retry_wait_time: "{{meraki_nginx_429_retry_wait_time}}"
    meraki_action_batch_retry_wait_time: "{{meraki_action_batch_retry_wait_time}}"
    meraki_retry_4xx_error: "{{meraki_retry_4xx_error}}"
    meraki_retry_4xx_error_wait_time: "{{meraki_retry_4xx_error_wait_time}}"
    meraki_maximum_retries: "{{meraki_maximum_retries}}"
    meraki_output_log: "{{meraki_output_log}}"
    meraki_log_file_prefix: "{{meraki_log_file_prefix}}"
    meraki_log_path: "{{meraki_log_path}}"
    meraki_print_console: "{{meraki_print_console}}"
    meraki_suppress_logging: "{{meraki_suppress_logging}}"
    meraki_simulate: "{{meraki_simulate}}"
    meraki_be_geo_id: "{{meraki_be_geo_id}}"
    meraki_use_iterator_for_get_pages: "{{meraki_use_iterator_for_get_pages}}"
    meraki_inherit_logging_config: "{{meraki_inherit_logging_config}}"
    state: present
    bootFileName: home_boot_file
    bootNextServer: 1.2.3.4
    bootOptionsEnabled: true
    dhcpLeaseTime: 1 day
    dhcpMode: dhcpServer
    dhcpOptions:
    - code: '5'
      type: text
      value: five
    dnsCustomNameservers:
    - 8.8.8.8, 8.8.4.4
    dnsNameserversOption: custom
    fixedIpAssignments:
    - ip: 192.168.1.12
      mac: 22:33:44:55:66:77
      name: Cisco Meraki valued client
    interfaceId: string
    networkId: string
    reservedIpRanges:
    - comment: A reserved IP range
      end: 192.168.1.10
      start: 192.168.1.1
    switchStackId: string
```

## [Return Values](networks_switch_stacks_routing_interfaces_dhcp_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
