---
collection: ansible
version: "8"
title: "cisco.meraki.organizations_switch_ports_by_switch_info module – Information module for organizations _switch _ports _byswitch"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/organizations_switch_ports_by_switch_info_module.html
fetched_at: 2026-07-28T01:37:28+00:00
---
# cisco.meraki.organizations_switch_ports_by_switch_info module – Information module for organizations _switch _ports _byswitch

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
> see [Requirements](organizations_switch_ports_by_switch_info_module.md#ansible-collections-cisco-meraki-organizations-switch-ports-by-switch-info-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.organizations_switch_ports_by_switch_info`.

New in cisco.meraki 2.16.0

- [Synopsis](organizations_switch_ports_by_switch_info_module.md#synopsis)
- [Requirements](organizations_switch_ports_by_switch_info_module.md#requirements)
- [Parameters](organizations_switch_ports_by_switch_info_module.md#parameters)
- [Notes](organizations_switch_ports_by_switch_info_module.md#notes)
- [See Also](organizations_switch_ports_by_switch_info_module.md#see-also)
- [Examples](organizations_switch_ports_by_switch_info_module.md#examples)
- [Return Values](organizations_switch_ports_by_switch_info_module.md#return-values)

## [Synopsis](organizations_switch_ports_by_switch_info_module.md#id1)

- Get all organizations _switch _ports _byswitch.
- List the switchports in an organization by switch.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](organizations_switch_ports_by_switch_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](organizations_switch_ports_by_switch_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **configurationUpdatedAfter**  string | ConfigurationUpdatedAfter query parameter. Optional parameter to filter results by switches where the configuration has been updated after the given timestamp. |
| **direction**  string | direction (string), direction to paginate, either “next” (default) or “prev” page  **Default:** `"https://api.meraki.com/api/v1"` |
| **endingBefore**  string | EndingBefore query parameter. A token used by the server to indicate the end of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| **headers**  dictionary | Additional headers. |
| **mac**  string | Mac query parameter. Optional parameter to filter switchports belonging to switches by MAC address. All returned switches will have a MAC address that contains the search term or is an exact match. |
| **macs**  list / elements=string | Macs query parameter. Optional parameter to filter switchports by one or more MAC addresses belonging to devices. All switchports returned belong to MAC addresses of switches that are an exact match. |
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
| **name**  string | Name query parameter. Optional parameter to filter switchports belonging to switches by name. All returned switches will have a name that contains the search term or is an exact match. |
| **networkIds**  list / elements=string | NetworkIds query parameter. Optional parameter to filter switchports by network. |
| **organizationId**  string | OrganizationId path parameter. Organization ID. |
| **perPage**  integer | PerPage query parameter. The number of entries per page returned. Acceptable range is 3 - 50. Default is 50. |
| **portProfileIds**  list / elements=string | PortProfileIds query parameter. Optional parameter to filter switchports belonging to the specified port profiles. |
| **serial**  string | Serial query parameter. Optional parameter to filter switchports belonging to switches by serial number. All returned switches will have a serial number that contains the search term or is an exact match. |
| **serials**  list / elements=string | Serials query parameter. Optional parameter to filter switchports belonging to switches with one or more serial numbers. All switchports returned belong to serial numbers of switches that are an exact match. |
| **startingAfter**  string | StartingAfter query parameter. A token used by the server to indicate the start of the page. Often this is a timestamp or an ID but it is not limited to those. This parameter should not be defined by client applications. The link for the first, last, prev, or next page in the HTTP Link header should define it. |
| **total_pages**  string / required | total_pages(int), use with perPage to get total results up to total_pages\*perPage; -1 for all pages |

## [Notes](organizations_switch_ports_by_switch_info_module.md#id4)

> **Note:**
>
> - SDK Method used are switch.Switch.get_organization_switch_ports_by_switch,
> - Paths used are get /organizations/{organizationId}/switch/ports/bySwitch,
> - Supports `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco meraki SDK
> - The parameters starting with meraki_ are used by the Cisco meraki Python SDK to establish the connection

## [See Also](organizations_switch_ports_by_switch_info_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for switch getOrganizationSwitchPortsBySwitch](https://developer.cisco.com/meraki/api-v1/#!get-organization-switch-ports-by-switch)
> :   Complete reference of the getOrganizationSwitchPortsBySwitch API.

## [Examples](organizations_switch_ports_by_switch_info_module.md#id6)

```yaml+jinja
- name: Get all organizations _switch _ports _byswitch
  cisco.meraki.organizations_switch_ports_by_switch_info:
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
    perPage: 0
    startingAfter: string
    endingBefore: string
    networkIds: []
    portProfileIds: []
    name: string
    mac: string
    macs: []
    serial: string
    serials: []
    configurationUpdatedAfter: string
    organizationId: string
    total_pages: -1
    direction: next
  register: result
```

## [Return Values](organizations_switch_ports_by_switch_info_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  list / elements=dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `"[\n  {\n    \"name\": \"string\",\n    \"serial\": \"string\",\n    \"mac\": \"string\",\n    \"network\": {\n      \"name\": \"string\",\n      \"id\": \"string\"\n    },\n    \"model\": \"string\",\n    \"ports\": [\n      {\n        \"portId\": \"string\",\n        \"name\": \"string\",\n        \"tags\": [\n          \"string\"\n        ],\n        \"enabled\": true,\n        \"poeEnabled\": true,\n        \"type\": \"string\",\n        \"vlan\": 0,\n        \"voiceVlan\": 0,\n        \"allowedVlans\": \"string\",\n        \"rstpEnabled\": true,\n        \"stpGuard\": \"string\",\n        \"linkNegotiation\": \"string\",\n        \"accessPolicyType\": \"string\",\n        \"stickyMacAllowList\": [\n          \"string\"\n        ],\n        \"stickyMacAllowListLimit\": 0\n      }\n    ]\n  }\n]\n"` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
