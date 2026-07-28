---
collection: ansible
version: "8"
title: "cisco.meraki.networks_group_policies module – Resource module for networks _grouppolicies"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_group_policies_module.html
fetched_at: 2026-07-28T01:34:06+00:00
---
# cisco.meraki.networks_group_policies module – Resource module for networks _grouppolicies

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
> see [Requirements](networks_group_policies_module.md#ansible-collections-cisco-meraki-networks-group-policies-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_group_policies`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_group_policies_module.md#synopsis)
- [Requirements](networks_group_policies_module.md#requirements)
- [Parameters](networks_group_policies_module.md#parameters)
- [Notes](networks_group_policies_module.md#notes)
- [See Also](networks_group_policies_module.md#see-also)
- [Examples](networks_group_policies_module.md#examples)
- [Return Values](networks_group_policies_module.md#return-values)

## [Synopsis](networks_group_policies_module.md#id1)

- Manage operations create, update and delete of the resource networks _grouppolicies.
- Create a group policy.
- Delete a group policy.
- Update a group policy.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_group_policies_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_group_policies_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **bandwidth**  dictionary | The bandwidth settings for clients bound to your group policy. |
| **bandwidthLimits**  dictionary | The bandwidth limits object, specifying upload and download speed for clients bound to the group policy. These are only enforced if ‘settings’ is set to ‘custom’. |
| **limitDown**  integer | The maximum download limit (integer, in Kbps). Null indicates no limit. |
| **limitUp**  integer | The maximum upload limit (integer, in Kbps). Null indicates no limit. |
| **settings**  string | How bandwidth limits are enforced. Can be ‘network default’, ‘ignore’ or ‘custom’. |
| **bonjourForwarding**  dictionary | The Bonjour settings for your group policy. Only valid if your network has a wireless configuration. |
| **rules**  list / elements=dictionary | A list of the Bonjour forwarding rules for your group policy. If ‘settings’ is set to ‘custom’, at least one rule must be specified. |
| **description**  string | A description for your Bonjour forwarding rule. Optional. |
| **services**  list / elements=string | A list of Bonjour services. At least one service must be specified. Available services are ‘All Services’, ‘AirPlay’, ‘AFP’, ‘BitTorrent’, ‘FTP’, ‘iChat’, ‘iTunes’, ‘Printers’, ‘Samba’, ‘Scanners’ and ‘SSH’. |
| **vlanId**  string | The ID of the service VLAN. Required. |
| **settings**  string | How Bonjour rules are applied. Can be ‘network default’, ‘ignore’ or ‘custom’. |
| **contentFiltering**  dictionary | The content filtering settings for your group policy. |
| **allowedUrlPatterns**  dictionary | Settings for allowed URL patterns. |
| **patterns**  list / elements=string | A list of URL patterns that are allowed. |
| **settings**  string | How URL patterns are applied. Can be ‘network default’, ‘append’ or ‘override’. |
| **blockedUrlCategories**  dictionary | Settings for blocked URL categories. |
| **categories**  list / elements=string | A list of URL categories to block. |
| **settings**  string | How URL categories are applied. Can be ‘network default’, ‘append’ or ‘override’. |
| **blockedUrlPatterns**  dictionary | Settings for blocked URL patterns. |
| **patterns**  list / elements=string | A list of URL patterns that are blocked. |
| **settings**  string | How URL patterns are applied. Can be ‘network default’, ‘append’ or ‘override’. |
| **firewallAndTrafficShaping**  dictionary | The firewall and traffic shaping rules and settings for your policy. |
| **l3FirewallRules**  list / elements=dictionary | An ordered array of the L3 firewall rules. |
| **comment**  string | Description of the rule (optional). |
| **destCidr**  string | Destination IP address (in IP or CIDR notation), a fully-qualified domain name (FQDN, if your network supports it) or ‘any’. |
| **destPort**  string | Destination port (integer in the range 1-65535), a port range (e.g. 8080-9090), or ‘any’. |
| **policy**  string | ‘allow’ or ‘deny’ traffic specified by this rule. |
| **protocol**  string | The type of protocol (must be ‘tcp’, ‘udp’, ‘icmp’, ‘icmp6’ or ‘any’). |
| **l7FirewallRules**  list / elements=dictionary | An ordered array of L7 firewall rules. |
| **policy**  string | The policy applied to matching traffic. Must be ‘deny’. |
| **type**  string | Type of the L7 Rule. Must be ‘application’, ‘applicationCategory’, ‘host’, ‘port’ or ‘ipRange’. |
| **value**  string | The ‘value’ of what you want to block. If ‘type’ is ‘host’, ‘port’ or ‘ipRange’, ‘value’ must be a string matching either a hostname (e.g. Somewhere.com), a port (e.g. 8080), or an IP range (e.g. 192.1.0.0/16). If ‘type’ is ‘application’ or ‘applicationCategory’, then ‘value’ must be an object with an ID for the application. |
| **settings**  string | How firewall and traffic shaping rules are enforced. Can be ‘network default’, ‘ignore’ or ‘custom’. |
| **trafficShapingRules**  list / elements=dictionary | An array of traffic shaping rules. Rules are applied in the order that they are specified in. An empty list (or null) means no rules. Note that you are allowed a maximum of 8 rules. |
| **definitions**  list / elements=dictionary | A list of objects describing the definitions of your traffic shaping rule. At least one definition is required. |
| **type**  string | The type of definition. Can be one of ‘application’, ‘applicationCategory’, ‘host’, ‘port’, ‘ipRange’ or ‘localNet’. |
| **value**  string | If “type” is ‘host’, ‘port’, ‘ipRange’ or ‘localNet’, then “value” must be a string, matching either a hostname (e.g. “somesite.com”), a port (e.g. 8080), or an IP range (“192.1.0.0”, “192.1.0.0/16”, or “10.1.0.0/16 80”). ‘localNet’ also supports CIDR notation, excluding custom ports. If “type” is ‘application’ or ‘applicationCategory’, then “value” must be an object with the structure { “id” “meraki layer7/…” }, where “id” is the application category or application ID (for a list of IDs for your network, use the trafficShaping/applicationCategories endpoint). |
| **dscpTagValue**  integer | The DSCP tag applied by your rule. Null means ‘Do not change DSCP tag’. For a list of possible tag values, use the trafficShaping/dscpTaggingOptions endpoint. |
| **pcpTagValue**  integer | The PCP tag applied by your rule. Can be 0 (lowest priority) through 7 (highest priority). Null means ‘Do not set PCP tag’. |
| **perClientBandwidthLimits**  dictionary | An object describing the bandwidth settings for your rule. |
| **bandwidthLimits**  dictionary | The bandwidth limits object, specifying the upload (‘limitUp’) and download (‘limitDown’) speed in Kbps. These are only enforced if ‘settings’ is set to ‘custom’. |
| **limitDown**  integer | The maximum download limit (integer, in Kbps). |
| **limitUp**  integer | The maximum upload limit (integer, in Kbps). |
| **settings**  string | How bandwidth limits are applied by your rule. Can be one of ‘network default’, ‘ignore’ or ‘custom’. |
| **priority**  string | A string, indicating the priority level for packets bound to your rule. Can be ‘low’, ‘normal’ or ‘high’. |
| **groupPolicyId**  string | GroupPolicyId path parameter. Group policy ID. |
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
| **name**  string | The name for your group policy. Required. |
| **networkId**  string | NetworkId path parameter. Network ID. |
| **scheduling**  dictionary | The schedule for the group policy. Schedules are applied to days of the week. |
| **enabled**  boolean | Whether scheduling is enabled (true) or disabled (false). Defaults to false. If true, the schedule objects for each day of the week (monday - sunday) are parsed.  **Choices:**   - `false` - `true` |
| **friday**  dictionary | The schedule object for Friday. |
| **active**  boolean | Whether the schedule is active (true) or inactive (false) during the time specified between ‘from’ and ‘to’. Defaults to true.  **Choices:**   - `false` - `true` |
| **from**  string | The time, from ‘00 00’ to ‘24 00’. Must be less than the time specified in ‘to’. Defaults to ‘00 00’. Only 30 minute increments are allowed. |
| **to**  string | The time, from ‘00 00’ to ‘24 00’. Must be greater than the time specified in ‘from’. Defaults to ‘24 00’. Only 30 minute increments are allowed. |
| **monday**  dictionary | The schedule object for Monday. |
| **active**  boolean | Whether the schedule is active (true) or inactive (false) during the time specified between ‘from’ and ‘to’. Defaults to true.  **Choices:**   - `false` - `true` |
| **from**  string | The time, from ‘00 00’ to ‘24 00’. Must be less than the time specified in ‘to’. Defaults to ‘00 00’. Only 30 minute increments are allowed. |
| **to**  string | The time, from ‘00 00’ to ‘24 00’. Must be greater than the time specified in ‘from’. Defaults to ‘24 00’. Only 30 minute increments are allowed. |
| **saturday**  dictionary | The schedule object for Saturday. |
| **active**  boolean | Whether the schedule is active (true) or inactive (false) during the time specified between ‘from’ and ‘to’. Defaults to true.  **Choices:**   - `false` - `true` |
| **from**  string | The time, from ‘00 00’ to ‘24 00’. Must be less than the time specified in ‘to’. Defaults to ‘00 00’. Only 30 minute increments are allowed. |
| **to**  string | The time, from ‘00 00’ to ‘24 00’. Must be greater than the time specified in ‘from’. Defaults to ‘24 00’. Only 30 minute increments are allowed. |
| **sunday**  dictionary | The schedule object for Sunday. |
| **active**  boolean | Whether the schedule is active (true) or inactive (false) during the time specified between ‘from’ and ‘to’. Defaults to true.  **Choices:**   - `false` - `true` |
| **from**  string | The time, from ‘00 00’ to ‘24 00’. Must be less than the time specified in ‘to’. Defaults to ‘00 00’. Only 30 minute increments are allowed. |
| **to**  string | The time, from ‘00 00’ to ‘24 00’. Must be greater than the time specified in ‘from’. Defaults to ‘24 00’. Only 30 minute increments are allowed. |
| **thursday**  dictionary | The schedule object for Thursday. |
| **active**  boolean | Whether the schedule is active (true) or inactive (false) during the time specified between ‘from’ and ‘to’. Defaults to true.  **Choices:**   - `false` - `true` |
| **from**  string | The time, from ‘00 00’ to ‘24 00’. Must be less than the time specified in ‘to’. Defaults to ‘00 00’. Only 30 minute increments are allowed. |
| **to**  string | The time, from ‘00 00’ to ‘24 00’. Must be greater than the time specified in ‘from’. Defaults to ‘24 00’. Only 30 minute increments are allowed. |
| **tuesday**  dictionary | The schedule object for Tuesday. |
| **active**  boolean | Whether the schedule is active (true) or inactive (false) during the time specified between ‘from’ and ‘to’. Defaults to true.  **Choices:**   - `false` - `true` |
| **from**  string | The time, from ‘00 00’ to ‘24 00’. Must be less than the time specified in ‘to’. Defaults to ‘00 00’. Only 30 minute increments are allowed. |
| **to**  string | The time, from ‘00 00’ to ‘24 00’. Must be greater than the time specified in ‘from’. Defaults to ‘24 00’. Only 30 minute increments are allowed. |
| **wednesday**  dictionary | The schedule object for Wednesday. |
| **active**  boolean | Whether the schedule is active (true) or inactive (false) during the time specified between ‘from’ and ‘to’. Defaults to true.  **Choices:**   - `false` - `true` |
| **from**  string | The time, from ‘00 00’ to ‘24 00’. Must be less than the time specified in ‘to’. Defaults to ‘00 00’. Only 30 minute increments are allowed. |
| **to**  string | The time, from ‘00 00’ to ‘24 00’. Must be greater than the time specified in ‘from’. Defaults to ‘24 00’. Only 30 minute increments are allowed. |
| **splashAuthSettings**  string | Whether clients bound to your policy will bypass splash authorization or behave according to the network’s rules. Can be one of ‘network default’ or ‘bypass’. Only available if your network has a wireless configuration. |
| **vlanTagging**  dictionary | The VLAN tagging settings for your group policy. Only available if your network has a wireless configuration. |
| **settings**  string | How VLAN tagging is applied. Can be ‘network default’, ‘ignore’ or ‘custom’. |
| **vlanId**  string | The ID of the vlan you want to tag. This only applies if ‘settings’ is set to ‘custom’. |

## [Notes](networks_group_policies_module.md#id4)

> **Note:**
>
> - SDK Method used are networks.Networks.create_network_group_policy, networks.Networks.delete_network_group_policy, networks.Networks.update_network_group_policy,
> - Paths used are post /networks/{networkId}/groupPolicies, delete /networks/{networkId}/groupPolicies/{groupPolicyId}, put /networks/{networkId}/groupPolicies/{groupPolicyId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_group_policies_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for networks createNetworkGroupPolicy](https://developer.cisco.com/meraki/api-v1/#!create-network-group-policy)
> :   Complete reference of the createNetworkGroupPolicy API.
>
> [Cisco Meraki documentation for networks deleteNetworkGroupPolicy](https://developer.cisco.com/meraki/api-v1/#!delete-network-group-policy)
> :   Complete reference of the deleteNetworkGroupPolicy API.
>
> [Cisco Meraki documentation for networks updateNetworkGroupPolicy](https://developer.cisco.com/meraki/api-v1/#!update-network-group-policy)
> :   Complete reference of the updateNetworkGroupPolicy API.

## [Examples](networks_group_policies_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.networks_group_policies:
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
    bandwidth:
      bandwidthLimits:
        limitDown: 1000000
        limitUp: 1000000
      settings: custom
    bonjourForwarding:
      rules:
      - description: A simple bonjour rule
        services:
        - All Services
        vlanId: '1'
      settings: custom
    contentFiltering:
      allowedUrlPatterns:
        patterns: []
        settings: network default
      blockedUrlCategories:
        categories:
        - meraki:contentFiltering/category/1
        - meraki:contentFiltering/category/7
        settings: override
      blockedUrlPatterns:
        patterns:
        - http://www.example.com
        - http://www.betting.com
        settings: append
    firewallAndTrafficShaping:
      l3FirewallRules:
      - comment: Allow TCP traffic to subnet with HTTP servers.
        destCidr: 192.168.1.0/24
        destPort: '443'
        policy: allow
        protocol: tcp
      l7FirewallRules:
      - policy: deny
        type: host
        value: google.com
      - policy: deny
        type: port
        value: '23'
      - policy: deny
        type: ipRange
        value: 10.11.12.00/24
      - policy: deny
        type: ipRange
        value: 10.11.12.00/24:5555
      settings: custom
      trafficShapingRules:
      - definitions:
        - type: host
          value: google.com
        - type: port
          value: '9090'
        - type: ipRange
          value: 192.1.0.0
        - type: ipRange
          value: 192.1.0.0/16
        - type: ipRange
          value: 10.1.0.0/16:80
        - type: localNet
          value: 192.168.0.0/16
        dscpTagValue: 0
        pcpTagValue: 0
        perClientBandwidthLimits:
          bandwidthLimits:
            limitDown: 1000000
            limitUp: 1000000
          settings: custom
    name: No video streaming
    networkId: string
    scheduling:
      enabled: true
      friday:
        active: true
        from: '9:00'
        to: '17:00'
      monday:
        active: true
        from: '9:00'
        to: '17:00'
      saturday:
        active: false
        from: 0:00
        to: '24:00'
      sunday:
        active: false
        from: 0:00
        to: '24:00'
      thursday:
        active: true
        from: '9:00'
        to: '17:00'
      tuesday:
        active: true
        from: '9:00'
        to: '17:00'
      wednesday:
        active: true
        from: '9:00'
        to: '17:00'
    splashAuthSettings: bypass
    vlanTagging:
      settings: custom
      vlanId: '1'

- name: Update by id
  cisco.meraki.networks_group_policies:
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
    bandwidth:
      bandwidthLimits:
        limitDown: 1000000
        limitUp: 1000000
      settings: custom
    bonjourForwarding:
      rules:
      - description: A simple bonjour rule
        services:
        - All Services
        vlanId: '1'
      settings: custom
    contentFiltering:
      allowedUrlPatterns:
        patterns: []
        settings: network default
      blockedUrlCategories:
        categories:
        - meraki:contentFiltering/category/1
        - meraki:contentFiltering/category/7
        settings: override
      blockedUrlPatterns:
        patterns:
        - http://www.example.com
        - http://www.betting.com
        settings: append
    firewallAndTrafficShaping:
      l3FirewallRules:
      - comment: Allow TCP traffic to subnet with HTTP servers.
        destCidr: 192.168.1.0/24
        destPort: '443'
        policy: allow
        protocol: tcp
      l7FirewallRules:
      - policy: deny
        type: host
        value: google.com
      - policy: deny
        type: port
        value: '23'
      - policy: deny
        type: ipRange
        value: 10.11.12.00/24
      - policy: deny
        type: ipRange
        value: 10.11.12.00/24:5555
      settings: custom
      trafficShapingRules:
      - definitions:
        - type: host
          value: google.com
        - type: port
          value: '9090'
        - type: ipRange
          value: 192.1.0.0
        - type: ipRange
          value: 192.1.0.0/16
        - type: ipRange
          value: 10.1.0.0/16:80
        - type: localNet
          value: 192.168.0.0/16
        dscpTagValue: 0
        pcpTagValue: 0
        perClientBandwidthLimits:
          bandwidthLimits:
            limitDown: 1000000
            limitUp: 1000000
          settings: custom
    groupPolicyId: string
    name: No video streaming
    networkId: string
    scheduling:
      enabled: true
      friday:
        active: true
        from: '9:00'
        to: '17:00'
      monday:
        active: true
        from: '9:00'
        to: '17:00'
      saturday:
        active: false
        from: 0:00
        to: '24:00'
      sunday:
        active: false
        from: 0:00
        to: '24:00'
      thursday:
        active: true
        from: '9:00'
        to: '17:00'
      tuesday:
        active: true
        from: '9:00'
        to: '17:00'
      wednesday:
        active: true
        from: '9:00'
        to: '17:00'
    splashAuthSettings: bypass
    vlanTagging:
      settings: custom
      vlanId: '1'

- name: Delete by id
  cisco.meraki.networks_group_policies:
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
    groupPolicyId: string
    networkId: string
```

## [Return Values](networks_group_policies_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
