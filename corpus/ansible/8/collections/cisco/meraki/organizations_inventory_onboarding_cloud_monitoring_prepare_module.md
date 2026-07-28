---
collection: ansible
version: "8"
title: "cisco.meraki.organizations_inventory_onboarding_cloud_monitoring_prepare module – Resource module for organizations _inventory _onboarding _cloudmonitoring _prepare"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/meraki/organizations_inventory_onboarding_cloud_monitoring_prepare_module.html
fetched_at: 2026-07-28T01:36:59+00:00
---
# cisco.meraki.organizations_inventory_onboarding_cloud_monitoring_prepare module – Resource module for organizations _inventory _onboarding _cloudmonitoring _prepare

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
> see [Requirements](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#ansible-collections-cisco-meraki-organizations-inventory-onboarding-cloud-monitoring-prepare-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.meraki.organizations_inventory_onboarding_cloud_monitoring_prepare`.

New in cisco.meraki 2.16.0

- [Synopsis](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#synopsis)
- [Requirements](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#requirements)
- [Parameters](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#parameters)
- [Notes](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#notes)
- [See Also](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#see-also)
- [Examples](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#examples)
- [Return Values](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#return-values)

## [Synopsis](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#id1)

- Manage operation create of the resource organizations _inventory _onboarding _cloudmonitoring _prepare.
- Initiates or updates an import session. An import ID will be generated and used when you are ready to commit the import.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Requirements](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#id2)

The below requirements are needed on the host that executes this module.

- meraki >= 2.4.9
- python >= 3.5

## [Parameters](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **devices**  list / elements=dictionary | A set of devices to import (or update). |
| **sudi**  string | Device SUDI certificate. |
| **tunnel**  dictionary | TLS Related Parameters. |
| **certificateName**  string | Name of the configured TLS certificate. |
| **localInterface**  integer | Number of the vlan expected to be used to connect to the cloud. |
| **loopbackNumber**  integer | Number of the configured Loopback Interface used for TLS overlay. |
| **name**  string | Name of the configured TLS tunnel. |
| **user**  dictionary | User parameters. |
| **username**  string | The name of the device user for Meraki monitoring. |
| **vty**  dictionary | VTY Related Parameters. |
| **accessList**  dictionary | AccessList details. |
| **vtyIn**  dictionary | VTY in ACL. |
| **name**  string | Name. |
| **vtyOut**  dictionary | VTY out ACL. |
| **name**  string | Name. |
| **authentication**  dictionary | VTY AAA authentication. |
| **group**  dictionary | Group Details. |
| **name**  string | Group Name. |
| **authorization**  dictionary | VTY AAA authorization. |
| **group**  dictionary | Group Details. |
| **name**  string | Group Name. |
| **endLineNumber**  integer | Ending line VTY number. |
| **rotaryNumber**  integer | SSH rotary number. |
| **startLineNumber**  integer | Starting line VTY number. |
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

## [Notes](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#id4)

> **Note:**
>
> - SDK Method used are organizations.Organizations.create_organization_inventory_onboarding_cloud_monitoring_prepare,
> - Paths used are post /organizations/{organizationId}/inventory/onboarding/cloudMonitoring/prepare,
> - Does not support `check_mode`
> - The plugin runs on the control node and does not use any ansible connection plugins, but instead the embedded connection manager from Cisco DNAC SDK
> - The parameters starting with dnac_ are used by the Cisco DNAC Python SDK to establish the connection

## [See Also](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#id5)

> **See also:**
>
> [Cisco Meraki documentation for organizations createOrganizationInventoryOnboardingCloudMonitoringPrepare](https://developer.cisco.com/meraki/api-v1/#!create-organization-inventory-onboarding-cloud-monitoring-prepare)
> :   Complete reference of the createOrganizationInventoryOnboardingCloudMonitoringPrepare API.

## [Examples](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#id6)

```yaml+jinja
- name: Create
  cisco.meraki.organizations_inventory_onboarding_cloud_monitoring_prepare:
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
    devices:
    - sudi: "-----BEGIN CERTIFICATE-----\n        MIIDyTCCArGgAwIBAgIKBBNXOVCGU1YztjANBgkqhkiG9w0BAQsFADAnMQ4wDAYD\n\
        \        VQQKEwVDaXNjbzEVMBMGA1UEAxMMQUNUMiBTVURJIENBMB4XDTIxMDUzMTEzNTUx\n  \
        \      NVoXDTI5MDUxNDIwMjU0MVowbTEpMCcGA1UEBRMgUElEOkM5MjAwTC0yNFAtNEcg\n    \
        \    U046SkFFMjUyMjBSMksxDjAMBgNVBAoTBUNpc2NvMRgwFgYDVQQLEw9BQ1QtMiBM\n      \
        \  aXRlIFNVREkxFjAUBgNVBAMTDUM5MjAwTC0yNFAtNEcwggEiMA0GCSqGSIb3DQEB\n        AQUAA4IBDwAwggEKAoIBAQDaUPxW76g...
        \        TR1TuP36bHh13X3vtGiDsCD88Ci2TZIqd/EDkkc7v9ipUUYVVH+YDrPt2Aukb1PH\n  \
        \      D6K0R+KhgEzRo5x54TlU6oWvjUpwNZUwwdhMWIQaUVkMyZBYNy0jGPLO8jwZhyBg\n    \
        \    1Fneybr9pwedGbLrAaz+gdEikB8B4a/fvPjVfL5Ngb4QRjFqWuE+X3nLc0kHedep\n      \
        \  6nfgpUNXMlStVm5nIXKP6OjmzfCHPYh9L2Ehs1TrSk1ser9Ofx0ZMVL/jBZR2EIj\n        OZ8tH6KlX2/B2pbSPIO6kD5c4UA8Cf1...
        \        VR0PAQH/BAQDAgXgMAwGA1UdEwEB/wQCMAAwHwYDVR0jBBgwFoAUSNjx8cJw1Vu7\n  \
        \      fHMJk6+4uDAD+H8wTQYDVR0RBEYwRKBCBgkrBgEEAQkVAgOgNRMzQ2hpcElEPVVV\n    \
        \    VUNNaElGcUVFMklFUUVBQWNBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUE9MB0GA1Ud\n      \
        \  DgQWBBRdhMkFD/z5hokaQeLbaRsp4hkvbzANBgkqhkiG9w0BAQsFAAOCAQEAMtuh\n        YpBz4xEZ7YdJsLpw67Q0TTJGnTBRpzA...
        \        OwmH/iZ+tDfYQ3W3ElWTW93871DkuW4WQIfbnoHg/F7bF0DKYVkD3rpZjyz3NhzH\n  \
        \      d7cjTdJXQ85bTAOXDuxKH3qewrXxxOGXgh3I6NUq0UwMTWh84lND7Jl+ZAQkYNS2\n    \
        \    iHanTZFQBk3ML0NUb7fKDYGRTZRqwQ/upIO4S6LV1cxH/6V0qbMy3sCSHZoMLrW3\n      \
        \  0m3M6yKpe5+VZzHZwmWdUf3Ot+zKjhveK5/YNsMIASdvtvymxUizq2Hr1hvR/kPc\n        p1vuyWxipU8JfzOh/A==\n\
        \        -----END CERTIFICATE-----\n        "
      tunnel:
        certificateName: DeviceSUDI
        localInterface: 1
        loopbackNumber: 1000
        name: MERAKI
      user:
        username: Meraki
      vty:
        accessList:
          vtyIn:
            name: MERAKI_IN
          vtyOut:
            name: MERAKI_OUT
        authentication:
          group:
            name: ''
        authorization:
          group:
            name: MERAKI
        endLineNumber: 17
        rotaryNumber: 50
        startLineNumber: 16
    organizationId: string
```

## [Return Values](organizations_inventory_onboarding_cloud_monitoring_prepare_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meraki_response**  list / elements=string | A dictionary or list with the response returned by the Cisco Meraki Python SDK  **Returned:** always  **Sample:** `["[\n  {\n    \"message\": \"string\"", "\n    \"udi\": \"string\"", "\n    \"deviceId\": \"string\"", "\n    \"status\": \"string\"", "\n    \"configParams\": {\n      \"tunnel\": {\n        \"mode\": \"string\"", "\n        \"port\": \"string\"", "\n        \"host\": \"string\"", "\n        \"name\": \"string\"", "\n        \"rootCertificate\": {\n          \"content\": \"string\"", "\n          \"name\": \"string\"\n        }\n      }", "\n      \"cloudStaticIp\": \"string\"", "\n      \"user\": {\n        \"publicKey\": \"string\"", "\n        \"username\": \"string\"", "\n        \"secret\": {\n          \"hash\": \"string\"\n        }\n      }\n    }\n  }\n]\n"]` |

### Authors

- Francisco Munoz (@fmunoz)

### Collection links

- [Issue Tracker](https://github.com/meraki/dashboard-api-ansible/issues)
- [Repository (Sources)](https://github.com/meraki/dashboard-api-ansible)
