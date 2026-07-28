---
collection: ansible
version: "8"
title: "cisco.meraki.networks_clients_splash_authorization_status module – Resource module for networks _clients _splashauthorizationstatus"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_clients_splash_authorization_status_module.html
fetched_at: 2026-07-28T01:33:51+00:00
---
# cisco.meraki.networks_clients_splash_authorization_status module – Resource module for networks _clients _splashauthorizationstatus

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
> see [Requirements](networks_clients_splash_authorization_status_module.md#ansible-collections-cisco-meraki-networks-clients-splash-authorization-status-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_clients_splash_authorization_status`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_clients_splash_authorization_status_module.md#synopsis)
- [Requirements](networks_clients_splash_authorization_status_module.md#requirements)
- [Parameters](networks_clients_splash_authorization_status_module.md#parameters)
- [Notes](networks_clients_splash_authorization_status_module.md#notes)
- [See Also](networks_clients_splash_authorization_status_module.md#see-also)
- [Examples](networks_clients_splash_authorization_status_module.md#examples)
- [Return Values](networks_clients_splash_authorization_status_module.md#return-values)

## [Synopsis](networks_clients_splash_authorization_status_module.md#id1)

- Manage operation update of the resource networks _clients _splashauthorizationstatus.
- Update a client’s splash authorization. Clients can be identified by a client key or either the MAC or IP depending on whether the network uses Track-by-IP.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_clients_splash_authorization_status_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_clients_splash_authorization_status_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **clientId**  string | ClientId path parameter. Client ID. |
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
| **ssids**  dictionary | The target SSIDs. Each SSID must be enabled and must have Click-through splash enabled. For each SSID where isAuthorized is true, the expiration time will automatically be set according to the SSID’s splash frequency. Not all networks support configuring all SSIDs. |
| **0**  dictionary | Splash authorization for SSID 0. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **1**  dictionary | Splash authorization for SSID 1. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **10**  dictionary | Splash authorization for SSID 10. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **11**  dictionary | Splash authorization for SSID 11. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **12**  dictionary | Splash authorization for SSID 12. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **13**  dictionary | Splash authorization for SSID 13. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **14**  dictionary | Splash authorization for SSID 14. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **2**  dictionary | Splash authorization for SSID 2. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **3**  dictionary | Splash authorization for SSID 3. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **4**  dictionary | Splash authorization for SSID 4. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **5**  dictionary | Splash authorization for SSID 5. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **6**  dictionary | Splash authorization for SSID 6. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **7**  dictionary | Splash authorization for SSID 7. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **8**  dictionary | Splash authorization for SSID 8. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |
| **9**  dictionary | Splash authorization for SSID 9. |
| **isAuthorized**  boolean | New authorization status for the SSID (true, false).  **Choices:**   - `false` - `true` |

## [Notes](networks_clients_splash_authorization_status_module.md#id4)

> **Note:**
>
> - SDK Method used are networks.Networks.update_network_client_splash_authorization_status,
> - Paths used are put /networks/{networkId}/clients/{clientId}/splashAuthorizationStatus,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_clients_splash_authorization_status_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for networks updateNetworkClientSplashAuthorizationStatus](https://developer.cisco.com/meraki/api-v1/#!update-network-client-splash-authorization-status)
> :   Complete reference of the updateNetworkClientSplashAuthorizationStatus API.

## [Examples](networks_clients_splash_authorization_status_module.md#id6)

```yaml+jinja
- name: Update all
  cisco.meraki.networks_clients_splash_authorization_status:
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
    clientId: string
    networkId: string
    ssids:
      '0':
        isAuthorized: true
      '2':
        isAuthorized: false
```

## [Return Values](networks_clients_splash_authorization_status_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
