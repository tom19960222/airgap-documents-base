---
collection: ansible
version: "8"
title: "cisco.meraki.networks_appliance_vpn_site_to_site_vpn module – Resource module for networks _appliance _vpn _sitetositevpn"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_appliance_vpn_site_to_site_vpn_module.html
fetched_at: 2026-07-28T01:33:33+00:00
---
# cisco.meraki.networks_appliance_vpn_site_to_site_vpn module – Resource module for networks _appliance _vpn _sitetositevpn

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
> see [Requirements](networks_appliance_vpn_site_to_site_vpn_module.md#ansible-collections-cisco-meraki-networks-appliance-vpn-site-to-site-vpn-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_appliance_vpn_site_to_site_vpn`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_appliance_vpn_site_to_site_vpn_module.md#synopsis)
- [Requirements](networks_appliance_vpn_site_to_site_vpn_module.md#requirements)
- [Parameters](networks_appliance_vpn_site_to_site_vpn_module.md#parameters)
- [Notes](networks_appliance_vpn_site_to_site_vpn_module.md#notes)
- [See Also](networks_appliance_vpn_site_to_site_vpn_module.md#see-also)
- [Examples](networks_appliance_vpn_site_to_site_vpn_module.md#examples)
- [Return Values](networks_appliance_vpn_site_to_site_vpn_module.md#return-values)

## [Synopsis](networks_appliance_vpn_site_to_site_vpn_module.md#id1)

- Manage operation update of the resource networks _appliance _vpn _sitetositevpn.
- Update the site-to-site VPN settings of a network. Only valid for MX networks in NAT mode.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_appliance_vpn_site_to_site_vpn_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_appliance_vpn_site_to_site_vpn_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hubs**  list / elements=dictionary | The list of VPN hubs, in order of preference. In spoke mode, at least 1 hub is required. |
| **hubId**  string | The network ID of the hub. |
| **useDefaultRoute**  boolean | Only valid in ‘spoke’ mode. Indicates whether default route traffic should be sent to this hub.  **Choices:**   - `false` - `true` |
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
| **mode**  string | The site-to-site VPN mode. Can be one of ‘none’, ‘spoke’ or ‘hub’. |
| **networkId**  string | NetworkId path parameter. Network ID. |
| **subnets**  list / elements=dictionary | The list of subnets and their VPN presence. |
| **localSubnet**  string | The CIDR notation subnet used within the VPN. |
| **useVpn**  boolean | Indicates the presence of the subnet in the VPN.  **Choices:**   - `false` - `true` |

## [Notes](networks_appliance_vpn_site_to_site_vpn_module.md#id4)

> **Note:**
>
> - SDK Method used are appliance.Appliance.update_network_appliance_vpn_site_to_site_vpn,
> - Paths used are put /networks/{networkId}/appliance/vpn/siteToSiteVpn,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_appliance_vpn_site_to_site_vpn_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for appliance updateNetworkApplianceVpnSiteToSiteVpn](https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-site-to-site-vpn)
> :   Complete reference of the updateNetworkApplianceVpnSiteToSiteVpn API.

## [Examples](networks_appliance_vpn_site_to_site_vpn_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.meraki.networks_appliance_vpn_site_to_site_vpn:
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
    hubs:
    - hubId: N_4901849
      useDefaultRoute: true
    mode: spoke
    networkId: string
    subnets:
    - localSubnet: 192.168.1.0/24
      useVpn: true
```

## [Return Values](networks_appliance_vpn_site_to_site_vpn_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{"hubs": [{"hubId": "string", "useDefaultRoute": true}], "mode": "string", "subnets": [{"localSubnet": "string", "useVpn": true}]}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
