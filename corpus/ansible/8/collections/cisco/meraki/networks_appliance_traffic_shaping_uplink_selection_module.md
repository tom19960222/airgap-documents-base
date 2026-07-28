---
collection: ansible
version: "8"
title: "cisco.meraki.networks_appliance_traffic_shaping_uplink_selection module – Resource module for networks _appliance _trafficshaping _uplinkselection"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_appliance_traffic_shaping_uplink_selection_module.html
fetched_at: 2026-07-28T01:33:27+00:00
---
# cisco.meraki.networks_appliance_traffic_shaping_uplink_selection module – Resource module for networks _appliance _trafficshaping _uplinkselection

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
> see [Requirements](networks_appliance_traffic_shaping_uplink_selection_module.md#ansible-collections-cisco-meraki-networks-appliance-traffic-shaping-uplink-selection-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_appliance_traffic_shaping_uplink_selection`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_appliance_traffic_shaping_uplink_selection_module.md#synopsis)
- [Requirements](networks_appliance_traffic_shaping_uplink_selection_module.md#requirements)
- [Parameters](networks_appliance_traffic_shaping_uplink_selection_module.md#parameters)
- [Notes](networks_appliance_traffic_shaping_uplink_selection_module.md#notes)
- [See Also](networks_appliance_traffic_shaping_uplink_selection_module.md#see-also)
- [Examples](networks_appliance_traffic_shaping_uplink_selection_module.md#examples)
- [Return Values](networks_appliance_traffic_shaping_uplink_selection_module.md#return-values)

## [Synopsis](networks_appliance_traffic_shaping_uplink_selection_module.md#id1)

- Manage operation update of the resource networks _appliance _trafficshaping _uplinkselection.
- Update uplink selection settings for an MX network.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_appliance_traffic_shaping_uplink_selection_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_appliance_traffic_shaping_uplink_selection_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **activeActiveAutoVpnEnabled**  boolean | Toggle for enabling or disabling active-active AutoVPN.  **Choices:**   - `false` - `true` |
| **defaultUplink**  string | The default uplink. Must be one of ‘wan1’ or ‘wan2’. |
| **failoverAndFailback**  dictionary | WAN failover and failback behavior. |
| **immediate**  dictionary | Immediate WAN transition terminates all flows (new and existing) on current WAN when it is deemed unreliable. |
| **enabled**  boolean | Toggle for enabling or disabling immediate WAN failover and failback.  **Choices:**   - `false` - `true` |
| **loadBalancingEnabled**  boolean | Toggle for enabling or disabling load balancing.  **Choices:**   - `false` - `true` |
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
| **vpnTrafficUplinkPreferences**  list / elements=dictionary | Array of uplink preference rules for VPN traffic. |
| **failOverCriterion**  string | Fail over criterion for this uplink preference rule. Must be one of ‘poorPerformance’ or ‘uplinkDown’. |
| **performanceClass**  dictionary | Performance class setting for this uplink preference rule. |
| **builtinPerformanceClassName**  string | Name of builtin performance class, must be present when performanceClass type is ‘builtin’, and value must be one of ‘VoIP’. |
| **customPerformanceClassId**  string | ID of created custom performance class, must be present when performanceClass type is ‘custom’. |
| **type**  string | Type of this performance class. Must be one of ‘builtin’ or ‘custom’. |
| **preferredUplink**  string | Preferred uplink for this uplink preference rule. Must be one of ‘wan1’, ‘wan2’, ‘bestForVoIP’, ‘loadBalancing’ or ‘defaultUplink’. |
| **trafficFilters**  list / elements=dictionary | Array of traffic filters for this uplink preference rule. |
| **type**  string | Type of this traffic filter. Must be one of ‘applicationCategory’, ‘application’ or ‘custom’. |
| **value**  dictionary | Value object of this traffic filter. |
| **destination**  dictionary | Destination of this custom type traffic filter. |
| **cidr**  string | CIDR format address, or “any”. E.g. “192.168.10.0/24”, “192.168.10.1” (same as “192.168.10.1/32”), “0.0.0.0/0” (same as “any”). |
| **fqdn**  string | FQDN format address. Currently only availabe in ‘destination’ of ‘vpnTrafficUplinkPreference’ object. E.g. ‘www.google.com’. |
| **host**  integer | Host ID in the VLAN, should be used along with ‘vlan’, and not exceed the vlan subnet capacity. Currently only available under a template network. |
| **network**  string | Meraki network ID. Currently only available under a template network, and the value should be ID of either same template network, or another template network currently. E.g. “L_12345678”. |
| **port**  string | E.g. “any”, “0” (also means “any”), “8080”, “1-1024”. |
| **vlan**  integer | VLAN ID of the configured VLAN in the Meraki network. Currently only available under a template network. |
| **id**  string | ID of this applicationCategory or application type traffic filter. E.g. “meraki layer7/category/1”, “meraki layer7/application/4”. |
| **protocol**  string | Protocol of this custom type traffic filter. Must be one of ‘tcp’, ‘udp’, ‘icmp’, ‘icmp6’ or ‘any’. |
| **source**  dictionary | Source of this custom type traffic filter. |
| **cidr**  string | CIDR format address, or “any”. E.g. “192.168.10.0/24”, “192.168.10.1” (same as “192.168.10.1/32”), “0.0.0.0/0” (same as “any”). |
| **host**  integer | Host ID in the VLAN, should be used along with ‘vlan’, and not exceed the vlan subnet capacity. Currently only available under a template network. |
| **network**  string | Meraki network ID. Currently only available under a template network, and the value should be ID of either same template network, or another template network currently. E.g. “L_12345678”. |
| **port**  string | E.g. “any”, “0” (also means “any”), “8080”, “1-1024”. |
| **vlan**  integer | VLAN ID of the configured VLAN in the Meraki network. Currently only available under a template network. |
| **wanTrafficUplinkPreferences**  list / elements=dictionary | Array of uplink preference rules for WAN traffic. |
| **preferredUplink**  string | Preferred uplink for this uplink preference rule. Must be one of ‘wan1’ or ‘wan2’. |
| **trafficFilters**  list / elements=dictionary | Array of traffic filters for this uplink preference rule. |
| **type**  string | Type of this traffic filter. Must be one of ‘custom’. |
| **value**  dictionary | Value object of this traffic filter. |
| **destination**  dictionary | Destination of this custom type traffic filter. |
| **cidr**  string | CIDR format address, or “any”. E.g. “192.168.10.0/24”, “192.168.10.1” (same as “192.168.10.1/32”), “0.0.0.0/0” (same as “any”). |
| **port**  string | E.g. “any”, “0” (also means “any”), “8080”, “1-1024”. |
| **protocol**  string | Protocol of this custom type traffic filter. Must be one of ‘tcp’, ‘udp’, ‘icmp6’ or ‘any’. |
| **source**  dictionary | Source of this custom type traffic filter. |
| **cidr**  string | CIDR format address, or “any”. E.g. “192.168.10.0/24”, “192.168.10.1” (same as “192.168.10.1/32”), “0.0.0.0/0” (same as “any”). |
| **host**  integer | Host ID in the VLAN, should be used along with ‘vlan’, and not exceed the vlan subnet capacity. Currently only available under a template network. |
| **port**  string | E.g. “any”, “0” (also means “any”), “8080”, “1-1024”. |
| **vlan**  integer | VLAN ID of the configured VLAN in the Meraki network. Currently only available under a template network. |

## [Notes](networks_appliance_traffic_shaping_uplink_selection_module.md#id4)

> **Note:**
>
> - SDK Method used are appliance.Appliance.update_network_appliance_traffic_shaping_uplink_selection,
> - Paths used are put /networks/{networkId}/appliance/trafficShaping/uplinkSelection,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_appliance_traffic_shaping_uplink_selection_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for appliance updateNetworkApplianceTrafficShapingUplinkSelection](https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-traffic-shaping-uplink-selection)
> :   Complete reference of the updateNetworkApplianceTrafficShapingUplinkSelection API.

## [Examples](networks_appliance_traffic_shaping_uplink_selection_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.meraki.networks_appliance_traffic_shaping_uplink_selection:
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
    activeActiveAutoVpnEnabled: true
    defaultUplink: wan1
    failoverAndFailback:
      immediate:
        enabled: true
    loadBalancingEnabled: true
    networkId: string
    vpnTrafficUplinkPreferences:
    - failOverCriterion: poorPerformance
      performanceClass:
        builtinPerformanceClassName: VoIP
        customPerformanceClassId: '123456'
        type: custom
      preferredUplink: bestForVoIP
      trafficFilters:
      - type: applicationCategory
        value:
          destination:
            cidr: any
            fqdn: www.google.com
            host: 254
            network: L_12345678
            port: 1-1024
            vlan: 10
          id: meraki:layer7/category/1
          protocol: tcp
          source:
            cidr: 192.168.1.0/24
            host: 200
            network: L_23456789
            port: any
            vlan: 20
    wanTrafficUplinkPreferences:
    - preferredUplink: wan1
      trafficFilters:
      - type: custom
        value:
          destination:
            cidr: any
            port: any
          protocol: tcp
          source:
            cidr: 192.168.1.0/24
            host: 254
            port: 1-1024
            vlan: 10
```

## [Return Values](networks_appliance_traffic_shaping_uplink_selection_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{"activeActiveAutoVpnEnabled": true, "defaultUplink": "string", "failoverAndFailback": {"immediate": {"enabled": true}}, "loadBalancingEnabled": true, "vpnTrafficUplinkPreferences": [{"failOverCriterion": "string", "performanceClass": {"builtinPerformanceClassName": "string", "customPerformanceClassId": "string", "type": "string"}, "preferredUplink": "string", "trafficFilters": [{"type": "string", "value": {"destination": {"cidr": "string", "fqdn": "string", "host": 0, "network": "string", "port": "string", "vlan": 0}, "id": "string", "protocol": "string", "source": {"cidr": "string", "host": 0, "network": "string", "port": "string", "vlan": 0}}}]}], "wanTrafficUplinkPreferences": [{"preferredUplink": "string", "trafficFilters": [{"type": "string", "value": {"destination": {"cidr": "string", "port": "string"}, "protocol": "string", "source": {"cidr": "string", "host": 0, "port": "string", "vlan": 0}}}]}]}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
