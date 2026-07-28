---
collection: ansible
version: "8"
title: "cisco.meraki.organizations_appliance_vpn_vpn_firewall_rules module – Resource module for organizations _appliance _vpn _vpnfirewallrules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/organizations_appliance_vpn_vpn_firewall_rules_module.html
fetched_at: 2026-07-28T01:36:24+00:00
---
# cisco.meraki.organizations_appliance_vpn_vpn_firewall_rules module – Resource module for organizations _appliance _vpn _vpnfirewallrules

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
> see [Requirements](organizations_appliance_vpn_vpn_firewall_rules_module.md#ansible-collections-cisco-meraki-organizations-appliance-vpn-vpn-firewall-rules-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.organizations_appliance_vpn_vpn_firewall_rules`.

New in cisco.meraki 2.16.0

- [Synopsis](organizations_appliance_vpn_vpn_firewall_rules_module.md#synopsis)
- [Requirements](organizations_appliance_vpn_vpn_firewall_rules_module.md#requirements)
- [Parameters](organizations_appliance_vpn_vpn_firewall_rules_module.md#parameters)
- [Notes](organizations_appliance_vpn_vpn_firewall_rules_module.md#notes)
- [See Also](organizations_appliance_vpn_vpn_firewall_rules_module.md#see-also)
- [Examples](organizations_appliance_vpn_vpn_firewall_rules_module.md#examples)
- [Return Values](organizations_appliance_vpn_vpn_firewall_rules_module.md#return-values)

## [Synopsis](organizations_appliance_vpn_vpn_firewall_rules_module.md#id1)

- Manage operation update of the resource organizations _appliance _vpn _vpnfirewallrules.
- Update the firewall rules of an organization’s site-to-site VPN.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](organizations_appliance_vpn_vpn_firewall_rules_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](organizations_appliance_vpn_vpn_firewall_rules_module.md#id3)

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
| **rules**  list / elements=dictionary | An ordered array of the firewall rules (not including the default rule). |
| **comment**  string | Description of the rule (optional). |
| **destCidr**  string | Comma-separated list of destination IP address(es) (in IP or CIDR notation) or ‘any’ (FQDN not supported). |
| **destPort**  string | Comma-separated list of destination port(s) (integer in the range 1-65535), or ‘any’. |
| **policy**  string | ‘allow’ or ‘deny’ traffic specified by this rule. |
| **protocol**  string | The type of protocol (must be ‘tcp’, ‘udp’, ‘icmp’, ‘icmp6’ or ‘any’). |
| **srcCidr**  string | Comma-separated list of source IP address(es) (in IP or CIDR notation), or ‘any’ (FQDN not supported). |
| **srcPort**  string | Comma-separated list of source port(s) (integer in the range 1-65535), or ‘any’. |
| **syslogEnabled**  boolean | Log this rule to syslog (true or false, boolean value) - only applicable if a syslog has been configured (optional).  **Choices:**   - `false` - `true` |
| **syslogDefaultRule**  boolean | Log the special default rule (boolean value - enable only if you’ve configured a syslog server) (optional).  **Choices:**   - `false` - `true` |

## [Notes](organizations_appliance_vpn_vpn_firewall_rules_module.md#id4)

> **Note:**
>
> - SDK Method used are appliance.Appliance.update_organization_appliance_vpn_vpn_firewall_rules,
> - Paths used are put /organizations/{organizationId}/appliance/vpn/vpnFirewallRules,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](organizations_appliance_vpn_vpn_firewall_rules_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for appliance updateOrganizationApplianceVpnVpnFirewallRules](https://developer.cisco.com/meraki/api-v1/#!update-organization-appliance-vpn-vpn-firewall-rules)
> :   Complete reference of the updateOrganizationApplianceVpnVpnFirewallRules API.

## [Examples](organizations_appliance_vpn_vpn_firewall_rules_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.meraki.organizations_appliance_vpn_vpn_firewall_rules:
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
    rules:
    - comment: Allow TCP traffic to subnet with HTTP servers.
      destCidr: 192.168.1.0/24
      destPort: '443'
      policy: allow
      protocol: tcp
      srcCidr: Any
      srcPort: Any
      syslogEnabled: false
    syslogDefaultRule: false
```

## [Return Values](organizations_appliance_vpn_vpn_firewall_rules_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{"rules": [{"comment": "string", "destCidr": "string", "destPort": "string", "policy": "string", "protocol": "string", "srcCidr": "string", "srcPort": "string", "syslogEnabled": true}]}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
