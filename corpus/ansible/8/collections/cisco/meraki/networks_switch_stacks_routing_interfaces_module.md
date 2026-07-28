---
collection: ansible
version: "8"
title: "cisco.meraki.networks_switch_stacks_routing_interfaces module – Resource module for networks _switch _stacks _routing _interfaces"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_switch_stacks_routing_interfaces_module.html
fetched_at: 2026-07-28T01:35:13+00:00
---
# cisco.meraki.networks_switch_stacks_routing_interfaces module – Resource module for networks _switch _stacks _routing _interfaces

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
> see [Requirements](networks_switch_stacks_routing_interfaces_module.md#ansible-collections-cisco-meraki-networks-switch-stacks-routing-interfaces-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_switch_stacks_routing_interfaces`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_switch_stacks_routing_interfaces_module.md#synopsis)
- [Requirements](networks_switch_stacks_routing_interfaces_module.md#requirements)
- [Parameters](networks_switch_stacks_routing_interfaces_module.md#parameters)
- [Notes](networks_switch_stacks_routing_interfaces_module.md#notes)
- [See Also](networks_switch_stacks_routing_interfaces_module.md#see-also)
- [Examples](networks_switch_stacks_routing_interfaces_module.md#examples)
- [Return Values](networks_switch_stacks_routing_interfaces_module.md#return-values)

## [Synopsis](networks_switch_stacks_routing_interfaces_module.md#id1)

- Manage operations create, update and delete of the resource networks _switch _stacks _routing _interfaces.
- Create a layer 3 interface for a switch stack.
- Delete a layer 3 interface from a switch stack.
- Update a layer 3 interface for a switch stack.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_switch_stacks_routing_interfaces_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_switch_stacks_routing_interfaces_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **defaultGateway**  string | The next hop for any traffic that isn’t going to a directly connected subnet or over a static route. This IP address must exist in a subnet with a routed interface. |
| **interfaceId**  string | InterfaceId path parameter. Interface ID. |
| **interfaceIp**  string | The IP address this switch stack will use for layer 3 routing on this VLAN or subnet. This cannot be the same as the switch’s management IP. |
| **ipv6**  dictionary | The IPv6 settings of the interface. |
| **address**  string | The IPv6 address of the interface. Required if assignmentMode is ‘static’. Must not be included if assignmentMode is ‘eui-64’. |
| **assignmentMode**  string | The IPv6 assignment mode for the interface. Can be either ‘eui-64’ or ‘static’. |
| **gateway**  string | The IPv6 default gateway of the interface. Required if prefix is defined and this is the first interface with IPv6 configured for the stack. |
| **prefix**  string | The IPv6 prefix of the interface. Required if IPv6 object is included. |
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
| **multicastRouting**  string | Enable multicast support if, multicast routing between VLANs is required. Options are, ‘disabled’, ‘enabled’ or ‘IGMP snooping querier’. Default is ‘disabled’. |
| **name**  string | A friendly name or description for the interface or VLAN. |
| **networkId**  string | NetworkId path parameter. Network ID. |
| **ospfSettings**  dictionary | The OSPF routing settings of the interface. |
| **area**  string | The OSPF area to which this interface should belong. Can be either ‘disabled’ or the identifier of an existing OSPF area. Defaults to ‘disabled’. |
| **cost**  integer | The path cost for this interface. Defaults to 1, but can be increased up to 65535 to give lower priority. |
| **isPassiveEnabled**  boolean | When enabled, OSPF will not run on the interface, but the subnet will still be advertised.  **Choices:**   - `false` - `true` |
| **subnet**  string | The network that this routed interface is on, in CIDR notation (ex. 10.1.1.0/24). |
| **switchStackId**  string | SwitchStackId path parameter. Switch stack ID. |
| **vlanId**  integer | The VLAN this routed interface is on. VLAN must be between 1 and 4094. |

## [Notes](networks_switch_stacks_routing_interfaces_module.md#id4)

> **Note:**
>
> - SDK Method used are switch.Switch.create_network_switch_stack_routing_interface, switch.Switch.delete_network_switch_stack_routing_interface, switch.Switch.update_network_switch_stack_routing_interface,
> - Paths used are post /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces, delete /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId}, put /networks/{networkId}/switch/stacks/{switchStackId}/routing/interfaces/{interfaceId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_switch_stacks_routing_interfaces_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for switch createNetworkSwitchStackRoutingInterface](https://developer.cisco.com/meraki/api-v1/#!create-network-switch-stack-routing-interface)
> :   Complete reference of the createNetworkSwitchStackRoutingInterface API.
>
> [Cisco Meraki documentation for switch deleteNetworkSwitchStackRoutingInterface](https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-stack-routing-interface)
> :   Complete reference of the deleteNetworkSwitchStackRoutingInterface API.
>
> [Cisco Meraki documentation for switch updateNetworkSwitchStackRoutingInterface](https://developer.cisco.com/meraki/api-v1/#!update-network-switch-stack-routing-interface)
> :   Complete reference of the updateNetworkSwitchStackRoutingInterface API.

## [Examples](networks_switch_stacks_routing_interfaces_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.networks_switch_stacks_routing_interfaces:
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
    defaultGateway: 192.168.1.1
    interfaceIp: 192.168.1.2
    ipv6:
      address: 1:2:3:4::1
      assignmentMode: static
      gateway: 1:2:3:4::2
      prefix: 1:2:3:4::/48
    multicastRouting: disabled
    name: L3 interface
    networkId: string
    ospfSettings:
      area: '0'
      cost: 1
      isPassiveEnabled: true
    ospfV3:
      area: '1'
      cost: 2
      isPassiveEnabled: true
    subnet: 192.168.1.0/24
    switchStackId: string
    vlanId: 100

- name: Update by id
  cisco.meraki.networks_switch_stacks_routing_interfaces:
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
    interfaceId: string
    interfaceIp: 192.168.1.2
    ipv6:
      address: 1:2:3:4::1
      assignmentMode: static
      gateway: 1:2:3:4::2
      prefix: 1:2:3:4::/48
    multicastRouting: disabled
    name: L3 interface
    networkId: string
    ospfSettings:
      area: '0'
      cost: 1
      isPassiveEnabled: true
    ospfV3:
      area: '1'
      cost: 2
      isPassiveEnabled: true
    subnet: 192.168.1.0/24
    switchStackId: string
    vlanId: 100

- name: Delete by id
  cisco.meraki.networks_switch_stacks_routing_interfaces:
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
    state: absent
    interfaceId: string
    networkId: string
    switchStackId: string
```

## [Return Values](networks_switch_stacks_routing_interfaces_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
