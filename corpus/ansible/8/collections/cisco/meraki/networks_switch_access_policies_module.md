---
collection: ansible
version: "8"
title: "cisco.meraki.networks_switch_access_policies module – Resource module for networks _switch _accesspolicies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_switch_access_policies_module.html
fetched_at: 2026-07-28T01:34:50+00:00
---
# cisco.meraki.networks_switch_access_policies module – Resource module for networks _switch _accesspolicies

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
> see [Requirements](networks_switch_access_policies_module.md#ansible-collections-cisco-meraki-networks-switch-access-policies-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_switch_access_policies`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_switch_access_policies_module.md#synopsis)
- [Requirements](networks_switch_access_policies_module.md#requirements)
- [Parameters](networks_switch_access_policies_module.md#parameters)
- [Notes](networks_switch_access_policies_module.md#notes)
- [See Also](networks_switch_access_policies_module.md#see-also)
- [Examples](networks_switch_access_policies_module.md#examples)
- [Return Values](networks_switch_access_policies_module.md#return-values)

## [Synopsis](networks_switch_access_policies_module.md#id1)

- Manage operations create, update and delete of the resource networks _switch _accesspolicies.
- Create an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.
- Delete an access policy for a switch network.
- Update an access policy for a switch network. If you would like to enable Meraki Authentication, set radiusServers to empty array.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_switch_access_policies_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_switch_access_policies_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **accessPolicyNumber**  string | AccessPolicyNumber path parameter. Access policy number. |
| **accessPolicyType**  string | Access Type of the policy. Automatically ‘Hybrid authentication’ when hostMode is ‘Multi-Domain’. |
| **dot1x**  dictionary | 802.1x Settings. |
| **controlDirection**  string | Supports either ‘both’ or ‘inbound’. Set to ‘inbound’ to allow unauthorized egress on the switchport. Set to ‘both’ to control both traffic directions with authorization. Defaults to ‘both’. |
| **guestPortBouncing**  boolean | If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers.  **Choices:**   - `false` - `true` |
| **guestVlanId**  integer | ID for the guest VLAN allow unauthorized devices access to limited network resources. |
| **hostMode**  string | Choose the Host Mode for the access policy. |
| **increaseAccessSpeed**  boolean | Enabling this option will make switches execute 802.1X and MAC-bypass authentication simultaneously so that clients authenticate faster. Only required when accessPolicyType is ‘Hybrid Authentication.  **Choices:**   - `false` - `true` |
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
| **name**  string | Name of the access policy. |
| **networkId**  string | NetworkId path parameter. Network ID. |
| **radius**  dictionary | Object for RADIUS Settings. |
| **criticalAuth**  dictionary | Critical auth settings for when authentication is rejected by the RADIUS server. |
| **dataVlanId**  integer | VLAN that clients who use data will be placed on when RADIUS authentication fails. Will be null if hostMode is Multi-Auth. |
| **suspendPortBounce**  boolean | Enable to suspend port bounce when RADIUS servers are unreachable.  **Choices:**   - `false` - `true` |
| **voiceVlanId**  integer | VLAN that clients who use voice will be placed on when RADIUS authentication fails. Will be null if hostMode is Multi-Auth. |
| **failedAuthVlanId**  integer | VLAN that clients will be placed on when RADIUS authentication fails. Will be null if hostMode is Multi-Auth. |
| **reAuthenticationInterval**  integer | Re-authentication period in seconds. Will be null if hostMode is Multi-Auth. |
| **radiusAccountingEnabled**  boolean | Enable to send start, interim-update and stop messages to a configured RADIUS accounting server for tracking connected clients.  **Choices:**   - `false` - `true` |
| **radiusAccountingServers**  list / elements=dictionary | List of RADIUS accounting servers to require connecting devices to authenticate against before granting network access. |
| **host**  string | Public IP address of the RADIUS accounting server. |
| **port**  integer | UDP port that the RADIUS Accounting server listens on for access requests. |
| **secret**  string | RADIUS client shared secret. |
| **radiusCoaSupportEnabled**  boolean | Change of authentication for RADIUS re-authentication and disconnection.  **Choices:**   - `false` - `true` |
| **radiusGroupAttribute**  string | Acceptable values are `””` for None, or `”11”` for Group Policies ACL. |
| **radiusServers**  list / elements=dictionary | List of RADIUS servers to require connecting devices to authenticate against before granting network access. |
| **host**  string | Public IP address of the RADIUS server. |
| **port**  integer | UDP port that the RADIUS server listens on for access requests. |
| **secret**  string | RADIUS client shared secret. |
| **radiusTestingEnabled**  boolean | If enabled, Meraki devices will periodically send access-request messages to these RADIUS servers.  **Choices:**   - `false` - `true` |
| **urlRedirectWalledGardenEnabled**  boolean | Enable to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication.  **Choices:**   - `false` - `true` |
| **urlRedirectWalledGardenRanges**  list / elements=string | IP address ranges, in CIDR notation, to restrict access for clients to a specific set of IP addresses or hostnames prior to authentication. |
| **voiceVlanClients**  boolean | CDP/LLDP capable voice clients will be able to use this VLAN. Automatically true when hostMode is ‘Multi-Domain’.  **Choices:**   - `false` - `true` |

## [Notes](networks_switch_access_policies_module.md#id4)

> **Note:**
>
> - SDK Method used are switch.Switch.create_network_switch_access_policy, switch.Switch.delete_network_switch_access_policy, switch.Switch.update_network_switch_access_policy,
> - Paths used are post /networks/{networkId}/switch/accessPolicies, delete /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber}, put /networks/{networkId}/switch/accessPolicies/{accessPolicyNumber},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_switch_access_policies_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for switch createNetworkSwitchAccessPolicy](https://developer.cisco.com/meraki/api-v1/#!create-network-switch-access-policy)
> :   Complete reference of the createNetworkSwitchAccessPolicy API.
>
> [Cisco Meraki documentation for switch deleteNetworkSwitchAccessPolicy](https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-access-policy)
> :   Complete reference of the deleteNetworkSwitchAccessPolicy API.
>
> [Cisco Meraki documentation for switch updateNetworkSwitchAccessPolicy](https://developer.cisco.com/meraki/api-v1/#!update-network-switch-access-policy)
> :   Complete reference of the updateNetworkSwitchAccessPolicy API.

## [Examples](networks_switch_access_policies_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.networks_switch_access_policies:
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
    accessPolicyType: Hybrid authentication
    dot1x:
      controlDirection: inbound
    guestPortBouncing: false
    guestVlanId: 100
    hostMode: Single-Host
    increaseAccessSpeed: false
    name: 'Access policy #1'
    networkId: string
    radius:
      criticalAuth:
        dataVlanId: 100
        suspendPortBounce: true
        voiceVlanId: 100
      failedAuthVlanId: 100
      reAuthenticationInterval: 120
    radiusAccountingEnabled: true
    radiusAccountingServers:
    - host: 1.2.3.4
      port: 22
      secret: secret
    radiusCoaSupportEnabled: false
    radiusGroupAttribute: '11'
    radiusServers:
    - host: 1.2.3.4
      port: 22
      secret: secret
    radiusTestingEnabled: false
    urlRedirectWalledGardenEnabled: true
    urlRedirectWalledGardenRanges:
    - 192.168.1.0/24
    voiceVlanClients: true

- name: Update by id
  cisco.meraki.networks_switch_access_policies:
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
    accessPolicyNumber: string
    accessPolicyType: Hybrid authentication
    dot1x:
      controlDirection: inbound
    guestPortBouncing: false
    guestVlanId: 100
    hostMode: Single-Host
    increaseAccessSpeed: false
    name: 'Access policy #1'
    networkId: string
    radius:
      criticalAuth:
        dataVlanId: 100
        suspendPortBounce: true
        voiceVlanId: 100
      failedAuthVlanId: 100
      reAuthenticationInterval: 120
    radiusAccountingEnabled: true
    radiusAccountingServers:
    - host: 1.2.3.4
      port: 22
      secret: secret
    radiusCoaSupportEnabled: false
    radiusGroupAttribute: '11'
    radiusServers:
    - host: 1.2.3.4
      port: 22
      secret: secret
    radiusTestingEnabled: false
    urlRedirectWalledGardenEnabled: true
    urlRedirectWalledGardenRanges:
    - 192.168.1.0/24
    voiceVlanClients: true

- name: Delete by id
  cisco.meraki.networks_switch_access_policies:
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
    accessPolicyNumber: string
    networkId: string
```

## [Return Values](networks_switch_access_policies_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{"accessPolicyType": "string", "dot1x": {"controlDirection": "string"}, "guestPortBouncing": true, "guestVlanId": 0, "hostMode": "string", "increaseAccessSpeed": true, "name": "string", "radius": {"criticalAuth": {"dataVlanId": 0, "suspendPortBounce": true, "voiceVlanId": 0}, "failedAuthVlanId": 0, "reAuthenticationInterval": 0}, "radiusAccountingEnabled": true, "radiusAccountingServers": [{"host": "string", "port": 0}], "radiusCoaSupportEnabled": true, "radiusGroupAttribute": "string", "radiusServers": [{"host": "string", "port": 0}], "radiusTestingEnabled": true, "urlRedirectWalledGardenEnabled": true, "urlRedirectWalledGardenRanges": ["string"], "voiceVlanClients": true}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
