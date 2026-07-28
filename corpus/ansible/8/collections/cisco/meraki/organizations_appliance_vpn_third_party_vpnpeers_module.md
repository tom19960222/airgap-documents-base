---
collection: ansible
version: "8"
title: "cisco.meraki.organizations_appliance_vpn_third_party_vpnpeers module – Resource module for organizations _appliance _vpn _thirdpartyvpnpeers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/organizations_appliance_vpn_third_party_vpnpeers_module.html
fetched_at: 2026-07-28T01:36:22+00:00
---
# cisco.meraki.organizations_appliance_vpn_third_party_vpnpeers module – Resource module for organizations _appliance _vpn _thirdpartyvpnpeers

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
> see [Requirements](organizations_appliance_vpn_third_party_vpnpeers_module.md#ansible-collections-cisco-meraki-organizations-appliance-vpn-third-party-vpnpeers-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.organizations_appliance_vpn_third_party_vpnpeers`.

New in cisco.meraki 2.16.0

- [Synopsis](organizations_appliance_vpn_third_party_vpnpeers_module.md#synopsis)
- [Requirements](organizations_appliance_vpn_third_party_vpnpeers_module.md#requirements)
- [Parameters](organizations_appliance_vpn_third_party_vpnpeers_module.md#parameters)
- [Notes](organizations_appliance_vpn_third_party_vpnpeers_module.md#notes)
- [See Also](organizations_appliance_vpn_third_party_vpnpeers_module.md#see-also)
- [Examples](organizations_appliance_vpn_third_party_vpnpeers_module.md#examples)
- [Return Values](organizations_appliance_vpn_third_party_vpnpeers_module.md#return-values)

## [Synopsis](organizations_appliance_vpn_third_party_vpnpeers_module.md#id1)

- Manage operation update of the resource organizations _appliance _vpn _thirdpartyvpnpeers.
- Update the third party VPN peers for an organization.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](organizations_appliance_vpn_third_party_vpnpeers_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](organizations_appliance_vpn_third_party_vpnpeers_module.md#id3)

| Parameter | Comments |
| --- | --- |
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
| **organizationId**  string | OrganizationId path parameter. Organization ID. |
| **peers**  list / elements=dictionary | The list of VPN peers. |
| **ikeVersion**  string | Optional The IKE version to be used for the IPsec VPN peer configuration. Defaults to ‘1’ when omitted. |
| **ipsecPolicies**  dictionary | Custom IPSec policies for the VPN peer. If not included and a preset has not been chosen, the default preset for IPSec policies will be used. |
| **childAuthAlgo**  list / elements=string | This is the authentication algorithms to be used in Phase 2. The value should be an array with one of the following algorithms ‘sha256’, ‘sha1’, ‘md5’. |
| **childCipherAlgo**  list / elements=string | This is the cipher algorithms to be used in Phase 2. The value should be an array with one or more of the following algorithms ‘aes256’, ‘aes192’, ‘aes128’, ‘tripledes’, ‘des’, ‘null’. |
| **childLifetime**  integer | The lifetime of the Phase 2 SA in seconds. |
| **childPfsGroup**  list / elements=string | This is the Diffie-Hellman group to be used for Perfect Forward Secrecy in Phase 2. The value should be an array with one of the following values ‘disabled’,’group14’, ‘group5’, ‘group2’, ‘group1’. |
| **ikeAuthAlgo**  list / elements=string | This is the authentication algorithm to be used in Phase 1. The value should be an array with one of the following algorithms ‘sha256’, ‘sha1’, ‘md5’. |
| **ikeCipherAlgo**  list / elements=string | This is the cipher algorithm to be used in Phase 1. The value should be an array with one of the following algorithms ‘aes256’, ‘aes192’, ‘aes128’, ‘tripledes’, ‘des’. |
| **ikeDiffieHellmanGroup**  list / elements=string | This is the Diffie-Hellman group to be used in Phase 1. The value should be an array with one of the following algorithms ‘group14’, ‘group5’, ‘group2’, ‘group1’. |
| **ikeLifetime**  integer | The lifetime of the Phase 1 SA in seconds. |
| **ikePrfAlgo**  list / elements=string | Optional This is the pseudo-random function to be used in IKE_SA. The value should be an array with one of the following algorithms ‘prfsha256’, ‘prfsha1’, ‘prfmd5’, ‘default’. The ‘default’ option can be used to default to the Authentication algorithm. |
| **ipsecPoliciesPreset**  string | One of the following available presets ‘default’, ‘aws’, ‘azure’. If this is provided, the ‘ipsecPolicies’ parameter is ignored. |
| **localId**  string | Optional The local ID is used to identify the MX to the peer. This will apply to all MXs this peer applies to. |
| **name**  string | The name of the VPN peer. |
| **networkTags**  list / elements=string | A list of network tags that will connect with this peer. Use ‘all’ for all networks. Use ‘none’ for no networks. If not included, the default is ‘all’. |
| **privateSubnets**  list / elements=string | The list of the private subnets of the VPN peer. |
| **publicIp**  string | Optional The public IP of the VPN peer. |
| **remoteId**  string | Optional The remote ID is used to identify the connecting VPN peer. This can either be a valid IPv4 Address, FQDN or User FQDN. |
| **secret**  string | The shared secret with the VPN peer. |

## [Notes](organizations_appliance_vpn_third_party_vpnpeers_module.md#id4)

> **Note:**
>
> - SDK Method used are appliance.Appliance.update_organization_appliance_vpn_third_party_vpnpeers,
> - Paths used are put /organizations/{organizationId}/appliance/vpn/thirdPartyVPNPeers,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](organizations_appliance_vpn_third_party_vpnpeers_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for appliance updateOrganizationApplianceVpnThirdPartyVPNPeers](https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-third-party-vpn-peers)
> :   Complete reference of the updateOrganizationApplianceVpnThirdPartyVPNPeers API.

## [Examples](organizations_appliance_vpn_third_party_vpnpeers_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.meraki.organizations_appliance_vpn_third_party_vpnpeers:
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
    organizationId: string
    peers:
    - ikeVersion: '2'
      ipsecPolicies:
        childAuthAlgo:
        - sha1
        childCipherAlgo:
        - aes128
        childLifetime: 28800
        childPfsGroup:
        - disabled
        ikeAuthAlgo:
        - sha1
        ikeCipherAlgo:
        - tripledes
        ikeDiffieHellmanGroup:
        - group2
        ikeLifetime: 28800
        ikePrfAlgo:
        - prfsha1
      ipsecPoliciesPreset: default
      localId: myMXId@meraki.com
      name: Peer Name
      networkTags:
      - none
      privateSubnets:
      - 192.168.1.0/24
      - 192.168.128.0/24
      publicIp: 123.123.123.1
      remoteId: miles@meraki.com
      secret: Sample Password
```

## [Return Values](organizations_appliance_vpn_third_party_vpnpeers_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"name\": \"string\",\n    \"publicIp\": \"string\",\n    \"remoteId\": \"string\",\n    \"localId\": \"string\",\n    \"secret\": \"string\",\n    \"privateSubnets\": [\n      \"string\"\n    ],\n    \"ipsecPolicies\": {\n      \"ikeCipherAlgo\": [\n        \"string\"\n      ],\n      \"ikeAuthAlgo\": [\n        \"string\"\n      ],\n      \"ikePrfAlgo\": [\n        \"string\"\n      ],\n      \"ikeDiffieHellmanGroup\": [\n        \"string\"\n      ],\n      \"ikeLifetime\": 0,\n      \"childCipherAlgo\": [\n        \"string\"\n      ],\n      \"childAuthAlgo\": [\n        \"string\"\n      ],\n      \"childPfsGroup\": [\n        \"string\"\n      ],\n      \"childLifetime\": 0\n    },\n    \"ipsecPoliciesPreset\": \"string\",\n    \"ikeVersion\": \"string\",\n    \"networkTags\": [\n      \"string\"\n    ]\n  }\n]\n"` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
