---
collection: ansible
version: "8"
title: "cisco.meraki.networks_appliance_vpn_bgp module – Resource module for networks _appliance _vpn _bgp"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_appliance_vpn_bgp_module.html
fetched_at: 2026-07-28T01:33:31+00:00
---
# cisco.meraki.networks_appliance_vpn_bgp module – Resource module for networks _appliance _vpn _bgp

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
> see [Requirements](networks_appliance_vpn_bgp_module.md#ansible-collections-cisco-meraki-networks-appliance-vpn-bgp-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_appliance_vpn_bgp`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_appliance_vpn_bgp_module.md#synopsis)
- [Requirements](networks_appliance_vpn_bgp_module.md#requirements)
- [Parameters](networks_appliance_vpn_bgp_module.md#parameters)
- [Notes](networks_appliance_vpn_bgp_module.md#notes)
- [See Also](networks_appliance_vpn_bgp_module.md#see-also)
- [Examples](networks_appliance_vpn_bgp_module.md#examples)
- [Return Values](networks_appliance_vpn_bgp_module.md#return-values)

## [Synopsis](networks_appliance_vpn_bgp_module.md#id1)

- Manage operation update of the resource networks _appliance _vpn _bgp.
- Update a Hub BGP Configuration.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_appliance_vpn_bgp_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_appliance_vpn_bgp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **asNumber**  integer | An Autonomous System Number (ASN) is required if you are to run BGP and peer with another BGP Speaker outside of the Auto VPN domain. This ASN will be applied to the entire Auto VPN domain. The entire 4-byte ASN range is supported. So, the ASN must be an integer between 1 and 4294967295. When absent, this field is not updated. If no value exists then it defaults to 64512. |
| **enabled**  boolean | Boolean value to enable or disable the BGP configuration. When BGP is enabled, the asNumber (ASN) will be autopopulated with the preconfigured ASN at other Hubs or a default value if there is no ASN configured.  **Choices:**   - `false` - `true` |
| **ibgpHoldTimer**  integer | The IBGP holdtimer in seconds. The IBGP holdtimer must be an integer between 12 and 240. When absent, this field is not updated. If no value exists then it defaults to 240. |
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
| **neighbors**  list / elements=dictionary | List of BGP neighbors. This list replaces the existing set of neighbors. When absent, this field is not updated. |
| **allowTransit**  boolean | When this feature is on, the Meraki device will advertise routes learned from other Autonomous Systems, thereby allowing traffic between Autonomous Systems to transit this AS. When absent, it defaults to false.  **Choices:**   - `false` - `true` |
| **authentication**  dictionary | Authentication settings between BGP peers. |
| **password**  string | Password to configure MD5 authentication between BGP peers. |
| **ebgpHoldTimer**  integer | The EBGP hold timer in seconds for each neighbor. The EBGP hold timer must be an integer between 12 and 240. |
| **ebgpMultihop**  integer | Configure this if the neighbor is not adjacent. The EBGP multi-hop must be an integer between 1 and 255. |
| **ip**  string | The IPv4 address of the neighbor. |
| **ipv6**  dictionary | Information regarding IPv6 address of the neighbor, Required if `ip` is not present. |
| **address**  string | The IPv6 address of the neighbor. |
| **nextHopIp**  string | The IPv4 address of the remote BGP peer that will establish a TCP session with the local MX. |
| **receiveLimit**  integer | The receive limit is the maximum number of routes that can be received from any BGP peer. The receive limit must be an integer between 0 and 4294967295. When absent, it defaults to 0. |
| **remoteAsNumber**  integer | Remote ASN of the neighbor. The remote ASN must be an integer between 1 and 4294967295. |
| **sourceInterface**  string | The output interface for peering with the remote BGP peer. Valid values are ‘wired0’, ‘wired1’ or ‘vlan{VLAN ID}’(e.g. ‘vlan123’). |
| **ttlSecurity**  dictionary | Settings for BGP TTL security to protect BGP peering sessions from forged IP attacks. |
| **enabled**  boolean | Boolean value to enable or disable BGP TTL security.  **Choices:**   - `false` - `true` |
| **networkId**  string | NetworkId path parameter. Network ID. |

## [Notes](networks_appliance_vpn_bgp_module.md#id4)

> **Note:**
>
> - SDK Method used are appliance.Appliance.update_network_appliance_vpn_bgp,
> - Paths used are put /networks/{networkId}/appliance/vpn/bgp,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_appliance_vpn_bgp_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for appliance updateNetworkApplianceVpnBgp](https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vpn-bgp)
> :   Complete reference of the updateNetworkApplianceVpnBgp API.

## [Examples](networks_appliance_vpn_bgp_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.meraki.networks_appliance_vpn_bgp:
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
    asNumber: 64515
    enabled: true
    ibgpHoldTimer: 120
    neighbors:
    - allowTransit: true
      ebgpHoldTimer: 180
      ebgpMultihop: 2
      ip: 10.10.10.22
      receiveLimit: 120
      remoteAsNumber: 64343
    networkId: string
```

## [Return Values](networks_appliance_vpn_bgp_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
