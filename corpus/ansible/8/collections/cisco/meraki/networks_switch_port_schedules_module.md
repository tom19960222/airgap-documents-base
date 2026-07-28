---
collection: ansible
version: "8"
title: "cisco.meraki.networks_switch_port_schedules module – Resource module for networks _switch _portschedules"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/networks_switch_port_schedules_module.html
fetched_at: 2026-07-28T01:35:01+00:00
---
# cisco.meraki.networks_switch_port_schedules module – Resource module for networks _switch _portschedules

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
> see [Requirements](networks_switch_port_schedules_module.md#ansible-collections-cisco-meraki-networks-switch-port-schedules-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.networks_switch_port_schedules`.

New in cisco.meraki 2.16.0

- [Synopsis](networks_switch_port_schedules_module.md#synopsis)
- [Requirements](networks_switch_port_schedules_module.md#requirements)
- [Parameters](networks_switch_port_schedules_module.md#parameters)
- [Notes](networks_switch_port_schedules_module.md#notes)
- [See Also](networks_switch_port_schedules_module.md#see-also)
- [Examples](networks_switch_port_schedules_module.md#examples)
- [Return Values](networks_switch_port_schedules_module.md#return-values)

## [Synopsis](networks_switch_port_schedules_module.md#id1)

- Manage operations create, update and delete of the resource networks _switch _portschedules.
- Add a switch port schedule.
- Delete a switch port schedule.
- Update a switch port schedule.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](networks_switch_port_schedules_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](networks_switch_port_schedules_module.md#id3)

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
| **name**  string | The name for your port schedule. Required. |
| **networkId**  string | NetworkId path parameter. Network ID. |
| **portSchedule**  dictionary | The schedule for switch port scheduling. Schedules are applied to days of the week. When it’s empty, default schedule with all days of a week are configured. Any unspecified day in the schedule is added as a default schedule configuration of the day. |
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
| **portScheduleId**  string | PortScheduleId path parameter. Port schedule ID. |

## [Notes](networks_switch_port_schedules_module.md#id4)

> **Note:**
>
> - SDK Method used are switch.Switch.create_network_switch_port_schedule, switch.Switch.delete_network_switch_port_schedule, switch.Switch.update_network_switch_port_schedule,
> - Paths used are post /networks/{networkId}/switch/portSchedules, delete /networks/{networkId}/switch/portSchedules/{portScheduleId}, put /networks/{networkId}/switch/portSchedules/{portScheduleId},
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](networks_switch_port_schedules_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for switch createNetworkSwitchPortSchedule](https://developer.cisco.com/meraki/api-v1/#!create-network-switch-port-schedule)
> :   Complete reference of the createNetworkSwitchPortSchedule API.
>
> [Cisco Meraki documentation for switch deleteNetworkSwitchPortSchedule](https://developer.cisco.com/meraki/api-v1/#!delete-network-switch-port-schedule)
> :   Complete reference of the deleteNetworkSwitchPortSchedule API.
>
> [Cisco Meraki documentation for switch updateNetworkSwitchPortSchedule](https://developer.cisco.com/meraki/api-v1/#!update-network-switch-port-schedule)
> :   Complete reference of the updateNetworkSwitchPortSchedule API.

## [Examples](networks_switch_port_schedules_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.networks_switch_port_schedules:
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
    name: Weekdays schedule
    networkId: string
    portSchedule:
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

- name: Update by id
  cisco.meraki.networks_switch_port_schedules:
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
    name: Weekdays schedule
    networkId: string
    portSchedule:
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
    portScheduleId: string

- name: Delete by id
  cisco.meraki.networks_switch_port_schedules:
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
    portScheduleId: string
```

## [Return Values](networks_switch_port_schedules_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  dictionary | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `{}` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
