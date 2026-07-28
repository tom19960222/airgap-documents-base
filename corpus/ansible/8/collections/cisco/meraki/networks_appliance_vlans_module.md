---
collection: ansible
version: "8"
title: "cisco.meraki.networks_appliance_vlans module – Resource module for networks _appliance _vlans"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_appliance_vlans_module.html
fetched_at: 2026-07-28T01:33:28+00:00
---
# cisco.meraki.networks_appliance_vlans module – Resource module for networks _appliance _vlans

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
> see [Requirements](networks_appliance_vlans_module.md#ansible-collections-cisco-meraki-networks-appliance-vlans-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_appliance_vlans`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_appliance_vlans_module.md#synopsis)
- [Requirements](networks_appliance_vlans_module.md#requirements)
- [Parameters](networks_appliance_vlans_module.md#parameters)
- [Notes](networks_appliance_vlans_module.md#notes)
- [See Also](networks_appliance_vlans_module.md#see-also)
- [Examples](networks_appliance_vlans_module.md#examples)
- [Return Values](networks_appliance_vlans_module.md#return-values)

## [Synopsis](networks_appliance_vlans_module.md#id1)

- Manage operations create, update and delete of the resource networks _appliance _vlans.
- Add a VLAN.
- Delete a VLAN from a network.
- Update a VLAN.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_appliance_vlans_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_appliance_vlans_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **applianceIp**  string | The local IP of the appliance on the VLAN. |
| **cidr**  string | CIDR of the pool of subnets. Applicable only for template network. Each network bound to the template will automatically pick a subnet from this pool to build its own VLAN. |
| **dhcpBootFilename**  string | DHCP boot option for boot filename. |
| **dhcpBootNextServer**  string | DHCP boot option to direct boot clients to the server to load the boot file from. |
| **dhcpBootOptionsEnabled**  boolean | Use DHCP boot options specified in other properties.  **Choices:**   - `false` - `true` |
| **dhcpHandling**  string | The appliance’s handling of DHCP requests on this VLAN. One of ‘Run a DHCP server’, ‘Relay DHCP to another server’ or ‘Do not respond to DHCP requests’. |
| **dhcpLeaseTime**  string | The term of DHCP leases if the appliance is running a DHCP server on this VLAN. One of ‘30 minutes’, ‘1 hour’, ‘4 hours’, ‘12 hours’, ‘1 day’ or ‘1 week’. |
| **dhcpOptions**  list / elements=dictionary | The list of DHCP options that will be included in DHCP responses. Each object in the list should have “code”, “type”, and “value” properties. |
| **code**  string | The code for the DHCP option. This should be an integer between 2 and 254. |
| **type**  string | The type for the DHCP option. One of ‘text’, ‘ip’, ‘hex’ or ‘integer’. |
| **value**  string | The value for the DHCP option. |
| **dhcpRelayServerIps**  list / elements=string | The IPs of the DHCP servers that DHCP requests should be relayed to. |
| **dnsNameservers**  string | The DNS nameservers used for DHCP responses, either “upstream_dns”, “google_dns”, “opendns”, or a newline seperated string of IP addresses or domain names. |
| **fixedIpAssignments**  dictionary | The DHCP fixed IP assignments on the VLAN. This should be an object that contains mappings from MAC addresses to objects that themselves each contain “ip” and “name” string fields. See the sample request/response for more details. |
| **groupPolicyId**  string | The id of the desired group policy to apply to the VLAN. |
| **id**  string | The VLAN ID of the new VLAN (must be between 1 and 4094). |
| **ipv6**  dictionary | IPv6 configuration on the VLAN. |
| **enabled**  boolean | Enable IPv6 on VLAN.  **Choices:**   - `false` - `true` |
| **prefixAssignments**  list / elements=dictionary | Prefix assignments on the VLAN. |
| **autonomous**  boolean | Auto assign a /64 prefix from the origin to the VLAN.  **Choices:**   - `false` - `true` |
| **origin**  dictionary | The origin of the prefix. |
| **interfaces**  list / elements=string | Interfaces associated with the prefix. |
| **type**  string | Type of the origin. |
| **staticApplianceIp6**  string | Manual configuration of the IPv6 Appliance IP. |
| **staticPrefix**  string | Manual configuration of a /64 prefix on the VLAN. |
| **mandatoryDhcp**  dictionary | Mandatory DHCP will enforce that clients connecting to this VLAN must use the IP address assigned by the DHCP server. Clients who use a static IP address won’t be able to associate. Only available on firmware versions 17.0 and above. |
| **enabled**  boolean | Enable Mandatory DHCP on VLAN.  **Choices:**   - `false` - `true` |
| **mask**  integer | Mask used for the subnet of all bound to the template networks. Applicable only for template network. |
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
| **name**  string | The name of the new VLAN. |
| **networkId**  string | NetworkId path parameter. Network ID. |
| **reservedIpRanges**  list / elements=dictionary | The DHCP reserved IP ranges on the VLAN. |
| **comment**  string | A text comment for the reserved range. |
| **end**  string | The last IP in the reserved range. |
| **start**  string | The first IP in the reserved range. |
| **subnet**  string | The subnet of the VLAN. |
| **templateVlanType**  string | Type of subnetting of the VLAN. Applicable only for template network. |
| **vlanId**  string | VlanId path parameter. Vlan ID. |
| **vpnNatSubnet**  string | The translated VPN subnet if VPN and VPN subnet translation are enabled on the VLAN. |

## [Notes](networks_appliance_vlans_module.md#id4)

> **Note:**
>
> - SDK Method used are appliance.Appliance.create_network_appliance_vlan, appliance.Appliance.delete_network_appliance_vlan, appliance.Appliance.update_network_appliance_vlan,
> - Paths used are post /networks/{networkId}/appliance/vlans, delete /networks/{networkId}/appliance/vlans/{vlanId}, put /networks/{networkId}/appliance/vlans/{vlanId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_appliance_vlans_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for appliance createNetworkApplianceVlan](https://developer.cisco.com/meraki/api-v1/#!create-network-appliance-vlan)
> :   Complete reference of the createNetworkApplianceVlan API.
>
> [Cisco Meraki documentation for appliance deleteNetworkApplianceVlan](https://developer.cisco.com/meraki/api-v1/#!delete-network-appliance-vlan)
> :   Complete reference of the deleteNetworkApplianceVlan API.
>
> [Cisco Meraki documentation for appliance updateNetworkApplianceVlan](https://developer.cisco.com/meraki/api-v1/#!update-network-appliance-vlan)
> :   Complete reference of the updateNetworkApplianceVlan API.

## [Examples](networks_appliance_vlans_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.networks_appliance_vlans:
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
    applianceIp: 192.168.1.2
    cidr: 192.168.1.0/24
    groupPolicyId: '101'
    id: '1234'
    ipv6:
      enabled: true
      prefixAssignments:
      - autonomous: false
        origin:
          interfaces:
          - wan0
          type: internet
        staticApplianceIp6: 2001:db8:3c4d:15::1
        staticPrefix: 2001:db8:3c4d:15::/64
    mandatoryDhcp:
      enabled: true
    mask: 28
    name: My VLAN
    networkId: string
    subnet: 192.168.1.0/24
    templateVlanType: same

- name: Update by id
  cisco.meraki.networks_appliance_vlans:
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
    adaptivePolicyGroupId: '1234'
    applianceIp: 192.168.1.2
    cidr: 192.168.1.0/24
    dhcpBootFilename: sample.file
    dhcpBootNextServer: 1.2.3.4
    dhcpBootOptionsEnabled: false
    dhcpHandling: Run a DHCP server
    dhcpLeaseTime: 1 day
    dhcpOptions:
    - code: '5'
      type: text
      value: five
    dhcpRelayServerIps:
    - 192.168.1.0/24
    - 192.168.128.0/24
    dnsNameservers: google_dns
    fixedIpAssignments:
      22:33:44:55:66:77:
        ip: 1.2.3.4
        name: Some client name
    groupPolicyId: '101'
    ipv6:
      enabled: true
      prefixAssignments:
      - autonomous: false
        origin:
          interfaces:
          - wan0
          type: internet
        staticApplianceIp6: 2001:db8:3c4d:15::1
        staticPrefix: 2001:db8:3c4d:15::/64
    mandatoryDhcp:
      enabled: true
    mask: 28
    name: My VLAN
    networkId: string
    reservedIpRanges:
    - comment: A reserved IP range
      end: 192.168.1.1
      start: 192.168.1.0
    subnet: 192.168.1.0/24
    templateVlanType: same
    vlanId: string
    vpnNatSubnet: 192.168.1.0/24

- name: Delete by id
  cisco.meraki.networks_appliance_vlans:
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
    networkId: string
    vlanId: string
```

## [Return Values](networks_appliance_vlans_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{"applianceIp": "string", "cidr": "string", "groupPolicyId": "string", "id": "string", "interfaceId": "string", "ipv6": {"enabled": true, "prefixAssignments": [{"autonomous": true, "origin": {"interfaces": ["string"], "type": "string"}, "staticApplianceIp6": "string", "staticPrefix": "string"}]}, "mandatoryDhcp": {"enabled": true}, "mask": 0, "name": "string", "subnet": "string", "templateVlanType": "string"}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
