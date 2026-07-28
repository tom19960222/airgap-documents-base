---
collection: ansible
version: "8"
title: "cisco.meraki.networks_firmware_upgrades_staged_groups module – Resource module for networks _firmwareupgrades _staged _groups"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_firmware_upgrades_staged_groups_module.html
fetched_at: 2026-07-28T01:34:01+00:00
---
# cisco.meraki.networks_firmware_upgrades_staged_groups module – Resource module for networks _firmwareupgrades _staged _groups

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
> see [Requirements](networks_firmware_upgrades_staged_groups_module.md#ansible-collections-cisco-meraki-networks-firmware-upgrades-staged-groups-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_firmware_upgrades_staged_groups`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_firmware_upgrades_staged_groups_module.md#synopsis)
- [Requirements](networks_firmware_upgrades_staged_groups_module.md#requirements)
- [Parameters](networks_firmware_upgrades_staged_groups_module.md#parameters)
- [Notes](networks_firmware_upgrades_staged_groups_module.md#notes)
- [See Also](networks_firmware_upgrades_staged_groups_module.md#see-also)
- [Examples](networks_firmware_upgrades_staged_groups_module.md#examples)
- [Return Values](networks_firmware_upgrades_staged_groups_module.md#return-values)

## [Synopsis](networks_firmware_upgrades_staged_groups_module.md#id1)

- Manage operations create, update and delete of the resource networks _firmwareupgrades _staged _groups.
- Create a Staged Upgrade Group for a network.
- Delete a Staged Upgrade Group.
- Update a Staged Upgrade Group for a network.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_firmware_upgrades_staged_groups_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_firmware_upgrades_staged_groups_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **assignedDevices**  dictionary | The devices and Switch Stacks assigned to the Group. |
| **devices**  list / elements=dictionary | Data Array of Devices containing the name and serial. |
| **name**  string | Name of the device. |
| **serial**  string | Serial of the device. |
| **switchStacks**  list / elements=dictionary | Data Array of Switch Stacks containing the name and id. |
| **id**  string | ID of the Switch Stack. |
| **name**  string | Name of the Switch Stack. |
| **description**  string | Description of the Staged Upgrade Group. Length must be 1 to 255 characters. |
| **groupId**  string | GroupId path parameter. Group ID. |
| **isDefault**  boolean | Boolean indicating the default Group. Any device that does not have a group explicitly assigned will upgrade with this group.  **Choices:**   - `false` - `true` |
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
| **name**  string | Name of the Staged Upgrade Group. Length must be 1 to 255 characters. |
| **networkId**  string | NetworkId path parameter. Network ID. |

## [Notes](networks_firmware_upgrades_staged_groups_module.md#id4)

> **Note:**
>
> - SDK Method used are networks.Networks.create_network_firmware_upgrades_staged_group, networks.Networks.delete_network_firmware_upgrades_staged_group, networks.Networks.update_network_firmware_upgrades_staged_group,
> - Paths used are post /networks/{networkId}/firmwareUpgrades/staged/groups, delete /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId}, put /networks/{networkId}/firmwareUpgrades/staged/groups/{groupId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_firmware_upgrades_staged_groups_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for networks createNetworkFirmwareUpgradesStagedGroup](https://developer.cisco.com/meraki/api-v1/#!create-network-firmware-upgrades-staged-group)
> :   Complete reference of the createNetworkFirmwareUpgradesStagedGroup API.
>
> [Cisco Meraki documentation for networks deleteNetworkFirmwareUpgradesStagedGroup](https://developer.cisco.com/meraki/api-v1/#!delete-network-firmware-upgrades-staged-group)
> :   Complete reference of the deleteNetworkFirmwareUpgradesStagedGroup API.
>
> [Cisco Meraki documentation for networks updateNetworkFirmwareUpgradesStagedGroup](https://developer.cisco.com/meraki/api-v1/#!update-network-firmware-upgrades-staged-group)
> :   Complete reference of the updateNetworkFirmwareUpgradesStagedGroup API.

## [Examples](networks_firmware_upgrades_staged_groups_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.networks_firmware_upgrades_staged_groups:
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
    assignedDevices:
      devices:
      - name: Device Name
        serial: Q234-ABCD-5678
      switchStacks:
      - id: '1234'
        name: Stack Name
    description: The description of the group
    isDefault: false
    name: My Staged Upgrade Group
    networkId: string

- name: Update by id
  cisco.meraki.networks_firmware_upgrades_staged_groups:
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
    assignedDevices:
      devices:
      - name: Device Name
        serial: Q234-ABCD-5678
      switchStacks:
      - id: '1234'
        name: Stack Name
    description: The description of the group
    groupId: string
    isDefault: false
    name: My Staged Upgrade Group
    networkId: string

- name: Delete by id
  cisco.meraki.networks_firmware_upgrades_staged_groups:
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
    groupId: string
    networkId: string
```

## [Return Values](networks_firmware_upgrades_staged_groups_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
