---
collection: ansible
version: "8"
title: "cisco.meraki.networks_firmware_upgrades_staged_events_rollbacks module – Resource module for networks _firmwareupgrades _staged _events _rollbacks"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_firmware_upgrades_staged_events_rollbacks_module.html
fetched_at: 2026-07-28T01:34:00+00:00
---
# cisco.meraki.networks_firmware_upgrades_staged_events_rollbacks module – Resource module for networks _firmwareupgrades _staged _events _rollbacks

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
> see [Requirements](networks_firmware_upgrades_staged_events_rollbacks_module.md#ansible-collections-cisco-meraki-networks-firmware-upgrades-staged-events-rollbacks-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_firmware_upgrades_staged_events_rollbacks`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_firmware_upgrades_staged_events_rollbacks_module.md#synopsis)
- [Requirements](networks_firmware_upgrades_staged_events_rollbacks_module.md#requirements)
- [Parameters](networks_firmware_upgrades_staged_events_rollbacks_module.md#parameters)
- [Notes](networks_firmware_upgrades_staged_events_rollbacks_module.md#notes)
- [See Also](networks_firmware_upgrades_staged_events_rollbacks_module.md#see-also)
- [Examples](networks_firmware_upgrades_staged_events_rollbacks_module.md#examples)
- [Return Values](networks_firmware_upgrades_staged_events_rollbacks_module.md#return-values)

## [Synopsis](networks_firmware_upgrades_staged_events_rollbacks_module.md#id1)

- Manage operation create of the resource networks _firmwareupgrades _staged _events _rollbacks.
- Rollback a Staged Upgrade Event for a network.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_firmware_upgrades_staged_events_rollbacks_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_firmware_upgrades_staged_events_rollbacks_module.md#id3)

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
| **networkId**  string | NetworkId path parameter. Network ID. |
| **reasons**  list / elements=dictionary | The reason for rolling back the staged upgrade. |
| **category**  string | Reason for the rollback. |
| **comment**  string | Additional comment about the rollback. |
| **stages**  list / elements=dictionary | All completed or in-progress stages in the network with their new start times. All pending stages will be canceled. |
| **group**  dictionary | The Staged Upgrade Group containing the name and ID. |
| **id**  string | ID of the Staged Upgrade Group. |
| **milestones**  dictionary | The Staged Upgrade Milestones for the specific stage. |
| **scheduledFor**  string | The start time of the staged upgrade stage. (In ISO-8601 format, in the time zone of the network.). |

## [Notes](networks_firmware_upgrades_staged_events_rollbacks_module.md#id4)

> **Note:**
>
> - SDK Method used are networks.Networks.rollbacks_network_firmware_upgrades_staged_events,
> - Paths used are post /networks/{networkId}/firmwareUpgrades/staged/events/rollbacks,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_firmware_upgrades_staged_events_rollbacks_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for networks rollbacksNetworkFirmwareUpgradesStagedEvents](https://developer.cisco.com/meraki/api-v1/#!rollbacks-network-firmware-upgrades-staged-events)
> :   Complete reference of the rollbacksNetworkFirmwareUpgradesStagedEvents API.

## [Examples](networks_firmware_upgrades_staged_events_rollbacks_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.networks_firmware_upgrades_staged_events_rollbacks:
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
    networkId: string
    reasons:
    - category: performance
      comment: Network was slower with the upgrade
    stages:
    - group:
        id: '1234'
      milestones:
        scheduledFor: '2018-02-11T00:00:00Z'
```

## [Return Values](networks_firmware_upgrades_staged_events_rollbacks_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{"products": {"switch": {"nextUpgrade": {"toVersion": {"id": "string", "shortName": "string"}}}}, "reasons": [{"category": "string", "comment": "string"}], "stages": [{"group": {"description": "string", "id": "string", "name": "string"}, "milestones": {"canceledAt": "string", "completedAt": "string", "scheduledFor": "string", "startedAt": "string"}, "status": "string"}]}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
