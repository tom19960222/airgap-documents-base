---
collection: ansible
version: "8"
title: "cisco.meraki.networks_webhooks_http_servers module – Resource module for networks _webhooks _httpservers"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_webhooks_http_servers_module.html
fetched_at: 2026-07-28T01:35:27+00:00
---
# cisco.meraki.networks_webhooks_http_servers module – Resource module for networks _webhooks _httpservers

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
> see [Requirements](networks_webhooks_http_servers_module.md#ansible-collections-cisco-meraki-networks-webhooks-http-servers-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_webhooks_http_servers`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_webhooks_http_servers_module.md#synopsis)
- [Requirements](networks_webhooks_http_servers_module.md#requirements)
- [Parameters](networks_webhooks_http_servers_module.md#parameters)
- [Notes](networks_webhooks_http_servers_module.md#notes)
- [See Also](networks_webhooks_http_servers_module.md#see-also)
- [Examples](networks_webhooks_http_servers_module.md#examples)
- [Return Values](networks_webhooks_http_servers_module.md#return-values)

## [Synopsis](networks_webhooks_http_servers_module.md#id1)

- Manage operations create, update and delete of the resource networks _webhooks _httpservers.
- Add an HTTP server to a network.
- Delete an HTTP server from a network.
- Update an HTTP server. To change a URL, create a new HTTP server.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_webhooks_http_servers_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_webhooks_http_servers_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **httpServerId**  string | HttpServerId path parameter. Http server ID. |
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
| **name**  string | A name for easy reference to the HTTP server. |
| **networkId**  string | NetworkId path parameter. Network ID. |
| **payloadTemplate**  dictionary | The payload template to use when posting data to the HTTP server. |
| **name**  string | The name of the payload template. |
| **payloadTemplateId**  string | The ID of the payload template. Defaults to ‘wpt_00001’ for the Meraki template. For Meraki-included templates for the Webex (included) template use ‘wpt_00002’; for the Slack (included) template use ‘wpt_00003’; for the Microsoft Teams (included) template use ‘wpt_00004’; for the ServiceNow (included) template use ‘wpt_00006’. |
| **sharedSecret**  string | A shared secret that will be included in POSTs sent to the HTTP server. This secret can be used to verify that the request was sent by Meraki. |
| **url**  string | The URL of the HTTP server. Once set, cannot be updated. |

## [Notes](networks_webhooks_http_servers_module.md#id4)

> **Note:**
>
> - SDK Method used are networks.Networks.create_network_webhooks_http_server, networks.Networks.delete_network_webhooks_http_server, networks.Networks.update_network_webhooks_http_server,
> - Paths used are post /networks/{networkId}/webhooks/httpServers, delete /networks/{networkId}/webhooks/httpServers/{httpServerId}, put /networks/{networkId}/webhooks/httpServers/{httpServerId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_webhooks_http_servers_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for networks createNetworkWebhooksHttpServer](https://developer.cisco.com/meraki/api-v1/#!create-network-webhooks-http-server)
> :   Complete reference of the createNetworkWebhooksHttpServer API.
>
> [Cisco Meraki documentation for networks deleteNetworkWebhooksHttpServer](https://developer.cisco.com/meraki/api-v1/#!delete-network-webhooks-http-server)
> :   Complete reference of the deleteNetworkWebhooksHttpServer API.
>
> [Cisco Meraki documentation for networks updateNetworkWebhooksHttpServer](https://developer.cisco.com/meraki/api-v1/#!update-network-webhooks-http-server)
> :   Complete reference of the updateNetworkWebhooksHttpServer API.

## [Examples](networks_webhooks_http_servers_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.networks_webhooks_http_servers:
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
    name: Example Webhook Server
    networkId: string
    payloadTemplate:
      name: Meraki (included)
      payloadTemplateId: wpt_00001
    sharedSecret: shhh
    url: https://example.com

- name: Update by id
  cisco.meraki.networks_webhooks_http_servers:
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
    httpServerId: string
    name: Example Webhook Server
    networkId: string
    payloadTemplate:
      payloadTemplateId: wpt_00001
    sharedSecret: shhh

- name: Delete by id
  cisco.meraki.networks_webhooks_http_servers:
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
    httpServerId: string
    networkId: string
```

## [Return Values](networks_webhooks_http_servers_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{"id": "string", "name": "string", "networkId": "string", "payloadTemplate": {"name": "string", "payloadTemplateId": "string"}, "url": "string"}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
