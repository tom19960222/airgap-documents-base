---
collection: ansible
version: "8"
title: "cisco.meraki.organizations_inventory_onboarding_cloud_monitoring_imports module – Resource module for organizations _inventory _onboarding _cloudmonitoring _imports"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/organizations_inventory_onboarding_cloud_monitoring_imports_module.html
fetched_at: 2026-07-28T01:36:57+00:00
---
# cisco.meraki.organizations_inventory_onboarding_cloud_monitoring_imports module – Resource module for organizations _inventory _onboarding _cloudmonitoring _imports

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
> see [Requirements](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#ansible-collections-cisco-meraki-organizations-inventory-onboarding-cloud-monitoring-imports-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.organizations_inventory_onboarding_cloud_monitoring_imports`.

New in cisco.meraki 2.16.0

- [Synopsis](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#synopsis)
- [Requirements](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#requirements)
- [Parameters](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#parameters)
- [Notes](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#notes)
- [See Also](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#see-also)
- [Examples](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#examples)
- [Return Values](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#return-values)

## [Synopsis](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#id1)

- Manage operation create of the resource organizations _inventory _onboarding _cloudmonitoring _imports.
- Commits the import operation to complete the onboarding of a device into Dashboard for monitoring.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **devices**  list / elements=dictionary | A set of device imports to commit. |
| **deviceId**  string | Import ID from the Import operation. |
| **networkId**  string | Network Id. |
| **udi**  string | Device UDI certificate. |
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

## [Notes](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#id4)

> **Note:**
>
> - SDK Method used are organizations.Organizations.create_organization_inventory_onboarding_cloud_monitoring_import,
> - Paths used are post /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/imports,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for organizations createOrganizationInventoryOnboardingCloudMonitoringImport](https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-import)
> :   Complete reference of the createOrganizationInventoryOnboardingCloudMonitoringImport API.

## [Examples](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.organizations_inventory_onboarding_cloud_monitoring_imports:
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
    devices:
    - deviceId: 161b2602-a713-4aac-b1eb-d9b55205353d
      networkId: '1338481'
      udi: PID:C9200L-24P-4G SN:JAE25220R2K
    organizationId: string
```

## [Return Values](organizations_inventory_onboarding_cloud_monitoring_imports_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  list / elements=string | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `["[\n  {\n    \"status\": \"string\"", "\n    \"importId\": \"string\"", "\n    \"message\": \"string\"\n  }\n]\n"]` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
